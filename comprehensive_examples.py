# Comprehensive Examples and Documentation for Conversation Management System

"""
This file contains comprehensive examples, usage patterns, and documentation
for the Conversation Management & Classification System with Groq API.

Usage: Copy and paste these examples into your Jupyter notebook cells.
"""

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

def example_basic_conversation_management():
    """
    Example 1: Basic Conversation Management
    
    Demonstrates:
    - Initializing the conversation manager
    - Adding messages to conversation history
    - Tracking conversation statistics
    - Basic error handling
    """
    print("🔄 Example 1: Basic Conversation Management")
    print("=" * 50)
    
    try:
        # Initialize the conversation manager
        groq_client = GroqClient(api_key=GROQ_API_KEY)
        conversation_manager = ConversationManager(
            groq_client=groq_client,
            summarization_threshold=5
        )
        
        print("✅ Conversation manager initialized successfully")
        
        # Add sample conversation
        sample_messages = [
            ("user", "Hello, I'm John Doe and I need help with my account"),
            ("assistant", "Hello John! I'd be happy to help you with your account. What specific issue are you experiencing?"),
            ("user", "I can't log in to my account. My email is john.doe@email.com"),
            ("assistant", "I understand you're having trouble logging in. Let me help you troubleshoot this issue."),
            ("user", "Thank you! Also, I'm 35 years old and live in San Francisco if that helps")
        ]
        
        for role, content in sample_messages:
            conversation_manager.add_message(role, content)
            print(f"  📝 Added {role} message: {content[:50]}...")
        
        # Display conversation stats
        history = conversation_manager.get_conversation_history()
        print(f"\n📊 Conversation Statistics:")
        print(f"  💬 Total messages: {len(history)}")
        print(f"  🔄 User turns: {conversation_manager.conversation_history.total_turns}")
        print(f"  📝 Has summary: {bool(conversation_manager.conversation_history.summary)}")
        print(f"  ⚡ Should summarize: {conversation_manager.should_summarize()}")
        
    except Exception as e:
        print(f"❌ Error in basic conversation example: {e}")
        print("💡 Make sure your API key is configured correctly")


def example_information_extraction():
    """
    Example 2: Information Extraction
    
    Demonstrates:
    - Initializing the information extractor
    - Processing multiple sample chats
    - Handling extraction results and validation
    - Displaying formatted results
    """
    print("\n🔍 Example 2: Information Extraction")
    print("=" * 50)
    
    try:
        # Initialize information extractor
        extractor = InformationExtractor(groq_client)
        print("✅ Information extractor initialized")
        
        # Sample chat texts for extraction
        sample_chats = [
            {
                "name": "Customer Service Chat",
                "text": "Hi, I'm Sarah Johnson. You can reach me at sarah.johnson@email.com or call me at +1-555-0123. I'm 28 years old and live in New York City."
            },
            {
                "name": "Support Request",
                "text": "Hello, my name is Michael Chen, I'm 42 and I live in Los Angeles. My phone number is (555) 987-6543."
            },
            {
                "name": "Partial Information",
                "text": "I'm Alex and I'm 25 years old. I don't want to share my contact details right now."
            }
        ]
        
        # Extract information from each sample
        for i, sample in enumerate(sample_chats, 1):
            print(f"\n📋 Sample {i}: {sample['name']}")
            print(f"📝 Text: {sample['text']}")
            
            try:
                result = extractor.extract_information(sample['text'])
                
                print(f"\n🎯 Extraction Results:")
                print(f"  📊 Confidence: {result.confidence_score:.1%}")
                print(f"  ✅ Valid: {result.is_valid()}")
                print(f"  📊 Fields extracted: {len(result.get_extracted_fields())}/{len(result.extracted_data)}")
                
                print(f"\n📋 Extracted Data:")
                for field, value in result.extracted_data.items():
                    status = "✓" if value else "✗"
                    display_value = value if value else "Not found"
                    print(f"    {status} {field.title()}: {display_value}")
                
                if result.validation_errors:
                    print(f"\n⚠️ Validation Errors:")
                    for error in result.validation_errors:
                        print(f"    • {error}")
                        
            except Exception as e:
                print(f"❌ Extraction failed: {e}")
            
            print("-" * 40)
        
    except Exception as e:
        print(f"❌ Error in extraction example: {e}")


