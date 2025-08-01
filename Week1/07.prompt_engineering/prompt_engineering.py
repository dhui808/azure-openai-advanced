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

# Zero-shot classification
system_prompt ="""Predict up to 5 emojis as a response to a text chat message. The output
should only include emojis.

input: The new visual design is blowing my mind 🤯
output: ➕,💘, ❤‍🔥

input: Well that looks great regardless
output: ❤️,🪄

input: Unfortunately this won't work
output: 💔,😔

input: sounds good, I'll look into that
output: 🙏,👍

input: 10hr cut of jeff goldblum laughing URL
output: 😂,💀,⚰️
"""
user_prompt = "The new user interface is amazing!"
response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":system_prompt},
                {"role":"user","content": user_prompt,}])
print(response.choices[0].message.content)

