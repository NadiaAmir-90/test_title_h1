# from testapp.scraper import build_session,fetch_html
# from testapp.parse import parse_html

# def handler(site_name,url):

#     sessions=build_session()

#     try:
#         html=fetch_html(sessions,url)
#         parse_data=parse_html(html)

#         return{
#             "site_name":site_name,
#             "url":url,
#             "bs4_title": parse_data.get("title", ""),
#             "bs4_h1": parse_data.get("h1", ""),
#         }
#     finally:
#         sessions.close()


from testapp.scraper import build_session,fetch_html
from testapp.parse import parse_html

def handler(site_name,url):

    sessions=build_session()

    try:
        html=fetch_html(sessions,url)
        parse_data=parse_html(html)

        return{
            "site_name":site_name,
            "url":url,
            "bs4_title": parse_data.get("title", ""),
            "bs4_h1": parse_data.get("h1", ""),
        }
    finally:
        sessions.close()
