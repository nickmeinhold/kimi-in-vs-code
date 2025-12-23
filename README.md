# Kimi K2 in VSCode Copilot

Use Moonshot AI's Kimi K2 model in VSCode Copilot via OpenRouter.

## Quick Start

1. Get an API key from [OpenRouter](https://openrouter.ai/) (add some credit)
2. In VSCode Copilot, select OpenRouter as provider and enter your key
3. Choose Kimi K2 from the model list

That's it!

## Test Script

Want to test the API directly?

1. Create a `.env` file:
```
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_API_KEY=your-api-key-here
```

2. Install dependencies and run:
```bash
pip install openai python-dotenv
python test.py
```
