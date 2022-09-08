import telebot
import json
import requests

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')

bot = telebot.TeleBot(token)

print("Bot is ready")

@bot.message_handler(commands=['ping'])
def send_welcome(message):
	bot.reply_to(message, "Pong!")

@bot.message_handler(commands=['getip'])
def get_ip(message):
	ip = requests.get('http://ip.42.pl/raw').text
	bot.reply_to(message, f"IP Address succesfully found 🤤" + "\n" + "`{ip}`")
bot.polling()
