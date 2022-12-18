import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "5887815440:AAFwo7I5TbhC2dJdpCwPqq7NDHlxpmAbvnI")
    OWNER_ID = getenv("OWNER_ID", "5540577046")
    STRING_SESSION = getenv("STRING_SESSION", "1AZWarzUBu4Bf2pp5ecwocLKFl3zppo9FzqEM7wYWFg6cVUsHq5Q7psdtFZfFjZTTXNZkT7b771i-DOxj-yvG6RZhhoY3boc34GqhKgpq2IwMUgKOr6bFv1IGIMkMNkHu-4rl1E_FmJMqqOIiLaHlDW6iNvlt1j0dCUplbW0CnDjmnQs7dKfIA-VSBja96HWTn29i4VUYElih0UkQpXgNVPol5oPHjH0jnggoLV_5cQfntkfDwZ6l9_YVWg4X1O7gab1DCYfe7kXMO9TaDTxgCPIt5W1-_lBVSr2kQHG-WRfph8xIxRwNTn6NZB409wlYiXpA8Q-efWR6MwihXsxqYZkxfiyIZHU=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "notaakash")
    DB_URI = getenv("DATABASE_URL", "postgres://vuspgrkj:ZAnjM0eSEJKNBzwrsMnN5B6fX94XGuo-@mel.db.elephantsql.com/vuspgrkj")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001851677864")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001851677864")
    SYS_ADMIN = getenv("SYS_ADMIN", "")
    DEV_USERS = getenv("DEV_USERS", "")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "zNe9pCwbfzhYieq0vrp7cADw8yX1LBm_wlADijXC4nsffG8bd3wnpW5dMuMvA1hi")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
