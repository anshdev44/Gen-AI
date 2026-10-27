
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import BaseMessage, HumanMessage
from dotenv import load_dotenv
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

client = MultiServerMCPClient(
    {
        "expense": {
            "transport": "stdio",
            "command": "python",
            "args": [
                r"D:\python\mcp-cleints\mcp-server.py"
            ],
        }
    }
)


async def graph_bulder():
    llm = ChatGroq(model="openai/gpt-oss-120b")
    tools = await client.get_tools()
    llm_with_tools = llm.bind_tools(tools)

    async def chat_node(state: ChatState):
        response = await llm_with_tools.ainvoke(state["messages"])
        return {"messages": [response]}

    graph = StateGraph(ChatState)
    graph.add_node("chat", chat_node)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "chat")
    graph.add_conditional_edges("chat", tools_condition)
    graph.add_edge("tools", "chat")

    final_graph = graph.compile()
    return final_graph


async def main():
    final_graph=graph_bulder()
    result = await final_graph.ainvoke({
        "messages": [
            HumanMessage(content="What is 2 and 3 addition? Use the tool provided.")
        ]
    })

    print(result)

if __name__ == "__main__":
    asyncio.run(main())
