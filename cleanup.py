import json
import html
import re
from collections import defaultdict

with open("coaching_qa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Before cleanup: {len(data)} entries")

def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = text.strip()
    return text

seen = set()
cleaned = []
dupes = 0

for item in data:
    url = item["url"]
    if url in seen:
        dupes += 1
        continue
    seen.add(url)

    cleaned.append({
        "category": item["category"],
        "title":    html.unescape(item["title"]),
        "date":     item["date"],
        "url":      item["url"],
        "question": clean_text(item["question"]),
        "answer":   clean_text(item["answer"]),
    })

print(f"Duplicates removed: {dupes}")
print(f"After cleanup: {len(cleaned)} entries")

with open("coaching_qa.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)

# Regenerate markdown files
by_category = defaultdict(list)
for item in cleaned:
    by_category[item["category"]].append(item)

for category, items in by_category.items():
    filename = f"coaching_{category.lower().replace(' ', '_').replace('&', 'and')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Coaching Q&A: {category}\n\n")
        for item in items:
            f.write(f"## {item['title']}\n\n")
            f.write(f"**Date:** {item['date']}\n\n")
            f.write(f"**QUESTION:**\n\n{item['question']}\n\n")
            f.write(f"**ANSWER:**\n\n{item['answer']}\n\n")
            f.write("---\n\n")
    print(f"Saved {filename} ({len(items)} entries)")
