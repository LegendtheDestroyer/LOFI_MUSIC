from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ɪ ᴀᴍ 🦋 ˹𝕞ᴇss ꭙ 𝐌ᴜsɪᴄ˼♪ 🦋,

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ 🦋 ˹𝕞ᴇss ꭙ 𝐌ᴜsɪᴄ˼♪ 🦋 ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/TitanXSupport"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://graph.org/file/5dd3cf619ab16866d348c.mp4"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/829d73d62e52f5d945f2e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
