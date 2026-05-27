# Story-Mining Query Strategy — 10 Categories

Optional Phase 0 for the story skill. Run these queries when the existing research data lacks the specific, vivid details that make Settle-style stories feel real. This data persists on disk — scrape once, reuse across all copywriting outputs.

**When to scrape**: When you need bizarre counterintuitive facts, historical depth, personal transformation stories, insider confessions, documented news events, or specific numerical proof — and the existing research files don't have them.

**When to skip**: When the 5 core research files (JSON, slang, copy-brief, headlines, openers) already contain enough vivid personal stories, historical references, and proof details to build a compelling narrative.

**Actor convention**: All queries use `mcp__actors-mcp-server__call-actor`. Reddit and YouTube are the highest-signal sources for personal stories. Google SERP is best for documented facts, history, and news.

---

## Category 1: Bizarre & Counterintuitive Facts

**What this yields**: The "let me tell you a bizarre story about..." opener. Tabloid-style hooks. Surprising discoveries that make the reader think "how is that possible?"

| Query | Actor | What to extract |
|---|---|---|
| `"[niche] strange but true"` | Google SERP | Documented bizarre cases |
| `"weirdest [niche] case ever"` | Reddit, Google | Extreme outlier stories |
| `"[niche] discovery that changed everything"` | Google, YouTube | Serendipitous breakthrough moments |
| `"the strangest thing about [niche problem]"` | Reddit | Community-shared oddities |
| `"[niche] myth that turned out to be true"` | Google | Counterintuitive validated facts |
| `"unbelievable [niche] story"` | Reddit, YouTube | Dramatic personal accounts |

**Settle prototype**: "Let me tell you a bizarre story about a man who got arrested due to his prostate problems."

---

## Category 2: Historical Origin & Gravitas

**What this yields**: "Built-in gravitas." Documented history that makes the topic exciting. Ancient practices. The origin story of the problem or solution. Already-written stories you just retell.

| Query | Actor | What to extract |
|---|---|---|
| `"history of [niche problem]"` | Google, Wikipedia | Timeline of the problem |
| `"how ancient [civilization] dealt with [niche]"` | Google | Ancient practice details |
| `"who first discovered [niche solution]"` | Google | Origin story of the solution |
| `"[niche] in the 19th century"` / `"early 1900s"` | Google | Historical context |
| `"ancient [niche] practices still used today"` | Google | Continuity and gravitas |
| `"the forgotten history of [niche]"` | Google | Untold stories with mystery |
| `"[niche] through the ages"` | Google | Evolution narrative |
| `"[historical figure] [niche] [discovery / method]"` | Google, Wikipedia | Named historical anchor |

**Settle prototype**: "The world's first combat scientist — a Shanghai cop in the early 1900s who was in 600+ documented fights and taught US/UK soldiers how to kill Nazi stormtroopers with their bare hands."

---

## Category 3: Dramatic Personal Stories (Highest Signal)

**What this yields**: Complete narrative arcs: struggle → rock bottom → discovery → transformation. Real people's accounts with specific, vivid details you can retell. The bones of a Story About Someone Else.

| Query | Actor | What to extract |
|---|---|---|
| `"my [niche problem] nightmare"` | Reddit, YouTube | Personal horror stories |
| `"[niche problem] ruined my [life/career/marriage]"` | Reddit | High-stakes personal accounts |
| `"I thought I would [die/lose everything] from [niche]"` | Reddit | Life-or-death stakes |
| `"how I finally [beat/solved/escaped] [niche]"` | Reddit, YouTube | Complete transformation arc |
| `"[niche] success story against all odds"` | Google, Reddit | Dramatic turnaround |
| `"what finally worked for my [niche]"` | Reddit | The discovery moment |
| `"I tried everything for [niche] until"` | Reddit | Failure → discovery arc |
| `"[niche] almost killed me"` | Reddit | Maximum stakes |

**Settle prototype**: "I was 29 years old... dirt broke... pawned my championship winning bike and furniture just to eat... In truth, I had pretty much given up."

---

## Category 4: The Graveyard of Failed Solutions

**What this yields**: The "none of these did even a lick of good" section. Builds credibility by showing the protagonist didn't jump to the magic answer — they SUFFERED first, tried everything, and found only the real solution worked.

| Query | Actor | What to extract |
|---|---|---|
| `"[common solution] was a complete waste for [niche]"` | Reddit | Failed attempts |
| `"why [common solution] doesn't work for [niche]"` | Google, Reddit | The problem with existing options |
| `"I tried [solution] and it made [niche] worse"` | Reddit | Backfire stories |
| `"[niche] treatments that are useless"` | Reddit | Collective frustration |
| `"the dark side of [niche industry]"` | Google | Industry critique |
| `"things [niche industry] won't tell you"` | Google | Insider secrets |
| `"confessions of a former [niche practitioner]"` | Reddit, Google | Insider whistle-blowing |

**Settle prototype**: "He popped saw palmetto and beta-sitosterol supplements like M&M's. He also loaded up on prostate-friendly herbs... None of these solutions did even a lick of good for his prostate!"

---

## Category 5: News Events & Documented Reality

**What this yields**: "A nine-year-old kid choked out a Pit Bull." Reality that sounds made up — but is documented. News stories you can reference by name. Events the market may already know about.

