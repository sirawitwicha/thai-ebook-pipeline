# Ebook Pipeline v1 — Design

## Flow

```
[Phase 1] RESEARCH
  Apify Scrape:
    - Reddit (subreddits) -> pain points, complaints
    - Facebook Groups/Posts -> problems of Thai people
    - Pantip -> hot topics, questions
    - YouTube Comments -> what people complain about
    - Amazon Bestsellers -> what sells (direction)
    - Google Trends -> keyword direction

  Analyze -> summary:
    - Top 10 pain points (quoting real people)
    - Demand signal (trending up/down)
    - Competition analysis (existing books?)
    - Recommended niche + book angle

  Output: market-brief.md

[Phase 2] OUTLINE
  - Use pain points from research -> chapter topics
  - Each chapter = answers 1 pain point
  - TOC + 1-paragraph summary per chapter
  Output: outline.md -> APPROVAL

[Phase 3] WRITING
  Voice: RedRemasterRed style:
    - Conversational Thai (guh/meung/krup)
    - Rhetorical questions
    - Real examples, not theory
    - Curse words as rhythm (maeng/kod/sut)
    - Self-deprecating humor
    - End each chapter with a question to provoke thought

  Structure per chapter:
    1. Hook (real quote from research)
    2. Story - how normal people fail at this
    3. Analysis - why it happens
    4. Solution - practical steps
    5. Cliffhanger - hook for next chapter

  Write 3-5 chapters per batch
  Humanizer pass (Thai) -> remove AI-isms
  Output: drafts/

[Phase 4] EDIT
  - Chapter-by-chapter editing
  - Patch any section fast
  - Tone consistency check
  - Re-humanize if needed

[Phase 5] PDF
  - Thai font embedded
  - Clean layout (cover, TOC, chapters, about author)
  Output: output/book-title.pdf

[Phase 6] MARKETING
  - Extract quotes from book -> ad copy
  - Extract pain points from research -> ad headlines
  - 5 Facebook Ad headlines
  - 5 TikTok Script hooks
  - 3 Email sequences
  - 1 Landing page copy
  Output: output/marketing-kit.md
```