from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from bots.telegram_bot import send_jobs_telegram

def test_telegram():
    print("🤖 Testing Telegram Bot...")
    
    # Check if credentials are set
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram credentials not found!")
        print("Please set up your .env file with:")
        print("TELEGRAM_BOT_TOKEN=your_bot_token")
        print("TELEGRAM_CHAT_ID=your_chat_id")
        return False
    
    print(f"✅ Bot Token: {TELEGRAM_BOT_TOKEN[:10]}...")
    print(f"✅ Chat ID: {TELEGRAM_CHAT_ID}")
    
    # Create a test job
    test_job = {
        "title": "Test Job - Senior Python Developer",
        "company": "Test Company Inc",
        "link": "https://example.com/job",
        "posted": "2024-01-01T12:00:00",
        "source": "test",
        "salary": "💰 $80k - $120k",
        "location": "🌏 Remote",
        "tags": "Python, Django, React",
    }
    
    try:
        print("📤 Sending test message...")
        send_jobs_telegram([test_job], TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN)
        print("✅ Test message sent successfully!")
        print("📱 Check your Telegram for the test message")
        return True
    except Exception as e:
        print(f"❌ Error sending test message: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you created a bot with @BotFather")
        print("2. Make sure you sent a message to your bot")
        print("3. Check that your bot token and chat ID are correct")
        return False

if __name__ == "__main__":
    test_telegram() 