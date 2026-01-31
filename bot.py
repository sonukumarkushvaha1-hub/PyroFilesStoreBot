# (c) @AbirHasan2005

import os
import asyncio
import traceback
# Change pyrogram to hydrogram
from hydrogram import Client, filters
from hydrogram.errors import (
    UserNotParticipant,
    FloodWait,
    QueryIdInvalid
)
from hydrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
# ... keep your other imports same ...

MediaList = {}

# Hydrogram handles the time sync [16] error automatically
Bot = Client(
    name=Config.BOT_USERNAME, # Use 'name' instead of 'session_name'
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=30
)

# Use standard string checks for chat types
@Bot.on_message((filters.document | filters.video | filters.audio) & ~filters.chat(Config.DB_CHANNEL))
async def main(bot: Client, message: Message):
    if str(message.chat.type) == "ChatType.PRIVATE" or message.chat.type == "private":
        # ... your private chat logic ...
        pass
    elif str(message.chat.type) == "ChatType.CHANNEL" or message.chat.type == "channel":
        # ... your channel logic ...
        pass

# Use the standard run command
Bot.run()
