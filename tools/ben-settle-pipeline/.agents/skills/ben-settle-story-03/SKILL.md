---
name: ben-settle-story-03
description: Generate sales letter stories using Ben Settle's 5 storytelling methods, powered by market research data from the ben-settle-research skill. Writes stories section-by-section using a 7-part scaffold to prevent memory loss and ensure proper length. Use when the user wants to write a sales story, tell a story in copy, write the story section of a sales letter, or create the third step in the 5-step Copy Slacker formula. Triggers on: "write a story", "sales story", "copy story", "tell a story for my ad", "story section", "Ben Settle story", "copy slacker step 3", "origin story for my product", "need a story for my sales letter".
---

# Ben Settle Story Generator

Turns raw market research data into sales letter stories using Ben Settle's 5 storytelling methods from *Copy Slacker*.

**Role in the 5-step formula**: Headline → Opening Paragraph → **STORY** → Bullets → Close. Stories are the #1 skill in persuasive communication. Humans are hardwired for them. They sell even when you're not selling anything. Top Gun never once said "join the Navy" — but recruitment soared so high the military put recruiters IN the theaters.

## THE RULES

1. **Section by section, never all at once.** Stories are 400-575 words. Writing them in one pass causes memory loss, truncation, or rushed endings. Use the 7-part scaffold. Write ONE section at a time. Append to file. Only need the previous section's last paragraph + the next section's data inputs to continue.

2. **Tension is king.** Every section should make the reader think "what happens next?" Heaven and Hell: show them in hell (the problem), then ascend to heaven (the solution).

3. **"Short enough to get attention, long enough to cover the details."** Like a woman's skirt. Get to the point fast. Thin the plot, don't thicken it. But give enough specific, vivid detail to make it real.

4. **Stay in the market's world.** The story must be about what the market cares about. "If Jesus had started with 'here's how to be a good neighbor' it would have bored everyone. Instead, he told a parable about a man robbed on the road to Jericho." — Joe Vitale.

## The Narrative Chain

The story is step 3 of 5. It does NOT start fresh. It continues from steps 1 and 2.

```
Headline → Opening Paragraph → STORY → Bullets → Close
   ↑              ↑              ↑
  hooks       bags the       pays off the
  attention   attention      setup with a
                             full narrative
```

Every element set up in the headline and opening paragraph must carry through into the story — same protagonist, same enemy, same emotional arc, same voice. If the opening paragraph introduced Sarah, the story is ABOUT Sarah. If the headline named credit theft as the shotgun rack, the story shows credit theft happening to Sarah.

## Prerequisites

**Required**:
- `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`
- `YYYY-MM-DD_headlines.md` + `YYYY-MM-DD_opening-paragraphs.md` — story must continue from these

