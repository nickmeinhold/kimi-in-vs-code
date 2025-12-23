import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="moonshotai/kimi-k2",
    messages=[
        {
            "role": "user",
            "content": "Write a simple Python function to calculate the factorial of a number.",
        },
    ],
)
print(response.choices[0].message.content)
