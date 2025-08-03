# app.py
import uuid
from datetime import datetime
import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
#from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.schema.messages import SystemMessage
#from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

# import nest_asyncio
# nest_asyncio.apply()

st.set_page_config(page_title="Money Assistant", page_icon="💸")

st.title("💸 Money Assistant")

PROMPT = """
            You are a multilingual personal finance assistant.
            If the user's question is about account balances, money, or how much money a user/customer has, you must ALWAYS use the `get_money_info` tool. Do NOT answer balance-related queries directly—call the tool!
            If the user's message is not in English, always use the `detect_language` and `translate` tools to translate it to English before answering, and then translate your answer back.
            Call tools even for greetings or uncertain cases.
        """

# MCP Tool server konfigürasyonu
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
if "memory" not in st.session_state:
    memory = ConversationBufferMemory(return_messages=True)
    st.session_state.memory = memory

# Agent setup
@st.cache_resource
def setup_agent():
    llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))
    client = MultiServerMCPClient(tool_configs)
    tools = asyncio.run(client.get_tools())
    checkpointer = InMemorySaver()
    agent = create_react_agent(
        model=llm,
        tools=tools,
        checkpointer=checkpointer,
        prompt=PROMPT)
    return agent

agent = setup_agent()

config = {
        "configurable": {
            "thread_id": str(uuid.uuid4()),
            "thread_ts": str(datetime.utcnow()),
            
        }
    }

# UI
user_input = st.chat_input("Asistanınıza bir şey sorun...")

if user_input:
    st.chat_message("user").write(user_input)
    with st.chat_message("assistant"):
        async def process_stream():
            all_chunks = []
            async for chunk in agent.astream(
                {"messages": [{"role": "user", "content": user_input}]},
                stream_mode="updates", config=config
            ):
                all_chunks.append(chunk)
                print(chunk)
            
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
                st.write(final_response)
            else:
                st.write("İşleminiz tamamlanıyor...")
        
        asyncio.run(process_stream())