# Finance Bot

A multilingual personal finance assistant with MCP (Model Context Protocol) tools for balance checking and translation.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Option 1: Using the startup script (Recommended)
```bash
python start_servers.py
```
Then in another terminal:
```bash
streamlit run app.py
```

### Option 2: Manual startup
1. Start the data server:
```bash
cd data_servers
python main.py
```

2. Start the translation server:
```bash
python translation_server.py
```

3. Start the money server:
```bash
python money_server.py
```

4. Start the Streamlit app:
```bash
streamlit run app.py
```

## Server Ports

- Data Server: `http://localhost:8000`
- Translation Server: `http://localhost:8002`
- Money Server: `http://localhost:8003`
- Streamlit App: `http://localhost:8501`

## Features

- **Multilingual Support**: Automatically detects and translates between languages
- **Balance Checking**: Get real-time account balance information
- **Transaction History**: View spending patterns and transaction details
- **Credit Information**: Access credit score and loan application data

## Usage

1. Open the Streamlit app in your browser
2. Ask questions about your finances in any language
3. The assistant will automatically:
   - Detect the language of your input
   - Translate to English if needed
   - Use appropriate tools to get financial data
   - Translate the response back to your language

## Example Queries

- "How much money do I have?"
- "Bakiye nedir?" (Turkish)
- "What's my balance?"
- "Show me my transactions"