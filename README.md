# mini-rag app

This is an RAG implementation for question answering.

## Requirements

- Python 3.8 or later.

## Install Python using Miniconda

1) Download and Install MiniConda from [here](https://continuumio-docs.readthedocs-hosted.com/miniconda/install/)
2) Create a new environment using the following command:
```bash
conda create -n mini-rag python=3.8
```
3) Activate the environment using the following command:
```bash
conda activate mini-rag
```

## Installation
### Install the required packages
```bash
pip install -r requirements.txt
```

## setup the environment variables
```bash
cp -env.example .env
```

set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
