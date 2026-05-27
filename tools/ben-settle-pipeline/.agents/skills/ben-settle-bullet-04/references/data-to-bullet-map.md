# Data to Bullet Map — Which Research Feeds Which Bullet Type

Every bullet type pulls from specific research data fields. This reference maps each of the 12 types to its exact data sources, with extraction methods and quality checks.

---

## Quick Reference Matrix

| Bullet Type | Primary Source | Secondary Source | Batch |
|---|---|---|---|
| **#1 Curiosity** | Slang terms + Counterintuitive facts | Pain points | 1, 2, 5 |
| **#2 Can't Be Done** | Counterintuitive facts | Secret fantasies, Story-mining Cat 1 | 2, 6 |
| **#3 Proof & Credibility** | Proof anchors | Story-mining Cat 2/5/6 | 3, 6 |
| **#4 Contrast** | Proof anchors + Enemy details | Competitor weaknesses + Your gap | 3, 5 |
| **#5 Pain** | Pain points (verbatim) | Anger triggers, Enemy behaviors | 1, 5 |
| **#6 Straight Benefit** | Desire statements | What they want most, Secret fantasies | 4 |
| **#7 What NOT To Do** | Mistakes/Failures | Objections, story-mining Cat 4 | 1, 4 |
| **#8 Giveaway** | Proof elements (fully disclosable) | Insider knowledge (story-mining Cat 8) | 3, 6 |
| **#9 90% Solution** | Slang terms (with hidden depth) | Counterintuitive facts, Pain data | 2, 4 |
| **#10 Dramatic Sub-Head** | Any strong bullet's last 6-8 words | — | 7 |
| **#11 Compressed Finale** | All remaining unused data | — | 7 |
| **#12 Expansion** | Any high-value bullet (from batches 1-6) | Story-mining narrative paragraphs | 7 |

---

## Detailed Data-to-Type Mapping

### Type 1: Curiosity

**What it needs**: Something fascinating but incomplete. The reader MUST know the rest.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| `slang-dictionary.md` — ALL categories | Every slang term with quotation marks | Take the term → find the most surprising implication → state it but withhold the mechanism |
| `structured-profile.json` → pain_and_fear | `keeps_awake_at_night`, `anger_triggers` | Take a vivid pain point → hint at a counterintuitive cause or solution |
| `*_story-mining.md` — Category 1 | Bizarre & counterintuitive facts | State the bizarre fact → don't explain why it works |
| `structured-profile.json` → desires_and_aspirations | `secret_fantasies` | Hint at the fantasy being achievable → don't reveal how |
| `copy-brief.md` | The Enemy description | Name an enemy behavior → hint at a counter but don't reveal it |

**Construction pattern**: `[Specific detail/term/behavior] — and [surprising implication they must know]`

**Quality check**: Would a reader in this market feel an URGENT need to know the answer? If not, the curiosity isn't strong enough.

---

### Type 2: "Can't Be Done"

**What it needs**: A claim ALMOST unbelievable but TRUE. Right on the cusp of reality.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| `*_story-mining.md` — Category 1 | Bizarre & counterintuitive facts | State the bizarre fact as a claim → the truth makes it believable |
| `structured-profile.json` → desires_and_aspirations | `secret_fantasies` | Frame the fantasy as achievable → it sounds impossible but IS possible |
| `*_story-mining.md` — Category 3 | Dramatic personal stories | Extract the most dramatic turnaround → frame as a how-to claim |
| Slang terms with extreme implications | Terms like "untouchable," "invisible," "destroyed" | Frame the slang term's extreme implication as an achievable outcome |

**Construction pattern**: `How to [achieve seemingly impossible outcome] — and [specific detail that makes it credible]`

**Quality check**: Does this sound ALMOST too good to be true? If it sounds like an ordinary claim, it's not a Can't Be Done.

---

### Type 3: Proof & Credibility

**What it needs**: A benefit attached to a named authority, historical figure, documented fact, or statistic.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| `copy-brief.md` → Proof Elements | Every proof element | Attach a benefit claim to a proof element. "The [technique] that [historical figure] used to [achieve result]." |
| `*_story-mining.md` — Category 2 | Historical origin & gravitas | Name-drop the historical figure + what they did + modern application |
| `*_story-mining.md` — Category 5 | News events | "As reported in [publication], [fact] — and here's what it means for you." |
| `*_story-mining.md` — Category 6 | Specific numbers | "A study of [X] people found [Y]. Here's how to use that finding." |
| `structured-profile.json` → competitive_intelligence | Competitor data | "While [competitor] teaches [X], [proof source] proved [Y] actually works." |

**Construction pattern**: `The [technique/principle] that [named authority/historical figure/source] [used/proved/discovered] — and [how it applies to reader's problem]`

