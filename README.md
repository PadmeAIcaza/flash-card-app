# Flashcard (French → English) 🃏

A simple **Tkinter flashcard app** that shows a French word, waits **3 seconds**, then flips to the English translation. You can mark whether you got it **Right (✓)** or **Wrong (✗)** and it keeps a running score of marks. :contentReference[oaicite:0]{index=0}

---

## Features
- Loads French/English words from a CSV file :contentReference[oaicite:1]{index=1}  
- Randomly selects a word each round :contentReference[oaicite:2]{index=2}  
- Auto-flips the card after **3000 ms (3 seconds)** :contentReference[oaicite:3]{index=3}  
- Buttons to mark answers: **✓** (right) and **✗** (wrong) :contentReference[oaicite:4]{index=4}  
- Score displayed as a growing string of marks (e.g., `✓✗✓✓`) :contentReference[oaicite:5]{index=5}  

---

## Requirements
- Python 3.x
- `pandas`
- Tkinter (usually included with Python)

Install `pandas`:
```bash
pip install pandas

```
```markdown
project/
├─ src/
│  └─ main.py
├─ data/
│  └─ french_words.csv
└─ images/
   ├─ card_front.png
   ├─ card_back.png
   ├─ right.png
   └─ wrong.png
```