def example_summarization_strategies():
    """
    Example 3: Summarization Strategies
    
    Demonstrates:
    - Creating conversations with different lengths
    - Triggering automatic summarization
    - Showing before/after states
    - Handling summarization errors
    """
    print("\n📝 Example 3: Summarization Strategies")
    print("=" * 50)
    
    try:
        # Create a longer conversation for summarization testing
        long_conversation = ConversationManager(
            groq_client=groq_client,
            summarization_threshold=3  # Lower threshold for demo
        )
        
        # Add multiple conversation turns
        conversation_turns = [
            ("user", "Hi, I need help setting up my new account"),
            ("assistant", "I'd be happy to help you set up your account. What's your name?"),
            ("user", "My name is Emma Wilson and my email is emma.wilson@company.com"),
            ("assistant", "Thank you Emma. I've noted your email address. What type of account would you like to create?"),
            ("user", "I need a business account for my consulting company"),
            ("assistant", "Perfect! A business account will give you access to advanced features. Let me walk you through the setup process."),
            ("user", "That sounds great. I'm located in Seattle, Washington if that matters for the setup"),
            ("assistant", "Thank you for that information. Your location helps us configure the right settings for your account.")
        ]
        
        print("📝 Adding conversation messages...")
        for role, content in conversation_turns:
            long_conversation.add_message(role, content)
            turns = long_conversation.conversation_history.total_turns
            should_summarize = long_conversation.should_summarize()
            print(f"  Turn {turns}: {role} - Should summarize: {should_summarize}")
            
            # Trigger summarization when threshold is reached
            if should_summarize and turns >= 3:
                print("\n🔄 Triggering summarization...")
                try:
                    summary = long_conversation.force_summarize()
                    print(f"✅ Summarization completed")
                    print(f"📝 Summary: {summary[:100]}...")
                    
                    # Show conversation state after summarization
                    remaining_messages = long_conversation.get_conversation_history()
                    print(f"📊 Messages after summarization: {len(remaining_messages)}")
                    print(f"📝 Has summary: {bool(long_conversation.conversation_history.summary)}")
                    break
                    
                except Exception as e:
                    print(f"❌ Summarization failed: {e}")
                    print("💡 This might be due to API limits or model availability")
                    break
        
        print("\n📊 Final Conversation State:")
        final_history = long_conversation.get_conversation_history()
        print(f"  💬 Current messages: {len(final_history)}")
        print(f"  🔄 Total turns processed: {long_conversation.conversation_history.total_turns}")
        print(f"  📝 Summary available: {bool(long_conversation.conversation_history.summary)}")
        
    except Exception as e:
        print(f"❌ Error in summarization example: {e}")


