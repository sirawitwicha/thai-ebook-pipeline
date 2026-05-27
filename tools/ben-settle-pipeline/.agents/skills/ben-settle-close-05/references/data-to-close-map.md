# Data to Close Map — Which Research Feeds Which Component

Every close component pulls from specific data fields. If you cannot trace a guarantee, bonus, takeaway, or PS back to a specific piece of research data, delete it.

---

## Layer Overview

| Layer | Source | What It Feeds |
|---|---|---|
| **Layer 1: Continuity** | Headline + Opener + Story + Bullets | Voice, protagonist, emotional arc, narrative handoff point |
| **Layer 2: Core Research** | JSON + Slang + Copy Brief | Guarantee anchor, bonus topics, takeaway logic, PS material |
| **Layer 3: Story-Mining** | Enriched story scraping data | Bonus stories, PS stories, proof depth |
| **Layer 4: Close-Mining** | Enriched close scraping data | Deep objections, competitor pricing/guarantees, bonus demand signals, refund horror stories, takeaway validation |
| **Layer 5: Bullets** | Already-written bullets | Repurpose strongest bullets in PS, bonus descriptions |

---

## Connector (Bullets → Close)

| Input | Data Source | How to Use |
|---|---|---|
| Last bullet batch type | `*_bullets.md` — final batch written (usually Compressed Finale) | The connector picks up where bullets left off |
| Primary hook | `copy-brief.md` → Primary Hook | Reference implicitly in connector |
| Emotional arc completion | `structured-profile.json` → emotional_drivers.desired_feeling_on_arrival | The connector should feel like arriving at the solution |
| Story's bridge section | `*_story.md` → Section 7 (The Bridge) | Often the story's bridge IS the connector — or a variant of it |

---

## Component 1: Guarantee

### Data Sources

| What You Need | Where to Find It | Specific Field |
|---|---|---|
| Top objection to neutralize | `copy-brief.md` → Objection Inventory | Each objection IS a guarantee prompt |
| **DEEP objections (10+)** | `*_close-mining.md` → Category 1 | Verbatim buyer reluctance language from reviews/Reddit |
| **Refund horror stories** | `*_close-mining.md` → Category 5 | Exact details of how the market was burned by guarantees |
| Competitor guarantees | `copy-brief.md` → Competitive Positioning Map | What they offer → you offer more/better |
| **Competitor guarantee details** | `*_close-mining.md` → Category 2 | Competitor sales page guarantee language verbatim |
| Risk tolerance of market | `structured-profile.json` → pain_and_fear.insecurities | High insecurity → stronger guarantee needed |
| What they've been burned by | `slang-dictionary.md` → Direct Quotes | Look for complaints about being ripped off, "scam," "didn't work" |
| Product type feasibility | `structured-profile.json` → what_they_want_most | Digital product → easy refund. Service → satisfaction guarantee. Physical → return policy |

### Extraction Method

```
1. List every objection from copy-brief Objection Inventory
2. For each objection, ask: "What guarantee would make this objection irrelevant?"
3. List competitor guarantees from Competitive Positioning Map
4. Ask: "What can we guarantee that they CAN'T?"
5. Check slang dictionary Direct Quotes for "scam," "rip-off," "waste," "didn't work"
6. These phrases ARE your guarantee's emotional target
```

### Decision Tree

```
Is this a cold prospect (mass market)?
  YES → Use a guarantee. Level 2-3.
  NO → Is this your own warm list?
    YES → Burn the Boats (no guarantee) is viable. Ask user.
    NO → Use Level 1-2 guarantee.

Does the market show signs of being burned before?
  YES (slang has "scam," "rip-off," "didn't work") → Level 3-4 guarantee
  NO → Level 1-2 is sufficient

Is there a competitor with a famous guarantee?
  YES → Beat it. Be more dramatic, longer, more generous.
  NO → Create the category-standard guarantee.
```

---

## Component 2: Bonuses

### Data Sources

