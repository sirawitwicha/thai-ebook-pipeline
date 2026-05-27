# Voice DNA Analysis — Scientific Methodology

## How to measure voice match (NOT just keywords)

Voice = rhythm + cadence + confidence. Keyword counting is a SUPPLEMENTAL metric only.

---

## Dimension 1: RHYTHM (sentence length distribution)

Extract all non-header, non-table lines from source text. Classify by char length:

```
STACCATO (<20 chars): punch lines, drops, emphasis
NATURAL (20-40 chars): explanations, flow, narration
FLOW (40+ chars): build-up, wind-up before the punch
```

### RedMaster baseline (from 2,521 line script, 86,583 chars):
```
STACCATO: 18% (459/2518 lines)  — "เข้าใจป่ะ", "สัส!", "แม่งโคตรง่าย"
NATURAL:  52% (1320/2518 lines) — "ผมไม่แนะนำให้ไปตามด่าเขา"
FLOW:     29% (739/2518 lines)  — "ตั้งใจลดอายุขัยของตัวเองเพื่อความบันเทิงของพวกมึงอย่างแท้จริง"
```

### Pattern: FLOW → STACCATO → FLOW → NATURAL → STACCATO
"ลากยาว → สับ → ลากยาว → ไหล → สับ"

### Scoring rule:
- Target: match the 18/52/29 distribution
- Deviation >10% in any category = rhythm mismatch
- Too much STACCATO (>28%) = over-punchy, feels aggressive
- Too much FLOW (>39%) = loses punch, feels like textbook

---

## Dimension 2: CADENCE (punctuation is THE enemy)

### CRITICAL FINDING:
RedMaster uses **ZERO em dashes (—)** in 86,583 characters.
DeepSeek V4-PRO injects em dashes as sentence connectors — this is an AI-ism.
Our first draft had **646 em dashes** across 8 chapters.

### The fix:
1. After writing → `grep '—' *.md` to count
2. If count > 0 → split every line containing — at the dash
3. Put each clause on its own line → natural rhythm restored
4. "ครับ" becomes the real punctuation (used 505x in original = 5.8/1000 chars)

### Jared's cadence tools:
- Line breaks as clause separators
- "ครับ" as period/comma (every 2-3 sentences)
- Short staccato lines as emphasis markers
- "..." sparingly (4x in 86K chars)

---

## Dimension 3: CONFIDENCE (declarative stance)

RedMaster states opinions as FACTS. He never hedges.

### Confidence markers:
```
"คือ..."      — declares a fact ("คือจุดแข็งของผม")
"ไม่ใช่..."   — dismisses wrong ideas with authority
"ผมเชื่อว่า..." — absolute certainty, no "think" or "maybe"
```

### Anti-confidence (AI patterns — CUT THESE):
```
"อาจจะ"      — hedging  → CUT
"น่าจะ"      — weak certainty → CUT
"คิดว่า"     — weak stance → CUT
"คงจะ"       — speculation → CUT
"น่าจะเป็น"  — double hedge → CUT HARD
```

### Confidence test:
- "คือจุดแข็งของผม" ✓  — declarative, no apology
- "ผมคิดว่าน่าจะเป็นจุดแข็ง" ✗ — double hedge, AI-ism

---

## DNA Scoring Algorithm

Score each chapter against baseline per 1000 characters:

```
markers = ["ครับ", "คือ", "แม่ง", "รู้มั้ย"]
baseline_per_1K = [5.8, 2.8, 1.5, 0.1]

For each marker:
  actual = (count_in_chapter / chapter_chars) * 1000
  ratio = min(actual / baseline, 2.0)  # cap at 200% to prevent single-marker distortion
  score += ratio

DNA_Score = (score / 4) * 100
```

### Scoring thresholds:
- 90%+ = excellent match
- 80-89% = good, minor tweaks only
- 60-79% = needs editing pass
- Below 60% = rewrite

### Common failure patterns:
- "ครับ" density <3.0/1K — DeepSeek under-uses terminal particles
- "แม่ง" density <0.5/1K — formality creep in later chapters
- "คือ" density <1.5/1K — passive voice replacing declarative style
- Em dashes present — western punctuation leaked through

---

## Full Harness Process

1. **Extract** — load voice sample (redmaster.md or similar), split into lines
2. **Baseline** — compute rhythm %, keyword density, confidence markers
3. **Constrain** — inject baseline as writing constraints into system prompt
4. **Write** — generate chapter with rhythm targets
5. **Validate** — run voice-check.py, score DNA match
6. **Correct** — strip em dashes, add missing "ครับ"/"คือ"/"แม่ง"
7. **Re-score** — verify 80%+ before approving chapter
