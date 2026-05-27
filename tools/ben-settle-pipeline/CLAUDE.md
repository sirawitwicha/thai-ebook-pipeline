# Aplify Intel — Automated Copywriting Pipeline

Ben Settle's *Copy Slacker* 5-step formula (Headline → Opening → Story → Bullets → Close), automated as agent skills. Feed it market research or a book, get a complete sales letter out.

## The Pipeline (Non-Linear)

Bullets are the FOUNDATION, not step 4. The pipeline runs:

```
DATA ACQUISITION (pick one):
  Option A: ben-settle-research    → scrapes Reddit/YouTube/SERP via Apify MCP
  Option B: ben-settle-book-miner  → mines a book (page-by-page .md files)

  Both produce: structured-profile.json + slang-dictionary.md + copy-brief.md

COPYWRITING:
  ben-settle-bullet-04            → 100+ bullets (12 types) ← FOUNDATION
  ben-settle-headline-01          → 60+ headlines (11 types) ← feeds from bullets
  ben-settle-opening-paragraph-02 → 27 openers (9 types)
  ben-settle-story-03             → 400-575 word story (5 types, anti-compression)
  ben-settle-close-05             → guarantee, bonuses, takeaway, PS (4 components)
  ben-settle-assemble             → orchestrator + 10 editing passes (Chapter 8)
```

## Skills (`.agents/skills/`)

| Skill | Job | Input | Output |
|---|---|---|---|
| `ben-settle-research` | Scrape internet for market data | Niche name | profile.json, slang.md, copy-brief.md |
| `ben-settle-book-miner` | Mine a book for ammunition | `docs/<book>/page_*.md` | Same 3 files as research |
| `ben-settle-bullet-04` | Write 100+ bullets (12 types) | Profile + slang + copy-brief | `*_bullets.md` |
| `ben-settle-headline-01` | Write 60+ headlines (11 types) | Research + bullets | `*_headlines.md` |
| `ben-settle-opening-paragraph-02` | Write 27 openers (9 types) | Research + bullets | `*_opening-paragraphs.md` |
| `ben-settle-story-03` | Write 400-575 word story (5 types) | Research + headline + opener | `*_story.md` |
| `ben-settle-close-05` | Write close: guarantee, bonuses, takeaway, PS | Full narrative chain | `*_close.md` |
| `ben-settle-assemble` | Orchestrate pipeline + 10 editing passes | All outputs | `*_final-letter.md` |

Supporting: `apify-ultimate-scraper` (MCP actor reference), `skill-creator`, `brainstorming`

## Key Rules

- **Every claim must trace to research data or a book page.** No invented claims.
- **The market's exact language is the highest-value ammunition.** Slang dictionary entries feed all skills.
- **Anti-compression writing order** for stories: sections 6+7 written FIRST, then 1-5.
- **Token-aware bullet batching**: 7 batches, each reads only its data slice. Expansion bullets limited to 5 (50-100 words each).
- **Bullets feed headline/opener/story**, not the other way around. "Your headline is nothing more than a version of your best bullet." — Ben Settle.

## Output Location

All outputs go to `research-outputs/<project-slug>/` with `YYYY-MM-DD_` prefix.

## Source Docs

`docs/` contains Ben Settle's *Copy Slacker* book as page-by-page .md files (chapters 1-8), plus book-mining source material in `docs/the_modern_machiavelli/` (285 pages).

## MCP Servers

- `actors-mcp-server` / `apify` — web scraping (Reddit, YouTube, SERP, competitors)
- `mailerlite` — email marketing automation (connected: sirawitjunewicha@gmail.com)
- `playwright` — browser automation
- `tavily` — web search and research
- `filesystem` — file operations
- `resend`, `perplexity`, `supabase`, `stripe`, `vercel`, `sentry`, `linear`, `Ref`, `postgres` — available
