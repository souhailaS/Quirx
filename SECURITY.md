# Security Guidelines for Quirx

## API Key Management

### Secure Storage
- **Use the config file method**: `config/api_keys.env` (ignored by git)
- **Never commit API keys** to version control
- **Use environment variables** in production/CI environments
- **Avoid command line arguments** in shared environments (visible in process lists)

### File Structure
```
config/
├── api_keys.env.sample  ← Template (tracked by git)
├── api_keys.env        ← Your actual keys (ignored by git)
└── README.md           ← Instructions
```

### Best Practices

1. **Copy the sample file**:
   ```bash
   cp config/api_keys.env.sample config/api_keys.env
   ```

2. **Set appropriate file permissions**:
   ```bash
   chmod 600 config/api_keys.env  # Read/write for owner only
   ```

3. **Load securely**:
   ```bash
   source config/api_keys.env
   ```

4. **Verify git ignores the file**:
   ```bash
   git status  # Should not show config/api_keys.env as modified
   ```

### What's Protected by .gitignore

The following files are automatically ignored:
- `config/api_keys.env`
- `.env`
- `*.key`
- `*_key.txt`
- `*_keys.txt`

### CI/CD Environments

For automated testing, use your platform's secret management:

**GitHub Actions:**
```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

**Local Development:**
Always use the configuration file method to avoid accidentally exposing keys.

## Reporting Security Issues

If you discover a security vulnerability, please email: souhaila.serbout@example.com 