| Query | Actor | What to extract |
|---|---|---|
| `"[niche] in the news"` | Google (news filter) | Recent real events |
| `"famous [niche] case"` | Google | Landmark stories |
| `"[niche] lawsuit [large company/verdict]"` | Google | Legal drama with stakes |
| `"the [niche] case that changed everything"` | Google | Pivotal moments |
| `"[niche] world record"` | Google | Extreme achievements |
| `"[niche] documentary"` | Google, YouTube | Visual story material |
| `"[celebrity/public figure] [niche problem] story"` | Google | Borrowed fame/recognition |

**Settle prototype**: "I told another story within that same ad that, while not historical... it was a recent news story at the time, where a nine-year old kid choked out a Pit Bull to save him and his little girl friend."

---

## Category 6: Specific Numbers & Data Points

**What this yields**: Hard numbers for credibility. "600+ documented fights." "Within 4 months." "$75 million in a single day." Specificity = believability.

| Query | Actor | What to extract |
|---|---|---|
| `"[niche] statistics [current year]"` | Google | Hard numbers for credibility |
| `"cost of [niche problem] per year"` | Google | Financial stakes |
| `"how many people suffer from [niche]"` | Google | Scale of the problem |
| `"[niche] success rate"` | Google | Contrast numbers |
| `"average [niche sufferer] spends on solutions"` | Google | Financial pain |
| `"[niche] before and after statistics"` | Google | Transformation data |

**Settle prototype**: "Money flooded into my bank account — DAILY. Within just 4 months I was financially free... and out of the 'rat race' forever."

---

## Category 7: Pop Culture & Recognition Hooks

**What this yields**: Cultural touchpoints the market already knows. Indiana Jones. Top Gun. The Matrix. References that make your copy feel native to their world.

| Query | Actor | What to extract |
|---|---|---|
| `"[niche] in movies"` / `"in TV shows"` | Google | Pop culture references |
| `"famous [people/characters] with [niche problem]"` | Google | Recognition hooks |
| `"[niche] referenced in pop culture"` | Google | Cultural touchpoints |
| `"what [movie/show] got right about [niche]"` | Reddit | Audience-validated references |
| `"[niche] in [mythology / ancient texts / the Bible]"` | Google | Deep historical roots |

**Settle prototype**: "The Thuggee cult is where you get the name 'thug' from. It was the same cult from the movie Indiana Jones and the Temple of Doom."

---

## Category 8: Insider Knowledge & "Things They Don't Tell You"

**What this yields**: The hidden playbook. Secrets the industry keeps. Things only insiders know. Makes your copy feel like privileged information.

| Query | Actor | What to extract |
|---|---|---|
| `"what [niche experts/industry] won't tell you"` | Google | Insider secrets |
| `"I worked in [niche industry] for [X] years"` | Reddit | Insider confessions |
| `"secrets [niche profession] keeps"` | Google | Hidden knowledge |
| `"[niche] insider reveals"` | Google, YouTube | Whistleblower stories |
| `"what I wish I knew before [niche]"` | Reddit | Regret + lessons |
| `"the truth about [niche industry]"` | Google, Reddit | Unvarnished reality |

**Settle prototype**: "There was something he taught to the US and UK soldiers during WW2, when he was showing them how to kill Nazi stormtroopers with their bare hands."

---

## Category 9: The Enemy Exposed

**What this yields**: Vivid, specific details about what the enemy DOES. The horror of the alternative. What the market is currently suffering through. Makes your solution the obvious escape.

| Query | Actor | What to extract |
|---|---|---|
| `"the truth about [competitor/enemy name]"` | Google | Enemy exposed |
| `"why [enemy/industry] is [broken/corrupt]"` | Google, Reddit | Systemic critique |
| `"[enemy type] horror stories"` | Reddit | Enemy victim stories |
| `"how [enemy type] gets away with [bad behavior]"` | Google | The injustice detail |
| `"what [enemy] doesn't want [niche market] to know"` | Google | The hidden playbook |

**Settle prototype**: "A gruesomely invasive 'roto-rooter' surgery where they insert a metal instrument all the way down your penis shaft to remove portions of your prostate gland!"

---

## Category 10: Transformation & Emotional Reversal

**What this yields**: The "ascension to heaven." Specific results. Emotional payoff. The before→after that makes the reader think "I want THAT."

| Query | Actor | What to extract |
|---|---|---|
| `"[niche] before and after story"` | Reddit, YouTube | Transformation arc |
| `"how [niche solution] changed my life"` | Reddit, YouTube | Emotional payoff |
| `"I never thought [niche] could [result]"` | Reddit | Surprise + delight |
| `"from [worst state] to [best state] with [niche]"` | Reddit | Complete reversal |
| `"[niche] success in [short timeframe]"` | Reddit | Speed of results |

**Settle prototype**: "These new distributors signed up with no annoying objections... no 'hemming and hawing'... and no questions asked. They simply tracked me down, asked me to show them the plan, and signed up as distributors on the spot."

---

## Execution Notes

**Cost per category** (approximate, FREE tier):
- Reddit queries: ~$0.40-0.80 per category (100-200 results)
- Google SERP: ~$0.03 per category (6-8 queries)
- YouTube: ~$0.12 per category (30 videos)
- YouTube comments: ~$0.20 per category (100 comments)
- RAG Web Browser / WebFetch: FREE

**Full story-mining run** (all 10 categories): ~$3-5
**Targeted run** (3-4 categories most relevant to chosen story type): ~$1-2

**Data reuse**: Results are saved to `research-outputs/<niche>/YYYY-MM-DD_story-mining.md`. On subsequent runs, check if this file exists. If it does, read it instead of re-scraping. The story-mining data is a persistent asset — scrape once, use for headlines, openers, stories, bullets, and closes.
