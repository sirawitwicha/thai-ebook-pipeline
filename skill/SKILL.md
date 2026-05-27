---
name: thai-ebook-pipeline
description: "Thai ebook pipeline in RedRemasterRed voice — research, two-pass writing (content+soul+DNA validation), fast editing, PDF export, marketing kit"
version: 4.2.0
author: Hermes Agent
tags: [thai, ebook, writing, redremasterred, voice, pdf, marketing, research]
category: creative
---

# Thai Ebook Pipeline — v4

Write short-read ebooks (40-60 pages) in Thai with the **วาทศิลป์ของจาเร็ด (RedRemasterRed)** — ตลก แหลม คม มีเรื่องเล่า ไม่ใช่สอน

## Directory Structure

```
ebook-pipeline/
├── reference/
│   ├── voice-samples/       ← ตัวอย่างเสียง RedMaster (.md) ใช้ calibrate voice
│   └── voice-profile.md     ← Voice rules (auto-loaded)
├── market-data/
│   ├── raw/                 ← ข้อมูลดิบจาก Apify / Web research
│   └── analysis/            ← สรุป pain points + trends
├── drafts/                  ← ต้นฉบับ (บทละไฟล์)
└── output/                  ← PDF + marketing kit
```

## When to use

- User says "write an ebook in Thai"
- User says "rewrite this in RedMaster style", "make it have soul", "must be ตลก", "มีวาทศิลป์"
- User references RedRemasterRed, Redmaster, or JaredRedmaster style
- User wants Thai content that doesn't sound like generic AI writing

## The Voice: RedRemasterRed Profile (CRITICAL — user rejects without this)

### Hard Rules from Actual Usage (do NOT violate):
| Rule | Reason | Example |
|------|--------|---------|
| ❌ NO "มึง/กู" ในหนังสือ | User explicitly rejected | ใช้ "คุณ" "ผม" แทน |
| ❌ NO Pantip quotes เปิดบท | User said "ดู cheap" | ใช้ story จริง หรือ "เล่าเรื่องให้ฟังครับ" |
| ❌ NO ภาษาไทยทางการ | AI-ism | "อย่างไรก็ตาม" "ทั้งนี้" "กล่าวคือ" = ตัดทิ้ง |
| ❌ NO passive voice | ฟังดูแปล | "ถูกนำมาใช้" → "ใช้", "ถูกพัฒนา" → "พัฒนาขึ้น" |
| ✅ ใช้ "ครับ" ลงท้ายสม่ำเสมอ | Signature pattern | "ครับ" ~500 ครั้งใน script จริง |
| ✅ ใช้ "แม่ง" เป็นจังหวะ | Emphasis, not main dish | 1-2 ครั้งต่อบท พอ |
| ✅ เปิดด้วย Story เสมอ | Never open with concept | "เล่าเรื่องให้ฟังครับ... เมื่ออาทิตย์ที่แล้ว..." |
| ✅ ตัวเลขเจาะจง | สร้าง credibility | 80,000 ไม่พอ, 25=6.2M vs 35=2.3M |
| ✅ มีมุกแทรก | ยิ่งซีเรียส ยิ่งต้องมีมุก | "คือการเอาน้ำมันราดไฟแล้วคิดว่าดับ" |

### Core Writing Techniques (วาทศิลป์แบบจาเร็ด)

1. **เปิดด้วย Story, ไม่ใช่ Concept** — "เมื่ออาทิตย์ที่แล้ว ผมนั่งกินข้าวกับเพื่อน..." ดีกว่า "คุณรู้มั้ยว่าคนส่วนใหญ่..."
2. **Contrast / Irony** — คนภายนอกดูรวย แต่ภายในพัง
3. **ตั้งสมมุติฐานแล้วทุบ** — "คุณคิดว่า... แต่ความจริงคือ..."
4. **ประโยคสับจังหวะ** — สั้น-ยาว-สั้น-ยาว สลับ เหมือนดนตรี
5. **"ครับ" เป็น musical punctuation** — ลงท้ายทุก 2-3 ประโยค สร้าง rhythm
6. **"คือ" แทน hedging** — ความมั่นใจ ไม่ใช่ "อาจจะ" "น่าจะ"
7. **"แม่ง" เป็นเครื่องเทศ** — 1-2 ครั้งต่อบท พอ ต้องรู้สึก earned

