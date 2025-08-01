import numpy as np
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

model="text-embedding-3-small"
def cosine_similarity(query_embedding, embeddings, distance_metric='cosine'):
    if distance_metric == 'cosine':
        distances = np.dot(embeddings, query_embedding) / (np.linalg.norm(embeddings) * np.linalg.norm(query_embedding))
        distances = 1 - distances  
    else:
        raise ValueError("Métrica de distância não suportada. Utilize 'cosine'.")

    return distances
    
text = 'the quick brown fox jumped over the lazy dog'

client = AzureOpenAI(
  azure_endpoint = "https://abc.cognitiveservices.azure.com/", 
  api_key="my_key",  
  api_version="2024-12-01-preview"
)

client.embeddings.create(input=[text], model=model).data[0].embedding


# compare several words
automobile_embedding    = client.embeddings.create(input='automobile', model=model).data[0].embedding
vehicle_embedding       = client.embeddings.create(input='vehicle', model=model).data[0].embedding
dinosaur_embedding      = client.embeddings.create(input='dinosaur', model=model).data[0].embedding
stick_embedding         = client.embeddings.create(input='stick', model=model).data[0].embedding

print(cosine_similarity(automobile_embedding, vehicle_embedding))
print(cosine_similarity(automobile_embedding, dinosaur_embedding))
print(cosine_similarity(automobile_embedding, stick_embedding))