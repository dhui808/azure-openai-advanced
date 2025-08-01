### Setup Whisper Model
```
Install the Azure CLI: PowerShell
	winget install microsoft.azd
	Open another PowerShell/Prompt console:
	azd version
	
	azd auth login
		Logged in to Azure as *@outlook.com
	python openai_whisper.py
	
Install or update the Az PowerShell module:
	Install-Module -Name Az.Accounts -RequiredVersion
	
Create an Azure AI Foundry resource
	Go to Azure AI Foundry portal
	... More
	My Assets -> Models + endpoints
	Model deployments
	Deploy Model -> Deploy base Model
	Select whisper
	Confirm
	Deploy whisper
		Connected AI resource: abc-mdq2fnsa-eastus2
		Deployment type: Standard
		Model Version: 001
		Resource  Location: East US 2
	Deploy
	
	Endpoint Target URI: 
	Authentication type Key:

https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whisper-quickstart?tabs=command-line%2Cpython-new%2Ckeyless%2Ctypescript-keyless&pivots=programming-language-python
```

### Run openai_whisper.py
```
(azure) C:\project\Week1\10.openai_whisper>python openai_whisper.py
Transcription(text="I'm going to talk today about energy and climate. And that might seem a bit surprising, because my full-time work at the Foundation is mostly about vaccines and seeds, about the things that we need to invent and deliver to help the poorest 2 billion live better lives. But energy and climate are extremely important to these people, in fact, more important than to anyone else on the planet. The climate getting worse means that many years their crops won't grow. There'll be too much rain, not enough rain. Things will change in ways that their fragile environment simply can't support. And that leads to starvation, it leads to uncertainty, it leads to unrest. So the climate changes will be terrible for them. Also, the price of energy is very important to them. In fact, if you could pick just one thing to lower the price of, to reduce poverty, by far you would pick energy. Now, the price of energy has come down over time. Really, advanced civilization is based on advances in energy. The coal revolution fueled the industrial revolution. And even in the 1900s, we've seen a very rapid decline in the price of electricity. That's why we have refrigerators, air conditioning. We can make modern materials and do so many things. And so we're in a wonderful situation with electricity in the rich world. But as we make it cheaper, and let's say, let's go for making it twice as cheap, we need to meet a new constraint. And that constraint has to do with CO2. CO2 is warming the planet. And the equation on CO2 is actually a very straightforward one. If you sum up the CO2 that gets emitted, that leads to a temperature increase. And that temperature increase leads to some very negative effects. The effects on the weather, perhaps worse, the indirect effects, in that the natural ecosystems can't adjust to these rapid changes, and so you get ecosystem collapses.", logprobs=None)
```