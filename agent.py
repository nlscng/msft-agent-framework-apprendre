import asyncio
from py_compile import main
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent(
    instructions="You are good at telling jokes.",
    name="Joker"
)


# running the agent
async def run_agent():
    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

asyncio.run(run_agent())


# running the agent with streaming
async def run_agent_streaming():
    async for update in agent.run_stream("Tell me a joke about a pirate."):
        if update.text:
            print(update.text, end="", flush=True)
    print()  # New line after streaming is complete

asyncio.run(run_agent_streaming())