# DeepRoute API — One API Key for DeepSeek & Qwen

> **OpenAI-compatible API relay. No credit card required. PayPal accepted.**

[![DeepSeek](https://img.shields.io/badge/DeepSeek-V4%20Flash%20%7C%20V4%20Pro%20%7C%20R1-blue)]()
[![Qwen](https://img.shields.io/badge/Qwen-Max%20%7C%20Turbo%20%7C%20Plus%20%7C%20Flash-orange)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## Why DeepRoute?

| Pain Point | Solution |
|------------|----------|
| Need a credit card for every AI provider | **PayPal accepted, no card needed** |
| Multiple API keys for different models | **One key for all models** |
| Network issues accessing foreign APIs | **Stable global + China direct access** |
| Minimum deposits and monthly commitments | **Pay-as-you-go, no minimum** |

---

## Supported Models

| Model | Input ($/1M) | Output ($/1M) | Context |
|-------|:-----------:|:------------:|:-------:|
| **DeepSeek V4 Flash** | $0.16 | $0.32 | 128K |
| **DeepSeek V4 Pro** | $2.00 | $4.00 | 128K |
| **DeepSeek V3 (Chat)** | $0.16 | $0.32 | 64K |
| **DeepSeek R1** | $0.63 | $2.52 | 64K |
| **Qwen Max** | $0.87 | $2.60 | 32K |
| **Qwen Turbo** | $0.26 | $0.52 | 1M |
| **Qwen Plus** | $0.78 | $1.56 | 131K |
| **Qwen3.6 Flash** | $0.30 | $1.79 | 128K |
| **Qwen3.7 Max** | $3.00 | $9.00 | 128K |
| **QwQ Plus** | $0.95 | $2.85 | 32K |
| **QwQ 32B Preview** | $0.55 | $1.64 | 32K |

---

## Quick Start

### Python

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://deeproute-api.duckdns.org/v1",
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
curl https://deeproute-api.duckdns.org/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{"model": "deepseek-v4-flash", "messages": [{"role": "user", "content": "Hello!"}]}'
```

### Node.js

```javascript
import OpenAI from 'openai';
const client = new OpenAI({
  baseURL: 'https://deeproute-api.duckdns.org/v1',
  apiKey: 'your-api-key'
});
const stream = await client.chat.completions.create({
  model: 'deepseek-v4-flash',
  messages: [{role: 'user', content: 'Hello!'}],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || '');
}
```

---

## How to Buy

1. **Register** → [deeproute-api.duckdns.org/register](https://deeproute-api.duckdns.org/register) — free trial
2. **Get your API key** from dashboard
3. **Top up** via PayPal to `m15828417588@163.com`
4. **Start coding** — quota added within minutes

---

## Why Not Official Providers?

| | **DeepRoute** | DeepSeek Official | OpenRouter |
|---|:---:|:---:|:---:|
| Credit Card Required | **No** | Yes | Yes |
| PayPal Accepted | **Yes** | No | No |
| Minimum Deposit | **None** | Yes | None |
| Single Key for All Models | **Yes** | No | Yes |
| Telegram Support | **Yes** | Ticket | Forum |
| DeepSeek V4 Flash | $0.16/$0.32 | $0.14/$0.28 | $0.14/$0.28 |
| Qwen Max | $0.87/$2.60 | — | $1.60/$6.40 |

---

## Features

- ✅ OpenAI-compatible — works with any OpenAI SDK
- ✅ Streaming support — SSE server-sent events
- ✅ No credit card — PayPal only
- ✅ No minimum — load exactly what you need
- ✅ Multi-model — switch by changing one parameter
- ✅ Stable uptime — enterprise infrastructure

---

## Support

- **Telegram:** [@DeepRouteCN](https://t.me/DeepRouteCN)
- **Email:** m15828417588@163.com

---

## FAQ

**Q: Is the API compatible with OpenAI's SDK?**
A: Yes. Drop-in replacement — just change `base_url` and `api_key`.

**Q: Can I use it from China?**
A: Yes. Direct connection available, no VPN required.

**Q: How fast is quota added after PayPal?**
A: Minutes during business hours. Contact @DeepRouteCN for instant.

**Q: Do you offer refunds?**
A: Yes — contact us within 7 days for unused quota refunds.

---

## License

MIT
