# RedMaster Voice Harness — Quantitative DNA

Load this before any Thai writing pass. Contains actual voice patterns extracted from the 2,521-line script, not guesses.

## Baseline Metrics (84,062 chars of RedMaster script)

| Marker | Count | Per 1K Chars | % of Lines |
|--------|-------|-------------|------------|
| `ครับ` | 505 | 5.8 | ~24% |
| `คือ` | 244 | 2.8 | ~10% |
| `แม่ง` | 128 | 1.5 | ~5% |
| `มึง` | 297 | — | NOT IN BOOKS |
| `กู` | 202 | — | NOT IN BOOKS |
| `ไอ้` | 60 | 0.7 | — |
| `โคตร` | 9 | 0.1 | — |
| `สัส` | 18 | 0.2 | — |
| `รู้มั้ย` | 7 | 0.08 | — |
| `เข้าใจป่ะ` | 4 | 0.05 | — |
| `เอาจริง` | 10 | 0.12 | — |
| `อิอิ` | 1 | — | — |

## Sentence Structure
- Mean: 32 chars
- Median: 31 chars
- Stdev: 13 chars
- Range: 2-85 chars

## Paragraph Structure
- 1-3 sentences per paragraph
- New paragraph every 3-4 lines
- No walls of text. Ever.

## Signature Patterns (verbatim from script)

### Openers:
- "เล่าเรื่องให้ฟังครับ..."
- "คุณรู้มั้ยครับว่า..."
- "คือ..." (explanation opener)
- "เอาจริง ๆ..." (honesty moment before critique)
- Story first → analysis second → solution third

### Closers:
- Rhetorical question + punch line
- "แต่นั่นมันยังไม่ใช่ทั้งหมดครับ"
- "เปิดหน้าถัดไปครับ — แล้วคุณจะรู้ว่า..."

### Mid-paragraph rhythm:
- Short sentence (15-25 chars)
- Short sentence (15-25 chars) 
- Longer explanation (40-50 chars)
- Short punch (10-20 chars)
- "ครับ"

## Book Adaptation Rules (from user feedback)

| Script (Raw) | Book (Adapted) |
|-------------|----------------|
| กู, มึง → ❌ CUT entirely | ใช้ "ผม", "คุณ" |
| Pantip quotes → ❌ "ดู cheap" | ใช้ story จากประสบการณ์ |
| Raw curse words → keep ~30% | "แม่ง" 1-2x per chapter max |
| "ครับ" density: 5.8/1K | Target: 3-5/1K (slightly less than raw script) |
| "คือ" density: 2.8/1K | Target: 2-3/1K |

## Chapter Validation Script

```python
import pathlib, json

BASELINE = {"ครับ": 5.8, "คือ": 2.8, "แม่ง": 1.5}

def score_chapter(path):
    text = path.read_text(encoding="utf-8")
    chars = max(len(text), 1)
    results = {}
    for marker, base in BASELINE.items():
        per_k = (text.count(marker) / chars) * 1000
        pct = (per_k / base) * 100
        status = "✅" if pct >= 50 else ("⚠️" if pct >= 30 else "❌")
        results[marker] = {"per_k": per_k, "base": base, "pct": pct, "status": status}
    return results

# Run on all chapters
drafts_dir = pathlib.Path("ebook-pipeline/drafts/")
for f in sorted(drafts_dir.glob("0*.md")):
    scores = score_chapter(f)
    failed = [m for m, s in scores.items() if s["status"] == "❌"]
    status = "❌ NEEDS FIX" if failed else "✅ PASS"
    print(f"{status} {f.name}")
    if failed:
        for m in failed:
            s = scores[m]
            print(f"  {m}: {s['per_k']:.1f}/1K (need {s['base']:.1f})")
```

## When to Run Validation

1. After writing any chapter
2. After editing any chapter
3. Before PDF export (final quality gate)
4. Before showing to user — if it wouldn't pass, don't show it