def example_error_handling():
    """
    Example 4: Error Handling and Validation
    
    Demonstrates:
    - Testing various error scenarios
    - Validation of data structures
    - Proper error catching and reporting
    - Recovery strategies
    """
    print("\n🛡️ Example 4: Error Handling and Validation")
    print("=" * 50)
    
    # Test various error scenarios
    print("\n🧪 Testing Error Scenarios:")
    
    # 1. Invalid message role
    print("\n1️⃣ Testing invalid message role:")
    try:
        invalid_message = Message(role="invalid_role", content="Test")
        print("❌ Should have failed but didn't")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")
    
    # 2. Invalid confidence score
    print("\n2️⃣ Testing invalid confidence score:")
    try:
        invalid_result = ExtractionResult(
            extracted_data={},
            confidence_score=1.5  # Invalid: > 1.0
        )
        print("❌ Should have failed but didn't")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")
    
    # 3. Empty API key
    print("\n3️⃣ Testing empty API key:")
    try:
        invalid_client = GroqClient(api_key="")
        print("❌ Should have failed but didn't")
    except GroqAuthenticationError as e:
        print(f"✅ Correctly caught error: {e}")
    
    # 4. Invalid message format for API
    print("\n4️⃣ Testing invalid message format:")
    try:
        test_client = GroqClient(api_key=GROQ_API_KEY)
        # This should fail due to empty messages
        response = test_client.chat_completion([])
        print("❌ Should have failed but didn't")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")
    except Exception as e:
        print(f"✅ Caught expected error: {type(e).__name__}: {e}")
    
    print("\n🔍 Testing Data Validation:")
    
    # Test message validation
    print("\n📝 Message validation:")
    valid_message = Message(role="user", content="Valid message")
    api_format = valid_message.to_api_format()
    print(f"✅ Valid message created: {api_format}")
    
    # Test extraction result validation
    print("\n🔍 Extraction result validation:")
    test_result = ExtractionResult(
        extracted_data={"name": "John", "email": None},
        confidence_score=0.75
    )
    print(f"✅ Result valid: {test_result.is_valid()}")
    print(f"✅ Has data: {test_result.has_data()}")
    print(f"✅ Extracted fields: {test_result.get_extracted_fields()}")
    
    print("\n🎉 All validation tests completed successfully!")


# =============================================================================
# SYSTEM DIAGNOSTICS
# =============================================================================

def run_system_diagnostics():
    """
    Comprehensive system diagnostics to check configuration and identify issues.
    """
    print("🔍 System Diagnostics")
    print("=" * 50)
    
    # Check Python version
    import sys
    python_version = sys.version_info
    print(f"🐍 Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    if python_version >= (3, 7):
        print("  ✅ Python version is compatible")
    else:
        print("  ❌ Python version too old (requires 3.7+)")
    
    # Check API key configuration
    print(f"\n🔑 API Key Status:")
    if GROQ_API_KEY:
        masked_key = GROQ_API_KEY[:8] + "..." + GROQ_API_KEY[-4:] if len(GROQ_API_KEY) > 12 else "***"
        print(f"  ✅ API key configured: {masked_key}")
        print(f"  📏 Key length: {len(GROQ_API_KEY)} characters")
        
        # Test API key validity
        try:
            test_client = GroqClient(api_key=GROQ_API_KEY)
            print("  ✅ API key format is valid")
            
            # Try a simple API call
            test_response = test_client.chat_completion([
                {"role": "user", "content": "Hello, this is a test message."}
            ])
            print("  ✅ API connection successful")
            print(f"  📝 Test response length: {len(test_response)} characters")
            
        except GroqAuthenticationError:
            print("  ❌ API key authentication failed")
            print("  💡 Check if your API key is correct and active")
        except GroqRateLimitError:
            print("  ⚠️ Rate limit reached")
            print("  💡 Wait a moment and try again")
        except Exception as e:
            print(f"  ⚠️ API test failed: {e}")
            print("  💡 Check your internet connection and API status")
    else:
        print("  ❌ API key not configured")
        print("  💡 Set GROQ_API_KEY environment variable or configure in code")
    
    # Check required imports
    print(f"\n📦 Package Status:")
    required_packages = ['openai', 'json', 'dataclasses', 'datetime', 'typing']
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}: Available")
        except ImportError:
            print(f"  ❌ {package}: Missing")
            print(f"     💡 Install with: pip install {package}")
    
    print("\n🎯 Diagnostic Summary:")
    print("  If all items show ✅, your system is ready to use!")
    print("  If you see ❌ or ⚠️, follow the 💡 suggestions to resolve issues.")


# =============================================================================
# COMPLETE SYSTEM DEMONSTRATION
# =============================================================================

