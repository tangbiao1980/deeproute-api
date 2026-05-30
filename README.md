# DeepRoute API - Affordable DeepSeek & Qwen Access

OpenAI-compatible API relay for DeepSeek and Qwen models at 30-50% cheaper.

## Supported Models

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|-------------------|--------------------|
| DeepSeek V4 Flash | $0.16 | $0.32 |
| DeepSeek V3 (Chat) | $0.16 | $0.32 |
| DeepSeek V4 Pro | $2.00 | $4.00 |
| DeepSeek R1 | $0.63 | $2.52 |
| Qwen-Turbo | $0.11 | $0.22 |
| Qwen-Plus | $0.16 | $0.33 |
| Qwen-Max | $0.55 | $1.64 |
| QwQ 32B Preview | $0.55 | $1.64 |

## Quick Start

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://deeproute-api.duckdns.org/v1",
    api_key="your-api-key"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";
const openai = new OpenAI({
  baseURL: "https://deeproute-api.duckdns.org/v1",
  apiKey: "your-api-key"
});
```

```bash
curl https://deeproute-api.duckdns.org/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Register

Get your free API key: https://deeproute-api.duckdns.org/register

New accounts receive free trial credit.