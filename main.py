import asyncio
import logging
import sys
from hydrogram import Client, idle, enums
from config import API_ID, API_HASH, BOT_TOKEN

# plugins auto import
import plugins.start
import plugins.admin
import plugins.profile

logging.basicConfig(level=logging.INFO)

app = Client(
    "StoreBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=enums.ParseMode.HTML
)

async def main():
    await app.start()
    me = await app.get_me()

    print(f"🚀 Bot Started: @{me.username}")

    await app.send_message(me.id, "✅ Bot is live!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
