# Customer Voice Mining Workflow

## Why this matters (Ben Settle / copywriting approach)

The difference between a book that sells and a book that doesn't:
- Most authors write what they THINK the customer needs
- Best copywriters use the EXACT WORDS the customer uses

When you know the exact words your customer uses to describe their pain, you can:
1. Write headlines that grab attention
2. Write bullets that feel personal
3. Write ads that convert

## Process

### Step 1: Apify Reddit Search Scraper
Actor: `pb74arTxftNSjmZp2`

```json
{
  "searches": [
    {"query": "pain point keyword 1", "maxPosts": 15},
    {"query": "pain point keyword 2", "maxPosts": 15}
  ],
  "includeComments": true,
  "sort": "relevance"
}
```

Collect: post titles + top comments → extract exact customer phrasing

### Step 2: Extract Customer Vocabulary Table

| Customer says | Industry says | Use in ad/bullet |
|--------------|---------------|------------------|
| "เงินไม่พอ" | "สภาพคล่องต่ำ" ❌ | "เงินไม่พอ" ✅ |
| "หนี้ท่วม" | "ภาระหนี้สินสูง" ❌ | "หนี้ท่วม" ✅ |
| "บัตรเครดิตแม่งกินเงิน" | "ดอกเบี้ยบัตร 18%" | "บัตรเครดิตแม่งกินเงิน" ✅ |

### Step 3: Build Ad Hooks from Real Quotes

From Reddit posts and comments, extract:
- **The "I'm sick of this" statement** — what makes people angry enough to buy a solution
- **The "nobody told me" statement** — what people feel cheated about
- **The "I wish I knew" statement** — what people regret

### Tips
- Never invent customer quotes. Use real ones from research.
- The best ad hooks are direct quotes with slight reformatting.
- Thai customers on Pantip/Reddit use specific phrasing — capture the exact words.
