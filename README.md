# DeepRoute API — The Cheapest DeepSeek & Qwen API

OpenAI-compatible API relay. No credit card required. PayPal accepted.

## Why DeepRoute?

| Feature | DeepRoute | OpenRouter | DeepSeek Official |
|---------|-----------|------------|-------------------|
| **DeepSeek V4 Flash** | **$0.16/$0.32** | $0.14/$0.28 | $0.14/$0.28 |
| **Qwen-Max** | **$0.87/$2.60** | $1.60/$6.40 | — |
| **Qwen3.6 Flash** | **$0.30/$1.79** | Not available | — |
| **Free Trial** | ✅ Yes | ❌ | ✅ 5M tokens |
| **Credit Card Required** | **No** | Yes | Yes |
| **Payment** | **PayPal** | Credit Card | Credit Card |
| **Support** | **TG + Email** | Forum | Ticket |

## Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|-------------------|--------------------|
| DeepSeek V4 Flash | $0.16 | $0.32 |
| DeepSeek V3 (Chat) | $0.16 | $0.32 |
| DeepSeek R1 | $0.63 | $2.52 |
| DeepSeek V4 Pro | $2.00 | $4.00 |
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

```bash
curl https://deeproute-api.duckdns.org/v1/chat/completions \n  -H "Content-Type: application/json" \n  -H "Authorization: Bearer your-api-key" \n  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## How to Buy

1. **Register** at https://deeproute-api.duckdns.org/register — free trial included
2. **Send PayPal** to m15828417588@163.com
3. **Get quota added** — contact @DeepRouteCN or email m15828417588@163.com

No credit card. No minimum deposit. Pay exactly what you need.

## Contact

- Telegram: @DeepRouteCN
- Email: m15828417588@163.com
