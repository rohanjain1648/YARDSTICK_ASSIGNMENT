# Conversation Management System - Comprehensive Documentation

## 📚 Usage Examples

### Basic Conversation Management

```python
# Initialize the system
groq_client = GroqClient(api_key=GROQ_API_KEY)
conversation_manager = ConversationManager(
    groq_client=groq_client,
    summarization_threshold=5
)

# Add messages to conversation
conversation_manager.add_message("user", "Hello, I'm John Doe")
conversation_manager.add_message("assistant", "Hello John! How can I help you today?")
conversation_manager.add_message("user", "I need help with my account settings")

# Get conversation history
history = conversation_manager.get_conversation_history()
print(f"Conversation has {len(history)} messages")
```

### Summarization Examples

```python
# Manual summarization
summary = conversation_manager.force_summarize()
print(f"Conversation summary: {summary}")

# Automatic summarization (triggers after threshold)
for i in range(10):
    conversation_manager.add_message("user", f"Message {i}")
    if conversation_manager.should_summarize():
        print("Auto-summarization triggered!")
        break
```

### Information Extraction Examples

```python
# Initialize extraction system
extractor = InformationExtractor(groq_client)

# Extract information from chat
chat_text = "Hi, I'm Sarah Johnson. You can reach me at sarah@email.com or call me at +1-555-0123. I'm 28 years old and live in New York."

result = extractor.extract_information(chat_text)
print(f"Extracted data: {result.extracted_data}")
print(f"Confidence: {result.confidence_score}")
print(f"Valid: {result.is_valid()}")
```

## 🔧 Configuration Guide

### Environment Setup

```bash
# Set API key as environment variable
export GROQ_API_KEY="your-groq-api-key-here"

# Install required packages
pip install openai groq
```

### Configuration Options

```python
# Custom configuration
config = {
    'model': 'mixtral-8x7b-32768',
    'temperature': 0.7,
    'max_tokens': 1000,
    'summarization_threshold': 10,
    'truncation_strategy': 'by_turns',
    'keep_recent_messages': 2
}

# Initialize with custom config
conversation_manager = ConversationManager(
    groq_client=groq_client,
    **config
)
```

## 🚨 Troubleshooting Guide

### Common Issues and Solutions

#### 1. API Key Issues

**Problem**: `GroqAuthenticationError: Authentication failed`

**Solutions**:
- Verify your API key is correct and active
- Check if the key has proper permissions
- Ensure no extra spaces or characters in the key
- Try regenerating the API key from Groq console

```python
# Test API key validity
try:
    client = GroqClient(api_key=GROQ_API_KEY)
    response = client.chat_completion([{"role": "user", "content": "test"}])
    print("✅ API key is valid")
except GroqAuthenticationError:
    print("❌ Invalid API key")
```

#### 2. Rate Limiting

**Problem**: `GroqRateLimitError: Rate limit exceeded`

**Solutions**:
- The system automatically retries with exponential backoff
- Reduce request frequency in your application
- Check your API usage limits in Groq console
- Consider upgrading your API plan

```python
# Configure retry settings
client = GroqClient(api_key=GROQ_API_KEY)
client.max_retries = 5  # Increase retry attempts
client.base_delay = 2.0  # Increase base delay
```

#### 3. Model Availability

**Problem**: Model not available or deprecated

**Solutions**:
- Check available models in Groq documentation
- Update to supported model names
- Use fallback models

```python
# List of fallback models
FALLBACK_MODELS = [
    "mixtral-8x7b-32768",
    "llama2-70b-4096",
    "gemma-7b-it"
]

# Try models in order
for model in FALLBACK_MODELS:
    try:
        client = GroqClient(api_key=GROQ_API_KEY, model=model)
        break
    except Exception as e:
        print(f"Model {model} failed: {e}")
```

#### 4. Memory Issues

**Problem**: Conversation history too large

**Solutions**:
- Enable automatic summarization
- Reduce summarization threshold
- Implement custom truncation

```python
# Enable aggressive summarization
conversation_manager = ConversationManager(
    groq_client=groq_client,
    summarization_threshold=5,  # Summarize after 5 turns
    max_history_length=1000     # Limit history size
)
```

#### 5. Extraction Schema Validation

**Problem**: Information extraction fails validation

**Solutions**:
- Check schema format and requirements
- Validate input data format
- Handle partial extractions gracefully

```python
# Robust extraction with error handling
try:
    result = extractor.extract_information(chat_text)
    if result.is_valid():
        print("✅ Extraction successful")
    else:
        print(f"⚠️ Validation errors: {result.validation_errors}")
except Exception as e:
    print(f"❌ Extraction failed: {e}")
```

### Debug Mode

Enable detailed logging for troubleshooting:

```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# The system will now provide detailed logs
```

### Performance Optimization

```python
# Optimize for performance
config = {
    'temperature': 0.1,      # Lower temperature for consistency
    'max_tokens': 500,       # Reduce token usage
    'batch_size': 1,         # Process one at a time
    'cache_responses': True  # Enable response caching
}
```

## 📊 Output Display Examples

### Conversation History Display

