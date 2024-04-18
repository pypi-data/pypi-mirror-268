import click
from pathlib import Path
from colorama import init, Fore, Back, Style
import shutil
import os

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
background_color = Back.BLACK
reset = Style.RESET_ALL


def check_model_existence(repo_id, model_name):
    model_path = Path.home() / ".cache" / "huggingface" / "hub" / f"models--{repo_id.replace('/', '--')}--{model_name}"
    return model_path.exists()

def get_folder_size(path):
    total_size = 0
    for dirpath, _ , filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def list_models_in_remove_model():
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
                if folder_size < 50 * 1024 * 1024:
                    shutil.rmtree(model_dir)
                else:
                    click.echo(f"       * {blue}{repo_id}/{model_id}{reset}")
                    models_found = True
    if not models_found:
        click.echo(f"       {red}!!! No models available.{reset}")

def remove_model(model_identifier):
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    try:
        repo_id, model_name = model_identifier.split('/')
        model_dir = cache_dir / f"models--{repo_id}--{model_name}"
        if check_model_existence(repo_id, model_name):
            click.echo(f"\n    Removing Model {blue}{repo_id}/{model_name}{reset}...")
            shutil.rmtree(model_dir)
            click.echo(f"\n    {green}[Process complete]{reset} Removed Model {blue}{repo_id}/{model_name}{reset}")
            list_models_in_remove_model()
        else:
            click.echo(f"\n    {red}Model {repo_id}/{model_name} is not available!{reset}")
            list_models_in_remove_model()
    except:
        click.echo(f"\n    {red}[Invalid]{reset} Model format\n    Use format: {blue}repo_id/model_name{reset}\n")

