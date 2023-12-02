import os
from dotenv import load_dotenv
from openai import OpenAI

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
    print("-" * len(prompt))
    print(prompt.title())
    print("-" * len(prompt))

    print(response.choices[0].message.content, end="\n\n")
    
