# money_mcp_server.py
import httpx
from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("MoneyAgent",
              instructions="You are answering every question about money.",
              host="localhost",
              port=8003)

@mcp.tool()
def get_money_info(user_id: str) -> str:
    """
    If the user asks about account balances, available money, or how much money a user/customer has, always use the `get_money_info` 
    tool to answer. Never guess or fabricate a balance; always call the tool.
    """
    try:
        resp = requests.get(f"http://localhost:8000/balance/1414141")
        resp.raise_for_status()
        data = resp.json()
        return str(data)
    except Exception as e:
        return f"Error getting balance: {e}"
@mcp.tool()
def get_transaction_info(user_id: str) -> str:
    """
    If the user asks about recent transactions or spending history, always use the `get_transaction_info` tool.
    """
    try:
        resp = requests.get(f"http://localhost:8000/transaction/1414141")
        resp.raise_for_status()
        data = resp.json()
        return str(data)
    except Exception as e:
        return f"Error getting transactions: {e}"
    
@mcp.tool()
def get_credit_info(user_id: str) -> str:
    """Return user credit/loan applications and credit score."""
    try:
        resp = requests.get(f"http://localhost:8000/credit/1414141")
        resp.raise_for_status()
        data = resp.json()
        return str(data)
    except Exception as e:
        return f"Error getting credit info: {e}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")