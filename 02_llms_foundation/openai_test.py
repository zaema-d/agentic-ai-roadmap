# openai_test.py
# 🆕 Updated for openai>=1.0.0 SDK

import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")

# Create OpenAI client
client = OpenAI(api_key=api_key)

def test_openai_chat():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Explain the concept of gravity in simple terms."}
            ],
            temperature=0.7,
        )

        print("\n🧠 GPT Response:\n")
        print(response.choices[0].message.content)

    except Exception as e:
        print("❌ Error while calling OpenAI API:", e)

if __name__ == "__main__":
    test_openai_chat()