### Book Format Rules (PROVEN — 35,800 chars across 8 chapters)

**THIS IS A BOOK, NOT A SOCIAL MEDIA POST.** The #1 mistake is writing one-sentence-per-line like Twitter threads.

✅ **BOOK (correct):**
```
ผมอยากเล่าเรื่องของรุ่นพี่คนหนึ่งให้ฟังครับ ขอเรียกว่า "พี่เอ" แล้วกัน
พี่เอเป็นคนเก่งที่คุณน่าจะเจอได้ในทุกออฟฟิศในกรุงเทพ เรียนจบวิศวะ
จากมหาลัยรัฐ เกรดไม่ถึงขั้นเกียรตินิยมแต่ก็ดีพอที่จะสมัครงานบริษัทใหญ่
ได้ตั้งแต่ยังไม่รับปริญญา

ปีแรกที่ทำงาน เงินเดือน 25,000 บาท ตอนนั้นชีวิตของพี่เอคือชีวิตของ
เด็กจบใหม่ที่คุณคงเคยผ่านมาแล้ว หอพัก 3,500 บาทที่ไม่มีแม้แต่แอร์
กินข้าวราดแกง 60 บาท เดินทางด้วยรถเมล์ที่ร้อนจนเหงื่อแตกตั้งแต่เช้า
```

❌ **SOCIAL POST (wrong):**
```
ผมอยากเล่าเรื่องของรุ่นพี่คนหนึ่งให้ฟังครับ
ขอเรียกว่า "พี่เอ" แล้วกัน

พี่เอเป็นคนเก่งครับ
เป็นคนเก่งที่คุณน่าจะเจอได้ในทุกออฟฟิศในกรุงเทพ
เรียนจบวิศวะจากมหาลัยรัฐ
```

**Rules:**
- Paragraphs merge related ideas into flowing text (3-5 sentences per paragraph)
- Line breaks reserved for emphasis moments — the punch AFTER the buildup
- Books breathe. Readers need description, scene, atmosphere — not just information
- Target: 3,000-7,000 chars per chapter for short-read books

### Em Dash (—) = THE ENEMY

**Jared uses ZERO em dashes in 86,000 chars of script.**
DeepSeek injects them automatically — it's the #1 AI-ism in Thai writing.

❌ NEVER: "คือเพื่อนที่คุณคิดว่าประสบความสำเร็จที่สุด — คือคนที่รู้สึกจนที่สุด"
✅ ALWAYS: "คือเพื่อนที่คุณคิดว่าประสบความสำเร็จที่สุด คือคนที่รู้สึกจนที่สุด"

After writing, ALWAYS run: `chapter.replace("—", " ")` — must be zero.

### Quality Scoring (Run after every 3-5 chapter batch)

Score every chapter against RedMaster baseline:

| Metric | Target | How to check |
|--------|--------|--------------|
| "ครับ"/1000 chars | 4.0-6.0 | `text.count("ครับ")/len(text)*1000` |
| "คือ"/1000 chars | 3.0-7.0 | `text.count("คือ")/len(text)*1000` |
| "แม่ง"/1000 chars | 0.5-2.0 | `text.count("แม่ง")/len(text)*1000` |
| Em dashes | **0** | `text.count("—")` — must be zero |
| Voice DNA Score | >70% | Weighted avg of above vs baseline |
| Chapter length | 3,000-7,000 chars | `len(text)` |

**If score < 70%:** Rewrite. Don't ship weak chapters.

### Per-Chapter Structure (Book Format)

