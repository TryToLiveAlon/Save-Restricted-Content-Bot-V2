# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20970411"))
API_HASH = getenv("API_HASH", "6f059b1001f776a1622a1688f0e637cb")
BOT_TOKEN = getenv("BOT_TOKEN", 7434585617:AAE8B9BnoGrueVpe81VZH9x7jMijIUkmTJc")
OWNER_ID = int(getenv("OWNER_ID", "6140468904"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB",None)
LOG_GROUP = int(getenv("LOG_GROUP", "-1002209650474"))
FORCESUB = getenv("FORCESUB", "deathking_worldd")
