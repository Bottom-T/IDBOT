import os
from trakos import * 
from time import sleep
from user_agent import generate_user_agent
#1
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
 
bot = Client(
    "Telegram ID Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]


START_TEXT = "Hi {first},Send Text To Write Him At Book! \n\nBy @us7a5"



START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/us7a5')
        ]]
    )
#2
msg = message.text
url = f"http://apis.xditya.me/write?text={msg}"

bot_token.send_photo(message.chat.id,url,caption=f"<strong>Done\n@us7a5</strong>",parse_mode="html")




@bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )


Telegram.run()
