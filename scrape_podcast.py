import requests
from bs4 import BeautifulSoup
import json
import time
import re
import html as html_module

BASE_URL    = "https://staceyboehman.com"
PODCAST_URL = f"{BASE_URL}/podcast/"
HEADERS     = {"User-Agent": "Mozilla/5.0"}
OUTPUT_JSON = "podcast_transcripts.json"
DELAY       = 1.2


def get_episode_urls():
    """Crawl all podcast index pages and collect episode URLs."""
    urls = []
    page = 1
    while True:
        index_url = PODCAST_URL if page == 1 else f"{PODCAST_URL}page/{page}/?et_blog"
        resp = requests.get(index_url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "html.parser")

        # Episode links — anchor tags inside article elements
        articles = soup.find_all("article")
        if not articles:
            break
        found = 0
        for article in articles:
            link = article.find("a", href=True)
            if link and link["href"].startswith(BASE_URL):
                ep_url = link["href"].rstrip("/") + "/"
                if ep_url not in urls:
                    urls.append(ep_url)
                    found += 1

        print(f"  Page {page}: {found} episodes (total: {len(urls)})")

        # Check for next page
        older = soup.find("a", string=re.compile("Older", re.I))
        if not older:
            break
        page += 1
        time.sleep(DELAY)

    return urls


def scrape_episode(url):
    """Scrape title and transcript text from an episode page."""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Title
    title_tag = soup.find("h1") or soup.find("h2")
    title = title_tag.get_text().strip() if title_tag else url

    # Transcript: look for scrollable text box first, then entry-content
    transcript = ""

    # Some older episodes have a scroll box with class containing "transcript" or overflow:scroll
    scroll_box = soup.find("div", style=re.compile(r"overflow", re.I))
    if scroll_box:
        transcript = scroll_box.get_text(separator="\n").strip()

    # Fallback: main article entry-content
    if not transcript or len(transcript) < 200:
        content = soup.find("div", class_="entry-content")
        if content:
            # Remove nav, buttons, download links
            for tag in content.find_all(["a", "button"]):
                if any(w in (tag.get_text() + tag.get("href", "")).lower()
                       for w in ["download", "pdf", "subscribe", "itunes", "spotify"]):
                    tag.decompose()
            transcript = content.get_text(separator="\n").strip()

    # Clean up
    transcript = html_module.unescape(transcript)
    transcript = re.sub(r'\n{3,}', '\n\n', transcript)
    transcript = re.sub(r'[ \t]+', ' ', transcript)
    transcript = transcript.strip()

    # Skip if too short (just a player page with no text)
    if len(transcript) < 500:
        return None

    return {"title": title, "url": url, "transcript": transcript}


def main():
    print("Collecting episode URLs...")
    episode_urls = get_episode_urls()
    print(f"\nTotal episodes found: {len(episode_urls)}")

    results = []
    skipped = 0

    for i, url in enumerate(episode_urls):
        ep = scrape_episode(url)
        if not ep:
            print(f"  [{i+1}/{len(episode_urls)}] SKIP: {url}")
            skipped += 1
        else:
            short_title = ep["title"][:60]
            print(f"  [{i+1}/{len(episode_urls)}] OK ({len(ep['transcript'])} chars): {short_title}")
            results.append(ep)
        time.sleep(DELAY)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nDone! {len(results)} transcripts saved, {skipped} skipped.")
    print(f"Output: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
