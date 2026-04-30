import feedparser
from bs4 import BeautifulSoup

def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()


def load_medium_posts(rss_url):
    feed = feedparser.parse(rss_url)

    documents = []

    for entry in feed.entries:
        title = entry.title
        link = entry.link

        # Medium gives content in content[0]['value'] sometimes
        if "content" in entry:
            raw_html = entry.content[0].value
        else:
            raw_html = entry.summary

        clean_text = clean_html(raw_html)

        documents.append({
            "title": title,
            "content": clean_text,
            "link": link
        })

    return documents