from llm_connect_api.commands.add_model import add_model
from llm_connect_api.commands.fetch_result import fetch_result
from llm_connect_api.commands.hardware import show_hardware
from llm_connect_api.commands.list_models import list_models
from llm_connect_api.commands.list_tasks import list_tasks
from llm_connect_api.commands.execute import *
from llm_connect_api.commands.remove_model import remove_model

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    LLMConnect API is a developer-friendly Python-based CLI utility designed to manage and execute Language Models from HuggingFace on local servers or clusters. It enables users to run a variety of standard and custom tasks with popular models such as Llama-2, Mistral, Falcon, etc., and also supports multiple features including integration of new LLMs, hardware compatability check, and logging functionality.

    Available command:

        * lc list models

        * lc list tasks

        * lc fetch

        * lc add --model <MODEL_NAME>

        * lc hardware --model <MODEL_NAME>

        * lc exec --task <TASK_NAME> --model <MODEL_NAME> --input <INPUT>
    """
    pass

@cli.group()
def list():
    """
    List all available tasks or models."""
    pass

@list.command(name="models", help="List available models",context_settings=CONTEXT_SETTINGS)
def models():
    list_models()

@list.command(name="tasks", help="List available tasks",context_settings=CONTEXT_SETTINGS)
def tasks():
    list_tasks()

@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option('--model', required=True)
def add(model):
    """Add new HuggingFace Model.

    * Model format: repo_id/model_id"""
    add_model(model)


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option('--model', required=True)
def remove(model):
    """Remove an existing HuggingFace Model.

    * Model format: repo_id/model_id"""
    remove_model(model)

@cli.command(context_settings=CONTEXT_SETTINGS)
def fetch():
    """Fetch the logs of previous sessions."""
    fetch_result()

@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option('--model', required=True,
              help='Model name in format: repoID/modelID')

def hardware(model):
    """Check hardware compatibility for given HuggingFace model.

    * Model format: repo_id/model_id."""
    show_hardware(model)

@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option("--task", required=True, type=click.STRING, help="Specify the task name")
@click.option("--model", required=True, type=click.STRING, help="Specify the model name (repoID/modelID)")
@click.option("--input", required=False,  type=click.STRING, help="Specify input text (optional)")
def exec(task, model, input):
    """Execute an input prompt with given model and given task."""
    execute(task, model, input)


if __name__ == '__main__':
    cli()
