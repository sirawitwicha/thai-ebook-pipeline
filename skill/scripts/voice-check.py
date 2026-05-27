#!/usr/bin/env python3
"""Voice DNA Checker — score a chapter against RedMaster baseline.
Usage: python voice-check.py <chapter.md>
Output: DNA score (0-100%) + mismatch diagnostics."""

import sys, re
from pathlib import Path

# RedMaster baseline (per 1000 chars) from 86,583 char script
BASELINE = {
    "ครับ": 5.8,
    "คือ": 2.8,
    "แม่ง": 1.5,
    "รู้มั้ย": 0.1,
}

def analyze(text):
    chars = len(text)
    lines = [l.strip() for l in text.splitlines()
             if l.strip() and not l.startswith("#") and not l.startswith("|")
             and not l.startswith(">") and len(l) > 5]
    total_lines = len(lines)

    # Rhythm
    staccato = sum(1 for l in lines if len(l) < 20)
    natural = sum(1 for l in lines if 20 <= len(l) < 40)
    flow = sum(1 for l in lines if len(l) >= 40)

    # DNA
    scores = []
    details = {}
    for word, baseline in BASELINE.items():
        actual = (text.count(word) / chars) * 1000
        ratio = min(actual / baseline, 2.0)
        scores.append(ratio)
        details[word] = (actual, baseline, ratio)

    dna_score = (sum(scores) / len(scores)) * 100

    # Em dashes
    em_dashes = text.count("\u2014")

    return {
        "chars": chars,
        "lines": total_lines,
        "staccato_pct": (staccato / total_lines * 100) if total_lines else 0,
        "natural_pct": (natural / total_lines * 100) if total_lines else 0,
        "flow_pct": (flow / total_lines * 100) if total_lines else 0,
        "dna_score": dna_score,
        "details": details,
        "em_dashes": em_dashes,
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python voice-check.py <chapter.md>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    r = analyze(text)

    print(f"\n=== {path.name} ===")
    print(f"Chars: {r['chars']} | Lines: {r['lines']}")
    print(f"\n=== RHYTHM (target: S 18% N 52% F 29%) ===")
    print(f"STACCATO: {r['staccato_pct']:.0f}%  NATURAL: {r['natural_pct']:.0f}%  FLOW: {r['flow_pct']:.0f}%")
    print(f"\n=== VOICE DNA (per 1000 chars) ===")
    print(f"{'Word':<12} {'Actual':>7} {'Target':>7} {'Match':>7}")
    for word, (actual, baseline, ratio) in r['details'].items():
        print(f"{word:<12} {actual:>6.1f} {baseline:>7.1f} {ratio*100:>6.0f}%")
    print(f"\n=== DNA SCORE: {r['dna_score']:.0f}% ===")
    if r['dna_score'] >= 80:
        print("✅ PASS")
    elif r['dna_score'] >= 60:
        print("⚠️  NEEDS EDITING")
    else:
        print("❌ NEEDS REWRITE")

    if r['em_dashes'] > 0:
        print(f"\n⚠️  {r['em_dashes']} EM DASHES FOUND — STRIP THEM (Jared uses ZERO)")
    else:
        print(f"\n✅ Zero em dashes — clean")

if __name__ == "__main__":
    main()