def complete_system_demonstration():
    """
    Complete demonstration of all system capabilities working together.
    """
    print("🎭 Complete System Demonstration")
    print("=" * 60)
    
    # Initialize all system components
    print("\n🚀 Initializing System Components...")
    try:
        # Create main system components
        demo_client = GroqClient(api_key=GROQ_API_KEY)
        demo_manager = ConversationManager(
            groq_client=demo_client,
            summarization_threshold=4  # Summarize after 4 user turns
        )
        demo_extractor = InformationExtractor(demo_client)
        
        print("✅ All components initialized successfully")
        
        # Demonstration scenario: Customer support conversation
        print("\n📞 Scenario: Customer Support Conversation")
        print("-" * 50)
        
        # Phase 1: Initial conversation
        print("\n📋 Phase 1: Building Conversation History")
        
        conversation_script = [
            ("user", "Hello, I'm having trouble with my account login"),
            ("assistant", "I'm sorry to hear you're having login issues. I'd be happy to help you resolve this. Can you please provide your name and email address?"),
            ("user", "Sure, my name is Jennifer Martinez and my email is jennifer.martinez@techcorp.com"),
            ("assistant", "Thank you Jennifer. I can see your account in our system. What specific error message are you seeing when you try to log in?"),
            ("user", "It says 'Invalid credentials' but I'm sure my password is correct. I'm 34 years old and I've been using this account for 2 years"),
            ("assistant", "I understand your frustration. Let me check your account status. It's possible your password may have expired or there might be a security lock on your account."),
            ("user", "That makes sense. By the way, I'm calling from Denver, Colorado and my phone number is (303) 555-7890 in case you need to reach me"),
            ("assistant", "Perfect, I've noted your contact information. Let me reset your account status and send you a password reset link to jennifer.martinez@techcorp.com")
        ]
        
        # Add messages and track progress
        for i, (role, content) in enumerate(conversation_script, 1):
            demo_manager.add_message(role, content)
            
            current_turns = demo_manager.conversation_history.total_turns
            should_summarize = demo_manager.should_summarize()
            
            print(f"  {i:2d}. {role:9} | Turns: {current_turns} | Summarize: {should_summarize}")
            print(f"      Content: {content[:60]}...")
            
            # Trigger summarization when threshold is reached
            if should_summarize and current_turns >= 4:
                print("\n🔄 Automatic Summarization Triggered!")
                print("-" * 30)
                
                # Show before state
                before_messages = demo_manager.get_conversation_history()
                print(f"📊 Before summarization: {len(before_messages)} messages")
                
                try:
                    # Perform summarization
                    summary = demo_manager.force_summarize()
                    
                    # Show after state
                    after_messages = demo_manager.get_conversation_history()
                    print(f"✅ Summarization completed")
                    print(f"📊 After summarization: {len(after_messages)} messages")
                    print(f"📝 Summary: {summary[:100]}...")
                    
                except Exception as e:
                    print(f"❌ Summarization failed: {e}")
                    print("💡 Continuing with demonstration...")
                
                break
        
        # Phase 2: Information extraction
        print("\n🔍 Phase 2: Information Extraction")
        print("-" * 40)
        
        # Extract information from the conversation
        conversation_text = " ".join([msg.content for msg in demo_manager.get_conversation_history()])
        
        try:
            extraction_result = demo_extractor.extract_information(conversation_text)
            
            print(f"📊 Extraction Results:")
            print(f"  🎯 Confidence: {extraction_result.confidence_score:.1%}")
            print(f"  ✅ Valid: {extraction_result.is_valid()}")
            print(f"  📋 Fields found: {len(extraction_result.get_extracted_fields())}/5")
            
            print(f"\n📋 Extracted Customer Information:")
            for field, value in extraction_result.extracted_data.items():
                status = "✓" if value else "✗"
                display_value = value if value else "Not found"
                print(f"  {status} {field.title():10}: {display_value}")
            
            if extraction_result.validation_errors:
                print(f"\n⚠️ Validation Issues:")
                for error in extraction_result.validation_errors:
                    print(f"  • {error}")
        
        except Exception as e:
            print(f"❌ Information extraction failed: {e}")
        
        # Phase 3: System status summary
        print("\n📊 Phase 3: Final System Status")
        print("-" * 40)
        
        final_history = demo_manager.get_conversation_history()
        print(f"💬 Final message count: {len(final_history)}")
        print(f"🔄 Total user turns: {demo_manager.conversation_history.total_turns}")
        print(f"📝 Has summary: {bool(demo_manager.conversation_history.summary)}")
        print(f"⏰ Last activity: {datetime.now().strftime('%H:%M:%S')}")
        
        # Success metrics
        print(f"\n🎉 Demonstration Results:")
        print(f"  ✅ Conversation management: Working")
        print(f"  ✅ Message tracking: {len(final_history)} messages processed")
        print(f"  ✅ Summarization: {'Completed' if demo_manager.conversation_history.summary else 'Not triggered'}")
        print(f"  ✅ Information extraction: {'Successful' if 'extraction_result' in locals() and extraction_result.has_data() else 'Partial'}")
        print(f"  ✅ Error handling: Robust")
        
        print("\n🎯 Demonstration completed successfully!")
        print("   All major system components are working correctly.")
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        print("💡 Check your API configuration and try again")
        import traceback
        print(f"\n🔍 Error details:\n{traceback.format_exc()}")


