#─────────────────────────────────────────────────────
# Project    : Music bot
# Name       : CherryMusicbot
# Email      : tutorialtech99@gmail.com
# Developer  : @Uffsexyboi
# Developer  : @Seductive_caffine
# Powered by : TeamAlfabots
#─────────────────────────────────────────────────────
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get from my.telegram.org/app
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

# Get from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Get from MongoDB Atlas
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))

LOGGER_ID = int(getenv("LOGGER_ID", "0"))
OWNER_ID = int(getenv("OWNER_ID", "0"))

# Heroku App Name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")

# Get from dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

# Set UPSTREAM_REPO to YOUR OWN repo url (used only by the updater). Empty = updater disabled.
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/Alfabots_update"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/Alfabots_support"
)

AUTO_LEAVING_ASSISTANT = getenv(
    "AUTO_LEAVING_ASSISTANT",
    "False"
).lower() == "true"

# Get from developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

PLAYLIST_FETCH_LIMIT = int(
    getenv("PLAYLIST_FETCH_LIMIT", "25")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)

# Get from @Sessionbbbot
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/ljdsem.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/dz6u6n.jpg"
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/6qqup2.jpg"
STATS_IMG_URL = "https://files.catbox.moe/6qqup2.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/6qqup2.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/6qqup2.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/6qqup2.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/6qqup2.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/junujv.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/junujv.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/dz6u6n.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/dz6u6n.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(
    time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
)


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] SUPPORT_CHANNEL url must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] SUPPORT_CHAT url must start with https://"
        )
