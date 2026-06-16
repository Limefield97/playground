"""
Run this on your PC.
Requirements:
    pip install requests onnx-asr
    ffmpeg must be installed and on PATH (used to convert MP3 -> WAV)
      Windows: winget install ffmpeg

This script:
1. Downloads the 25 most recent Stacey-only live coaching MP3s
2. Converts each to 16kHz mono WAV (required by Parakeet)
3. Transcribes with your local Parakeet TDT v3 model
4. Saves transcripts as .md files ready to upload to Claude Projects
"""

import requests
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import onnx_asr

AUTH    = ("krilov@gmail.com", "86ZpqEPQX_*Tn")
HEADERS = {"User-Agent": "Mozilla/5.0"}
FEED    = "https://2kfor2k.staceyboehman.com/feed/2k-members/"
GUESTS  = re.compile(
    r"\bwith\s+(Janessa Dean|Olivia Vizachero|Melissa Parsons|Courtney Gray"
    r"|Maggie Reyes|Clare Ochoa|Jille Dunsmore|Piper|Amy Latta)\b", re.I
)

MODEL_DIR      = Path(r"C:\Users\jkrilov\AppData\Roaming\com.pais.handy\models\parakeet-tdt-0.6b-v3-int8")
DOWNLOAD_DIR   = Path("coaching_audio")
TRANSCRIPT_DIR = Path("coaching_call_transcripts")
NUM_CALLS      = 25

DOWNLOAD_DIR.mkdir(exist_ok=True)
TRANSCRIPT_DIR.mkdir(exist_ok=True)


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
    filepath  = DOWNLOAD_DIR / f"{idx:02d}_{safe_name}.mp3"
    if filepath.exists():
        print(f"  Already downloaded: {filepath.name}")
        return filepath
    print(f"  Downloading: {ep['title'][:60]}...")
    resp = requests.get(ep["url"], auth=AUTH, headers=HEADERS, stream=True, timeout=120)
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
    print(f"    Done ({filepath.stat().st_size / 1024 / 1024:.1f} MB)")
    return filepath


def convert_to_wav(mp3_path):
    """Convert MP3 to 16kHz mono WAV using ffmpeg (required by Parakeet)."""
    wav_path = mp3_path.with_suffix(".wav")
    if wav_path.exists():
        return wav_path
    print(f"  Converting to WAV...")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(mp3_path), "-ar", "16000", "-ac", "1", str(wav_path)],
        check=True, capture_output=True
    )
    return wav_path


def transcribe(wav_path, model):
    print(f"  Transcribing with Parakeet...")
    t0 = time.time()
    result = model.recognize(str(wav_path), language="en")
    elapsed = time.time() - t0
    text = getattr(result, "text", None) or (result if isinstance(result, str) else str(result))
    print(f"    Done in {elapsed:.0f}s")
    return text.strip()


def save_transcript(ep, transcript, idx):
    safe_name = re.sub(r'[^\w\-]', '_', ep["title"])[:60]
    filepath  = TRANSCRIPT_DIR / f"live_call_{idx:02d}_{safe_name}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {ep['title']}\n\n")
        f.write(f"**Date:** {ep['date']}\n\n")
        f.write("---\n\n")
        f.write(transcript)
        f.write("\n")
    print(f"  Saved: {filepath.name} ({filepath.stat().st_size // 1024}KB)")
    return filepath


def main():
    episodes = get_stacey_episodes()
    print(f"Found {len(episodes)} Stacey-only calls to process\n")

    print(f"Loading Parakeet model from {MODEL_DIR}...")
    model = onnx_asr.load_model(
        "nemo-parakeet-tdt-0.6b-v3",
        path=str(MODEL_DIR),
        quantization="int8",
    )
    print("Model loaded.\n")

    for i, ep in enumerate(episodes, 1):
        print(f"[{i}/{len(episodes)}] {ep['title'][:70]}")
        try:
            mp3_path = download_mp3(ep, i)
            wav_path = convert_to_wav(mp3_path)
            transcript = transcribe(wav_path, model)
            save_transcript(ep, transcript, i)
            wav_path.unlink()  # delete WAV after transcribing (MP3 kept for resume)
        except Exception as e:
            print(f"  ERROR: {e}")
        print()

    print(f"Done! Transcripts saved to ./{TRANSCRIPT_DIR}/")
    print("Upload those .md files to your Claude Project.")


if __name__ == "__main__":
    main()