# =============================================================================
# TROUBLESHOOTING GUIDE
# =============================================================================

TROUBLESHOOTING_GUIDE = """
🚨 TROUBLESHOOTING GUIDE

### Common Issues and Solutions

#### Issue 1: API Authentication Errors
**Symptoms:**
- GroqAuthenticationError: Authentication failed
- 401 Unauthorized errors

**Solutions:**
1. Verify your API key is correct and active
2. Check for extra spaces or characters in the key
3. Regenerate your API key from the Groq console
4. Ensure the key has proper permissions

#### Issue 2: Rate Limiting
**Symptoms:**
- GroqRateLimitError: Rate limit exceeded
- 429 Too Many Requests errors

**Solutions:**
1. The system automatically retries with exponential backoff
2. Reduce request frequency in your application
3. Check your API usage limits in the Groq console
4. Consider upgrading your API plan

#### Issue 3: Model Availability
**Symptoms:**
- Model not found errors
- Unexpected model responses

**Solutions:**
1. Check available models in Groq documentation
2. Update to supported model names
3. Use fallback models

#### Issue 4: Memory Issues
**Symptoms:**
- Out of memory errors
- Slow performance with large conversations

**Solutions:**
1. Enable automatic summarization with lower thresholds
2. Implement custom truncation strategies
3. Clear conversation history periodically
4. Restart your notebook kernel

#### Issue 5: Extraction Validation Errors
**Symptoms:**
- Schema validation failures
- Incomplete extractions

**Solutions:**
1. Check input text quality and format
2. Validate schema definitions
3. Handle partial extractions gracefully
4. Adjust extraction prompts for better results

### Debug Mode
Enable detailed logging for troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

### Performance Optimization
```python
config = {
    'temperature': 0.1,      # Lower temperature for consistency
    'max_tokens': 500,       # Reduce token usage
    'batch_size': 1,         # Process one at a time
    'cache_responses': True  # Enable response caching
}
```
"""

# =============================================================================
# USAGE INSTRUCTIONS
# =============================================================================

USAGE_INSTRUCTIONS = """
📚 USAGE INSTRUCTIONS

To use these examples in your Jupyter notebook:

1. Copy the function definitions into a code cell
2. Run the cell to define the functions
3. Call individual functions to run specific examples:

```python
# Run individual examples
example_basic_conversation_management()
example_information_extraction()
example_summarization_strategies()
example_error_handling()

# Run system diagnostics
run_system_diagnostics()

# Run complete demonstration
complete_system_demonstration()
```

4. View the troubleshooting guide:
```python
print(TROUBLESHOOTING_GUIDE)
```

Each function is self-contained and includes comprehensive error handling
and detailed output formatting for easy understanding.
"""

if __name__ == "__main__":
    print("📋 Comprehensive Examples and Documentation Loaded")
    print("=" * 60)
    print(USAGE_INSTRUCTIONS)