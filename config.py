import os
from dotenv import load_dotenv
load_dotenv()

# Updated keywords to be more inclusive
KEYWORDS = [
    # Tech keywords
    "web", "react", "nextjs", "python", "nodejs", 
    "javascript", "typescript", "frontend", "backend", "fullstack",
    "developer", "engineer", "programmer", "software", "tech",
    
    # Design keywords
    "design", "designer", "ui", "ux", "product", "creative",
    
    # Marketing keywords
    "marketing", "content", "social", "digital", "growth",
    
    # General remote keywords
    "remote", "work from home", "wfh", "virtual", "online",
    
    # Job type keywords
    "manager", "director", "lead", "senior", "junior", "associate",
    
    # Industry keywords
    "startup", "saas", "tech", "digital", "online", "web"
]

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

DB_PATH = "db/seen_jobs.sqlite"
