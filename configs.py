import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "hdsssssa_bot")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", -1003789755565))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5569039254))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003544601199")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1003789755565))
