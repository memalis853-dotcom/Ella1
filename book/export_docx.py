"""Export a book module (e.g. healing_plates) to an editable Word document via pandoc.

Usage: python3 export_docx.py healing_plates
Needs out/<module>/p01.png (from build.py) for the cover image.
"""
import importlib
import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
from PIL import Image

HERE = Path(__file__).parent
OUT = HERE / "out"
BUILD = OUT / "docx-build"
GREEN, TERRA, INK, MUTED = "2E5E4E", "C8643B", "2B2722", "6E665B"
HEAD_FONT, BODY_FONT = "Georgia", "Calibri"

PAGEBREAK = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'
TOC_FIELD = '''
```{=openxml}
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click here and choose “Update Field” to show the contents with page numbers.</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
```
'''


def html_to_md(html):
    html = re.sub(r'<div class="(author-photo|lines)[^"]*".*?</div>', "", html, flags=re.S)
    oils = re.findall(r'<div class="oil"><span class="on">(.*?)</span>.*?<b>(.*?)</b></div>', html)
    if oils:
        table = "<table><tr><th>Oil</th><th>Score (out of 10)</th></tr>" + "".join(
            f"<tr><td>{n}</td><td>{v}</td></tr>" for n, v in oils) + "</table>"
        html = re.sub(r'<div class="oils">.*?</div>\s*$', table, html, flags=re.S)
    html = html.replace('<div class="n">', '<div class="n"><b>Step ').replace('</div><div><h3>', '</b></div><div><h3>')
    md = subprocess.run(["pandoc", "-f", "html", "-t", "markdown-raw_html-native_divs-native_spans-fenced_divs-bracketed_spans",
                         "--wrap=none"], input=html, capture_output=True, text=True, check=True).stdout
    md = re.sub(r"^#{1,6} ", "#### ", md, flags=re.M)   # in-chapter headings sit below the chapter heading
    return md


def esc(s):
    return s.replace("*", r"\*").replace("_", r"\_")


def recipe_md(r, label):
    meta = " · ".join(x for x in [label, r.get("region"), r.get("time")] if x)
    lines = [f"### {esc(r['name'])}", "", f"*{meta}*", ""]
    if r.get("goodfor"):
        lines += ["**Good for:** " + ", ".join(r["goodfor"]), ""]
    lines += ["**You need**", ""] + [f"- ☐ {esc(i)}" for i in r["ing"]] + [""]
    lines += ["**Steps**", ""] + [f"{n}. {esc(s)}" for n, s in enumerate(r["steps"], 1)] + [""]
    if r.get("why"):
        lines += [f"**Why it helps:** {esc(r['why'])}", ""]
    if r.get("tip"):
        lines += [f"**{r.get('tip_label') or 'Swap it'}:** {esc(r['tip'])}", ""]
    return "\n".join(lines)


def page_md(kind, p, mod_name):
    if kind == "cover":
        return f"![]({(BUILD / 'cover.png').as_posix()}){{width=6.3in}}\n"
    if kind == "toc":
        return f"::: {{custom-style=\"Kicker\"}}\n{p['kicker']}\n:::\n\n**Contents**\n{TOC_FIELD}"
    if kind == "divider":
        return f"# {p['kicker']}: {p['title']}\n\n{p['text']}\n"
    head = ""
    if p and p.get("kicker"):
        head += f"::: {{custom-style=\"Kicker\"}}\n{p['kicker']}\n:::\n\n"
    if kind == "text":
        photo = ""
        if 'author-photo' in p["html"]:
            photo = f"![]({(BUILD / 'author.jpg').as_posix()}){{width=2.2in}}\n\n"
        return head + f"## {p['title']}\n\n" + photo + html_to_md(p["html"])
    if kind == "day":
        out = f"::: {{custom-style=\"Kicker\"}}\nWeek {p['week']}\n:::\n\n## Day {p['day']}\n\n"
        if p.get("quote"):
            out += f"*{esc(p['quote'])}*\n\n"
        return out + "\n".join(recipe_md(r, lab) for r, lab in [(p["b"], "Breakfast"), (p["l"], "Lunch"), (p["d"], "Dinner")])
    if kind in ("cards", "two"):
        out = head + (f"## {p['title']}\n\n" if p.get("title") else "")
        if p.get("intro"):
            out += p["intro"] + "\n\n"
        out += "\n".join(recipe_md(r, r.get("label")) for r in p["recipes"])
        if p.get("note"):
            out += "\n" + html_to_md(p["note"])
        return out
    if kind == "calendar":
        rows = [c for week in p["weeks"] for c in week if c]
        heads = {"B": "Breakfast", "L": "Lunch", "D": "Dinner"}
        cols = [heads[m[1]] for m in rows[0]["meals"]] if len(rows[0]["meals"]) > 1 else ["Lunch box"]
        t = "| Day | " + " | ".join(cols) + " |\n|---|" + "---|" * len(cols) + "\n"
        t += "".join(f"| **{c['day']}** | " + " | ".join(m[2] for m in c["meals"]) + " |\n" for c in rows)
        return head + f"## {p['title']}\n\n" + t
    if kind == "grocery":
        out = head + f"## {p['title']}\n\n{p['intro']}\n\n"
        for cat, items in p["cats"]:
            out += f"#### {cat}\n\n" + "".join(f"- ☐ {esc(i)}\n" for i in items) + "\n"
        return out
    if kind == "brands":
        out = head + f"## {p['title']}\n\n*{p['intro']}*\n\n"
        for reg in p["regions"]:
            out += f"#### {reg['name']}\n\n" + "".join(f"- **{k}:** {esc(v)}\n" for k, v in reg["rows"]) + "\n"
        return out
    raise ValueError(kind)


