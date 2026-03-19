# main.py
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
import config

bot = Client(
    "musicbot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins") # 👈 Ye plugins folder ko scan karega
)

assistant = Client(
    "assistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION_STRING
)

call = PyTgCalls(assistant)

async def main():
    print("Starting clients...")
    await bot.start()
    await assistant.start()
    await call.start()
    print("--- BOT STARTED SUCCESSFULLY ---")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
