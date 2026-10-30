"""Healing Plates — the complete 30-day family meal plan (main book)."""
import week1
from plates_days import CAL_NAMES, DAYS_8_30, GROCERY, TREATS
from preview import AUTHOR, BOOK1, BRANDS, FREE, FREE_FROM_HTML, GUT_HTML, treats

MARKS = {BOOK1: "plates"}

HOW_TO_HTML = """
<p class="lead">This book is made to be easy. No long science, no fancy equipment — just real food, one day at a time.</p>
<div class="step"><div class="n">1</div><div><h3>Read the short chapters first</h3><p>They explain <i>why</i> we cook this way — gut health, foods to enjoy, foods to leave out, and simple daily habits.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Make the Kitchen Basics on a Sunday</h3><p>Seasoning mix, bread, flatbread and granola. They are used all month and save you hours.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Shop once a week</h3><p>Each week starts with a tick-box shopping list. Cross off what you already have.</p></div></div>
<div class="step"><div class="n">4</div><div><h3>Follow the day pages</h3><p>Every day has breakfast, lunch and dinner. Swap days around freely — just keep the foods safe.</p></div></div>
<div class="step"><div class="n">5</div><div><h3>Go gently</h3><p>Change is hard for children who love sameness. Keep one “safe” food on every plate and offer new foods next to it. No pressure, no battles.</p></div></div>
<div class="callout gold"><div class="t">Every recipe in this book is free from</div>
<p>""" + " · ".join(FREE) + """ — and baked, boiled or steamed instead of deep-fried. Recipes serve a family of 4 (2 adults, 2 children).</p></div>
<p class="disclaimer">This book shares food and lifestyle ideas from one mother's experience. It is not medical advice and does not replace your doctor, dietitian or therapist. Always check with your child's doctor before making big diet changes or giving herbs or supplements, especially if your child takes medication.</p>
"""

OILS = [("Extra virgin olive oil", 9.6), ("Cold-pressed avocado oil", 9.6), ("Traditional unrefined red palm oil", 9.5),
        ("Extra virgin coconut oil", 8.9), ("High-oleic sunflower oil", 8.0)]
OIL_HTML = "".join(f"""<div class="oil"><span class="on">{name}</span><span class="bar"><i style="width:{score * 10}%"></i></span><b>{score}</b></div>"""
                   for name, score in OILS)

ENJOY_HTML = """
<p class="lead">Healing food is not about what we take away — it's about what we add. Build every plate around these.</p>
<div class="grid2">
 <div class="box"><h3>1. Root vegetables first</h3><p>Squash, sweet potato, pumpkin and yam are the best carbs for our children. They are packed with plant nutrients, give slow natural sugars and fibre, and support the body's natural cleansing.</p></div>
 <div class="box"><h3>2. Green leafy vegetables</h3><p>Ugu, efo, kale, spinach and sukuma are full of anti-inflammatory goodness and help keep the body's elimination pathways open. <b>Broccoli sprouts are top of the list.</b></p></div>
 <div class="box"><h3>3. Wild blueberries &amp; mangoes</h3><p>All fruits are great, but these two are the author's favourites — rich in antioxidants that support the brain and the body under stress.</p></div>
 <div class="box"><h3>4. Coriander &amp; parsley</h3><p>Traditional cleansing herbs. Add them generously to soups, stews and smoothies — and always season fish with coriander.</p></div>
</div>
<h2>The cooking oil scorecard</h2>
<p class="muted small">The author's ranking of the healthiest oils to cook with (out of 10). Use these instead of vegetable oil blends.</p>
<div class="oils">""" + OIL_HTML + """</div>
"""

