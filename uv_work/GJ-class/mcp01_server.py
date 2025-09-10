from mcp.server.fastmcp import FastMCP #MCP 서버 만드는 라이브러리

# Create an MCP server
mcp = FastMCP("GJ-class")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport='stdio')

# 터미널에서 mcp dev mcp01_server.py 로 서버 실행 가능