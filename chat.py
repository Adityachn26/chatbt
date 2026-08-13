from db import init_db, save_message,load_messages
import os
from google import genai
from dotenv import load_dotenv

init_db()
history = load_messages()
for role,content in history:
    print(f"{role}:{content}")
if history:
    print("---previous conversation loaded---")


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-flash-latest")

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break
    save_message("user",user_input)

    response = chat.send_message(user_input)
    reply = response.text

    save_message("assistant",reply)

    print("Bot:", reply)