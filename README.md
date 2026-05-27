# DeepRoute API - Affordable DeepSeek & Qwen Access

OpenAI-compatible API relay for DeepSeek and Qwen models at 30-50% cheaper.

## Supported Models

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|-------------------|--------------------|
| DeepSeek-V3 | $0.20 | $0.80 |
| DeepSeek-R1 | $0.45 | $1.80 |
| Qwen-Turbo | $0.12 | $0.40 |
| Qwen-Plus | $0.25 | $0.80 |
| Qwen-Max | $0.60 | $2.00 |
| QwQ-32B | $0.50 | $1.60 |
| Qwen3.5-Plus | $0.30 | $1.00 |
| Qwen3.5-Turbo | $0.15 | $0.50 |

## Quick Start

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://67.216.205.237:3000/v1",
    api_key="your-api-key"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from 'openai';
const openai = new OpenAI({
  baseURL: 'http://67.216.205.237:3000/v1',
  apiKey: 'your-api-key'
});
```

```bash
curl http://67.216.205.237:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Register

Get your free API key: http://67.216.205.237:3000/register

New accounts receive free trial credit.
