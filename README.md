# Django Web Scraping & Validation Pipeline

A robust Django-based project designed for automated web scraping, content verification, and data processing using **Beautiful Soup 4**, **Playwright**, and custom management commands.It combines lightning-fast HTTP parsing with headless browser automation (Playwright) to handle dynamic JavaScript-rendered pages, perform structural checks, and store audit outcomes in a database.

---
 
### Key Features:
* **Custom Management Commands:** Execute data pipelines easily via CLI (`python manage.py <command>`).
* **Dual Scraping Strategy:** Utilizes Beautiful Soup for speed and Playwright for dynamic/headless browser rendering.
* **Database Integration:** Stores scraping results, audit logs, and status flags (e.g., `title_passed`) using Django Models.
* **Environment Configuration:** Secure credential and configuration management using `python-dotenv`.

---

## Tech Stack

* **Backend:** Python 3.12, Django
* **Scraping & Automation:** Beautiful Soup 4, Playwright, lxml, Requests


---

## 📋 Prerequisites & Setup Guide:
### 1. Clone the Repository & Navigate to Folder
```bash
git clone [https://github.com/NadiaAmir-90/your-repo-name.git](https://github.com/NadiaAmir-90/your-repo-name.git)
cd your-repo-name
On macOS / Linux / Git Bash:

Bash
python -m venv venv
source venv/bin/activate

python -m venv venv
.\venv\Scripts\Activate.ps1
Bash
pip install -r requirements.txt

Bash
playwright install

Code snippet
SECRET_KEY=your-super-secret-key-here
DEBUG=True

RENTBYOWNER_URL=[https://www.rentbyowner.com/all/usa](https://www.rentbyowner.com/all/usa)
HOTALA_URL=[https://www.hotala.com/all/usa](https://www.hotala.com/all/usa)
DEVICE_MODE=Desktop

REQUEST_TIMEOUT=15
REQUEST_DELAY=1

python manage.py makemigrations
python manage.py migrate

Bash
python manage.py runserver

Bash
python manage.py scrape_websites
python manage.py scrape_with_playwright