| What You Need | Where to Find It | Specific Field |
|---|---|---|
| Secret fantasies | `structured-profile.json` → desires_and_aspirations.secret_fantasies | Each fantasy IS a bonus topic |
| **Bonus demand signals** | `*_close-mining.md` → Category 4 | Exact "I wish someone would..." / "does anyone have a template for..." quotes |
| Desire anchors | `copy-brief.md` → Desire Anchors | Each anchor IS a bonus topic |
| Urgent crisis resolution | `structured-profile.json` → pain_and_fear.urgent_crisis | "Quick win" bonus |
| Slang terms for bonus names | `slang-dictionary.md` → ALL categories | Every slang term is a potential bonus NAME |
| Bar complaint monologue | `copy-brief.md` → Bar Complaint Monologue | Unexpressed desires hiding in complaints |
| What they want most | `structured-profile.json` → desires_and_aspirations.what_they_want_most | Core bonus anchor |
| What they're afraid to ask for | `structured-profile.json` → pain_and_fear.insecurities | "Secret" bonus |

### Bonus Naming Formula

```
[Slang Term] + [Benefit/Outcome]
"The [Slang] [System/Protocol/Method/Playbook/Checklist]"

Examples from dark-psychology research:
"The Grey Rock Protocol" (slang: "grey rock")
"The Sunday Scaries Elimination System" (slang: "Sunday Scaries")
"The Flying Monkey Disarming Playbook" (slang: "flying monkeys")
"The Credit Thief Trap" (slang: "credit theft")
```

### Bonus Value Anchoring

Every bonus needs a verifiable value anchor. Pull from:
- `story-mining` → if this bonus content sold elsewhere, cite the price
- `competitive_intelligence` → if competitors charge for similar, cite their price
- `proof_elements` → if the bonus contains documented research, cite the source's authority

### Extraction Method

```
1. List every secret_fantasy → each gets a bonus
2. List every desire_anchor → each gets a bonus
3. Scan slang dictionary for vivid, market-specific terms → these are bonus NAMES
4. For each bonus, ask: "Would someone buy the product JUST to get this bonus?"
   YES → This is a hot bonus. Give it a story or bullets.
   NO → Still include it, but don't lead with it.
5. Prioritize: hot bonuses first, then supporting bonuses
```

---

## Component 3: The Takeaway

### Data Sources

| What You Need | Where to Find It | Specific Field |
|---|---|---|
| Who should NOT buy | `copy-brief.md` → Objection Inventory | Flip each objection: who would MAKE this objection valid? |
| **Verified mismatch reasons** | `*_close-mining.md` → Category 6 | Real reviews saying "this wasn't for me because [legit reason]" |
| The enemy's traits | `copy-brief.md` → The Enemy | The enemy's traits = the type of person we DON'T want as a customer |
| Primary buyer description | `structured-profile.json` → primary_buyer_description | The OPPOSITE of this person = who to exclude |
| Pain data — lazy/unmotivated | `structured-profile.json` → pain_and_fear | "People who just want to complain but won't take action" |
| Bad-fit signals | `slang-dictionary.md` → Direct Quotes | Look for complaints from people who wouldn't be good customers |
| Product limitations | `story-mining` → Failed Solutions (Cat 4) | What has failed for others — people who want that shouldn't buy |

### Takeaway Construction Formula

```
"If you're the type who [bad-fit behavior from research], then [product] is NOT for you. [Genuine reason why]. You're better off [alternative — shows you care about their outcome, not just their money]."

"But if you're [ideal buyer description from research], and you're ready to [action they need to take], then [product] was made for you."
```

### Extraction Method

```
1. Read primary_buyer_description. Define the OPPOSITE of this person.
2. Read objection_inventory. For each objection, ask: "What type of buyer would make this objection LEGITIMATE?"
3. Read bar_complaint_monologue. Look for mentions of "lazy coworkers," "people who don't get it," etc.
4. List 3-5 genuine bad-fit buyer types.
5. For each, write WHY they're a bad fit (must be TRUE, not manufactured).
```

### Authenticity Check

After writing a takeaway, ask:
- Is this actually true about the product?
- Would I tell a real person this to their face?
- Am I excluding people for their benefit, or for manipulation?
- Does this match the tone of the rest of the copy?

If any answer is wrong, rewrite. "It can't be 'Ben told me to do the takeaway so I'm going to use it.'"

---

## Component 4: The Almighty PS

### Data Sources

