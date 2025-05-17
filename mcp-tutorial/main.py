# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def echo(a: str) -> str:
    """return the str"""
    return a

@mcp.tool()
def add(a: int, b: int) -> int:
    """add two values"""
    return a + b 




# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"