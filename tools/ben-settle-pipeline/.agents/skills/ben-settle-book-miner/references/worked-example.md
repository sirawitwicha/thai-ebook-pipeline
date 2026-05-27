# Worked Example: Mining The Modern Machiavelli

This shows the `ben-settle-book-miner` skill applied to a real 285-page book. Follow the pattern — same structural scan first, then chunk-by-chunk mining with page citations.

---

## Step 1: The Structural Scan

First 15 pages + table of contents → one-page structural map.

```markdown
## Book Structural Scan
**Title**: The Modern Machiavelli — Playing Office Politics to Win
**Author**: Not named (published 2020)
**Niche**: Office politics / career advancement / workplace power dynamics
**Total pages**: 285

### Chapter Map
| Ch | Title | Pages | What It Teaches | Key Techniques Named |
|---|---|---|---|---|
| 1 | Introduction to Office Politics | ~1-25 | Why politics is unavoidable, "suck it up" mindset, locus of control | "Politics is the art of the possible" |
| 2 | Power in the Workplace | ~25-50 | Formal vs informal power, power sources, reading political power | TBD |
| 3 | Essential Skills | ~50-70 | Persuasion, charm, communication foundations | TBD |
| 4 | Fundamentals & Your Situation | ~70-90 | Decoding your values, political skill, organizational type | TBD |
| 5 | Initial Impressions | ~90-110 | First impressions, tailoring style, professional appearance | TBD |
| 6 | Reputation Management | ~110-130 | Baseline expectations, moving beyond, meetings efficiency | TBD |
| 7 | Decision-Making | ~130-150 | Questions, decision process, persuading others | TBD |
| 8 | Interacting with Others | ~150-170 | Communication basics, getting ideas across, saying no, tough discussions | TBD |
| 9 | Managing Upwards | ~170-190 | Dealing with boss, new managers, weak player strategy, "detecting insane managers" | "Detecting insane managers" |
| 10 | Managing Downwards | ~190-210 | Leadership personality, maximizing team, taking over new team, removing people | TBD |
| 11 | Networks | ~210-225 | Creating, tracking, nurturing professional networks | TBD |
| 12 | Influencing Others | ~225-240 | Picking targets, tradeable currencies, influence strategies, newcomer mistakes | "Tradeable currencies" |
| 13 | Negotiation | ~240-255 | Formal and informal negotiation approaches | TBD |
| 14 | When Things Go Wrong | ~255-270 | Last-ditch methods, covering your arse | "Cover your arse" strategies |
| 15 | Moving On | ~270-280 | Deciding to leave, negotiating new roles, spotting layoffs | TBD |
| 16 | Typical Political Shenanigans | ~280-285 | Defending against and using common political tactics | TBD |

### Dominant Voice
- Tone: Clinical/rationalist — like a strategy manual. No-nonsense, unsentimental.
- Reading level: 12th grade / university. Sophisticated vocabulary but not academic.
- Narrative style: 2nd person instructional ("you will find yourself..."). No stories — pure analysis.
- Voice signature: The rational strategist. No emotion. No aggression. Just cold logic about how power actually works.

### Thesis
Office politics is not "bad" or sleazy — it's a natural part of any group of humans. Those who refuse to learn it are choosing to lose. This book provides a systematic, rational approach to political skill across every dimension of workplace life: managing up, managing down, influencing peers, negotiating, protecting your reputation, and knowing when to leave.
```

---

## Step 2: Chunk 1 — Pain & Fear Profile (Worked Example)

**Pages mined**: 10, 12, 14-16 (early pages diagnosing why the reader needs this)

**Data fed to the Chunk 1 prompt**:

```
From page 10:
"find yourself left behind by those who *are* willing to play the game. If you
want to excel in your career, then you will have to learn."
"‘Matrix’-style management is everywhere... success will require you to lead
them without having authority to back you up. This is only possible with
persuasion and charm – the basic building blocks of office politics."
"Jobs are changing faster than ever... Short hops between roles create the
fastest route up... Understanding negotiation and influence lets you succeed
even when you are new to the political power structure."

From page 12:
"out of control and the world is conspiring against you. Sure, the
economy or your boss may suck, the politics of your current job
may be stacked against you. But complaining doesn't help
anything. Suck it up, see the world as one which you can change."
"the 'art of the possible'... you probably won't achieve your perfect goal
but you may still get the next-best thing."
"those with limited skills make moves that the experienced would
never even think of – random, chaotic approaches that give you no insight
into their goals or motivations"
"you should _never_ base any long term planning on [people making decisions
against their own interests]. Even the best idealist or the greatest fool
will eventually realise that they can make other choices to improve their lives."

[Additional pages fed: 14-16 — the "why people fail at office politics" section]
```

**Chunk 1 Output**:

