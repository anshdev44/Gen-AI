# Expense MCP client

Requires Python 3.11 or newer and `uv`.

Install the project dependencies:

```powershell
uv sync
```

Set `GROQ_API_KEY` in a `.env` file. Run the client from this directory:

```powershell
uv run python one.py
```

The client starts `mcp-server.py` over stdio automatically. You do not need to
start the MCP server in a separate terminal.