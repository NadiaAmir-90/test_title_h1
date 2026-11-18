from bs4 import BeautifulSoup

def parse_html(html):
    """parse the html and extracts title and h1 """

    soup=BeautifulSoup(html,"html.parser")
    
    title_tag=soup.find("title")

    if title_tag:
        title=title_tag.get_text(strip=True)
    else:
        title=""
    
    h1_tag=soup.find("h1")

    if h1_tag:
        h1=h1_tag.get_text(strip=True)
    else:
        h1=""

    return{
        "title":title,
        "h1":h1,
        }
    


