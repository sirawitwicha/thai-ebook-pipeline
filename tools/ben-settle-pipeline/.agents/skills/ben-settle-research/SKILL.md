---
name: ben-settle-research
description: Automated market research pipeline for copywriting. Use when the user wants to research a niche/market for copywriting, write a sales letter, create a customer avatar, find voice-of-customer data, discover market pain points and desires, do competitive copywriting analysis, or perform "Criminally Profitable Research" on any target audience. Triggers on: "research my market", "copywriting research", "customer avatar", "voice of customer", "market pain points", "Ben Settle research", "sales copy research", "who is my audience", "what does my market want", "write sales letter for", "what keeps them awake at night", "buyer psychology research".
---

# Ben Settle "Criminally Profitable Research" Pipeline

Automated market research that crawls inside your prospect's psychology. Based on Ben Settle's *Copy Slacker* methodology: 45 questions answered through scraping, observation, and synthesis — not surveys asking people what they *say* they want, but analyzing what they actually *buy, say, and do* in public.

**Core insight**: "It's not about the weedkiller. It's about the crab grass." — Research the market, not the product. When you know the market well enough, you can write most of the sales copy without even seeing the product.

## Prerequisites

- Apify MCP server connected (`actors-mcp-server`) — used for all scraping
- The `apify-ultimate-scraper` skill installed — read its `references/actor-index.md` for available Actors

## When the user asks for research

Confirm three things before starting:
1. **The niche/topic** — be specific (e.g., "golf swing aids for seniors" not "golf")
2. **Competitor URLs or product names** (optional but helpful)
3. **Scope** — quick scan (~$2-3) or deep dive (~$5-8)

Then execute the pipeline below.

**Data reuse**: Before scraping, check if the project folder already has existing research files. Data persists on disk — if a previous run completed successfully, ask: "I found existing research data for [niche]. Use it, or re-scrape fresh?" If the user wants to add story-mining data on top of existing research, run Phase 0. Otherwise, skip to Phase 1.

---

## Phase 0 (Optional): Story-Mining — Enriched Data for Storytelling

**Goal**: Gather the specific, vivid details that make Settle-style stories feel real — bizarre facts, historical depth, personal transformation accounts, insider confessions, documented news events, and numerical proof. This data is used by `ben-settle-story-03` and can be scraped once and reused across all copywriting outputs.

**When to run**: When the user anticipates writing a sales story, or when they want richer detail beyond the core research. Ask the user: "Should I add story-mining? It scrapes additional data specifically for storytelling — bizarre facts, historical background, personal transformation stories, insider secrets. Adds ~$1-3 and 2-3 minutes."

**If user says yes**: Read the story-mining query strategy from the `ben-settle-story-03` skill at `../ben-settle-story-03/references/story-mining-queries.md`. Select the 3-5 categories most relevant to the niche. Run the queries. Save all results to `research-outputs/<niche-slug>/YYYY-MM-DD_story-mining.md`. This file becomes a persistent asset — future skills (headlines, openers, stories, bullets, closes) can all draw from it.

**If user says no**: Skip. The core pipeline still produces excellent research for headlines and openers.

**If story-mining data already exists** (from a previous run): Ask "Story-mining data already exists for this niche. Use it or re-scrape?"

---

## Phase 1: Social Listening — Voice of Customer

**Goal**: Harvest the market's exact language, pain, fears, desires, slang, and complaints from where they talk honestly.

Read `references/actor-mapping.md` for exact MCP tool calls and parameters.

### 1a. Reddit (highest signal)
Search relevant subreddits for discussions. Reddit is the closest digital equivalent to the forums Ben Settle calls "the single most powerful research tool."

Use `mcp__actors-mcp-server__call-actor` with:
- actor: `trudax/reddit-scraper-lite`
- input: searches for the niche topic, `searchPosts: true`, `searchComments: true`, `maxItems: 100`, `maxComments: 50`, `sort: "relevance"`, `time: "year"`

Fetch results via `mcp__actors-mcp-server__get-dataset-items`.

### 1b. YouTube Comments
Search for niche videos, then scrape comments on the top ones.

- First: `streamers/youtube-scraper` — `searchTerms` for niche, `maxResults: 30`
- Then: `streamers/youtube-comments-scraper` — on top 5-10 video URLs extracted, `maxComments: 50`

### 1c. Facebook Groups (if niche has active FB community)
`apify/facebook-groups-scraper` or `apify/facebook-posts-scraper` for public group content.
Skip if niche is primarily B2B or doesn't congregate on Facebook.

---

## Phase 2: Competitive Intelligence

**Goal**: Map the competitor landscape — what's being sold, what claims are made, what holes exist.

