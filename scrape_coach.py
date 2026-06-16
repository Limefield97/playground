import requests
from bs4 import BeautifulSoup
import json
import time
import random

COOKIES = {
    "sess_":     "75rs9mhw7sf6q86j9q5g",
    "PHPSESSID": "4415506a315a506a3fc811483822",
    "t_":        "mr_5",
    "wordpress_logged_in_144e0bc188c8905af9f2b7928ef0a6cf": "krilov%40gmail.com%7C1781792093%7CIGcQaKUYcBKHbuWXBRXwycm5dmd0Az52RwKWhnDUKnn%7C061dcec189f4c1103b65a3dab52493590899dcde25b1987256cc6c26d2b98340",
    "wordpress_sec_144e0bc188c8905af9f2b7928ef0a6cf":        "krilov%40gmail.com%7C1781792093%7CIGcQaKUYcBKHbuWXBRXwycm5dmd0Az52RwKWhnDUKnn%7C2b2d87cdba735b1118276716939119aceb8beba0a94c7ac59e063d0a994e28bc",
}

BASE_URL   = "https://2kfor2k.staceyboehman.com"
API_URL    = f"{BASE_URL}/wp-json/wp/v2/sbquestions"
HEADERS    = {"User-Agent": "Mozilla/5.0"}

CATEGORIES = {
    9:  "Clean Selling",
    18: "Consults and Evals",
    11: "Making Offers",
    12: "Model Help",
    13: "Money Beliefs",
    14: "Organic Marketing",
    15: "Overcoming Objections",
}

POSTS_PER_CATEGORY = 30
OUTPUT_FILE        = "coaching_qa.json"
DELAY_SECONDS      = 1.0


def get_post_ids_for_category(cat_id, count):
    ids = []
    page = 1
    while len(ids) < count:
        params = {
            "questioncategory": cat_id,
            "per_page": 100,
            "page": page,
            "_fields": "id,slug,title,date",
            "status": "publish",
        }
        resp = requests.get(API_URL, params=params, headers=HEADERS, cookies=COOKIES, timeout=15)
        if resp.status_code != 200:
            print(f"  API error {resp.status_code} on page {page}: {resp.text[:200]}")
            break
        batch = resp.json()
        if not batch:
            break
        ids.extend(batch)
        page += 1
        if len(batch) < 100:
            break
    random.shuffle(ids)
    return ids[:count]


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

    return question, answer


def main():
    results = []

    for cat_id, cat_name in CATEGORIES.items():
        print(f"\n[{cat_name}] Fetching post list...")
        posts = get_post_ids_for_category(cat_id, POSTS_PER_CATEGORY)
        print(f"  Got {len(posts)} posts. Scraping...")

        for i, post in enumerate(posts):
            slug  = post["slug"]
            title = post["title"]["rendered"]
            date  = post["date"][:10]

            question, answer = scrape_post(slug)

            if not question or not answer:
                print(f"  [{i+1}/{len(posts)}] SKIP (no Q or A): {title}")
                continue

            results.append({
                "category": cat_name,
                "title":    title,
                "date":     date,
                "url":      f"{BASE_URL}/sbquestions/{slug}/",
                "question": question,
                "answer":   answer,
            })
            print(f"  [{i+1}/{len(posts)}] OK: {title}")
            time.sleep(DELAY_SECONDS)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nDone! Saved {len(results)} Q&A pairs to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
