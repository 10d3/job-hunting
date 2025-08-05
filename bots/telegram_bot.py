import asyncio
from telegram import Bot
from telegram.constants import ParseMode

async def send_jobs_telegram_async(jobs, chat_id, bot_token):
    if not jobs:
        return
        
    bot = Bot(token=bot_token)
    
    # Send summary message
    summary_msg = f"🎯 *Found {len(jobs)} new job(s)!*\n\n"
    await bot.send_message(chat_id=chat_id, text=summary_msg, parse_mode=ParseMode.MARKDOWN)
    
    # Send each job as a separate message
    for i, job in enumerate(jobs, 1):
        # Format salary and location
        salary = job.get('salary', 'Not specified')
        location = job.get('location', 'Not specified')
        tags = job.get('tags', 'No tags')
        
        # Create the message
        msg = f"""🚀 *{job['title']}*
🏢 *Company:* {job['company']}
💰 *Salary:* {salary}
🌍 *Location:* {location}
🏷️ *Tags:* {tags}
🔗 [View Job]({job['link']})
📅 *Posted:* {job['posted']}
📊 *Source:* {job['source']}

---
*Job {i} of {len(jobs)}*"""
        
        try:
            await bot.send_message(
                chat_id=chat_id, 
                text=msg, 
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
        except Exception as e:
            print(f"❌ Error sending Telegram message: {e}")
            # Fallback to simple message if formatting fails
            simple_msg = f"🚀 {job['title']} at {job['company']}\n🔗 {job['link']}"
            await bot.send_message(chat_id=chat_id, text=simple_msg)

def send_jobs_telegram(jobs, chat_id, bot_token):
    """Synchronous wrapper for the async function"""
    asyncio.run(send_jobs_telegram_async(jobs, chat_id, bot_token))