```
1. SCENE (1-2 paragraphs) — specific story, vivid details, atmosphere
2. TRANSITION (1 paragraph) — bridge from story to lesson
3. LESSON (3-5 paragraphs) — the meat, numbers, examples, contrast
4. SOLUTION/PREVIEW (1-2 paragraphs) — what to do / what's next
5. CLIFFHANGER (1 paragraph) — hook for next chapter
```
8. **ตัวเลขชัดเจน** — 80,000 เก็บไม่ได้ / 25=6.2M vs 35=2.3M (มีตัวเลข anchor ให้คน visualize)
9. **มุกแทรกในจังหวะซีเรียส** — ยิ่งเนื้อหาหนัก ยิ่งต้องมีมุกคั่น
10. **ไม่ใช่สอน แต่ "เล่าให้ฟัง"** — ใช้ "ครับ" ไม่ใช่ "ควรจะ"
11. **Simile เปรียบเทียบมั่วแต่แม่น** — "เหมือนกินหมูกระทะฟรี แต่ต้องจ่ายห้อง ICU"

## Pipeline Overview

### Stage 0: Customer Voice Mining (CRITICAL for ad copy + outline)

**Goal:** Find exact words, phrases, and pain points real customers use — not what you think they feel.

**Sources (ใน order ของ effectiveness):**
1. **Reddit Search Scraper** (Apify: `pb74arTxftNSjmZp2`) — search pain points with "searches" field
   - Input format: `{"searches":[{"query":"...","maxPosts":15},...], "includeComments":true}`
   - Collect: post titles + top comments = real customer wording
2. **Amazon Review Scraper** (Apify: `bYWmT1ZFYWbl859nG`) — see what people praise/complain about
3. **RAG Web Browser** (Apify: `3ox4R101TgZz67sLr`) — general web + niche research
4. **YouTube Comments Scraper** (Apify: `p7UMdpQnjKmmpR21D`) — comments on Thai videos
   - Input format: `{"videoUrls":["https://..."]}`
5. **Google Trends** (Apify: `DyNQEYDj9awfGQf9A`) — demand validation
   - Input format: `{"keywords":["..."], "geo":"TH", "timeRange":"today 3-m"}`

**สิ่งที่ต้องเก็บ:**
- คำพูดตรงๆ ของคนมีปัญหา (สำหรับใช้เป็น ad hook)
- ศัพท์ที่ลูกค้าใช้ vs ศัพท์ที่คนเขียนหนังสือใช้
- Pain point priority (อะไรเจ็บที่สุด)
- ข้อที่คน complain ว่าหนังสือ/คอร์สที่มีอยู่ไม่ดี

**Analysis Output:** `market-data/analysis/market-brief.md`

### Stage 1: Outline & Approval
1. Map each pain point → 1 chapter
2. Voice calibration: เขียน 1 ย่อหน้าตัวอย่าง RedMaster style ให้ approve ก่อน — **ผู้ใช้จะ reject ถ้า tone ไม่ตรง**
3. User approves → start writing

### Stage 2: Writing — TWO-PASS METHOD (CRITICAL)

⚠️ **One-pass writing will be rejected.** The user has explicitly rejected raw model output. Two-pass is mandatory.

#### Pass 1: Structure + Content
```
1. HOOK — เปิดด้วย story จริง, ตัวอย่างจากชีวิต (never Pantip quotes)
2. STAKES — "นี่คือปัญหาที่คนเป็นล้านเจอ"
3. ANALYSIS — "แล้วทำไมถึงเป็นแบบนั้น?"
4. CONTRAST — "สิ่งที่คนส่วนใหญ่ทำ VS สิ่งที่ควรทำ"
5. SOLUTION — ขั้นตอนชัดเจน, ตัวเลขเฉพาะ
6. CLIFFHANGER — เชื่อมบทหน้า
```

#### Pass 2: "Soul Pass" (REQUIRED — user WILL reject without this)
After Pass 1, go through every paragraph and inject:
- Rhetorical questions ("คุณรู้มั้ยครับว่า...", "แล้วคุณคิดว่าเกิดอะไรขึ้น?")
- Contrast/Irony ("ภายนอกดูดี แต่ภายในพัง")
- ประชดตัวเอง ("ผมก็เคยโง่แบบนั้น")
- ตัวเลขตอกย้ำ
- ประโยคสับจังหวะ
- Closing คม
- มุกแทรก ("ดอกเบี้ยทำงานเงียบๆเหมือนแมวเดิน")

