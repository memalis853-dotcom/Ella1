"""Build the printable Dairy-Free & Gluten-Free menu (HTML + PDF)."""
import html, pathlib, subprocess

HERE = pathlib.Path(__file__).parent
N, S = "n", "s"  # N = naturally DF & GF, S = made DF & GF with swaps

SECTIONS = [
  ("Soups", "Served with eba, pounded yam, amala or plantain fufu (no semolina or wheat swallow)", [
    ("Afang Soup", N), ("Atama / Banga Soup", N), ("Black Soup", N), ("Edikang-Ikong Soup", N),
    ("Editan Soup", N), ("Efo Riro", N), ("Egusi Soup", N), ("Ewedu", N), ("Fisherman Soup", N),
    ("Gbegiri", N), ("Groundnut Soup", N), ("Nsala Soup (Ofe Owerri)", N), ("Ogbono Soup", N),
    ("Oha Soup", N), ("Seafood Okra", N), ("Waterleaf Soup", N)]),
  ("Rice", None, [
    ("Smokey Jollof", N), ("Coconut Jollof Rice", N), ("Asun Jollof Rice", N), ("Asun Rice", N),
    ("Suya Rice", N), ("Banga Rice", N), ("Native Rice", N), ("Local Rice", N),
    ("Signature Coconut Rice", N), ("Caribbean Rice and Peas", N), ("Dirty Rice", N),
    ("Jambalaya Rice", N, "with GF sausage"), ("Flavoured Herb Rice", S, "olive oil, no butter"),
    ("Special Fried Rice", S, "tamari, no soy sauce"), ("Pineapple Fried Rice", S, "tamari, no soy sauce"),
    ("Chinese Rice", S, "tamari, no soy sauce"), ("Chicken Biryani", S, "coconut yogurt marinade")]),
  ("Stews & Sauces", None, [
    ("Buka Stew", N), ("Nigerian Turkey Sauce", N), ("Ofada Sauce", N), ("Ofe Akwu", N),
    ("Curry Goat", N), ("Oxtail Sauce", N), ("Vegetable Sauce", N),
    ("Fish in Chilli Sauce", S, "rice-flour coated fish"), ("Bolognese Sauce", S, "no parmesan"),
    ("Beef Goulash", S, "coconut yogurt, cornstarch-thickened"),
    ("Butter Chicken Curry", S, "coconut cream & coconut yogurt"),
    ("Casserole Sauce", S, "cornstarch-thickened"), ("Sweet and Sour Beef", S, "tamari & cornstarch")]),
  ("Porridges", None, [
    ("Beans and Corn (Adalu)", N), ("Ekpang Nkukwo", N), ("Ewa Agoyin", N, "with dodo or GF bread"),
    ("Fried Beans Porridge", N), ("Ikokore", N), ("Oxtail and Plantain Porridge", N)]),
  ("Pasta & Noodles", "All pasta is gluten-free (rice, corn or chickpea)", [
    ("Asun Pasta", S), ("Prawn Native Pasta", S), ("Creamy Jollof Pasta", S, "coconut milk"),
    ("Spicy Beef Penne", S), ("Seafood Pasta", S),
    ("Creamy Chicken Alfredo", S, "coconut or cashew cream"), ("Pesto Pasta", S, "dairy-free pesto"),
    ("Spaghetti and Meatballs", S, "GF crumbs in meatballs"),
    ("Mac and Cheese", S, "dairy-free cheese sauce"), ("Lasagna", S, "GF sheets, dairy-free cheese"),
    ("Fresh Pasta (from scratch)", S, "GF flour blend"),
    ("Singapore Noodles", S, "rice noodles, tamari"), ("Spicy Chili Garlic Noodles", S, "rice noodles, tamari")]),
  ("Grills", None, [
    ("Grilled Fish", N), ("Rotisserie Chicken", N), ("T-bone Beef Steak", S, "olive-oil baste"),
    ("Honey Barbecue Chicken Wings", S, "homemade GF BBQ sauce")]),
  ("Sides", None, [
    ("Suya", N), ("Peppered Goat Meat", N), ("Grilled Turkey", N), ("Grilled Prawns", N),
    ("Fluffy Moimoi", N), ("Kelewele", N), ("Nkwobi", N), ("Fish Pepper Soup", N), ("Hummus", N),
    ("Hash Browns", N, "homemade"), ("Stuffed Masa", N, "rice flour only"),
    ("Nigerian Full Salad", S, "dairy-free dressing"),
    ("Chicken Caesar Salad", S, "DF dressing, chickpea croutons"), ("Naan Bread", S, "GF flour, coconut yogurt")]),
  ("Breakfast", None, [
    ("Akara", N), ("Yamarita", S, "rice-flour coating"), ("Buttered Potatoes", S, "dairy-free butter"),
    ("Creamy Mashed Potatoes", S, "oat milk"), ("Crispy Fried Chicken", S, "rice-flour coating"),
    ("Chicken and Chips", S), ("Potato Balls", S, "GF crumbs"), ("Frittata", S, "no cheese"),
    ("Flavoured Pancakes", S), ("Waffles", S), ("Garlic Bread", S, "GF bread"),
    ("Grilled Cheese Sandwich", S, "GF bread, DF cheese"), ("Shawarma", S, "GF wrap, garlic toum"),
    ("Turkey Sandwich", S, "GF bread"), ("Sub Sandwich", S, "GF bread"),
    ("Tortilla Vegetable Wrap", S, "GF wrap")]),
  ("Desserts & Iced Treats", None, [
    ("Berry Mix Popsicles", N), ("Apple Pie", S, "GF crust"), ("Velvet Cheesecake", S, "cashew filling, GF base"),
    ("Parfait", S, "coconut yogurt, GF granola"), ("Panna Cotta", S, "coconut milk"),
    ("Oreo-style Crumble", S, "GF cookies"), ("Blueberry Ice Cream", S, "coconut base"),
    ("Chocolate Chip Ice Cream", S, "coconut base"), ("Cookies & Cream Ice Cream", S, "coconut base"),
    ("Cookies & Cream Milkshake", S, "oat milk"), ("Eggnog", S, "oat milk & coconut cream"),
    ("Waffles and Ice Cream", S)]),
  ("Drinks & Mocktails", None, [
    ("Zobo (Hibiscus)", N), ("Tigernut Drink (Kunun Aya)", N), ("Tropical Juice", N), ("Kiwi Fizz", N),
    ("Wavy", N), ("Blue Pina Colada", N, "coconut cream")]),
]

