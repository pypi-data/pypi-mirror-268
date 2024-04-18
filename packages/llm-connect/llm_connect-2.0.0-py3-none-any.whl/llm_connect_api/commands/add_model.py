import click
from transformers import AutoTokenizer, AutoModelForCausalLM
from pathlib import Path
from colorama import init, Fore, Back, Style
import shutil
import os
from huggingface_hub import login

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

def download_model(repo_id, model_name):
    click.echo(f"\n    Downloading {blue}{repo_id}/{model_name}{reset} from {blue}HuggingFace{reset}...")
    AutoModelForCausalLM.from_pretrained(f"{repo_id}/{model_name}",trust_remote_code=True)
    AutoTokenizer.from_pretrained(f"{repo_id}/{model_name}")
    click.echo(f"\n    {blue}{repo_id}/{model_name}{reset} downloaded successfully!\n")

def list_models_in_add_model():
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    models_found = False
    click.echo("\n    Available Models: ")
    for model_dir in cache_dir.iterdir():
        if model_dir.is_dir() and model_dir.name.startswith("models--"):
            parts = model_dir.name.split("--")
            if len(parts) == 3:
                repo_id = parts[1]
                model_id = parts[2]

                # Check the size of the folder
                folder_size = get_folder_size(model_dir)
                if folder_size < 50 * 1024 * 1024:  # 10 MB in bytes
                    shutil.rmtree(model_dir)
                else:
                    click.echo(f"       * {blue}{repo_id}/{model_id}{reset}")
                    models_found = True

    if not models_found:
        click.echo(f"       {red}!!! No models available.{reset}")


cache_dir1 = Path.home() / ".cache" / "huggingface" / "hub"
models_found1 = False
for model_dir1 in cache_dir1.iterdir():
    if model_dir1.is_dir() and model_dir1.name.startswith("models--"):
        parts1 = model_dir1.name.split("--")
        if len(parts1) == 3:
            repo_id1 = parts1[1]
            model_id1 = parts1[2]

            folder_size1 = get_folder_size(model_dir1)
            if folder_size1 < 50 * 1024 * 1024:
                shutil.rmtree(model_dir1)
            else:
                models_found1 = True


def add_model(model_identifier):
    try:
        token = input(f"\n    {blue}Enter HuggingFace access token to read{reset}:")
        login(token)
    except ValueError:
        click.echo(f"\n    {red}[Invalid]{reset} Token\n    HuggingFace Login Failed!{reset}")
    try:
        repo_id, model_name = model_identifier.split('/')
        if check_model_existence(repo_id, model_name):
            click.echo(f"\n    Model {blue}{repo_id}/{model_name}{reset} is already available!")

            list_models_in_add_model()
        else:
            try:
                download_model(repo_id, model_name)
                list_models_in_add_model()
            except OSError:
                click.echo(f"\n    {blue}{model_identifier}{reset} is either {red}Non-Public/Gated{reset} or {red}Not a Valid Model Identifier{reset} listed on 'https://huggingface.co/models'\n")
            except ModuleNotFoundError:
                click.echo(f"\n    {blue}{model_identifier}{reset} is either {red}Non-Public/Gated{reset} or {red}Not a Valid Model Identifier{reset} listed on 'https://huggingface.co/models'\n")

    except ValueError:
        click.echo(f"\n    {red}[Invalid]{reset} Model format\n    Use format: {blue}repo_id/model_name{reset}\n")
    except FileNotFoundError:
        click.echo(f"\n    {red}[Invalid]{reset} Model format\n    Use format: {blue}repo_id/model_name{reset}\n")