AVOID_HTML = """
<p class="lead">Here is what we leave out of every recipe in this book — and why.</p>
<table class="tbl">
<tr><th style="width:24%">We leave out</th><th>Why</th></tr>
<tr><td>Gluten</td><td>Many children with autism and gut trouble feel better without it. It can irritate a sensitive gut.</td></tr>
<tr><td>Dairy</td><td>High in fat and sugar. Lactose is hard to digest for many children, and the milk protein can inflame the gut.</td></tr>
<tr><td>Corn</td><td>A common hidden allergen — in pap, custard, baking powder, syrups and most “gluten-free” products.</td></tr>
<tr><td>Eggs</td><td>One of the most common food allergens in children. In the author's experience, removing them made a real difference.</td></tr>
<tr><td>Processed sugar &amp; junk</td><td>Cookies, cakes and sweets mix fat and sugar, feed unhelpful gut bugs and cause energy spikes and crashes.</td></tr>
<tr><td>Caffeine</td><td>Tea, coffee, matcha, chocolate and energy drinks push up the stress hormone cortisol and disturb sleep.</td></tr>
<tr><td>Pork</td><td>High in fat, and processed pork (bacon, ham, sausages) contains nitrates.</td></tr>
<tr><td>Tuna &amp; trout</td><td>Big fish high up the food chain collect more mercury. We choose small fish — and season them with coriander.</td></tr>
</table>
<h2>Clean home checklist</h2>
<div class="grid2">
 <div class="box"><ul class="ticks">
  <li>Swap foil for parchment paper — foil can leach aluminium into food.</li>
  <li>Replace scratched non-stick pans with stainless steel, cast iron or ceramic.</li>
  <li>Wash fruit and vegetables well to reduce pesticides.</li></ul></div>
 <div class="box"><ul class="ticks">
  <li>Check make-up, deodorant and skin creams — some contain heavy metals.</li>
  <li>Choose fragrance-free, simple products for your child.</li>
  <li>Cook from scratch and cut down on over-processed food.</li></ul></div>
</div>
"""

HABITS_HTML = """
<p class="lead">Food is only part of healing. These small daily habits from the author's own routine make a big difference.</p>
<div class="grid2">
 <div class="box"><h3>Better sleep</h3><ul><li>Lemon balm tea about 2 hours before bed — the author's favourite sleep herb.</li><li>Same bedtime every night, dim lights, no screens for the last hour.</li></ul></div>
 <div class="box"><h3>Easy bowels</h3><ul><li>Plenty of water every day.</li><li>Add seeds: chia, flax, pumpkin, sunflower, psyllium husk.</li><li>Fruits: celery, cucumber, mango, blueberry, watermelon.</li></ul></div>
 <div class="box"><h3>Move every day</h3><ul><li>Bouncing on a trampoline gets the lymphatic system moving.</li><li>Dancing, jumping and outdoor play all count.</li></ul></div>
 <div class="box"><h3>Detox slowly</h3><ul><li>Go gently. Too much, too fast can make children feel worse.</li><li>See the Healing Sips bonus book for one gentle drink a day.</li></ul></div>
</div>
<h2>Energy &amp; recovery</h2>
<p>Every cell has tiny “batteries” called mitochondria. When they are drained — by a heavy load on the body, missing nutrients, stress or toxins — children can struggle more.</p>
<div class="grid2">
 <div class="box"><h3>Signs of low energy reserves</h3><ul><li>Poor sleep</li><li>Bad reactions when detox is tried</li><li>Going backwards after an illness</li><li>Speech delay</li><li>Tiredness</li></ul></div>
 <div class="box"><h3>Recharge the batteries</h3><ul><li><b>Get out in the sun</b> every morning.</li><li><b>Keep them moving</b> — the trampoline is perfect.</li><li><b>Protect sleep</b> like gold.</li><li>Eat colourful, nutrient-rich food every day.</li></ul></div>
</div>
"""

