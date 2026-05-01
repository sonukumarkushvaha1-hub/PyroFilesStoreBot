import os

class Config(object):
    # 1. API Credentials (my.telegram.org se)
    API_ID = int(os.environ.get("API_ID", "32460404"))
    API_HASH = os.environ.get("API_HASH", "410d526521ae7dcc474e0f4246788560")
    
    # 2. Bot Credentials (@BotFather se)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8583460812:AAFg5QveoCDIzUhxytPQzgSpGfBDhGhw9s8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "hdsssssa_bot")
    # Aapki Telegram User ID (Numeric)
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5569039254"))
    
    # 3. Database Settings (MongoDB)
    # Aapka naya clean URL jo aapne bheja tha
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sonukumarkushvaha1_db_user:Hwsb4hIkZ71eeApp@cluster0.2eu5lot.mongodb.net/?appName=Cluster0")
    # Storage Channel ID (Jahan files save hongi)
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003626737474"))
    # Database ka naam (Optional)
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    
    # 4. Force Subscribe Settings
    # The Film Club Channel ID
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003544601199")
    # Log Channel ID (Aap apni ya DB channel ki ID daal sakte hain)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003626737474"))
    
    # 5. UI/UX & Logic Settings
    FORWARD_AS_COPY = True
    BROADCAST_AS_COPY = True
    # Banned users ki list (Khali rakhein abhi)
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split() if x.isdigit())
    
    # 6. Customizable Texts
    HOME_TEXT = """
Hi [{}](tg://user?id={})

Main **The Film Club** ka official File Store Bot hoon.
Mujhe koi bhi file bhejein, main uska permanent link bana dunga.

**Main Features:**
* Permanent Link Generation
* Force Subscribe Enabled
* High-Speed File Sharing
"""
