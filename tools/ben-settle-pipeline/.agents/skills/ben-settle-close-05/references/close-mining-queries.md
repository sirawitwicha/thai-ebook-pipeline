# Close-Mining Query Strategy — 6 Categories

Optional data enrichment for the close skill. Run these queries when the existing research data lacks the buying-decision intelligence needed for guarantees, bonuses, takeaway logic, and PS material. This data persists on disk — scrape once, reuse if the close is regenerated.

**When to scrape**: The objection inventory has fewer than 10 entries, competitor pricing/guarantees are unknown, there's no bonus demand signal data, or the takeaway reasons feel manufactured rather than data-backed.

**When to skip**: The core research files already contain rich objection data (10+ with neutralization strategies), competitor intelligence includes their pricing and guarantees, and the slang dictionary has enough "I wish someone would..." type quotes to fuel bonus creation.

**What makes this different from research and story-mining**: Research scraped for PAIN and IDENTITY. Story-mining scraped for NARRATIVE and HISTORY. Close-mining scrapes for BUYING DECISIONS — objections, price sensitivity, competitor offers, refund experiences, and bonus wishlists. Different questions asked of the same or similar sources.

**Actor convention**: Use `mcp__actors-mcp-server__call-actor` for Google SERP, Reddit, YouTube, and Amazon. Use WebFetch via Bash for individual competitor pages. The `apify/rag-web-browser` dedicated tool is fast for single-URL fetches.

---

## Category 1: Objection Mining — The "I'm Not Buying Because..."

**What this yields**: Deep objections beyond the surface 7. The real reasons people hesitate, refuse, or regret buying in this niche. Amazon 1-2 star reviews are the single richest source — people write ESSAYS about why a book/course disappointed them. Reddit "should I buy" threads capture the pre-purchase internal debate verbatim.

**Why the close needs this**: Each objection IS a guarantee prompt. "This sounds manipulative" → defensive framing guarantee. "I've been burned before" → cash-back guarantee. "It won't work for MY situation" → universal applicability guarantee. Without deep objections, guarantees are generic.

| Query | Actor | What to Extract |
|---|---|---|
| `site:amazon.com "[competitor book] reviews"` | `apify/rag-web-browser` → WebFetch | 1-2 star reviews — the EXACT language of disappointment |
| `"[competitor book] was a waste of money"` | Google SERP, Reddit | Buyer's remorse language |
| `"should I buy [niche product] reddit"` | `apify/rag-web-browser` | Pre-purchase hesitation, price objections, comparison shopping |
| `"is [competitor book] worth it reddit"` | `apify/rag-web-browser` | Value skepticism, "you can get this free on YouTube" objections |
| `"[niche] book wasn't what I expected"` | Google SERP, Reddit | Expectation mismatch — what they wanted vs what they got |
| `"don't buy [competitor product]"` | Google SERP, Reddit, YouTube | Warning posts — the most emotionally charged objections |
| `"I regret buying [niche product]"` | Reddit, Google SERP | Post-purchase regret language — buyer's exact words |

**Extraction targets**: 15-25 verbatim objections, each noted with source. Prioritize objections that are SPECIFIC (not "it was bad" but "it spent 200 pages on theory and never once told me what to say in a meeting").

**Settle principle**: The market's own skepticism = your most credible close element. When they see their exact objection in your guarantee, they think "oh, he knows what I'm worried about."

---

## Category 2: Competitor Offer Intelligence

**What this yields**: What competitors charge, what they guarantee, what bonuses they offer, how they structure their close. This is your competitive baseline — you must BEAT it or be dramatically DIFFERENT.

**Why the close needs this**: If every competitor offers a 30-day guarantee, a 30-day guarantee is invisible. If every competitor charges $9.99 for an ebook, a $9.99 price point is commodity. You need to know what the market already sees to make YOUR close stand out.

| Query | Actor | What to Extract |
|---|---|---|
| Competitor sales pages (direct URLs) | WebFetch via Bash / `apify/rag-web-browser` | Guarantee language, bonus structure, price, CTA |
| `"[competitor] money-back guarantee"` | Google SERP | Competitor guarantee terms |
| `"[competitor] course price"` or `"[competitor] book price"` | Google SERP | Price points across the market |
| `"best [niche] books"` → Amazon page | `apify/rag-web-browser` → WebFetch | Top competitor prices, review counts, formats |
| `"[niche] course"` → Udemy / Teachable landing pages | Google SERP → WebFetch | Course pricing, guarantee badges, bonus lists |
| Competitor YouTube descriptions | YouTube scraper | Free lead magnets, tripwire offers, pricing tiers |

