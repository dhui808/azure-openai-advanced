import re
import requests
import sys
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)

CHAT_COMPLETIONS_MODEL = os.getenv('CHAT_COMPLETION_NAME')

prompt = "### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\n\n query: "
print(prompt)
response = client.chat.completions.create(
  model=CHAT_COMPLETIONS_MODEL,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content": prompt}],
  temperature=0,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["#",";"])
print(response.choices[0].message.content)

