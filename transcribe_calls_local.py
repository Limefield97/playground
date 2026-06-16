"""
Run this on your PC (not in the cloud).
Requirements:
    pip install openai-whisper requests
    # Also needs ffmpeg: https://ffmpeg.org/download.html

This script:
1. Downloads the 25 most recent Stacey-only live coaching MP3s
2. Transcribes each with Whisper (runs locally, free, no API key needed)
3. Saves transcripts as individual .md files ready to upload to Claude Projects
"""

import requests
import json
import os
import re
import time
import whisper

AUTH    = ("krilov@gmail.com", "86ZpqEPQX_*Tn")
HEADERS = {"User-Agent": "Mozilla/5.0"}
FEED    = "https://2kfor2k.staceyboehman.com/feed/2k-members/"
GUESTS  = re.compile(
    r"\bwith\s+(Janessa Dean|Olivia Vizachero|Melissa Parsons|Courtney Gray"
    r"|Maggie Reyes|Clare Ochoa|Jille Dunsmore|Piper|Amy Latta)\b", re.I
)

DOWNLOAD_DIR   = "coaching_audio"
TRANSCRIPT_DIR = "coaching_call_transcripts"
NUM_CALLS      = 25
WHISPER_MODEL  = "base"   # options: tiny, base, small, medium, large
                           # base = good quality, ~1GB RAM, ~3-5 min per hour of audio
                           # small = better, ~2GB RAM, ~5-8 min per hour
                           # medium = best without GPU, ~5GB RAM, ~15 min per hour

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)


def get_stacey_episodes():
    import xml.etree.ElementTree as ET
    print("Fetching RSS feed...")
    resp = requests.get(FEED, auth=AUTH, headers=HEADERS, timeout=20)
    root = ET.fromstring(resp.text)
    episodes = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "").strip()
        enc   = item.find("enclosure")
        mp3   = enc.get("url") if enc is not None else ""
        date  = item.findtext("pubDate", "")[:16]
        if not GUESTS.search(title) and mp3:
            episodes.append({"title": title, "date": date, "url": mp3})
    return episodes[:NUM_CALLS]


def download_mp3(ep, idx):
    safe_name = re.sub(r'[^\w\-]', '_', ep["title"])[:60]
    filename  = f"{idx:02d}_{safe_name}.mp3"
    filepath  = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.exists(filepath):
        print(f"  Already downloaded: {filename}")
        return filepath
    print(f"  Downloading: {ep['title'][:60]}...")
    resp = requests.get(ep["url"], auth=AUTH, headers=HEADERS, stream=True, timeout=60)
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
    size_mb = os.path.getsize(filepath) / (1024 * 1024)
    print(f"    Done ({size_mb:.1f} MB)")
    return filepath


def transcribe(audio_path, model):
    print(f"  Transcribing with Whisper ({WHISPER_MODEL})...")
    result = model.transcribe(audio_path, language="en", verbose=False)
    return result["text"].strip()


def save_transcript(ep, transcript, idx):
    safe_name = re.sub(r'[^\w\-]', '_', ep["title"])[:60]
    filename  = f"live_call_{idx:02d}_{safe_name}.md"
    filepath  = os.path.join(TRANSCRIPT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {ep['title']}\n\n")
        f.write(f"**Date:** {ep['date']}\n\n")
        f.write("---\n\n")
        f.write(transcript)
        f.write("\n")
    size_kb = os.path.getsize(filepath) // 1024
    print(f"  Saved: {filename} ({size_kb}KB)")
    return filepath


def main():
    episodes = get_stacey_episodes()
    print(f"Found {len(episodes)} Stacey-only calls to process\n")

    print(f"Loading Whisper model '{WHISPER_MODEL}'...")
    model = whisper.load_model(WHISPER_MODEL)
    print("Model loaded.\n")

    for i, ep in enumerate(episodes, 1):
        print(f"[{i}/{len(episodes)}] {ep['title'][:70]}")
        try:
            audio_path = download_mp3(ep, i)
            transcript = transcribe(audio_path, model)
            save_transcript(ep, transcript, i)
            # Optional: delete MP3 after transcribing to save disk space
            # os.remove(audio_path)
        except Exception as e:
            print(f"  ERROR: {e}")
        print()

    print(f"Done! Transcripts saved to ./{TRANSCRIPT_DIR}/")
    print("Upload those .md files to your Claude Project alongside the other files.")


if __name__ == "__main__":
    main()
