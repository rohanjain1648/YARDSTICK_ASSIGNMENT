# Requirements Document

## Introduction

This project implements a conversation management system with summarization capabilities and JSON schema-based classification using the Groq API with OpenAI SDK compatibility. The system will manage conversational data, perform intelligent summarization, and extract structured information from user chats without using external frameworks.

## Requirements

### Requirement 1

**User Story:** As a developer, I want to maintain a running conversation history of user-assistant chats, so that I can track the complete context of interactions.

#### Acceptance Criteria

1. WHEN a new conversation message is added THEN the system SHALL store it in the conversation history
2. WHEN retrieving conversation history THEN the system SHALL return all stored messages in chronological order
3. WHEN the conversation history is accessed THEN the system SHALL maintain message metadata including timestamps and roles

### Requirement 2

**User Story:** As a developer, I want to implement conversation summarization with customizable truncation options, so that I can keep conversation history concise while preserving important context.

#### Acceptance Criteria

1. WHEN truncation by conversation turns is requested THEN the system SHALL limit history to the last n messages
2. WHEN truncation by character/word length is requested THEN the system SHALL limit history to specified length constraints
3. WHEN summarization is triggered THEN the system SHALL use Groq API to generate a concise summary of the conversation
4. WHEN summarization options are configured THEN the system SHALL apply the specified truncation method

### Requirement 3

**User Story:** As a developer, I want periodic summarization after every k-th conversation run, so that I can automatically maintain manageable conversation history size.

#### Acceptance Criteria

1. WHEN k conversation runs are completed THEN the system SHALL automatically trigger summarization
2. WHEN periodic summarization occurs THEN the system SHALL replace the original conversation history with the summarized version
3. WHEN the summarization threshold is configurable THEN the system SHALL allow setting custom k values
4. WHEN summarization is performed THEN the system SHALL preserve the most recent unsummarized messages

### Requirement 4

**User Story:** As a developer, I want to demonstrate conversation management functionality with multiple samples, so that I can validate the system works correctly across different scenarios.

#### Acceptance Criteria

1. WHEN multiple conversation samples are provided THEN the system SHALL process each sample correctly
2. WHEN different truncation settings are applied THEN the system SHALL show varied outputs based on the settings
3. WHEN k-th run summarization is demonstrated THEN the system SHALL show summarization occurring at the specified intervals
4. WHEN outputs are displayed THEN the system SHALL clearly show the before and after states

### Requirement 5

**User Story:** As a developer, I want to create a JSON schema for extracting specific information from chats, so that I can structure and validate extracted data.

#### Acceptance Criteria

1. WHEN a JSON schema is defined THEN it SHALL specify extraction of 5 details: name, email, phone, location, and age
2. WHEN the schema is created THEN it SHALL include proper validation rules for each field type
3. WHEN information extraction is performed THEN the system SHALL use the defined schema for structure validation
4. WHEN extracted data is returned THEN it SHALL conform to the JSON schema format

### Requirement 6

**User Story:** As a developer, I want to use OpenAI function calling with Groq API for structured information extraction, so that I can reliably extract and validate chat information.

#### Acceptance Criteria

1. WHEN function calling is implemented THEN the system SHALL use Groq API's OpenAI-compatible SDK
2. WHEN structured extraction is performed THEN the system SHALL use function calling to enforce JSON schema compliance
3. WHEN extraction fails THEN the system SHALL handle errors gracefully and provide meaningful feedback
4. WHEN multiple extraction attempts are made THEN the system SHALL maintain consistent schema validation

### Requirement 7

**User Story:** As a developer, I want to demonstrate JSON schema classification with sample chats, so that I can validate the extraction accuracy and schema compliance.

#### Acceptance Criteria

1. WHEN at least 3 sample chats are processed THEN the system SHALL extract information from each successfully
2. WHEN extraction results are validated THEN the system SHALL verify outputs against the defined schema
3. WHEN validation errors occur THEN the system SHALL report specific schema violations
4. WHEN demonstration is complete THEN the system SHALL show clear before/after examples with extracted data

### Requirement 8

**User Story:** As a developer, I want the implementation to use only standard Python libraries with Groq API, so that I can avoid framework dependencies while maintaining functionality.

#### Acceptance Criteria

1. WHEN the system is implemented THEN it SHALL use only standard Python libraries plus requests/openai client
2. WHEN Groq API is integrated THEN it SHALL use the OpenAI-compatible SDK for all API interactions
3. WHEN external dependencies are added THEN they SHALL be limited to essential API client libraries only
4. WHEN the code is structured THEN it SHALL demonstrate clean implementation without framework abstractions

### Requirement 9

**User Story:** As a developer, I want the project delivered as a Google Colab notebook with comprehensive documentation, so that I can easily run and understand the implementation.

#### Acceptance Criteria

1. WHEN the notebook is created THEN it SHALL include clean, well-documented code with clear explanations
2. WHEN outputs are generated THEN they SHALL be visible for each task demonstration
3. WHEN API integration is implemented THEN the notebook SHALL include proper API key configuration
4. WHEN the project is complete THEN it SHALL be pushed to GitHub with clean repository structure