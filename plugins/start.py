from hydrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(c, m):
    await m.reply_text("👋 Welcome! Bot is running.")
