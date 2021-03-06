import os

from dotenv import load_dotenv

import telebot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')  # Here is your's TELEGRAM BOT API TOKEN
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')  # Here is Chat Id of admin who you want send messages to.

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_instructions(message):
    this_chat_id = message.chat.id
    print(this_chat_id)
    bot.send_message(this_chat_id, "Напишите сообщение, оно будет сразу отправлено админу. Потом с вами свяжиться в лс админ @suicidenjoy")


@bot.message_handler(func=lambda message: True)
def forward_message(message):
    from_chat_id = message.chat.id
    to_chat_id = ADMIN_CHAT_ID
    this_message_id = message.message_id
    bot.forward_message(to_chat_id, from_chat_id, this_message_id)


bot.polling()
