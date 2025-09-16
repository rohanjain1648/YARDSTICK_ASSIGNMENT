# 🔑 API Key Setup and Configuration Guide

## Getting Your Groq API Key

### Step 1: Create a Groq Account
1. Visit [https://console.groq.com](https://console.groq.com)
2. Click "Sign Up" to create a new account or "Log In" if you already have one
3. Complete the registration process with your email and verify your account

### Step 2: Access the API Keys Section
1. Once logged in, navigate to your dashboard
2. Look for "API Keys" in the left sidebar or main menu
3. Click on "API Keys" to access the key management section

### Step 3: Generate Your API Key
1. Click "Create API Key" or "Generate New Key"
2. Give your key a descriptive name (e.g., "Conversation Management System")
3. Set appropriate permissions (usually "Full Access" for development)
4. Click "Create" to generate the key
5. **IMPORTANT**: Copy the key immediately - you won't be able to see it again!

### Step 4: Secure Your API Key
- Store the key in a secure location
- Never share your API key publicly
- Don't commit it to version control systems
- Consider using environment variables or secret management systems

## Configuration Methods

### Method 1: Environment Variable (Recommended)

**For Windows:**
```cmd
set GROQ_API_KEY=your-api-key-here
```

**For macOS/Linux:**
```bash
export GROQ_API_KEY="your-api-key-here"
```

**For permanent setup, add to your shell profile:**
```bash
echo 'export GROQ_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Method 2: Google Colab Secrets (For Colab Users)

1. In Google Colab, click the key icon (🔑) in the left sidebar
2. Click "Add new secret"
3. Name: `GROQ_API_KEY`
4. Value: Your actual API key
5. Toggle "Notebook access" to ON
6. Use in code:
```python
from google.colab import userdata
GROQ_API_KEY = userdata.get('GROQ_API_KEY')
```

### Method 3: Direct Assignment (Development Only)

```python
# NOT recommended for production
GROQ_API_KEY = "your-api-key-here"
```

### Method 4: Configuration File

Create a `config.json` file:
```json
{
    "groq_api_key": "your-api-key-here",
    "model": "mixtral-8x7b-32768",
    "temperature": 0.7
}
```

Load in Python:
```python
import json
with open('config.json', 'r') as f:
    config = json.load(f)
GROQ_API_KEY = config['groq_api_key']
```

## Validation and Testing

### Quick API Key Test
```python
# Test your API key
try:
    client = GroqClient(api_key=GROQ_API_KEY)
    response = client.chat_completion([
        {"role": "user", "content": "Hello, this is a test."}
    ])
    print("✅ API key is working correctly!")
    print(f"📝 Response: {response[:100]}...")
except Exception as e:
    print(f"❌ API key test failed: {e}")
```

### Comprehensive Validation
```python
def validate_api_setup():
    """Comprehensive API setup validation."""
    print("🔍 API Setup Validation")
    print("=" * 40)
    
    # Check if key exists
    if not GROQ_API_KEY:
        print("❌ API key not found")
        return False
    
    # Check key format
    if len(GROQ_API_KEY) < 20:
        print("⚠️ API key seems too short")
    
    # Mask key for display
    masked = GROQ_API_KEY[:8] + "..." + GROQ_API_KEY[-4:]
    print(f"✅ API key found: {masked}")
    
    # Test API connection
    try:
        client = GroqClient(api_key=GROQ_API_KEY)
        response = client.chat_completion([
            {"role": "user", "content": "Test message"}
        ])
        print("✅ API connection successful")
        return True
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

# Run validation
validate_api_setup()
```

## Security Best Practices

### ✅ Do's
- Use environment variables for API keys
- Rotate your API keys regularly
- Monitor your API usage in the Groq console
- Use different keys for development and production
- Set up usage alerts and limits
- Store keys in secure secret management systems

### ❌ Don'ts
- Never commit API keys to version control
- Don't share keys in chat messages or emails
- Avoid hardcoding keys in source code
- Don't use production keys for testing
- Never log API keys in application logs
- Don't store keys in plain text files

### Key Rotation Process
1. Generate a new API key in the Groq console
2. Update your environment variables or configuration
3. Test the new key thoroughly
4. Revoke the old key once confirmed working
5. Update any documentation or team members

## Troubleshooting API Key Issues

### Common Problems and Solutions

#### Problem: "Authentication failed" error
**Solutions:**
- Verify the key is copied correctly (no extra spaces)
- Check if the key is still active in Groq console
- Ensure proper permissions are set
- Try regenerating the key

#### Problem: "Rate limit exceeded" error
**Solutions:**
- Check your usage limits in Groq console
- Implement proper rate limiting in your code
- Consider upgrading your API plan
- Use exponential backoff for retries

#### Problem: Key not found in environment
**Solutions:**
- Restart your terminal/IDE after setting environment variables
- Check the exact variable name (case-sensitive)
- Verify the export command syntax
- Try setting the variable in your shell profile

#### Problem: Permission denied errors
**Solutions:**
- Check API key permissions in Groq console
- Ensure your account has necessary access levels
- Verify billing information is up to date
- Contact Groq support if issues persist

## Usage Monitoring

### Track Your API Usage
```python
class APIUsageTracker:
    def __init__(self):
        self.calls = 0
        self.tokens = 0
        self.errors = 0
    
    def log_call(self, tokens_used):
        self.calls += 1
        self.tokens += tokens_used
    
    def log_error(self):
        self.errors += 1
    
    def get_stats(self):
        return {
            'total_calls': self.calls,
            'total_tokens': self.tokens,
            'error_rate': self.errors / max(self.calls, 1)
        }

# Usage
tracker = APIUsageTracker()
# ... make API calls ...
print(f"Usage stats: {tracker.get_stats()}")
```

### Set Up Alerts
- Configure usage alerts in Groq console
- Monitor costs and token usage
- Set up automated notifications for unusual activity
- Implement client-side usage limits

## Support and Resources

### Official Documentation
- [Groq API Documentation](https://console.groq.com/docs)
- [OpenAI SDK Documentation](https://github.com/openai/openai-python)
- [Groq Model Information](https://console.groq.com/docs/models)

### Community Resources
- Groq Discord Community
- Stack Overflow (tag: groq-api)
- GitHub Issues and Discussions

### Getting Help
1. Check the troubleshooting section above
2. Review Groq's official documentation
3. Search community forums for similar issues
4. Contact Groq support through their console
5. Create detailed bug reports with error messages and code samples

---

**Remember**: Your API key is like a password - keep it secure and never share it publicly!