**ตรวจสอบ Pass 2 checklist:**
- [ ] เปิดด้วย story จริง ไม่ใช่ concept
- [ ] มี rhetorical question อย่างน้อย 1 จุดต่อย่อหน้า
- [ ] มี contrast จุดที่คนอ่าน "อ้าว!"
- [ ] มีมุกคั่นตอนเนื้อหาหนัก
- [ ] มีตัวอย่างตัวเลขเจาะจง
- [ ] "ครับ" ลงท้ายสม่ำเสมอ
- [ ] ไม่มี "มึง/กู"
- [ ] ไม่มี quote Pantip
- [ ] ไม่มีภาษาไทยทางการ
- [ ] มี closing คมก่อนจบบท

### Stage 4: Editing & Iteration
- File structure: `ebook-pipeline/drafts/01-*.md`, `02-*.md`, etc.
- แก้ได้เฉพาะจุด: `patch(old_string="...", new_string="...")`

### Stage 5: PDF Export
ใช้ FPDF2 + Sarabun font

### Stage 6: Marketing Kit
Auto-generate ad hooks, email sequences, landing page

## Quick Start Workflow
```
1. Load skill: skill_view(name="thai-ebook-pipeline")
2. Tell me niche/topic
3. Research → market-brief.md
4. Outline → approve
5. Write Pass 1 (structure + content)
6. Write Pass 2 (soul pass — voice + humor)
7. Edit chapter-by-chapter
8. Final humanizer pass
9. Export PDF
10. Generate marketing-kit.md
```

### Pass 3: Voice DNA Validation (REQUIRED — prevents silent voice drift)

After Pass 2, quantify each chapter against the RedMaster baseline. Do NOT skip this — user explicitly asked "have you harness any voice file?" because chapters drifted from the voice.

**Baseline (จาก redmaster.md 2,521 บรรทัด, 84,062 chars):**

| Marker | Baseline | Meaning |
|--------|----------|---------|
| `ครับ` | 5.8 ครั้ง/1,000 chars | THE signature. 24% ของทุกบรรทัด |
| `คือ` | 2.8/1,000 | Primary connector (not "ซึ่ง", "โดย") |
| `แม่ง` | 1.5/1,000 | Emphasis spice — must appear |
| `รู้มั้ย` | 0.1/1,000 | Rhetorical question marker |
| Sentence avg | 32 chars | Short. Punchy. |

**Score each chapter:**
```python
for f in sorted(drafts_dir.glob("*.md")):
    text = f.read_text()
    chars = len(text)
    for marker in ["ครับ", "คือ", "แม่ง"]:
        count = text.count(marker)
        per_k = (count / chars) * 1000
        base = baseline[marker]
        if per_k < base * 0.3:  # below 30% of baseline = FAIL
            print(f"❌ {f.name}: '{marker}' at {per_k:.1f}/1K (need {base:.1f})")
```

**If any chapter scores below 50% of baseline on `ครับ` or `แม่ง`:** inject missing markers before proceeding. Don't ship chapters with ❌ scores.

**Gotcha:** DeepSeek V4-PRO writes good Thai stories but consistently UNDER-uses `ครับ` (2-3x lower than baseline) and `แม่ง` (nearly absent in later chapters). This is NOT a model flaw — it's a post-processing requirement. Always validate every chapter.

### Voice Harness Reference Files

`references/voice-dna.md` — quantitative baseline (word frequency, rhythm targets, scoring method)
`references/voice-harness.md` — full calibration guide (patterns, rules, anti-patterns)
`scripts/voice-check.py` — run against any chapter: `python voice-check.py <chapter.md>` — scores 0-100%
`references/voice-profile.md` — narrative analysis of voice personality

---

## Model Selection for Thai Writing (learned from real usage)

