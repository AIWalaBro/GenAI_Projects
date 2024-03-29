# Deploy LLM App as api using Langserve-Langchain

## Steps to install

```bash
- conda create -p venv_langserve python=3.10 -y
```
```bash
- conda activate venv_langserve
```
```bash
- pip install -r requirements.txt
```
```bash
- python app.py
- python client.py
```

```bash
`Note:` if you get version issues, please install 
if version issue :
    - pip install -U langchain-community
        - from langchain_community.chat_models import ChatOpenAI
else:
    - pip install -U langchain-openai
        - from langchain_openai import ChatOpenAI

# this for the server
- pip install sse_starlette

# if pydantic erro comes
- pip install pydantic==1.10.13
```

## Requirement file libraries used purposes

`Langchain:` It appears to be a software development framework or tool related to language processing or blockchain technology.


`Langchain-OpenAI:` This could be an extension or integration of Langchain with OpenAI's technology, possibly for natural language processing.


`Langchain-Core:` Likely the core or foundational component of the Langchain framework, handling essential functionalities.


`Python-dotenv:` A Python library used for managing environment variables in a .env file, commonly used in development to store sensitive configuration data.


`FastAPI:` A modern web framework for building APIs with Python, known for its fast performance and easy-to-use design.


`Uvicorn:` An ASGI (Asynchronous Server Gateway Interface) server that serves FastAPI applications, enabling high-performance asynchronous web applications in Python.



