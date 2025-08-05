import requests
import os
from dotenv import load_dotenv

def get_chat_id():
    print("🔍 Getting your Telegram Chat ID...")
    
    # Load environment variables
    load_dotenv()
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not bot_token:
        print("❌ No bot token found!")
        print("Please set your TELEGRAM_BOT_TOKEN in the .env file")
        return None
    
    print(f"✅ Bot token found: {bot_token[:10]}...")
    print("\n📱 Please send a message to your bot first!")
    print("1. Open Telegram")
    print("2. Search for your bot's username")
    print("3. Send any message (like 'Hello')")
    print("4. Press Enter here to continue...")
    
    input("Press Enter after sending a message to your bot...")
    
    # Get updates from Telegram
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if not data.get("ok"):
            print(f"❌ Error: {data.get('description', 'Unknown error')}")
            return None
        
        updates = data.get("result", [])
        
        if not updates:
            print("❌ No messages found!")
            print("Make sure you sent a message to your bot first.")
            return None
        
        # Get the first message
        message = updates[0].get("message", {})
        chat = message.get("chat", {})
        chat_id = chat.get("id")
        
        if chat_id:
            print(f"✅ Your Chat ID is: {chat_id}")
            print(f"✅ Your name: {chat.get('first_name', 'Unknown')}")
            print(f"✅ Your username: @{chat.get('username', 'Unknown')}")
            
            # Update .env file
            env_file = ".env"
            env_content = ""
            
            if os.path.exists(env_file):
                with open(env_file, 'r') as f:
                    env_content = f.read()
            
            # Add or update TELEGRAM_CHAT_ID
            if "TELEGRAM_CHAT_ID=" in env_content:
                # Update existing
                lines = env_content.split('\n')
                for i, line in enumerate(lines):
                    if line.startswith("TELEGRAM_CHAT_ID="):
                        lines[i] = f"TELEGRAM_CHAT_ID={chat_id}"
                        break
                env_content = '\n'.join(lines)
            else:
                # Add new
                if env_content and not env_content.endswith('\n'):
                    env_content += '\n'
                env_content += f"TELEGRAM_CHAT_ID={chat_id}\n"
            
            with open(env_file, 'w') as f:
                f.write(env_content)
            
            print(f"✅ Updated .env file with your Chat ID!")
            print("🎉 You're ready to test your bot!")
            
            return chat_id
        else:
            print("❌ Could not find chat ID in response")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    get_chat_id() 