---
name: ben-settle-book-miner
description: Mines any book that has been converted to page-by-page .md files for copywriting ammunition. Answers all 45 Ben Settle research questions FROM the book's pages — treating the author's expertise as the data source. Produces the same structured-profile.json, slang-dictionary.md, and copy-brief.md as the internet-research pipeline, but with deeper, proprietary ammunition no competitor can access. Use when the user has a book in .md-per-page format and wants to extract copywriting ammunition from it. Triggers on: "mine this book", "extract ammunition from book", "book miner", "turn this book into copy data", "analyze book for copywriting", "book research", "extract from pages".
---

# Ben Settle Book Miner

Converts a book (in page-by-page .md format) into the three standard research output files that feed the entire copywriting pipeline.

**What this replaces**: Phases 1-3 of `ben-settle-research` (the Apify internet scraping). Instead of scraping Reddit, YouTube, and SERP for raw customer conversations, you mine the author's systematized expertise from the book's pages.

**Why this matters**: A book is compressed expertise. The author spent years learning this. Every chapter has frameworks, metaphors, techniques, and insights you won't find on Reddit. The bullets, headlines, and stories that come out of this will carry unique ammunition no competitor's copy can match.

**Output is identical to ben-settle-research**: `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`. The downstream pipeline (bullet-04, headline-01, opening-02, story-03, close-05) runs unchanged — it doesn't know or care whether the data came from internet scraping or book mining.

## THE RULES

1. **The book IS the data.** Every answer to the 45 questions must be traceable to a specific page, passage, or framework from the book. Do not invent. Do not assume. If the book doesn't answer a question, mark it "Insufficient data in book."

2. **The author's voice IS the market's voice.** When extracting slang, metaphors, and vernacular, pull the author's EXACT language. The author's way of explaining things becomes YOUR way of writing copy. This is proprietary ammunition — no other copywriter has access to the same book's language.

3. **Named techniques and frameworks are the highest-value ammunition.** A technique the author named (e.g., "The Mirror Principle," "The 24-Hour Rule") is more valuable than a general observation. Named techniques produce Curiosity bullets, Giveaway bullets, and 90% Solution bullets with specificity that generic research can never match.

4. **The book's structure IS the bullet organization.** The chapters and their natural progression (problem → diagnosis → solution → mastery) map directly to how you'll organize the bullet list.

## Prerequisites

- A folder of .md files, one per page, named `page_001.md`, `page_002.md`, etc.
- The folder must be under `docs/<book-name>/` or the user specifies the path.
- The book can be any language, any niche, any length.

## Workflow

### Step 1: Locate and Verify the Book

1. **User mentioned a book** → Glob `docs/*/page_001.md` to find matching folders.
2. **User didn't specify** → List all folders containing `page_*.md` files and ASK.
3. **No book folders exist** → Tell user: "Convert your book to .md files (one per page) and place them in `docs/<book-name>/`."
4. **Exactly one folder exists** → Use it, but confirm with user.

Verify: count the pages, read the first 5 pages and the table of contents (usually pages 1-5), identify the book's title, author, niche, and structure.

### Step 2: MANDATORY — Read the References

Read `references/book-mining-prompts.md`. These are the 6 adapted synthesis chunks — same 45 questions as the research skill, but the "data" fed to each chunk is BOOK PAGES instead of internet scrapes.

### Step 3: MANDATORY — The Structural Scan

Before mining, read the table of contents and the first 15 pages. Produce a one-page structural scan:

```markdown
## Book Structural Scan
**Title**: [book title]
**Author**: [if available]
**Niche**: [what market this book serves]
**Total pages**: [N]

### Chapter Map
| Ch | Title | Pages | What It Teaches | Key Techniques Named |
|---|---|---|---|---|

### Dominant Voice
- Tone: [aggressive/wake-up-call / clinical/academic / street-smart / nurturing / other]
- Reading level: [estimate]
- Narrative style: [1st person / 3rd person / instructional / story-driven]

### Thesis
[One paragraph: what this book promises and why it matters to the reader]
```

