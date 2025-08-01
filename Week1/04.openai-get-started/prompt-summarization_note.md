## Setup
```
https://azure.microsoft.com/en-us/get-started/azure-portal


	Create an Azure AI Foundry resource
	We’ll grant your user identity the Azure AI User role so you can develop with all projects under this resource.
	Your data is encrypted by default using Microsoft-managed keys.
	Go to Azure AI Foundry portal
	... More
	My Assets -> Models + endpoints
	Model deployments
	Deploy Model -> Deploy base Model
	Select gpt-4.1-mini
	Confirm
	Deploy gpt-4.1-mini
		Deployment type: Global standard
		Model Version: 2025-04-14
		Resource  Location: East US 2
	Create resource and deploy
	
		Endpoint
		Target URI:
		Authentication type Key:

Global standard is cheaper but less secure since data may go to other country.
```

### Build your first prompt  
```
This short exercise will provide a basic introduction for submitting prompts to an OpenAI model for a simple task "summarization".  

![](images/generative-AI-models-reduced.jpg)  


**Steps**:  
conda activate azure
1. Install OpenAI library in your python environment  
	pip install tiktoken
2. Load standard helper libraries and set your typical OpenAI security credentials for the OpenAI Service that you've created  
3. Choose a model for your task  
4. Create a simple prompt for the model  
5. Submit your request to the model API!
```

### Run prompt-summarization-2.py
```
(azure) C:\project\Week1\04.openai-get-started>python prompt-summarization-2.py
That sounds wonderful! Paris is a city full of incredible sights and experiences. Here are some must-see attractions and activities:

1. **Eiffel Tower** – The iconic symbol of Paris. You can go up for a stunning view of the city.
2. **Louvre Museum** – Home to thousands of works of art, including the Mona Lisa and the Venus de Milo.
3. **Notre-Dame Cathedral** – Although under restoration, it’s still worth visiting the area and seeing the façade.
4. **Champs-Élysées and Arc de Triomphe** – Walk down this famous avenue and visit the Arc de Triomphe for panoramic views.
5. **Montmartre and Sacré-Cœur Basilica** – Explore this artistic neighborhood and enjoy the view from the basilica’s dome.
6. **Sainte-Chapelle** – Known for its stunning stained glass windows.
7. **Seine River Cruise** – Take a boat tour on the Seine, especially beautiful at night.
8. **Musée d'Orsay** – Famous museum housed in a former railway station, showcasing Impressionist masterpieces.
9. **Luxembourg Gardens** – A lovely spot for a relaxing walk or picnic.
10. **Le Marais District** – Trendy area with boutiques, cafés, and historic Jewish quarter.

If you have extra time, consider a day trip to **Versailles Palace** or the charming neighborhood of **Saint-Germain-des-Prés**.

Would you like recommendations on dining, shopping, or hidden gems as well?
```

### Run prompt-summarization.py
```
(azure) C:\project\Week1\04.openai-get-started>python prompt-summarization.py

(azure) C:\project\Week1\04.openai-get-started>python prompt-summarization.py
Why do programmers prefer dark mode?

Because light attracts bugs!
```

### Run summarize-text.py
```
(azure) C:\project\Week1\04.openai-get-started>python summarize-text.py
Scaling up language models significantly enhances their ability to perform new NLP tasks with few examples or simple instructions, reducing the need for large task-specific datasets and approaching or matching the performance of traditional fine-tuning methods.
```

### Run classify-text.py
```
(azure) C:\project\Week1\04.openai-get-started>python classify-text.py
Classify the following inquiry into one of the following: categories: [Pricing, Hardware Support, Software Support]

inquiry: Hello, one of the keys on my laptop keyboard broke recently and I'll need a replacement:

Classified category:
Classified category: Hardware Support
```

### Run generate-new-product-name.py
```
(azure) C:\project\Week1\04.openai-get-started>python generate-new-product-name.py
Product description: A home milkshake maker
Seed words: fast, healthy, compact.
Product names: HomeShaker, Fit Shaker, QuickShake, Shake Maker

Product description: A pair of shoes that can fit any foot size.
Seed words: adaptable, fit, omni-fit.
Here are product name suggestions based on your descriptions and seed words:

1. For the home milkshake maker:
- QuickShake (matches "fast")
- Fit Shaker (suggests healthy and fitness)
- HomeShaker (descriptive and home-friendly)
- CompactShake (combining compact and shake)

2. For the shoes that fit any foot size:
- Omni-Fit Shoes (directly from the seed word)
- AdaptFit
- FitFlex
- VersaFit Shoes

If you'd like, I can help generate product taglines or more name options!
```

### Set up Embeddings
```
	My Assets -> Models + endpoints
	Model deployments
	Deploy Model -> Deploy base Model
	Select text-embedding-3-small
	Confirm
	Deploy 
		Deployment type: Global standard
		Model Version: 1
		Resource  Location: East US
	Deploy

	Traget URI:
	Key:
```

### Run embeddings.py
```
(azure) C:\project\Week1\04.openai-get-started>python embeddings.py
0.3682127371790198
0.6689172400713537
0.7729230263044823
```

### Comparing article from cnn daily news dataset
```
	pip install pandas

```

### Run comparing_articles.py
```
(azure) C:\project\Week1\04.openai-get-started>python comparing_articles.py
                                            articles                                         highligths
0  BREMEN, Germany -- Carlos Alberto, who scored ...  Werder Bremen pay a club record $10.7 million ...
1  (CNN) -- Football superstar, celebrity, fashio...  Beckham has agreed to a five-year contract wit...
2  LOS ANGELES, California (CNN) -- Youssif, the ...  Boy on meeting Spider-Man: "It was my favorite...
0.6693133578213519
0.8841862966109504
```
