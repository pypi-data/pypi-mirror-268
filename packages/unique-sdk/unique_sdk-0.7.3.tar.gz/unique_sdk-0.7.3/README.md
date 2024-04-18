# Unique Python SDK

Unique FinanceGPT is a tailored solution for the financial industry, designed to increase productivity by automating manual workloads through AI and ChatGPT solutions.

The Unique Python SDK provides access to the public API of Unique FinanceGPT. It also enables verification of Webhook signatures to ensure the authenticity of incoming Webhook requests.

## Table of Contents

1. [Installation](#installation)
2. [Requirements](#requirements)
3. [Usage Instructions](#usage-instructions)
4. [Webhook Triggers](#webhook-triggers)
5. [Available API Resources](#available-api-resources)
   - [Message](#message)
   - [Chat Completion](#chat-completion)
   - [Search](#search)
   - [Search String](#search-string)
6. [Error Handling](#error-handling)
7. [Examples](#examples)

## Installation

Install UniqueSDK and its peer dependency `requests` via pip using the following commands:

```bash
pip install unique_sdk
pip install requests
```

## Requirements

- Python >=3.11 (Other Python versions 3.6+ might work but are not tested)
- requests (peer dependency. Other HTTP request libraries might be supported in the future)
- Unique App-ID & API Key

Please contact your customer success manager at Unique for your personal developer App-ID & API Key.

## Usage instructions

The library needs to be configured with your Unique `app_id` & `api_key`. Additionally, each individual request must be scoped to a User and provide a `user_id` & `company_id`.

```python
import unique_sdk
unique_sdk.api_key = "ukey_..."
unique_sdk.app_id = "app_..."
```

The SDK includes a set of classes for API resources. Each class contains CRUD methods to interact with the resource.

### Example

```python
import unique_sdk
unique_sdk.api_key = "ukey_..."
unique_sdk.app_id = "app_..."

# list messages for a single chat
messages = unique_sdk.Message.list(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
)

print(messages.data[0].text)
```

## Webhook Triggers

A core functionality of FinanceGPT is the ability for users to engage in an interactive chat feature. SDK developers can hook into this chat to provide new functionalities.

Your App (refer to `app-id` in [Requirements](#requirements)) must be subscribed to each individual Unique event in order to receive a webhook.

Each webhook sent by Unique includes a set of headers:

```yaml
X-Unique-Id: evt_... # Event id, same as in the body.
X-Unique-Signature: ... # A HMAC-SHA256 hex signature of the entire body.
X-Unique-Version: 1.0.0 # Event payload version.
X-Unique-Created-At: 1705960141 # Unix timestamp (seconds) of the delivery time.
X-Unique-User-Id: ... # The user who initiated the message.
X-Unique-Company-Id: ... # The company to which the user belongs.
```

### Success & Retry on Failure

- Webhooks are considered successfully delivered if your endpoint returns a status code between `200` and `299`.
- If your endpoint returns a status code of `300` - `399`, `429`, or `500` - `599`, Unique will retry the delivery of the webhook with an exponential backoff up to five times.
- If your endpoint returns any other status (e.g., `404`), it is marked as expired and will not receive any further requests.

### Webhook Signature Verification

The webhook body, containing a timestamp of the delivery time, is signed with HMAC-SHA256. Verify the signature by constructing the `event` with the `unique_sdk.Webhook` class:

```python
from http import HTTPStatus
from flask import Flask, jsonify, request
import unique_sdk

endpoint_secret = "YOUR_ENDPOINT_SECRET"

@app.route("/webhook", methods=["POST"])
def webhook():
    event = None
    payload = request.data

    sig_header = request.headers.get("X-Unique-Signature")
    timestamp = request.headers.get("X-Unique-Created-At")

    if not sig_header or not timestamp:
        print("⚠️  Webhook signature or timestamp headers missing.")
        return jsonify(success=False), HTTPStatus.BAD_REQUEST

    try:
        event = unique_sdk.Webhook.construct_event(
            payload, sig_header, timestamp, endpoint_secret
        )
    except unique_sdk.SignatureVerificationError as e:
        print("⚠️  Webhook signature verification failed. " + str(e))
        return jsonify(success=False), HTTPStatus.BAD_REQUEST
```

The `construct_event` method will compare the signature and raise a `unique_sdk.SignatureVerificationError` if the signature does not match. It will also raise this error if the `createdAt` timestamp is outside of a default tolerance of 5 minutes. Adjust the `tolerance` by passing a fifth parameter to the method (tolerance in seconds), e.g.:

```python
event = unique_sdk.Webhook.construct_event(
    payload, sig_header, timestamp, endpoint_secret, 0
)
```

### Available Unique Events

#### User Message Created

```json
{
  "id": "evt_...", // see header
  "version": "1.0.0", // see header
  "event": "unique.chat.user-message.created", // The name of the event
  "createdAt": "1705960141", // see header
  "userId": "...", // see header
  "companyId": "...", // see header
  "payload": {
    "chatId": "chat_...", // The id of the chat
    "assistantId": "assistant_...", // The id of the selected assistant
    "text": "Hello, how can I help you?" // The user message
  }
}
```

This webhook is triggered for every new chat message sent by the user. This event occurs regardless of whether it is the first or a subsequent message in a chat. Use the `unique_sdk.Message` class to retrieve other messages from the same `chatId` or maintain a local state of the messages in a single chat.

This trigger can be used in combination with assistants marked as `external`. Those assistants will not execute any logic, enabling your code to respond to the user message and create an answer.

#### External Module Chosen

```json
{
  "id": "evt_...",
  "version": "1.0.0",
  "event": "unique.chat.external-module.chosen",
  "createdAt": "1705960141", // Unix timestamp (seconds)
  "userId": "...",
  "companyId": "...",
  "payload": {
    "name": "example-sdk", // The name of the module selected by the module chooser
    "description": "Example SDK", // The description of the module
    "configuration": {}, // Module configuration in JSON format
    "chatid": "chat_...", // The chat ID
    "assistantId:": "assistant_...", // The assistant ID
    "userMessage": {
      "id": "msg_...",
      "text": "Hello World!", // The user message leading to the module selection
      "createdAt": "2024-01-01T00:00:00.000Z" // ISO 8601
    },
    "assistantMessage": {
      "id": "msg_...",
      "createdAt": "2024-01-01T00:00:00.000Z" // ISO 8601
    }
  }
}
```

This Webhook is triggered when the Unique FinanceGPT AI selects an external module as the best response to a user message. The module must be marked as `external` and available for the assistant used in the chat to be selected by the AI.

Unique's UI will create an empty `assistantMessage` below the user message and update this message with status updates.

**The SDK is expected to modify this assistantMessage with its answer to the user message.**

```python
unique_sdk.Message.modify(
    user_id=user_id,
    company_id=company_id,
    id=assistant_message_id,
    chatId=chat_id,
    text="Here is your answer.",
)
```

## Available API Resources

- [Message](#message)
- [Chat Completion](#chat-completion)
- [Search](#search)
- [Search String](#search-string)

### Message

#### `unique_sdk.Message.list`

Retrieve a list of messages for a provided `chatId`.

```python
messages = unique_sdk.Message.list(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
)
```

#### `unique_sdk.Message.retrieve`

Get a single chat message.

```python
message = unique_sdk.Message.retrieve(
    user_id=user_id,
    company_id=company_id,
    id=message_id,
    chatId=chat_id,
)
```

#### `unique_sdk.Message.create`

Create a new message in a chat.

```python
message = unique_sdk.Message.create(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    assistantId=assistant_id,
    text="Hello.",
    role="ASSISTANT",
)
```

#### `unique_sdk.Message.modify`

Modify an existing chat message.

```python
message = unique_sdk.Message.modify(
    user_id=user_id,
    company_id=company_id,
    id=message_id,
    chatId=chat_id,
    text="Updated message text"
)
```

#### `unique_sdk.Message.delete`

Delete a chat message.

```python
message = unique_sdk.Message.delete(
    message_id,
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
)
```

#### `unique_sdk.Integrated.stream`

Streams the answer to the chat frontend. Given the messages.

if the stream creates [source0] it is referenced with the references from the search context.

E.g.

```
Hello this information is from [srouce1]
```

adds the reference at index 1 and then changes the text to:

```
Hello this information is from <sub>0</sub>
```

```python
unique_sdk.Integrated.chat_stream_completion(
    user_id=userId,
    company_id=companyId,
    assistantMessageId=assistantMessageId,
    userMessageId=userMessageId,
    messages=[
        {
            "role": "system",
            "content": "be friendly and helpful"
        },
        {
            "role": "user",
            "content": "hello"
        }
    ],
    chatId=chatId,

    searchContext=  [
        {
            "id": "ref_qavsg0dcl5cbfwm1fvgogrvo",
            "chunkId": "0",
            "key": "some reference.pdf : 8,9,10,11",
            "sequenceNumber": 1,
            "url": "unique://content/cont_p8n339trfsf99oc9f36rn4wf"
        }
    ],  # optional
    debugInfo={
        "hello": "test"
    }, # optional
    startText= "I want to tell you about: ", # optional
    model= "AZURE_GPT_4_32K_0613", # optional
    timeout=8000,  # optional in ms
    temperature=0.3,  # optional
)
```

**Warning:** Currently, the deletion of a chat message does not automatically sync with the user UI. Users must refresh the chat page to view the updated state. This issue will be addressed in a future update of our API.

### Chat Completion

#### `unique_sdk.ChatCompletion.create`

Send a prompt to an AI model supported by Unique FinanceGPT and receive a result. The `messages` attribute must follow the [OpenAI API format](https://platform.openai.com/docs/api-reference/chat).

```python
chat_completion = unique_sdk.ChatCompletion.create(
    company_id=company_id,
    model="AZURE_GPT_35_TURBO",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ]
)
```

### Search

#### `unique_sdk.Search.create`

Search the Unique FinanceGPT Knowledge database for RAG (Retrieval-Augmented Generation). The API supports vector search and a `searchType` that combines vector and full-text search, enhancing the precision of search results.

These are the options are available for `searchType`:

- `VECTOR`
- `COMBINED`

`limit` (max 1000) and `page` are optional for iterating over results.
`chatOnly` Restricts the search exclusively to documents uploaded within the chat.
`scopeIds` Specifies a collection of scope IDs to confine the search.

```python
search = unique_sdk.Search.create(
    user_id,
    company_id,
    chatId=chat_id
    searchString="What is the meaning of life, the universe and everything?",
    searchType="VECTOR",
    chatOnly=false,
    scopeIds=["scope_..."],
    limit=20,
    page=1
)
```

### Search String

#### `unique_sdk.SearchString.create`

User messages are sometimes suboptimal as input prompts for vector or full-text knowledge base searches. This is particularly true as a conversation progresses and a user question may lack crucial context for a successful search.

This API transforms and translates (into English) the user's message into an ideal search string for use in the [Search.create](#unique_sdksearchcreate) API method.

Adding a `chatId` or `messages` as arguments allows the message history to provide additional context to the search string. For example, "Who is the author?" will be expanded to "Who is the author of the book 'The Hitchhiker's Guide to the Galaxy'?" if previous messages referenced the book.

```python
search_string = unique_sdk.SearchString.create(
    user_id,
    company_id,
    prompt="Was ist der Sinn des Lebens, des Universums und des ganzen Rests?",
    chat_id=chat_id
)
```

## Error Handling

## Examples

An example Flask app demonstrating the usage of each API resource and how to interact with Webhooks is available in our repository at `/examples/custom-assistant`.

## Credits

This is a _fork_ / inspired-by the fantastic Stripe Python SDK (https://github.com/stripe/stripe-python).
