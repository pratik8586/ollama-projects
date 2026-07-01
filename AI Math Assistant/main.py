from model import Model

if __name__ == '__main__':

    tool  = Model()

    while True:
        question = input("\nAsk me something (type exit to quit): ")

        if question == "exit":
            break
        answer = tool.answer_queries(question)

        print("\nAssistant:", answer)