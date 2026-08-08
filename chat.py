import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-flash-latest")

messages = []

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    response = chat.send_message(user_input)
    reply = response.text

    messages.append({"role": "assistant", "content": reply})

    print("Bot:", reply)