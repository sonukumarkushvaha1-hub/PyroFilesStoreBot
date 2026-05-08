import os
import asyncio
import humanize
from aiohttp import web
from hydrogram import Client, filters
from hydrogram.enums import ChatType
from hydrogram.errors import FloodWait
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from motor.motor_asyncio import AsyncIOMotorClient

# --- 1. CONFIGURATION ---
# It is better to use Environment Variables for security.
class Config:
    API_ID = int(os.environ.get("API_ID", "24193557"))
    API_HASH = os.environ.get("API_HASH", "750435b0d0c64c7406a6401037560da8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002394567890"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TheFilmClubBot")
    MONGODB_URI = os.environ.get("MONGODB_URI", "")

# --- 2. DATABASE SETUP ---
db_client = AsyncIOMotorClient(Config.MONGODB_URI) if Config.MONGODB_URI else None
db = db_client["TheFilmClub_DB"] if db_client else None
files_col = db["stored_files"] if db is not None else None

# --- 3. BOT CLIENT ---
Bot = Client(
    name=Config.BOT_USERNAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    sleep_threshold=30
)

# --- 4. WEB SERVER (For Render Health Checks) ---
async def health_check(request):
    return web.Response(text="Bot Status: Active")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render uses port 8080 by default for Web Services
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

# --- 5. COMMAND HANDLERS ---

@Bot.on_message(filters.command("start") & filters.private)
async def start_cmd(bot: Client, message: Message):
    # Check if user is accessing a stored file link
    if len(message.command) > 1:
        data = message.command[1]
        if data.startswith("file_"):
            msg_id = int(data.split("_")[1])
            try:
                await bot.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=Config.DB_CHANNEL,
                    message_id=msg_id
                )
                return
            except Exception:
                await message.reply_text("❌ Error: This file is no longer available.")
                return

    await message.reply_text(
        text=f"👋 Hello {message.from_user.mention}!\n\nI am **The Film Club** bot. Send me any file, and I will generate a permanent sharing link for you.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Official Channel", url="https://t.me/TheFilmClub")]
        ])
    )

# --- 6. FILE STORAGE HANDLER ---

@Bot.on_message((filters.document | filters.video | filters.audio) & ~filters.chat(Config.DB_CHANNEL))
async def handle_files(bot: Client, message: Message):
    if message.chat.type != ChatType.PRIVATE:
        return

    try:
        # Get media details
        media = message.document or message.video or message.audio
        file_name = getattr(media, "file_name", "File")
        file_size = humanize.naturalsize(media.file_size)

        # Copy file to the database channel
        db_msg = await message.copy(chat_id=Config.DB_CHANNEL)
        
        # Generate the start parameter link
        share_link = f"https://t.me/{Config.BOT_USERNAME}?start=file_{db_msg.id}"

        # Save record to MongoDB
        if files_col is not None:
            await files_col.insert_one({
                "file_name": file_name,
                "msg_id": db_msg.id,
                "file_size": file_size,
                "sender_id": message.from_user.id
            })

        await message.reply_text(
            text=(
                f"✅ **File Stored Successfully!**\n\n"
                f"📄 **Name:** `{file_name}`\n"
                f"⚖️ **Size:** `{file_size}`\n\n"
                f"🔗 **Link:** `{share_link}`"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Share Link", url=share_link)]
            ]),
            quote=True
        )

    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        print(f"Error occurred: {e}")

# --- 7. MAIN RUNNER ---
async def main():
    # Start the web server and the bot simultaneously
    await start_web_server()
    await Bot.start()
    print("Bot is online. Waiting for files...")
    # Keep the script running
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
