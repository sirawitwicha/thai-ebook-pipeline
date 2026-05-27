# Apify Actor Reference — Ebook Research Pipeline

## Recommended Actors (minimize cost, maximize signal)

### 1. RAG Web Browser — BEST for general research
**ID:** `3ox4R101TgZz67sLr`
**Best for:** Market overview, niche validation, finding competitor books, general pain point discovery
**Input:**
```json
{"query": "most profitable ebook niches Thailand", "maxPages": 5}
```
**Cost:** Very low ($0.01-0.03 per run)
**Output:** Crawled page markdown + search metadata
**Pitfall:** Limited to text extraction from search results; not good for comments/forums

### 2. Reddit Search Scraper — Customer voice
**ID:** `pb74arTxftNSjmZp2` (NOT `oAuCIx3ItNrs2okjQ` which needs different format)
**Best for:** Mining real customer wording, pain points, frustrations
**Input:**
```json
{
  "searches": [
    {"query": "I can't save money", "maxPosts": 15},
    {"query": "credit card debt stress", "maxPosts": 15}
  ],
  "includeComments": true,
  "sort": "relevance"
}
```
**CRITICAL:** Field must be `"searches"` (array) — NOT `"searchTerms"`
**Cost:** Low-medium
**Output:** Post titles, bodies, subreddits, scores, comments

### 3. Amazon Review Scraper — Book market intelligence  
**ID:** `bYWmT1ZFYWbl859nG`
**Best for:** Finding what people love/hate about existing books in your niche
**Input:**
```json
{"searchTerms": ["personal finance", "money management"]}
```
**Cost:** Medium
**Output:** Products with reviews, ratings, pricing

### 4. YouTube Comments Scraper — Thai audience voice
**ID:** `p7UMdpQnjKmmpR21D`
**Best for:** Comments on Thai finance/AI/lifestyle videos
**Input:**
```json
{"videoUrls": ["https://www.youtube.com/watch?v=..."]}
```
**CRITICAL:** Field must be `"videoUrls"` (array) — NOT `"searchKeywords"`
**Pitfall:** Need video URLs first; use YouTube search separately

### 5. Google Trends — Demand validation
**ID:** `DyNQEYDj9awfGQf9A`
**Best for:** Validating that demand for your niche is real and trending
**Input:**
```json
{"keywords": ["keyword1", "keyword2"], "geo": "TH", "timeRange": "today 3-m"}
```
**CRITICAL:** `timeRange` must be one of: `"now 1-H"`, `"now 4-H"`, `"now 1-d"`, `"now 7-d"`, `"today 1-m"`, `"today 3-m"`, `"today 5-y"`, `"all"`
**NOT:** `"today 12-m"` (rejected — Google doesn't support 12-month window)

## Actors NOT worth using for this pipeline
- Reddit Scraper Lite (`oAuCIx3ItNrs2okjQ`) — uses different input format, returns unrelated content with search
- Reddit Posts Search (`9tC5hyQSyOISZh1AK`) — all runs FAILED; unclear input format

## Tips
- RAG Web Browser + Reddit Search Scraper = best combo for research
- Run multiple RAG Browser queries in parallel (different angles)
- Save ALL raw data to `ebook-pipeline/market-data/raw/` for future reference
