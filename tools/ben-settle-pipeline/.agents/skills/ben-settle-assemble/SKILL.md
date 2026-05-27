---
name: ben-settle-assemble
description: The orchestration meta-skill that runs the full 5-step Copy Slacker pipeline, assembles all outputs into one unified sales letter, and executes 10 editing passes following Ben Settle's "Put It All Together" methodology from Chapter 8. Use when the user wants to generate a complete sales letter end-to-end, chain all pipeline skills, or assemble existing outputs into a final draft. Triggers on: "assemble the letter", "put it all together", "write the full ad", "generate the full sales letter", "chain the pipeline", "run the full formula", "assemble everything", "final draft", "complete sales letter".
---

# Ben Settle Assemble — The Orchestration Meta-Skill

Takes all 5 Copy Slacker skills and orchestrates them into one unified sales letter, following the "Lash It All Together" methodology from *Copy Slacker* Chapter 8.

**What this skill does**: Chains the pipeline skills in order → assembles outputs into one document → runs 10 editing passes (the AI equivalent of "read it out loud 10 times") → delivers a final, market-checked sales letter.

## THE RULES

1. **Every word must earn its place.** During editing, ask: "Will the market care about this? Is this sentence absolutely clear? Could it be said with fewer words? Is it dramatic enough? Does this word really need to be there?"

2. **Only the market's opinion matters.** "You have no client but the market." — Gene Schwartz. Check every claim against the research data. Would they say it this way? Is this in their language?

3. **Sales copy can never be too long. Only too boring.** Don't cut for length. Cut for boredom. If a section is interesting, it stays. If it drags, cut or rewrite.

4. **The assembly order is NOT the reading order.** Bullets are the foundation (Phase 2). Headline + Opener + Story feed from bullets (Phase 3). Close feeds from everything (Phase 4). The reader sees: Headline → Opener → Story → Bullets → Close. But the WRITING follows the non-linear pipeline.

5. **"Be very specific about the problem but very vague about the solution."** Every section should make the reader feel the problem deeply. The 90/10 rule: give the WHAT, withhold the HOW. For the HOW, they have to buy.

## Prerequisites

- All 5 skills must exist in `.agents/skills/`
- Research must be complete (`structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`)
- The 5 sub-skills should each have generated their outputs (or this skill can trigger them)

## Workflow

### Phase 1: Check Pipeline Readiness

Glob `research-outputs/<niche-slug>/` and inventory what exists:

| File Pattern | Status | If Missing |
|---|---|---|
| `*_structured-profile.json` | Required | Run `ben-settle-research` |
| `*_slang-dictionary.md` | Required | Run `ben-settle-research` |
| `*_copy-brief.md` | Required | Run `ben-settle-research` |
| `*_bullets.md` | Foundation | Run `ben-settle-bullet-04` |
| `*_headlines.md` | Step 1 | Run `ben-settle-headline-01` |
| `*_opening-paragraphs.md` | Step 2 | Run `ben-settle-opening-paragraph-02` |
| `*_story.md` | Step 3 | Run `ben-settle-story-03` |
| `*_close.md` | Step 5 | Run `ben-settle-close-05` |

Present the user a checklist of what exists and what needs to be generated. Offer: "Generate all missing, or let me pick which to run?"

### Phase 2: Run Missing Skills (Non-Linear Order)

If the user says generate all, run in THIS order:

```
1. ben-settle-research        → structured-profile.json, slang-dictionary.md, copy-brief.md
2. [Optional] story-mining     → *_story-mining.md
3. ben-settle-bullet-04        → *_bullets.md           (FOUNDATION)
4. ben-settle-headline-01      → *_headlines.md         (from bullets)
5. ben-settle-opening-paragraph-02 → *_opening-paragraphs.md  (from bullets)
6. ben-settle-story-03         → *_story.md             (from headline+opener+bullets)
7. [Optional] close-mining     → *_close-mining.md
8. ben-settle-close-05         → *_close.md             (from everything)
```

**Critical**: Bullets MUST be generated before headline, opener, and story (non-linear pipeline). Each skill that follows reads `*_bullets.md` and feeds from it.

For each skill run, present the Top Picks to the user. Let them confirm or adjust before proceeding.

### Phase 3: Assemble the Chaotic Plug

Read ALL output files. Create a working document organized by section:

```
## HEADLINE
[Selected headline verbatim]

## OPENING PARAGRAPH  
[Selected opener verbatim]

## STORY
[Full story — all 7 sections]

## BULLETS
[All bullets, organized by type]

## CLOSE
[Full close — connector + offer + bonuses + guarantee + takeaway + PS]
```

This is the "chaos file" — raw, unedited, all parts present. Save as `YYYY-MM-DD_first-draft.md`.

### Phase 4: The 10 Editing Passes

Adapted from Ben's "read it out loud 10 times." Each pass has a specific lens. Do NOT try to fix everything in one pass — that's why the 10-pass system exists.

**Do 3-4 passes per session. Budget 2-3 sessions total. Between sessions, let the draft "sit" (metaphorically).**

