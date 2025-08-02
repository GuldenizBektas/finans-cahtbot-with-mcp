# app.py
import uuid
from datetime import datetime
import streamlit as st
import asyncio
#from langchain.chat_models import ChatOpenAI
#from langchain_openai import ChatOpenAI
from langchain.schema.messages import SystemMessage
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="Money Assistant", page_icon="💸")

st.title("💸 Money Assistant")

# MCP Tool server konfigürasyonu
# tool_configs = [
#     {
#         "name": "money_agent",
#         "url": "http://localhost:8000/mcp",
#         "transport": "streamable_http"
#     }
# ]

tool_configs = {
    "get_money_info": {
            #"command": "python",
            "url": "http://localhost:8001/mcp",
            #"args": ["./money_server.py"],
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
    #llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key="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")
    llm = init_chat_model("gpt-4o", model_provider="openai", 
                          temperature=0, 
                          api_key="xxx")
    client = MultiServerMCPClient(tool_configs)
    tools = asyncio.run(client.get_tools())
    checkpointer = InMemorySaver()
    agent = create_react_agent(
        model=llm,
        tools=tools,
        checkpointer=checkpointer,
        prompt="You are finance chatbot.")
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
        result = agent.invoke({
        "input": user_input
    }, config)
        print(result)
        output_message = result["messages"][-1]
        st.write(output_message.content)