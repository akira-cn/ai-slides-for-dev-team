import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

async def main():
    agent = Agent(
        task="最近Github上有哪些热门的前端项目？",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())
