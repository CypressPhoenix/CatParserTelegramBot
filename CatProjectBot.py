import telebot
import os
import logging
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
telegram_bot_token = env_vars['bot_token']
bot = telebot.TeleBot(telegram_bot_token)
Photo = open('./Cat.jpg', 'rb')

@bot.message_handler(commands=['Cat'])
def send_welcome(message):
	Photo = open('./Cat2.jpg', 'rb')
	bot.send_photo(message.chat.id, Photo)

bot.infinity_polling()