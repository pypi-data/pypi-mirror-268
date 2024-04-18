import sys
import click
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import shutil
from ..config import (available_tasks)

device = "cuda" if torch.cuda.is_available() else "cpu"
import os
from datetime import datetime
from colorama import init, Fore, Style, Back

init(autoreset=True)

green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
background_color = Back.BLACK
reset = Style.RESET_ALL

script_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_directory, 'execution_logs.txt')

def get_folder_size(path):
    total_size = 0
    for dirpath, _ , filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def list_tasks_in_execute():
    tasks = f"""
    Available tasks:
       * {blue}NER{reset}                 #Name Entity Recognition from input content
       * {blue}Summary{reset}             #Summary of input content
       * {blue}AnalyseSentiment{reset}    #Sentiment analysis of input content
       * {blue}DetectBias{reset}          #Bias Detection in input content
       * {blue}TagTopic{reset}            #Topic tagging to input content
       * {blue}Custom{reset}              #Custom user prompt
    """
    click.echo(tasks)

def check_model_existence(repo_id, model_name):
    model_path = Path.home() / ".cache" / "huggingface" / "hub" / f"models--{repo_id.replace('/', '--')}--{model_name}"
    return model_path.exists()

def list_models_in_execute():
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

def execute(task, model, input_text=None):
    lowercase_tasks = [task.lower() for task in available_tasks]
    if task.lower() not in lowercase_tasks:
        click.echo(f"\n    {red}!!!{reset} Task {blue}{task}{reset} is not available.")
        f"{list_tasks_in_execute()}\n"
        return
    repo_id, model_id = model.split('/') if '/' in model else (None, model)
    model_path = Path.home() / ".cache" / "huggingface" / "hub" / f"models--{repo_id.replace('/', '--')}--{model_id}"
    if not model_path.exists():
        click.echo(
            f"\n    {red}!!!{reset} Model {blue}{model}{reset} is not available.\n    Add model using ${yellow}lc add --model {model}{reset}")
        f"{list_models_in_execute()}\n"
        return
    model_path = f"{repo_id}/{model_id}"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto",
                                                 trust_remote_code=True)
    while True:
        click.echo(f"\n    Executing task {blue}{task}{reset} using model {blue}{repo_id}/{model_id}{reset}...\n")
        lowercase_tasks = [task.lower() for task in available_tasks]
        if task.lower() not in lowercase_tasks:
            click.echo(f"    {red}!!!{reset} Task {blue}{task}{reset} is not available.")
            f"{list_tasks_in_execute()}\n"
            task = input("\n    Enter task: ")
        if check_model_existence(repo_id, model_id):
            if task.lower() == 'custom':
                custom_input = input_text if input_text is not None else input(
                    f"    Enter your {blue}custom{reset} prompt: ")
                prompt = f"{custom_input}"
            elif task.lower() == 'ner':
                ner_text = input_text if input_text is not None else input(
                    f"    {magenta}Enter text to recognise entities{reset}\n")
                prompt = f"Recognise the entities from the following text: {ner_text}."
            elif task.lower() == 'tagtopic':
                topics = input(f"    {magenta}Enter list of topics e.g. technology, art, news etc..{reset}\n")
                tagtopic_text = input(f"    {magenta}Enter input text for topic tagging:{reset}\n")
                prompt = f"Classify the following text in one of the topics from the list [{topics}]: {tagtopic_text}. Strictly respond with a one-word answer only."
            elif task.lower() == 'summary':
                summary_text = input_text if input_text is not None else input(
                    f"    {magenta}Enter text to summarise{reset}\n")
                prompt = f"Concisely summarise the following text: {summary_text}."
            elif task.lower() == 'analysesentiment':
                sentiment_text = input_text if input_text is not None else input(
                    f"    {magenta}Enter text to analyse sentiment{reset}\n")
                prompt = f"Analyze the sentiment of the following text: {sentiment_text}."
            elif task.lower() == 'detectbias':
                bias_text = input_text if input_text is not None else input(
                    f"    {magenta}Enter text to detect bias{reset}\n")
                prompt = f"Analyze the following text for any biases: {bias_text}."
            def generate_text():
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=2800)
                result = pipe(prompt, pad_token_id=pipe.tokenizer.eos_token_id)
                generated_text = result[0]['generated_text'].replace(prompt, "").strip()
                print(f"\n    {yellow}Generated text:{reset} {generated_text}")
                if task.lower() == 'custom':
                    log_entry = f"\n###################################################\n\n    {magenta}[{time}]{reset}\n    {magenta}Model:{reset} {model_id}\n    {magenta}Task:{reset} {task}\n    {magenta}Input:{reset} {custom_input}\n    {magenta}Output:{reset} {generated_text}\n"
                elif task.lower() == 'ner':
                    log_entry = f"\n###################################################\n\n    {magenta}[{time}]{reset}\n    {magenta}Model:{reset} {model_id}\n    {magenta}Task:{reset} {task}\n    {magenta}Input:{reset} {ner_text}\n    {magenta}Output:{reset} {generated_text}\n"
                elif task.lower() == 'tagtopic':
                    log_entry = f"\n###################################################\n\n    {magenta}[{time}]{reset}\n    {magenta}Model:{reset} {model_id}\n    {magenta}Task:{reset} {task}\n    {magenta}Input:{reset} {tagtopic_text}\n    {magenta}Output:{reset} {generated_text}\n"
                else:
                    log_entry = f"\n###################################################\n\n    {magenta}[{time}]{reset}\n    {magenta}Model:{reset} {model_id}\n    {magenta}Task:{reset} {task}\n    {magenta}Input:{reset} {input_text}\n    {magenta}Output:{reset} {generated_text}\n"
                if not os.path.exists(log_file_path):
                    with open(log_file_path, 'w'):
                        pass
                with open(log_file_path, 'a') as log_file:
                    log_file.write(log_entry)
            generate_text()
        else:
            click.echo(
                f"    {magenta}Model{reset} {blue}{model}{reset} {magenta}is not downloaded. You can download it using{reset} ${yellow}lc add --model {model}{reset}")
        torch.cuda.empty_cache()
        while True:
            continue_choice = input(f"\n    {magenta}Do you want to exit? (yes/no):{reset} ").strip().lower()
            if continue_choice == 'yes' or continue_choice == 'y':
                sys.exit()
            elif continue_choice == 'no' or continue_choice == 'n':
                task = input("\n    Enter task: ")
                input_text = None
                break
            else:
                print(f"    {red}\n    Please select yes/y or no/n{reset}")
