#─────────────────────────────────────────────────────
# Project    : Music bot
# Name       : CherryMusicbot
# Email      : tutorialtech99@gmail.com
# Developer  : @Uffsexyboi
# Developer  : @Seductive_caffine
# Powered by : TeamAlfabots
#─────────────────────────────────────────────────────
_seed = {}


def set_seed(chat_id, video_id):
    if video_id:
        _seed[chat_id] = video_id


def get_seed(chat_id):
    return _seed.get(chat_id)
