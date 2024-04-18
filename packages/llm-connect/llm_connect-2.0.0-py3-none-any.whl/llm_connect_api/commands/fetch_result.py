import click
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_directory, 'execution_logs.txt')
def fetch_result():
    if os.path.exists(log_file_path):
        click.echo(f"\n    Fetching previous LLM sessions...\n")
        with open(log_file_path, 'r') as file:
            content = file.read()
            click.echo(content)
    else:
        click.echo("\n    No previous logs!\n")
