# Output Schemas & Templates

## Deliverable 1: Structured JSON Profile

```json
{
  "research_metadata": {
    "niche": "",
    "date": "",
    "data_sources": {
      "reddit_posts": 0,
      "reddit_comments": 0,
      "youtube_videos": 0,
      "youtube_comments": 0,
      "competitor_pages": 0,
      "google_trends_terms": 0,
      "competitor_reviews": 0
    },
    "cost_estimate_usd": 0
  },
  "composite_customer": {
    "pain_and_fear": {
      "keeps_awake_at_night": [],
      "top_terrors_ranked": [],
      "pain_physical": [],
      "pain_emotional": [],
      "pain_psychological": [],
      "pain_spiritual": [],
      "insecurities": [],
      "anger_triggers": [],
      "anger_targets": [],
      "blame_targets": [],
      "worries": [],
      "urgent_crisis": "",
      "daily_frustrations_top3": [],
      "guilt_sources": []
    },
    "identity_and_worldview": {
      "values": [],
      "religion": "",
      "income_bracket": "",
      "political_views": "",
      "primary_buyer_description": "",
      "buying_decision_maker": "",
      "age_range": "",
      "gender": "",
      "occupation": "",
      "education_level": "",
      "reading_level_grade": null,
      "debt_status": "",
      "location": "",
      "home_ownership": "",
      "slang_dictionary": {},
      "life_roles": []
    },
    "desires_and_aspirations": {
      "enemies": [],
      "what_they_want_most": "",
      "secret_fantasies": [],
      "craves_recognition_from": [],
      "wants_to_impress": [],
      "what_they_do_for_fun": []
    },
    "media_and_culture": {
      "books_mentioned": [],
      "movies_mentioned": [],
      "tv_shows_mentioned": [],
      "online_communities": []
    },
    "competitive_intelligence": {
      "number_one_urgent_problem": "",
      "competitors": [],
      "buying_stage": "",
      "related_products_bought": [],
      "market_awareness_1_to_10": null
    },
    "emotional_drivers": {
      "feelings_during_search": "",
      "desired_feeling_on_arrival": "",
      "bar_complaint_monologue": ""
    }
  },
  "copywriting_brief": {
    "headline_starters": [],
    "primary_hook": "",
    "pain_point_bullets": [],
    "the_enemy": "",
    "desire_anchors": [],
    "slang_dictionary": {},
    "proof_elements": [],
    "objection_inventory": [],
    "tone_calibration": {
      "reading_level": "",
      "vocabulary": "",
      "emotional_register": "",
      "pace": "",
      "relationship": ""
    },
    "competitive_positioning_map": [],
    "bar_complaint_monologue": ""
  }
}
```

## Deliverable 2: Copy Brief Template

Save as `YYYY-MM-DD_<niche-slug>_copy-brief.md`:

```markdown
# Copywriting Brief: [NICHE]
**Date**: YYYY-MM-DD
**Methodology**: Ben Settle "Criminally Profitable Research" — 45 Questions
**Data Sources**: [summary of what was scraped]

---

## Headline Starters
10 raw headline ideas in market's exact language:

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 

---

## Primary Hook
[One sentence — the single strongest emotional angle]

---

## Pain Point Bullets
[10 bullets in market's exact language]

---

## The Enemy
[Who/what the market blames — what you rail against in copy]

---

## Desire Anchors
[5 outcomes phrased as "How to X without Y"]

---

## Slang & Vernacular Dictionary
[Every insider term, jargon word, phrase pattern]

---

## Proof Elements Inventory
[Credibility markers: certifications, social proof, authority signals, demonstrations, case studies, testimonials]

---

## Objection Inventory
[Every reason they won't buy, grouped by type, with neutralizing strategies]

---

## Tone Calibration
- **Reading level**: 
- **Vocabulary**: 
- **Emotional register**: 
- **Pace**: 
- **Relationship**: 

---

## Competitive Positioning Map
| Competitor | Their Hook | Their Weakness | Your Gap |
|---|---|---|---|
| | | | |

---

## The "Bar Complaint" Monologue
[2-3 paragraph first-person narrative — AS the prospect talking to a friend. Read this before every writing session.]

---

*Generated via ben-settle-research skill — Apify MCP pipeline*
```
```
