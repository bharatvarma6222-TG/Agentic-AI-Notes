from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(city:str)->str:
    """Get the weather of a location"""
    return "it's always cloudy in the tokyo"

if __name__=="__main__":
    mcp.run(transport="streamable-http")