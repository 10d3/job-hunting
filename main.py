from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, DISCORD_WEBHOOK
from db.database import init_db
from scrappers.remoteok import scrape_remoteok
from bots.telegram_bot import send_jobs_telegram
# from bots.discord_bot import send_jobs_discord

def main():
    init_db()

    all_jobs = []
    all_jobs += scrape_remoteok()
    # You can add: all_jobs += scrape_indeed(), etc.

    if not all_jobs:
        print("✅ No new jobs found.")
        return

    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        send_jobs_telegram(all_jobs, TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN)

    # if DISCORD_WEBHOOK:
    #     send_jobs_discord(all_jobs, DISCORD_WEBHOOK)

    print(f"✅ Sent {len(all_jobs)} new jobs.")

if __name__ == "__main__":
    main()
