"""Design preview: a handful of sample pages from each of the 3 books, for approval."""

BOOK1 = "Healing Plates"
BOOK2 = "Healing Lunch Box"
BOOK3 = "Healing Sips"
AUTHOR = "Stella Efionayi"
MARKS = {BOOK1: "plates", BOOK2: "box", BOOK3: "sips"}
FREE = ["Gluten", "Dairy", "Corn", "Egg", "Caffeine", "Tuna", "Pork"]

PHOTO = """<div style="width:52mm;height:52mm;border-radius:50%;margin:0 auto 4mm;border:2.5mm solid #E3A12F;
background:#F2E6D2;display:flex;align-items:center;justify-content:center;text-align:center;color:#6E665B;
font-weight:800;font-size:10pt">YOUR PHOTO<br>GOES HERE</div>"""

day1 = dict(
    week=1, day=1,
    quote="“Small changes, one plate at a time. You are doing better than you think.”",
    b=dict(name="Boiled Yam with Ugu & Tomato Sauce", time="30 min",
           ing=["½ medium yam, peeled & sliced", "2 cups ugu (or spinach), chopped", "3 fresh tomatoes, chopped",
                "1 onion, sliced", "2 tbsp unrefined red palm oil", "¼ tsp ground crayfish (optional)", "Pinch of salt"],
           steps=["Boil the yam in salted water for 15–20 min until soft.",
                  "Warm the palm oil gently — don't let it smoke. Add onion, cook 2 min.",
                  "Add tomatoes and crayfish. Cook 5 min.",
                  "Stir in the ugu, cook 2 min, then turn off the heat.",
                  "Spoon the sauce over the yam."],
           why="Yam gives slow, steady energy. Ugu is rich in iron and magnesium.",
           tip="No yam? Use sweet potato. No ugu? Use spinach, kale or sukuma wiki."),
    l=dict(name="Okro Soup with Chicken & Pounded Yam", time="40 min",
           ing=["500 g chicken pieces", "15 fresh okro, chopped", "1 cup ugu or spinach", "1 onion, 2 ata rodo peppers",
                "1 tbsp ground crayfish", "2 tbsp red palm oil, salt", "Pounded yam or amala, to serve"],
           steps=["Season chicken with onion and salt. Cook in 2 cups water for 20 min.",
                  "Add palm oil, pepper and crayfish. Cook 5 min.",
                  "Add okro and cook only 3–4 min so it stays green.",
                  "Stir in the greens and turn off the heat.",
                  "Serve with pounded yam."],
           why="Okro is soft and gentle on the gut and helps keep things moving.",
           tip="Picky eater? Blend the okro smooth so there are no “slimy bits” to see.", tip_label="Kid tip"),
    d=dict(name="Coriander Pepper Fish & Green Plantain", time="35 min",
           ing=["4 small mackerel (titus) or tilapia", "3 green (unripe) plantains", "1 handful fresh coriander",
                "2 garlic cloves, 1 small onion", "1 scotch bonnet (skip for kids)", "1 tbsp olive oil, juice of 1 lemon, salt"],
           steps=["Blend coriander, garlic, onion, pepper, oil, lemon and salt to a paste.",
                  "Rub the paste over the fish. Rest 15 min.",
                  "Bake on parchment at 200 °C / 400 °F for 20–25 min (no foil).",
                  "Meanwhile, peel and boil the plantains for 20 min.",
                  "Serve with sliced cucumber."],
           why="Small fish carry far less mercury than tuna. Green plantain feeds good gut bacteria."),
)

week1 = [
    ("Yam & ugu sauce", "Okro soup & pounded yam", "Coriander pepper fish"),
    ("Millet hausa koko", "Jollof rice & chicken", "Chicken pepper soup"),
    ("Plantain & sweet potato hash", "Beans & ripe plantain", "Roast chicken & root veg"),
    ("Buckwheat banana pancakes", "Egusi soup & amala", "Sukuma wiki & beef"),
    ("Yam porridge (asaro)", "Sweet potato lentil soup", "Egg-free moi moi & salad"),
    ("Coconut rice porridge", "Waakye & fish stew", "Turkey meatballs & lentil pasta"),
    ("Avocado sweet potato toast", "Kenyan pilau & kachumbari", "Green plantain porridge"),
]

