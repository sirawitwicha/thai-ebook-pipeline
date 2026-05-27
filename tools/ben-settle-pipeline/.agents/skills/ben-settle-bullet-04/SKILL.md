---
name: ben-settle-bullet-04
description: Generate 100 irresistible sales bullets using Ben Settle's 12 bullet types, powered by market research data. Bullets are the FOUNDATION of all copy — the headline is just your best bullet elevated. Use when the user wants to write bullets, generate a bullet list for sales copy, create the fourth step in the Copy Slacker formula, or build the raw material that headlines, stories, and openers all draw from. Triggers on: "write bullets", "bullet points", "sales bullets", "bullet list", "Ben Settle bullets", "copy slacker step 4", "bullet copy", "fascinations", "100 bullets".
---

# Ben Settle Bullet Generator

Produces 100+ bullets from market research data using Ben Settle's 12 bullet types. Bullets are not step 4 of 5 that "comes after the story." Bullets are the FOUNDATION. Gary Halbert wrote ads that were almost ALL bullets. The headline is nothing more than your best bullet elevated to the top. The story exists to get the reader to the bullets.

## THE RULE

**Every bullet must trace back to a specific piece of research data.** A curiosity bullet anchors to a slang term. A pain bullet anchors to a keeps_awake_at_night entry. A proof bullet anchors to a proof element. If you cannot point to the exact research excerpt that spawned a bullet, delete it.

## Prerequisites

- Completed research from `ben-settle-research` skill in `research-outputs/<niche-slug>/`
- Required: `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`
- Optional but powerful: `*_story-mining.md` — adds bizarre facts, history, news, numbers for proof/curiosity bullets
- NOT required: headline, opener, or story files. Bullets are written FROM research, not from prior copy outputs. Those skills can later draw FROM bullets.

## Workflow

### Step 1: Locate the Research

Glob `research-outputs/*/`. Ask user which project. Read the 3 core files. If `*_story-mining.md` exists, read it too.

### Step 2: MANDATORY — Read References

Read `references/12-bullet-types.md` for the full methodology. Read `references/data-to-bullet-map.md` for which research data feeds which bullet types. Read `references/bullet-batching.md` for the 7-batch memory-safe system.

### Step 3: MANDATORY — Fill the Bullet Data Inventory

Before writing any bullet, extract these from the research into a working inventory:

| Inventory Section | Source | Extract | Target count |
|---|---|---|---|
| Pain points (verbatim) | `keeps_awake_at_night`, `anger_triggers`, `pain_emotional`, `daily_frustrations` | Every distinct pain phrase | 15+ |
| Slang terms | `slang_dictionary` all categories | Every term with its exact quote | 30+ |
| Proof anchors | `proof_elements`, story-mining Cat 2/5/6 | Every proof element, fact, number, historical reference | 15+ |
| Desire statements | `secret_fantasies`, `what_they_want_most`, `desire_anchors` | Every desire outcome | 10+ |
| Enemy details | `enemies`, `the_enemy`, `anger_targets` | Enemy behaviors, tactics, traits | 10+ |
| Objections | `objection_inventory[].objection` | Every objection verbatim | 7+ |
| Mistakes/Failures | `slang_dictionary` Errors, story-mining Cat 4 | What they do wrong, what they tried that failed | 10+ |
| Counterintuitive facts | Slang unusual entries, story-mining Cat 1/8 | Surprising, bizarre, insider knowledge | 10+ |

### Step 4: Write Bullets — 7 Batches

**DO NOT write all 100 bullets at once.** Use the 7-batch system from `references/bullet-batching.md`. Each batch reads only its slice of the inventory — not the full research. After each batch, append to file, then reset context.

| Batch | Data Source | Bullet Types | Target |
|---|---|---|---|
| 1 | Pain points + Enemy details | Pain (#5), What NOT To Do (#7), Curiosity (#1) | 15-18 |
| 2 | Slang terms + Counterintuitive facts | Curiosity (#1), Can't Be Done (#2), 90% Solution (#9) | 15-18 |
| 3 | Proof anchors + Historical/News | Proof (#3), Giveaway (#8), Contrast (#4) | 15-18 |
| 4 | Desire statements + Mistakes | Straight Benefit (#6), What NOT To Do (#7), 90% Solution (#9) | 15-18 |
| 5 | Objections + Enemy tactics | Contrast (#4), Pain (#5), Curiosity (#1) | 12-15 |
| 6 | Story-mining Cat 1-10 (if exists) | Can't Be Done (#2), Proof (#3), Giveaway (#8) | 12-15 |
| 7 | All remaining data | Compressed Finale (#11) + Expansion (#12) + Sub-Heads (#10) | 15-20 |

**Total target: 100-120 bullets**

### Step 5: Assembly — Apply Layout Tactics

After all 7 batches are written, read the full bullet list once and apply:

1. **Beef up bookends** — Move the 2 strongest bullets to first position. Move 2 more strongest to last position.
2. **Loop effect** — Insert an Expansion bullet (#12) every 12-15 bullets. Break up the rhythm.
3. **Dramatic sub-heads** — Take the last 6-8 words of 3-4 strong bullets and break them into sub-headlines. Insert throughout.
4. **Vary up ammo** — Ensure no two adjacent bullets are the same type. If types #1 and #1 are back-to-back, swap one with a different type from elsewhere.
5. **Eye relief** — Alternate bolding: bold, not bold, bold, not bold.
6. **Number them** — 1 to 100. Numbered lists create completion drive.

### Step 6: Flag Headline Candidates

Read the assembled bullet list. Identify the 3-5 strongest bullets — the ones that create the most intense curiosity, pain, or desire. These ARE headline candidates. Mark them clearly at the top of the output.

### Step 7: Present

Save to `research-outputs/<niche-slug>/YYYY-MM-DD_bullets.md`. Format:

```markdown
# Ben Settle Bullets: [NICHE]
**Generated**: YYYY-MM-DD
**Total bullets**: [count]
**Headline candidates**: [3-5 bullet numbers flagged]

## Headline Candidates
[3-5 best bullets — any of these could become the headline]

## Full Bullet List
[100+ numbered bullets with alternating bold, expansion breaks, sub-heads]
```

## Reference Files

- `references/bullet-batching.md` — **READ THIS FIRST.** The 7-batch system with reset protocol. Each batch is self-contained.
- `references/12-bullet-types.md` — Complete methodology for each type with classic examples.
- `references/data-to-bullet-map.md` — Which inventory sections feed which bullet types.
- `references/worked-example.md` — 12 data→bullet transformations.
