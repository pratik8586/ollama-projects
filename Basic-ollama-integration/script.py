# This is a sample Python script.
import app


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app import App

def call_agent(text):
    bot = App()
    result = bot.translate(text)
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_agent("I love programming")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
