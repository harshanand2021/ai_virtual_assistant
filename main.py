import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

messages = []

def completion(message):
    global messages
    chat_completion = client.chat.completions.create(
        messages.append(
            {
                "role": "user",
                "content": message,
            }
        ),
        model="gpt-4o",
    )
    print(chat_completion)
    message =   {
        "role": "assistant",
        "content" : chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis said this - {message['content']}")
    
if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, how may I help you ?")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)