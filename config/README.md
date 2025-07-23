# Configuration Directory

This directory contains configuration files for Quirx.

## API Keys Setup

### Quick Setup
1. Copy the sample file:
   ```bash
   cp config/api_keys.env.sample config/api_keys.env
   ```

2. Edit `config/api_keys.env` with your actual API keys:
   ```bash
   nano config/api_keys.env  # or use your preferred editor
   ```

3. Load the environment variables:
   ```bash
   source config/api_keys.env
   ```

4. Run Quirx:
   ```bash
   quirx --prompt-file examples/prompt_classifier.txt --input "I love this!" --provider openai
   ```

### Security Notes

- **`api_keys.env`** - Contains your actual API keys (ignored by git)
- **`api_keys.env.sample`** - Template file (tracked by git)
- Never commit actual API keys to version control
- The `.gitignore` file prevents accidental commits of sensitive files

### Alternative Methods

You can also set environment variables directly:
```bash
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"
```

Or use the command line argument:
```bash
quirx --api-key "your-key-here" --provider openai
``` 