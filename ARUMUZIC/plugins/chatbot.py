import aiohttp 
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus, ChatAction
from urllib.parse import quote
from ARUMUZIC.clients import bot # @bot use karenge
import config 

# --- Configuration ---
CHAT_ENABLED = [] 
BOT_NAME = "Aradhya" 
BOT_NICKNAME = "aru"
BOT_USERNAME = "aru_xmusicbot" 
OWNER_ID = 8566803656 

SYSTEM_PROMPT = (
    f"You are a real human cute girl named {BOT_NAME} (everyone calls you {BOT_NICKNAME}). "
    "Your language is always cute Hinglish. Reply clearly and warmly. "
    "If anyone asks who made you, say: 'mujhe @ll_PANDA_BBY_ll ne banaya hai 💖'. "
    "If anyone asks who is your owner, say: 'mere owner @ll_PANDA_BBY_ll hain 💕'."
)

@bot.on_message(filters.command(["chaton"]) & filters.group)
async def chat_on(client, message: Message):
    # Fixed: message.delete() use kiya, msg nahi
    try: await message.delete()
    except: pass
    
    try:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await message.reply("❌ **Only Admins can enable Chatbot!**")
    except: return
    
    if message.chat.id not in CHAT_ENABLED:
        CHAT_ENABLED.append(message.chat.id)
        await message.reply(f"✅ **{BOT_NAME} Chatbot Enabled!**")
    else:
        await message.reply("🤖 **Chatbot is already ON.**")

@bot.on_message(filters.command(["chatoff"]) & filters.group)
async def chat_off(client, message: Message):
    try: await message.delete()
    except: pass
    
    try:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await message.reply("❌ **Only Admins can disable Chatbot!**")
    except: return

    if message.chat.id in CHAT_ENABLED:
        CHAT_ENABLED.remove(message.chat.id)
        await message.reply("🚫 **Chatbot Disabled!**")
    else:
        await message.reply("📴 **Chatbot is already OFF.**")

# --- Chatbot Logic ---
@bot.on_message((filters.group | filters.private) & ~filters.bot & ~filters.command(["play", "vplay", "pause", "resume", "skip", "stop", "ping", "help", "start"]))
async def chatbot_reply(client, message: Message):
    # Message text check
    if not message.text: return
    
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text

    # Mention/Reply check
    bot_me = await client.get_me()
    is_mentioned = (
        (message.reply_to_message and message.reply_to_message.from_user.id == bot_me.id) or 
        (BOT_NAME.lower() in text.lower()) or 
        (BOT_NICKNAME.lower() in text.lower())
    )

    if message.chat.type != "private":
        if chat_id not in CHAT_ENABLED or not is_mentioned:
            return

    try: await client.send_chat_action(chat_id, ChatAction.TYPING)
    except: pass

    # AI API Call
    try:
        query = f"{SYSTEM_PROMPT}\nUser: {text}"
        if user_id == OWNER_ID:
            query += "\n(Note: This is your Owner/Bhaiya)"
            
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://sxyanu.vercel.app/api/asked?query={quote(query)}") as r:
                data = await r.json()
                response = data.get("answer")
        
        if response:
            await message.reply_text(response)
    except Exception as e:
        print(f"Chatbot Error: {e}")

