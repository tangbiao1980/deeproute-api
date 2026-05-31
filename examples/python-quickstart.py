"""DeepRoute API - Python Quickstart
pip install openai
"""
from openai import OpenAI

client = OpenAI(
    base_url="https://deeproute-api.duckdns.org/v1",
    api_key="sk-your-api-key-here"  # Get your key at https://deeproute-api.duckdns.org/register
)

# DeepSeek V4 Flash - cheapest model
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello! What is the capital of France?"}]
)
print(response.choices[0].message.content)

# Switch model by changing model name:
# "deepseek-chat" - DeepSeek V3
# "deepseek-reasoner" - DeepSeek R1
# "qwen3.6-flash" - Qwen3.6 Flash
# "qwen3.7-max" - Qwen3.7 Max
# "qwq-plus" - QwQ Plus
