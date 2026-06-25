"""
Run from C:\Users\jkrilov\Downloads\coaching_audio

Downloads the next 15 Stacey-only calls from the private 2K podcast feed
that are NOT already in the current folder.

Stacey-only = episode title has no person's name (no "with [Name]" pattern)
"""

import os
import re
import time
import requests
import xml.etree.ElementTree as ET
from pathlib import Path

FEED_URL  = "https://2kfor2k.staceyboehman.com/feed/2k-members/"
USERNAME  = "krilov@gmail.com"
PASSWORD  = "86ZpqEPQX_*Tn"
LIMIT     = 15
OUT_DIR   = Path(".")

# Titles with a guest/client name typically contain "with [Name]" or "Coaching [Name]"
# Stacey's own calls are group calls with no named guest
NAME_PATTERN = re.compile(
    r'\bwith\s+[A-Z][a-z]+\b'          # "with Jennifer"
    r'|\bCoaching\s+[A-Z][a-z]+\b'     # "Coaching Sarah"
    r'|\b[A-Z][a-z]+\s+[A-Z][a-z]+\b', # "Jenny Meenan" style full names
    re.IGNORECASE
)

def is_stacey_call(title):
    # Keep calls that look like group/teaching calls, skip named-client calls
    return not NAME_PATTERN.search(title)

def sanitize(title):
    title = re.sub(r'[\\/*?:"<>|]', '_', title)
    title = re.sub(r'\s+', '_', title.strip())
    return title[:80]

def already_downloaded():
    return {f.stem.lower() for f in OUT_DIR.glob("*.mp3")}

def fetch_feed():
    print("Fetching RSS feed...")
    resp = requests.get(FEED_URL, auth=(USERNAME, PASSWORD), timeout=30)
    resp.raise_for_status()
    return ET.fromstring(resp.content)

def main():
    existing = already_downloaded()
    print(f"Already have {len(existing)} MP3s in folder\n")

    root = fetch_feed()
    ns = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}
    items = root.findall('.//item')
    print(f"Feed has {len(items)} episodes total\n")

    downloaded = 0
    skipped_existing = 0
    skipped_named = 0

    for item in items:
        if downloaded >= LIMIT:
            break

        title_el = item.find('title')
        title = title_el.text.strip() if title_el is not None else 'unknown'

        enclosure = item.find('enclosure')
        if enclosure is None:
            continue
        url = enclosure.get('url', '')
        if not url:
            continue

        safe = sanitize(title)
        if safe.lower() in existing:
            skipped_existing += 1
            continue

        if not is_stacey_call(title):
            skipped_named += 1
            print(f"  SKIP (named client): {title}")
            continue

        filename = OUT_DIR / f"{safe}.mp3"
        print(f"[{downloaded+1}/{LIMIT}] {title}")
        print(f"  Downloading {url[:80]}...")

        try:
            r = requests.get(url, auth=(USERNAME, PASSWORD), stream=True, timeout=60)
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=65536):
                    f.write(chunk)
            size_mb = filename.stat().st_size / 1_000_000
            print(f"  Saved: {filename.name} ({size_mb:.1f}MB)\n")
            downloaded += 1
            time.sleep(1)
        except Exception as e:
            print(f"  ERROR: {e}\n")

    print(f"Done! Downloaded {downloaded} new calls")
    print(f"Skipped {skipped_existing} already in folder, {skipped_named} named-client calls")

if __name__ == "__main__":
    main()
