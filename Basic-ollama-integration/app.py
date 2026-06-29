from langchain_ollama import ChatOllama

class App:
    def __init__(self):
        self.llm =  ChatOllama(
                    model="llama3.2:latest",
                    temperature=0)

    def translate(self, text):
        messages  = [("system",
             "You are a helpful assistant that translates English to French. Translate the user sentence.",
              ),
             ("human", text)
        ]

        ai_msg = self.llm.invoke(messages)
        return ai_msg.content
