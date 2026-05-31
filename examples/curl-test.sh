#!/bin/bash
# DeepRoute API - cURL Quickstart
# Get your API key at https://deeproute-api.duckdns.org/register

API_KEY="sk-your-api-key-here"

# DeepSeek V4 Flash - cheapest model
curl https://deeproute-api.duckdns.org/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer $API_KEY"   -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Hello! Who are you?"}]
  }'
