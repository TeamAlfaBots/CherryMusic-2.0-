#─────────────────────────────────────────────────────
# Project    : Music bot
# Name       : CherryMusicbot
# Email      : tutorialtech99@gmail.com
# Developer  : @Uffsexyboi
# Developer  : @Seductive_caffine
# Powered by : TeamAlfabots
#─────────────────────────────────────────────────────
from pyrogram import filters
from pyrogram.types import Message

from CherryMusic import nand
from CherryMusic.core.call import Cherry

welcome = 20
close = 30


@nand.on_message(filters.video_chat_started, group=welcome)
@nand.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Cherry.stop_stream_force(message.chat.id)
