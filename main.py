import telebot
import config
import time
from bot_function.chek_message import ChekMessage

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def message_start(message):
    """Начало работы с ботом."""
    time.sleep(300)
    bot.send_message(message.chat.id, 'Начнем игру...')
    quest = 0
    quest_now = ChekMessage(bot)
    quest_now.send_msg(message, quest)


while True:  # Бесконечный цикл проверки
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
