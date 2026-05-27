---
name: ben-settle-close-05
description: Generate high-converting sales letter closes using Ben Settle's 4 close components (Guarantee, Bonuses, Takeaway, PS), powered by the full narrative chain and market research data. This is the 5th and final step in the Copy Slacker formula — where you get paid. Use when the user wants to write a close, create an offer, write a guarantee, design bonuses, write a PS, or complete the final step of a sales letter. Triggers on: "write a close", "closing", "sales close", "offer section", "guarantee", "bonuses", "P.S.", "call to action", "Ben Settle close", "copy slacker step 5", "get paid", "how to close my ad".
---

# Ben Settle Close Generator

Turns the full narrative chain + market research into sales letter closes using Ben Settle's 4 close components from *Copy Slacker* Chapter 7.

**Role in the 5-step formula**: Headline hooks → Opening bags the attention → Story pays it off → Bullets build desire → **CLOSE gets paid**. You've got them dressed up wanting to go somewhere. That somewhere is to buy what you're selling.

## THE RULES

1. **The close does not start fresh.** It continues from everything that came before — same voice, same enemy, same emotional arc, same slang. If the story used 1st person, the close uses 1st person. If the headline was defiance, the close is defiance.

2. **You do not invent bonuses or guarantees from thin air.** Every bonus must anchor to a desire, secret fantasy, or pain point from the research data. Every guarantee must address a specific objection from the inventory. Every takeaway must name a real type of bad-fit buyer the research revealed.

3. **Always include a deadline.** "Nothing gets done without a deadline." Even if the user doesn't specify one, generate deadline language. It could be a date to get a bonus by, a lower price by, or the threat of the offer closing.

4. **Testimonials never interrupt narrative flow.** They go in sidebars or PS sections — never mid-story, never mid-bullets. Inserting a testimonial mid-flow is "like putting up a sign that says STOP READING."

5. **The takeaway must be genuine, not a tactic.** It must be rooted in honesty about who the product is actually for and not for. It cannot sound like attitude-for-attitude's-sake. Matter-of-fact, not performative.

## Prerequisites

**Required**:
- `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`
- `*_headlines.md`, `*_opening-paragraphs.md`, `*_story.md`, `*_bullets.md` — the full narrative chain

**Optional but powerful**:
- `*_story-mining.md` — enriched data for bonus stories, PS stories, proof anchoring
- `*_close-mining.md` — buying-decision intelligence: deep objections, competitor offers, bonus demand signals, refund horror stories

## Workflow

### Step 1: Locate and Load Everything

Glob `research-outputs/*/` to find the project folder. Read ALL files:

1. `structured-profile.json` — desires, secret fantasies, objections, proof
2. `slang-dictionary.md` — exact prospect language for bonus names, takeaway language
3. `copy-brief.md` — primary hook, the enemy, tone calibration, competitive positioning
4. `*_headlines.md` — note the Top Picks (continuity anchor)
5. `*_opening-paragraphs.md` — note the Top Picks (continuity anchor)
6. `*_story.md` — note the protagonist, emotional arc, story type (continuity anchor)
7. `*_bullets.md` — note the strongest bullets (can repurpose in PS)
8. `*_story-mining.md` — if exists, for bonus stories and PS material
9. `*_close-mining.md` — if exists, for enriched objections, competitor offers, bonus demand signals

### Step 2: MANDATORY — Read the References

Read `references/4-close-components.md` for the full methodology behind each component. Read `references/data-to-close-map.md` for which research data feeds which component.

### Step 3: MANDATORY — The Close Brief

Before writing a single line, fill out this brief from the research data:

#### Section A: The Narrative Chain Summary
From the headline, opener, and story files:
- Which headline was used? What's its dominant emotion?
- Which opener was used? What's its narrative voice (1st/3rd person)?
- What story type was used? Who is the protagonist?
- What was the story's transformation arc? (Hell → Heaven)

#### Section B: The Product Identity
From the copy brief and research context, define:
- What is being sold? (product name, format, core promise)
- What type of offer is this? (ebook, course, newsletter, coaching, physical product, SaaS)
- Price point (if known) or price range

#### Section C: Guarantee Raw Material (from objection_inventory + competitive_positioning)
Extract:
- Every objection verbatim — each one suggests a guarantee angle
- Competitor weaknesses — what they DON'T offer that you can guarantee
- Risk level of the market (mass market cold → yes guarantee; warm list → optional)
- The most dramatic, ballsy guarantee this market data supports

#### Section D: Bonus Raw Material (from secret_fantasies + desire_anchors + slang)
Extract:
- Every secret fantasy — each is a potential bonus
- Every desire anchor — each is a bonus topic
- Slang terms that could NAME a bonus (e.g., "The Grey Rock Protocol," "The Sunday Scaries Cure")
- The top 3-5 most emotionally charged desires from the research

