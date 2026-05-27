# Synthesis Prompts — Chunked LLM Analysis

After all scraped data is collected, feed each chunk's prompt to the LLM with the RELEVANT subset of scraped data. Each chunk is independent — run them in sequence or parallel.

**Important**: Always include the [SCRAPED DATA] placeholder text in your prompt to the LLM. Replace it with the actual data for that chunk.

---

## Chunk 1: Pain & Fear Profile
**Questions covered**: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q11, Q15, Q24
**Feed this data**: Reddit posts/comments, YouTube comments, competitor 1-3 star reviews

```
You are a direct response copywriter doing Ben Settle-style "Criminally Profitable Research." Your job is to extract the raw, unfiltered emotional truth about a target market from their own words.

Analyze the data below — real conversations, complaints, and reviews from people in the [NICHE] market. Answer each question using ONLY what you find in the data. If the data doesn't answer a question, say "Insufficient data" — do not invent or assume.

QUESTIONS TO ANSWER:

1. WHAT KEEPS THEM AWAKE AT NIGHT? — Sunday night insomnia. What do they stare at the ceiling about? Quote exact phrases.
2. TOP TERRORS (in order) — Their "house of horrors." Both what they admit and what they're ashamed to admit. Most fears are irrational — identify which are rational vs irrational.
3. WHAT CAUSES THEM PAIN? — Physical, emotional, psychological, spiritual. List each type separately.
4. THEIR INSECURITIES — What do they hope nobody finds out? What are they embarrassed about? Make this list as long as the data supports.
5. WHAT MAKES THEM ANGRY? — List every anger trigger you find. Quote the exact language.
6. WHO ARE THEY ANGRY AT? — Specific targets: people, institutions, "gurus," companies, systems. Name them.
7. WHO DO THEY BLAME? — For their problems. Even irrational blame. Even excuses. Who or what is "at fault"?
8. WHAT DO THEY WORRY ABOUT MOST? — Not just fears. Nagging, pressing, terrifying worries. Separate from Q1/Q2.
11. URGENT HOT BUTTON CRISIS — What's the crisis in their life RIGHT NOW? Not last year — now.
15. TOP 3 DAILY FRUSTRATIONS — What frustrates them every single day? Quote their exact complaints.
24. WHAT DO THEY FEEL GUILTY ABOUT? — Even if they'd never admit it. What weighs on their conscience?

FORMAT YOUR ANSWER:
- For each question, list findings as bullet points
- Quote exact phrases from the data in "quotation marks" wherever possible
- Mark items as [HIGH SIGNAL] if they appear repeatedly across multiple sources
- End with a "Copywriter's Summary" — the single most powerful pain/fear angle for this market

[SCRAPED DATA]
```

---

## Chunk 2: Identity & Worldview
**Questions covered**: Q9, Q10, Q13, Q14, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q25, Q26, Q32, Q41
**Feed this data**: Reddit posts/comments, YouTube comments, Google SERP results, LinkedIn posts (if B2B), Facebook group content

```
You are a direct response copywriter doing market research. Analyze the data below to build a demographic and psychographic profile of the [NICHE] market. Answer only from the data — do not invent.

QUESTIONS TO ANSWER:

9. WHAT ARE THEIR VALUES? — What do they hold sacred? What lines won't they cross? What values must your copy NEVER violate?
10. WHAT RELIGION ARE THEY? — Or irreligious/atheist/agnostic? How does this affect how you talk to them?
13. INCOME BRACKET — Low/middle/high? How does this affect their buying psychology (prestige vs necessity)?
14. POLITICAL VIEWS — General leanings. Do they care about politics? Does it shape their buying?
17. WHO ARE THE MAIN BUYERS? — Describe the PRIMARY buyer persona. Not the lukewarm buyer — the HOT buyer who pulls out their credit card fastest.
18. WHO MAKES BUYING DECISIONS? — Do they need "permission" from a spouse? Are you selling to one person or multiple?
19. HOW OLD ARE THEY? — Generation, age range. How does this affect communication style?
20. GENDER — Who is the primary buyer? Should copy be gendered or neutral?
21. OCCUPATION — What do they do? Blue/white collar, executive, student, unemployed?
22. EDUCATION LEVEL — Reading level? Should you use big words or keep it at 5th grade level?
23. ARE THEY IN DEBT? — How do they handle money? Cash or credit? Comfortable with debt or despise it?
25. WHERE ARE THEY LOCATED? — Geography, urban/suburban/rural, what's their town like?
26. HOME OWNERSHIP — Own or rent? Expensive or cheap? What's their living situation?
32. SLANG & VERNACULAR — Extract every slang term, figure of speech, unique jargon, and phrase pattern. Build a mini dictionary. This is how you sound like an insider.
41. WHAT ROLES DO THEY PLAY? — Boss, parent, caretaker, leader, victim, provider? What hats do they wear?

FORMAT:
- Bullet points per question
- Quote exact language for Q32 (slang)
- End with a "Buyer Persona Summary" — a 3-sentence composite description of the ideal customer

[SCRAPED DATA]
```

