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
    TOKEN = getenv("TOKEN", "5887815440:AAF95gTRiUm0Dl81zOazBBLaF0hO01xb0dc")
    OWNER_ID = getenv("OWNER_ID", "5540577046")
    STRING_SESSION = getenv("STRING_SESSION", "1AZWarzwBu3xk1G65wgK4zw6o54z9rvz7WdMk5sAYKu6zBMzhrLn0rqJ_9ei9CDH6Zn1gSWJ41L5W9CGqLFix2zE0G4lfyJ-liT94CYU71CrCgiUjzly0LkNKPJ7Uk9Uq1RmJzBVorKk4LNCtFTN6ZngqyBuvF9A8j4ivLHo8_wKLP-8iAEeZ2zvQrGbzVP6YNqbNeL516nDCE2wkj5DmmyI9WW0DBy_RBvJDiilXZV0rnpZBIfH15q5JibNhop32g-nywZtMM03XzAnH04O6oGKgG8HwzqZopFcwzCljM9ucjEWS2cHkCOBV4dphow98s-0i1Rn5qLRmr3xvusggBicmko73CjQ=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "notaakash")
    DB_URI = getenv("DATABASE_URL", "postgres://gsgbbfzj:QLmkpmgt6DVxpC9d6RzdlhPg30CW_j54@mel.db.elephantsql.com/gsgbbfzj")
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