FREE_FROM_HTML = """
<p class="lead">Many “safe-looking” foods hide gluten, dairy, corn or caffeine. Here is where they hide — especially in our African kitchens.</p>
<table class="tbl">
<tr><th style="width:24%">Avoid</th><th>Where it hides</th></tr>
<tr><td>Gluten</td><td>Bread, semovita, wheat swallow, chin chin, puff-puff, meat pie, pasta, <b>Milo, Bournvita &amp; Ovaltine</b> (barley malt), soy sauce, many stock cubes</td></tr>
<tr><td>Dairy</td><td>Peak/Three Crowns milk, butter, cheese, yogurt, ice cream, whey, casein, “non-dairy” creamers that contain casein</td></tr>
<tr><td>Corn</td><td><b>Pap/ogi/akamu</b>, kenkey, banku, tuwo masara, ugali, pap (SA), custard powder, cornflour, popcorn, <b>baking powder</b> (corn starch), glucose syrup, xanthan gum, many gluten-free flour blends</td></tr>
<tr><td>Egg</td><td>Cakes, mayonnaise, some pasta, egg rolls, meat pies, many “gluten-free” breads and pancake mixes</td></tr>
<tr><td>Caffeine</td><td>Tea (black &amp; green), coffee, matcha, cola, energy drinks, <b>kola nut</b>, chocolate &amp; cocoa, Milo</td></tr>
<tr><td>Tuna</td><td>Canned tuna, tuna salad, some sandwiches, sushi and fish pies</td></tr>
<tr><td>Pork</td><td>Bacon, ham, sausages, lard, gelatine (sweets &amp; jelly), some suya</td></tr>
</table>
<div class="callout gold"><div class="t">The 10-second label rule</div>
<p>Turn the pack over. Read the ingredients <b>every time</b> — brands change their recipes. If you can't pronounce it, or it says “may contain”, leave it on the shelf.</p></div>
"""

GUT_HTML = """
<p class="lead">When the gut is out of balance, everything feels harder — sleep, moods, toilet troubles and picky eating. These 5 steps are the heart of this book.</p>
<div class="step"><div class="n">1</div><div><h3>Remove the irritants</h3>
<p>Dairy, gluten, fried food, cookies, bread, processed food, refined sugar, corn, pap and garri. <b>Swap:</b> dairy → coconut; flour → tapioca, potato or buckwheat flour.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Support digestion with healing nutrients</h3>
<p>Zinc and magnesium from leafy vegetables and pumpkin seeds.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Repair the gut</h3>
<p>Keep the gut hydrated and nourished: berries, psyllium husk, okro stew, egusi soup (no tripe or intestine).</p></div></div>
<div class="step"><div class="n">4</div><div><h3>Knock down the bad bugs</h3>
<p>Garlic, onions, rosemary, thyme, potatoes, carrots, courgette, pumpkin, coconut yogurt, green banana and gluten-free oats.</p></div></div>
<div class="step"><div class="n">5</div><div><h3>[ Step 5 — waiting for your notes ]</h3>
<p class="muted">Send me the fifth step and it goes here.</p></div></div>
<div class="callout terra"><div class="t">Picky eating is not bad behaviour</div>
<p>A child who eats only three foods is often a child whose nervous system feels unsafe. Go gently. One new food at a time, next to a food they already love.</p></div>
"""

