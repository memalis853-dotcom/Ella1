"""Healing Celebrations — Bonus Book 4: birthday cake, party food & survival guide."""
from plates_days import TREATS
from preview import AUTHOR, FREE, treats
from week1 import BOOK5, CAKE, CAKE_TIPS, NAIJA_RECIPES, PARTY, PARTY_HTML, R

MARKS = {BOOK5: "party"}

WELCOME_HTML = """<div class="author-photo small"><img src="img/author.webp" alt="Tris Eliverson"></div>
<div class="letter">
<p class="hello">Dear Mama, dear Papa,</p>
<p>Birthdays, owambes, Christmas, Eid, school parties — they should be full of joy. But when your child has allergies, they can be full of worry instead. Will there be anything they can eat? Will they feel left out?</p>
<p>This little book is my answer. A real birthday cake your child can blow candles out on. Party food the whole room will enjoy — not “special” food that looks different. And a simple plan for every party, church event and day out.</p>
<p>Every recipe is free from gluten, dairy, corn, eggs, caffeine, tuna, pork, processed sugar and nuts.</p>
<p class="heart">Every child deserves a slice. ♥</p>
<div class="sign">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div></div>"""

NEW = [
    R("Carob Birthday Cupcakes", "45 min · makes 12",
      ["1 batch Celebration Cake batter (see the cake page)", "3 tbsp carob powder (add to the dry ingredients)",
       "Frosting: cream from 2 chilled tins coconut milk", "2 tbsp carob powder + 1 tbsp pure maple syrup",
       "Berries or coconut flakes, to decorate"],
      ["Heat oven to 180 °C / 350 °F. Line a muffin tin with 12 cases.",
       "Make the cake batter, adding the carob to the dry ingredients.", "Fill the cases ⅔ full. Bake 18–20 min. Cool.",
       "Whisk coconut cream, carob and maple until fluffy.", "Pipe or spread on top and decorate."],
      why="Chocolate-style cupcakes with no cocoa, caffeine, dairy, egg or nuts.", label="Party"),
    R("Party Jollof Rice (serves 12)", "1 hr 15 min",
      ["6 cups long-grain parboiled rice", "12 tomatoes, 6 red peppers, 2 onions, 2 scotch bonnets — blended",
       "4 tbsp tomato paste, ½ cup olive oil", "2 tsp thyme, 2 tsp pure curry powder, 4 bay leaves",
       "4 tsp Healing Seasoning Mix, salt", "6 cups chicken stock"],
      ["Cook the blend in a large pot 20 min until thick.", "Fry tomato paste in the oil 3 min, add the blend and spices. Cook 10 min.",
       "Add stock and washed rice. Cover tightly with parchment and a lid.",
       "Cook on low 30–35 min, stirring gently once.", "Let it rest 10 min, then fluff and serve."],
      why="The heart of every Naija party — made without stock cubes or MSG.",
      tip="For the smoky “party” taste, let the bottom catch very slightly at the end.", tip_label="Party secret",
      label="Party"),
    R("Baked Peppered Chicken", "1 hr",
      ["2 kg chicken pieces", "2 tsp Healing Seasoning Mix, 1 tsp thyme, salt", "4 red peppers, 1 scotch bonnet, 1 onion — blended",
       "3 tbsp olive oil", "1 tsp paprika"],
      ["Season chicken and bake at 200 °C / 400 °F for 35 min.", "Cook the pepper blend in oil with paprika 10 min until thick.",
       "Toss the baked chicken in the pepper sauce.", "Return to the oven 10 min to glaze."],
      why="Party chicken that's baked, not deep-fried — but still saucy and delicious.", label="Party"),
    R("Mini Moi Moi Cups", "1 hr 15 min · makes 18",
      ["3 cups black-eyed beans, soaked & peeled", "2 red peppers, 1 scotch bonnet, 1 onion", "4 tbsp red palm oil",
       "1 tbsp crayfish, 2 tsp seasoning mix, salt", "About 1½ cups warm water", "Silicone cupcake cases"],
      ["Blend beans, peppers and onion with water until very smooth.", "Stir in oil, crayfish, seasoning and salt.",
       "Fill silicone cases ⅔ full and set in a steamer.", "Steam 35–40 min until firm.", "Cool slightly and pop out."],
      why="Egg-free, perfectly portioned and easy for little hands at a party.", label="Party"),
]

RECIPES = NEW[:1] + NEW[1:] + [PARTY[0], NAIJA_RECIPES[0], PARTY[2], PARTY[3], PARTY[1],
                                treats[0], TREATS[2][1], TREATS[4][1]]
for r in RECIPES:
    r["label"] = "Party"

