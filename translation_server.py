# translation_server.py

from mcp.server.fastmcp import FastMCP
from openai import OpenAI
from langchain_openai import ChatOpenAI
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()



mcp = FastMCP(
    "TranslationAgent",
    instructions="You are a translation agent. You can detect language and translate any text between languages using GPT.",
    host="localhost",
    port=8002
)
client = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

def gpt_call(messages, model="gpt-4o-mini", temperature=None):
    response = client.invoke(messages, model=model, temperature=temperature)
    return response.content.strip()

@mcp.tool()
def detect_language(text: str) -> str:
    """
    Detect the language of the given text (e.g., 'tr', 'en', 'de', 'fr').
    """
    prompt = (
        "Detect the language of the following text. "
        "Respond only with the ISO 639-1 language code (e.g., 'en', 'tr', 'fr', 'de', 'ru', etc.), and nothing else:\n\n"
        f"{text}"
    )
    result = gpt_call([{"role": "user", "content": prompt}])
    # Filter the result to get only a valid two-letter language code
    code = result.strip().lower().replace(".", "").replace("'", "")
    if len(code) > 2:
        code = code[:2]
    return code

@mcp.tool()
def translate(text: str, target_lang: str = "en") -> str:
    """
    Translate the given text to the target language.
    """
    prompt = (
        f"Translate the following text to {target_lang}. "
        "Return only the translated text. Do not explain or add anything else.\n\n"
        f"{text}"
    )
    result = gpt_call([{"role": "user", "content": prompt}])
    return result

if __name__ == "__main__":
    mcp.run(transport="streamable-http")