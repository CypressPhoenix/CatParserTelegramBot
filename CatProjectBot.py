import random
import telebot
import logging
from dotenv import dotenv_values
import requests
from bs4 import BeautifulSoup
import wget
import subprocess


env_vars = dotenv_values('.env')
telegram_bot_token = env_vars['bot_token']
bot = telebot.TeleBot(telegram_bot_token)

#def find_cat(command):
#	urlcat = f'https://unsplash.com/s/photos/{command}?license=free'

# @bot.message_handler(commands=['Cat'])
# def send_welcome(message):
# 	command = message.text.split()[0]
# 	Photo = open('Cat1.jpg', 'rb')
# 	bot.send_photo(message.chat.id, Photo)
#

@bot.message_handler(commands=['good-cat'])
def send_good_cat(message):
	command = message.text.split()[0]
	respone = find_cat(command)
	parsed_cat = parsecat(respone)
	cat = random.choice(parsed_cat)
	bot.send_message(message.chat.id, cat)

def find_cat(command):
	urlcat = f'https://unsplash.com/s/photos/{command}?license=free'
	response = requests.get(urlcat)
	html = response.content
	return html

def parsecat(html):
    soup = BeautifulSoup(html, 'html.parser')
    download_links = soup.find_all('a', title='Download photo')
    download_urls = [link['href'] for link in download_links]
    return download_urls

bot.infinity_polling()