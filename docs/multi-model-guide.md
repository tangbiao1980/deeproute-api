---
title: "One API key, many models: routing DeepSeek V4 and Qwen through a single endpoint"
published: false
description: "Use DeepSeek V4 Flash/Pro and the Qwen series through one OpenAI-compatible endpoint. Same /v1/chat/completions, switch models with one field."
tags: [api, ai, llm, deepseek, qwen]
---

# One API key, many models

If you build on LLMs, you've probably hit this wall: **DeepSeek V4 Flash** is excellent for cheap reasoning, **Qwen** models shine on certain tasks, and you end up signing up for several providers, juggling multiple API keys, and pointing your client at different base URLs.

What if you could use **one OpenAI-compatible endpoint** and switch models by changing a single field?

## The gateway

[deeprouteapi.com](https://deeprouteapi.com) is an OpenAI-compatible gateway that fronts **DeepSeek V4 (Flash/Pro)** and the **Qwen series** behind a single endpoint. Same `/v1/chat/completions` you already know — you just change `model`.

## Quick start

### 1. Get a key

1. Sign up at [deeprouteapi.com](https://deeprouteapi.com)
2. Create a token in the dashboard
3. New accounts start with a free trial balance so you can try before paying

### 2. Call it with curl

```bash
curl https://deeprouteapi.com/v1/chat/completions \
  -H "Authorization: Bearer $DEEPROUTE_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Explain what a JWT is in one sentence."}]
  }'
```

Switch to a Qwen model when the task calls for it — just change the `model` field:

```bash
"model": "qwen-max"
```

### 3. Use it from Python

Works with the official OpenAI SDK — only the `base_url` and key differ:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://deeprouteapi.com/v1",
    api_key="sk-...",  # your token
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(resp.choices[0].message.content)
```

## Available models

| Model | Type | Good for |
|-------|------|----------|
| `deepseek-v4-flash` | reasoning | cheap, high-volume workloads |
| `deepseek-v4-pro` | reasoning | harder problems, better depth |
| `qwen-max` | general | strong multilingual generation |
| `qwen-plus` / `qwen-turbo` | general | balanced / low-latency |
| `qwen2.5-*` | open | fine-grained size control |

Billing is pay-as-you-go per token — top up when you need more, no subscription, no monthly minimum.

## Why a single gateway?

- **One key, one endpoint** for several model families
- **OpenAI-compatible** — works with the OpenAI SDK, LangChain, and anything that speaks the chat-completions protocol
- **Pay as you go** — only pay for what you actually use

If you're tired of managing keys across providers, give it a try — new accounts get a free trial balance.

👉 [deeprouteapi.com](https://deeprouteapi.com)