**NEW — Bullet-enriched stories**: If `*_bullets.md` exists, read it as **Layer 4**. Bullet types map directly to story sections:
- **Expansion bullets (#12)** → Story sections 4-5 (Discovery + Transformation). These are pre-written narrative paragraphs.
- **Pain bullets (#5)** → Story sections 2-3 (Escalates + Rock Bottom). Vivid suffering language ready to insert.
- **Proof bullets (#3)** → Story section 6 (Evidence). Credibility anchors already formatted.
- **Headline Candidates** → Confirm the story's emotional hook matches the best bullet.

If headline or opening paragraph files don't exist, ask the user whether to generate them first or proceed with research-only data.

## Workflow

### Step 1: Locate and Read ALL Files

Glob `research-outputs/<niche-slug>/` to find the project folder. Read ALL FIVE files completely:

1. `structured-profile.json`
2. `slang-dictionary.md`
3. `copy-brief.md`
4. The headline file (`*_headlines.md`) — note which headline(s) are Top Picks or user-selected
5. The opening paragraph file (`*_opening-paragraphs.md`) — note which opener(s) are Top Picks or user-selected

### Step 2: MANDATORY — Read the References

Read `references/5-story-types.md`, `references/data-to-story-map.md`, and `references/story-scaffolding.md`.

### Step 3: Auto-Select Headline and Opening Paragraph

Read the Top Picks sections from both files. Auto-select the #1 Top Pick from each. If the user specified a preference earlier in the conversation, use that instead.

**Alignment check**: The headline and opener must share the same emotional register, same enemy (implicitly or explicitly), and same target reader. If the #1 Top Pick headline is anger-driven ("credit theft") but the #1 Top Pick opener is a calm question ("Do you know?"), they're misaligned. In that case, pick the headline+opener pair that share the strongest alignment — matching emotion, matching enemy, matching voice.

Present to the user: "I'll use [Headline] and [Opener]. They're aligned on [shared emotion/enemy]. OK?" If they object, use their preference. If they don't respond, proceed with your selection.

### Step 4: Extract Continuity Data

From the SELECTED headline and opener, extract:

| Continuity Element | Where to find it |
|---|---|
| The emotional hook | The headline's core emotion (fury, defiance, exhaustion, etc.) |
| The enemy (if named) | Headline text + opener text — search for enemy labels |
| The protagonist (if introduced) | Opener — who was described? Name? Situation? Belief? |
| The narrative voice | Opener's POV (1st/3rd person) and tone calibration from copy brief |
| Where the opener LEFT OFF | Last paragraph of the selected opener — Section 1 of story starts HERE |

**If the opener didn't introduce a specific protagonist**: Create one from the `primary_buyer_description`. Use a first name or a blank (____). Give them a specific situation matching the headline's emotion.

### Step 5: Check Story Data — To Scrape or Not to Scrape?

The 5 core research files provide pain, slang, proof, and voice. But story-specific data (personal accounts, historical details, news events, insider confessions) may need additional scraping.

**Check what exists**:
- Does the folder contain a `*_story-mining.md` file? If yes, read it — you have enriched story data.
- Do the YouTube comments or Reddit data from the research phase contain full personal transformation stories (not just complaints, but complete arcs: struggle → rock bottom → discovery → result)? If yes, you may have enough for Type 2/3.
- Does the proof elements list contain specific historical references with dates, names, and documented events? If yes, you may have enough for Type 4.

**Ask the user**: "I can write the story with the existing research data alone — it'll be solid. But if you want richer details (historical depth, specific personal accounts, bizarre counterintuitive facts, news events I can reference), I can scrape additional story-mining data. This adds ~$0.50-1.00 and 2-3 minutes. Scrape more, or proceed with what we have?"

If the user says scrape: read `references/story-mining-queries.md`, run the queries most relevant to the chosen story type, save results to `research-outputs/<niche>/YYYY-MM-DD_story-mining.md`.

If the user says proceed: move to Step 6 with existing data.

If the user doesn't specify: proceed with existing data. Most stories can be written well from the 5 core research files alone.

### Step 6: Choose the Story Type

Recommend the best type based on what data is available:

| If you have... | Best type |
|---|---|
| A personal transformation story from YouTube/Reddit | Type 2: Story About Someone Else |
| Only composite pain data, no specific person's story | Type 3: Dramatized (Parable) |
| Specific historical references with dates/names/events | Type 4: Historical Story |
| A named authority figure with documented credentials | Type 5: Meet The Guru |
| The product creators' own journey (and you're writing in 1st person) | Type 1: Story About You |

Present to user: "I recommend Type [X] because [reason]. OK?" If they prefer another type, use that.

### Step 7: MANDATORY — Fill the Story Brief

Pull from THREE data layers. Each layer feeds different sections of the story.

| Story Element | Layer 1: Continuity | Layer 2: Core Research | Layer 3: Story-Mining | Layer 4: Bullets (if exist) |
|---|---|---|---|---|---|
| Protagonist | From selected opener | `primary_buyer_description` | Personal story accounts | — |
| Emotional hook | Headline's dominant emotion | `feelings_during_search` | — | Headline Candidates from bullets — confirm alignment |
| The Enemy | Name from headline + opener | `enemies` + `the_enemy` | Category 9 (Enemy Exposed) | Pain bullets about the enemy — pre-written vivid language |
| The Hell (pain) | — | `keeps_awake_at_night`, `anger_triggers` | Category 3 (Personal Stories) | **Type 5 Pain bullets** — ready-to-insert suffering details |
| Failed solutions | — | `objection_inventory` | Category 4 (Failed Solutions) | **Type 7 What NOT To Do bullets** — mistakes they're making |
| Rock Bottom | — | `bar_complaint_monologue`, `urgent_crisis` | Category 3 | **Type 5 Pain bullets** — the worst moments, pre-phrased |
| The Discovery | — | `secret_fantasies`, `number_one_urgent_problem` | Category 1, 2, 8 | **Type 12 Expansion bullets** — full narrative paragraphs about discoveries |
| The Transformation | — | `what_they_want_most`, `desired_feeling_on_arrival` | Category 10 | **Type 6 Straight Benefit bullets** — outcomes, pre-phrased |
| The Proof | — | `proof_elements` | Category 2, 5, 6 | **Type 3 Proof bullets** — credibility anchors already formatted |
| Slang & Voice | Tone from copy brief | `slang_dictionary` all Direct Quotes | — | **Type 1 Curiosity bullets** — the market's exact phrasing |

**When Layer 4 exists**: It is the PRIMARY source for story section detail. The bullets have already processed raw research into compelling, specific language. Do not re-generate from raw data what the bullets already provide. Insert the bullet language directly into story sections.

**How to use this**: When story-mining data EXISTS, it becomes the PRIMARY source for vivid details (Sections 2-6). The core research provides the structural understanding (who the market is, what they feel). The story-mining provides the specific, named, documented, bizarre, and visceral details that make the story feel REAL.

When story-mining data DOES NOT exist, use only Layers 1-2. The story will still be solid — just less rich in documented specifics.

### Step 8: Write the Story — Anti-Compression Order

**DO NOT write sections 1→2→3→4→5→6→7.** Later sections compress as context fills. Follow the anti-compression order from `references/story-scaffolding.md`:

```
PHASE A (Fresh context — ending first):
  → Write Section 6 (Evidence) — 50-75 words. From story brief Layer 3.
  → Write Section 7 (Bridge) — 25-50 words. From story brief.
  → HOLD. Do NOT append to file yet.

PHASE B (Build narrative):
  → Section 1 (Setup) → append.
  → Read last ¶. Section 2 (Escalates) → append.
  → Read last ¶. Section 3 (Rock Bottom) → append.
  → Read last ¶. Section 4 (Discovery) → append.
  → Read last ¶. Section 5 (Transformation) → append.

PHASE C (Flow check + final assembly):
  → Read Section 5's last sentence + pre-written Section 6.
  → Adjust Section 5's ending if the transition feels abrupt.
  → Append Sections 6 and 7.
```

**Layer priority** — Layer 3 (story-mining) is PRIMARY when available:

| Section | Primary Data Source |
|---|---|
| 6. Evidence | Layer 3: History (Cat 2), News (Cat 5), Numbers (Cat 6) |
| 7. Bridge | Layer 1: Primary hook |
| 1. Setup | Layer 1: Continuity hero + Layer 3: Real backstory (Cat 3) |
| 2. Escalates | Layer 2: Pain + Layer 3: Suffering language (Cat 3), Enemy tactics (Cat 9) |
| 3. Rock Bottom | Layer 2: Bar complaint + Layer 3: Worst moment (Cat 3), Failed solutions (Cat 4) |
| 4. Discovery | Layer 2: Urgent problem + Layer 3: Bizarre facts (Cat 1), History (Cat 2), Insider (Cat 8) |
| 5. Transformation | Layer 2: Desired outcome + Layer 3: Real results (Cat 10), Pop culture (Cat 7) |

### Step 9: Review for Tension

After all 7 sections are written, read the full story once. Check:
- Does each section end with a hook that makes you want the next?
- Is there a clear Heaven & Hell arc?
- Are the details SPECIFIC and VIVID (not generic)?
- Does it use the market's exact language from the slang dictionary?

If any section falls flat, rewrite just that section — not the whole story.

### Step 10: Present

Save to `research-outputs/<niche-slug>/YYYY-MM-DD_story.md` using this exact header format:

```markdown
# Ben Settle Story: [NICHE]
**Generated**: YYYY-MM-DD
**Story type**: [Type # — Name]
**Data layers**: Continuity (headline + opener) + Core Research (JSON + slang + copy-brief) [+ Story-Mining (SERP + Reddit) if used]
**Word count**: [total]

## Narrative Chain
**Headline**: [The selected headline — verbatim]
**Opening Paragraph**: [The selected opener's title/label + first 1-2 sentences]

---

[Story sections follow]
```

**Why this matters**: Anyone reading the story file can immediately see the full narrative chain. The headline tells them what hook was used. The opener tells them how the story was set up. The story shows the payoff. All three are linked and traceable.

Present the story to the user with the headline and opener shown first, then the full story text.

## Reference Files

- `references/story-scaffolding.md` — **READ THIS FIRST.** The 7-part section-by-section method with word counts, inputs, and examples.
- `references/5-story-types.md` — Complete methodology for each of the 5 types with classic examples.
- `references/data-to-story-map.md` — Which research data fields feed which story elements.
- `references/story-mining-queries.md` — 10-category query strategy for scraping story-specific enriched data.
- `references/worked-example.md` — Full story written section-by-section from research data.
