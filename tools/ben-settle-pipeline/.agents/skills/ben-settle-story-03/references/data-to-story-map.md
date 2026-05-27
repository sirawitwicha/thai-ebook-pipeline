# Data → Story Map

How each research data field — AND the prior headline and opening paragraph outputs — feeds the 7-part story scaffold and 5 story types.

**CRITICAL**: The story is step 3 in a narrative chain. Read the headline and opening paragraph files FIRST. The protagonist, enemy, emotional hook, and narrative voice were already established. Do not invent new ones. The story's job is to CONTINUE what the opener started and PAY OFF what the headline promised.

## Continuity Sources (Read Before Raw Research)

| Continuity Element | Source File | What to Extract |
|---|---|---|
| Protagonist identity | `*_opening-paragraphs.md` | Who was introduced? Name? Situation? Belief? |
| Emotional hook | `*_headlines.md` (Top Picks) | What emotion did the headline rack? The story must embody this. |
| Enemy name/type | Headline + Opener | Was the enemy named? Use the SAME one. |
| Promise made | Headline + If/Then opener | What was the reader promised? The story is evidence for this promise. |
| Where the opener STOPPED | Last paragraph of chosen opener | Section 1 of the story STARTS here. |
| Narrative voice | Opener + Tone calibration | First person? Third person? Defiant? Weary? Match it. |

## Quick Reference: Which Data Feeds Which Section

| Scaffold Section | Primary Data Sources |
|---|---|
| 1. The Setup | `primary_buyer_description`, `bar_complaint_monologue` (opening), `identity_and_worldview.values` |
| 2. Problem Escalates | `pain_and_fear.keeps_awake_at_night`, `pain_and_fear.pain_emotional`, `pain_and_fear.pain_physical`, `slang_dictionary` (Emotional States category) |
| 3. Rock Bottom | `pain_and_fear.urgent_crisis`, `bar_complaint_monologue` (most emotional paragraph), `pain_and_fear.insecurities`, `pain_and_fear.guilt_sources` |
| 4. The Discovery | `competitive_intelligence.number_one_urgent_problem`, `proof_elements`, `desires_and_aspirations.secret_fantasies`, `slang_dictionary` (historical/counterintuitive entries) |
| 5. The Transformation | `desires_and_aspirations.what_they_want_most`, `emotional_drivers.desired_feeling_on_arrival`, `desires_and_aspirations.secret_fantasies` |
| 6. The Evidence | `proof_elements`, `competitive_intelligence.competitors[].proof_elements`, `slang_dictionary` (Pop Culture & Philosophical Touchstones) |
| 7. The Bridge | `copy_brief.primary_hook`, `desire_anchors` |

## Quick Reference: Which Data Feeds Which Story Type

| Story Type | Critical Data Sources |
|---|---|
| 1. Story About You | `bar_complaint_monologue` (as first-person), `pain_and_fear.*` (personal struggle), `desires_and_aspirations.what_they_want_most` (the discovery) |
| 2. Story About Someone Else | YouTube comments (real stories), Reddit threads, `slang_dictionary` (for their voice), `pain_and_fear.*` (their suffering) |
| 3. Dramatized (Parable) | ALL pain data (composite character), `primary_buyer_description` (the protagonist), `the_enemy` (the antagonist), `urgent_crisis` (the dramatic stakes) |
| 4. Historical Story | `proof_elements` with historical weight, `slang_dictionary` (Pop Culture & Philosophical Touchstones), `competitive_intelligence.competitors[].name` (historical figures) |
| 5. Meet The Guru | `competitive_intelligence.competitors[0]` (the guru), `proof_elements` (guru's credentials), `primary_buyer_description` (the student who seeks the guru) |

---

## Deep Dive: Extracting Story Material

### From `structured-profile.json`

| Field | Story Use |
|---|---|
| `pain_and_fear.keeps_awake_at_night[]` | The EXACT suffering details for Sections 2-3. Each entry is a story beat. |
| `pain_and_fear.anger_triggers[]` | What made them furious. This is the antagonist's actions in the story. |
| `pain_and_fear.insecurities[]` | Internal conflict. The shame they couldn't tell anyone. Rock bottom material. |
| `pain_and_fear.urgent_crisis` | The WHY NOW. The stakes. What happens if they DON'T solve this? |
| `desires_and_aspirations.enemies[]` | The villain. Every story needs an antagonist. This IS the antagonist. |
| `desires_and_aspirations.secret_fantasies[]` | The "heaven" outcome. What the protagonist dreams of. |
| `desires_and_aspirations.what_they_want_most` | The core desire. The emotional resolution of the story. |
| `emotional_drivers.feelings_during_search` | The protagonist's emotional state. Use these exact words in the story. |
| `emotional_drivers.desired_feeling_on_arrival` | The transformation arc. Hell → Heaven. |
| `identity_and_worldview.primary_buyer_description` | The protagonist's identity. Age, role, beliefs. "Sarah, 34, mid-level manager..." |
| `competitive_intelligence.competitors[]` | Authority figures for Meet The Guru. Historical research for Type 4. |

### From `copy-brief.md`

| Section | Story Use |
|---|---|
| `primary_hook` | The thematic spine of the story. Every section should echo this. |
| `pain_point_bullets` | Each bullet IS a story beat for Sections 2-3. Flesh them out into scenes. |
| `the_enemy` | The antagonist description. Their defining trait. How they operate. |
| `desire_anchors` | The "heaven" outcomes. What the story promises. |
| `proof_elements` | Credibility for Section 6. Historical anchors. Authority figures. |
| `tone_calibration` | The narrative voice. Anger-driven = gritty. Aspiration-driven = hopeful. |
| `bar_complaint_monologue` | **THE single most valuable source.** Rewrite it in third person for Type 2. Keep it first person for Type 1. Use its exact emotional arc for all types. |

### From `slang-dictionary.md`

| Category | Story Use |
|---|---|
| Power & Manipulation Tactics | The antagonist's playbook. What the enemy DOES. |
| Emotional States | The protagonist's inner world. How they FEEL at each stage. |
| Survival & Counter-Strategies | The discovery. What the protagonist learned to do. |
| Corporate Speak & Euphemisms | World-building details. Makes the story feel real and specific. |
| Identity & Self-Labels | The protagonist's self-concept. "I was a total skeptic." |
| Metaphors & Imagery | Vivid language for every section. "The ladder is a vertical tunnel of shit." |
| Direct Quotes | **Narrative voice.** Drop these verbatim into the story. Dialogue, inner thoughts, realizations. |

---

## The "Composite Character" Method (for Type 3 — Parables)

When creating a dramatized story, build ONE character from multiple research sources:

1. **Name**: Use a blank (____) or a common first name. Never a real person's name without permission.
2. **Identity**: From `primary_buyer_description` — their age, role, beliefs.
3. **Suffering**: From `pain_and_fear` — pile 3-4 specific pains onto one character.
4. **Voice**: From `slang_dictionary` Direct Quotes — their inner monologue uses market language.
5. **Breaking point**: From `bar_complaint_monologue` — the emotional climax.
6. **Discovery**: From `desire_anchors` + `proof_elements` — what they found and why it's credible.

This creates a character who is NOT any real person, but feels MORE real because they embody the entire market's experience.