BRANDS = [
    dict(name="Nigeria", rows=[("Swallows", "Ola-Ola & Iyan Ado pounded yam flour, plantain flour"),
                               ("Rice", "Ofada, Mama Gold, Royal Stallion"),
                               ("Dairy-free", "Kara or Chaokoh coconut milk, homemade tigernut milk (kunu aya)"),
                               ("Oils", "Figaro extra virgin olive oil, unrefined red palm oil"),
                               ("Shops", "Spar, Prince Ebeano, Justrite, Grand Square, local markets")]),
    dict(name="Ghana", rows=[("Swallows", "Pure cassava or plantain fufu flour (no corn), yam flour"),
                             ("Dairy-free", "Coconut milk, homemade tigernut milk"),
                             ("Drinks", "Sobolo (no sugar), ginger, coconut water"),
                             ("Shops", "Melcom, MaxMart, Shoprite, Makola market")]),
    dict(name="Kenya", rows=[("Flours", "Pure wimbi (finger millet) or sorghum flour — check no maize is added"),
                             ("Dairy-free", "Kara coconut milk, coconut cream"),
                             ("Drinks", "Ginger-lemongrass “chai” without tea leaves"),
                             ("Shops", "Naivas, Quickmart, Carrefour, Chandarana")]),
    dict(name="South Africa", rows=[("Dairy-free", "Oh Mylk, Alpro, Rhodes coconut milk"),
                                    ("Drinks", "Freshpak Rooibos (naturally caffeine-free)"),
                                    ("Pantry", "Nature's Choice, Bob's Red Mill gluten-free"),
                                    ("Shops", "Woolworths, Checkers, Dis-Chem, Faithful to Nature")]),
    dict(name="United Kingdom", rows=[("Dairy-free", "Koko, Alpro, The Coconut Collaborative, Violife"),
                                      ("African foods", "Tropical Sun yam, plantain & cassava flours"),
                                      ("Sauces", "Free & Easy"),
                                      ("Shops", "Tesco & Sainsbury's Free From, Holland & Barrett, African shops")]),
    dict(name="USA & Canada", rows=[("Flours", "Otto's Naturals cassava flour, Bob's Red Mill gluten-free"),
                                    ("Dairy-free", "So Delicious, Cocojune, Daiya, Earth's Own"),
                                    ("Snacks", "Enjoy Life, MadeGood"),
                                    ("Shops", "Whole Foods, Loblaws (PC Free From), Thrive Market")]),
]

lunchboxes = [
    dict(label="Day 1", name="Sweet Potato Chicken Bites Box", region="Nut-free", time="Prep the night before",
         ing=["6–8 sweet potato chicken bites", "Cucumber sticks", "Mango slices", "Small pot of coconut yogurt (dip)"],
         steps=["Mash 1 boiled sweet potato with 1 cup shredded cooked chicken, pinch of salt & thyme.",
                "Stir in 2 tbsp tapioca flour. Roll into small balls and flatten.",
                "Bake at 200 °C / 400 °F for 20 min. Cool and refrigerate.",
                "Morning: pack the bites, cucumber, mango and the dip."],
         why="Protein + slow carbs keep energy steady through the school day.",
         tip="Pack one food they already love next to the new one. No pressure.", tip_label="Parent tip"),
    dict(label="Day 2", name="Mini Jollof Rice & Chicken Box", region="Nut-free", time="Use leftovers",
         ing=["1 cup leftover jollof rice", "3–4 pieces baked chicken", "Carrot sticks", "Watermelon cubes"],
         steps=["Warm the jollof rice and chicken in the morning.",
                "Pack into a thermos to keep warm until lunch.",
                "Add carrot sticks and watermelon in a separate section."],
         why="A familiar home favourite makes lunchtime feel safe for sensitive eaters.",
         tip="Cook extra jollof at dinner — tomorrow's lunch is already done.", tip_label="Time saver"),
]

detox = [
    dict(label="Day 1", name="The Daily Detox Smoothie", region="Author's recipe", time="5 min",
         ing=["1 celery stick", "½ green apple", "Handful of blueberries", "1 tbsp fresh coriander (cilantro)",
              "1 tbsp fresh parsley", "1 cup water (or more)"],
         steps=["Wash everything well.", "Blend until smooth.", "Drink fresh, in the morning."],
         goodfor=["Gentle daily cleanse", "Bowels", "Hydration", "Antioxidants"],
         why="Celery is the base. Apple adds fibre. Coriander and parsley are traditional cleansing herbs.",
         tip="Children: start with half a cup. Detox should be slow and gentle.", tip_label="Go slowly"),
    dict(label="Day 2", name="Boosted Detox Smoothie", region="Author's recipe", time="5 min",
         ing=["Everything from Day 1", "¼ tsp spirulina powder", "¼ tsp lion's mane powder", "Brahmi (bacopa) — adults only"],
         steps=["Make the Day 1 smoothie.", "Add the spirulina and lion's mane.", "Blend again and drink fresh."],
         goodfor=["Brain & focus", "Mould & yeast support", "Energy"],
         why="Spirulina is rich in iron and protein. Lion's mane is a mushroom traditionally used for focus.",
         tip="Ask your child's doctor before adding any herb or supplement, especially with medication.",
         tip_label="Safety first"),
]


