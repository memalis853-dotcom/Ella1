"""Healing Lunch Box — Bonus Book 1: 30 days of school lunches & snacks."""
import week1
from preview import AUTHOR, BOOK2, FREE
from week1 import LUNCH_RULES, LUNCHBOXES, NAIJA_HTML, NAIJA_RECIPES, R, SNACKS_HTML

MARKS = {BOOK2: "box"}
FREE_LB = FREE + ["Nut"]

WELCOME_HTML = """<div class="author-photo small"><img src="img/author.webp" alt="Tris Eliverson"></div>
<div class="letter">
<p class="hello">Dear Mama, dear Papa,</p>
<p>I know the feeling of packing a lunch box and wondering if it will come home untouched. I know the worry of sending your child to school with allergies, and the little ache when everyone else has biscuits and crisps.</p>
<p>These 30 lunch boxes are the ones that work in my home. They are safe, simple and fun — familiar Nigerian favourites next to nuggets, pinwheels and pizza bites that children are proud to open in front of their friends.</p>
<p>Every box is free from gluten, dairy, corn, eggs, caffeine, tuna, pork, processed sugar <b>and nuts</b>, so it is school-safe.</p>
<p class="heart">Pack it with love. That's the most important ingredient. ♥</p>
<div class="sign">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div></div>"""

PICKY_HTML = """
<p class="lead">If your child eats only a few foods, you are not doing anything wrong. Many children — especially autistic children — feel safer with food that is predictable. These gentle tricks help.</p>
<div class="grid2">
 <div class="box"><h3>1. Food chaining</h3><p>Start from a food they love and change <b>one small thing</b> at a time:<br>shop nuggets → homemade nuggets → nuggets with paprika → chicken strips → chicken skewers.</p></div>
 <div class="box"><h3>2. Same food, new shape</h3><p>Cut sandwiches, fruit and flatbread with cookie cutters. Stars, hearts and dinosaurs make the same food feel new.</p></div>
 <div class="box"><h3>3. The learning portion</h3><p>Put one tiny piece of a new food in its own section. No need to eat it — just let it sit there. It can take 15 or more tries.</p></div>
 <div class="box"><h3>4. Respect the senses</h3><p>Keep foods separate, offer dips, and notice what your child prefers: crunchy or soft, warm or cold, smooth or lumpy.</p></div>
 <div class="box"><h3>5. Let them help</h3><p>Children eat what they choose, wash, pack or build. Offer two choices: “Pinwheels or nuggets tomorrow?”</p></div>
 <div class="box"><h3>6. Praise the try</h3><p>Celebrate touching, smelling or licking a new food — not just eating it. Use the “I tried it!” chart in Healing Printables.</p></div>
</div>
<div class="callout terra"><div class="t">When to ask for extra help</div>
<p>If your child eats fewer than 20 foods, is losing weight, gags or vomits often, or mealtimes cause great distress, ask your doctor about a feeding therapist. You don't have to do this alone.</p></div>
"""

PANTRY = [
    ("Batch-cook & freeze", ["Chicken nuggets", "Mini meatballs", "Baked akara bites", "Mini moi moi cups",
                             "Mama's chicken, potato & carrot soup", "Banana bread bites"]),
    ("Carbs", ["Rice & rice pasta", "Cassava flour (for flatbreads)", "Easy Buckwheat Bread", "Sweet potatoes",
               "Ripe & green plantains", "Plain rice crackers (check: no corn)"]),
    ("Fruit", ["Apples, bananas, grapes", "Mango, pineapple, watermelon", "Berries", "Oranges & tangerines"]),
    ("Vegetables", ["Cucumber, carrots, peppers", "Cherry tomatoes", "Lettuce", "Peas & broccoli"]),
    ("Dips", ["Coconut yogurt", "Hummus (contains sesame)", "Sunflower-seed butter", "Guacamole",
              "Sunshine Ketchup (no sugar)"]),
    ("Crunch", ["Baked plantain chips (ipekere)", "Crunchy chickpeas", "Pumpkin & sunflower seeds",
                "Toasted coconut chips"]),
    ("Kit", ["Bento box with sections", "Small thermos", "Ice pack", "Silicone cupcake cases",
             "Cookie cutters", "Paper straws & blunt picks"]),
]

