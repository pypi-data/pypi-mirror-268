import click
from colorama import init, Fore, Back, Style

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
background_color = Back.BLACK
reset = Style.RESET_ALL

def list_tasks():
    tasks = f"""
    Available Tasks:
       * {blue}NER{reset}                 #Name Entity Recognition from input content
       * {blue}Summary{reset}             #Summary of input content
       * {blue}AnalyseSentiment{reset}    #Sentiment analysis of input content
       * {blue}DetectBias{reset}          #Bias detection in input content
       * {blue}TagTopic{reset}            #Topic tagging to input content
       * {blue}Custom{reset}              #Custom user prompt
    """
    click.echo(tasks)
