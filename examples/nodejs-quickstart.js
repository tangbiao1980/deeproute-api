// DeepRoute API - Node.js Quickstart
// npm install openai
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://deeproute-api.duckdns.org/v1",
  apiKey: "sk-your-api-key-here"  // Get your key at https://deeproute-api.duckdns.org/register
});

async function main() {
  const response = await client.chat.completions.create({
    model: "deepseek-v4-flash",  // Cheapest model: $0.16/1M tokens
    messages: [{ role: "user", content: "Hello! What is the capital of Japan?" }]
  });
  console.log(response.choices[0].message.content);
}
main();
