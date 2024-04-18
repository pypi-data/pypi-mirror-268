# LLMConnect API

## Table of Contents
- [Introduction](#Introduction)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
- [Commands](#commands)
- [Predefined tasks](#predefined-tasks)
  - [Command]()
  - [Output]()
- [Command examples]()
- [Author]()
- [License]()

## Introduction
LLMConnect API is a developer-friendly Python-based CLI utility designed to manage and evaluate Language Models including LLMs and SLMs on local servers or clusters. It enables users to run a variety of standard and custom tasks with popular models such as Llama-2, Mistral, Falcon, etc., and also supports the integration of new LLMs.


## Features
- Task Versatility: Execute predefined tasks like NER, Sentiment Analysis, Summarisation, or craft your own.
- Model Selection: Choose and add your custom LLMs and SLMs from HuggingFace.
- Adaptable Environments: Operate seamlessly on local servers and extend to local network clusters.
- Hardware Compatibility: Ensure efficient LLM functioning with GPU compatibility checks and memory monitoring.

CLI Interface:
- Navigate tasks, models, and hardware diagnostics with simple, intuitive commands.

Development & Security:
- Developed in Python 3.x, emphasising seamless LLM integration, and detailed documentation.
- Features enhanced input validation for secure, reliable operations.

Deployment:
- Eager to experience the power of Large Language Models through a Python-based Command Line Interface? LLMConnect API is your gateway to harnessing this technology on your local systems!

## Installation

### Required libraries
- Python 3.10
- click==8.1.7
- setuptools~=68.2.0
- transformers
- torch~=2.1.0
- accelerate
- bitsandbytes
- colorama

## Commands
- **lc list**
```
List all available tasks or models.

  Usage:
    lc list [OPTIONS] COMMAND [ARGS]

  Options:
    -h, --help  Show this message and exit.

  Commands:
    models  List available models
    tasks   List available tasks
```

- **lc add**
```
Add new Hugging Face Model. 

  Usage:
    lc add [OPTIONS]
    Model format: repo_id/model_id

  Options:
    --model TEXT  [required]
    -h, --help    Show this message and exit.
```

- **lc remove**
```
  Remove an existing HuggingFace Model.

  Usage:
    lc remove [OPTIONS]
    Model format: repo_id/model_id

  Options:
    --model TEXT  [required]
    -h, --help    Show this message and exit.
```

- **lc hardware**
```
Check hardware compatibility for given Hugging Face model.

  Usage: 
    lc hardware [OPTIONS]
    Model format: repo_id/model_id.

  Options:
    --model TEXT  Model name in format: repoID/modelID  [required]
    -h, --help    Show this message and exit.
```

- **lc exec**
```
Execute an input prompt with given model and given task.

  Usage: 
    lc exec [OPTIONS]

  Options:
    --task TEXT   Specify the task name  [required]
    --model TEXT  Specify the model name (repoID/modelID)  [required]
    --input TEXT  Specify input text (optional)
    -h, --help    Show this message and exit.
```

- **lc fetch**
```
Fetch the logs of previous sessions.

  Usage:
    lc fetch [OPTIONS]

  Options:
    -h, --help  Show this message and exit.
```
## Predefined tasks
### Command
lc list tasks
### Output
Available Tasks:
- NER                 
- Summary             
- AnalyseSentiment   
- DetectBias        
- TagTopic            
- Custom              

## Command examples
- lc list models
- lc list tasks
- lc add --model ceadar-ie/FinanceConnect-13B
- lc remove --model ceadar-ie/FinanceConnect-13B
- lc hardware --model ceadar-ie/FinanceConnect-13B
- lc exec --task NER --model ceadar-ie/FinanceConnect-13B --input "Hi! I'm LLMConnect API"
- lc fetch

## Code Repository
[LLM Connect API - GitLab](https://gitlab.com/CeADARIreland_Public/llm-connect-api/)

## Author
CeADAR Connect Group

## License
APACHE 2.0
