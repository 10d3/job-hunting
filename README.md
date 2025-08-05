# 🤖 Job Hunting Automation

A smart job scraper that monitors RemoteOK for new remote job opportunities and sends instant Telegram notifications when matching jobs are found.

## ✨ Features

- **🔍 Smart Job Scraping**: Automatically scrapes RemoteOK for the newest job postings
- **📱 Telegram Notifications**: Instant notifications with detailed job information
- **🎯 Keyword Filtering**: Only shows jobs matching your specific criteria
- **💾 Database Tracking**: Prevents duplicate notifications for the same job
- **⚡ Efficient**: Fast execution with optimized scrolling (5 scrolls max)
- **🆕 Newest First**: Focuses on the most recent job postings
- **📊 Detailed Info**: Salary, location, tags, company info, and direct links

## 🗺️ Roadmap

### Phase 1: Multi-Platform Support 🚀
- [x] **RemoteOK** - ✅ **COMPLETED** - Smart job scraper with infinite scroll
- [ ] **WeWorkRemotely** - Add scraper for WeWorkRemotely.com
- [ ] **Stack Overflow Jobs** - Integrate Stack Overflow job listings
- [ ] **LinkedIn Jobs** - Add LinkedIn remote job monitoring
- [ ] **Indeed Remote** - Scrape Indeed for remote positions
- [ ] **AngelList** - Monitor startup job postings
- [ ] **GitHub Jobs** - Add GitHub job board integration

### Phase 2: AI-Powered Auto-Application 🤖
- [x] **Smart Job Filtering** - ✅ **COMPLETED** - Keyword-based job matching
- [x] **Database Tracking** - ✅ **COMPLETED** - Prevents duplicate notifications
- [x] **Telegram Notifications** - ✅ **COMPLETED** - Instant job alerts
- [ ] **AI Resume Generator** - Create tailored resumes for each job
- [ ] **Cover Letter AI** - Generate personalized cover letters
- [ ] **Application Tracking** - Track application status and responses
- [ ] **Smart Matching** - AI to determine job-skill fit score
- [ ] **Auto-Fill Forms** - Automatically fill job application forms
- [ ] **Follow-up Automation** - Automated follow-up emails

### Phase 3: Advanced Features 🎯
- [x] **Efficient Scraping** - ✅ **COMPLETED** - Optimized scrolling (5 attempts max)
- [x] **Newest First Processing** - ✅ **COMPLETED** - Focuses on recent jobs
- [x] **Detailed Job Info** - ✅ **COMPLETED** - Salary, location, tags, company info
- [ ] **Salary Negotiation AI** - AI-powered salary negotiation assistance
- [ ] **Interview Prep** - AI interview preparation and practice
- [ ] **Company Research** - Automated company background research
- [ ] **Networking Bot** - Automated LinkedIn networking
- [ ] **Portfolio Optimization** - AI suggestions for portfolio improvements
- [ ] **Skill Gap Analysis** - Identify missing skills for target jobs

### Phase 4: Enterprise Features 🏢
- [ ] **Multi-User Support** - Support for multiple job seekers
- [ ] **Team Dashboard** - Web dashboard for job hunting teams
- [ ] **Analytics** - Job application success analytics
- [ ] **API Integration** - REST API for third-party integrations
- [ ] **Mobile App** - Native mobile application
- [ ] **Advanced Notifications** - Slack, Discord, email notifications

### Phase 5: AI Enhancement 🧠
- [ ] **Job Market Analysis** - AI-powered job market insights
- [ ] **Salary Prediction** - AI salary prediction based on skills and experience
- [ ] **Career Path Planning** - AI career development recommendations
- [ ] **Skill Development** - Personalized learning path recommendations
- [ ] **Market Trends** - Real-time job market trend analysis
- [ ] **Predictive Analytics** - Predict job availability and demand

### 🎯 Current Implementation Status

**✅ Completed Features:**
- RemoteOK job scraper with infinite scroll
- Smart keyword filtering system
- SQLite database for job tracking
- Telegram notifications with detailed formatting
- Efficient processing (20 newest jobs)
- Duplicate prevention system
- Comprehensive error handling

**🔄 In Progress:**
- Discord webhook support (code ready, needs testing)
- Dashboard development (directory created)

**📋 Next Priority:**
- Add WeWorkRemotely scraper
- Implement Discord notifications
- Create web dashboard
- Add more job sites

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install playwright python-dotenv python-telegram-bot

