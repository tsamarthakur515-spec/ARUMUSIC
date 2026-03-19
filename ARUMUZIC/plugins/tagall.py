import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

# Ek list taaki hum tag stop kar sakein
TAG_STOP = []

@Client.on_message(filters.command(["tagall", "utag"]) & filters.group)
async def tag_all_members(client: Client, message: Message):
    chat_id = message.chat.id
    
    # Check if user is Admin
    user = await client.get_chat_member(chat_id, message.from_user.id)
    if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("❌ **ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs!**")

    # Tag message extract
    if len(message.command) < 2:
        tag_text = "ʜᴇʏ, ᴡᴀᴋᴇ ᴜᴘ!"
    else:
        tag_text = message.text.split(None, 1)[1]

    if chat_id in TAG_STOP:
        TAG_STOP.remove(chat_id)

    m = await message.reply("✨ **ᴛᴀɢɢɪɴɢ sᴛᴀʀᴛᴇᴅ...**\n`Use /cancel to stop.`")
    
    # Saare members nikalne ke liye
    members = []
    async for member in client.get_chat_members(chat_id):
        if not member.user.is_bot: # Bots ko tag nahi karenge
            members.append(member.user.mention)

    # 5-5 members ka batch banayenge taaki Spam na lage
    count = 0
    text = f"📢 **{tag_text}**\n\n"
    
    for i in range(0, len(members), 5):
        if chat_id in TAG_STOP:
            break
            
        batch = members[i:i+5]
        tag_line = f"{text}" + " ".join(batch)
        
        await client.send_message(chat_id, tag_line)
        count += len(batch)
        
        # 3 second ka gap taaki bot ban na ho (Flood wait safety)
        await asyncio.sleep(3)

    if chat_id in TAG_STOP:
        TAG_STOP.remove(chat_id)
        await message.reply(f"🚫 **ᴛᴀɢɢɪɴɢ sᴛᴏᴘᴘᴇᴅ!**\nᴛᴏᴛᴀʟ ᴛᴀɢɢᴇᴅ: `{count}`")
    else:
        await message.reply(f"✅ **ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛᴀɢɢᴇᴅ!**\nᴛᴏᴛᴀʟ: `{count}`")

@Client.on_message(filters.command(["cancel", "stopall"]) & filters.group)
async def stop_tagging(client, message: Message):
    # Admin check for cancel too
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return
        
    TAG_STOP.append(message.chat.id)
    await message.reply("⏳ **sᴛᴏᴘᴘɪɴɢ ᴛᴀɢɢᴀʟʟ...**")
