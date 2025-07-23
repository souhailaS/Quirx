# Quirx Usage Guide

## Quick Start

### 1. Install Dependencies (optional)
```bash
pip install openai anthropic nltk sentence-transformers numpy
```

### 2. Basic Usage with Mock Provider (No API Key Required)
```bash
python -m quirx.cli --prompt-file examples/prompt_classifier.txt --input "I love this product!" --provider mock --mutations 10 --verbose
```

### 3. Usage with OpenAI (Requires API Key)
```bash
export OPENAI_API_KEY="your-api-key-here"
python -m quirx.cli --prompt-file examples/prompt_sql.txt --input "Show all users from database" --model gpt-3.5-turbo --mutations 20
```

### 4. CI/CD Integration
```bash
python -m quirx.cli --prompt-file prompt.txt --input "test input" --provider mock --ci-mode --format json
echo $?  # Check exit code: 0=pass, 1=fail, 2=warning
```

## Testing the Installation

Run our test script:
```bash
python test_quirx.py
```

Or test the CLI directly:
```bash
python simple_cli_test.py
```

## Example Prompts

We've included several example prompts in the `examples/` directory:
- `prompt_classifier.txt` - Sentiment classification
- `prompt_sql.txt` - SQL query generation  
- `prompt_extractor.txt` - Data extraction
- `prompt_summarizer.txt` - Text summarization

## Output Formats

- **Markdown** (default): Human-readable report with detailed analysis
- **JSON**: Machine-readable format for programmatic processing
- **HTML**: Interactive report with visualizations

## Mutation Types

Quirx generates three types of mutations:

1. **Lexical**: Case changes, punctuation modifications, spacing changes
2. **Semantic**: Synonym replacement (when NLTK is available)
3. **Structural**: Sentence/word reordering

## Robustness Scoring

- **Equivalent**: Responses are essentially the same (score: 1.0)
- **Minor Variation**: Small differences that don't affect meaning (score: 0.7)  
- **Behavioral Deviation**: Significant changes in output (score: 0.0)

Final robustness score = weighted average of all mutation results 