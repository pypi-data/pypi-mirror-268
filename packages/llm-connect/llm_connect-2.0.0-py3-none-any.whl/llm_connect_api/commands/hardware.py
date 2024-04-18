import torch
import click
from pathlib import Path
import subprocess
from colorama import init, Fore, Back, Style
import shutil
import os, sys

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
background_color = Back.BLACK
reset = Style.RESET_ALL

def get_folder_size(path):
    total_size = 0
    for dirpath, _ , filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def check_model_existence(repo_id, model_name):
    model_path = Path.home() / ".cache" / "huggingface" / "hub" / f"models--{repo_id.replace('/', '--')}--{model_name}"
    return model_path.exists()

def list_models_in_hardware():
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    models_found = False
    click.echo("\n    Available Models: ")
    for model_dir in cache_dir.iterdir():
        if model_dir.is_dir() and model_dir.name.startswith("models--"):
            parts = model_dir.name.split("--")
            if len(parts) == 3:
                repo_id = parts[1]
                model_id = parts[2]

                folder_size = get_folder_size(model_dir)
                if folder_size < 50 * 1024 * 1024:
                    shutil.rmtree(model_dir)
                else:
                    click.echo(f"       * {blue}{repo_id}/{model_id}{reset}")
                    models_found = True
    if not models_found:
        click.echo(f"       {red}!!! No models available.{reset}")


def check_nvidia_gpu():
    if torch.cuda.is_available():
        total_memory = torch.cuda.get_device_properties(0).total_memory
        available_memory = total_memory - torch.cuda.memory_allocated(0)
        total_memory_gb = total_memory / (1024 ** 3)
        available_memory_gb = available_memory / (1024 ** 3)
        return True, total_memory_gb, available_memory_gb
    else:
        return False, None, None

def get_model_size(repo_id, model_name):
    model_path = Path.home() / ".cache" / "huggingface" / "hub" / f"models--{repo_id.replace('/', '--')}--{model_name}"
    try:
        du_output = subprocess.check_output(['du', '-sb', model_path], universal_newlines=True)
        size_str = du_output.split()[0]
        size_in_bytes = int(size_str)
        size_in_gb = size_in_bytes / (1024 ** 3)
        return size_in_gb
    except subprocess.CalledProcessError:
        return 0

def show_hardware(model_name):
    click.echo(f"\n    Checking hardware and software compatibility...\n")
    try:
        repo_id, model_name = model_name.split('/')
    except ValueError:
        click.echo(f"\n    {red}[Invalid]{reset} Model format\n    Use format: {blue}repo_id/model_name{reset}\n")
        sys.exit()
    if not check_model_existence(repo_id, model_name):
        click.echo(f"    {red}[Invalid]{reset} model: {blue}{repo_id}/{model_name}{reset}")
        f"{list_models_in_hardware()}\n"
        return
    else:
        gpu_available, total_memory_gb, _ = check_nvidia_gpu()
        if gpu_available:
            model_size = get_model_size(repo_id, model_name)
            if model_size <= total_memory_gb:
                click.echo(f"    {green}[Valid]{reset} GPU Memory for {blue}{model_name}{reset}")
                click.echo(f"       * GPU memory: {total_memory_gb:.2f} GB")
                click.echo(f"       * Model size: {model_size:.2f} GB\n")
            else:
                click.echo(f"    {red}[Invalid]{reset} GPU Memory for {blue}{model_name}{reset}")
                click.echo(f"       * GPU memory: {total_memory_gb:.2f} GB")
                click.echo(f"       * Model size: {model_size:.2f} GB\n")
        else:
            click.echo(f"    {red}[Invalid]{reset} CUDA drivers\n    Check CUDA Drivers ${yellow}nvidia-smi{reset}\n\n    You can still execute commands locally using {yellow}CPU{reset}\n")
