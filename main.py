import os
from dotenv import load_dotenv
from openai import OpenAI

"""
A simple command line utility to demonstrate how to make a call to
the OpenAI API. Rename .env to .env.development and then place your
OpenAI API key in the file.
For more information about the API go to:
https://platform.openai.com/docs/overview

Usage: python main.py
At the prompt, enter a query. The API will return a response.
Uses gpt-3.5-turbo as it's cheap. Change to gpt-4-turbo for better results,
but at a higher cost.
"""

# load .env file
env = os.getenv('ENVIRONMENT', 'development')
dotenv_path = f".env.{env}"
load_dotenv(dotenv_path=dotenv_path)

# prompt for a message
prompt = input("What is your question? : ")

# check prompt is not empty
if prompt != "":
    
    client = OpenAI()

    # retrieve api key
    client.api_key = os.getenv("OPENAI_API_KEY")

    # generate response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=500,
    )
    
    # print response to the console
    print("-" * len(prompt))
    print(prompt.title())
    print("-" * len(prompt))

    print(response.choices[0].message.content, end="\n\n")
    
