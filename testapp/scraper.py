
import requests

from config import REQUEST_TIMEOUT, DEVICE_MODE


def build_session():
    """Create and configure a reusable HTTP session. """
    session=requests.Session()
    

    session = requests.Session()

    session.headers.update({
        "User-Agent":(
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    })

    return session


def fetch_html(session, url):
    """Fetch website HTML using the existing session."""

    response=session.get(url,timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