def set_font(style, name, size=None, color=None, bold=None, italic=None):
    style.font.name = name
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        fonts.attrib.pop(qn(a), None)
    if fonts.getparent() is None:
        rpr.append(fonts)
    if size:
        style.font.size = Pt(size)
    if color:
        style.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic


def make_reference(book_title):
    ref = BUILD / "reference.docx"
    subprocess.run(["pandoc", "-o", str(ref), "--print-default-data-file", "reference.docx"], check=True)
    doc = Document(ref)
    st = {s.name: s for s in doc.styles}
    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if name in st:
            set_font(st[name], BODY_FONT, 11, INK)
    set_font(st["Heading 1"], HEAD_FONT, 30, GREEN, True)
    set_font(st["Heading 2"], HEAD_FONT, 24, GREEN, True)
    set_font(st["Heading 3"], HEAD_FONT, 15, TERRA, True)
    set_font(st["Heading 4"], HEAD_FONT, 12.5, TERRA, True, False)
    for h, before in (("Heading 1", 0), ("Heading 2", 0), ("Heading 3", 14), ("Heading 4", 10)):
        st[h].paragraph_format.space_before = Pt(before)
        st[h].paragraph_format.space_after = Pt(4)
    k = doc.styles.add_style("Kicker", 1)
    set_font(k, BODY_FONT, 9, TERRA, True)
    k.paragraph_format.space_after = Pt(0)
    # footer with book name and page number
    sec = doc.sections[0]
    fp = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = fp.add_run(f"{book_title} · Tris Eliverson · ")
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor.from_string(MUTED)
    r2 = fp.add_run()
    for t, txt in (("begin", None), (None, " PAGE "), ("end", None)):
        if t:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), t)
        else:
            el = OxmlElement("w:instrText")
            el.text = txt
        r2._r.append(el)
    r2.font.size = Pt(8.5)
    doc.save(ref)
    return ref


def main(mod_name):
    BUILD.mkdir(parents=True, exist_ok=True)
    mod = importlib.import_module(mod_name)
    Image.open(OUT / mod_name / "p01.png").convert("RGB").save(BUILD / "cover.png")
    Image.open(HERE / "img" / "author.webp").convert("RGB").save(BUILD / "author.jpg", quality=90)
    pages = list(mod.pages())
    book_title = pages[0][0]
    md = PAGEBREAK.join(page_md(kind, data, mod_name) for _, kind, data in pages)
    src = BUILD / f"{mod_name}.md"
    src.write_text(md, encoding="utf-8")
    ref = make_reference(book_title)
    dest = OUT / f"{mod_name}.docx"
    subprocess.run(["pandoc", str(src), "-f", "markdown", "-o", str(dest), f"--reference-doc={ref}",
                    "--resource-path", str(BUILD)], check=True)
    doc = Document(dest)
    doc.core_properties.title = book_title
    doc.core_properties.author = "Tris Eliverson"
    doc.save(dest)
    print("wrote", dest)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "healing_plates")