| Model | Thai Quality | Use For |
|-------|-------------|---------|
| DeepSeek V3 / chat | ❌ Weak — formal, stiff, "เสหน่ห์" | Do NOT use |
| DeepSeek V4-PRO (no DNA rules) | ⚠️ Acceptable stories, ครับ=2.8, แม่ง=0.0 | First draft only |
| DeepSeek V4-PRO (with DNA enforcement) | ✅ ครับ=4.2, คือ=3.8, แม่ง=0.7 | **Production — proven** |
| Gemini 2.5 Pro | ⏭️ Skip — not needed. V4-PRO + DNA is sufficient. | N/A |

**Key insight:** The model matters less than DNA enforcement. V4-PRO without rules = unusable. V4-PRO with rules = excellent. Gemini may or may not be better — only testing will tell.

**Gemini 2.5 Pro Status (2026-05-27):** `GOOGLE_API_KEY` validated — 31 models available including `gemini-2.5-pro`. Thai writing quality NOT YET TESTED. To test: `/model gemini-2.5-pro` then write a calibration chapter with full DNA rules enforced, score, and compare against V4-PRO baseline.

See `references/model-comparison-methodology.md` for the full A/B testing protocol.

### CRITICAL: Voice DNA Injection During Writing (NOT just post-processing)

**Discovery (2026-05-27):** Writing WITH voice DNA rules actively enforced during generation produces FAR better results than writing without rules and post-processing later. Same model (DeepSeek V4-PRO), same topic:

| Approach | ครับ/1K | คือ/1K | แม่ง/1K | Quality |
|----------|---------|---------|---------|---------|
| Write without DNA rules, fix later | 2.8 | 2.9 | **0.0** | ❌ Rejected |
| Write WITH DNA rules enforced | 4.2 | 3.8 | **0.7** | ✅ Passes |

**The lesson:** Post-processing cannot inject soul. You must write with the voice rules active in every paragraph. The model will naturally under-use `ครับ` and skip `แม่ง` entirely unless prompted to include them during generation. Steps 6-8 below (post-processing passes) are SAFETY NETS, not the primary method. The primary method is writing right the first time.

```
1. Load voice sample (ebook-pipeline/reference/voice-samples/redmaster.md)
2. Extract voice DNA baseline (metrics above)
3. Write Chapter 1 as calibration — WITH DNA rules active in every paragraph — score, fix until >70%
4. Write chapters 2-5 in batch — WITH DNA rules active — score each immediately
5. Write chapters 6-8 in batch — WITH DNA rules active — score each immediately
6. Safety pass: strip ALL em dashes (chapter.replace("—", " "))
7. Safety pass: add "ครับ" where still missing (target 4-6/1000 chars)
8. Safety pass: add "แม่ง" where still missing (target 0.5-2/1000 chars)
9. Final voice DNA audit — all chapters >70%
10. Export PDF + Marketing Kit
```

### Per-Chapter Structure (Book Format)

```
1. SCENE (1-2 paragraphs) — specific story, vivid details, atmosphere
   "มีภาพหนึ่งที่ผมจำไม่เคยลืมครับ..." or "ผมอยากเล่าเรื่องของรุ่นพี่คนหนึ่ง..."
   NOT a concept, NOT a lesson — a STORY with sensory detail

2. TRANSITION (1 paragraph) — bridge from story to lesson
   "ประโยคนี้มันติดอยู่ในหัวผมเป็นอาทิตย์เลยครับ"
   Make the reader see themselves in the story

3. LESSON (3-5 paragraphs) — the meat, numbers, examples
   Build up long → deliver short punch
   "คือคณิตศาสตร์ชั้นมัธยม — คือดอกเบี้ยทบต้น"

4. SOLUTION / PREVIEW (1-2 paragraphs) — direction + hope
   "แต่สิ่งที่ผมอยากให้คุณรู้คือ..."

5. CLIFFHANGER (1 paragraph) — hook for next chapter
   "ในบทหน้า — เราจะมาดูกับดักอีกแบบ..."
```

### Thai Anti-AI Writing Rules — Book Edition

