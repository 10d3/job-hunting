import os
from dotenv import load_dotenv
load_dotenv()

KEYWORDS = ["web", "react", "nextjs", "python", "nodejs"]

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

DB_PATH = "db/seen_jobs.sqlite"