**Extraction targets**: For each competitor: price, guarantee terms, bonus count/names, format, CTA language. Build a comparison table.

**How to avoid similarity**: Don't scrape the same competitor content pages you already scraped in research. Focus on their SALES pages, checkout pages, and "buy now" pages — not their blog posts or about pages. The research phase scraped their CONTENT. This phase scrapes their OFFER.

---

## Category 3: Price Anchoring & Value Perception

**What this yields**: What the market expects to pay. What feels "too expensive" vs "a steal." The price range that makes your offer feel like house odds.

**Why the close needs this**: You can't write "this is a steal at $X" without knowing what the market considers a steal. You can't write "competitors charge $Y for less" without knowing what competitors actually charge. Price anchoring makes the offer feel inevitable.

| Query | Actor | What to Extract |
|---|---|---|
| `"how much does [niche] coaching cost"` | Google SERP | High-end price anchors |
| `"is [competitor product] worth [price]"` | Reddit, Google | Price-value perception |
| `"[niche] course worth [price] reddit"` | Reddit | Value debate — "worth it at $X but not $Y" |
| `"cheap vs expensive [niche] [book/course]"` | Reddit, Quora | Price tier perception |
| `"how much should I pay for [niche solution]"` | Reddit, Quora | Direct price expectation data |
| `"cost of [niche problem] per year"` | Google SERP | Cost-of-inaction anchor — what staying stuck costs |
| `"average [niche] [book/course] price"` | Google SERP | Market price baseline |

**Extraction targets**: A price range map: "too cheap to trust" → "impulse buy" → "considered purchase" → "premium" → "too expensive." Plus specific competitor prices for anchoring.

**Settle principle**: The product price should feel like house odds compared to what staying stuck costs. One promotion pays for the book 100x over. That math needs real numbers.

---

## Category 4: Bonus Demand Signals — "I Wish Someone Would Just..."

**What this yields**: Exact things the market is ASKING for that don't exist yet. These are bonuses the market has already pre-sold itself on — you just need to create them and name them in their language.

**Why the close needs this**: Bonuses pulled from desire data are good. Bonuses pulled from "I wish someone would give me a template for..." are GREAT. The market literally told you what to include as a bonus. You're not guessing.

| Query | Actor | What to Extract |
|---|---|---|
| `"does anyone have a template for [niche task]"` | Reddit | Direct bonus requests |
| `"I wish there was a [niche tool/checklist]"` | Reddit, Google | Unexpressed bonus ideas |
| `"can someone just tell me what to say when [niche situation]"` | Reddit, Quora | Script/template bonuses |
| `"looking for [niche] spreadsheet/tracker"` | Reddit | Tool bonuses |
| `"anyone have examples of [niche situation]"` | Reddit | Case study / swipe file bonuses |
| `"where can I find [niche resource]"` | Reddit, Google | Resource gap — you fill it as a bonus |
| `"[niche] [checklist/template/script] reddit"` | `apify/rag-web-browser` | Bonus format validation — what formats they actually want |
| YouTube comments on competitor videos: "can you give an example" | YouTube Comments scraper | Specific "show me" requests — each is a bonus idea |

**Extraction targets**: 5-10 specific bonus ideas the market is asking for, with the exact language they used to ask for it. Bonus naming should use THEIR words.

**Settle principle**: "Pick bonuses touching strong emotional hot buttons. Think of hot impulse-buy type bonuses that scratch a burning itch." When the bonus is something they've LITERALLY ASKED FOR, the impulse is built in.

---

## Category 5: Guarantee & Refund Horror Stories

**What this yields**: How the market has been burned by guarantees. The refund horror stories. The "their guarantee is worthless because..." complaints. This tells you exactly what your guarantee must overcome.

**Why the close needs this**: A guarantee that matches generic fears is fine. A guarantee that specifically addresses "I tried to refund a digital product and they made me jump through 47 hoops" is devastating. You're writing the guarantee they WISH their last purchase had.

