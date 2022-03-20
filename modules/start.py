from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start(bot: Client, msg: Message):
    await bot.send_message(msg.chat.id, "Dosya gönderin.")