"""Healing Sips — Bonus Book 2: the 30-day gentle detox & juicing plan."""
from preview import AUTHOR, BOOK3, FREE
from week1 import DETOX, DETOX_RULES, R

MARKS = {BOOK3: "sips"}

WELCOME_HTML = """<div class="author-photo small"><img src="img/author.webp" alt="Tris Eliverson"></div>
<div class="letter">
<p class="hello">Dear Mama, dear Papa,</p>
<p>When I started my child's healing journey, one of the simplest things I did was add <b>one gentle drink a day</b>. A green smoothie in the morning. A calming cup of lemon balm before bed. Slowly, gently, things began to shift — and I saw a real, significant improvement in my child.</p>
<p>This book holds those drinks: my own daily detox smoothie first, then 29 more juices, smoothies and tonics for the whole family. Each one tells you what it is good for, so you can choose the right glass for the day.</p>
<p>Please go slowly. Detox is not about doing more — it's about doing a little, every day, with love.</p>
<p class="heart">One gentle glass a day. ♥</p>
<div class="sign">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div></div>"""

INGREDIENTS = [
    ("Celery", "Digestion, hydration — the foundation of my daily detox"),
    ("Green apple", "Fibre that helps bind and carry out waste"),
    ("Coriander & parsley", "Traditional cleansing herbs"),
    ("Blueberries", "Antioxidants for the brain"),
    ("Ginger", "Calms nausea and settles the tummy"),
    ("Lemon & lime", "Vitamin C, freshness, liver support"),
    ("Beetroot", "Liver support and healthy blood flow"),
    ("Cucumber & watermelon", "Hydration and easy bowels"),
    ("Pineapple & pawpaw", "Natural enzymes that help digestion"),
    ("Turmeric", "Calms inflammation"),
    ("Chia, flax & psyllium", "Gentle fibre for regular bowels"),
    ("Broccoli sprouts", "Sulforaphane — top of my greens list"),
    ("Moringa & ugu", "Iron, calcium and energy"),
    ("Baobab", "Vitamin C and fibre that feeds good gut bacteria"),
    ("Spirulina", "Iron and protein; I use it for mould and yeast support"),
    ("Sea moss", "Minerals for gut and skin (rich in iodine — see safety)"),
    ("Black seed oil", "Gut and immunity (age 3+, 3 times a week)"),
    ("Lemon balm", "Sleep and calm — naturally caffeine-free"),
]
ING_HTML = """<p class="lead">Know what's in your glass. Mix and match these to make your own healing drinks.</p>
<table class="tbl"><tr><th style="width:32%">Ingredient</th><th>Good for</th></tr>""" + "".join(
    f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in INGREDIENTS) + "</table>"

PANTRY = [
    ("Kit", ["Blender", "Fine sieve or nut-milk bag (for juices)", "Glass jars & bottles", "Ice-cube trays (freeze leftovers)",
             "Glass or stainless-steel cups", "Paper straws"]),
    ("Fresh every week", ["Celery, cucumber, spinach, kale", "Green apples, lemons, limes", "Ginger, fresh mint",
                          "Coriander & parsley", "Seasonal fruit: pineapple, mango, pawpaw, watermelon, oranges"]),
    ("Freezer", ["Frozen mango & pineapple", "Frozen berries & blueberries", "Sliced ripe bananas"]),
    ("Pantry", ["Chia & ground flaxseed", "Dried hibiscus (zobo)", "Tiger nuts", "Dates", "Coconut water",
                "Coconut milk", "Rooibos tea", "Dried lemon balm"]),
    ("Powders & extras", ["Spirulina", "Lion's mane", "Moringa", "Baobab", "Turmeric", "Sea moss (dried or gel)",
                          "Black seed oil", "Raw honey or pure maple syrup"]),
]
SEAMOSS_HTML = """<div class="callout gold"><div class="t">How to make sea moss gel</div>
<p>Rinse 30 g dried sea moss very well. Soak in fresh water for 12–24 hours until soft. Rinse again, then blend with 1 cup fresh water until smooth. Store in a glass jar in the fridge for up to 2 weeks. Children: 1 tsp a day; adults: 1 tbsp.</p></div>"""


