# terminal_money_assistant.py
import uuid
from datetime import datetime
import asyncio
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.schema.messages import SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

PROMPT = """
You are a multilingual personal finance assistant.
- Always answer in the same language as the user's question.
- If the user's question is about account balances, money, or how much money a user/customer has, ALWAYS use the get_money_info tool. Do NOT answer balance-related queries directly—call the tool.
- If the user's question is about transactions, spending history, or purchases, ALWAYS use get_transaction_info.
- If the user's question is about credit cards, loans, or credit score, ALWAYS use get_credit_info.
- For questions not in English, first use detect_language and translate to convert it to English, answer the question, then translate your answer back to the original language.
- Call tools even for greetings or uncertain cases.
"""


# MCP Tool server configuration
tool_configs = {
    "MoneyAgent": {
        "url": "http://localhost:8003/mcp",
        "transport": "streamable_http"
    },
    "TranslationAgent": {
        "url": "http://localhost:8002/mcp",
        "transport": "streamable_http"
    }
}

# Memory setup
memory = ConversationBufferMemory(return_messages=True)

# Agent setup
def setup_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("GITHUB_TOKEN"),
        base_url="https://models.inference.ai.azure.com"
    )
    client = MultiServerMCPClient(tool_configs)
    tools = asyncio.run(client.get_tools())
    checkpointer = InMemorySaver()
    agent = create_react_agent(
        model=llm,
        tools=tools,
        checkpointer=checkpointer,
        prompt=PROMPT
    )
    return agent

agent = setup_agent()

config = {
    "configurable": {
        "thread_id": str(uuid.uuid4()),
        "thread_ts": str(datetime.utcnow()),
    }
}

print("💸 Money Assistant (çıkmak için 'exit')\n")

while True:
    user_input = input("Soru: ").strip()
    if user_input.lower() == "exit":
        print("Görüşürüz! 👋")
        break
    if not user_input:
        continue

    async def process_stream(user_input):
        all_chunks = []
        async for chunk in agent.astream(
            {"messages": [{"role": "user", "content": user_input}]},
            stream_mode="updates",
            config=config
        ):
            all_chunks.append(chunk)
            print(chunk)  # istersen burayı kaldırabilirsin

        # Find the final response from all chunks
        final_response = ""
        for chunk in reversed(all_chunks):
            if 'agent' in chunk and 'messages' in chunk['agent']:
                messages = chunk['agent']['messages']
                for message in messages:
                    if hasattr(message, 'content') and message.content and message.content.strip():
                        final_response = message.content
                        break
                if final_response:
                    break

        if final_response:
            print("\nAssistant:", final_response, "\n")
        else:
            print("Assistant: İşleminiz tamamlanıyor...\n")

    asyncio.run(process_stream(user_input))
