<h1 align="center">🍒 CherryMusicbot</h1>

<p align="center"><b>Telegram voice-chat music bot — Pyrogram + PyTgCalls</b></p>

| | |
|---|---|
| **Project** | Music bot |
| **Name** | CherryMusicbot |
| **Email** | tutorialtech99@gmail.com |
| **Developer** | @Uffsexyboi |
| **Developer** | @Seductive_caffine |
| **Powered by** | TeamAlfabots |

## Required variables

| Variable | Description |
|---|---|
| `API_ID`, `API_HASH` | From https://my.telegram.org |
| `BOT_TOKEN` | From @BotFather |
| `MONGO_DB_URI` | MongoDB connection string |
| `OWNER_ID` | **Your** Telegram user ID (no default) |
| `LOGGER_ID` | Log group/channel ID |
| `STRING_SESSION` | Pyrogram v2 assistant session (`STRING_SESSION2..5` optional) |
| `SHRUTI_API_URL`, `SHRUTI_API_KEY` | Download API URL and key (point to your own API if self-hosted) |

Optional: `UPSTREAM_REPO` (your own repo, enables `/update`), `UPSTREAM_BRANCH`, `GIT_TOKEN`, `SUPPORT_CHANNEL`, `SUPPORT_CHAT`, `DURATION_LIMIT`, `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

## Run

**VPS**
```bash
bash setup      # installs deps and writes .env
bash start      # python3 -m CherryMusic
```

**Docker**
```bash
docker build -t cherrymusic .
docker run --env-file .env cherrymusic
```

**Heroku** — use `app.json` / `heroku.yml` (container stack).

## Security notes
- Never commit `.env` or `cookies/` (both are in `.gitignore`).
- Only `OWNER_ID` can use `/eval` and `/sh`. Sudo users cannot.

## Credits
- **CherryMusicbot:** @Uffsexyboi, @Seductive_caffine — Powered by TeamAlfabots

Full details in [CREDITS.md](CREDITS.md).
