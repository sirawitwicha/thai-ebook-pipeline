---
name: ben-settle-headline-01
description: Generate high-converting headlines using Ben Settle's 11 headline types, powered by market research data from the ben-settle-research skill. Use when the user wants to write headlines for sales copy, generate headline options from research data, brainstorm headlines using "Criminally Profitable Research" data, or turn voice-of-customer data into attention-grabbing headlines. Triggers on: "write headlines", "generate headlines", "headline ideas", "Ben Settle headlines", "sales headlines", "copy headlines", "headline types", "Knock-Knocks exercise", "shotgun rack headline".
---

# Ben Settle Headline Generator

Turns raw market research data into headlines using Ben Settle's 11 proven headline types from *Copy Slacker*.

## THE RULE

**You do not write headlines. You HARVEST them from the research data.**

Ben Settle's highest-performing headline ("Has the Golf God Arrived or is This Just a Complete Scam?") was not written. A prospect in a Facebook group said those exact words. Settle put them in the headline. That's it. That's the whole job.

Before you generate ANY headline, you must be able to point to the exact phrase, data field, or research excerpt it came from. If you cannot trace a headline back to a specific piece of research data, delete it. You invented it.

**The bullet shortcut**: "Your headline is nothing more than a version of your best bullet." — Ben Settle. If `*_bullets.md` exists, its Headline Candidates section IS your primary source. These bullets have already been field-tested against the research data. Elevating one to a headline is the most reliable path.

## Prerequisites

- Completed research from `ben-settle-research` skill in `research-outputs/<niche-slug>/`
- Three files MUST exist: `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`
- **NEW — Bullet-first pipeline**: If `*_bullets.md` exists, read it FIRST. Its Headline Candidates are your primary raw material.

## Workflow

### Step 1: Locate and Load ALL Available Data

**Which project are we working on?** Determine this first:

1. **If the user mentioned a niche in their request** (e.g., "write headlines for the keto research") — scan `research-outputs/` for a folder matching that niche name. Use Glob: `research-outputs/*/` to list all available project folders.

2. **If the user didn't specify** — list all folders under `research-outputs/` and ASK: "Which research project should I generate headlines for?" Present the options.

3. **If no research folders exist** — tell the user to run `ben-settle-research` on their niche first. The headline skill requires completed research.

4. **If exactly one folder exists** — use it, but confirm with the user: "I found research for '[niche]' — use this?"

Once the folder is identified, read ALL three files completely. Do not skim. The headlines are hiding in plain sight inside these files.

- `YYYY-MM-DD_structured-profile.json` — composite customer: every pain, fear, desire, enemy, secret fantasy, emotional state, competitive gap
- `YYYY-MM-DD_slang-dictionary.md` — 100+ entries of the market's EXACT language, organized by category, with verbatim quotes
- `YYYY-MM-DD_copy-brief.md` — the synthesized output: primary hook, pain bullets, the enemy, desire anchors, objection inventory, competitive positioning, and the bar complaint monologue
- `YYYY-MM-DD_bullets.md` — **IF EXISTS, READ THIS FIRST.** The Headline Candidates section contains 3-5 bullets that are already proven compelling. "Your headline is nothing more than a version of your best bullet." Skip directly to harvesting these as headlines before doing any other extraction.

### Step 1b: Bullet Shortcut (if bullets exist)

If `*_bullets.md` is present:
1. Read the Headline Candidates section
2. These 3-5 bullets ARE headline-ready. Apply the 11 headline types to ELEVATE them, not replace them.
3. Each candidate bullet → format it as a headline using the appropriate type (e.g., a curiosity bullet becomes a Curiosity Headline, a pain bullet becomes an Emotion Headline)
4. Proceed to Step 3 for the full extraction table, but use the bullet candidates as your PRIMARY source

If `*_bullets.md` does NOT exist: proceed normally. The skill works standalone from research data.

### Step 2: MANDATORY — Read the Worked Example

Read `references/worked-example.md`. This shows 15 exact data→headline transformations from a real research run. Study the pattern before you generate anything. The pattern is always: **find a phrase in the research → match it to a headline type → format → verify it traces back**.

### Step 3: MANDATORY — Systematic Extraction Table

Before writing a single headline, fill out this table. Extract EVERYTHING listed. This is not optional. You are mining the research for headline raw material.

Create a working document (scratchpad, not saved) with these sections:

#### Section A: Exact Prospect Phrases (from slang dictionary Direct Quotes section + bar complaint monologue)
List EVERY direct quote, verbatim. These are headlines in raw form. Read the monologue aloud — every sentence that hits you in the gut goes here.

#### Section B: Emotional Paydirt (from pain_and_fear + emotional_drivers)
Extract:
- The single dominant resident emotion (one word: rage, exhaustion, defiance, betrayal, etc.)
- Top 3 `keeps_awake_at_night` entries (verbatim)
- Top 3 `anger_triggers` (verbatim — these ARE headlines)
- Top 3 `insecurities` (verbatim — their secret fears = your Market-Oriented headlines)
- `urgent_crisis` (verbatim)
- `feelings_during_search` (verbatim — this is what your headline must speak to)

