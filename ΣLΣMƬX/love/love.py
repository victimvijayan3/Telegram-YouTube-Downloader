'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from IDLER.Trial import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_message(
    filters.command(
      "love",
      prefixes='/')) 
async def love(
    _,
    ydl: Message
    ):
  usrs = ydl.from_user.first_name
  joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "🍷 Gï†hµß:",
          url="https://github.com/HypeVoidSoul?tab=repositories")]
        ])
  '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
  Aww = f"""
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟

🎈Dear,
Sir,Ma'am  <b>**{usrs}**</b>

ɪꜰ ʏᴏᴜ ʟɪᴋᴇᴅ ᴍʏ ᴘʀᴏᴊᴇᴄᴛ ᴀɴᴅ ᴡᴀɴᴛ ᴛᴏ ʙᴇ ᴀ ɢɪᴛʜᴜʙ ᴄᴏɴᴛʀɪʙᴜᴛᴏʀ ᴛʜᴇɴ:
- 📧ʏᴏᴜ ᴍᴀʏ ᴇᴍᴀɪʟ ᴍᴇ ᴀᴛ `hypevoidsoul@gmail.com`
- 📬ʏᴏᴜ ᴄᴀɴ ᴘᴇʀꜱᴏɴᴀʟ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ @HypeVoidSoul  
- ✨ꜱᴛᴀʀ & ꜰᴏʀᴋ ᴍʏ ɢɪᴛʜᴜʙ ʀᴇᴘᴏ.

ɪꜰ ʏᴏᴜ ʟɪᴋᴇᴅ ᴍʏ ᴘʀᴏᴊᴇᴄᴛ ᴀɴᴅ ᴊᴜꜱᴛ ᴡᴀɴᴛ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ꜱᴍɪʟᴇ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ:
- 🌹 ꜱʜᴀʀᴇ ᴍʏ ʙᴏᴛꜱ @hypevoidlab ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ʜᴀᴘᴘʏ 🌹
    
🍮 ᴛʜᴀɴᴋꜱ ᴀ ʟᴏᴛ ꜰᴏʀ ᴜꜱɪɴɢ ᴍʏ ʙᴏᴛ 🍮

🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
""" 
  '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'     
  await ydl.reply_photo(
        youliurl,
        reply_markup=joinButton,
        caption=Aww
        )
  raise StopPropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
