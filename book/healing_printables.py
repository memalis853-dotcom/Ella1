"""Healing Printables — Bonus Book 3: cards, trackers, charts & planners."""
from healing_plates import TESTS
from preview import AUTHOR, FREE
from week1 import (ALLERGY_CARD, BOOK4, PLANNER_HTML, REWARD_HTML, SAFE_HTML, SHOP_HTML, SWAP_HTML,
                   tracker)

MARKS = {BOOK4: "print"}
DOCX_AS_IMAGES = True

HOW_HTML = """
<p class="lead">These pages are made to be printed, stuck on the fridge, slipped into a school bag and scribbled on. Use them every day — they make the healing journey easier to follow and easier to share.</p>
<div class="grid2">
 <div class="box"><h3>Printing tips</h3><ul>
  <li>Print on A4 or US Letter — choose “Fit to page”.</li>
  <li>Print the trackers and planners as many times as you need.</li>
  <li>Thicker paper or card works best for allergy cards.</li></ul></div>
 <div class="box"><h3>Make them last</h3><ul>
  <li>Laminate the cheat sheet and planners, or slip them into plastic sleeves.</li>
  <li>Use a dry-wipe pen and reuse them every week.</li>
  <li>Keep allergy cards in the school bag, car and your purse.</li></ul></div>
</div>
<div class="callout"><div class="t">Share them</div>
<p>Give a copy of the allergy card and the safe-foods list to teachers, nannies, grandparents and anyone who feeds your child. The more people who know, the safer your child is.</p></div>
<p class="disclaimer" style="margin-top:4mm">© Tris Eliverson. All rights reserved. You may print these pages for your own family's use. Please do not share or resell the file. Not medical advice — always follow your doctor's guidance.</p>
"""

HIDDEN = [
    ("Gluten", "wheat, barley, rye, spelt, malt, semolina, semovita, durum, couscous, bulgur, seitan, brewer's yeast"),
    ("Dairy", "milk, butter, cream, cheese, whey, casein, caseinate, lactose, ghee, milk solids, buttermilk, curds"),
    ("Corn", "maize, cornflour, cornstarch, corn syrup, glucose syrup, dextrose, maltodextrin, xanthan gum, polenta. May come from corn: baking powder, citric acid, vanilla extract"),
    ("Egg", "egg, albumin, ovalbumin, lysozyme, mayonnaise, meringue, anything starting “ovo-”"),
    ("Caffeine", "coffee, tea, matcha, green tea, guarana, cola, cocoa, chocolate, kola nut, yerba mate, energy drinks"),
    ("Processed sugar", "sugar, cane sugar, sucrose, glucose, fructose, corn syrup, invert syrup, dextrose, caramel"),
    ("Pork", "pork, ham, bacon, lard, gelatine, pancetta, chorizo, salami, pepperoni"),
    ("Nuts (school)", "almond, cashew, hazelnut, walnut, pecan, pistachio, peanut, groundnut, kuli kuli"),
]
HIDDEN_HTML = """<p class="muted">Print, cut out and keep in your purse or phone case. Read labels for these words.</p>
<div class="minicards">""" + "".join(f'<div class="mini"><b>{a}</b><span>{b}</span></div>' for a, b in HIDDEN) + "</div>"

LUNCH_PLAN_HTML = """<p class="muted small">Plan the school week. Remember: one safe food + one new food in every box.</p>
<table class="track tall plan"><tr><th style="width:12%">Day</th><th>Main</th><th>Fruit</th><th>Vegetable</th><th>Snack</th><th style="width:13%">Drink</th></tr>""" + "".join(
    f"<tr><td>{d}</td><td></td><td></td><td></td><td></td><td></td></tr>" for d in ["Mon", "Tue", "Wed", "Thu", "Fri"]) + """</table>
<div class="grid2" style="margin-top:4mm"><div class="box"><h3>Prep on Sunday</h3><div class="lines" style="height:40mm"></div></div>
<div class="box"><h3>New food to try this week</h3><div class="lines" style="height:40mm"></div></div></div>"""

SUPP_HTML = """<p class="muted small">Write down every herb or supplement, how much, and anything you notice.</p>
<table class="track sip"><tr><th style="width:13%">Date</th><th style="width:27%">Herb / supplement</th><th style="width:12%">Amount</th><th style="width:10%">Time</th><th>Notes &amp; reactions</th></tr>""" + "".join(
    "<tr><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(22)) + """</table>
<div class="callout terra" style="margin-top:3mm"><div class="t">Safety first</div>
<p>Start one new herb or supplement at a time, at a small amount. Always check with your child's doctor first, especially if they take medication.</p></div>"""

DOCTOR_HTML = """<p class="muted small">Fill this in before an appointment and take it with you.</p>
<div class="grid2">
 <div class="box"><h3>Signs I've noticed (and since when)</h3><div class="lines" style="height:52mm"></div></div>
 <div class="box"><h3>My questions</h3><div class="lines" style="height:52mm"></div></div>
</div>
<div class="box" style="margin-top:3.5mm"><h3>Tests to ask about</h3><ul class="checks">""" + "".join(
    f"<li>{t}</li>" for t, _ in TESTS) + """</ul></div>
<div class="box" style="margin-top:3.5mm"><h3>What the doctor said · next steps</h3><div class="lines" style="height:42mm"></div></div>"""

PAGES = [
    ("Allergy cards", ALLERGY_CARD),
    ("Label decoder cards", HIDDEN_HTML),
    ("Smart swaps cheat sheet", SWAP_HTML),
    ("Food & mood tracker · Days 1–15", tracker(1, 15)),
    ("Food & mood tracker · Days 16–30", tracker(16, 30)),
    ("I tried it!", REWARD_HTML),
    ("Weekly meal planner", PLANNER_HTML),
    ("Lunch box planner", LUNCH_PLAN_HTML),
    ("My shopping list", SHOP_HTML),
    ("Herb & supplement log", SUPP_HTML),
    ("Doctor visit notes", DOCTOR_HTML),
    ("My child's safe foods", SAFE_HTML),
]


def pages():
    out = [("cover", dict(series="Bonus Book 3", title=BOOK4, logo="print",
                          subtitle="Allergy cards, trackers, charts & planners to make every day easier",
                          tagline="Print. Stick on the fridge. Breathe.", free=FREE,
                          badge=(str(len(PAGES)), "pages<br>to print"), author=AUTHOR), None),
           ("text", dict(kicker="Start here", title="How to use your printables", html=HOW_HTML), "How to use your printables"),
           ("toc", None, None)]
    for i, (title, html) in enumerate(PAGES, 1):
        out.append(("text", dict(kicker=f"Printable {i}", title=title, html=html, white=True), title))
    toc = [(t, i + 1) for i, (_, _, t) in enumerate(out) if t]
    for kind, data, _ in out:
        if kind == "toc":
            data = dict(kicker="Inside this pack", title="Contents", items=toc)
        yield BOOK4, kind, data