```
Q1. WHAT KEEPS THEM AWAKE AT NIGHT?
- Being trapped in a "matrix" organization where they have responsibility 
  but no authority — having to lead people who have "no formal requirement 
  to do what you say" [page 10]
- Watching less competent but more political people "cruise past them on 
  their way to meaningful jobs with real salaries" [page 3 — foreword]
- Realizing they've been passed over not because of skill deficits but 
  because they refused to learn the game [page 10 — "find yourself left behind"]

Q2. TOP TERRORS
1. Being rendered powerless in a flat organizational structure where 
   traditional authority no longer works [page 10 — CORE TECHNIQUE]
2. Making a bad first impression at a new role and losing the political 
   window to establish themselves [page 10 — "make a good impression fast"]
3. Having their career derailed by "random, chaotic" colleagues whose 
   unpredictable political moves can't be defended against [page 12]
4. Basing long-term plans on people who eventually act in self-interest 
   [page 12 — "never base any long term planning on this"]
5. Not spotting that layoffs are coming until it's too late [Chapter 15 — TOC]

Q3. WHAT CAUSES THEM PAIN?
- Psychological: The cognitive dissonance of being told politics is "bad" 
  or "sleazy" while watching political players win [page 10 — "Accept the 
  idea of office politics"]
- Career: Being "left behind" by those willing to play the political game 
  [page 10]
- Professional: The frustration of having expertise but lacking the 
  political skill to get recognition for it [implied throughout]
- Emotional: Feeling "out of control" — like "the world is conspiring 
  against you" [page 12]

Q4. THEIR INSECURITIES
- They're afraid they're "not political by nature" — that some people 
  are born with it and they weren't [page 10 — the book directly counters this]
- They worry they waited too long to learn — that they're already behind 
  those who've been playing politics for years
- They fear that engaging in politics means becoming "sleazy" or 
  compromising their values [page 10 — "Accept the idea of office politics 
  is not 'bad'"]
- They're embarrassed that they've been "naive" about how organizations 
  actually work

Q5. WHAT MAKES THEM ANGRY?
- Watching people who are "not really all that good at it" still win 
  through random, chaotic political moves [page 12 — "random, chaotic 
  approaches that give you no insight into their goals"]
- Being told "just focus on your work" while political players get ahead 
  [page 10 — implied in the counter-argument the book makes]
- "Insane management decisions" derailing their carefully-designed plans 
  [page 12]
- The realization that they've been playing by rules that don't exist 
  [page 3 — foreword: "people who claim office politics is a waste of time... 
  are losers"]

Q6. WHO ARE THEY ANGRY AT?
- "Losers" (the author's term) — people who claim politics doesn't matter 
  and give bad career advice [page 3]
- "Insane managers" — arbitrary, irrational bosses [page 12 + Chapter 9's 
  "detecting insane managers"]
- Colleagues who use political tactics without skill — "random, chaotic 
  approaches" [page 12]
- The economy, the boss, "the politics of your current job" — external 
  forces they blame [page 12]

Q7. WHO DO THEY BLAME?
- The economy for making jobs insecure [page 12]
- Their boss for "sucking" [page 12]
- "The politics of your current job" for being "stacked against you" 
  [page 12]
- The education system for never teaching this [implied]
- BUT the book reframes all of this: "Suck it up, see the world as one 
  which you can change. You are responsible for your own success" [page 12]

Q8. WHAT DO THEY WORRY ABOUT MOST?
- That they'll never catch up to those who started learning politics earlier
- That their current company is a political dead end
- That every new job is a reset where they have to build political capital 
  from scratch [page 10 — "short hops between roles"]
- That they're fundamentally not cut out for politics [page 10 — the book 
  argues this is learnable]

Q11. URGENT HOT BUTTON CRISIS
- Matrix management is making traditional authority obsolete RIGHT NOW 
  [page 10 — "everywhere"]
- Jobs are changing faster than ever — the old "stay 30 years" model is 
  dead. Every role change requires re-establishing political position. 
  [page 10]
- The reader may already be "left behind" — the crisis is ongoing, not 
  looming [page 10]

Q15. TOP 3 DAILY FRUSTRATIONS
1. Leading people who have no formal obligation to follow — the matrix 
   management trap [page 10]
2. Having plans derailed by "insane management decisions" or unpredictable 
   colleagues [page 12]
3. Making decisions that others won't support because you haven't built 
   the political groundwork [implied from chapter structure]

Q24. WHAT DO THEY FEEL GUILTY ABOUT?
- Feeling that politics is "sleazy" — guilt about even considering it 
  [page 10 — "Accept the idea... is not 'bad'"]
- Having been naive for too long
- Possibly having dismissed politics earlier in their career and now 
  paying the price

---

PAIN PROFILE SUMMARY:
The Modern Machiavelli's reader is someone who took the "merit" bet and 
lost. They did good work. They avoided politics because they thought it 
was sleazy. And now they're watching less competent people pass them by. 
The core pain is not just career stagnation — it's the dawning realization 
that the rules they were taught ("work hard, be good, results speak") are 
NOT the rules the game is played by. The author's framing turns this from 
despair into agency: "Suck it up. You are responsible. Here's the manual."
```

---

## How The Remaining 5 Chunks Work

Same pattern. Different pages. Different questions.

- **Chunk 2 (Identity)**: Mine pages 3-15 (intro), the foreword, any "who this is for" language, all value statements throughout
- **Chunk 3 (Desires)**: Mine later chapters — 14-16 ("what success looks like"), the promises in chapter introductions
- **Chunk 4 (Culture)**: Scan ALL pages for references — this book is light on pop culture but references Machiavelli, business literature, management theory
- **Chunk 5 (Competitive)**: Mine pages 10-12 (what doesn't work, the "losers" framing), plus any section where the author positions against alternative approaches
- **Chunk 6 (Emotional)**: Mine the foreword, introduction, chapter 1 hooks, conclusion — anywhere the author is directly persuading the reader to engage

After all 6 chunks: Final Assembly produces `structured-profile.json`, `slang-dictionary.md`, `copy-brief.md`.
