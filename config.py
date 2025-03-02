# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "29385418"))
API_HASH = getenv("API_HASH", "5737577bcb32ea1aac1ac394b96c4b10")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6660736046").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://towaye6074:A2jR9c7DCr3gX09q@cluster0.g8c3j.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002209650474")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002010103322"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "Modijiurl.com")
AD_API = getenv("AD_API", "cecd5d2f94043ddd1a36edc074e4eb18b13b39f1")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