#### Section E: Takeaway Raw Material (from objection_inventory + primary_buyer_description + the_enemy)
Extract:
- Who should NOT buy this? (from objections, pain data, bar complaint monologue)
- What type of person is the ENEMY? (these people are NOT qualified)
- What type of person is the IDEAL buyer? (the takeaway defines the OPPOSITE of who's excluded)
- A genuine reason rooted in the product's reality — not a fake reason

#### Section F: PS Raw Material (from proof_elements + bullets + story-mining)
Extract:
- A strong testimonial or proof element (if available)
- 2-3 of the strongest bullets that could be expanded into a PS story
- A deadline angle (what expires? when? why?)
- A story-mining factoid that didn't fit in the main story

#### Section G: The Deadline
Define:
- What expires? (bonus, price, availability, the offer itself)
- When? (specific date or trigger)
- Why is it real? (limited quantity, launch window, beta pricing, etc.)

### Step 3b: Check Close Data — To Scrape or Not to Scrape?

The 5 core research files provide pain, desires, slang, and basic objections. But close-specific data (deep objections from real buyers, competitor offer details, refund horror stories, bonus demand signals, takeaway validation) may need additional scraping.

**Check what exists**:
- Does the objection inventory have 10+ entries with detailed neutralization strategies? If yes, you may have enough for guarantees.
- Does the competitive positioning map include competitor PRICES and GUARANTEES? If yes, you may have enough for anchoring.
- Does the slang dictionary include "I wish someone would..." or "does anyone have a template for..." type quotes? If yes, you may have enough for bonuses.
- Does the folder contain a `*_close-mining.md` file? If yes, read it — you have enriched close data.

**Ask the user**: "I can write the close with the existing research data alone — it'll be solid. But if you want richer detail (deeper objections from real buyer reviews, competitor pricing and guarantees, exact bonus ideas the market is asking for, refund horror stories to reverse-engineer the guarantee against), I can scrape additional close-mining data. This adds ~$0.30-0.80 and 2-4 minutes. Scrape more, or proceed with what we have?"

If the user says scrape: read `references/close-mining-queries.md`. Assess which of the 6 categories need data (skip categories where sufficient data already exists). Run only the needed categories. Save results to `research-outputs/<niche-slug>/YYYY-MM-DD_close-mining.md`.

If the user says proceed: move to Step 4 with existing data.

If the user doesn't specify: proceed with existing data. Most closes can be written well from the 5 core research files alone.

### Step 4: Write the Connector

Write a short, punchy connector paragraph (1-3 sentences) that transitions from bullets into the close. It should:
- Feel like a natural conclusion to the bullet section
- Not be a hard-sell pivot ("and now, the offer!")
- Reference the primary hook implicitly
- Set up the offer without announcing it

Settle's approach: "I like to go into the close right after the bullets. If you did the first 4 parts right, did your research right, and are offering them something they want... then you've got them all dressed up wanting to go somewhere."

### Step 5: Write the 4 Close Components

Read `references/4-close-components.md` for the full methodology.

Generate each component separately. Not every close needs all 4 — the brief will tell you which are appropriate.

**Component 1: The Guarantee** (if appropriate for this market)
- 3 options: conservative, dramatic, and extreme (Ben's "balls-to-the-wall" style)
- Each must tie to a specific objection from the research

**Component 2: Bonuses**
- 3-5 bonuses, each named in the market's language
- Each bonus has: name (using slang), 1-2 sentence description, verifiable value anchor
- At least one bonus should be so compelling "people would buy just to get it"

**Component 3: The Takeaway**
- 2-3 variations of who should NOT buy
- Must be genuine and rooted in the product's reality
- Each names a specific type of bad-fit buyer the research revealed

**Component 4: The Almighty PS**
- 2-3 PS variations (different approaches: testimonial PS, bonus story PS, takeaway PS, deadline PS)
- Each has a clear purpose — not PS for PS's sake

### Step 6: Write the Offer Block

Assemble the components into the actual offer. Include:
1. Connector paragraph
2. What they get (product + all bonuses listed)
3. The price (or price anchoring if price is unknown)
4. The guarantee (if used)
5. The deadline
6. The CTA (call to action — what they click/do)

### Step 7: Select Top 2 Configurations

Choose the 2 strongest close configurations. For each, write a one-sentence reason WHY, referencing the research data and which Settle principle it embodies.

### Step 8: Format and Deliver

Save to `research-outputs/<niche-slug>/YYYY-MM-DD_close.md`:

```markdown
# Ben Settle Close: [NICHE]
**Generated**: YYYY-MM-DD
**Narrative chain**: [headline type] → [opener type] → [story type] → [bullet count] bullets

## Narrative Chain Summary
**Headline**: [verbatim]
**Opener**: [first sentence]
**Story**: [protagonist + arc summary in one line]

---

## Connector (Bullets → Offer)
[1-3 sentences]

## Component 1: The Guarantee
[2-3 options — conservative, dramatic, extreme]

## Component 2: Bonuses
[3-5 named bonuses with descriptions]

## Component 3: The Takeaway
[2-3 variations of who should NOT buy]

## Component 4: The Almighty PS
[2-3 PS variations]

## Offer Block — Configuration A
[Assembled close: connector → offer → bonuses → guarantee → deadline → CTA]

## Offer Block — Configuration B
[Alternative assembly]

## Top 2 Picks
[With reasoning]
```

### Step 9: Present to User

Present the Top 2 Picks with reasoning. Offer to show all components. Ask which resonate — use feedback to refine.

## Reference Files

- `references/4-close-components.md` — **READ THIS FIRST.** Complete methodology for each of the 4 components with classic examples from Ben's own ads.
- `references/data-to-close-map.md` — Which research data fields and narrative chain elements feed which close component.
- `references/close-mining-queries.md` — 6-category query strategy for scraping close-specific enriched data (objections, competitor offers, bonus demand signals, refund horror stories).
- `references/worked-example.md` — Full close written step-by-step from the dark-psychology research data.
