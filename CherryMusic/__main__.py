#─────────────────────────────────────────────────────
# Project    : Music bot
# Name       : CherryMusicbot
# Email      : tutorialtech99@gmail.com
# Developer  : @Uffsexyboi
# Developer  : @Seductive_caffine
# Powered by : TeamAlfabots
#─────────────────────────────────────────────────────
import asyncio
import importlib
import logging
import os

from aiohttp import web
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from CherryMusic import LOGGER, nand, userbot
from CherryMusic.core.call import Cherry
from CherryMusic.misc import sudo
from CherryMusic.plugins import ALL_MODULES
from CherryMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


class _EndedCallNoiseFilter(logging.Filter):
    def filter(self, record):
        message = record.getMessage()
        return not ("SetVideoCallStatus" in message and "GROUPCALL_FORBIDDEN" in message)


logging.getLogger("asyncio").addFilter(_EndedCallNoiseFilter())


async def _start_web():
    """Tiny web server so hosts that need an open PORT (and pingers) work."""
    app = web.Application()
    app.router.add_get("/", lambda r: web.Response(text="CherryMusic is running"))
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    await web.TCPSite(runner, "0.0.0.0", port).start()
    LOGGER("CherryMusic").info(f"Web server started on port {port}")


async def init():
    await _start_web()
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await nand.start()
    for all_module in ALL_MODULES:
        importlib.import_module("CherryMusic.plugins" + all_module)
    LOGGER("CherryMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Cherry.start()
    try:
        await Cherry.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("CherryMusic").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Cherry.decorators()
    LOGGER("CherryMusic").info(
        "CherryMusicbot Started Successfully.\n\nPowered by TeamAlfabots"
    )
    await idle()
    await nand.stop()
    await userbot.stop()
    LOGGER("CherryMusic").info("Stopping CherryMusic Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    
