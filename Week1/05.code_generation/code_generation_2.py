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

code = "Can you explain what does this code do?\n#\n# ###\n\
   Code:\n\
   SELECT d.name FROM Department d JOIN Employee e ON d.id = e.department_id WHERE e.id IN (SELECT employee_id FROM Salary_Payments WHERE date > now() - interval '3 months') GROUP BY d.name HAVING COUNT(*) > 10\n#\n#\
   Answer:\n# "

response = client.chat.completions.create(
  model=CHAT_COMPLETIONS_MODEL,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content": code}],
  temperature=0,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,)
print(response.choices[0].message.content)


