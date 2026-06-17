"""
Run this from C:\Users\jkrilov\Downloads\coaching_audio
(the folder where the MP3s already are)

Requirements already installed:
    onnx-asr, requests
    ffmpeg on PATH

This script transcribes all MP3s already in the current folder
using your local Parakeet TDT v3 model.
"""

import os
import re
import subprocess
import time
from pathlib import Path

import onnx_asr

MODEL_DIR      = Path(r"C:\Users\jkrilov\AppData\Roaming\com.pais.handy\models\parakeet-tdt-0.6b-v3-int8")
CHUNK_MINUTES  = 10
TRANSCRIPT_DIR = Path("coaching_call_transcripts")
TRANSCRIPT_DIR.mkdir(exist_ok=True)


def make_wav_chunks(mp3_path):
    chunk_dir = mp3_path.parent / (mp3_path.stem + "_chunks")
    chunk_dir.mkdir(exist_ok=True)
    existing = sorted(chunk_dir.glob("chunk_*.wav"))
    if existing:
        print(f"  Using {len(existing)} existing chunks")
        return existing
    print(f"  Splitting into {CHUNK_MINUTES}-min WAV chunks...")
    chunk_pattern = str(chunk_dir / "chunk_%03d.wav")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(mp3_path),
         "-ar", "16000", "-ac", "1",
         "-f", "segment", "-segment_time", str(CHUNK_MINUTES * 60),
         chunk_pattern],
        check=True, capture_output=True
    )
    chunks = sorted(chunk_dir.glob("chunk_*.wav"))
    print(f"  Created {len(chunks)} chunks")
    return chunks


def transcribe(mp3_path, model):
    chunks = make_wav_chunks(mp3_path)
    parts = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  Chunk {i}/{len(chunks)}...", end=" ", flush=True)
        t0 = time.time()
        result = model.recognize(str(chunk), language="en")
        text = getattr(result, "text", None) or (result if isinstance(result, str) else str(result))
        parts.append(text.strip())
        print(f"{time.time()-t0:.0f}s")
        chunk.unlink()
    chunk_dir = mp3_path.parent / (mp3_path.stem + "_chunks")
    try:
        chunk_dir.rmdir()
    except Exception:
        pass
    return " ".join(parts)


def save_transcript(mp3_path, transcript):
    out = TRANSCRIPT_DIR / (mp3_path.stem + ".md")
    # Use filename as title, clean it up
    title = mp3_path.stem.replace("_", " ").strip()
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n---\n\n")
        f.write(transcript)
        f.write("\n")
    print(f"  Saved: {out.name} ({out.stat().st_size // 1024}KB)")


def main():
    mp3s = sorted(Path(".").glob("*.mp3"))
    if not mp3s:
        print("No MP3 files found in current folder.")
        print(f"Run this script from the folder containing the MP3s.")
        return

    print(f"Found {len(mp3s)} MP3 files to transcribe\n")

    print(f"Loading Parakeet model...")
    model = onnx_asr.load_model(
        "nemo-parakeet-tdt-0.6b-v3",
        path=str(MODEL_DIR),
        quantization="int8",
    )
    print("Model loaded.\n")

    for i, mp3 in enumerate(mp3s, 1):
        out = TRANSCRIPT_DIR / (mp3.stem + ".md")
        if out.exists():
            print(f"[{i}/{len(mp3s)}] SKIP (already transcribed): {mp3.name}")
            continue
        print(f"[{i}/{len(mp3s)}] {mp3.name}")
        try:
            transcript = transcribe(mp3, model)
            save_transcript(mp3, transcript)
        except Exception as e:
            print(f"  ERROR: {e}")
        print()

    print(f"Done! Transcripts in: {TRANSCRIPT_DIR.resolve()}")


if __name__ == "__main__":
    main()
