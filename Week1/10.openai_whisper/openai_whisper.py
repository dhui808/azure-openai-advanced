import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv()
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  azure_ad_token_provider=token_provider,
  api_version="2024-10-21"
)

# from openai import AzureOpenAI
# client = AzureOpenAI()

audio_file = open("./TedTalk_Bill_Gates.wav", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper", # Replace with model deployment name
  file=audio_file
)

print(transcript)
