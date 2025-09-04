import telebot
import os
import sys
sys.path.append(os.getcwd())
from config import token
from logic import calculate
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start","help"])
def start(message):
    bot.send_message(message.chat.id, "Я калькулятор бот! Пришли мне выражение, и я его посчитаю.\nПример: `4 * 9 - 5 + 1 / 8`", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    expr = message.text
    result = calculate(expr)
    bot.send_message(message.chat.id, result)

if __name__ == "__main__":
    print("Запуск")
    bot.polling(none_stop=True)