# Data → Headline Map

How each research data field from `ben-settle-research` output feeds specific headline types. Always pull exact language from the data — the best headlines are HARVESTED, not written.

---

## Quick Reference: Which Data Feeds Which Type

| Headline Type | Primary Data Sources | What to Extract |
|---|---|---|
| 1. Proof | `proof_elements`, `competitive_intelligence.competitors[].proof_elements` | Credibility markers, authority figures, certifications, institutional validation |
| 2. Market-Oriented | `pain_and_fear.*`, `desires_and_aspirations.enemies`, `bar_complaint_monologue` | Exact pain/fear/insecurity language, identity statements, worldview |
| 3. Emotion | `emotional_drivers.feelings_during_search`, `pain_and_fear.anger_triggers`, `pain_and_fear.pain_emotional` | Dominant resident emotion, frustration language, emotional words |
| 4. Blatant Offer | `desires_and_aspirations.what_they_want_most`, `competitive_intelligence.number_one_urgent_problem` | What they desperately want, the irresistible offer |
| 5. Contrast | `pain_and_fear.*` vs `desires_and_aspirations.secret_fantasies`, slang contradictions | Paradoxes, counterintuitive truths, "how to X without Y" |
| 6. Tabloid | Slang dictionary unusual entries, `competitive_intelligence.competitors[].weaknesses`, unique proof elements | Sensational quirks, unusual creator stories, surprising data points |
| 7. Curiosity | Slang dictionary (insider terms), `pain_and_fear.*`, `media_and_culture.online_communities` | Insider knowledge the market doesn't know yet, "what never to X" |
| 8. Straight Benefit | `number_one_urgent_problem`, `desires_and_aspirations.what_they_want_most` | Specific, measurable benefit addressing urgent problem |
| 9. Question | `bar_complaint_monologue`, `pain_and_fear.keeps_awake_at_night`, `objection_inventory` | Questions the market is already asking themselves |
| 10. Objection | `objection_inventory`, `bar_complaint_monologue`, `pain_and_fear.insecurities` | Their skepticism, what they don't believe, "this won't work because..." |
| 11. Combine & Conquer | Any combination of the above | Merge two headline types using their respective data sources |

---

## Deep Dive: Extracting Headline Material from Each Data Field

### From `pain_and_fear`

| Field | Headline Use |
|---|---|
| `keeps_awake_at_night` | Market-Oriented, Emotion, Question headlines. These ARE headlines waiting to be formatted. |
| `top_terrors_ranked` | Emotion, Market-Oriented. "What they're terrified of" = the emotional core of your headline. |
| `anger_triggers` | Emotion, Market-Oriented. Anger is the easiest emotion to rack a shotgun with. |
| `anger_targets` | Market-Oriented, Objection. "Who they're angry at" = the enemy you can name in the headline. |
| `urgent_crisis` | Straight Benefit, Blatant Offer. The crisis is WHY they need the solution NOW. |
| `daily_frustrations_top3` | Emotion, Market-Oriented. Daily frustrations = headlines they'll read during those frustrations. |

**Extraction method**: Look for phrases that make you FEEL something. If a line from the pain data makes YOU angry or sad, it will make the prospect feel seen.

### From `identity_and_worldview`

| Field | Headline Use |
|---|---|
| `values` | Market-Oriented. "What lines won't they cross?" — your headline must not violate these. |
| `slang_dictionary` | EVERY headline type. Slang makes you sound like an insider. Drop one perfect slang term into a headline and it transforms. |
| `primary_buyer_description` | Market-Oriented. "This is for [buyer], not [non-buyer]" — filtering headline. |

**Extraction method**: The slang dictionary is your headline vocabulary. Scan it before writing. Each slang term is a potential headline anchor word.

### From `desires_and_aspirations`

| Field | Headline Use |
|---|---|
| `enemies` | Market-Oriented, Emotion, Tabloid. Naming the enemy in a headline = instant shotgun rack. |
| `what_they_want_most` | Blatant Offer, Straight Benefit, Contrast. The fantasy outcome = the promise in your headline. |
| `secret_fantasies` | Tabloid, Curiosity, Contrast. "What they secretly want" = the thing they'll read about. |
| `bar_complaint_monologue` | Question, Objection, Emotion, Market-Oriented. **THIS IS THE SINGLE MOST VALUABLE FIELD FOR HEADLINES.** Read it aloud. The headline is hiding in here — find their exact phrasing. |

**Extraction method**: The bar complaint monologue is where Settle found his "Golf God" headline. A prospect literally said the headline in their own words. Look for phrases in quotation marks, emotional outbursts, and "I just want..." statements.

### From `competitive_intelligence`

| Field | Headline Use |
|---|---|
| `number_one_urgent_problem` | Straight Benefit. This IS the benefit your headline promises to solve. |
| `competitors[].weaknesses` | Proof, Objection, Contrast. What competitors can't claim = what YOUR headline CAN claim. |
| `market_awareness_1_to_10` | Determines headline sophistication. 1-3: must name the problem. 7-10: can be more direct/offer-based. |
| `competitive_positioning_map[].your_gap` | Proof, Contrast. The gap YOU fill = the unique angle for your headline. |

### From `emotional_drivers`

| Field | Headline Use |
|---|---|
| `feelings_during_search` | Emotion, Market-Oriented. What they're feeling when they find you = what your headline must speak to. |
| `desired_feeling_on_arrival` | Contrast, Blatant Offer. The transformation arc = [current state] → [desired state] contrast headlines. |

### From `copywriting_brief`

| Field | Headline Use |
|---|---|
| `headline_starters` | Directly adaptable. These are raw headline ideas from the research phase — refine them using the 11 types. |
| `primary_hook` | The core angle. Every headline should be a variation on this hook. |
| `pain_point_bullets` | Market-Oriented, Emotion. Bullet language = headline language. Read bullets as headline fragments. |
| `the_enemy` | Market-Oriented, Tabloid, Proof. Naming the enemy = instant identification. |
| `slang_dictionary` | Same as above — this is your headline vocabulary. |
| `proof_elements` | Proof. Every proof element is a potential headline anchor. |
| `objection_inventory[].objection` | Objection. Each objection IS a potential headline. The objection itself, stated honestly. |
| `tone_calibration` | Determines headline voice. Anger-driven = aggressive headlines. Aspiration-driven = desire headlines. |
| `competitive_positioning_map` | Proof, Contrast. "What they say vs what we say" = contrast headline. |

---

## The Harvesting Process

Ben Settle didn't "write" his best headline. He HARVESTED it. Here's how to do the same:

1. **Read the bar complaint monologue out loud.** Listen for a phrase that hits you in the gut.
2. **Scan the slang dictionary.** Look for terms that are unique to this market. Drop one into any headline type.
3. **Search the pain data for "I just want..." or "I hate..." or "Why does..." statements.** These are headlines in raw form.
4. **Look at the objection inventory.** The market's skepticism told honestly = the most credible headline possible.
5. **Find a proof element no competitor can claim.** Join it to your biggest promise.
6. **Identify the ONE emotion that defines this market.** Lead with it.

---

## Quality Check: Does This Headline Pass?

Before finalizing any headline, ask:

1. **Knock-Knocks test**: Would this get the door opened, or would it get slammed?
2. **Shotgun rack test**: Does this cut through all distractions and demand attention?
3. **Market language test**: Could a competitor write this same headline? If yes, it's not specific enough.
4. **Curiosity test**: Does this create an itch that must be scratched?
5. **Believability test**: Does this sound like a scam, or does the proof make it credible?
6. **6-7 word test**: Can the core idea be expressed in 6-7 words? If not, it may be too complex.
