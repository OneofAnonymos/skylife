import telebot
from dotenv import load_dotenv
import os

import profile, jobs, skills, travel

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.from_user.id)
    profile.create_user(user_id)
    bot.send_message(message.chat.id, f"   {message.from_user.first_name}!\n  /profile  .")

@bot.message_handler(commands=['profile'])
def show_profile(message):
    user_id = str(message.from_user.id)
    info = profile.get_profile(user_id)
    bot.send_message(message.chat.id, info)

jobs.register(bot)
skills.register(bot)
travel.register(bot)

bot.infinity_polling()