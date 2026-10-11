
# Python MCP Server

A simple Model Context Protocol (MCP) server built with Python, demonstrating how AI assistants can interact with custom tools.

## Overview

This project explores the Model Context Protocol (MCP), a standardized way to connect AI applications with external tools and services.

The server exposes two tools:

- `add(a, b)`: Adds two numbers.
- `greet(name)`: Returns a personalized greeting.

## Technologies

- Python
- MCP Python SDK
- MCP Inspector
- Cursor IDE / Agent
- STDIO transport

## Project Structure

```text
my-mcp-server/
├── server.py
├── README.md
├── requirements.txt
├── .gitignore
└── .cursor/
    └── mcp.json
```

## Installation

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
python server.py
```

The server communicates through STDIO, so it waits for requests from an MCP client rather than displaying an interactive terminal interface.

## Testing

The server was tested using MCP Inspector and integrated with Cursor Agent.

Both tools were successfully invoked, including a direct MCP tool call from Cursor Agent.

## What I Learned

- MCP client-server architecture
- Tool registration and invocation
- STDIO-based communication
- MCP Inspector testing
- Connecting custom tools to an AI coding assistant

## Future Improvements

- Add more practical tools
- Integrate external APIs
- Explore MCP resources and prompts
- Implement more robust error handling
```
