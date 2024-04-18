# This is a personal library developed by Qichang Zheng.
## Installation
```bash
pip install qichang
```

## LLM Conversation
### For single conversation
```python
import qichang
llm = qichang.LLM_API()
llm.chat('GPT3.5', 'Hello, how are you?')
llm.chat('GPT4', 'Hello, how are you?')
```

### For multi-turn conversation
#### We currently have two servers in Virginia and Singapore. This function will automatically choose the server with the lowest latency, but you can also manually set the server.
```python
import qichang
llm = qichang.LLM_API()
# Manually set the server
# llm.server = 'Virginia'
# llm.server = 'Singapore'
# Here we need to specify the chatID (string) to distinguish different conversations
llm.chat('GPT3.5', 'Hello, how are you?', 'ChatID')
llm.chat('GPT4', 'What did I just asked?', 'ChatID')
```

## Model Downloader
#### This is a tool to download the huggingface models in China. Note that this function only works for some models, the author is working on further improvement.
```python
import qichang
downloader = qichang.Model_Downloader()
downloader.download('Qwen/Qwen-7B-Chat', 'test') # Download the model to the folder 'test'
```

## Davinci Embedding
### This is a tool to get the embedding of the text from the Davinci model.
```python
import os
import qichang

os.environ["OPENAI_API_KEY"] = "your_api_key"

Embedder = qichang.Embedder()
Embedder.embedding('Hello, how are you?')
```
