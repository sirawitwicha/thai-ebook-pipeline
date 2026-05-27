# RedMaster Voice DNA — Quantitative Baseline

Extracted from redmaster.md (2,521 lines, 84,062 chars).

## Word Frequency (per 1000 chars — NON-NEGOTIABLE targets)

| Marker | Count | Per 1000 chars | Role |
|--------|-------|---------------|------|
| `ครับ` | 505 | **5.8** | THE signature. Must appear at least 3.0/1K in every chapter. |
| `คือ` | 244 | **2.8** | Primary declarative connector. NOT "ซึ่ง", NOT "โดย" |
| `แม่ง` | 128 | **1.5** | Emphasis spice. Must appear at least 0.5/1K in every chapter. |
| `มึง` | 297 | 3.4 | Intimate address (แต่ USER ห้ามใช้ — ebook use "คุณ") |
| `กู` | 202 | 2.3 | Self-reference (แต่ USER ห้ามใช้ — ebook use "ผม") |
| `รู้มั้ย` | 7 | 0.1 | Rhetorical engagement |

## Rhythm Distribution (sentence-length profile)

Analyzed against non-empty, non-heading lines:

| Category | Chars | Percentage | Purpose |
|----------|-------|-----------|---------|
| STACCATO | <20 | **18%** | Punch lines. "เข้าใจป่ะ", "สัส!", "คือจุดแข็งของผม" |
| NATURAL | 20-40 | **52%** | Explanation flow, the bulk |
| FLOW | 40+ | **29%** | Build-up, wind-up before the punch |

**Sentence avg:** 32 chars. Median: 31 chars.

## Cadence Pattern

The signature rhythm is:
```
FLOW (40+ chars)   — "ตั้งใจลดอายุขัยของตัวเองเพื่อความบันเทิงของพวกมึงอย่างแท้จริง"
  ↓
STACCATO (<20)     — "และนั่นแหละครับ"  ← PUNCH
  ↓
NATURAL (20-40)    — "ผมเชื่อว่าสิ่งที่ผมทำได้ดีที่สุดครับ"
  ↓
STACCATO (<20)     — "และไม่กล้าที่จะทำ"  ← PUNCH
```

**Do NOT write all NATURAL.** That's monotonous, soulless. The STACCATO punches are what make Jared's voice.

## Confidence Markers (zero hedging)

Jared NEVER hedges. He states facts.

Patterns:
- "คือ..." → "คือจุดแข็งของผม", "คือกับดักครับ"
- "ไม่ใช่...แต่..." → dismissing wrong ideas
- "คุณรู้มั้ยครับว่า..." → rhetorical engagement
- Short declarative: "แม่งโคตรง่าย", "เข้าใจป่ะ"

**ANTI-PATTERN (KILLS VOICE):**
- "อาจจะ...", "น่าจะ...", "คิดว่า...", "คงจะ..."

## Scoring Methodology

```python
# Score a chapter against baseline
for marker in ["ครับ", "คือ", "แม่ง"]:
    actual = (text.count(marker) / len(text)) * 1000
    target = baseline[marker]
    ratio = min(actual / target, 2.0)  # cap at 200%
    scores.append(ratio)

voice_score = sum(scores) / len(scores) * 100
# ≥70% = acceptable
# <70% = rewrite
```

## Gotcha: Model-Specific Drift

DeepSeek V4-PRO writes vivid Thai stories but:
- UNDER-uses "ครับ" by 2-3x (2.0-3.0/1K vs 5.8 target)
- Almost completely DROPS "แม่ง" after first chapter (0.0/1K)
- Writes too many NATURAL sentences (50-60%), too few STACCATO

This is NOT fixable with better prompting — requires post-processing injection of missing markers.
