# Kimi K2 API Example

A simple example of using Moonshot AI's Kimi K2 model via OpenRouter.

## Why Use a Virtual Environment?

A virtual environment isolates your project's dependencies from your system Python and other projects. This prevents:

- **Version conflicts**: Project A needs `openai==1.0` but Project B needs `openai==2.0`? No problem—each has its own isolated packages.
- **System pollution**: Your global Python stays clean. No accumulation of random packages over time.
- **Reproducibility**: Anyone can recreate your exact environment from `requirements.txt`.
- **Easy cleanup**: Delete the `venv` folder and everything is gone. No leftover packages.

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate it

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

You'll see `(venv)` in your terminal prompt when it's active.

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

### 4. Configure your API key

Create a `.env` file (or copy the example):

```
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_API_KEY=your-openrouter-api-key-here
MODEL_NAME=moonshotai/kimi-k2
```

Get your API key from [OpenRouter](https://openrouter.ai/).

### 5. Run the example

```bash
python test.py
```

## Deactivating

When you're done:

```bash
deactivate
```

## Files

- `test.py` - Example script that calls Kimi K2
- `.env` - Your API credentials (never commit this!)
- `.gitignore` - Excludes `.env` and `venv/` from git
