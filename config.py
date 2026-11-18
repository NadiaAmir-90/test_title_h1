
import os
from pathlib import Path
from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


# Django configuration
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")


# Website configuration
WEBSITES = {
    "rentbyowner": os.getenv("RENTBYOWNER_URL"),
    "hotala": os.getenv("HOTALA_URL"),
}

WEBSITES_URLS = [
    url.strip()
    for url in WEBSITES.values()
    if url and url.strip()
]


# Scraping configuration
DEVICE_MODE = os.getenv("DEVICE_MODE", "Desktop")

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 15))
REQUEST_DELAY = int(os.getenv("REQUEST_DELAY", 1))


# Report directory
REPORT_DIR = BASE_DIR / "reports"
