import os
import asyncio
from hydrogram import Client, filters
from hydrogram.enums import ChatType
from hydrogram.errors import FloodWait
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# --- Configuration (Aap apni details yahan bharein) ---
class Config:
    API_ID = int(os.environ.get("API_ID", "12345"))
    API_HASH = os.environ.get("API_HASH", "abcdef")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100..."))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TheFilmClubBot")

# --- Bot Initialization ---
# Hydrogram me 'name' use hota hai session_name ki jagah
Bot = Client(
    name=Config.BOT_USERNAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    sleep_threshold=30
)

@Bot.on_message(filters.command("start") & filters.private)
async def start_handler(bot: Client, message: Message):
    await message.reply_text(
        text=f"Hello {message.from_user.mention},\n\nI am a File Store Bot. "
             "Send me any file and I will save it in my database!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("About", callback_data="about")]
        ])
    )

@Bot.on_message((filters.document | filters.video | filters.audio) & ~filters.chat(Config.DB_CHANNEL))
async def main_handler(bot: Client, message: Message):
    # 1. Chat Type Check (Latest Hydrogram Standard)
    if message.chat.type == ChatType.PRIVATE:
        try:
            # File ko DB Channel me copy karna (Server load nahi padega)
            sent_message = await message.copy(chat_id=Config.DB_CHANNEL)
            
            # Link banana (Aapka shareable link logic)
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=file_{sent_message.id}"
            
            await message.reply_text(
                text=f"**File Stored Successfully!**\n\nLink: `{share_link}`",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Share Link", url=share_link)]
                ]),
                quote=True
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            print(f"Error in Private: {e}")

    elif message.chat.type == ChatType.CHANNEL:
        # Channel logic (e.g., automatically storing files sent to specific channels)
        pass

# --- Bot Execution ---
if __name__ == "__main__":
    print("-----------------------")
    print("Bot Started Successfully")
    print("-----------------------")
    Bot.run()
