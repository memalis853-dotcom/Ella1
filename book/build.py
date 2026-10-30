"""Render book pages to HTML and print them to PDF with Chromium.

Usage: python3 build.py preview
"""
import importlib
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment

from templates import DOC, MACROS, PAGES

HERE = Path(__file__).parent
OUT = HERE / "out"


def render(module_name):
    mod = importlib.import_module(module_name)
    env = Environment(autoescape=False)
    tpls = {k: env.from_string(MACROS + v) for k, v in PAGES.items()}
    html_pages = []
    n = {}
    for book, kind, data in mod.pages():
        n[book] = n.get(book, 0) + 1
        html_pages.append(tpls[kind].render(p=data, book=book, n=n[book]))
    doc = env.from_string(DOC).render(title=module_name, pages=html_pages, rendered=html_pages)
    out = HERE / f"{module_name}.html"
    out.write_text(doc, encoding="utf-8")
    return out


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "preview"
    html = render(name)
    OUT.mkdir(exist_ok=True)
    subprocess.run(["node", str(HERE / "print.js"), str(html), str(OUT / f"{name}.pdf"), str(OUT / name)], check=True)