This structural scan is your map. It tells you which pages feed which chunks.

### Step 4: Mine the Book — 6 Chunks

Read `references/book-mining-prompts.md` for the full prompt for each chunk.

For each of the 6 chunks:

1. **Select the pages relevant to that chunk** using the structural scan
2. **Read those pages** — read them fully, do not skim
3. **Feed the pages as data** into the chunk's prompt
4. **Save the chunk output** as a working file (scratchpad, not saved to disk yet)
5. **Move to the next chunk**

The 6 chunks:

| Chunk | Questions | What to Feed | Where to Find in Book |
|---|---|---|---|
| **1. Pain & Fear** | Q1-8, 11, 15, 24 | Pages describing the reader's problem, suffering, fears | Early chapters (problem diagnosis), case studies, "before" descriptions |
| **2. Identity & Worldview** | Q9-10, 13-14, 17-26, 32, 41 | Pages describing who the reader is, how they think, what they believe | Introduction, "who this book is for" sections, cultural references throughout |
| **3. Desires & Aspirations** | Q12, 16, 31, 37-39 | Pages describing the promised transformation, the outcome, the "after" | Later chapters (solution), "what you'll achieve" sections, chapter conclusions |
| **4. Media & Culture** | Q34-36, 44 | Pages referencing books, movies, historical figures, communities | Throughout — note every reference as you mine |
| **5. Competitive Intelligence** | Q28, 33, 42-43, 45 | Pages discussing alternative approaches, what doesn't work, why THIS way | Early chapters (failed solutions), comparisons to competing frameworks |
| **6. Emotional & Decision Drivers** | Q29, 30, 40 | The book's emotional register throughout — how the author makes the reader FEEL | Introduction, conclusion, "imagine this" passages, most emotionally charged sections |

**Mining principle**: Chunks 1-3 feed from SPECIFIC sections (early, middle, late chapters). Chunks 4 and 6 mine the ENTIRE book — every page is a source for voice, tone, cultural references, and emotional register.

### Step 5: MANDATORY — Read the Worked Example

Read `references/worked-example.md`. This shows the first two chunks of the Modern Machiavelli (285 pages) being mined. Study the pattern: how pages are selected per chunk, how answers are extracted, how evidence is cited.

### Step 6: Synthesize — Final Assembly

After all 6 chunks are complete, run the Final Assembly prompt from `references/book-mining-prompts.md`. This takes all 6 chunk outputs and produces:

1. **`structured-profile.json`** — follows the standard schema from `ben-settle-research`
2. **`slang-dictionary.md`** — 100+ entries of the book's unique language, metaphors, techniques, and frameworks
3. **`copy-brief.md`** — the synthesized output: primary hook, pain bullets, the enemy, desire anchors, objection inventory, tone calibration, competitive positioning, and the "bar complaint" monologue (in the AUTHOR'S voice)

Save all three to `research-outputs/<book-slug>/YYYY-MM-DD_` prefix.

### Step 7: Present to User

Present:
1. The structural scan
2. Key findings: dominant pain, #1 enemy, top 5 named techniques, core desire
3. The Primary Hook from the copy brief
4. Path to the three output files

Then ask: "Ready to run the bullet pipeline on this data?"

---

## Data Trace Requirement

Every answer in every chunk must cite its source: "From page 47 — the author's description of..." or "From chapter 3 — the Mirror Technique as described on page 112." This traceability is what makes the ammunition defensible and verifiable.

---

## Reference Files

- `references/book-mining-prompts.md` — **READ THIS FIRST.** The 6 adapted synthesis chunks + final assembly prompt. Same 45 questions, adapted for book page data.
- `references/worked-example.md` — The Modern Machiavelli book being mined. Shows the structural scan + first two chunks with page citations.
- `references/output-schemas.md` — **Cross-reference from `ben-settle-research`**. The JSON schema and markdown template for output files. Identical format — no need to duplicate.
