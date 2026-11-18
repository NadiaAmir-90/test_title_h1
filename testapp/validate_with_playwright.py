import csv
from pathlib import Path
from django.core.management.base import CommandError
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from config import REPORT_DIR,REQUEST_TIMEOUT
from testapp.models import Results 


def playwright_handler(site_name, url):
    """
    Collect website title and H1 using Playwright,
    compare them with BeautifulSoup results,
    and save comparison results to the database.
    """
    bs4_csv_file = REPORT_DIR / "results.csv"

    with open(bs4_csv_file, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        bs4_data=next((row for row in reader if row["site_name"]==site_name or row["url"]==url),None)

    if bs4_data is None:
        raise CommandError(f"No BeautifulSoup data found for {site_name}.")
    bs4_title=bs4_data["bs4_title"]
    bs4_h1=bs4_data["bs4_h1"]


    #  Collect data using Playwright
    with sync_playwright() as p:
        browser =p.chromium.launch(headless=True)

        try:
            page=browser.new_page()
            page.goto(url,wait_until="domcontentloaded",timeout=REQUEST_TIMEOUT*1000)
            playwright_title=page.title()
            playwright_h1=page.locator("h1").first.inner_text()
        finally:
            browser.close()
        
    title_passed=(bs4_title.strip().lower()==playwright_title.strip().lower())
    h1_passed=(bs4_h1.strip().lower()==playwright_h1.strip().lower())



    # Prepare comparison result
    result={
        "site_name":site_name,
        "bs4_title":bs4_title,
        "playwright_title":playwright_title,
        "title_passed": title_passed,
        "bs4_h1": bs4_h1,
        "playwright_h1": playwright_h1,
        "h1_passed": h1_passed,

    }
    
    #  Save comparison result to Django database
    Results.objects.update_or_create(
        site_name=site_name,
        defaults={
            "bs4_title":bs4_title,
            "playwright_title":playwright_title,
            "title_passed":title_passed,
            "bs4_h1":bs4_h1,
            "playwright_h1":playwright_h1,
            "h1_passed":h1_passed,
        }

    )

    return result
