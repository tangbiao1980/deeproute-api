# DeepRoute API - Affordable DeepSeek & Qwen Access

OpenAI-compatible API relay for DeepSeek and Qwen models at competitive prices.

## Supported Models

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|-------------------|--------------------|
| DeepSeek V4 Flash | $0.16 | $0.32 |
| DeepSeek V4 Pro | $2.00 | $4.00 |
| DeepSeek V3 (Chat) | $0.16 | $0.32 |
| DeepSeek R1 | $0.63 | $2.52 |
| Qwen3.6 Flash | $0.30 | $1.79 |
| Qwen Flash | $0.10 | $0.49 |
| Qwen3.6 Plus | $0.60 | $3.60 |
| Qwen3.7 Max | $3.00 | $9.00 |
| QwQ Plus | $0.95 | $2.85 |
| QwQ 32B Preview | $0.55 | $1.64 |
| Qwen Max | $0.87 | $2.60 |
| Qwen Plus | $0.78 | $1.56 |
| Qwen Turbo | $0.26 | $0.52 |
| Qwen3 Coder Plus | $0.60 | $3.60 |
| Qwen3 Coder Flash | $0.25 | $1.50 |
| Qwen3 VL Flash | $0.65 | $1.95 |

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
curl https://deeproute-api.duckdns.org/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer your-api-key"   -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Register

Get your free API key: https://deeproute-api.duckdns.org/register

New accounts receive free trial credit.