#### Section C: The Enemy & The Villain (from desires_and_aspirations.enemies + copy brief the_enemy)
Extract:
- The #1 enemy name (one phrase: "the narcissistic boss," "the credit thief," etc.)
- The enemy's defining trait from copy brief
- The line "They thrive because YOU play fair and they don't" (this is headline gold)

#### Section D: Proof Arsenal (from copy_brief.proof_elements + competitive_intelligence)
List every proof element. Flag the 2-3 that NO competitor can claim. These are your Proof Headline anchors.

#### Section E: The Objection Goldmine (from copy_brief.objection_inventory)
List EVERY objection verbatim. Each one IS a potential Objection Headline. The market handed you their skepticism — use it.

#### Section F: The Slang Headline Vocabulary (from slang dictionary)
Scan ALL categories. Extract every term that could anchor a headline. Prioritize terms with quotation marks — these are verbatim prospect language. Minimum 20 terms extracted.

#### Section G: The Competitive Gap (from competitive_positioning_map)
For each competitor: their weakness + your gap. This feeds Proof, Contrast, and Combine & Conquer headlines.

#### Section H: The "Golf God" Hunt
Scan the bar complaint monologue, the slang dictionary Direct Quotes, the pain data, and every quotation-marked phrase. Look for a phrase where the prospect literally said something that COULD be a headline. Settle found his in a Facebook group — "If you asked me this at my front door, I'd think it's a complete scam or that the Golf God has arrived." Your market has said something similar. FIND IT.

### Step 4: Generate Headlines — One Type at a Time

Read `references/11-headline-types.md` for the methodology behind each type. Read `references/data-to-headline-map.md` to know which extraction feeds which type.

For each headline type, work through this sub-process:

1. **Identify which Section (A-H) feeds this type** — use data-to-headline-map.md
2. **Pull 3-5 raw phrases from that Section** — verbatim, do not edit yet
3. **Apply the headline type's construction formula** from 11-headline-types.md
4. **Format, but preserve the market's words** — change as little as possible
5. **Verify traceability** — can you point to the exact research excerpt this came from?

**Anti-generic enforcement**: After writing each headline, ask:
- Does this contain a SPECIFIC word or phrase from the research data?
- Could a competitor in a DIFFERENT niche write this same headline?
- If yes to #2 → DELETE IT. It's too generic. Go back to the extraction table and find a more specific phrase.

Generate 3-5 headlines per type. For Combine & Conquer, generate 5-10 by mixing types.

### Step 5: Generate Knock-Knocks

The Knock-Knocks exercise: *"What can you say in 6 or 7 words when the person opens the door and, instead of slamming it, they grab you by the arm, yank you inside, and demand you tell them more?"*

Produce 5-7 of these. They must be:
- 6-7 words maximum (or very close)
- Drawn from Section A (exact prospect phrases) or Section B (emotional paydirt)
- Instant recognition — the prospect thinks "that's ME" within 1 second

### Step 6: Select Top 5 Picks

Choose the 5 strongest headlines across all types. For each, write a one-sentence reason WHY it's strong, referencing the research data it came from and which Settle principle it embodies.

### Step 7: Format and Deliver

Save to `research-outputs/<niche-slug>/YYYY-MM-DD_headlines.md` using the template below. Then present the Top 5 Picks to the user first.

```markdown
# Ben Settle Headlines: [NICHE]
**Generated**: YYYY-MM-DD
**Research basis**: [path to research folder]
**Dominant resident emotion**: [from Section B]
**#1 Enemy**: [from Section C]

## Knock-Knocks (6-7 Word Shotgun Racks)
[5-7 options]

## 1. Proof Headlines
[3-5 options — each citing its proof element]

## 2. Market-Oriented Headlines
[3-5 options — each naming a specific market pain/identity]

## 3. Emotion Headlines
[3-5 options — each anchored to the dominant resident emotion]

## 4. Blatant Offer Headlines
[3-5 options]

## 5. Contrast Headlines
[3-5 options — each with a specific contradiction from the data]

## 6. Tabloid Headlines
[3-5 options — each with a specific sensational twist]

## 7. Curiosity Headlines
[3-5 options — each with an implied mechanism]

## 8. Straight Benefit Headlines
[3-5 options — each with a specific, measurable benefit]

## 9. Question Headlines
[3-5 options — each asking a question the market already asks themselves]

## 10. Objection Headlines
[3-5 options — each naming a specific objection from the inventory]

## 11. Combine & Conquer
[5-10 options — each mixing at least 2 types]

## Top Picks (The 5 Strongest)
[Curated with one-sentence reasoning for each]
```

### Step 8: Present to User

Present the Top 5 Picks first with their reasoning. Offer to show all 11 categories. Ask which resonate — use feedback to refine.

## Reference Files

- `references/worked-example.md` — **READ THIS FIRST.** 15 step-by-step data→headline transformations with exact source tracing.
- `references/11-headline-types.md` — Complete methodology: why each type works, construction formulas, classic examples.
- `references/data-to-headline-map.md` — Which research data fields feed which headline types, with extraction methods.
