# Actor Mapping: Data Sources → Apify MCP Actors

Each section maps a research need to the specific MCP tool call. All calls use `mcp__actors-mcp-server__call-actor` to start the Actor and `mcp__actors-mcp-server__get-dataset-items` to fetch results.

## Cost Tracking

All prices are Apify FREE tier. With proxy traffic, budget 1.5-2x the listed amounts.

---

## Phase 1a: Reddit (Voice of Customer Gold)

**Actor**: `trudax/reddit-scraper-lite`
**Pricing**: $0.004/result + $0.02 start

```json
{
  "actor": "trudax/reddit-scraper-lite",
  "input": {
    "searches": ["REPLACE_WITH_NICHE_KEYWORDS"],
    "searchPosts": true,
    "searchComments": true,
    "maxItems": 100,
    "maxComments": 50,
    "maxPostCount": 50,
    "sort": "relevance",
    "time": "year",
    "includeNSFW": false,
    "skipComments": false,
    "proxy": {
      "useApifyProxy": true,
      "apifyProxyGroups": ["RESIDENTIAL"]
    }
  },
  "waitSecs": 45
}
```

**Keywords strategy**: Use 3-5 searches from different angles:
- `"[niche] advice"` — people seeking help
- `"[niche] sucks"` or `"[niche] regret"` — pain/frustration
- `"[niche] vs [alternative]"` — comparison language
- `"anyone else [niche problem]"` — shared experience
- `"best [niche] 2024"` or `"best [niche] 2025"` — buying intent

**Why this Actor**: Reddit's anonymity produces the kind of honesty Ben Settle talks about — people say things they'd never tell their spouse. The exact phrasing, stories, and complaints are copywriting gold.

---

## Phase 1b: YouTube Voice of Customer

### Step 1 — Find Videos

**Actor**: `streamers/youtube-scraper`
**Pricing**: $0.004/video
**CRITICAL**: The parameter is `searchQueries` (NOT `searchTerms`).

```json
{
  "actor": "streamers/youtube-scraper",
  "input": {
    "searchQueries": "REPLACE_WITH_NICHE_KEYWORDS",
    "maxResults": 30,
    "sort": "relevance"
  },
  "waitSecs": 30
}
```

### Step 2 — Scrape Comments (HIGHEST SIGNAL SOURCE)

**Actor**: `streamers/youtube-comments-scraper`
**Pricing**: $0.002/comment
**CRITICAL**: The parameter is `startUrls` as an array of objects with `url` property (NOT `videoUrls` as plain strings). Scrape ALL videos with comments > 0, not just top 5-10. YouTube comments are consistently the single highest-signal voice-of-customer source across all niches tested.

```json
{
  "actor": "streamers/youtube-comments-scraper",
  "input": {
    "startUrls": [
      {"url": "REPLACE_WITH_VIDEO_URL_1"},
      {"url": "REPLACE_WITH_VIDEO_URL_2"}
    ],
    "maxComments": 50,
    "sortCommentsBy": "TOP_COMMENTS"
  },
  "waitSecs": 45
}
```

**Why these Actors**: YouTube comments are raw, unfiltered audience reaction. People explain their problems, argue with each other, and use their natural vocabulary — exactly what you need for Q32 (slang) and Q40 (how they complain). This is consistently the highest-signal data source in the pipeline. Comments from videos with 100K+ views regularly contain full paragraphs of exact prospect language — fears, frustrations, desires, and slang — written in their natural voice. **Prioritize this above all other Phase 1 sources.**

---

## Phase 1c: Facebook Groups (Optional)

**Actor**: `apify/facebook-posts-scraper`
**Pricing**: Apify-maintained, fixed cost

```json
{
  "actor": "apify/facebook-posts-scraper",
  "input": {
    "startUrls": ["REPLACE_WITH_GROUP_OR_PAGE_URLS"],
    "maxPosts": 50,
    "maxComments": 30
  },
  "waitSecs": 30
}
```

Skip if niche has weak Facebook presence. B2B niches should use LinkedIn instead.

---

## Phase 2a: Google SERP (Competitor Mapping)

**Actor**: `apify/google-search-scraper`
**Pricing**: $0.0045/page + $0.001 start

```json
{
  "actor": "apify/google-search-scraper",
  "input": {
    "queries": "REPLACE_WITH_SEARCH_QUERIES",
    "maxPagesPerQuery": 1,
    "countryCode": "us",
    "searchLanguage": "en"
  },
  "waitSecs": 30
}
```

**Query strategy** (one per line in the `queries` string):
```
best [niche] books
best [niche] courses
[niche] reviews
[niche] vs
how to [solve niche problem]
[niche] success stories
why [niche] doesn't work
[niche] scam or legit
```

Extract URLs from `organicResults[]` for Phase 2b.

---

## Phase 2b: Competitor Page Extraction

**Primary approach**: Use the built-in `WebFetch` tool (FREE, no memory limits) to extract content from top competitor URLs found in Phase 2a.