**Quality check**: Is the proof source NAMED? Anonymous proof ("studies show") doesn't count. Specific proof ("a 2019 Harvard study of 567 employees") counts.

---

### Type 4: Contrast

**What it needs**: Two ideas that don't belong together, forced into the same bullet. The clash creates irresistible tension.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| Proof anchors + Enemy details | Two data sources that CLASH | Pair an enemy behavior with a proof element. "How [enemy behavior] actually reveals [counterintuitive truth backed by proof]." |
| `copy-brief.md` → competitive_positioning | Competitor weaknesses + Your gaps | "Why [competitor's famous advice] is exactly what [the enemy] WANTS you to do." |
| Slang term + Opposite meaning | Two slang terms that contradict | "Why [slang term A] is the enemy of [slang term B] — and which one to use." |
| Desire + Pain | A desired outcome + a painful consequence of pursuing it wrong | "How [desire] can actually [cause pain] — unless you know [one thing]." |

**Construction pattern**: `[Idea A] + [Idea B that contradicts it] = [surprising resolution]`

**Quality check**: Do the two elements actually clash? P.T. Barnum and Mother Theresa in the same sentence is jarring. Generic contrast ("buy this, not that") is not.

---

### Type 5: Pain

**What it needs**: A specific, vivid, cringe-inducing consequence. Physical or psychological. The reader should flinch.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| `structured-profile.json` → pain_and_fear | `keeps_awake_at_night` (verbatim) | Take the pain verbatim → add one more layer of consequence |
| `structured-profile.json` → pain_and_fear | `pain_emotional`, `pain_psychological` | State the emotional consequence → make it hyper-specific |
| `structured-profile.json` → pain_and_fear | `anger_triggers` | The trigger + the visceral reaction it causes |
| `copy-brief.md` | The Enemy description | Enemy behavior + the feeling it creates IN THE READER |
| `slang-dictionary.md` | Direct Quotes — emotionally charged complaints | Use the exact complaint language — it's pre-calibrated for pain |

**Construction pattern**: `[Specific situation] → [visceral consequence]. The reader thinks: "That's me."`

**Quality check**: Does it make YOU uncomfortable reading it? If you don't flinch, neither will they.

---

### Type 6: Straight Benefit

**What it needs**: A clear, specific benefit. What they get. No tricks — the benefit IS the hook.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| `structured-profile.json` → desires_and_aspirations | `what_they_want_most` | State the desired outcome directly. "How to [desired outcome]." |
| `structured-profile.json` → desires_and_aspirations | `secret_fantasies` | State the fantasy as achievable. Make it specific, not vague. |
| `copy-brief.md` | Desire Anchors | Each anchor is a benefit bullet ready to format |
| `slang-dictionary.md` | Terms describing desired states | Frame the term as an outcome. "How to become [slang term for desired state]." |

**Construction pattern**: `How to [specific, measurable benefit] — [optional second benefit for double whammy]`

**Quality check**: Is the benefit SPECIFIC? "How to be happier at work" fails. "How to walk into Monday morning staff meetings feeling calm instead of nauseous" passes.

---

### Type 7: What NOT To Do

**What it needs**: A specific mistake. The reader must urgently need to know if they're making it.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| `structured-profile.json` → pain_and_fear | Failed attempts, what they tried that didn't work | "The #1 mistake people make when [situation] — and why it makes everything worse." |
| `copy-brief.md` | Objection Inventory | Flip each objection: what action leads to this objection being VALID? |
| `*_story-mining.md` — Category 4 | Failed Solutions (the graveyard) | Every failed solution IS a "what not to do" bullet |
| `slang-dictionary.md` | Direct Quotes — complaints about bad advice | "Why [common advice] is the worst thing you can do when [situation]." |

**Construction pattern**: `[The mistake] — and [the specific consequence]. (Most people do this [without knowing / at the worst moment].)`

**Quality check**: Would a significant portion of the market be making this mistake RIGHT NOW? If yes, it's a high-value bullet.

---

### Type 8: The Giveaway

**What it needs**: A COMPLETE tip, fact, or secret. No tease. Full disclosure. Proves you're not a charlatan.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| Proof elements that can be fully disclosed | A technique that's genuinely useful but not the whole system | State the full technique. "Here's exactly how to [X]: [step 1, step 2, step 3]." |
| `*_story-mining.md` — Category 8 | Insider knowledge | Full disclosure of insider information |
| `slang-dictionary.md` | Terms with concrete, teachable techniques | Give the full definition + application. No withholding. |

**Construction pattern**: `[Complete technique/secret] — here's exactly how it works: [disclosure].`