| Query | Actor | What to Extract |
|---|---|---|
| `"tried to get a refund on [niche product]"` | Reddit, Google | Refund friction horror stories |
| `"money-back guarantee is a scam"` | Reddit, Google | Guarantee skepticism |
| `"they refused to refund my [niche purchase]"` | Reddit | Broken promises |
| `"beware of [niche] guarantee"` | Reddit, Google | Specific guarantee complaints |
| `"digital product refund nightmare"` | Reddit, Google | Cross-niche refund trauma |
| `"their guarantee said [X] but when I tried"` | Reddit | Guarantee vs reality gap |

**Extraction targets**: 5-10 specific guarantee complaints. What EXACTLY went wrong: hoops to jump through, time limits that were too short, "you didn't follow the system" excuses, hidden conditions.

**Settle principle**: "Make it as generous and dramatic as possible." Knowing what the market's been burned by tells you where to be dramatic. "No questions asked" hits harder when they've been interrogated for refunds before.

---

## Category 6: Takeaway Validation

**What this yields**: Real, verified reasons people were NOT a fit for the product. Reviews and comments where people say "this wasn't for me because..." — honestly, not angrily. This validates that your takeaway is genuine, not manufactured.

**Why the close needs this**: A takeaway that sounds made-up ("don't buy if you're not SERIOUS about success") is worse than no takeaway at all. A takeaway backed by actual review data ("as one reader said, 'I work at a 3-person startup so the corporate dynamics didn't apply to me'") is credible and ethical.

| Query | Actor | What to Extract |
|---|---|---|
| `"[competitor book] wasn't for me because"` | Amazon reviews, Reddit | Honest mismatch reasons |
| `"[niche product] only applies if"` | Reddit, Google | Scope limitations people noticed |
| `"who is [niche product] actually for"` | Reddit, Quora | Audience fit discussion |
| `"[competitor book] is too [advanced/basic/theoretical]"` | Amazon reviews, Reddit | Level mismatch complaints |
| `3 star reviews of [competitor product]` | Amazon → WebFetch | Nuanced "good but not for me" reviews |
| `"this book assumes you work in [industry/situation]"` | Amazon reviews | Scope assumptions |

**Extraction targets**: 5-10 genuine mismatch reasons. These become the TAKEAWAY: real reasons, from real buyers, that the product isn't right for everyone.

**Settle principle**: "It can't be 'Ben told me to do the takeaway so I'm going to use it.'" The takeaway must be rooted in honesty. These real mismatch reasons ARE that honesty.

---

## Execution Protocol

### Step 1: Gap Assessment
Before running queries, assess what's already in the research files:
- Objection count: If 10+ with neutralization strategies → skip Category 1
- Competitor pricing known: If prices are in competitive positioning → skip Categories 2-3
- Bonus ideas: If 5+ specific "I wish" quotes exist in slang dictionary → skip Category 4
- Guarantee complaints: If research has refund horror stories → skip Category 5
- Takeaway data: If buyer description clearly defines who's excluded → skip Category 6

Only scrape categories where gaps exist.

### Step 2: Prioritized Execution
Run the highest-value categories first. Category 1 (Objections) and Category 4 (Bonus Demand Signals) almost always deliver the most ROI for close quality.

### Step 3: Save and Trace
Save results to `research-outputs/<niche-slug>/YYYY-MM-DD_close-mining.md`. Every extracted piece of data must include its source URL so the close can trace back.

```markdown
# Close-Mining Data: [NICHE]
**Generated**: YYYY-MM-DD
**Categories run**: [list which of the 6]

## Category 1: Objection Mining
[Verbatim objections with source URLs]

## Category 2: Competitor Offer Intelligence
[Competitor prices, guarantees, bonuses with source URLs]
...
```

### Step 4: Feed Into Close Brief
After scraping, return to the skill's Step 3 (Close Brief) and fill Sections C-F with the enriched data. Then proceed with writing.

---

## Cost Estimate

Close-mining typically runs 3-5 Apify actors + 5-10 WebFetches. Estimated cost: $0.30-0.80 USD. Runtime: 2-4 minutes for the full protocol. Running only Category 1 + 4 (highest ROI) takes ~1-2 minutes and $0.15-0.40.
