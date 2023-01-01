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
    TOKEN = getenv("TOKEN", "5400035200:AAHS4WEpHpN1ptcJP69_Qxoa-19LZLLqnhw")
    OWNER_ID = getenv("OWNER_ID", "5540577046")
    STRING_SESSION = getenv("STRING_SESSION", "AQCFP5pUwSOCs9ZIlYdUWCmh5NIBtPaWyBQm_ywZlu3w1DsOh9NRTdzWWYKqeU3zdsL7qGqVI5vAeagwqqQFzcKsmcDx-MycMhKyMMmS7C39UQBVJAmsmfULq7KpR1YDt0JWRpxUPFKRfPIZkTILftukojQvzuSzNQRiCGVnq7VHxJe3aSHqXZ0CFX-n-g0LBOsO-yfIH_H2QulLkAHr3Tp8MADowpf3TSJFABoM5n0WVz2r30s5pOjvlpKzu0IURGUKFxc_37ZmrjQOGTScTnEasciL3RwAK6SYs6sUyiS3BlDOVHcYEVmGFsXcT1rNC1u_vHVngMrSHw-jyiPZ7eq2AAAAAUT_6vMA")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "notaakash")
    DB_URI = getenv("DATABASE_URL", "postgres://flbgihxq:GT0XlOITIkrSfGbu1lXws1oDoHJdppRt@mel.db.elephantsql.com/flbgihxq")
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
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1486727193 5802072593").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