MORE = [
    R("Mama's Soup Thermos", "Use frozen soup",
      ["1 portion Mama's Chicken, Potato & Carrot Soup", "2 slices buckwheat bread, cut into soldiers",
       "Cucumber sticks", "Apple slices + squeeze of lemon"],
      ["Heat the soup until piping hot.", "Warm the thermos with boiling water for 5 min, empty, then fill with soup.",
       "Pack the bread soldiers, cucumber and apple separately."],
      why="My child's favourite soup — all the vegetables blended in, so nothing to pick out.",
      tip="Freeze soup in single portions on Sunday. Lunch is ready all week.", tip_label="Time saver",
      label="Day 8", region="Author's family favourite"),
    R("Mini Moi Moi & Dodo Box", "Prep ahead",
      ["3 egg-free mini moi moi cups (steamed in silicone cases)", "Handful baked dodo bites", "Cucumber coins",
       "Watermelon cubes"],
      ["Steam moi moi in silicone cases 35–40 min. Cool and refrigerate (or freeze).",
       "Bake ripe plantain cubes in a little coconut oil at 200 °C / 400 °F for 20 min.",
       "Pack moi moi, dodo, cucumber and watermelon in separate sections."],
      why="A taste of home — beans set perfectly without egg and are full of plant protein.", label="Day 9"),
    R("Rainbow Pasta Salad Pot", "15 min",
      ["1 cup cooked rice pasta (cold)", "½ cup cooked chicken, diced", "Cucumber, cherry tomatoes, pepper — diced",
       "1 tbsp olive oil + squeeze of lemon + pinch of salt", "Grapes (halved for under-5s)"],
      ["Toss pasta, chicken and vegetables.", "Stir through olive oil, lemon and salt.",
       "Pack with a small pot of grapes."],
      why="Colourful, cold and easy to eat with a fork — no soggy bread.", label="Day 10"),
    R("Chicken Shawarma Pinwheels", "15 min",
      ["1 cassava flatbread", "½ cup cooked shawarma-spiced chicken, sliced", "1 tbsp garlic coconut yogurt sauce",
       "Lettuce, grated carrot", "Orange segments"],
      ["Spread the yogurt sauce over the flatbread.", "Add chicken, lettuce and carrot.",
       "Roll tightly and slice into 6 pinwheels.", "Pack with orange segments."],
      why="A Naija favourite in a fun swirl — no wheat wrap, no mayonnaise.", label="Day 11"),
    R("Fish Finger Box", "Use leftovers",
      ["4 baked fish fingers (cassava crumb)", "2 tbsp minty pea dip (peas blended with olive oil)", "Carrot sticks",
       "Grapes"],
      ["Bake extra fish fingers at dinner and chill.", "Blend cooked peas with olive oil, mint and salt for the dip.",
       "Pack everything with the dip in a little pot."],
      why="White fish is gentle, low in mercury and great cold or warm.", label="Day 12"),
    R("Mama's Pasta Thermos", "Use leftovers",
      ["1 portion Mama's Pasta with Meat & Tomato Sauce", "Cucumber sticks", "Banana"],
      ["Heat the pasta and sauce until piping hot.", "Warm the thermos with boiling water, empty, then fill.",
       "Pack cucumber and a banana."],
      why="A dinner my child asks for again and again — just as good at lunchtime.",
      label="Day 13", region="Author's family favourite"),
    R("Akara Bites & Mango Box", "Prep ahead",
      ["5 baked akara bites", "2 tbsp tomato dip", "Mango cubes", "Cucumber sticks"],
      ["Bake akara bites in a mini muffin tin (see Naija Snack Corner). Cool.",
       "Pack with the tomato dip, mango and cucumber."],
      why="Akara is naturally gluten-free and egg-free — and baked, not fried.", label="Day 14"),
    R("Rainbow Fried Rice Thermos", "Use leftovers",
      ["1 cup chicken fried rice (no sweetcorn)", "Extra peas & diced carrot", "Pineapple chunks"],
      ["Reheat the fried rice with a splash of water until steaming.", "Fill a pre-warmed thermos.",
       "Pack pineapple separately."],
      why="Shop fried rice often has sweetcorn and soy sauce — this one has neither.", label="Day 15"),
    R("Mini Turkey Burger Sliders", "Prep ahead",
      ["2 mini turkey burgers (cooked & chilled)", "2 small rounds of buckwheat bread or lettuce “buns”",
       "Cucumber slices", "Sweet potato fries (baked)", "Sunshine Ketchup"],
      ["Make mini burgers with the turkey burger recipe in Healing Plates.",
       "Sandwich each in bread rounds or lettuce leaves.", "Pack with fries, cucumber and a dip."],
      why="Kids feel grown-up with a mini burger — and it's completely safe.", label="Day 16"),
    R("Chicken Suya Sticks & Dodo", "Prep ahead",
      ["4 nut-free chicken suya sticks (mild)", "Baked dodo bites", "Sliced cucumber & tomato", "Tangerine"],
      ["Rub chicken strips with ginger, paprika, garlic and onion powder (no groundnut, little pepper).",
       "Bake at 220 °C / 425 °F for 12–15 min. Cool.", "Pack with dodo, salad and fruit."],
      why="All the suya flavour, without the groundnut — school-safe.", label="Day 17"),
    R("Butternut Mac Bites Box", "Prep ahead",
      ["4 butternut mac bites", "Steamed broccoli florets", "Apple slices", "Coconut yogurt dip"],
      ["Spoon leftover butternut “mac & cheese” into a muffin tin.", "Bake at 200 °C / 400 °F for 15 min until set.",
       "Cool, then pack with broccoli, apple and dip."],
      why="Golden, cheesy-tasting bites with squash hidden inside.", label="Day 18"),
    R("Roast Chicken & Potato Salad Box", "Use leftovers",
      ["Leftover roast chicken pieces", "½ cup cooked potatoes, cubed", "2 tbsp coconut yogurt + chives + lemon",
       "Peas, cherry tomatoes", "Grapes"],
      ["Mix potatoes with coconut yogurt, chives, lemon and salt.", "Add peas.",
       "Pack with chicken, tomatoes and grapes."],
      why="Creamy potato salad with no egg mayonnaise.", label="Day 19"),
    R("Pancakes-for-Lunch Box", "Use leftovers",
      ["4 mini banana buckwheat pancakes", "Small pot of coconut yogurt", "Berries",
       "1 tbsp sunflower-seed butter (dip)"],
      ["Make extra pancakes at breakfast and cool.", "Pack with yogurt, berries and the seed-butter dip."],
      why="Breakfast-for-lunch feels like a treat — and it's still a balanced meal.", label="Day 20"),
    R("Beans & Dodo Thermos", "Use leftovers",
      ["1 portion beans & ripe plantain porridge", "Cucumber sticks", "Orange segments"],
      ["Reheat the beans until steaming.", "Fill a pre-warmed thermos.", "Pack cucumber and orange separately."],
      why="Honey beans are naturally sweet and full of fibre — filling all afternoon.", label="Day 21"),
    R("Rainbow Rice Paper Rolls", "20 min",
      ["4 rice paper sheets", "Cooked chicken strips", "Cucumber, carrot, pepper — thin sticks", "Lettuce, mango strips",
       "Coconut aminos dip"],
      ["Dip a rice paper sheet in warm water for 10 seconds.", "Fill with chicken, vegetables and mango.",
       "Fold the sides in and roll tightly.", "Pack with a little pot of coconut aminos."],
      why="See-through rolls let children see exactly what's inside — no surprises.",
      tip="Check the rice paper label: rice, tapioca, salt and water only.", tip_label="Allergy note", label="Day 22"),
    R("Coconut Chicken Curry Thermos", "Use leftovers",
      ["1 portion mild coconut chicken curry", "½ cup rice", "Cucumber coins", "Mango"],
      ["Reheat the curry and rice until piping hot.", "Fill a pre-warmed thermos.", "Pack cucumber and mango."],
      why="Mild, creamy and warming — turmeric and ginger are gentle on tummies.", label="Day 23"),
    R("Jollof Spaghetti Thermos", "Use leftovers",
      ["1 portion jollof spaghetti with chicken", "Carrot sticks", "Watermelon"],
      ["Reheat until steaming.", "Fill a pre-warmed thermos.", "Pack carrot sticks and watermelon."],
      why="Jollof + pasta = a lunch box that always comes home empty.", label="Day 24"),
    R("Pizza Quesadilla Wedges", "15 min",
      ["1 cassava flatbread", "2 tbsp passata + pinch oregano", "2 tbsp dairy-free cheese", "Cooked chicken, chopped",
       "Cherry tomatoes, grapes"],
      ["Spread passata on half the flatbread. Add cheese and chicken.", "Fold over and toast in a dry pan 2 min each side.",
       "Cool and cut into 4 wedges.", "Pack with tomatoes and grapes."],
      why="Pizza flavour in a crispy wedge — easy to hold and eat.", label="Day 25"),
    R("Build-a-Taco Box", "Use leftovers",
      ["2 small cassava flatbreads", "Taco-spiced beef mince (cold or in thermos)", "Shredded lettuce, diced tomato",
       "2 tbsp guacamole", "Dairy-free cheese, grated"],
      ["Pack each filling in its own section.", "Add the flatbreads folded in half.",
       "Your child builds their own tacos at lunch."],
      why="Building their own lunch gives children control — and they eat more.", label="Day 26"),
    R("Coconut Rice & Fish Bites", "Use leftovers",
      ["1 cup coconut rice", "4 baked fish bites (white fish, cassava crumb)", "Cucumber & tomato salad",
       "Pineapple"],
      ["Cut fish into bites, coat and bake at 220 °C / 425 °F for 10 min.", "Pack rice and fish bites.",
       "Add salad and pineapple."],
      why="Coconut rice makes fish feel like a party.", label="Day 27"),
    R("Hummus Dipper Box", "10 min",
      ["3 tbsp hummus", "Cucumber, carrot & pepper sticks", "6 plain rice crackers (no corn)",
       "Cooked chicken pieces", "Grapes"],
      ["Spoon hummus into a small pot.", "Arrange vegetables, crackers and chicken around it.", "Add grapes."],
      why="Dipping makes vegetables fun — even for veggie-shy children.",
      tip="Hummus contains sesame. If sesame is a problem, use guacamole instead.", tip_label="Allergy note",
      label="Day 28"),
    R("Picnic Box", "Use leftovers",
      ["2 chicken skewers (cold)", "Egg-free potato salad", "Rainbow fruit kebab on a paper straw",
       "Plantain chips"],
      ["Pack the skewers and potato salad.", "Thread fruit onto a paper straw.", "Add a handful of plantain chips."],
      why="A little picnic in a box — perfect for sunny days and school trips.", label="Day 29"),
    R("Day 30 Celebration Box", "Use leftovers",
      ["Mini portion of party jollof", "Baked chicken piece", "Baked dodo", "1 banana bread bite",
       "A note: “You did it! 30 days!”"],
      ["Pack the jollof, chicken and dodo.", "Add a banana bread bite as a treat.",
       "Tuck in a little note or sticker to celebrate."],
      why="Thirty days of safe, happy lunches — that's worth celebrating!", label="Day 30"),
]