# Install Playwright browsers
playwright install
```

### 2. Set Up Telegram Bot

1. **Create a bot** with [@BotFather](https://t.me/botfather) on Telegram
2. **Get your chat ID** by running:
   ```bash
   python get_chat_id.py
   ```
3. **Create `.env` file**:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```

### 3. Run the Scraper

```bash
python main.py
```

## 📁 Project Structure

```
job_hunting/
├── main.py                 # Main entry point
├── config.py              # Configuration and keywords
├── scrappers/
│   └── remoteok.py        # RemoteOK job scraper
├── bots/
│   └── telegram_bot.py    # Telegram notification bot
├── db/
│   └── database.py        # SQLite database operations
├── utils/
│   └── filters.py         # Keyword matching logic
├── get_chat_id.py         # Telegram setup helper
├── test_telegram.py       # Test Telegram notifications
└── .env                   # Environment variables
```

## ⚙️ Configuration

### Keywords

Edit `config.py` to customize your job search:

```python
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
```

### Performance Settings

In `scrappers/remoteok.py`:
- `max_scroll_attempts = 5` - Number of scroll attempts
- `max_jobs_to_process = 20` - Number of newest jobs to process

## 📱 Telegram Notifications

You'll receive beautifully formatted messages like:

```
🎯 Found 3 new job(s)!

🚀 Senior Python Developer
🏢 Company: Tech Corp
💰 Salary: 💰 $80k - $120k
🌍 Location: 🌏 Remote
🏷️ Tags: Python, Django, React
🔗 View Job
📅 Posted: 2024-01-01T12:00:00
📊 Source: remoteok

---
Job 1 of 3
```

## 🔧 Setup Guide

### Step 1: Create Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/start` then `/newbot`
3. Choose a name and username for your bot
4. Save the bot token

### Step 2: Get Chat ID

1. Send a message to your bot
2. Run: `python get_chat_id.py`
3. Follow the instructions

### Step 3: Configure Environment

Create `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### Step 4: Test Setup

```bash
python test_telegram.py
```

### Step 5: Run Scraper

```bash
python main.py
```

## 📊 How It Works

1. **🌐 Loads RemoteOK** - Opens the website and waits for content
2. **🔄 Scrolls Efficiently** - Triggers infinite scroll to load more jobs (5 attempts max)
3. **🔍 Finds New Jobs** - Processes the 20 newest job postings
4. **🎯 Filters by Keywords** - Matches jobs against your keyword list
5. **💾 Checks Database** - Skips jobs already seen
6. **📱 Sends Notifications** - Delivers detailed job info to Telegram
7. **📊 Shows Summary** - Displays statistics about the run

## 🎯 Sample Output

```
🌐 Loading RemoteOK...
📊 Initial jobs found: 1
🔄 Scrolling to load more jobs...
📊 Jobs after scroll 1: 47
📊 Jobs after scroll 2: 97
📊 Jobs after scroll 3: 147
📊 Jobs after scroll 4: 197
📊 Jobs after scroll 5: 247
📊 Final job count: 247
🔍 Processing first 20 newest jobs...
✅ Added: Senior Python Developer at TechCorp
✅ Added: Frontend Engineer at StartupXYZ
⏭️ Skipped existing job: 1234567
❌ Filtered out: Sales Manager at CompanyABC (no keyword match)

📊 Summary:
  - Total jobs found: 247
  - Newest jobs processed: 20
  - New jobs added: 5
  - Existing jobs skipped: 12
  - Filtered out: 3
```

## 🚀 Automation

### Cron Job (Linux/Mac)

Add to crontab to run every hour:
```bash
0 * * * * cd /path/to/job_hunting && python main.py
```

### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger to run every hour
4. Action: Start a program
5. Program: `python`
6. Arguments: `main.py`
7. Start in: `C:\path\to\job_hunting`

## 🔧 Troubleshooting

### Common Issues

**"No module named 'dotenv'"**
```bash
pip install python-dotenv
```

**"No module named 'playwright'"**
```bash
pip install playwright
playwright install
```

**Telegram bot not responding**
- Make sure you sent a message to your bot first
- Check that your bot token is correct
- Verify your chat ID is correct

**No jobs found**
- Check your internet connection
- RemoteOK might be down
- Try running again later

### Debug Mode

Run with verbose output:
```bash
python main.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [RemoteOK](https://remoteok.com) for job listings
- [Playwright](https://playwright.dev) for web automation
- [python-telegram-bot](https://python-telegram-bot.org) for Telegram integration

## 📞 Support

If you encounter any issues:

1. Check the troubleshooting section
2. Review the logs for error messages
3. Test individual components
4. Open an issue on GitHub

---

**Happy Job Hunting! 🎯**
