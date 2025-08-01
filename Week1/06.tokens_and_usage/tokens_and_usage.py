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
  api_version="2024-02-15-preview"
)

CHAT_COMPLETIONS_MODEL = os.getenv('CHAT_COMPLETION_NAME')

encoding=tiktoken.encoding_for_model("gpt-3.5-turbo")
prompt = "Azure OpenAI service is General Available now!"
tokens = encoding.encode(prompt)
print('Total number of tokens:', len(tokens))
print('Tokens :', tokens)
print('Words : ', [encoding.decode([t]) for t in tokens])

response = client.chat.completions.create(
  model=CHAT_COMPLETIONS_MODEL,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content": prompt}],
    max_tokens=60,
    n=2,
)

print('='*30, 'ANSWER #1', '='*30)
print(response.choices[0].message.content)
print('='*30, 'ANSWER #2', '='*30)
print(response.choices[1].message.content)

# Usage
print(response.usage)