**Quality check**: Is the tip genuinely useful by itself? Can the reader take action on it immediately? If they'd still need to buy to use it, it's not a giveaway.

**Usage limit**: 1-2 per 100 bullets. Overuse destroys the mystery that makes other bullets work.

---

### Type 9: The 90% Solution

**What it needs**: State the WHAT clearly. Withhold the WHY or HOW. David Deutsch's method — bait, not the whole can.

**Data sources ranked by yield**:

| Source | Specific Field(s) | Extraction Method |
|---|---|---|
| Slang terms with hidden depth | Terms where the surface meaning is known but the MECHANISM is hidden | "Why [slang term] works — and the [surprising reason] most people get wrong." |
| Counterintuitive facts | Facts where the WHAT is clear but the WHY is surprising | "What [common advice] is doing to your [outcome]. (The reason has nothing to do with [what you'd expect].)" |
| Pain data with surprising causes | Pain points where the REAL cause is counterintuitive | "Why you [pain]. It's not because of [expected cause]. It's because of [hint at real cause]." |

**Construction pattern**: `[The what — clearly stated]. [The why/how — hinted at but withheld].`

**Quality check**: Does the reader need to buy to get the missing 10%? Is the withheld part genuinely valuable (not obvious)?

---

### Type 10: Dramatic Sub-Headline

**What it needs**: The last 6-8 words of a strong bullet, broken out into a bold, centered sub-headline that shatters monotony.

**Data sources**: Any strong bullet from Batches 1-6.

**Construction pattern**: Take a bullet. If its last 6-8 words are dramatic, isolate them:

```
"How to build genuine influence in your organization...
**WITHOUT KISSING A SINGLE BIT OF ASS!**"
```

**Usage**: 3-4 per 100-bullet list. Every 15-20 bullets.

---

### Type 11: Compressed Finale

**What it needs**: A lead-in bullet followed by a paragraph of 10-15 rapid short bullets separated by "...", ending with a dramatic sub-head.

**Data sources**: Quick scan of all remaining unused inventory items. Any compelling fact, benefit, or claim that didn't fit in previous batches.

**Construction pattern**:
```
"And a whole lot more, including...
[bullet 1]... [bullet 2]... [bullet 3]... [bullet 4]...
**DRAMATIC SUB-HEAD**
... [bullet 5]... [bullet 6]..."
```

**Usage**: Once, at the end. The overwhelming final push.

---

### Type 12: Expansion Bullets

**What it needs**: A high-value bullet picked from Batches 1-6, followed by 2-4 sentences of expansion ("Let's take a second to unpack this"), creating an editorial feel.

**Data sources**: Any bullet from Batches 1-6 that has enough depth to expand. Prioritize bullets that:
- Contain a named technique or concept
- Have historical or research depth
- Tell a micro-story within the expansion

**Construction pattern**:
```
[Original bullet]

Let's take a second to unpack this. [2-4 sentences of expansion — specific, detailed, credible].

[Transition back to bullets or dramatic sub-head]
```

**Usage**: Every 12-15 bullets. 5 maximum per 100-bullet list (token constraint — each expansion is 50-100 words).

---

## Data Source to Inventory Cross-Reference

When filling the Bullet Data Inventory (Step 3 of SKILL.md), here's exactly where to pull from:

| Inventory Section | `structured-profile.json` | `slang-dictionary.md` | `copy-brief.md` | `story-mining.md` |
|---|---|---|---|---|
| **Pain points** | `pain_and_fear.*`, `keeps_awake_at_night`, `anger_triggers`, `daily_frustrations`, `pain_emotional`, `pain_physical`, `pain_psychological` | Direct Quotes — complaints | Pain Point Bullets, Bar Complaint Monologue | — |
| **Slang terms** | — | ALL categories, every term with quotation marks | Slang & Vernacular Dictionary table | — |
| **Proof anchors** | `proof_elements` | — | Proof Elements Inventory | Cat 2 (Historical), Cat 5 (News), Cat 6 (Numbers) |
| **Desire statements** | `secret_fantasies`, `what_they_want_most` | Terms describing desired states | Desire Anchors | Cat 10 (Transformation) |
| **Enemy details** | `desires_and_aspirations.enemies` | Terms describing enemy behaviors | The Enemy, Competitive Positioning Map | Cat 9 (Enemy Exposed) |
| **Objections** | `objection_inventory[].objection` | — | Objection Inventory | — |
| **Mistakes/Failures** | Failed attempts, `bar_complaint_monologue` | Direct Quotes — bad advice complaints | — | Cat 4 (Failed Solutions) |
| **Counterintuitive facts** | — | Unusual slang entries | — | Cat 1 (Bizarre), Cat 8 (Insider Knowledge) |