❌ **HARD BAN:**
- "—" (em dash) — Jared uses 0 in 86K chars. DeepSeek injects ~80 per chapter. Strip ALWAYS.
- "อย่างไรก็ตาม", "ทั้งนี้", "กล่าวคือ", "เป็นต้น"
- "สิ่งสำคัญคือ", "สิ่งที่ควรทราบคือ"
- Passive voice: "ถูกนำมาใช้", "ถูกพัฒนา"
- One-sentence-per-line (that's social media, not a book)
- Opening with a concept instead of a story
- Hedging: "อาจจะ", "น่าจะ", "คงจะ"

✅ **ALWAYS DO:**
- "ครับ" density: 4-6 per 1000 chars
- "คือ" as confidence marker, not hedging
- Paragraphs (3-5 sentences), not one-liners
- Book has space to breathe — descriptions, scenes, pauses

## Gemini 2.5 Pro — Verdict: NOT NEEDED

**Status (2026-05-27):** API key validated ✅. **Not tested for Thai writing — and no longer necessary.**

DeepSeek V4-PRO with voice DNA enforcement produces excellent Thai writing (ครับ=4.2, แม่ง=0.7). The bottleneck was never the model — it was the PROCESS. If you want to test Gemini for curiosity, go ahead, but it's not required for production-quality output.

## Pitfalls

- **Post-processing cannot inject soul** — DNA rules must be enforced DURING writing, not applied after. Writing without rules then trying to fix with find-and-replace produces zero `แม่ง` and weak `ครับ` density (proven: 2.8 vs 4.2). Write right the first time; use post-processing only as a safety net.
- **One-pass gets rejected** — user has explicitly rejected raw model output. Two-pass mandatory. Three-pass (DNA validation) strongly recommended.
- **Model voice drift** — DeepSeek V4-PRO writes good stories but consistently under-uses `ครับ` (2-3x below baseline) and `แม่ง` (nearly absent in later chapters). This is a KNOWN post-processing requirement, not a surprise. Always run DNA validation after writing.
- **"Harness" means quantify** — user asked "have you harnessed the voice file?" = you must run the scoring script, not just claim you followed the rules. If you can't produce the numbers, you didn't harness.
- **Pantip quotes → "ดู cheap"** — use real stories, not forum quotes
- **มึง/กู → rejected** — user wants professional but conversational
- **Voice drift across chapters** — check tone against voice profile every 3 chapters
- **คำสบถเป็นเครื่องเทศ ไม่ใช่อาหารหลัก** — use sparingly
- **PDF fonts** — must embed Thai font (Sarabun), otherwise ขึ้นเป็นสี่เหลี่ยม
- **Chapter files** — keep separate, never merge into one monster file
- **Apify Reddit scraper** needs `"searches"` (array), NOT `"searchTerms"`
- **Apify Trends** needs `timeRange: "today 1-m"` or `"today 3-m"`, NOT `"today 12-m"`
- **Apify YouTube** needs `"videoUrls"` (array), NOT `"searchKeywords"`
- **V4-PRO vs V3** — V3 Thai writing is rejected as "เสหน่ห์" (lacks soul). Always use V4-PRO for Pass 2.
- **Gemini API key validation** — GCP keys need billing + Generative Language API enabled. AI Studio keys work immediately. Validate with: `GET https://generativelanguage.googleapis.com/v1beta/models?key=*** (200 = valid, 400/403 = invalid). Previously all user keys were GCP-sourced and invalid; now has a working key (validated 2026-05-27).

## Files in this skill

| File | Purpose |
|------|---------|
| SKILL.md | Main playbook — full pipeline |
| references/voice-profile.md | Voice analysis + writing rules from actual usage |
| references/voice-harness.md | **Quantitative voice DNA + chapter scoring script** |
| references/apify-workflow.md | Apify actor IDs, input formats, pitfalls |
| references/gemini-api-validation.md | Validate GOOGLE_API_KEY via REST + key-type guide |
| references/model-comparison-methodology.md | **A/B testing protocol for comparing LLM Thai writing quality** |
| references/voice-profile.md | Voice analysis + rules from actual usage |
| references/apify-workflow.md | Apify actor IDs, input formats, pitfalls |
| references/gemini-api-validation.md | Validate GOOGLE_API_KEY via REST + key-type guide |
| templates/chapter-template.md | Template: Two-Pass Method |
| scripts/export-pdf.py | Python export script |