CAL = ["Nugget happy box", "Pizza pinwheels", "Rainbow rice balls", "Turkey roll-ups", "Meatball skewers",
       "Jollof thermos", "DIY “lunchable”", "Mama's soup thermos", "Moi moi & dodo", "Rainbow pasta salad",
       "Shawarma pinwheels", "Fish finger box", "Mama's pasta thermos", "Akara bites & mango", "Fried rice thermos",
       "Turkey sliders", "Suya sticks & dodo", "Mac bites box", "Chicken potato salad", "Pancakes for lunch",
       "Beans & dodo thermos", "Rice paper rolls", "Coconut curry thermos", "Jollof spaghetti", "Pizza wedges",
       "Build-a-taco box", "Coconut rice & fish", "Hummus dippers", "Picnic box", "Celebration box"]

CLOSING_HTML = """
<p class="lead">Thirty lunch boxes. Thirty days of your child eating safely at school — and maybe even trying something new.</p>
<div class="grid2">
 <div class="box"><h3>Keep it going</h3><ul>
  <li>Start again at Day 1 — or repeat the family favourites.</li>
  <li>Swap any box for a leftover dinner from Healing Plates.</li>
  <li>Keep a stash of frozen nuggets, akara and soup for busy weeks.</li></ul></div>
 <div class="box"><h3>Don't forget</h3><ul>
  <li>Give the school a copy of the allergy card (Healing Printables).</li>
  <li>Check labels every time — recipes change.</li>
  <li>Celebrate every new food tried.</li></ul></div>
</div>
<div class="sign" style="margin-top:6mm">With love, Tris Eliverson</div><div class="role">Autism mum · Recipe creator</div>
<p class="disclaimer" style="margin-top:8mm">© Tris Eliverson. All rights reserved. For personal use only — please do not share or resell. This book shares food ideas from personal experience and is not medical advice. Always check food labels and your school's food policy. Cut grapes, cherry tomatoes and other round foods lengthways for children under 5.</p>
"""