---

## Chunk 3: Desires & Aspirations
**Questions covered**: Q12, Q16, Q31, Q37, Q38, Q39
**Feed this data**: Reddit posts, YouTube comments, competitor sales pages (what they promise), competitor testimonials

```
You are a direct response copywriter uncovering what a market secretly desires. People don't always admit what they want — sometimes they don't even know. Your job is to read between the lines of the data below and extract both stated and unstated desires.

QUESTIONS TO ANSWER:

12. WHO ARE THEIR ENEMIES? — Everyone has enemies. List every enemy or perceived enemy you find. These are targets you can rail against in copy.
16. WHAT DO THEY WANT MORE THAN ANYTHING? — Not what they SAY they want. What would they crawl through broken glass to have? Look at what they BUY, not what they say.
31. WHAT DO THEY SECRETLY FANTASIZE ABOUT? — Fame? Power? Revenge? Recognition? The body they want? The life they imagine? Read between the lines.
37. WHO DO THEY CRAVE RECOGNITION FROM? — Whose approval matters most? A parent? A boss? A former doubter? A romantic interest?
38. WHO DO THEY WANT TO IMPRESS? — Whose radar do they want to be on? Who are they performing for?
39. WHAT DO THEY DO FOR FUN? — What they ACTUALLY do, not what they say they do. Observe behavior patterns in the data.

FORMAT:
- For each question, separate what they SAY from what the data REVEALS
- Quote aspirational language from the data
- End with a "Core Desire Statement" — one sentence capturing what this market truly wants, in language that would resonate emotionally

[SCRAPED DATA]
```

---

## Chunk 4: Media & Culture Consumption
**Questions covered**: Q34, Q35, Q36, Q44
**Feed this data**: Reddit posts (media references), YouTube video topics/titles, Google SERP (what content ranks)

```
You are a direct response copywriter mapping a market's cultural consumption. What they read, watch, and discuss reveals how to talk to them — what references will resonate, what stories they respond to, what cultural touchpoints make you sound like "one of them."

QUESTIONS TO ANSWER:

34. WHAT BOOKS ARE THEY READING? — Fiction, non-fiction, self-help, business, fantasy? List specific titles and authors you find mentioned. These are conversation anchors for your copy.
35. WHAT MOVIES ARE THEY WATCHING? — Genres, specific films, franchises they reference. What kind of stories do they gravitate toward?
36. WHAT TV SHOWS ARE THEY WATCHING? — Specific shows. Characters they talk about. Ben Settle once referenced Jack Bauer (from "24") in a self-defense ad because Claritas data showed his market watched it — those references make copy feel native.
44. WHERE DO THEY HANG OUT ONLINE? — Forums, subreddits, Facebook groups, Discord servers, Twitter communities, TikTok niches. "The single most powerful research tool I've ever used" — Ben Settle. List every community you find and note the tone/vibe of each.

FORMAT:
- List findings with specific titles and references
- Note which communities are highest-signal (most active, most honest, most emotional)
- End with a "Cultural Playbook" — the top 5-10 references you could naturally weave into copy

[SCRAPED DATA]
```

---

## Chunk 5: Competitive & Market Intelligence
**Questions covered**: Q28, Q33, Q42, Q43, Q45
**Feed this data**: Google SERP results, competitor sales pages (from RAG Web Browser), Amazon listings, Facebook ads, competitor reviews

```
You are a direct response copywriter analyzing the competitive landscape. Your goal is to understand what's already being sold, how it's being sold, and where the gaps are that YOUR copy can exploit.

QUESTIONS TO ANSWER:

28. #1 URGENT PROBLEM THEY'RE TRYING TO SOLVE — Narrow it to ONE overarching, urgent problem. If you get this right, 80% of your copywriting job is done before you write a word.
33. WHO IS SUCCESSFULLY SELLING SIMILAR — List competitors. What are their hooks? What benefits do they lead with? What proof elements do they use? What's their offer structure? Where are the holes in their approach?
42. ARE THEY LOOKING TO BE SOLD OR LOOKING FOR INFO? — Based on search queries and behavior, where on the awareness spectrum are they? Report-style or pitch-style?
43. WHAT RELATED PRODUCTS ARE THEY BUYING? — What else is in their basket? What do they buy before/after/alongside? This reveals upsell opportunities and adjacent market understanding.
45. MARKET AWARENESS (1-10 SCALE) — Gene Schwartz's scale:
    - 1-3: Don't know they have a problem (must show them the problem first)
    - 4-6: Know they have a problem, researching solutions (education-focused copy)
    - 7-8: Know solutions exist, comparing options (differentiation copy)
    - 9-10: Know about your product, want it now (offer/closing copy)

FORMAT:
- For each competitor, structure: Name, Hook, Lead Benefit, Offer, Proof Elements, Weaknesses/Gaps
- End with a "Competitive Gap Analysis" — what is nobody saying that your copy can own?

[SCRAPED DATA]
```