SPEECH_HTML = """
<p class="lead">These are the food steps the author took while supporting her own child's speech. Every child is different — but many parents find a calmer gut helps everything else.</p>
<div class="step"><div class="n">1</div><div><h3>Change the plate</h3><p>Move towards more plant-based meals. Cut gluten, dairy, processed food and processed sugar.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Add brain-friendly vegetables</h3><p>Squash, leafy greens, kale, cabbage and <b>broccoli sprouts</b> — rich in sulforaphane.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Smart swaps</h3><p>Lentil pasta instead of wheat pasta. Buckwheat flour for bread.</p></div></div>
<div class="step"><div class="n">4</div><div><h3>Gentle support</h3><p>The author used <b>lion's mane and spirulina</b>, and found them helpful once her child began to talk. For gut troubles, <b>sea moss with black seed oil</b> (½ tsp, 3 times a week, age 3+).</p></div></div>
<div class="callout terra"><div class="t">Please keep working with your team</div>
<p>Food is a support, not a cure. Keep going with speech therapy, and always ask your child's doctor before starting any herb or supplement.</p></div>
"""

HERBS = [("Stimming (vocal, hand flapping, rocking)", "Lion's mane, brahmi, ashwagandha"),
         ("Sensory-seeking behaviour", "Lion's mane, brahmi"), ("Sleep", "Lemon balm, ashwagandha, lion's mane"),
         ("Hyperactivity", "Lemon balm, ashwagandha"), ("Picky eating", "Sea moss, lion's mane"),
         ("Constipation / diarrhoea", "Black seed oil, sea moss, milk thistle"),
         ("Vomiting / reflux", "Brahmi, ashwagandha, sea moss"), ("Frequent infections", "Astragalus, black seed oil, sea moss"),
         ("Eczema", "Sea moss, black seed oil"), ("Mould detox", "Astragalus, spirulina, black seed oil, sea moss")]
HERBS_HTML = """<p class="lead">Herbs many parents use alongside a healing diet. This is the author's personal guide.</p>
<table class="tbl"><tr><th style="width:42%">Symptom</th><th>Herbs parents commonly use</th></tr>""" + "".join(
    f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in HERBS) + """</table>
<div class="callout terra"><div class="t">Safety first — please read</div>
<ul><li>Talk to your child's doctor before giving any herb, especially if they take medication.</li>
<li>Many herbs (like ashwagandha, licorice and milk thistle) are not well studied in young children.</li>
<li>Sea moss is rich in iodine — check first if there is any thyroid condition.</li>
<li>Start one herb at a time, with a small amount, and watch closely.</li></ul></div>"""

TESTS = [("Ferritin & full blood count", "Tiredness, pale skin, clumsiness, developmental delay, frequent infections, picky eating, unexplained behaviour changes"),
         ("Iron studies", "Hyperactivity, poor sleep, emotional ups and downs, restlessness, headaches, restricted diet"),
         ("Vitamin B12", "Speech delay, clumsiness, developmental plateau, vegetarian or low-meat diet, gut problems"),
         ("Thyroid (TSH ± free T4)", "Hyperactivity or very low energy, mood swings, constipation, growth worries, family history, speech delay"),
         ("Coeliac screen (tTG-IgA + total IgA)", "Bloating, changing stools, low iron, behaviour worse after meals, family autoimmune history, slow growth"),
         ("CRP (± ESR)", "Ongoing tummy pain or gut problems, unexplained tiredness, poor growth, chronic diarrhoea"),
         ("Vitamin D", "Little time outdoors, autoimmune family history, low mood"),
         ("Liver function & albumin", "Gut problems, poor absorption, tiredness, regular medication, growth worries"),
         ("Metabolic panel", "Tiredness, great thirst, past jaundice, frequent weeing, sleep issues, energy spikes and crashes"),
         ("Zinc & copper", "Often not offered as standard — may need a private lab"),
         ("Fasting glucose & insulin", "Huge appetite, sleep problems, strong reaction to carbohydrates")]
TESTS_HTML = """<p class="lead">If your child shows some of these signs, these are tests you can ask your doctor about.</p>
<table class="tbl"><tr><th style="width:30%">Test</th><th>Signs that make it worth asking</th></tr>""" + "".join(
    f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in TESTS) + """</table>
<p class="disclaimer" style="margin-top:3mm">Your doctor will decide which tests are right for your child. Take this page to your appointment.</p>"""

