from Badbot import app ,BOT_USERNAME, SUDO_USER
from pyrogram import filters,enums


@app.on_message(filters.command("shizuban") & filters.user(SUDO_USER))
async def ban_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_USERNAME)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.ban_chat_member(chat_id, member.user.id)
                    await msg.reply_text(f"𝐖ʟᴄ 𝐁ᴀʙʏ 😘❤️ {member.user.mention}")                    
            except Exception:
                pass
    else:
        await msg.reply_text(" 𝐁𝐀𝐁𝐘 𝐄𝐒𝐄 𝐌𝐀𝐓 𝐊𝐀𝐑𝐍𝐀 😉❤️ ")  
                                         
    

      

