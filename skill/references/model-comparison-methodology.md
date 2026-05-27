# Model Comparison Methodology for Thai Ebook Writing

How to A/B test two LLMs for Thai ebook writing quality with voice DNA metrics.

## Setup

```bash
# Create parallel draft directories
mkdir -p ebook-pipeline/drafts-{model-a,model-b}

# Copy outline to both
cp ebook-pipeline/drafts/outline.md ebook-pipeline/drafts-{model-a,model-b}/
```

## Protocol

### Phase 1: Calibration (1 chapter)

1. Switch to Model A: `/model <model-a>`
2. Write Chapter 1 with FULL voice DNA rules enforced during generation
3. Run DNA scoring immediately after writing
4. Fix any metric below threshold (targeted string replacements)
5. Repeat for Model B

### Phase 2: Batch Writing (chapters 2-8)

For each model, write chapters 2-8 with DNA rules active. Score each chapter immediately after writing. Apply targeted fixes where needed.

### Phase 3: DNA Audit

Run the scoring script against both draft directories:

```python
import pathlib

baseline = {"ครับ": (4.0, 6.0), "คือ": (3.0, 7.0), "แม่ง": (0.5, 2.0)}

for model_dir in ["drafts-model-a", "drafts-model-b"]:
    print(f"\n=== {model_dir} ===")
    total_chars = 0
    counts = {"ครับ": 0, "คือ": 0, "แม่ง": 0, "—": 0}
    
    for f in sorted(pathlib.Path(model_dir).glob("0*-*.md")):
        text = f.read_text()
        chars = len(text)
        total_chars += chars
        for marker in counts:
            counts[marker] += text.count(marker)
        
        # Per-chapter scores
        k = text.count("ครับ") / chars * 1000
        kh = text.count("คือ") / chars * 1000
        m = text.count("แม่ง") / chars * 1000
        ed = text.count("—")
        
        flags = []
        if k < 3.5: flags.append(f"ครับ={k:.1f}")
        if kh < 3.0: flags.append(f"คือ={kh:.1f}")
        if m < 0.5: flags.append(f"แม่ง={m:.1f}")
        if ed > 0: flags.append(f"—={ed}")
        
        status = "✅" if not flags else "⚠️ " + ", ".join(flags)
        print(f"  {f.name}: chars={chars:,} ครับ={k:.1f} คือ={kh:.1f} แม่ง={m:.1f} —={ed} {status}")
    
    print(f"  TOTAL: chars={total_chars:,} ครับ={counts['ครับ']/total_chars*1000:.1f} คือ={counts['คือ']/total_chars*1000:.1f} แม่ง={counts['แม่ง']/total_chars*1000:.1f} —={counts['—']}")
```

### Phase 4: Human Evaluation

Beyond metrics, evaluate:
- **Humor landing** — do jokes actually land, or feel forced?
- **Natural flow** — does it read like spoken Thai or translated English?
- **AI-sounding patterns** — generic transitions, hedging, formal register
- **Emotional impact** — does it make you feel something?

## Real Comparison: DeepSeek V4-PRO (2026-05-27)

Book: การเงินมนุษย์เงินเดือน (8 chapters)

| Metric | Without DNA Rules | With DNA Rules | Delta |
|--------|------------------|----------------|-------|
| ครับ/1K | 2.8 | 4.2 | +50% |
| คือ/1K | 2.9 | 3.8 | +31% |
| แม่ง/1K | 0.0 | 0.7 | ∞ |
| em-dash | 0 | 0 | — |
| Total chars | 35,800 | 27,580 | -23% |

**Key finding:** Same model, same topic — DNA enforcement during writing is the difference between reject and accept. The model's default Thai output is NOT production-ready without active voice guidance.