HARD_DAY_HTML = """
<p class="lead">Some days are just hard. Meltdowns, no sleep, no energy. These meals take 15 minutes or less — and they're still safe and healing.</p>
<div class="grid2">
 <div class="box"><h3>From the freezer</h3><ul><li>Mama's chicken &amp; potato soup + buckwheat toast</li><li>Frozen meatballs + passata + rice pasta</li><li>Banana oat muffins + a smoothie</li></ul></div>
 <div class="box"><h3>From the cupboard</h3><ul><li>Rice noodles + coconut milk + spinach + leftover chicken</li><li>Sardines in tomato sauce + boiled yam</li><li>Tinned beans + rice + avocado</li></ul></div>
 <div class="box"><h3>No cooking at all</h3><ul><li>Cassava wrap + leftover chicken + avocado</li><li>Coconut yogurt + granola + fruit</li><li>DIY “lunchable” plate: rice crackers, chicken, cucumber, grapes</li></ul></div>
 <div class="box"><h3>Leftover makeovers</h3><ul><li>Jollof rice → fried rice next day</li><li>Butternut mac → baked mac bites</li><li>Roast chicken → soup, wraps, fried rice</li><li>Stew → pour over pasta or boiled yam</li></ul></div>
</div>
<div class="callout"><div class="t">Be kind to yourself</div><p>A simple safe meal is a win. Cereal-for-dinner days happen to every parent — just make it a safe one.</p></div>
"""

CLOSING_HTML = """
<p class="lead">Thirty days. Ninety meals. Hundreds of small, brave choices — by you <i>and</i> your child.</p>
<p>Whatever changed this month — a better night's sleep, a calmer afternoon, one new food tried, one less tummy ache — it matters. Write it down. Celebrate it.</p>
<div class="grid2">
 <div class="box"><h3>What next?</h3><ul>
  <li>Start again at Day 1 — it gets easier every round.</li>
  <li>Mark your family's favourite days and repeat them.</li>
  <li>Keep using your food &amp; mood tracker from the Printables pack.</li>
  <li>Bring foods back one at a time, and watch closely.</li></ul></div>
 <div class="box"><h3>Your bonus books</h3><ul>
  <li><b>Healing Lunch Box</b> — 30 days of school lunches.</li>
  <li><b>Healing Sips</b> — 30 gentle detox drinks.</li>
  <li><b>Healing Printables</b> — trackers, cards &amp; charts.</li>
  <li><b>Healing Celebrations</b> — birthday cake &amp; parties.</li></ul></div>
</div>
<p class="heart" style="margin-top:4mm">You are doing an amazing job. Your child is lucky to have you.</p>
<div class="sign">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div>
<p class="disclaimer" style="margin-top:8mm">© Tris Eliverson. All rights reserved. This book is for personal use only — please do not share or resell. The information in this book is based on personal experience and is for general information only. It is not medical advice. Always consult a qualified health professional before making changes to your child's diet or giving herbs or supplements. Always check food labels, as ingredients can change.</p>
"""

NOTES_HTML = '<p class="muted">Favourite recipes, changes that worked, foods your child tried…</p><div class="lines"></div>'


