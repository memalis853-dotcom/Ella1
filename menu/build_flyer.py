"""One-page Dairy-Free & Gluten-Free flyer (HTML + PDF)."""
import html, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
N, S = "n", "s"
BLOCKS = [
  ("Soups", "with eba, pounded yam or amala", [("Egusi", N), ("Efo Riro", N), ("Afang", N), ("Ogbono", N), ("Banga", N), ("Seafood Okra", N)]),
  ("Rice", None, [("Smokey Jollof", N), ("Coconut Jollof", N), ("Asun Jollof", N), ("Suya Rice", N), ("Native Rice", N), ("Special Fried Rice", S)]),
  ("Stews & Proteins", None, [("Nigerian Turkey Sauce", N), ("Ofada Sauce", N), ("Curry Goat", N), ("Peppered Goat Meat", N), ("Grilled Fish", N), ("Suya", N)]),
  ("Afro-Fusion Pasta", "made with gluten-free pasta", [("Asun Pasta", S), ("Prawn Native Pasta", S), ("Creamy Jollof Pasta", S), ("Creamy Chicken Alfredo", S)]),
  ("Sides & Small Bites", None, [("Fluffy Moimoi", N), ("Akara", N), ("Kelewele", N), ("Honey BBQ Wings", S), ("Crispy Fried Chicken", S)]),
  ("Porridges", None, [("Ikokore", N), ("Adalu (Beans & Corn)", N), ("Oxtail & Plantain Porridge", N)]),
  ("Desserts", None, [("Velvet Cheesecake", S), ("Parfait", S), ("Panna Cotta", S), ("Apple Pie", S)]),
  ("Drinks", None, [("Zobo", N), ("Tigernut (Kunun Aya)", N), ("Tropical Juice", N), ("Blue Pina Colada", N)]),
]
def li(name, k):
    star = '<sup>*</sup>' if k == S else ''
    return f'<li><span>{html.escape(name)}{star}</span><i class="t {k}">DF</i><i class="t {k}">GF</i></li>'
blocks = "".join(f'<section><h2>{t}</h2>' + (f'<p class="sub">{s}</p>' if s else '') + '<ul>' + "".join(li(*x) for x in items) + '</ul></section>' for t, s, items in BLOCKS)
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>DF &amp; GF Flyer</title>
<link rel="stylesheet" href="../book/fonts/fonts.css"><style>
@page {{ size: Letter; margin: 0; }}
* {{ box-sizing:border-box; }}
html,body {{ margin:0; }}
body {{ font-family:'Nunito',sans-serif; color:#2a1d16; background:#fff; }}
.sheet {{ width:8.5in; height:11in; padding:0.35in 0.5in; display:flex; flex-direction:column; }}
.top {{ background:#b3261e; color:#fff; border-radius:14px; padding:16px 22px 14px; text-align:center; }}
.biz {{ font-size:9pt; letter-spacing:.18em; text-transform:uppercase; opacity:.9; border-bottom:1.5px dashed rgba(255,255,255,.6); display:inline-block; min-width:3.4in; padding-bottom:3px; height:20px; }}
h1 {{ font-family:'Fraunces',serif; font-weight:800; font-size:30pt; line-height:1.05; margin:6px 0 3px; }}
.tl {{ font-size:12pt; margin:0; font-weight:600; }}
.badges {{ display:flex; justify-content:center; gap:10px; margin-top:10px; flex-wrap:wrap; }}
.badges span {{ background:#fff; color:#b3261e; font-weight:900; font-size:9pt; padding:4px 11px; border-radius:20px; }}
.legend {{ display:flex; justify-content:center; gap:22px; font-size:9pt; color:#4a3a30; margin:10px 0 8px; }}
.grid {{ flex:1; display:grid; grid-template-columns:1fr 1fr; gap:6px 26px; align-content:start; }}
section {{ border-top:2px solid #b3261e; padding-top:4px; }}
h2 {{ font-family:'Fraunces',serif; font-weight:800; color:#b3261e; font-size:14pt; margin:0; }}
.sub {{ font-size:8pt; font-style:italic; color:#7a6658; margin:0 0 2px; }}
ul {{ list-style:none; margin:2px 0 0; padding:0; }}
li {{ display:flex; align-items:center; gap:3px; font-size:10pt; font-weight:700; padding:1.5px 0; border-bottom:1px dotted #eadfd5; }}
li span {{ flex:1; }}
sup {{ color:#b3261e; font-weight:900; line-height:0; vertical-align:baseline; position:relative; top:-0.4em; }}
.t {{ font-style:normal; font-size:6.8pt; font-weight:900; padding:1px 4px; border-radius:3px; border:1px solid #2e7d4f; }}
.t.n {{ background:#2e7d4f; color:#fff; }} .t.s {{ background:#fff; color:#2e7d4f; }}
.bottom {{ margin-top:8px; background:#fbefe7; border-radius:12px; padding:10px 16px; }}
.cta {{ text-align:center; font-family:'Fraunces',serif; font-weight:800; color:#b3261e; font-size:14pt; margin:0 0 6px; }}
.lines {{ display:flex; gap:18px; font-size:10pt; font-weight:800; }}
.lines span {{ flex:1; border-bottom:1.5px dashed #b9a99c; padding-bottom:3px; }}
.fine {{ font-size:7.2pt; color:#6b5a4e; margin:7px 0 0; text-align:center; }}
</style></head><body><div class="sheet">
<div class="top">
  <div class="biz"></div>
  <h1>Dairy-Free &amp; Gluten-Free<br>Naija Kitchen</h1>
  <p class="tl">Party trays · Family meals · Small chops · Catering</p>
  <div class="badges"><span>No Dairy</span><span>No Gluten</span><span>Full Flavour</span></div>
</div>
<div class="legend"><span><i class="t n">DF</i> <i class="t n">GF</i> Naturally free</span><span><i class="t s">DF</i> <i class="t s">GF</i><sup>*</sup> Made free with swaps</span></div>
<div class="grid">{blocks}</div>
<div class="bottom">
  <p class="cta">Order now · Brampton · Mississauga · Caledon · Kitchener</p>
  <div class="lines"><span>WhatsApp:</span><span>Instagram:</span></div>
  <p class="fine">Full menu available on request. Our kitchen also handles wheat, milk, eggs, nuts, fish, shellfish and soy, so traces are possible. Please tell us about allergies when you order.</p>
</div>
</div></body></html>"""
out = HERE / "df-gf-flyer.html"; out.write_text(page, encoding="utf-8")
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{out}');await p.evaluate(()=>document.fonts.ready);
await p.pdf({{path:'{HERE/"df-gf-flyer.pdf"}',format:'Letter',printBackground:true,preferCSSPageSize:true}});
await p.setViewportSize({{width:816,height:1056}});await p.screenshot({{path:'{HERE/"df-gf-flyer.png"}'}});await b.close();}})();"""
subprocess.run(["node","-e",js],check=True)
