import json
import html
import re
from math import ceil

with open("coaching_mindset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

# Clean all entries
for item in data:
    item["title"]    = html.unescape(item["title"])
    item["question"] = clean_text(item["question"])
    item["answer"]   = clean_text(item["answer"])

# Split into 7 equal chunks
n = len(data)
chunk_size = ceil(n / 7)
chunks = [data[i:i+chunk_size] for i in range(0, n, chunk_size)]

for idx, chunk in enumerate(chunks, 1):
    filename = f"coaching_mindset_part{idx}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Coaching Q&A: Mindset & Universal — Part {idx} of {len(chunks)}\n\n")
        for item in chunk:
            f.write(f"## {item['title']}\n\n")
            f.write(f"**Date:** {item['date']}  \n")
            f.write(f"**Topics:** {', '.join(item['tags'])}\n\n")
            f.write(f"**QUESTION:**\n\n{item['question']}\n\n")
            f.write(f"**ANSWER:**\n\n{item['answer']}\n\n")
            f.write("---\n\n")
    import os
    size_kb = os.path.getsize(filename) // 1024
    print(f"Saved {filename} — {len(chunk)} entries, {size_kb}KB")
