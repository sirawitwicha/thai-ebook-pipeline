---
name: ben-settle-opening-paragraph-02
description: Generate high-converting sales letter opening paragraphs using Ben Settle's 9 persuasive openers, powered by market research data from the ben-settle-research skill. Use when the user wants to write opening paragraphs for sales copy, bridge from headline to story, bag the attention the headline flagged, or write the second step in the 5-step Copy Slacker formula. Triggers on: "opening paragraph", "sales letter opener", "copy lead", "open my ad", "start my sales letter", "how to open my copy", "what comes after the headline", "Ben Settle opener", "copy slacker step 2".
---

# Ben Settle Opening Paragraph Generator

Turns raw market research data into opening paragraphs using Ben Settle's 9 persuasive sales letter openers from *Copy Slacker*.

**Role in the 5-step formula**: Headline flags the attention → Opening paragraph BAGS the attention. John Carlton: the headline gets their attention, the opening paragraph gets them situated, settled in, and *ready and willing to read your ad.* If you get this right, they absorb everything you say next. If you get it wrong, they're gone — even if your headline was great.

## THE RULE

**You do not write opening paragraphs from thin air. You BUILD them from the research data.**

The opening paragraph must feel like a natural continuation of the headline — same voice, same enemy, same emotion. It must not sound "salesy." It should read like a fascinating conversation about a shared interest. Every opener pulls its raw material from specific research data fields. If you cannot trace an opener back to a specific piece of research data, delete it.

## Prerequisites

- Completed research from `ben-settle-research` skill in `research-outputs/<niche-slug>/`
- Three files MUST exist: `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`
- Ideally: a headline file from `ben-settle-headline-01` — the opening paragraph bridges FROM a specific headline
- **NEW — Bullet-enriched openers**: If `*_bullets.md` exists, read it as a source. Specific bullet types map to opener types:
  - **Giveaway bullets (#8)** → Brutal Honesty opener — "here's a real tip, no strings"
  - **What NOT To Do bullets (#7)** → "Do You Know?" opener — "do you know you should never..."
  - **Proof bullets (#3)** → If/Then + Proof opener — credibility already formatted
  - **Pain bullets (#5)** → Emotion opener — suffering language ready to use
  - **Curiosity bullets (#1)** → Ask a Question opener — the bullet IS the question

## Workflow

### Step 1: Locate and Load the Research Data

Determine which project:

1. **User mentioned a niche** → Glob `research-outputs/*/` and find the matching folder.
2. **User didn't specify** → List all folders under `research-outputs/` and ASK.
3. **No research folders exist** → Tell user to run `ben-settle-research` first.
4. **Exactly one folder exists** → Use it, but confirm with user.

Once identified, read ALL three research files completely.

### Step 2: MANDATORY — Read the Worked Example

Read `references/worked-example.md`. This shows 9 exact data→opening paragraph transformations from a real research run. Study the pattern before generating anything.

### Step 3: MANDATORY — Systematic Extraction Table

Before writing a single opener, fill out this table from the research data:

#### Section A: The Headline Hook (if available)
If the user has a headline file from `ben-settle-headline-01`, read it. Note which headline(s) the user selected or which are the Top Picks. The opening paragraph bridges FROM the headline.

#### Section B: The Emotional State (from emotional_drivers)
Extract:
- `feelings_during_search` verbatim — what they're feeling when they find you
- `desired_feeling_on_arrival` verbatim — the emotional transformation you're selling
- The arc: [current state] → [trigger] → [desired state]

#### Section C: The Enemy & The Story Villain (from desires_and_aspirations.enemies + copy brief the_enemy)
Extract:
- The #1 enemy name
- A specific, vivid detail about the enemy's behavior (from pain_point_bullets or slang)
- What the enemy DOES that the prospect recognizes

#### Section D: Proof Arsenal (from copy_brief.proof_elements)
List every proof element. Flag the 2-3 most dramatic, visual, or story-worthy. These become the "ancient gladiators and samurai" of your If/Then + Proof opener.

#### Section E: The Tabloid / Sensational Angle (from slang dictionary + pain data)
Extract:
- The most bizarre, surprising, or counterintuitive fact from the research
- Any story-worthy detail from the competitor analysis or slang dictionary
- The "bizarre story" hook — something that sounds like a tabloid cover

#### Section F: The Brutal Honesty Elements (from objection_inventory + pain_and_fear.insecurities)
List every flaw, drawback, insecurity, and objection. These are your "I am not a doctor" raw material. The market's own skepticism = your most credible opener.

#### Section G: The "Do You Know?" Curiosity Bombs (from slang dictionary + pain data + competitor intelligence)
Extract 5+ counterintuitive facts the market doesn't know. Each must be:
- TRUE (from the research)
- SURPRISING (contradicts common belief)
- RELEVANT (directly impacts the prospect)

#### Section H: Exact Prospect Language (from slang dictionary Direct Quotes + bar complaint monologue)
Extract verbatim phrases. These become your "let me tell you a story" narrative voice.

### Step 4: Generate Openers — One Type at a Time

Read `references/9-opening-types.md` for the full methodology behind each type. Read `references/data-to-opening-map.md` to know which extraction feeds which opener type.

For each of the 9 types, produce **2-3 opening paragraph options** (3-5 sentences each). Each must:

1. **Bridge from a headline** — reference the headline's emotion or promise implicitly
2. **Use specific research data** — pull from Sections A-H
3. **Not sound "salesy"** — read it aloud; does it sound like a fascinating conversation?
4. **End with a transition** — set up the story that follows (next chapter in the formula)

**Critical**: Adapt these to YOUR market. Do not copy Settle's examples word-for-word. The templates are shells — fill them with the market's language from the research.

### Step 5: Write the "Bite-Sized" Condensed Versions

For each of the 9 openers, also produce a 1-2 sentence ultra-condensed version. These are for mobile, short attention spans, or email.

### Step 6: Select Top 3 Picks

Choose the 3 strongest openers. For each, write a one-sentence reason WHY it's strong, referencing the research data and which Settle principle it embodies.

### Step 7: Format and Deliver

Save to `research-outputs/<niche-slug>/YYYY-MM-DD_opening-paragraphs.md`:

```markdown
# Ben Settle Opening Paragraphs: [NICHE]
**Generated**: YYYY-MM-DD
**Research basis**: [path to research folder]
**Headline used**: [if applicable — which headline this bridges from]

## Opener 1: "Let me tell you a story"
[2-3 options, each 3-5 sentences]

## Opener 2: If/Then
[2-3 options]

## Opener 3: If/Then (with proof)
[2-3 options]

## Opener 4: Brutal and Blatant Honesty
[2-3 options]

## Opener 5: Sensationalist
[2-3 options]

## Opener 6: Ask a Question
[2-3 options]

## Opener 7: Do You Know?
[2-3 options]

## Opener 8: The Bite-Sized Open
[2-3 options]

## Opener 9: Would You Take Advice From?
[2-3 options]

## Bite-Sized Condensed (Mobile/Email)
[1-2 sentence versions of each]

## Top 3 Picks
[Curated with reasoning]
```

### Step 8: Present to User

Present the Top 3 Picks with reasoning. Offer to show all 9 categories. Ask which resonate.

## Reference Files

- `references/worked-example.md` — **READ THIS FIRST.** 9 step-by-step data→opening paragraph transformations.
- `references/9-opening-types.md` — Complete methodology: why each type works, construction formulas, classic examples.
- `references/data-to-opening-map.md` — Which research data fields feed which opener type, with extraction methods.
