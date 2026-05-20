from hydrogram import Client, filters

@Client.on_message(filters.command("profile"))
async def profile(c, m):
    await m.reply_text(f"👤 Your ID: {m.from_user.id}")
