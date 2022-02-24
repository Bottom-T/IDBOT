import os
from trakos import * 
from time import sleep
from user_agent import generate_user_agent
#1
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
 
Telegram = Client(
    "Telegram ID Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]


@Telegram.message_handler(commands=['start'])
def start(message):
r = requests.session()
    first = message.from_user.first_name
    Telegram.send_message(message.chat.id, text=f"**Hi {first},Send Text To Write Him At Book! \n\nBy @us7a5 **",parse_mode="markdown")
@Telegram.message_handler(func=lambda m: True)
def Get(message):
    Telegram.send_message(message.chat.id,f"<strong>Wait Please.</strong>",parse_mode="html") 
    msg = message.text
    url = f"http://apis.xditya.me/write?text={msg}"
    Telegram.send_photo(message.chat.id,url,caption=f"<strong>Done\n@us7a5</strong>",parse_mode="html")

        

Telegram.run()
