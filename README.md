# DeepRoute API — One API Key for DeepSeek V4 & Qwen

> **OpenAI-compatible API relay. No credit card required. PayPal accepted.**
>
> 🌐 **Global:** [https://deeprouteapi.com](https://deeprouteapi.com)

[![DeepSeek](https://img.shields.io/badge/DeepSeek-V4%20Flash%20%7C%20V4%20Pro-blue)]()
[![Qwen](https://img.shields.io/badge/Qwen-Max%20%7C%20Plus%20%7C%20Turbo%20%7C%20Flash-orange)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## Why DeepRoute?

| Pain Point | Solution |
|------------|----------|
| Need a credit card for every AI provider | **PayPal accepted, no card needed** |
| Multiple API keys for different models | **One key for all models** |
| Separate accounts per provider | **One gateway, many models** |
| Minimum deposits and monthly commitments | **Pay-as-you-go, no minimum** |

---

## Supported Models

| Model | Input ($/1M) | Output ($/1M) |
|-------|:-----------:|:------------:|
| **DeepSeek V4 Flash** | $0.19 | $0.38 |
| **DeepSeek V4 Pro** | $0.60 | $1.21 |
| **Qwen Max** | $0.88 | $1.75 |
| **Qwen Plus** | $0.44 | $0.88 |
| **Qwen Turbo** | $0.14 | $0.27 |
| **Qwen3.6 Flash** | $0.66 | $1.31 |
| **Qwen3.6 Plus** | $1.07 | $2.14 |
| **Qwen Coder Flash** | $1.42 | $2.85 |
| **Qwen Coder Plus** | $2.14 | $4.27 |
| **Qwen2.5 72B** | $1.10 | $2.19 |
| **Qwen2.5 32B / 14B / 7B** | from $0.11 | from $0.22 |
| **QwQ 32B Preview** | $0.55 | $1.10 |

Pay-as-you-go, no subscription, no minimum deposit.

---

## Quick Start

### Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://deeprouteapi.com/v1",
    api_key="your-api-key"
)
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### cURL

```bash
curl https://deeprouteapi.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{"model": "deepseek-v4-flash", "messages": [{"role": "user", "content": "Hello!"}]}'
```

Switch models by changing the `model` field — `deepseek-v4-flash`, `deepseek-v4-pro`, `qwen-max`, `qwen-plus`, `qwen-turbo`, etc.

---

## How to Buy

1. **Register** → [deeprouteapi.com/register](https://deeprouteapi.com/register) — new accounts get a free trial balance
2. **Get your API key** from the dashboard
3. **Top up** via PayPal — order page: [deeprouteapi.com/order](https://deeprouteapi.com/order)
4. **Start coding** — quota is added automatically after payment

---

## Why Not Just Official Providers?

| | **DeepRoute** | DeepSeek Official | OpenRouter |
|---|:---:|:---:|:---:|
| Credit Card Required | **No** | Yes | Yes |
| PayPal Accepted | **Yes** | No | No |
| Minimum Deposit | **None** | Yes | None |
| Single Key for All Models | **Yes** | No | Yes |
| Telegram Support | **Yes** | Ticket | Forum |
| DeepSeek V4 Flash | $0.19/$0.38 | $0.14/$0.28 | $0.14/$0.28 |
| Qwen Max | $0.88/$1.75 | — | $1.60/$6.40 |

---

## Features

- ✅ OpenAI-compatible — works with any OpenAI SDK
- ✅ Streaming support — SSE server-sent events
- ✅ No credit card — PayPal only
- ✅ No minimum — load exactly what you need
- ✅ Multi-model — switch by changing one parameter
- ✅ Stable uptime — enterprise infrastructure

---

## Guide

Read the full tutorial: [Multi-model gateway guide](docs/multi-model-guide.md)

---

## Support

- **Telegram:** [@DeepRouteCN](https://t.me/DeepRouteCN)
- **Email:** m15828417588@163.com

---

## FAQ

**Q: Is the API compatible with OpenAI's SDK?**
A: Yes. Drop-in replacement — just change `base_url` and `api_key`.

**Q: Can I use it from anywhere?**
A: Yes. [deeprouteapi.com](https://deeprouteapi.com) is globally accessible.

**Q: How fast is quota added after PayPal?**
A: Automatically within minutes via PayPal Instant Payment Notification.

**Q: Do you offer refunds?**
A: Yes — contact us within 7 days for unused quota refunds.

---

## License

MIT
