# (c) @AbirHasan2005
import os

class Config(object):
    # API Credentials -
    API_ID = int(os.environ.get("API_ID", "32460404"))
    API_HASH = os.environ.get("API_HASH", "410d526521ae7dcc474e0f4246788560")
    
    # Bot Credentials -
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5963477340:AAETOE2Y5BrTqQ25kVp4ERiCNHs3ygR2w6w")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Hinmabot") # यहाँ से @ हटा दिया है
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5569039254")) # आपकी Owner ID
    
    # Database Settings -
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003789755565"))
    # पासवर्ड से < > हटा दिए गए हैं
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://yadavjikibhaish600_db_user:NgUBo6FJiL3cssc4@cluster0.iwrhl8n.mongodb.net/?appName=Cluster0")
    
    # Channel Settings
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003789755565")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    
    # Other Settings
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
    OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
    
    # Texts
    ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database.

🤖 **My Name:** [Files Store Bot](https://t.me/{{BOT_USERNAME}})
📝 **Language:** [Python3](https://www.python.org)
📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
📡 **Hosted on:** [Render](https://render.com)
"""
    ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005
[Donate Now](https://www.paypal.me/AbirHasan2005)
"""
    HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.
Send me any file I will give you a permanent Sharable Link.
"""