def tracker():
    rows = "".join(f"<tr><td>{d}</td><td></td><td></td><td></td><td></td></tr>" for d in range(1, 31))
    return f"""<p class="muted small">Write down each drink and how your child felt. Look back after a week — patterns jump out.</p>
<table class="track sip"><tr><th style="width:8%">Day</th><th style="width:30%">Drink</th><th style="width:12%">Amount</th><th>Sleep · tummy · mood</th><th style="width:20%">Notes</th></tr>{rows}</table>"""


MORE = [
    R("Beet, Carrot & Apple Juice", "10 min",
      ["1 small beetroot, peeled", "2 carrots", "1 green apple", "½ lemon, peeled", "Small piece of ginger"],
      ["Wash and chop everything.", "Juice — or blend with ½ cup water and strain.", "Drink fresh."],
      goodfor=["Liver support", "Healthy blood", "Energy"],
      why="A sweet, bright red juice that children love — beetroot supports the liver.",
      tip="Beetroot can turn wee and poo pink. That's normal!", tip_label="Good to know", label="Day 8"),
    R("Pineapple-Ginger Tummy Soother", "5 min",
      ["1 cup pineapple", "½ cucumber", "Small piece of ginger", "½ cup coconut water", "Few mint leaves"],
      ["Blend everything until smooth.", "Strain if you like it smooth.", "Serve cool."],
      goodfor=["Digestion", "Bloating", "Nausea"],
      why="Pineapple has natural enzymes and ginger calms the tummy.", label="Day 9"),
    R("Zobo Cooler (No Sugar)", "20 min + chilling",
      ["1 cup dried hibiscus (zobo) leaves", "6 cups water", "Thumb of ginger, 4 cloves",
       "Pineapple peel (from 1 pineapple)", "4–6 dates (to sweeten)"],
      ["Rinse zobo. Boil with ginger, cloves and pineapple peel for 15 min.", "Add dates, turn off heat, steep 30 min.",
       "Strain well and chill."],
      goodfor=["Antioxidants", "Hydration", "Vitamin C"],
      why="Our favourite Naija drink, made without sugar — naturally caffeine-free.",
      tip="Hibiscus is not recommended in pregnancy. Ask your doctor if you take blood-pressure medicine.",
      tip_label="Safety first", label="Day 10"),
    R("Ugu & Pineapple Green Juice", "10 min",
      ["1 big handful ugu (pumpkin leaves) or spinach", "1½ cups pineapple", "½ cucumber", "½ lime",
       "½ cup water"],
      ["Wash the ugu very well.", "Blend everything, then strain through a cloth.", "Drink fresh."],
      goodfor=["Iron", "Blood building", "Energy"],
      why="Ugu is one of the richest local sources of iron. Pineapple makes it sweet.", label="Day 11"),
    R("Moringa Mango Smoothie", "5 min",
      ["1 cup frozen mango", "½ banana", "½ tsp moringa powder", "1 cup coconut water", "Squeeze of lime"],
      ["Blend everything until smooth.", "Drink fresh."],
      goodfor=["Iron & calcium", "Energy", "Immunity"],
      why="Moringa is an African superfood leaf packed with minerals.",
      tip="Start with ¼ tsp moringa for children — it has a strong taste.", tip_label="Go slowly", label="Day 12"),
    R("Pawpaw Lime Smoothie", "5 min",
      ["1½ cups ripe pawpaw (papaya)", "½ banana", "Juice of ½ lime", "½ cup coconut milk", "1 tsp chia seeds"],
      ["Blend everything until smooth.", "Drink straight away."],
      goodfor=["Digestion", "Constipation", "Skin"],
      why="Pawpaw contains papain, a natural enzyme that helps break down food.", label="Day 13"),
    R("Golden Turmeric Milk (Warm)", "10 min",
      ["1 cup coconut milk (or ½ coconut milk, ½ water)", "½ tsp turmeric", "Pinch of cinnamon & ginger",
       "Pinch of black pepper", "1 tsp honey or maple (optional)"],
      ["Warm everything in a small pan, whisking, for 5 min — do not boil.", "Cool until warm and drink before bed."],
      goodfor=["Calm", "Sleep", "Inflammation"],
      why="A cosy bedtime drink. Black pepper helps the body absorb turmeric.", label="Day 14"),
    R("Kiwi, Spinach & Apple Smoothie", "5 min",
      ["2 kiwis, peeled", "1 handful spinach", "1 green apple", "1 cup water or coconut water", "1 tsp ground flaxseed"],
      ["Blend everything until smooth.", "Drink fresh."],
      goodfor=["Vitamin C", "Immunity", "Bowels"],
      why="Kiwi is one of the best natural helpers for regular bowels.", label="Day 15"),
    R("Baobab Berry Smoothie", "5 min",
      ["1 cup mixed berries", "½ banana", "1 tsp baobab powder", "1 cup coconut milk", "Few ice cubes"],
      ["Blend everything until smooth.", "Drink fresh."],
      goodfor=["Vitamin C", "Good gut bacteria", "Energy"],
      why="Baobab, the African “tree of life” fruit, is rich in prebiotic fibre.", label="Day 16"),
    R("Tiger Nut Milk (Kunu Aya)", "15 min + soaking",
      ["1 cup tiger nuts, soaked overnight", "3 cups water", "3–4 dates", "Small piece of ginger",
       "Pinch of cinnamon"],
      ["Drain the soaked tiger nuts.", "Blend with water, dates, ginger and cinnamon until smooth.",
       "Strain through a cloth. Chill and drink within 2 days."],
      goodfor=["Good gut bacteria", "Dairy-free energy", "Digestion"],
      why="Tiger nuts are tubers, not nuts — a creamy, naturally sweet, school-safe milk.", label="Day 17"),
    R("Carrot, Orange & Ginger Juice", "10 min",
      ["4 carrots", "2 oranges, peeled", "Small piece of ginger", "Pinch of turmeric (optional)"],
      ["Juice everything — or blend with ½ cup water and strain.", "Drink fresh."],
      goodfor=["Immunity", "Skin", "Eyes"],
      why="Full of beta-carotene and vitamin C — a sunshine drink for winter colds.", label="Day 18"),
    R("Cucumber, Mint & Lime Water", "5 min + chilling",
      ["½ cucumber, sliced", "Handful fresh mint", "1 lime, sliced", "1 litre water"],
      ["Put everything in a jug.", "Chill for at least 1 hour.", "Top up with water through the day."],
      goodfor=["Hydration", "Kidneys", "Fresh breath"],
      why="Children who don't like plain water often love “spa water”.", label="Day 19"),
    R("Green Apple, Celery & Parsley Juice", "10 min",
      ["2 green apples", "3 celery sticks", "Handful fresh parsley", "½ lemon, peeled"],
      ["Juice — or blend with ½ cup water and strain.", "Drink fresh, before breakfast."],
      goodfor=["Kidneys", "Gentle cleanse", "Digestion"],
      why="Parsley is one of my traditional cleansing herbs. Apple keeps it sweet.", label="Day 20"),
    R("Coconut Water Refresher", "5 min",
      ["1 cup coconut water", "½ cup fresh orange juice", "Squeeze of lime", "Tiny pinch of sea salt"],
      ["Stir everything together.", "Serve cool."],
      goodfor=["Hydration", "Electrolytes", "After illness"],
      why="A natural sports drink — perfect after a tummy bug or a hot day.", label="Day 21"),
    R("Blueberry Banana Brain Smoothie", "5 min",
      ["1 cup blueberries (wild if you can)", "1 ripe banana", "1 tbsp ground flaxseed", "1 cup coconut milk",
       "¼ tsp lion's mane (optional)"],
      ["Blend everything until smooth.", "Drink fresh."],
      goodfor=["Brain", "Antioxidants", "Focus"],
      why="Wild blueberries are one of my top foods for the brain.", label="Day 22"),
    R("Red Beet & Berry Smoothie", "5 min",
      ["1 small cooked beetroot", "1 cup strawberries", "½ banana", "1 cup coconut water", "Squeeze of lemon"],
      ["Blend everything until smooth.", "Drink fresh."],
      goodfor=["Circulation", "Stamina", "Liver support"],
      why="The berries hide the earthy beet taste — a bright pink treat.", label="Day 23"),
    R("Chia Lemonade", "5 min + 10 min resting",
      ["Juice of 2 lemons", "2 cups water", "1 tbsp chia seeds", "1–2 tsp honey or maple syrup"],
      ["Stir lemon, water and honey together.", "Add chia and stir again.", "Rest 10 min until the seeds swell."],
      goodfor=["Bowels", "Hydration", "Vitamin C"],
      why="Chia seeds are my top tip for constipation — and children love the “bubbles”.", label="Day 24"),
    R("Avocado, Kale & Pear Smoothie", "5 min",
      ["½ avocado", "1 handful kale (stems removed)", "1 ripe pear", "1 cup coconut water", "Squeeze of lime"],
      ["Blend everything until creamy.", "Drink fresh."],
      goodfor=["Healthy fats", "Liver support", "Fibre"],
      why="Creamy and filling — a meal in a glass for busy mornings.", label="Day 25"),
    R("Warm Ginger-Lemon Tonic", "10 min",
      ["1 cup hot water", "3 thin slices fresh ginger", "Juice of ½ lemon", "1 tsp raw honey (age 1+)"],
      ["Steep ginger in hot water for 5 min.", "Add lemon and honey.", "Cool until warm and sip slowly."],
      goodfor=["Immunity", "Nausea", "Colds"],
      why="The first thing to make when someone feels unwell.",
      tip="Use only 1 slice of ginger for young children.", tip_label="Kid tip", label="Day 26"),
    R("Rooibos Orange Iced Tea", "10 min + chilling",
      ["2 rooibos tea bags", "2 cups hot water", "1 orange, sliced", "Few mint leaves", "1 tsp honey (optional)"],
      ["Steep rooibos in hot water for 5 min.", "Add orange, mint and honey.", "Chill and serve over ice."],
      goodfor=["Calm", "Antioxidants", "Skin & eczema"],
      why="Rooibos from South Africa is naturally caffeine-free — a safe “tea” for children.", label="Day 27"),
    R("Pineapple Coriander Cleanse Juice", "5 min",
      ["1½ cups pineapple", "Handful fresh coriander", "½ cucumber", "Juice of ½ lime", "½ cup water"],
      ["Blend everything until smooth.", "Strain if you like.", "Drink fresh."],
      goodfor=["Gentle cleanse", "Digestion", "Hydration"],
      why="Coriander is one of my favourite cleansing herbs — pineapple makes it delicious.", label="Day 28"),
    R("Prune & Pear Smoothie", "5 min + soaking",
      ["4 prunes, soaked in warm water 10 min", "1 ripe pear", "½ banana", "1 cup coconut milk", "1 tsp chia seeds"],
      ["Blend everything (with the soaking water) until smooth.", "Drink in the morning."],
      goodfor=["Constipation", "Fibre", "Gut"],
      why="Prunes and pears are gentle, natural helpers for stuck tummies.", label="Day 29"),
    R("Rainbow Celebration Smoothie", "10 min",
      ["Layer 1: 1 cup mango blended with coconut water", "Layer 2: 1 cup strawberries blended with banana",
       "Layer 3: 1 kiwi + handful spinach blended with apple", "Clear glasses, paper straws"],
      ["Blend each layer separately.", "Pour slowly into glasses, one layer at a time.",
       "Serve with a straw and a big cheer!"],
      goodfor=["Celebration", "Vitamins", "Fun"],
      why="Thirty days of gentle healing — time to celebrate with a rainbow!", label="Day 30"),
]