### 2a. Google SERP
`apify/google-search-scraper` with 5-8 queries covering:
- `"best [niche] books"` / `"best [niche] courses"`
- `"[niche problem] solution"`
- `"[niche] reviews"`
- `"[niche] vs"`
- `"how to [solve niche problem]"`

Set `maxPagesPerQuery: 1`, `countryCode: "us"`.

### 2b. Competitor Page Extraction
Feed top search results into `apify/rag-web-browser` (FREE) to extract clean markdown from:
- Competitor sales pages / landing pages
- Amazon product pages for top-selling books in niche
- Review pages

This Actor is optimized for single-URL retrieval with clean markdown output.

### 2c. Competitor Reviews (if relevant)
If competitors have Google Maps business pages: `compass/Google-Maps-Reviews-Scraper`
If competitors are on Yelp: `tri_angle/yelp-review-scraper`

Mine 1-3 star reviews especially — these reveal what competitors fail to deliver (your opportunity).

### 2d. Facebook Ads (optional)
`apify/facebook-ads-scraper` — search for competitor brand names to see their active ad creatives and positioning.

---

## Phase 3: Trend & Demand Validation

**Goal**: Confirm the market is alive and understand what's trending.

### 3a. Google Trends
`apify/google-trends-scraper` with 3-5 search terms including:
- Core niche term
- Problem-oriented terms
- Competitor brand names

### 3b. TikTok Trends (if niche skews younger)
`clockworks/tiktok-trends-scraper` or `clockworks/tiktok-hashtag-scraper`

### 3c. LinkedIn (B2B niches only)
`harvestapi/linkedin-profile-posts` — search for niche-related posts to understand professional discourse.

---

## Phase 4: LLM Synthesis — CHUNKED

After all scraped data is collected, synthesize in **6 chunks** (not one massive prompt). This prevents context overload and produces better results.

Read `references/synthesis-prompt.md` for the exact prompts to use for each chunk. The chunks are:

| Chunk | Category | Questions |
|---|---|---|
| 1 | Pain & Fear Profile | Q1-8, Q11, Q15, Q24 |
| 2 | Identity & Worldview | Q9-10, Q13-14, Q17-26, Q32, Q41 |
| 3 | Desires & Aspirations | Q12, Q16, Q31, Q37-39 |
| 4 | Media & Culture | Q34-36, Q44 |
| 5 | Competitive Intelligence | Q28, Q33, Q42, Q43, Q45 |
| 6 | Emotional & Decision Drivers | Q29-30, Q40 |

For each chunk:
1. Feed the relevant scraped data subset + the chunk's synthesis prompt
2. Collect the chunk's output
3. Feed the next chunk (each chunk is independent, so they can run in parallel if the model supports it)

Chunk outputs are building toward the final composite.

---

## Phase 5: Final Assembly

After all 6 chunks are complete, run the **Final Assembly** prompt from `references/synthesis-prompt.md` to produce two output files:

### Output 1: `research-outputs/<niche-slug>/YYYY-MM-DD_structured-profile.json`
A structured JSON combining all chunks into a single "Composite Customer" profile per `references/output-schemas.md`.

### Output 2: `research-outputs/<niche-slug>/YYYY-MM-DD_copy-brief.md`
A freeform copywriting brief containing:
- **Headline starters** (5-10 options derived from pain/fear/desire discoveries)
- **Primary hook** (the #1 emotional angle)
- **Pain point bullets** (top 10, in market's exact language)
- **The Enemy** (who/what the market blames — to rail against)
- **Desire anchors** (what they secretly fantasize about)
- **Slang & vernacular dictionary** (to write like an insider)
- **Proof elements** (credibility markers that matter to this market)
- **Objection inventory** (what stops them from buying)
- **Tone calibration** (education level, reading level, emotional register)
- **Competitor positioning map** (what's already being said, and the gap)

---

## Cost awareness

Before running, estimate and inform the user:

| Phase | Approx. cost (FREE tier) |
|---|---|
| Phase 1 (Reddit + YouTube) | ~$0.80-1.20 |
| Phase 2 (SERP + competitor pages) | ~$0.03-0.10 |
| Phase 3 (Trends + optional) | ~$0.01-0.20 |
| **Total per research run** | **~$1-3** |

Apify has a $5 minimum top-up. One top-up covers 2-4 research runs.

## Reference files

- `references/45-questions.md` — The full Ben Settle methodology with context on WHY each question matters
- `references/actor-mapping.md` — Exact MCP tool calls and parameters for each data source
- `references/synthesis-prompt.md` — Chunked LLM prompts for Phase 4 and Final Assembly
- `references/output-schemas.md` — JSON schema and copy brief template for Phase 5
