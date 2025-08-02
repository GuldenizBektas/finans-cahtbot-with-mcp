# money_mcp_server.py

from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("MoneyAgent",
              instructions="You are answering every question about money.",
              host="localhost",
              port="8001")

@mcp.tool()
async def get_balance(user_id: str) -> str:
    """
    Lokalde çalışan API'den bir kullanıcının bakiye bilgilerini getir.
    """
    try:
        resp = requests.get(f"http://localhost:8000/balance/{user_id}")
        resp.raise_for_status()
        data = resp.json()
        return f"User {user_id} has a balance of {data['balance']} {data['currency']}"
    except Exception as e:
        return f"Error getting balance: {e}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")