def item(entry):
    name, kind, *note = entry
    note_html = f'<span class="note">{html.escape(note[0])}</span>' if note else ""
    star = '<sup class="star">*</sup>' if kind == S else ""
    return (f'<li><span class="nm">{html.escape(name)}{star}</span>{note_html}'
            f'<span class="tags"><b class="tag {kind}">DF</b><b class="tag {kind}">GF</b></span></li>')

sections_html = "".join(
    f'<section><h2>{t}</h2>' + (f'<p class="sub">{html.escape(sub)}</p>' if sub else "")
    + "<ul>" + "".join(item(e) for e in items) + "</ul></section>"
    for t, sub, items in SECTIONS)

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Dairy-Free &amp; Gluten-Free Menu</title>
<link rel="stylesheet" href="../book/fonts/fonts.css">
<style>
@page {{ size: Letter; margin: 0.45in 0.5in; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family:'Nunito',sans-serif; color:#2a1d16; background:#fff; font-size:9.6pt; }}
header {{ text-align:center; border-bottom:3px solid #b3261e; padding-bottom:8px; margin-bottom:10px; }}
.biz {{ display:inline-block; border-bottom:1.5px dashed #b9a99c; min-width:3.6in; height:22px; margin-bottom:4px; }}
.biz-l {{ font-size:7.5pt; letter-spacing:.12em; text-transform:uppercase; color:#8a776a; }}
h1 {{ font-family:'Fraunces',serif; font-weight:800; font-size:27pt; color:#b3261e; margin:4px 0 2px; }}
.tagline {{ font-size:10.5pt; color:#5b4a3f; margin:0; }}
.legend {{ display:flex; justify-content:center; gap:22px; margin:9px 0 2px; font-size:8.6pt; color:#4a3a30; flex-wrap:wrap; }}
.legend span {{ display:inline-flex; align-items:center; gap:5px; }}
.cols {{ column-count:2; column-gap:0.35in; }}
section {{ break-inside:avoid-column; margin:0 0 10px; }}
h2 {{ font-family:'Fraunces',serif; font-weight:800; font-size:14pt; color:#b3261e; margin:0 0 2px;
      border-bottom:1px solid #e7d9cd; padding-bottom:2px; }}
.sub {{ font-size:8pt; font-style:italic; color:#7a6658; margin:2px 0 3px; }}
ul {{ list-style:none; margin:0; padding:0; }}
li {{ display:flex; align-items:baseline; gap:6px; padding:2.4px 0; border-bottom:1px dotted #eadfd5; }}
.nm {{ font-weight:700; }}
.note {{ font-size:7.6pt; color:#8a776a; font-style:italic; flex:1; }}
.nm + .tags {{ margin-left:auto; }}
.tags {{ display:flex; gap:3px; white-space:nowrap; }}
.tag {{ font-size:6.6pt; font-weight:900; letter-spacing:.04em; padding:1px 4px; border-radius:3px; }}
.tag.n {{ background:#2e7d4f; color:#fff; border:1px solid #2e7d4f; }}
.tag.s {{ background:#fff; color:#2e7d4f; border:1px solid #2e7d4f; }}
.star {{ color:#b3261e; font-weight:900; }}
footer {{ margin-top:8px; border-top:3px solid #b3261e; padding-top:7px; font-size:7.8pt; color:#5b4a3f; break-inside:avoid; }}
footer p {{ margin:3px 0; }}
.order {{ display:flex; gap:20px; margin-top:7px; font-size:9pt; font-weight:700; color:#2a1d16; flex-wrap:wrap; }}
.order span {{ flex:1; min-width:2in; border-bottom:1.5px dashed #b9a99c; padding-bottom:2px; }}
@media screen {{ body {{ max-width:8.5in; margin:24px auto; padding:0 16px; }} }}
</style></head><body>
<header>
  <div class="biz"></div><div class="biz-l">Business name</div>
  <h1>Dairy-Free &amp; Gluten-Free Menu</h1>
  <p class="tagline">Naija favourites &amp; intercontinental dishes, made free from dairy and gluten</p>
  <div class="legend">
    <span><b class="tag n">DF</b><b class="tag n">GF</b> Naturally dairy-free &amp; gluten-free</span>
    <span><b class="tag s">DF</b><b class="tag s">GF</b><sup class="star">*</sup> Made dairy-free &amp; gluten-free with swaps</span>
  </div>
</header>
<div class="cols">{sections_html}</div>
<footer>
  <p><b>DF</b> = dairy-free &nbsp;·&nbsp; <b>GF</b> = gluten-free &nbsp;·&nbsp; Swaps include GF pasta and flour, tamari, coconut cream, oat milk and dairy-free cheese and butter.</p>
  <p><b>Allergy note:</b> our kitchen also handles wheat, milk, eggs, peanuts, tree nuts, fish, shellfish and soy. We take great care, but we cannot guarantee any dish is completely free of traces. Please tell us about any allergy when you order.</p>
  <div class="order"><span>Order / WhatsApp:</span><span>Instagram:</span></div>
</footer>
</body></html>"""

out_html = HERE / "df-gf-menu.html"
out_html.write_text(page, encoding="utf-8")
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{out_html}');await p.evaluate(()=>document.fonts.ready);
await p.pdf({{path:'{HERE / "df-gf-menu.pdf"}',format:'Letter',printBackground:true,preferCSSPageSize:true}});
await p.setViewportSize({{width:900,height:1100}});await p.screenshot({{path:'{HERE / "preview.png"}',fullPage:true}});
await b.close();}})();"""
subprocess.run(["node", "-e", js], check=True)
print("built", out_html)
