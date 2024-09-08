import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 28559079
API_HASH = "a76c2fdd01244a9c21f2d7a50f7364d0"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7341746518:AAGRtO1EP28djFVmMmZmGX1JyVMMcHaieiw"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://sachinopboy1:sachinopboy1@cluster0.yijkd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002175086921

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7282263969

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/monarch1_X"
SUPPORT_GROUP = "https://t.me/OG_MEMBARSS"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGzxucAEf0DOeGdnh74m-xZ0EXTYkGRYQUhSMiOUxNojy5bydHhHgIh48Kh95fbLqWVsb4YzEUl1bWfvINXiX-RsYIreBIHs71FW5oo0D8dXqC36FsfB4odW04wbwieNAXo6CF8O2lBDeWCrCJ0ekeqZsU3X2d9CCNauYitps7gfSwX1LkspE0glqbPwFtuIRilMdLuKZb64I1B8eaxz_-MO3my5DTGp33HbaQQNfkWuOJjP_0UZ-JCEvspluhG8VflyFA5mJqVyDQ1iWxo9GdaavMwP8e1p7e91H6VvT8r0y7ylRkXNTcE5quNqmDE6MPbHaAoSJ0LOYQctUGg61mH7orqbwAAAAG2E8n1AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://envs.sh/bkG.jpg"

PING_IMG_URL = "https://envs.sh/bkG.jpg"

PLAYLIST_IMG_URL = "https://envs.sh/bkG.jpg"
STATS_IMG_URL = "https://envs.sh/bkG.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/bkG.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/bkG.jpg"
STREAM_IMG_URL = "https://envs.sh/bkG.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/bkG.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/bkG.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/bkG.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/bkG.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/bkG.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
