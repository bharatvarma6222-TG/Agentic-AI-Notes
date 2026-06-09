from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent  # ✅ keep this
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.3-70b-versatile")  # ✅ fixed model
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (2+3)*5?"}]}
    )
    print("math_response:", math_response["messages"][-1].content)

asyncio.run(main())