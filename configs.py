import os

class Config(object):
    # --- API Credentials ---
    # Render par 'API_ID' aur 'API_HASH' ke naam se keys honi chahiye
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    
    # --- Bot Credentials ---
    # 'BOT_TOKEN' wahi naya wala jo aapne BotFather se liya
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Haruko_Bot")
    # Screenshot mein 'OWNER_ID' hai, toh wahi fetch karega
    BOT_OWNER = int(os.environ.get("OWNER_ID", "5569039254"))
    
    # --- Database Settings ---
    # Screenshot mein 'CHANNEL_ID' aur 'DATABASE_URL' keys hain
    DB_CHANNEL = int(os.environ.get("CHANNEL_ID", "-1003789755565"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0") # Default name from screenshot

    # --- Force Subscribe (The Film Club) ---
    # Aapki naye screenshot wali key 'UPDATES_CHANNEL'
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003544601199")
    
    # --- Settings ---
    # Ise True rakhne se files copy karke forward hongi, original source safe rahega
    FORWARD_AS_COPY = True
    OTHER_USERS_CAN_SAVE_FILE = True
    
    # --- Bot Texts ---
    HOME_TEXT = "Hi [{}](tg://user?id={})\n\nMain **The Film Club** ka official File Store Bot hoon. Mujhe koi bhi file bhejein, main uska permanent link bana dunga."