MENUS_HTML = """
<p class="lead">Three ready-made party menus. Mix and match — every dish is in this book.</p>
<div class="grid3">
 <div class="box"><h3>Kids' birthday</h3><ul>
  <li>Celebration Vanilla Berry Cake</li><li>Carob Birthday Cupcakes</li><li>Nut-Free Chicken Suya Skewers</li>
  <li>Rainbow Fruit Wands</li><li>Coconut Mango Ice Pops</li><li>Zobo Party Punch</li></ul></div>
 <div class="box"><h3>Naija party &amp; owambe</h3><ul>
  <li>Party Jollof Rice</li><li>Baked Peppered Chicken</li><li>Mini Moi Moi Cups</li>
  <li>Baked Plantain Puff-Puff Bites</li><li>Crunchy Cassava Chin Chin</li><li>Zobo Party Punch</li></ul></div>
 <div class="box"><h3>Christmas, Eid &amp; holidays</h3><ul>
  <li>Party Jollof Rice</li><li>Baked Peppered Chicken</li><li>Suya Skewers</li>
  <li>Strawberry Coconut Cheesecake Cups</li><li>Carob Fudge Bites</li><li>Rainbow Fruit Wands</li></ul></div>
</div>
<h2>Make-ahead plan</h2>
<div class="grid3">
 <div class="box"><h3>One week before</h3><ul><li>Bake and freeze the cake or cupcakes (un-iced).</li><li>Make chin chin and fudge bites — store airtight.</li><li>Make a batch of Healing Seasoning Mix.</li></ul></div>
 <div class="box"><h3>The day before</h3><ul><li>Steam the moi moi cups.</li><li>Make zobo punch and chill.</li><li>Marinate the chicken. Freeze ice pops.</li><li>Chill coconut milk for frosting.</li></ul></div>
 <div class="box"><h3>On the day</h3><ul><li>Cook jollof and bake the chicken.</li><li>Bake puff-puff bites.</li><li>Frost the cake, make fruit wands.</li><li>Breathe — and enjoy the party!</li></ul></div>
</div>
"""

HOST_LETTER = """<p class="muted">Print, fill in and send to the party host a few days before. Keep a copy in your bag.</p>
<div class="cutcard" style="padding:7mm 8mm">
<p>Dear <span class="fill"></span>,</p>
<p>Thank you so much for inviting <span class="fill"></span> to the party — we are really looking forward to it!</p>
<p>My child has food allergies and cannot eat: &nbsp;☐ Gluten (wheat) &nbsp;☐ Dairy (milk) &nbsp;☐ Corn &nbsp;☐ Egg &nbsp;☐ Caffeine &nbsp;☐ Tuna &nbsp;☐ Pork &nbsp;☐ Nuts &nbsp;☐ Processed sugar</p>
<p>Other: <span class="fill" style="min-width:130mm"></span></p>
<p>To make it easy for you, I will bring: <span class="fill" style="min-width:90mm"></span></p>
<p>Could you please let me know what food will be served, so I can make sure my child has something similar? It means a lot that they can join in like everyone else.</p>
<p>If you have any questions, please call me on: <span class="fill" style="min-width:70mm"></span></p>
<p style="margin-top:5mm">Thank you for helping keep my child safe and happy! ♥</p>
<p style="margin-top:6mm">From: <span class="fill"></span></p>
</div>"""

CLOSING_HTML = """
<p class="lead">Every candle blown out, every party joined, every “yes, you can have that” — these are the moments we heal for.</p>
<div class="grid2">
 <div class="box"><h3>Remember</h3><ul>
  <li>Freeze cake slices for surprise school birthdays.</li>
  <li>Always pack a “party box” — just in case.</li>
  <li>Share the host letter and allergy card ahead of time.</li></ul></div>
 <div class="box"><h3>The whole series</h3><ul>
  <li><b>Healing Plates</b> — the 30-day family meal plan</li>
  <li><b>Healing Lunch Box</b> — 30 days of school lunches</li>
  <li><b>Healing Sips</b> — 30 gentle detox drinks</li>
  <li><b>Healing Printables</b> — cards, trackers &amp; planners</li></ul></div>
</div>
<div class="sign" style="margin-top:6mm">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div>
<p class="disclaimer" style="margin-top:8mm">© Tris Eliverson. All rights reserved. For personal use only — please do not share or resell. This book shares recipes and ideas from personal experience and is not medical advice. Always check food labels, and always supervise children with food allergies at parties.</p>
"""


def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def pages():
    out = []

    def add(kind, data, toc=None):
        out.append((kind, data, toc))

    n_recipes = len(RECIPES) + 1
    add("cover", dict(series="Bonus Book 4", title=BOOK5, logo="party",
        subtitle="A real birthday cake, party food & a survival guide for parties, church events and eating out",
        tagline="Every child deserves a slice.", free=FREE + ["Nut"], badge=(str(n_recipes), "party<br>recipes"),
        author=AUTHOR))
    add("text", dict(kicker="Welcome", title="Every child deserves a slice", html=WELCOME_HTML), "Every child deserves a slice")
    add("toc", None)
    add("cards", dict(kicker="The star of the party", title="A real birthday cake", kind="treat", recipes=[CAKE],
        intro="Every child deserves to blow out candles on a cake they can actually eat.", after=CAKE_TIPS),
        "A real birthday cake")
    for i, trio in enumerate(chunks(RECIPES, 3)):
        add("two", dict(kind="treat", recipes=trio, small=True), "Party food & treats" if i == 0 else None)
    add("text", dict(kicker="Plan it", title="Party menus & make-ahead plan", html=MENUS_HTML), "Party menus & make-ahead plan")
    add("text", dict(kicker="Be prepared", title="Party survival guide", html=PARTY_HTML), "Party survival guide")
    add("text", dict(kicker="Printable", title="Letter to the party host", html=HOST_LETTER, white=True), "Letter to the party host")
    add("text", dict(kicker="Celebrate", title="Here's to every celebration", html=CLOSING_HTML), "Here's to every celebration")

    toc = [(t, i + 1) for i, (_, _, t) in enumerate(out) if t]
    for kind, data, _ in out:
        if kind == "toc":
            data = dict(kicker="Inside this book", title="Contents", items=toc)
        yield BOOK5, kind, data