CAL = ["Daily Detox Smoothie", "Boosted Detox Smoothie", "Sea moss gut soother", "Lemon balm bedtime tea",
       "Morning celery juice", "Watermelon cucumber cooler", "Broccoli sprout mango", "Beet, carrot & apple",
       "Pineapple-ginger soother", "Zobo cooler", "Ugu & pineapple juice", "Moringa mango", "Pawpaw lime",
       "Golden turmeric milk", "Kiwi spinach apple", "Baobab berry", "Tiger nut milk", "Carrot orange ginger",
       "Cucumber mint water", "Apple celery parsley", "Coconut water refresher", "Blueberry brain smoothie",
       "Beet & berry", "Chia lemonade", "Avocado kale pear", "Ginger-lemon tonic", "Rooibos iced tea",
       "Pineapple coriander", "Prune & pear", "Rainbow celebration"]

CLOSING_HTML = """
<p class="lead">Thirty gentle glasses. Thirty small acts of love for your child's body.</p>
<div class="grid2">
 <div class="box"><h3>What next?</h3><ul>
  <li>Keep your family's favourite drinks in the weekly routine.</li>
  <li>Return to the Daily Detox Smoothie as your everyday base.</li>
  <li>Look back at your tracker — what changed?</li></ul></div>
 <div class="box"><h3>Remember</h3><ul>
  <li>Slow and steady is the healing way.</li>
  <li>Always check with your doctor before herbs and supplements.</li>
  <li>Water is still the best drink of all.</li></ul></div>
</div>
<div class="sign" style="margin-top:6mm">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div>
<p class="disclaimer" style="margin-top:8mm">© Tris Eliverson. All rights reserved. For personal use only — please do not share or resell. This book shares recipes and ideas from personal experience and is not medical advice. Juices and herbs can interact with medicines. Always ask a qualified health professional before giving herbs or supplements to children, or if you are pregnant or breastfeeding. No honey for babies under 1 year.</p>
"""


