# How to Use Kimi K2 in VSCode Copilot (The Easy Way)

Moonshot AI's Kimi K2 is a powerful language model with 1 trillion parameters and a 128K context window. Here's how to use it in VSCode Copilot in under 2 minutes.

## What You'll Need

- VSCode with GitHub Copilot extension
- An OpenRouter account (free to sign up)

## Step 1: Get an OpenRouter API Key

1. Go to [OpenRouter](https://openrouter.ai/)
2. Sign up or log in
3. Navigate to API Keys and create one

## Step 2: Configure VSCode Copilot

1. Open VSCode
2. Open Copilot Chat (Cmd+Shift+I on Mac, Ctrl+Shift+I on Windows)
3. Click the model selector dropdown
4. Click "Manage Models..."
5. Select **OpenRouter** as the provider
6. Enter your API key when prompted
7. Select **Kimi K2** from the available models

That's it. You're now using Kimi K2 in VSCode.

## Using Kimi K2 in Python Scripts

Want to call Kimi K2 from your own code? It's just as simple.

### Setup

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install openai python-dotenv
```

### Create a .env file

```
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_API_KEY=your-api-key-here
```

### Write your script

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="moonshotai/kimi-k2",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms."},
    ],
)
print(response.choices[0].message.content)
```

### Run it

```bash
python test.py
```

## Example Repository

I've put together a complete working example at:

**https://github.com/nickmeinhold/kimi-in-vs-code**

Clone it, add your `.env` file with your API key, and you're ready to go.

## Why Kimi K2?

- **1 trillion total parameters** (32B active during inference)
- **128K token context window**
- Strong performance on coding and reasoning tasks
- Available through OpenRouter with simple API access

## Conclusion

No proxy servers. No Docker containers. No complicated setup. Just connect VSCode Copilot directly to OpenRouter and start using Kimi K2.

---

*The example code is available at [github.com/nickmeinhold/kimi-in-vs-code](https://github.com/nickmeinhold/kimi-in-vs-code)*
