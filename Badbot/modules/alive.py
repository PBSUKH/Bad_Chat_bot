from pyrogram import Client, filters
from Badbot import app

# ---------------------------
@app.on_message(filters.command("alive", prefixes="."))
def alive(_, message):
    message.reply_text("**🥀 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Gᴇɴɪᴜs Mᴀsᴛᴇʀ ✨ @II_BAD_MUNDA_II**")
  
