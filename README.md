# Django Web Scraping & Validation Pipeline

A Django-based project designed for automated web scraping, content validation, and data processing using **Beautiful Soup 4 (BS4)** and **Playwright**.
The project combines fast HTTP-based HTML parsing with headless browser automation to handle both static and JavaScript-rendered web pages. It extracts webpage information, performs structural validation, compares results, and stores validation outcomes in a Django database.

---

## 🚀 Key Features

- **Custom Django Management Commands:** Execute scraping and validation workflows directly from the terminal.
- **Dual Scraping Strategy:**
  - Beautiful Soup 4 for fast HTML parsing.
  - Playwright for browser-based inspection of dynamically rendered content.
- **Content Validation:** Extract and validate webpage titles and H1 headings.
- **Database Integration:** Store scraping results, validation outcomes, audit information, and status flags such as `title_passed`.
-
---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python 3.12, Django |
| Web Scraping | Beautiful Soup 4, Requests |
| Browser Automation | Playwright |
| HTML Parsing | html.parser|
| Configuration | python-dotenv |



## ⚙️ Installation & Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/NadiaAmir-90/test_title_h1.git
```

Navigate to the project directory:

```bash
cd test_title_h1
```

### 2. Create a Virtual Environment

**Linux / macOS / Git Bash:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

Install the required Playwright browser binaries:

```bash
playwright install
```

If the project only uses Chromium, you can install it separately:

```bash
playwright install chromium
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```env
SECRET_KEY=your-super-secret-key-here
DEBUG=True

RENTBYOWNER_URL=https://www.rentbyowner.com/all/usa
HOTALA_URL=https://www.hotala.com/all/usa

DEVICE_MODE=Desktop

REQUEST_TIMEOUT=15
REQUEST_DELAY=1
```

**Configuration Description:**

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key. |
| `DEBUG` | Enables or disables Django debug mode. |
| `RENTBYOWNER_URL` | Target URL for RentByOwner. |
| `HOTALA_URL` | Target URL for Hotala. |
| `DEVICE_MODE` | Browser/device mode (Desktop, Mobile, or Tablet). |
| `REQUEST_TIMEOUT` | Maximum time allowed for an HTTP request. |
| `REQUEST_DELAY` | Delay between scraping requests. |

### 6. Apply Database Migrations

Create migration files if your models have changed:

```bash
python manage.py makemigrations
```

Apply migrations to the database:

```bash
python manage.py migrate
```

### 7. Run the Django Development Server

```bash
python manage.py runserver
```

---

## 🔄 Running the Scraping Pipeline

The project provides two separate Django management commands.

### Step 1: Run Beautiful Soup Scraping

```bash
python manage.py scrape_websites
```
### Step 2: Run Playwright Validation

```bash
python manage.py scrape_with_playwright
```

---

## 📁 Project Execution Order

```text
                 Target Websites
                        |
                        v
              Beautiful Soup (BS4)
                        |
                        v
                 HTTP Requests
                        |
                        v
                  HTML Parsing
                        |
                        v
             Extract Page Information
                        |
                        v
                Initial Results
                        |
                        v
               Playwright Browser
                        |
                        v
              Browser-based Extraction
                        |
                        v
              Compare Both Results
                        |
                        v
                Django ORM
                        |
                        v
                Database Storage
```

---

