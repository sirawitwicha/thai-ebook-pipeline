# Bullet Batching — The 7-Batch Memory-Safe System

100 bullets in one pass = memory loss, generic repetition after bullet #25, same patterns recycled. The fix: 7 independent batches. Each batch reads only its slice of the data inventory. Each batch produces 12-20 bullets. Between batches, context resets — the next batch starts fresh.

---

## The 7 Batches

### Batch 1: PAIN BULLETS (15-18 bullets)
**Data to read**: Inventory sections: Pain points + Enemy details
**Bullet types**: Pain (#5), What NOT To Do (#7), Curiosity (#1)
**Method**: Each pain point becomes 1-2 bullets. Enemy behaviors become "what not to do" bullets. Stack pain on pain.

```
Example (from office politics niche):
- The exact phrase that makes a credit thief completely unravel in a meeting — and why it works every single time.
- Why being the most competent person in the room actually makes you the #1 target for office manipulators.
```

**Append to file. Reset context.**

---

### Batch 2: SLANG & BIZARRE BULLETS (15-18 bullets)
**Data to read**: Inventory sections: Slang terms + Counterintuitive facts
**Bullet types**: Curiosity (#1), Can't Be Done (#2), 90% Solution (#9)
**Method**: Each slang term becomes a curiosity bullet. Counterintuitive facts become "Can't Be Done" bullets. Slang with hidden depth becomes 90% Solution.

```
Example:
- "Grey rocking" — the psychological technique that makes toxic coworkers completely forget you exist. (And why it's the most dangerous thing you can do if you do it wrong.)
- What "managing up" actually means — and the one word you should never use when doing it.
```

**Append to file. Reset context.**

---

### Batch 3: PROOF BULLETS (15-18 bullets)
**Data to read**: Inventory sections: Proof anchors + story-mining historical/news data
**Bullet types**: Proof (#3), Giveaway (#8), Contrast (#4)
**Method**: Each proof element gets a bullet. Contrast two proof elements together. Give away one complete proof-backed tip.

```
Example:
- The one word Socrates — perhaps the greatest master of persuasion who ever lived — used to win arguments against people who were dead set against him. (Machiavelli stole it. You can too.)
- A scientifically documented workplace gaslighting pattern — published in a peer-reviewed medical journal — that 9.2% of workers experience. Here's exactly what it looks like.
```

**Append to file. Reset context.**

---

### Batch 4: DESIRE & MISTAKE BULLETS (15-18 bullets)
**Data to read**: Inventory sections: Desire statements + Mistakes/Failures
**Bullet types**: Straight Benefit (#6), What NOT To Do (#7), 90% Solution (#9)
**Method**: Each desire becomes a benefit bullet. Each mistake becomes a "what not to do" bullet. Stack benefit → mistake → benefit.

```
Example:
- How to make yourself politically untouchable at work — in 30 days — without kissing ass, backstabbing, or becoming someone you despise.
- The #1 mistake competent professionals make when their boss steals their idea in a meeting. (Doing this almost guarantees it will happen again.)
```

**Append to file. Reset context.**

---

### Batch 5: OBJECTION & ENEMY BULLETS (12-15 bullets)
**Data to read**: Inventory sections: Objections + Enemy details
**Bullet types**: Contrast (#4), Pain (#5), Curiosity (#1)
**Method**: Each objection becomes a contrast or curiosity bullet. Enemy tactics become pain bullets. Turn objections into irresistible questions.

```
Example:
- Why "just focus on your work and stay above the politics" is the worst career advice ever given — and the Harvard Business Review agrees.
- How a narcissistic boss deploys "flying monkeys" — and the exact moment you realize you've been one without knowing it.
```

**Append to file. Reset context.**

---

### Batch 6: STORY-MINING BULLETS (12-15 bullets)
**Data to read**: `*_story-mining.md` — Categories 1-10 (if it exists)
**Bullet types**: Can't Be Done (#2), Proof (#3), Giveaway (#8)
**Method**: Bizarre facts become Can't Be Done. Historical facts become Proof. News events become Giveaway.

```
Example:
- The bizarre true story of a CXO who documented his entire rise through corporate ranks using Machiavellian principles — and what happened when his colleagues found out.
- 567 employees were studied for workplace emotional manipulation. The results were published in a scientific journal. Here's the one finding that shocked the researchers themselves.
```

**If no story-mining data exists: skip this batch. Append to file (if run). Reset context.**

---

### Batch 7: COMPRESSED FINALE + EXPANSION + SUB-HEADS (15-20 bullets)
**Data to read**: Quick scan of all remaining unused inventory items
**Bullet types**: Compressed Finale (#11), Expansion (#12), Dramatic Sub-Head (#10)
**Method**: Rapid-fire short bullets. Pick 2-3 and expand them mid-list. End 3-4 bullets with dramatic sub-heads.

```
Example:
- And a whole lot more, including...

How to spot a manipulator within 5 minutes of meeting them — before they even open their mouth... The "grey rock" method that made one woman's entire toxic department forget she existed... Why HR is never in your corner (and the one document you should write TODAY)... How to use the Socratic method to make a gaslighter completely unravel in front of everyone...

THE DAY I STOPPED REACTING EMOTIONALLY
AND STARTED RESPONDING STRATEGICALLY
WAS THE DAY EVERYTHING SHIFTED

- The 12 manipulation patterns that show up in every single toxic workplace — and the exact counter-tactic for each one... Why being "too good" at your job is exactly what makes you a target... How to build alliances without becoming a brown-noser... The four words that instantly destroy a credit thief's credibility in any meeting...
```

**Append to file. ALL BATCHES COMPLETE.**

---

## The Reset Protocol

Before starting each batch:
1. Announce which batch you're starting (e.g., "BATCH 2: SLANG & BIZARRE")
2. Read ONLY the inventory sections listed for that batch
3. Read the LAST 3 BULLETS from the file (to avoid exact duplicates, not for continuity)
4. Write this batch's bullets
5. Append to file
6. Announce: "Batch complete. Resetting."

Do NOT re-read the full bullet list or full research between batches. Only the specific inventory slice for the next batch + last 3 bullets for duplicate check.

## Anti-Repetition Rules

- No two bullets may start with the same word
- No bullet type may appear 3 times consecutively (vary up ammo)
- Every bullet must contain at least ONE specific detail (number, name, quote, technique name)
- If you catch yourself writing a bullet that could apply to ANY niche, delete it and pull a more specific data point from the inventory