def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def pages():
    out = []

    def add(kind, data, toc=None):
        out.append((kind, data, toc))

    add("cover", dict(series="Bonus Book 1", title=BOOK2, logo="box",
        subtitle="30 Days of Allergy-Free School Lunches & Snacks Kids Will Actually Eat",
        tagline="Nut-free and school-safe.", free=FREE_LB, badge=("30", "lunch<br>boxes"), author=AUTHOR))
    add("text", dict(kicker="Welcome", title="A lunch box made with love", html=WELCOME_HTML), "A lunch box made with love")
    add("toc", None)
    add("text", dict(kicker="Before you start", title="7 golden lunch box rules", html=LUNCH_RULES), "7 golden lunch box rules")
    add("text", dict(kicker="For picky eaters", title="The picky eater playbook", html=PICKY_HTML), "The picky eater playbook")
    add("grocery", dict(kicker="Stock up once", title="Lunch box pantry list",
        intro="Keep these in the kitchen and freezer and you can pack a safe lunch in minutes.", cats=PANTRY),
        "Lunch box pantry list")
    cells = [dict(day=i + 1, meals=[("l", "L", n)]) for i, n in enumerate(CAL)]
    weeks = [cells[i:i + 7] for i in range(0, 30, 7)]
    weeks[-1] += [None] * (7 - len(weeks[-1]))
    add("calendar", dict(kicker="Your month at a glance", title="30 lunch boxes", weeks=weeks, month=True, one=True, col="Lunch box"),
        "Your month at a glance")
    boxes = LUNCHBOXES + MORE
    for i, trio in enumerate(chunks(boxes, 3)):
        add("two", dict(kind="lunchbox", recipes=trio, small=True), "The 30 lunch boxes" if i == 0 else None)
    add("text", dict(kicker="Snack attack", title="10 snacks kids can't say no to", html=SNACKS_HTML),
        "10 snacks kids can't say no to")
    add("text", dict(kicker="Taste of home", title="Naija snack corner", html=NAIJA_HTML), "Naija snack corner")
    add("two", dict(kind="lunchbox", recipes=NAIJA_RECIPES))
    add("text", dict(kicker="You did it", title="Thirty happy lunches", html=CLOSING_HTML), "Thirty happy lunches")

    toc = [(t, i + 1) for i, (_, _, t) in enumerate(out) if t]
    for kind, data, _ in out:
        if kind == "toc":
            data = dict(kicker="Inside this book", title="Contents", items=toc)
        yield BOOK2, kind, data