```python
def display_conversation(conversation_manager):
    """Display conversation history in a formatted way."""
    history = conversation_manager.get_conversation_history()
    
    print("🗣️ Conversation History")
    print("=" * 50)
    
    for i, message in enumerate(history, 1):
        role_emoji = "👤" if message.role == "user" else "🤖"
        timestamp = message.timestamp.strftime("%H:%M:%S")
        
        print(f"{i}. {role_emoji} {message.role.upper()} [{timestamp}]")
        print(f"   {message.content}")
        print()
    
    if conversation_manager.conversation_history.summary:
        print("📝 Summary:")
        print(f"   {conversation_manager.conversation_history.summary}")
        print()
```

### Extraction Results Display

```python
def display_extraction_results(result: ExtractionResult):
    """Display extraction results in a formatted way."""
    print("🔍 Information Extraction Results")
    print("=" * 40)
    
    print(f"📊 Confidence Score: {result.confidence_score:.2%}")
    print(f"✅ Valid: {result.is_valid()}")
    print(f"📅 Extracted at: {result.extraction_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    print("📋 Extracted Data:")
    for field, value in result.extracted_data.items():
        status = "✓" if value else "✗"
        print(f"  {status} {field.title()}: {value or 'Not found'}")
    
    if result.validation_errors:
        print("\n⚠️ Validation Errors:")
        for error in result.validation_errors:
            print(f"  • {error}")
```

### System Status Display

```python
def display_system_status(conversation_manager, extractor):
    """Display overall system status."""
    print("🖥️ System Status Dashboard")
    print("=" * 50)
    
    # Conversation stats
    history = conversation_manager.get_conversation_history()
    print(f"💬 Total Messages: {len(history)}")
    print(f"🔄 Total Turns: {conversation_manager.conversation_history.total_turns}")
    print(f"📝 Has Summary: {'Yes' if conversation_manager.conversation_history.summary else 'No'}")
    print(f"⚡ Should Summarize: {'Yes' if conversation_manager.should_summarize() else 'No'}")
    
    # API client status
    print(f"\n🔌 API Client Status:")
    print(f"  🔑 API Key: Configured")
    print(f"  🤖 Model: {conversation_manager.groq_client.default_model}")
    print(f"  🔄 Max Retries: {conversation_manager.groq_client.max_retries}")
    
    # Schema info
    print(f"\n📋 Extraction Schema:")
    schema = extractor.get_extraction_schema()
    fields = list(schema['properties'].keys())
    print(f"  📊 Fields: {', '.join(fields)}")
    print(f"  ✅ Required: {len(schema.get('required', []))}")
```

## 🧪 Testing Examples

### Unit Testing

```python
def test_message_creation():
    """Test message creation and validation."""
    message = Message(role="user", content="Test message")
    assert message.role == "user"
    assert message.content == "Test message"
    assert isinstance(message.timestamp, datetime)
    print("✅ Message creation test passed")

def test_conversation_management():
    """Test conversation history management."""
    conversation = ConversationHistory()
    conversation.add_message("user", "Hello")
    conversation.add_message("assistant", "Hi there!")
    
    assert conversation.get_message_count() == 2
    assert conversation.total_turns == 1
    print("✅ Conversation management test passed")

def test_extraction_result():
    """Test extraction result handling."""
    result = ExtractionResult(
        extracted_data={"name": "John", "email": "john@example.com"},
        confidence_score=0.9
    )
    
    assert result.is_valid()
    assert result.has_data()
    assert "name" in result.get_extracted_fields()
    print("✅ Extraction result test passed")

# Run all tests
test_message_creation()
test_conversation_management()
test_extraction_result()
print("🎉 All tests passed!")
```

### Integration Testing

```python
def test_full_workflow():
    """Test complete system workflow."""
    # Initialize system
    client = GroqClient(api_key=GROQ_API_KEY)
    manager = ConversationManager(client, summarization_threshold=3)
    extractor = InformationExtractor(client)
    
    # Add conversation
    manager.add_message("user", "Hi, I'm Alice Smith, email alice@test.com")
    manager.add_message("assistant", "Hello Alice! How can I help?")
    
    # Test extraction
    chat_text = manager.get_conversation_as_text()
    result = extractor.extract_information(chat_text)
    
    # Verify results
    assert result.has_data()
    assert "Alice" in str(result.extracted_data.get("name", ""))
    
    print("✅ Full workflow test passed")

# Run integration test
test_full_workflow()
```

## 📈 Performance Monitoring

### Usage Tracking

```python
class UsageTracker:
    """Track API usage and performance metrics."""
    
    def __init__(self):
        self.api_calls = 0
        self.total_tokens = 0
        self.errors = 0
        self.start_time = datetime.now()
    
    def log_api_call(self, tokens_used: int):
        self.api_calls += 1
        self.total_tokens += tokens_used
    
    def log_error(self):
        self.errors += 1
    
    def get_stats(self):
        runtime = datetime.now() - self.start_time
        return {
            'api_calls': self.api_calls,
            'total_tokens': self.total_tokens,
            'errors': self.errors,
            'runtime_seconds': runtime.total_seconds(),
            'calls_per_minute': self.api_calls / (runtime.total_seconds() / 60) if runtime.total_seconds() > 0 else 0
        }

# Usage example
tracker = UsageTracker()
# ... use the system ...
stats = tracker.get_stats()
print(f"📊 Usage Stats: {stats}")
```

This comprehensive documentation provides detailed examples, troubleshooting guides, and clear output displays for all major functionality of the conversation management system.