---

## Chunk 6: Emotional & Decision Drivers
**Questions covered**: Q29, Q30, Q40
**Feed this data**: Reddit posts, YouTube comments, competitor sales pages, all emotional language from previous chunks

```
You are a direct response copywriter mapping the emotional journey of a buyer. Understanding how they FEEL at each stage — from problem discovery to purchase — is what separates copy that sells from copy that gets ignored.

QUESTIONS TO ANSWER:

29. WHAT FEELINGS ARE THEY EXPERIENCING DURING SEARCH? — When they type a keyword into Google, when they click your link, when they open your email. What's their emotional state? Frustrated? Desperate? Curious? Skeptical? Hopeful? Defeated? This determines your headline approach.
30. HOW DO YOU WANT THEM TO FEEL WHEN THEY SEE YOUR SALES LETTER? — All decisions are emotional. The decision to be "logical" is itself emotional. What emotional transformation should your copy create? From [current state] → to [desired state]?
40. WHAT DO THEY COMPLAIN ABOUT TO FRIENDS OVER DRINKS? — Picture them at a bar, talking to their best friend about the problem. What exact words do they use? What emotions show on their face? What's the tone in their voice? This is your headline in raw form.

FORMAT:
- For Q29: Describe the emotional state in vivid, sensory language (not clinical labels)
- For Q30: Map the emotional transformation arc: Current State → Trigger → Journey → Arrival State
- For Q40: Write the "bar complaint" in first person, as if you ARE the prospect talking to their friend. Use the exact vernacular from the data. Get the tone right — frustrated, sarcastic, defeated, or whatever the data shows.
- End with a "Headline Goldmine" — 5-10 raw headline starters derived directly from the emotional language in the data

[SCRAPED DATA]
```

---

## Final Assembly Prompt

Run this AFTER all 6 chunks are complete. Feed ALL chunk outputs together.

```
You are a direct response copywriter assembling a complete market research profile and copywriting brief from the 6 analysis chunks below.

Using ONLY the chunk outputs provided, produce TWO deliverables:

## DELIVERABLE 1: Structured JSON Profile
Follow the schema. Every field that has data must be filled. Fields without data should be marked null. Do not invent data.

## DELIVERABLE 2: Copywriting Brief
A freeform but comprehensive brief containing:

### Headline Starters (10)
Raw headline ideas derived from the strongest pain/fear/desire signals. Use the market's exact phrasing. These should be ugly first drafts — not polished headlines. The best ones will feel uncomfortable or too direct.

### Primary Hook
The single strongest emotional angle. One sentence. This is the north star for all copy.

### Pain Point Bullets (10)
In market's exact language. Each should make the prospect think "that's exactly how I feel." Use sentence fragments. Use emotional words. Stack them for impact.

### The Enemy
Who or what the market blames. This is what you rail against in copy. Can be a person type, institution, mindset, or situation. Be specific.

### Desire Anchors (5)
What they secretly want. Phrased as outcomes: "How to [desire] without [feared tradeoff]"

### Slang & Vernacular Dictionary
Every slang term, jargon word, and phrase pattern found. Group by source if helpful. This is what makes your copy sound like an insider wrote it.

### Proof Elements Inventory
Every credibility marker that matters: certifications, social proof types, authority signals, demonstration ideas, case study angles, testimonial themes.

### Objection Inventory
Every reason they won't buy. Group by type: Price, Trust, Need, Urgency, Complexity, Identity ("this isn't for people like me"). For each, note what proof or framing could neutralize it.

### Tone Calibration
- Reading level: [grade level]
- Vocabulary: [simple/moderate/sophisticated]
- Emotional register: [fear-driven/aspiration-driven/anger-driven/etc]
- Pace: [urgent/measured/calm]
- Relationship: [friend/authority/coach/insider/outsider]

### Competitive Positioning Map
For each major competitor: their hook, their weakness, and the gap YOUR copy will occupy.

### The "Bar Complaint" Monologue
A 2-3 paragraph first-person narrative — AS the prospect talking to their friend at a bar about this problem. This is your empathy anchor when writing. Read it before every writing session.

[CHUNK 1 OUTPUT]
[CHUNK 2 OUTPUT]
[CHUNK 3 OUTPUT]
[CHUNK 4 OUTPUT]
[CHUNK 5 OUTPUT]
[CHUNK 6 OUTPUT]
```
