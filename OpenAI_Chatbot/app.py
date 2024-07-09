from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#Import API key
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

while True:
    question = input("User : ")
    if question != "bye":
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            max_tokens=50, #Number of tokens from response
            n=1, #Number of response we could get from the response
            temperature=0.8, #Changes the randomness of the response
            messages=[
                {'role':'user',
                 'content':question}
                ]
            )
        
        for choice in response.choices:
            print(f"AI: {choice.message.content}")
            
    else:
        print("AI: Bye")
        break