from playwright.sync_api import sync_playwright
from db.database import is_new_job, save_job
from utils.filters import match_keywords
from datetime import datetime
import time

def scrape_remoteok():
    new_jobs = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Set user agent to avoid bot detection
        page.set_extra_http_headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        print("🌐 Loading RemoteOK...")
        page.goto("https://remoteok.com/", timeout=60000)
        
        # Wait for initial content
        page.wait_for_selector("tr.job", timeout=10000)
        
        # Initial job count
        initial_jobs = page.locator("tr.job").count()
        print(f"📊 Initial jobs found: {initial_jobs}")
        
        # Scroll multiple times to trigger infinite scroll
        print("🔄 Scrolling to load more jobs...")
        previous_job_count = 0
        current_job_count = initial_jobs
        scroll_attempts = 0
        max_scroll_attempts = 5  # Reduced from 10 to 5
        
        while scroll_attempts < max_scroll_attempts and current_job_count > previous_job_count:
            previous_job_count = current_job_count
            
            # Scroll down in steps
            for i in range(3):  # Scroll 3 times per attempt
                page.evaluate("window.scrollBy(0, 1000)")
                time.sleep(1)
            
            # Wait for new content to load
            time.sleep(3)
            
            # Check if new jobs were loaded
            current_job_count = page.locator("tr.job").count()
            print(f"📊 Jobs after scroll {scroll_attempts + 1}: {current_job_count}")
            
            scroll_attempts += 1
            
            # If no new jobs loaded, try scrolling to the very bottom
            if current_job_count == previous_job_count:
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(3)
                current_job_count = page.locator("tr.job").count()
                print(f"📊 Jobs after scrolling to bottom: {current_job_count}")
        
        # Wait for network to be idle after all scrolling
        page.wait_for_load_state("networkidle", timeout=10000)
        
        # Final job count
        jobs = page.locator("tr.job")
        final_job_count = jobs.count()
        print(f"📊 Final job count: {final_job_count}")
        
        # Process only the first 20 jobs (newest ones) to focus on recent postings
        max_jobs_to_process = 20
        jobs_to_process = min(final_job_count, max_jobs_to_process)
        print(f"🔍 Processing first {jobs_to_process} newest jobs...")
        
        new_jobs_count = 0
        existing_jobs_count = 0
        filtered_jobs_count = 0
        
        # Process limited number of jobs (newest first)
        for i in range(jobs_to_process):
            job = jobs.nth(i)
            job_id = job.get_attribute("data-id")
            
            if not job_id:
                continue
                
            # Check if job is new
            if not is_new_job(job_id):
                existing_jobs_count += 1
                print(f"⏭️ Skipped existing job: {job_id}")
                continue

            try:
                # Extract job title using specific selector
                title = job.locator('h2[itemprop="title"]').inner_text()
                
                # Extract company name using specific selector
                company = job.locator('h3[itemprop="name"]').inner_text()
                
                # Extract job URL - use more specific selector to avoid multiple elements
                job_link_element = job.locator('a.preventLink[itemprop="url"]')
                if job_link_element.count() > 0:
                    link = "https://remoteok.com" + job_link_element.get_attribute("href")
                else:
                    # Fallback to data-href if preventLink not found
                    link = "https://remoteok.com" + job.get_attribute("data-href")
                
                # Extract posting date
                time_element = job.locator("time")
                if time_element.count() > 0:
                    posted = time_element.get_attribute("datetime")
                    if not posted:
                        posted = time_element.inner_text()
                else:
                    posted = datetime.utcnow().isoformat()
                
                # Extract salary if available
                salary_element = job.locator('.location:has-text("💰")')
                salary = ""
                if salary_element.count() > 0:
                    salary = salary_element.inner_text()
                
                # Extract location - use more specific selector to avoid salary info
                location_element = job.locator('.location:not(:has-text("💰"))')
                location = ""
                if location_element.count() > 0:
                    location = location_element.first.inner_text()
                
                # Extract job tags/skills
                tags_elements = job.locator("td.tags h3")
                tags = []
                for j in range(tags_elements.count()):
                    tag_text = tags_elements.nth(j).inner_text()
                    if tag_text:
                        tags.append(tag_text)
                
                # Extract company logo URL
                logo_element = job.locator("img.logo")
                logo_url = ""
                if logo_element.count() > 0:
                    logo_url = logo_element.get_attribute("src")

                # Check keyword matching
                search_text = title + " " + company + " " + " ".join(tags)
                if not match_keywords(search_text):
                    filtered_jobs_count += 1
                    print(f"❌ Filtered out: {title} at {company} (no keyword match)")
                    continue

                job_data = {
                    "id": f"remoteok-{job_id}",
                    "title": title,
                    "company": company,
                    "link": link,
                    "posted": posted,
                    "source": "remoteok",
                    "salary": salary,
                    "location": location,
                    "tags": ", ".join(tags),
                    "logo_url": logo_url,
                    "send_to_telegram": False,
                }

                save_job(job_data)
                new_jobs.append(job_data)
                new_jobs_count += 1
                print(f"✅ Added: {title} at {company}")
                
            except Exception as e:
                print(f"❌ Error processing job {i+1}: {e}")
                continue
                
        browser.close()
        
        print(f"\n📊 Summary:")
        print(f"  - Total jobs found: {final_job_count}")
        print(f"  - Newest jobs processed: {jobs_to_process}")
        print(f"  - New jobs added: {new_jobs_count}")
        print(f"  - Existing jobs skipped: {existing_jobs_count}")
        print(f"  - Filtered out: {filtered_jobs_count}")
        
    return new_jobs
