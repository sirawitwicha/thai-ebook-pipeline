# Data → Opening Paragraph Map

How each research data field from `ben-settle-research` output feeds specific opening paragraph types.

## Quick Reference

| Opener | Primary Data Sources | What to Extract |
|---|---|---|
| 1. Let me tell you a story | `bar_complaint_monologue`, `desires_and_aspirations.enemies`, YouTube comments | A specific, vivid story about the enemy, a customer, or the discovery moment |
| 2. If/Then | `number_one_urgent_problem`, `desires_and_aspirations.what_they_want_most`, `primary_buyer_description` | The condition (their pain) → the benefit (what they want) |
| 3. If/Then + Proof | Above + `proof_elements`, `competitive_intelligence.competitors[].proof_elements`, slang historical references | The condition → the proof-anchored benefit → "and you can do it today" |
| 4. Brutal Honesty | `objection_inventory`, `insecurities`, `competitors[].weaknesses` (your own flaws) | What you're NOT, what your product WON'T do, the uncomfortable truth |
| 5. Sensationalist | Slang unusual entries, `tabloid_quirk`, surprising YouTube comments, `secret_fantasies` | Bizarre, surprising, "tabloid cover" detail |
| 6. Ask a Question | `competitive_intelligence` gaps, `slang_dictionary` counterintuitive entries, `pain_and_fear` vs `desires` contrasts | Surprising fact that contradicts market belief |
| 7. Do You Know? | `daily_frustrations_top3`, `pain_and_fear.insecurities`, slang that reveals wrong assumptions | Counterintuitive facts that challenge universal assumptions |
| 8. Bite-Sized Open | `dominant_resident_emotion`, `bar_complaint_monologue` (first line), `primary_buyer_description` | 2-4 word gut-punch |
| 9. Would You Take Advice? | `enemies` (as the source), `proof_elements`, `competitive_positioning_map` | Outrageous source + dramatic teaser from research |

---

## Deep Dive: Extracting Opener Material

### From `copy-brief.md`

| Section | Opener Use |
|---|---|
| `headline_starters` / Top Picks | The opener bridges FROM a specific headline. Reference its emotion or promise. |
| `pain_point_bullets` | If/Then condition: "If you've ever [pain bullet]..." |
| `the_enemy` | "Let me tell you a story about [the enemy]." Also: "Would you take advice from [the enemy]?" |
| `desire_anchors` | The "then" part of If/Then: "...then here's how to [desire anchor]." |
| `proof_elements` | Inject into If/Then + Proof. Pick the most dramatic, visual, story-worthy ones. |
| `objection_inventory[].objection` | Brutal Honesty: lead with these. "Yes, this [IS/IS NOT] [objection]." |
| `tone_calibration` | Determines opener voice. Anger-driven → defiant Brutal Honesty. Aspiration → story-driven. |
| `bar_complaint_monologue` | **Most valuable for openers.** The first 2-3 sentences of the monologue ARE an opener. The story of "I didn't sign up for this" IS the "let me tell you a story." |

### From `structured-profile.json`

| Field | Opener Use |
|---|---|
| `pain_and_fear.keeps_awake_at_night[0]` | If/Then condition, Sensationalist hook, "Do You Know?" consequence |
| `pain_and_fear.urgent_crisis` | The WHY behind the If/Then — "If you're experiencing [crisis], then..." |
| `pain_and_fear.anger_triggers` | Brutal Honesty: "Yes, this might make you angry. Good." |
| `pain_and_fear.insecurities` | Brutal Honesty: "I'm not [credential]. I'm not [authority]. In fact..." |
| `desires_and_aspirations.enemies[0]` | Story villain, "Would you take advice from?" source |
| `desires_and_aspirations.secret_fantasies` | Sensationalist hook, If/Then benefit |
| `desires_and_aspirations.what_they_want_most` | The "then" benefit |
| `identity_and_worldview.primary_buyer_description` | The "if" condition target |
| `competitive_intelligence.number_one_urgent_problem` | The core If/Then condition |
| `competitive_intelligence.competitors[].weaknesses` | Brutal Honesty: what you're NOT compared to them |
| `competitive_intelligence.market_awareness_1_to_10` | Determines opener sophistication: low awareness → story/curiosity openers; high awareness → direct If/Then |
| `emotional_drivers.feelings_during_search` | Bite-Sized Open: distill the dominant feeling into 2-4 words |
| `emotional_drivers.desired_feeling_on_arrival` | The emotional promise woven into If/Then |

### From `slang-dictionary.md`

| Category | Opener Use |
|---|---|
| Power & Manipulation Tactics | "Do You Know?" counterintuitive facts, Sensationalist details |
| Emotional States | "Let me tell you a story" emotional texture, Bite-Sized Open |
| Survival Strategies | If/Then proof ("how they did it"), Brutal Honesty ("what I'm not") |
| Corporate Speak & Euphemisms | "Do You Know?" — "Do you know what 'visibility problem' really means?" |
| Identity & Self-Labels | Brutal Honesty self-description, Bite-Sized Open identity statement |
| Metaphors & Imagery | Sensationalist vivid language, story texture |
| Direct Quotes | **The narrative voice for every opener.** These ARE your opening sentences. |

---

## Critical Transitions

Every opener must end by transitioning into the story. Stockpile these transition patterns:

- "And the story of how [this happened / I discovered this / this works] is..."
- "But before I show you [the solution], let me tell you what happened when..."
- "Here's what I found — and why it changes everything..."
- "The reason why goes back to [timeframe / discovery moment]..."
- "It sounds absurd. But there's a true story behind it..."