def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def pages():
    out = []

    def add(kind, data, toc=None):
        out.append((kind, data, toc))

    add("cover", dict(series="Bonus Book 2", title=BOOK3, logo="sips",
        subtitle="The 30-Day Gentle Detox & Juicing Plan for the Whole Family",
        tagline="One gentle glass a day.", free=FREE, badge=("30", "detox<br>recipes"), author=AUTHOR))
    add("text", dict(kicker="Welcome", title="One gentle glass a day", html=WELCOME_HTML), "One gentle glass a day")
    add("toc", None)
    add("text", dict(kicker="Before you start", title="The gentle way to detox", html=DETOX_RULES), "The gentle way to detox")
    add("text", dict(kicker="Know your ingredients", title="What's in your glass", html=ING_HTML), "What's in your glass")
    add("grocery", dict(kicker="Get ready", title="Detox pantry & kit",
        intro="Stock these once and you can make any drink in this book.", cats=PANTRY, after=SEAMOSS_HTML),
        "Detox pantry & kit")
    cells = [dict(day=i + 1, meals=[("d", "S", n)]) for i, n in enumerate(CAL)]
    weeks = [cells[i:i + 7] for i in range(0, 30, 7)]
    weeks[-1] += [None] * (7 - len(weeks[-1]))
    add("calendar", dict(kicker="Your month at a glance", title="30 healing sips", weeks=weeks, month=True, one=True, col="Drink"),
        "Your month at a glance")
    mine = lambda t: t and t.replace("the author's", "my").replace("The author's", "My")
    drinks = [dict(r, why=mine(r.get("why"))) for r in DETOX] + MORE
    for i, trio in enumerate(chunks(drinks, 3)):
        add("two", dict(kind="detox", recipes=trio, small=True), "The 30 drinks" if i == 0 else None)
    add("text", dict(kicker="Printable", title="30-day sip tracker", html=tracker(), white=True), "30-day sip tracker")
    add("text", dict(kicker="You did it", title="Thirty days of gentle healing", html=CLOSING_HTML),
        "Thirty days of gentle healing")

    toc = [(t, i + 1) for i, (_, _, t) in enumerate(out) if t]
    for kind, data, _ in out:
        if kind == "toc":
            data = dict(kicker="Inside this book", title="Contents", items=toc)
        yield BOOK3, kind, data
