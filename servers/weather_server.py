from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    num = random.randint(0, 100)
    return f"It's sunny and {num} times hotter than normal"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