```
WebFetch(url: "COMPETITOR_URL", prompt: "Extract all key claims, benefits, emotional language, and target audience signals")
```

**Alternative — RAG Web Browser** (Apify Actor, FREE but requires 8GB memory — available on Starter plan and above):
```json
{
  "actor": "apify/rag-web-browser",
  "input": {
    "query": "REPLACE_WITH_URL",
    "maxResults": 1,
    "outputFormats": ["markdown"]
  },
  "waitSecs": 45
}
```

**Alternative — Website Content Crawler** (Apify Actor, FREE, lower memory):
```json
{
  "actor": "apify/website-content-crawler",
  "input": {
    "startUrls": ["REPLACE_WITH_URLS"],
    "maxCrawlPages": 3,
    "crawlerType": "cheerio"
  },
  "waitSecs": 30
}
```

Use `WebFetch` for quick single-page extraction (no cost, no memory limit). Use `rag-web-browser` when you need clean markdown output for LLM synthesis. Use `website-content-crawler` for bulk multi-page crawls. Prefer `WebFetch` as the default — it's the most reliable and has zero cost.

**Target URLs**:
- Amazon product pages for top books in niche (product description + customer reviews)
- Competitor sales/landing pages
- Blog posts ranking for niche terms (see what content is working)
- Goodreads lists for niche books (see what readers respond to)
- Reddit threads about niche book recommendations

---

## Phase 2c: Competitor Reviews (Optional but High-Value)

### Google Maps Reviews

**Actor**: `compass/Google-Maps-Reviews-Scraper`
**Pricing**: Apify-maintained

```json
{
  "actor": "compass/Google-Maps-Reviews-Scraper",
  "input": {
    "startUrls": ["REPLACE_WITH_GOOGLE_MAPS_URLS"],
    "maxReviews": 100,
    "sort": "newest"
  },
  "waitSecs": 30
}
```

### Yelp Reviews

**Actor**: `tri_angle/yelp-review-scraper`
**Pricing**: Apify-maintained

```json
{
  "actor": "tri_angle/yelp-review-scraper",
  "input": {
    "startUrls": ["REPLACE_WITH_YELP_URLS"],
    "maxReviews": 100
  },
  "waitSecs": 30
}
```

**Why reviews matter**: Ben Settle advises mining competitor testimonials for insights. 1-3 star reviews are especially valuable — they reveal what competitors fail to deliver. These are the gaps your copy exploits.

---

## Phase 2d: Facebook Ads (Optional)

**Actor**: `apify/facebook-ads-scraper`
**Pricing**: $0.0058/ad

```json
{
  "actor": "apify/facebook-ads-scraper",
  "input": {
    "searchQuery": "REPLACE_WITH_COMPETITOR_OR_NICHE",
    "country": "US",
    "maxItems": 30
  },
  "waitSecs": 30
}
```

Shows what competitors are actively advertising — their hooks, angles, and positioning in real time.

---

## Phase 3a: Google Trends

**Actor**: `apify/google-trends-scraper`
**Pricing**: $0.003/result + negligible start fee
**CAUTION**: This Actor is often unreliable — can hang for 5+ minutes without producing results, especially on free/entry tiers. The timeRange parameter uses specific values only: `"now 1-H"`, `"now 4-H"`, `"now 1-d"`, `"now 7-d"`, `"today 1-m"`, `"today 3-m"`, `"today 5-y"`, `"all"`. `"today 12-m"` is NOT valid.

```json
{
  "actor": "apify/google-trends-scraper",
  "input": {
    "searchTerms": ["REPLACE_WITH_TERMS"],
    "timeRange": "today 5-y",
    "geo": "US"
  },
  "waitSecs": 45
}
```

Use 3-5 terms: core niche term, problem-oriented term, and competitor brand names.

**If this Actor times out or hangs** (common), skip it. The trend signal is nice-to-have but the voice-of-customer data from Reddit and YouTube is far more valuable for copywriting. Do not block the pipeline waiting for this Actor.

---

## Phase 3b: TikTok Trends (Optional — Younger Demographics)

**Actor**: `clockworks/tiktok-trends-scraper`
**Pricing**: Apify-maintained

```json
{
  "actor": "clockworks/tiktok-trends-scraper",
  "input": {
    "channel": "REPLACE_WITH_CATEGORY"
  },
  "waitSecs": 30
}
```

Only use if target demographic skews under 35.

---

## Phase 3c: LinkedIn (B2B Niche Only)

**Actor**: `harvestapi/linkedin-profile-posts`
**Pricing**: Community, ~$0.002/post

```json
{
  "actor": "harvestapi/linkedin-profile-posts",
  "input": {
    "searchTerm": "REPLACE_WITH_NICHE",
    "maxPosts": 30
  },
  "waitSecs": 30
}
```

Use only for B2B/professional niches. Reveals how professionals frame the problem and what language they use.

---

## Result Fetching

After each Actor run completes, fetch results:

```
mcp__actors-mcp-server__get-dataset-items
  datasetId: <from run output>
  limit: 100
```

Save all raw data before moving to Phase 4 synthesis.