def pages():
    yield BOOK1, "cover", dict(series="The 30-Day Allergy-Free Family Meal Plan", title=BOOK1, logo="plates",
        subtitle="Breakfast, lunch & dinner free from gluten, dairy, corn, egg, caffeine & tuna",
        tagline="Finally… food the whole family can eat.",
        free=FREE, badge=("90", "family<br>meals"),
        author=AUTHOR)
    yield BOOK1, "text", dict(kicker="Welcome", title="You are not alone",
        html=PHOTO + """<div class="letter">
<p>If you are holding this book, I know a little of your story. The child who eats only three foods. The nights that don't end. The family members who say “just give him bread, he'll be fine.” The quiet worry when the words haven't come yet.</p>
<p>I have stood in that kitchen too. <b>[ Your story goes here — a few lines in your own words. ]</b></p>
<p>This book is the one I wish I had. No long science. No fancy ingredients you can't find. Just real food from our homes — yam, plantain, okro, rice, beans — made safe for your family, one day at a time.</p>
<p>You don't have to be perfect. You just have to start.</p>
<div class="sign">With love, Stella Efionayi</div></div>""")
    yield BOOK1, "text", dict(kicker="Know before you shop", title="Where allergens hide", html=FREE_FROM_HTML)
    yield BOOK1, "text", dict(kicker="Restoring the gut", title="5 steps to healing the gut", html=GUT_HTML)
    yield BOOK1, "calendar", dict(kicker="Your month at a glance", title="Week 1",
        weeks=[[dict(day=i + 1, meals=[("b", "B", w[0]), ("l", "L", w[1]), ("d", "D", w[2])]) for i, w in enumerate(week1)]])
    yield BOOK1, "grocery", dict(kicker="Tick as you shop", title="Week 1 shopping list",
        intro="Everything for Days 1–7. Cross off what you already have.",
        cats=[("Vegetables & greens", ["Ugu or spinach (3 bunches)", "Okro (15)", "Fresh tomatoes (8)", "Onions (6)", "Sweet potatoes (4)", "Cucumber (2)", "Garlic (1 bulb)"]),
              ("Roots & fruit", ["Yam (1 large)", "Green plantain (4)", "Ripe plantain (4)", "Blueberries", "Mango (2)", "Lemons (3)"]),
              ("Protein", ["Chicken (1.5 kg)", "Mackerel or tilapia (4 small)", "Beef (500 g)", "Turkey mince (500 g)", "Brown or black-eyed beans (2 cups)"]),
              ("Pantry", ["Unrefined red palm oil", "Extra virgin olive oil", "Ground crayfish", "Buckwheat flour", "Tapioca flour", "Millet", "Rice", "Coconut milk (2 tins)"]),
              ("Herbs & spices", ["Fresh coriander", "Thyme", "Ata rodo / scotch bonnet", "Curry powder (no fillers)", "Sea salt"])])
    yield BOOK1, "day", day1
    yield BOOK1, "brands", dict(kicker="Make shopping easier", title="Allergy-friendly brands near you",
        intro="Always read the label — brands can change their recipes. Many gluten-free products still contain corn or egg.",
        regions=BRANDS)
    yield BOOK2, "cover", dict(series="Bonus Book 1", title=BOOK2, logo="box",
        subtitle="30 Days of Allergy-Free School Lunches & Snacks Kids Will Actually Eat",
        tagline="Nut-free and school-safe.",
        free=FREE + ["Nut"], badge=("30", "lunch<br>boxes"),
        author=AUTHOR)
    yield BOOK2, "two", dict(kind="box", recipes=lunchboxes)
    yield BOOK3, "cover", dict(series="Bonus Book 2", title=BOOK3, logo="sips",
        subtitle="The 30-Day Gentle Detox & Juicing Plan for the Whole Family",
        tagline="One gentle glass a day.",
        free=FREE, badge=("30", "detox<br>recipes"),
        author=AUTHOR)
    yield BOOK3, "two", dict(kind="detox", recipes=detox)