#### Pass 1: The Market Language Check
**Read the full letter. For every sentence, ask:**
- Is this in THEIR language? (Check against slang dictionary)
- Does this sound like how they actually talk?
- Is any sentence "corporate speak" or "academic speak"?
- Replace any phrase a real person in this market wouldn't say.

#### Pass 2: The Continuity Check
**Read the full letter. Check:**
- Does the headline's voice carry through to the opener?
- Does the opener's protagonist carry through to the story?
- Does the story's emotional arc carry through to the bullets?
- Do the bullets' desire build into the close?
- Is the narrative voice (1st/3rd person) consistent throughout?
- Is the same enemy present throughout?

#### Pass 3: The Tension Check
**Read the full letter. At each section boundary, ask:**
- Does this section end with a hook that makes me want the next?
- Is there a clear Heaven & Hell arc running through the entire letter?
- Does any section release tension too early?
- Does the story properly set up the bullets?
- Does the close maintain tension from the last bullet?

#### Pass 4: The Specificity Check
**Read the full letter. For every claim:**
- Is there a specific detail backing it? (number, name, date, quote)
- Replace any generic claim with a specific one from the research data.
- "Many people" → "567 employees across 3 industries"
- "A long time ago" → "In 1532"
- "It works well" → "One reader used it to reverse a credit theft within 48 hours"

#### Pass 5: The "Would They Care?" Check
**Read the full letter. For every sentence:**
- Would the market care about this?
- Is this about THEM or about ME?
- Cut any sentence that's writer-centric, ego-driven, or irrelevant to the market.
- "Kill your darlings" — Stephen King. If you love a sentence but it doesn't serve the market, cut it.

#### Pass 6: The Clarity & Pithiness Check
**Read the full letter. For every sentence:**
- Is this absolutely clear? Could anyone misunderstand it?
- Can this sentence be shorter?
- Can 3 words do the job of 5?
- Hemingway test: would a 10th grader understand this?
- Cut filler words. Cut redundant sentences. Cut throat-clearing.

#### Pass 7: The Drama Check
**Read the full letter. For every section:**
- Is this dramatic enough? Does it hit the gut?
- Are any bullets flat or generic?
- Does the story have emotional weight?
- Would the market feel something reading this? (Anger, hope, recognition, urgency)
- If a section reads cold, infuse more of the market's exact pain language.

#### Pass 8: The Objection Sweep
**Read the full letter as a SKEPTIC. For every claim:**
- Would the market believe this?
- Where would they object?
- Does the guarantee address their real fears?
- Does the takeaway sound genuine or manufactured?
- Strengthen any weak spots with proof or more specific detail.

#### Pass 9: The Rhythm & Flow Check
**Read the full letter. Listen for:**
- Sentence length variety (mix short punchy with medium flowing)
- Paragraph breaks — are any too long?
- Sub-headline placement — do they shatter monotony every 15-20 bullets?
- Transition smoothness between sections
- Does the letter build momentum or stall?

#### Pass 10: The Final Polish
**Read the full letter once more. Fix:**
- Spelling, grammar, typos
- Consistent formatting
- Verify every claim traces back to research data
- Verify no section was accidentally cut during editing
- One final check: "Would I buy this?"

### Phase 5: Deliver the Final Letter

Save as `YYYY-MM-DD_final-letter.md`:

```markdown
# [PRODUCT NAME] — Complete Sales Letter
**Niche**: [niche]
**Date**: YYYY-MM-DD
**Pipeline**: Research → Bullets → Headline → Opener → Story → Close
**Editing passes**: 10

---

[FULL SALES LETTER TEXT]

---

## Source Trace
**Headline**: from *_headlines.md, Top Pick #X
**Opener**: from *_opening-paragraphs.md, Top Pick #X  
**Story**: from *_story.md, Type X
**Bullets**: from *_bullets.md, [N] bullets across 12 types
**Close**: from *_close.md, Configuration X

## Research Basis
[path to research folder + key data files used]
```

Present the final letter to the user with word count, section breakdown, and the option to run additional passes on any section they flag.

---

## The Parris Lampropoulos Structure Check

Before delivering, verify the letter follows this sequence for maximum believability:

1. **The Story** — someone's problem and what happened (emotional engagement)
2. **The Mechanism** — why/how it works (intellectual engagement)
3. **The Hard Data** — studies, statistics, proof (credibility lock-in)

If the letter is ordered differently, that's fine — but this structure is the most profitable Ben has ever used. If the letter isn't working, try re-ordering to this.

---

## Anti-Overwhelm Rules

Adapted from Gene Schwartz's kitchen timer method and Ray Edwards' "smallest possible goal":

1. **One skill at a time.** Don't think about the close while writing headlines.
2. **One editing pass at a time.** Don't fix drama while checking continuity.
3. **3-4 passes per session.** More than that and the brain compresses — quality drops.
4. **Let it sit between sessions.** The 1-2 day gap that Ben recommends translates to: between editing sessions, move to a different task. Come back fresh.
5. **Make goals too small to fail.** If stuck on a section, just write ONE sentence. Then another.
