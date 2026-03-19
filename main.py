import asyncio
from pyrogram import idle
from ARUMUZIC.clients import bot, assistant, call # 👈 Clients file se import karo

async def start_bot():
    print("🚀 Starting ARUMUSIC Clients...")
    await bot.start()
    await assistant.start()
    await call.start()
    
    print("---------------------------------")
    print("✨ ARUMUSIC IS NOW ONLINE! ✨")
    print("✅ ALL MODULES LOADED")
    print("---------------------------------")
    
    await idle()
    
    await bot.stop()
    await assistant.stop()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\n🛑 Bot Stopped.")
