
from mcp.server import MCPServer

# MCP sunucumuzu oluşturuyoruz
mcp = MCPServer("Hilal MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """İki sayıyı toplar."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Kullanıcıyı ismiyle selamlar."""
    return f"Merhaba {name}! MCP Server çalışıyor!"

if __name__ == "__main__":
    mcp.run(transport="stdio")