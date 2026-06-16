import json
from collections import defaultdict

with open("coaching_qa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

by_category = defaultdict(list)
for item in data:
    by_category[item["category"]].append(item)

for category, items in by_category.items():
    filename = f"coaching_{category.lower().replace(' ', '_').replace('&', 'and')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Coaching Q&A: {category}\n\n")
        for item in items:
            f.write(f"## {item['title']}\n\n")
            f.write(f"**QUESTION:**\n\n{item['question']}\n\n")
            f.write(f"**ANSWER:**\n\n{item['answer']}\n\n")
            f.write("---\n\n")
    print(f"Saved {filename} ({len(items)} entries)")