def pages():
    out = []

    def add(kind, data, toc=None):
        out.append((kind, data, toc))

    add("cover", dict(series="The 30-Day Allergy-Free Family Meal Plan", title=BOOK1, logo="plates",
        subtitle="Breakfast, lunch & dinner free from gluten, dairy, corn, egg, caffeine, tuna & processed sugar",
        tagline="Finally… food the whole family can eat.", free=FREE, badge=("90", "family<br>meals"), author=AUTHOR))
    add("text", week1.WELCOME, "A letter to you")
    add("toc", None)
    add("text", dict(kicker="Start here", title="How to use this book", html=HOW_TO_HTML), "How to use this book")
    add("divider", dict(kicker="Part 1", title="Understanding healing food",
        text="Short, simple chapters on why we cook this way — from the author's own notes and experience."), None)
    add("text", dict(kicker="Know before you shop", title="Where allergens hide", html=FREE_FROM_HTML), "Where allergens hide")
    add("text", dict(kicker="Restoring the gut", title="5 steps to healing the gut", html=GUT_HTML), "5 steps to healing the gut")
    add("text", dict(kicker="Build every plate", title="Foods to enjoy", html=ENJOY_HTML), "Foods to enjoy & the oil scorecard")
    add("text", dict(kicker="What we leave out", title="Foods & things to avoid", html=AVOID_HTML), "Foods & things to avoid")
    add("text", dict(kicker="Every day", title="Healing habits", html=HABITS_HTML), "Healing habits, energy & recovery")
    add("text", dict(kicker="From the author's journey", title="Food steps that may support speech", html=SPEECH_HTML), "Food steps that may support speech")
    add("text", dict(kicker="Natural support", title="Herbs by symptom", html=HERBS_HTML), "Herbs by symptom")
    add("text", dict(kicker="Talk to your doctor", title="Tests worth asking about", html=TESTS_HTML), "Tests worth asking about")
    add("divider", dict(kicker="Part 2", title="The 30-day plan",
        text="Kitchen basics, your month at a glance, weekly shopping lists and 90 family meals."), None)
    add("cards", dict(kicker="Make once, use all month", title="Kitchen basics", recipes=week1.BASICS[:3], kind="breakfast"), "Kitchen basics")
    add("cards", dict(recipes=week1.BASICS[3:], kind="breakfast"))

    names = {i + 1: n for i, n in enumerate(week1.WEEK1_NAMES)} | CAL_NAMES
    cells = [dict(day=d, meals=[("b", "B", names[d][0]), ("l", "L", names[d][1]), ("d", "D", names[d][2])]) for d in range(1, 31)]
    weeks = [cells[i:i + 7] for i in range(0, 30, 7)]
    weeks[-1] += [None] * (7 - len(weeks[-1]))
    add("calendar", dict(kicker="Your month at a glance", title="30 days of family meals", weeks=weeks, month=True), "Your month at a glance")

    all_days = week1.DAYS + DAYS_8_30
    week_treats = {1: treats} | TREATS
    for w in range(1, 6):
        first, last = (w - 1) * 7 + 1, min(w * 7, 30)
        cats = week1.GROCERY if w == 1 else GROCERY[w]
        add("grocery", dict(kicker=f"Week {w} · tick as you shop", title=f"Week {w} shopping list",
            intro=f"Everything for Days {first}–{last}. Cross off what you already have.", cats=cats),
            f"Week {w} · Days {first}–{last}")
        for d in all_days[first - 1:last]:
            add("day", d)
        if w in week_treats:
            add("two", dict(kind="treat", recipes=week_treats[w],
                note="Every Friday is <b>Sweet Treat Day</b> — because healing food should still feel like a celebration."))

    add("divider", dict(kicker="Part 3", title="Extra help",
        text="Quick meals for hard days, where to shop, and a few words before you go."), None)
    add("text", dict(kicker="For the hard days", title="15-minute rescue meals", html=HARD_DAY_HTML), "15-minute rescue meals")
    add("brands", dict(kicker="Make shopping easier", title="Allergy-friendly brands near you",
        intro="Always read the label — brands can change their recipes. Many gluten-free products still contain corn or egg.",
        regions=BRANDS), "Allergy-friendly brands near you")
    add("text", dict(kicker="Your notes", title="My notes", html=NOTES_HTML, white=True), "My notes")
    add("text", dict(kicker="You did it", title="Thirty days of love", html=CLOSING_HTML), "Thirty days of love")

    toc = [(t, i + 1) for i, (_, _, t) in enumerate(out) if t]
    for kind, data, _ in out:
        if kind == "toc":
            data = dict(kicker="Inside this book", title="Contents", items=toc)
        yield BOOK1, kind, data
