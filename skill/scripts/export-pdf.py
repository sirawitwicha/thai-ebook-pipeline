#!/usr/bin/env python3
"""
Export ebook from drafts/ to PDF.
Usage: python export-pdf.py [book-title]

จะรวมไฟล์ drafts/*.md เรียงตามเลขหน้า → output/<book-title>.pdf
ต้องมี Sarabun font ใน ebook-pipeline/reference/fonts/
"""

import sys
import re
import pathlib

# Config
BOOK_TITLE = sys.argv[1] if len(sys.argv) > 1 else "ebook"
BASE_DIR = pathlib.Path(__file__).resolve().parent  # scripts/
PIPELINE_DIR = BASE_DIR.parent.parent.parent / "ebook-pipeline"
DRAFTS_DIR = PIPELINE_DIR / "drafts"
OUTPUT_DIR = PIPELINE_DIR / "output"
FONTS_DIR = PIPELINE_DIR / "reference" / "fonts"

FONT_REGULAR = FONTS_DIR / "Sarabun-Regular.ttf"
FONT_BOLD = FONTS_DIR / "Sarabun-Bold.ttf"

try:
    from fpdf import FPDF
except ImportError:
    print("Need fpdf2: pip install fpdf2")
    sys.exit(1)


class ThaiEbook(FPDF):
    def __init__(self):
        super().__init__()
        if FONT_REGULAR.exists():
            self.add_font("Sarabun", "", str(FONT_REGULAR), uni=True)
        if FONT_BOLD.exists():
            self.add_font("Sarabun", "B", str(FONT_BOLD), uni=True)
        self.thai_font = "Sarabun" if FONT_REGULAR.exists() else "Courier"

    def cover_page(self):
        self.add_page()
        self.set_font(self.thai_font, "B", 24)
        self.cell(0, 40, "", new_x="LMARGIN", new_y="NEXT")
        self.multi_cell(0, 10, BOOK_TITLE, align="C")

    def toc_page(self, chapters):
        self.add_page()
        self.set_font(self.thai_font, "B", 16)
        self.cell(0, 10, "สารบัญ", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        self.set_font(self.thai_font, "", 12)
        for i, title in enumerate(chapters, 1):
            self.cell(0, 8, f"  {i}. {title}", new_x="LMARGIN", new_y="NEXT")

    def chapter(self, title, body):
        self.add_page()
        self.set_font(self.thai_font, "B", 16)
        self.multi_cell(0, 10, title)
        self.ln(5)
        self.set_font(self.thai_font, "", 12)
        self.multi_cell(0, 7, body)


def extract_title_from_md(content):
    title_match = re.search(r"^#\s+(.+)", content)
    return title_match.group(1).strip() if title_match else ""


def extract_body_from_md(content):
    lines = content.splitlines()
    body = []
    started = False
    for line in lines:
        if line.startswith("# "):
            started = True
            continue
        if started:
            body.append(line)
    return "\n".join(body)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(DRAFTS_DIR.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {DRAFTS_DIR}")
        sys.exit(1)

    pdf = ThaiEbook()
    pdf.cover_page()

    chapters_content = []
    for f in md_files:
        content = f.read_text(encoding="utf-8")
        title = extract_title_from_md(content)
        body = extract_body_from_md(content)
        chapters_content.append((title, body))

    titles = [t for t, _ in chapters_content if t]
    pdf.toc_page(titles)

    for title, body in chapters_content:
        pdf.chapter(title, body)

    output_path = OUTPUT_DIR / f"{BOOK_TITLE}.pdf"
    pdf.output(str(output_path))
    print(f"PDF written: {output_path}")
    print(f"Pages: {pdf.page_no()}")


if __name__ == "__main__":
    main()
