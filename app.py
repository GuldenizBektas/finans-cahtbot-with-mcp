# app.py

import streamlit as st
import asyncio
from langchain.chat_models import ChatOpenAI
from langgraph.mcp.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="Money Assistant", page_icon="💸")

st.title("💸 Money Assistant")

# MCP Tool server konfigürasyonu
tool_configs = [
    {
        "name": "money_agent",
        "url": "http://localhost:8000/mcp",
        "transport": "streamable_http"
    }
]

# Memory setup
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# Agent setup
@st.cache_resource
def setup_agent():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    client = MultiServerMCPClient(tool_configs)
    tools = asyncio.run(client.get_tools())
    return create_react_agent(
        llm=llm,
        tools=tools,
        memory=st.session_state.memory
    )

agent = setup_agent()

# UI
user_input = st.chat_input("Asistanınıza bir şey sorun...")

if user_input:
    st.chat_message("user").write(user_input)
    with st.chat_message("assistant"):
        result = agent.invoke({"input": user_input})
        st.write(result["output"])