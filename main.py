import os
from openai import OpenAI
import dotenv

# Load environment variables from .env file
api_key = dotenv.load_dotenv()

if not api_key:
    raise ValueError("API KEY not found in environment variables")

client = OpenAI(api_key=api_key)

messages = []

def completion(message):
    global messages
    messages.append(
            {
                "role": "user",
                "content": message
            }
        )
    chat_completion = client.chat.completions.create(messages =  messages,model="gpt-4o",)
    # print(chat_completion)
    message =   {
        "role": "assistant",
        "content" : chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis said this - {message['content']}")
    
if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, how may I help you ?\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)