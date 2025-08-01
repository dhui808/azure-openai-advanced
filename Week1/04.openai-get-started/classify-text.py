import re
import requests
import sys
import os
from openai import AzureOpenAI
import tiktoken
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-12-01-preview"
)

# Select the General Purpose curie model for text
model = "gpt-4.1-mini"
deployment = "gpt-4.1-mini"

prompt = "Classify the following inquiry into one of the following: categories: [Pricing, Hardware Support, Software Support]\n\ninquiry: Hello, one of the keys on my laptop keyboard broke recently and I'll need a replacement:\n\nClassified category:"
print(prompt)

response = client.chat.completions.create(
    max_completion_tokens=800,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=model,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content":prompt},])

print(response.choices[0].message.content)
