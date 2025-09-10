from dotenv import load_dotenv
load_dotenv()

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio
from langchain_openai import ChatOpenAI 

async def main():
    client = MultiServerMCPClient(
        {
            "test": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["./mcp02_server.py"],
                "transport": "stdio",
            },
        }
    )
    tools = await client.get_tools()
    llm = ChatOpenAI(model="gpt-4o")
    agent = create_react_agent(llm, tools)
    response = await agent.ainvoke({"messages": "연봉 5천만원 거주자의 소득세는 얼마인가요?"})

    final_message = response['messages'][-1]
    print(final_message)

if __name__ == "__main__":
    asyncio.run(main())

# 새로운 터미널에서 python mcp01_client.py 로 실행
