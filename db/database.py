import sqlite3
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            link TEXT,
            salary TEXT,
            location TEXT,
            source TEXT,
            posted_at TEXT,
            send_to_telegram BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    conn.close()

def is_new_job(job_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT 1 FROM jobs WHERE id = ?", (job_id,))
    exists = c.fetchone()
    conn.close()
    return exists is None

def save_job(job):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO jobs (id, title, company, link, salary, location, source, posted_at, send_to_telegram) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (job["id"], job["title"], job["company"], job["link"], job["salary"], job["location"], job["source"], job["posted"], job["send_to_telegram"]))
    conn.commit()
    conn.close()
