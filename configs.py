import os

class Config(object):
    # API Credentials
    API_ID = int(os.environ.get("API_ID", "32460404"))
    API_HASH = os.environ.get("API_HASH", "410d526521ae7dcc474e0f4246788560")
    
    # Bot Credentials
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6592940928:AAGL1ctYGLxbV4adD30XkcGmyU2RK5_6ERM")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Itadomobot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5569039254"))
    
    # Database Settings (Storage Channel)
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003789755565"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://yadavjikibhaish600_db_user:NgUBo6FJiL3cssc4@cluster0.iwrhl8n.mongodb.net/?appName=Cluster0")
    
    # --- Force Subscribe Setup ---
    # User ko ye channel join karna padega file lene ke liye
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003544601199")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    
    # Logic Settings
    FORWARD_AS_COPY = True
    OTHER_USERS_CAN_SAVE_FILE = True
    
    # Bot Texts
    HOME_TEXT = "Hi [{}](tg://user?id={})\n\nMain **The Film Club** ka official File Store Bot hoon. Mujhe koi bhi file bhejein, main uska permanent link bana dunga."
