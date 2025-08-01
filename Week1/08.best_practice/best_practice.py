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

# 1. Use the latest model for best results.


# 2. Put instructions at the begining of the prompt and use ### or """ to separate the instruction and context

print("2. Put instructions at the begining of the prompt and use ### or \"\"\" to separate the instruction and context")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Summarize the text below as a bullet point list of the most important points. \n\n \
        ###\n\nWe’re happy to announce that OpenAI and Microsoft are extending our partnership.\
        This multi-year, multi-billion dollar investment from Microsoft follows their previous investments \
        in 2019 and 2021, and will allow us to continue our independent research and develop AI that is \
        increasingly safe, useful, and powerful. \n\n \
        In pursuit of our mission to ensure advanced AI benefits all of humanity, OpenAI remains a \
        capped-profit company and is governed by the OpenAI non-profit. This structure allows us to \
        raise the capital we need to fulfill our mission without sacrificing our core beliefs about \
        broadly sharing benefits and the need to prioritize safety. \
        Microsoft shares this vision and our values, and our partnership is instrumental to our progress. \n###',}],
        max_tokens=400,)

print(response.choices[0].message.content)

# 3. Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc
print("3. Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Write a poem about OpenAI.',}],
        max_tokens=400,)

print(response.choices[0].message.content)


response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Write a short inspiring poem about OpenAI, \
                focusing on the recent DALL-E product launch in the style of Ernest Hemingway',}],
        max_tokens=400,)

print(response.choices[0].message.content)


# 4. Articulate the desired output format through examples (example 1, example 2). 
print("4. Articulate the desired output format through examples (example 1, example 2). ")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Extract the companyn names then years in the following text below and output start index and end index of each entity.\
                Generate output as {"text": "OpenAI", "start": 28, "end": 34} \
                ###\
                We’re happy to announce that OpenAI and Microsoft are extending our partnership.\
                This multi-year, multi-billion dollar investment from Microsoft follows their previous investments \
                in 2019 and 2021, and will allow us to continue our independent research and develop AI that is \
                increasingly safe, useful, and powerful. \n\n \
                ###\
                ',}],
        max_tokens=400,)

print(response.choices[0].message.content)


response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Extract the entities mentioned in the text below. \
                Extract the important entities mentioned in the text below. \
                First extract all company names, then extract all years, \
                then extract specific topics which fit the content and finally extract general overarching themes\n\n \
                Desired format: \
                Company names: <comma_separated_list_of_company_names> \
                Years: -||- \
                Specific topics: -||- \
                General themes: -||- \
                """\
                We’re happy to announce that OpenAI and Microsoft are extending our partnership.\
                This multi-year, multi-billion dollar investment from Microsoft follows their previous investments \
                in 2019 and 2021, and will allow us to continue our independent research and develop AI that is \
                increasingly safe, useful, and powerful. \n\n \
                """\
                ',}],
        max_tokens=400,)

print(response.choices[0].message.content)


# 5. Start with zero-shot, then few-shot (example), neither of them worked, then fine-tune (To update)
print("5. Start with zero-shot, then few-shot (example), neither of them worked, then fine-tune (To update)")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant. Extract keywords from the corresponding texts below."},
                {"role":"user","content": 'Text: \n\
            We’re happy to announce that OpenAI and Microsoft are extending our partnership.\
            This multi-year, multi-billion dollar investment from Microsoft follows their previous investments \
            in 2019 and 2021, and will allow us to continue our independent research and develop AI that is \
            increasingly safe, useful, and powerful. \n\nKeywords:    ',}],
        max_tokens=400,)

print(response.choices[0].message.content)


response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant. Extract keywords from the corresponding texts below.\n\n \
                Text: Stripe provides APIs that web developers can use to integrate \
                payment processing into their websites and mobile applications. \
                Keywords: Stripe, payment processing, APIs, web developers, websites, mobile applications \
                ###\n\
                Text: OpenAI has trained cutting-edge language models that are very good at understanding \
                and generating text. Our API provides access to these models and can be used to solve virtually \
                any task that involves processing language. \n\
                Keywords: language models, text processing, API.\n\n\
                ##W"},
                {"role":"user","content": '\n\
                Text: We’re happy to announce that OpenAI and Microsoft are extending our partnership.\
                This multi-year, multi-billion dollar investment from Microsoft follows their previous investments \
                in 2019 and 2021, and will allow us to continue our independent research and develop AI that is \
                increasingly safe, useful, and powerful. \n\n\
                Keywords:',}],
        max_tokens=400,)

print(response.choices[0].message.content)


# 6. Reduce “fluffy” and imprecise descriptions
print("6. Reduce “fluffy” and imprecise descriptions")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Write a description for a new product. This product is a new generation of car seat. \
                The description for this product should be fairly short, a few sentences only, and not too much more.',}],
        max_tokens=400,)

print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'Write a description for a new product. This product is a new generation of car seat. \
                Use a 3 to 5 sentence paragraph to describe this product.',}],
        max_tokens=400,)

print(response.choices[0].message.content)


# 7. Instead of just saying what not to do, say what to do instead
print("7. Instead of just saying what not to do, say what to do instead")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'The following is a conversation between an Agent and a Customer. DO NOT ASK USERNAME OR PASSWORD. DO NOT REPEAT. \n\n\
                Customer: I can’t log in to my account.\n\
                Agent:',}],
        max_tokens=400,)

print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content":'The following is a conversation between an Agent and a Customer. The agent will attempt to diagnose the \
                problem and suggest a solution, whilst refraining from asking any questions related to PII. \
                Instead of asking for PII, such as username or password, refer the user to the help \
                article www.samplewebsite.com/help/faq \n\n\
                Customer: I can’t log in to my account. \n\
                Agent:',}],
        max_tokens=400,)

print(response.choices[0].message.content)

# 8. Code Generation Specific - Use “leading words” to nudge the model toward a particular pattern
print("8. Code Generation Specific - Use \“leading words\” to nudge the model toward a particular pattern")

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content": 'The following is a conversation between an Agent and a Customer. DO NOT ASK USERNAME OR PASSWORD. DO NOT REPEAT. \n\n\
                Customer: I can’t log in to my account.\n\
                Agent:',}],
        max_tokens=400,)

print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=CHAT_COMPLETIONS_MODEL,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content":'# Write a simple python function that \n\
                # 1. Ask me for a number in mile\n\
                # 2. It converts miles to kilometers\n\
                 import ',}],
        max_tokens=400,)

print(response.choices[0].message.content)


# 9. Use the Generate Anything feature
print("9. Use the Generate Anything feature")

