import requests
from bs4 import BeautifulSoup
import random
import time
from urllib.parse import urljoin, urlparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

def scrapeWikiArticle(url, max_pages=10):
    current_url = url
    for i in range(max_pages):
        response = requests.get(url=current_url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch {current_url}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id="firstHeading")


        if title:
            print(f"[{i+1}/{max_pages}] Title: {title.text}")

        raw_links = soup.select(
            "#bodyContent p a[href*='/wiki/'], #bodyContent li a[href*='/wiki/']"
        )

        article_links = []
        for link in raw_links:
            target_url = urljoin("https://en.wikipedia.org", link["href"])
            parsed_url = urlparse(target_url)
            if parsed_url.netloc != "en.wikipedia.org":
                continue
            if not parsed_url.path.startswith("/wiki/"):
                continue

            page_title = parsed_url.path[len("/wiki/"):]
            if ":" not in page_title and page_title != "Main_Page":
                article_links.append(target_url)

        if not article_links:
            print("No valid internal wiki links found")
            break
        
        next_href = random.choice(article_links)
        current_url = next_href
        time.sleep(1)

    
scrapeWikiArticle("https://en.wikipedia.org/wiki/December_1971")