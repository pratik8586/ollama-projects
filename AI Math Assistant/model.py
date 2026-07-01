from langchain_ollama import ChatOllama
from langchain_core.tools import Tool, tool
from langchain.agents import create_agent

class Model:
    def __init__(self):
        self.llm = ChatOllama(model="qwen3:1.7b")
        # self.llm_with_tool = self.llm.bind_tools([self.add_numbers])
        self.agent = create_agent(model=self.llm, tools=[self.add_numbers, self.multiply_numbers])

    def answer_queries(self, question: str):
        """response = self.llm_with_tool.invoke(text)
        print(response)
        if response.tool_calls:
            result = self.add_numbers.invoke({"inputs": text})
            return result
        return response.content"""
        response = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            },debug=True
        )
        print(response)
        return response["messages"][-1]

    @tool
    def add_numbers( a: int, b: int) -> int:
        """add two numbers"""
        print("Inside add_numbers tool")

        return a+b

    @tool
    def multiply_numbers(a: int, b: int) -> int:
        """Multiply two numbers."""
        print(f"Tool: Multiplying {a} * {b}")
        return a * b





