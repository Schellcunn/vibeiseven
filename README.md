# vibeiseven

## Setup Instructions

This project uses the OpenAI API to check if a number is even using a language model. You need to set up your API key and (optionally) the model name as environment variables.

### 1. Obtain an OpenAI API Key
- Sign up or log in at https://platform.openai.com/
- Go to your API keys page and create a new secret key.

### 2. Set Environment Variables

#### On Windows (PowerShell)
```
$env:OPENAI_API_KEY="your-api-key-here"
$env:OPENAI_MODEL="gpt-4.1-mini"  # Optional, defaults to gpt-4.1-mini if not set
```

#### On Linux/macOS (bash)
```
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_MODEL="gpt-4.1-mini"  # Optional, defaults to gpt-4.1-mini if not set
```

You can also add these lines to your shell profile (e.g., `.bashrc`, `.zshrc`, or PowerShell profile) for persistence.

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Usage

Import and use the `vibeiseven` function in your code:

```python
from checker import vibeiseven

result = vibeiseven("42")  # Accepts string or float
print(result)  # True if even, False otherwise
```

---

### 4. Tests
Honestly didnt make those, I dont maintain the API
Works probably, first time also making python packages.