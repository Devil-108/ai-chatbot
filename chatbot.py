
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found. Please configure your API key.")

client = Anthropic(api_key=api_key)

messages = []

print("AI Chatbot is ready!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=messages
        )

        assistant_reply = response.content[0].text

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

        print(f"\nAI: {assistant_reply}\n")

    except Exception as error:
        print(f"Error: {error}")
