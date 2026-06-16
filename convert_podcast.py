import json
from math import ceil

with open("podcast_transcripts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter out near-empty entries
data = [ep for ep in data if len(ep["transcript"]) > 1000]
print(f"Episodes with real content: {len(data)}")

# Split into chunks that stay under ~400KB each
chunk_size = 10
chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

for idx, chunk in enumerate(chunks, 1):
    filename = f"podcast_part{idx:02d}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Make Money as a Life Coach Podcast — Part {idx} of {len(chunks)}\n\n")
        for ep in chunk:
            f.write(f"## {ep['title']}\n\n")
            f.write(f"**URL:** {ep['url']}\n\n")
            f.write(ep["transcript"])
            f.write("\n\n---\n\n")
    import os
    size_kb = os.path.getsize(filename) // 1024
    print(f"Saved {filename} — {len(chunk)} episodes, {size_kb}KB")
