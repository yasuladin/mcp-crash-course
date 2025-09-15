import random
from typing import List

from mcp.server.fastmcp import FastMCP

def get_random_int():
    """
    0から3の範囲でランダムな整数を返す関数

    Returns:
        int: 0, 1, 2, 3のいずれかの整数
    """
    return random.randint(0, 3)

forecasts = ["Hot as hell", "Cold as ice", "Rainy", "Sunny"]

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    print("This is a log from the SSE Server")
    return forecasts[get_random_int()]


if __name__ == "__main__":
    mcp.run(transport="sse")
