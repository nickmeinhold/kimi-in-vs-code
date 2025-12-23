# How to Use Kimi K2 in VSCode Copilot - Corrected Tutorial

## What's Wrong with the Apidog Tutorial

The [Apidog tutorial](https://apidog.com/blog/kimi-k2-vscode-copilot/) overcomplicates the setup and contains errors.

### Main Problem: fake-ollama is Unnecessary

The tutorial introduces "fake-ollama" as a bridge between VSCode and OpenRouter. **This is completely unnecessary.** VSCode Copilot has built-in support for OpenRouter - you can connect directly without any proxy server.

### Other Errors

1. **Wrong build system**: The tutorial claims fake-ollama uses Python (`pip install`, `python main.py`), but it's actually written in **Go**. The repo has no `requirements.txt` or Python files - only `main.go` and `go.mod`.

2. **fake-ollama doesn't proxy requests**: Looking at the source code, fake-ollama is a mock server that returns hardcoded responses. It doesn't forward requests to external APIs.

---

## The Simple Way: Direct OpenRouter in VSCode Copilot

### Step 1: Get an OpenRouter API Key

1. Go to [OpenRouter](https://openrouter.ai/)
2. Sign up / log in
3. Create an API key

### Step 2: Configure VSCode Copilot

1. Open VSCode
2. Open Copilot Chat
3. Click the model selector (or type `/` and select "Select a Model")
4. Click "Manage Models..." or look for custom model options
5. Select **OpenRouter** as the provider
6. Enter your OpenRouter API key when prompted
7. Select **Kimi K2** (`moonshotai/kimi-k2`) from the available models

That's it. No proxy servers, no fake-ollama, no Docker containers.

---

## Using Kimi K2 in Python Scripts

If you want to use Kimi K2 in your own code:

### Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install openai python-dotenv
```

### Create .env file

```
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_API_KEY=your-openrouter-api-key-here
```

### Example script (test.py)

```python
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
        {"role": "user", "content": "Write a Python function to calculate factorial."},
    ],
)
print(response.choices[0].message.content)
```

---

## Summary

| Apidog Tutorial | Reality |
|-----------------|---------|
| Need fake-ollama proxy server | VSCode Copilot connects to OpenRouter directly |
| `pip install` and `python main.py` | fake-ollama is Go, not Python |
| Complex multi-step setup | Just select OpenRouter in Copilot and enter API key |
