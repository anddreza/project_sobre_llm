import os

from crewai import Agent, Task, Crew
from langchain_core import *
from crewai_tools import SerperDevTool
from litellm import completion

#load_dotenv('/content/drive/MyDriver/Colab Notebooks/IA/.env')
from dotenv import load_dotenv
load_dotenv('.env')

response = completion(
    model="groq/llama3-8b-8192",
    messages=[
        {"role": "user", "content": "hello"}
    ]
)

if response is None:
    print("Erro ao obter resposta do modelo.")
else:
    print(response)
