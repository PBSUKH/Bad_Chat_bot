
# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_NAME = os.environ.get("BOT_NAME")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------
DEEP_API = os.environ.get("DEEP_API")
# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID"))
# ------------------------------------------------
GPT_API = os.environ.get("GPT_API")
# ------------------------------------------------
DAXX_API = os.environ.get("DAXX_API")
# ------------------------------------------------
SUDO_USER = list(int(i) for i in os.environ.get("SUDO_USER", "6898413162").split(" "))
# ------------------------------------------------
MONGO_DB = os.environ.get("MONGO_DB")
# ------------------------------------------------
MONGO_URL = getenv("MONGO_URL", "")
# ------------------------------------------------
SESSION_STRING = getenv("SESSION_STRING", "")
# ------------------------------------------------
SUPPORT_GRP = getenv("SUPPORT_GRP", "ll_THE_BAD_BOT_ll")
# ------------------------------------------------
UPDATE_CHNL = getenv("UPDATE_CHNL", "ll_BAD_MUNDA_WORLD_ll")
# ------------------------------------------------
