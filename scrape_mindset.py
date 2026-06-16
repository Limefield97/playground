import requests
from bs4 import BeautifulSoup
import json
import time
import html as html_module
import re

COOKIES = {
    "sess_":     "75rs9mhw7sf6q86j9q5g",
    "PHPSESSID": "4415506a315a506a3fc811483822",
    "t_":        "mr_5",
    "wordpress_logged_in_144e0bc188c8905af9f2b7928ef0a6cf": "krilov%40gmail.com%7C1781792093%7CIGcQaKUYcBKHbuWXBRXwycm5dmd0Az52RwKWhnDUKnn%7C061dcec189f4c1103b65a3dab52493590899dcde25b1987256cc6c26d2b98340",
    "wordpress_sec_144e0bc188c8905af9f2b7928ef0a6cf":        "krilov%40gmail.com%7C1781792093%7CIGcQaKUYcBKHbuWXBRXwycm5dmd0Az52RwKWhnDUKnn%7C2b2d87cdba735b1118276716939119aceb8beba0a94c7ac59e063d0a994e28bc",
}

BASE_URL = "https://2kfor2k.staceyboehman.com"
API_URL  = f"{BASE_URL}/wp-json/wp/v2/sbquestions"
HEADERS  = {"User-Agent": "Mozilla/5.0"}

KEYWORDS = [
    "self doubt", "confidence", "imposter", "worthiness",
    "identity", "resistance", "belief", "intentional",
    "mindset", "quit", "fear",
]
RESULTS_PER_KEYWORD = 20  # top 20 per keyword
OLDEST_COUNT        = 100  # pull 100 oldest posts from 2019-2020
OUTPUT_JSON         = "coaching_mindset.json"
OUTPUT_MD           = "coaching_mindset_universal.md"
DELAY               = 0.8


def clean_text(text):
    text = html_module.unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def fetch_post_list(params):
    resp = requests.get(API_URL, params={**params, "_fields": "id,slug,title,date"}, headers=HEADERS, cookies=COOKIES, timeout=15)
    if resp.status_code == 200:
        return resp.json()
    print(f"  API error {resp.status_code}")
    return []


def scrape_post(slug):
    url = f"{BASE_URL}/sbquestions/{slug}/"
    resp = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=15)
    if resp.status_code != 200:
        return None, None
    soup = BeautifulSoup(resp.text, "html.parser")
    article = soup.find("article", class_="et_pb_post")
    if not article:
        return None, None
    entry = article.find("div", class_="entry-content")
    question = entry.get_text(separator="\n").strip() if entry else ""
    answer_header = article.find("h4", class_="SB_SingleQuestionPage")
    if answer_header:
        answer_parts = []
        for sib in answer_header.find_next_siblings():
            if "SMC_SB_QA_SingleQuestionPage_BackSection" in sib.get("class", []):
                break
            text = sib.get_text(separator="\n").strip()
            if text:
                answer_parts.append(text)
        answer = "\n\n".join(answer_parts)
    else:
        answer = ""
    return clean_text(question), clean_text(answer)


def collect_posts():
    posts_to_scrape = {}  # slug -> {title, date, tags}

    # 1. Keyword searches
    for kw in KEYWORDS:
        print(f"\n[keyword: {kw}] Fetching top {RESULTS_PER_KEYWORD}...")
        batch = fetch_post_list({"search": kw, "per_page": RESULTS_PER_KEYWORD, "orderby": "relevance"})
        for p in batch:
            slug = p["slug"]
            if slug not in posts_to_scrape:
                posts_to_scrape[slug] = {"title": p["title"]["rendered"], "date": p["date"][:10], "tags": []}
            if kw not in posts_to_scrape[slug]["tags"]:
                posts_to_scrape[slug]["tags"].append(kw)
        print(f"  {len(batch)} posts added (running total: {len(posts_to_scrape)} unique)")

    # 2. Oldest 100 posts (2019-2020 archive)
    print(f"\n[oldest posts] Fetching {OLDEST_COUNT} from the archive...")
    fetched = 0
    page = 1
    while fetched < OLDEST_COUNT:
        batch = fetch_post_list({"order": "asc", "orderby": "date", "per_page": 100, "page": page})
        if not batch:
            break
        for p in batch:
            slug = p["slug"]
            if slug not in posts_to_scrape:
                posts_to_scrape[slug] = {"title": p["title"]["rendered"], "date": p["date"][:10], "tags": ["archive-2019-2020"]}
                fetched += 1
            if fetched >= OLDEST_COUNT:
                break
        page += 1
    print(f"  {fetched} new unique old posts added (total: {len(posts_to_scrape)} unique)")

    return posts_to_scrape


def main():
    posts_meta = collect_posts()
    print(f"\nTotal unique posts to scrape: {len(posts_meta)}")

    # Load existing URLs to avoid re-scraping already collected posts
    try:
        with open("coaching_qa.json", "r", encoding="utf-8") as f:
            existing = json.load(f)
        existing_urls = {item["url"] for item in existing}
        print(f"Skipping posts already in coaching_qa.json: checking {len(existing_urls)} existing URLs")
    except FileNotFoundError:
        existing_urls = set()

    results = []
    slugs = list(posts_meta.keys())
    for i, slug in enumerate(slugs):
        meta  = posts_meta[slug]
        url   = f"{BASE_URL}/sbquestions/{slug}/"

        if url in existing_urls:
            print(f"  [{i+1}/{len(slugs)}] SKIP (already in dataset): {meta['title']}")
            continue

        question, answer = scrape_post(slug)
        if not question or not answer:
            print(f"  [{i+1}/{len(slugs)}] SKIP (no content): {meta['title']}")
            continue

        results.append({
            "category": "Mindset & Universal",
            "tags":     meta["tags"],
            "title":    html_module.unescape(meta["title"]),
            "date":     meta["date"],
            "url":      url,
            "question": question,
            "answer":   answer,
        })
        print(f"  [{i+1}/{len(slugs)}] OK [{', '.join(meta['tags'])}]: {meta['title']}")
        time.sleep(DELAY)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("# Coaching Q&A: Mindset & Universal\n\n")
        for item in results:
            f.write(f"## {item['title']}\n\n")
            f.write(f"**Date:** {item['date']}  \n")
            f.write(f"**Topics:** {', '.join(item['tags'])}\n\n")
            f.write(f"**QUESTION:**\n\n{item['question']}\n\n")
            f.write(f"**ANSWER:**\n\n{item['answer']}\n\n")
            f.write("---\n\n")

    print(f"\nDone! Scraped {len(results)} new posts.")
    print(f"Saved: {OUTPUT_JSON} and {OUTPUT_MD}")


if __name__ == "__main__":
    main()
