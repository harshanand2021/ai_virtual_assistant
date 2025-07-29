import os
from openai import OpenAI

key=os.getenv("API_KEY")

client = OpenAI(
    api_key = key,
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
    user_question = input("Hi I am Jarvis, how may I help you ?")
    completion(user_question)