| What You Need | Where to Find It | Specific Field |
|---|---|---|
| Testimonials | `copy-brief.md` → Proof Elements | Any named person who endorsed or benefited |
| **Competitor pricing for anchoring** | `*_close-mining.md` → Category 3 | "Competitors charge $X for half this information" |
| Bonus story material | `story-mining` → Category 1 (Bizarre), Category 10 (Transformation) | Micro-story for PS |
| Deadline angle | `copy-brief.md` → urgency signals in pain_and_fear | What makes the offer time-sensitive |
| Strong bullets to repurpose | `*_bullets.md` → scan all types | A single great bullet expanded into PS mini-story |
| Takeaway reinforcement | Takeaway Component (from this skill) | Restate key takeaway with new framing |
| Historical/proof depth | `story-mining` → Category 2 (Historical), Category 6 (Numbers) | "This isn't new — [historical figure] wrote about this in [year]..." |
| **Refund complaint language** | `*_close-mining.md` → Category 5 | "Unlike those guarantees where [specific complaint]..." |

### PS Type Decision Matrix

| If You Have... | Best PS Type |
|---|---|
| A strong testimonial | Testimonial PS |
| A hot bonus that deserves its own story | Bonus Story PS |
| A genuine exclusion reason | Takeaway PS |
| A deadline that needs reinforcement | Deadline PS |
| A bullet that's almost too good for the bullet section | Bullet-Expansion PS |
| Multiple of the above | Multiple PS's (2-4) |

### PS Construction Formulas

**Testimonial PS**:
```
P.S. [Name], a [role/credential], [did/bought/used product] and wrote me this:
"[verbatim or slightly edited testimonial]"
```

**Bonus Story PS** (Settle's pattern):
```
P.S. One more thing: [1-2 sentence setup about the bonus's origin or value]. [What's in it]. [Why it's valuable]. [What it's worth]. And [how to get it — order by deadline].
```

**Takeaway PS** (Settle's pattern):
```
P.S. There is one "downside" to [product]: [genuine limitation]. Why? [honest reason]. That's why if you're [bad-fit type]... Then Please Do NOT Order! [Product] is for [ideal buyer]. [Close with benefit to ideal buyer].
```

**Deadline PS**:
```
P.S. [Deadline statement — clear, urgent, no hedging]. [Consequence of missing it]. [Action to take now].
```

---

## The Deadline — Cross-Cutting Requirement

Every close must include a deadline. Pull from:

| What You Need | Where to Find It | How to Use |
|---|---|---|
| Natural urgency | `structured-profile.json` → urgent_crisis | "This problem gets worse every day you don't solve it" |
| Launch/beta window | User-provided | "Launch price expires [date]" |
| Bonus scarcity | Bonus component | "The [hot bonus] is only available if you order by [date]" |
| Market-driven urgency | `copy-brief.md` → competitive_intelligence | "The people outmaneuvering you right now are counting on you never learning this" |

---

## Full Close Assembly Map

| Close Section | Primary Layer | Specific Sources |
|---|---|---|
| Connector | Layer 1 + Layer 2 | Story's Bridge section + Primary Hook + Desired Feeling |
| Guarantee | Layer 2 + Layer 4 | Objection Inventory + Competitive Positioning + Insecurities + Close-Mining Cat 1 (deep objections) + Cat 5 (refund horror stories) |
| Bonuses | Layer 2 + Layer 3 + Layer 4 | Secret Fantasies + Desire Anchors + Slang Terms + Story-Mining Cat 10 + Close-Mining Cat 4 (bonus demand signals) |
| Takeaway | Layer 2 + Layer 4 | Primary Buyer Description (inverted) + Objection Inventory + The Enemy + Close-Mining Cat 6 (verified mismatch reasons) |
| PS #1 (Testimonial) | Layer 2 + Layer 3 | Proof Elements + Story-Mining Cat 3 |
| PS #2 (Bonus Story) | Layer 3 + Layer 4 | Story-Mining Cat 1, 2, 7, 10 + Close-Mining Cat 4 |
| PS #3 (Deadline/Takeaway) | Layer 2 + Layer 4 | Urgent Crisis + Takeaway Component + Close-Mining Cat 5 (refund language) |
| CTA | Layer 1 | Narrative Voice + Tone Calibration |
| Price Anchoring | Layer 4 | Close-Mining Cat 3 (price perception data) + Cat 2 (competitor prices) |
