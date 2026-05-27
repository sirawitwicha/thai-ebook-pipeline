# Thai Ebook Pipeline — RedRemasterRed Voice

ระบบเขียน ebook ภาษาไทยด้วย AI ในสไตล์ **จาเร็ด (RedRemasterRed)** — วาทศิลป์ ตลก แหลม คม มีเรื่องเล่า

## Structure

```
ebook-pipeline/
├── skill/                  # Hermes Agent skill (ใช้กับ hermes-agent)
│   ├── SKILL.md            # Playbook หลัก — pipeline + voice rules
│   ├── references/         # Voice DNA, market research, Apify guides
│   ├── scripts/            # Voice checker, PDF export
│   └── templates/          # Chapter template
├── reference/
│   └── voice-samples/      # ตัวอย่างเสียง RedMaster (redmaster.md)
├── market-data/
│   ├── raw/                # ข้อมูลดิบจาก Apify / Web research
│   └── analysis/           # สรุป pain points + trends
├── drafts/                 # Draft 1 — DeepSeek V4-PRO (no DNA enforcement)
├── drafts-v2-refined/      # Draft 2 — DeepSeek V4-PRO + Voice DNA enforced ✅
└── output/                 # PDF + marketing kit (generated)
```

## วิธีใช้

### 1. ติดตั้ง skill ใน Hermes Agent

Copy `skill/` ไปที่ `~/.hermes/skills/creative/thai-ebook-pipeline/`

```bash
cp -r skill/* ~/.hermes/skills/creative/thai-ebook-pipeline/
```

### 2. ใช้กับ Hermes Agent

```
skill_view(name="thai-ebook-pipeline")
```

แล้วบอก niche — ระบบจะ research → outline → เขียน → DNA audit → PDF export

### 3. Voice DNA Targets (RedRemasterRed)

| Marker | Target | Meaning |
|--------|--------|---------|
| `ครับ` | 4.0-6.0/1K chars | Signature punctuation |
| `คือ` | 3.0-7.0/1K chars | Confidence connector |
| `แม่ง` | 0.5-2.0/1K chars | Emphasis spice |
| `—` (em dash) | **0** | Jared uses ZERO in 86K chars |

## Key Discovery (May 2026)

**DeepSeek V4-PRO + Voice DNA enforcement = Excellent Thai writing. No Gemini needed.**

- DeepSeek V4-PRO without DNA rules → formal, stiff, zero `แม่ง`
- DeepSeek V4-PRO with DNA enforcement → vivid, humorous, natural flow
- The model isn't the bottleneck — the **process** (calibrate → write → audit → inject → audit) is what matters

## หนังสือ

- **Title:** เงินเดือนหมดก่อนสิ้นเดือน? นี่คือวิธีที่แม่งใช้ได้จริง
- **Niche:** การเงินมนุษย์เงินเดือน (Personal Finance for Thai Salary Workers)
- **Target:** 40-50 หน้า, 8 บท, ขาย 99-199 บาทบน Meb/Ookbee

## Backup Strategy

Repo นี้คือ source of truth — ถ้าคอมหาย, clone ใหม่, ลง skill ใน Hermes Agent, ใช้ต่อได้ทันที
