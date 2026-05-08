import os
import asyncio
import humanize
from aiohttp import web
from hydrogram import Client, filters
from hydrogram.enums import ChatType
from hydrogram.errors import FloodWait
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from motor.motor_asyncio import AsyncIOMotorClient

# --- 1. CONFIG SECTION (Yahan apni details bharein) ---
class Config:
    # Telegram se mili hui API ID (Example: 1234567)
    API_ID = int(os.environ.get("API_ID", "24193557")) 
    
    # Telegram se mila hua API HASH (Example: "abcdef123456...")
    API_HASH = os.environ.get("API_HASH", "750435b0d0c64c7406a6401037560da8")
    
    # BotFather se mila hua BOT TOKEN
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7941235378:AAH0p_Gv2-WXXXXX....")
    
    # Wo channel jahan files save hongi (Starts with -100)
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002394567890"))
    
    # Aapka bot username bina @ ke
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TheFilmClubBot")
    
    # MongoDB Atlas ka link (Agar hai toh, warna khali chhodein)
    MONGODB_URI = os.environ.get("MONGODB_URI", "")

# --- 2. DATABASE ---
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

# --- 4. RENDER HEALTH CHECK SERVER ---
async def health_check(request):
    return web.Response(text="Bot is Alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

# --- 5. HANDLERS ---

@Bot.on_message(filters.command("start") & filters.private)
async def start_cmd(bot: Client, message: Message):
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
                await message.reply_text("❌ Error: File database se delete ho gayi hai.")
                return

    await message.reply_text(
        text=f"👋 Hello {message.from_user.mention}!\n\nMain **The Film Club** bot hoon. Mujhe koi file bhejein, main link bana dunga.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Join Channel", url="https://t.me/TheFilmClub")]
        ])
    )

@Bot.on_message((filters.document | filters.video | filters.audio) & ~filters.chat(Config.DB_CHANNEL))
async def handle_files(bot: Client, message: Message):
    if message.chat.type != ChatType.PRIVATE: return

    try:
        media = message.document or message.video or message.audio
        file_name = getattr(media, "file_name", "File")
        file_size = humanize.naturalsize(media.file_size)

        db_msg = await message.copy(chat_id=Config.DB_CHANNEL)
        share_link = f"https://t.me/{Config.BOT_USERNAME}?start=file_{db_msg.id}"

        if files_col is not None:
            await files_col.insert_one({"file_name": file_name, "msg_id": db_msg.id})

        await message.reply_text(
            text=f"✅ **File Stored!**\n\n📄 **Name:** `{file_name}`\n⚖️ **Size:** `{file_size}`\n\n🔗 **Link:** `{share_link}`",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Share Link", url=share_link)]]),
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        print(f"Error: {e}")

# --- 6. RUN ---
async def main():
    await start_web_server()
    await Bot.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
