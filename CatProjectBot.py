import telebot
import logging
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
telegram_bot_token = env_vars['bot_token']
bot = telebot.TeleBot(telegram_bot_token)


@bot.message_handler(commands=['Cat'])
def send_welcome(message):
	Photo = open('Cat1.jpg', 'rb')
	bot.send_photo(message.chat.id, Photo)

bot.infinity_polling()