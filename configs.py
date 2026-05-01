import os

class Config(object):
    # API & Bot Credentials (Render se fetch honge)
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5569039254"))
    
    # Database Settings
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003789755565"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    # Force Subscribe (The Film Club)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003544601199")
    
    # Simple Logic Settings
    FORWARD_AS_COPY = True
    OTHER_USERS_CAN_SAVE_FILE = True
    
    # Bot Messages
    HOME_TEXT = "Hi [{}](tg://user?id={})\n\nMain **The Film Club** ka official File Store Bot hoon. Mujhe koi bhi file bhejein, main uska permanent link bana dunga."
