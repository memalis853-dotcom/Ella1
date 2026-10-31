"""Week 1 draft of all three books (for approval before writing weeks 2-5)."""
import preview
from preview import AUTHOR, BOOK1, BOOK2, BOOK3, BRANDS, FREE, FREE_FROM_HTML, GUT_HTML, treats

BOOK4 = "Healing Printables"
BOOK5 = "Healing Celebrations"
MARKS = {BOOK1: "plates", BOOK2: "box", BOOK3: "sips", BOOK4: "print", BOOK5: "party"}

WELCOME = next(d for b, k, d in preview.pages() if k == "text" and d.get("title") == "You are not alone")


def R(name, time, ing, steps, why=None, tip=None, tip_label=None, **kw):
    return dict(name=name, time=time, ing=ing, steps=steps, why=why, tip=tip, tip_label=tip_label, **kw)


# ---------------------------------------------------------------- basics
BASICS = [
    R("Flax “Egg” (replaces 1 egg)", "5 min",
      ["1 tbsp ground flaxseed", "3 tbsp water"],
      ["Stir the flaxseed and water together.", "Leave for 5 minutes until thick, like egg white.",
       "Use in pancakes, muffins and meatballs in place of 1 egg."],
      why="Binds food just like egg, and adds fibre and omega-3.", label="Basic"),
    R("Healing Seasoning Mix (replaces stock cubes)", "15 min + 4–6 hrs drying",
      ["1 cup cooked chicken breast or lean beef, shredded (no skin, no fat)", "2 tbsp onion powder, 1 tbsp garlic powder",
       "1 tbsp dried thyme, 1 tsp ground ginger", "1 tbsp ground crayfish (optional)",
       "1 tsp white pepper, 1 tsp pure curry powder", "1 tbsp sea salt"],
      ["Spread the cooked meat thinly on a parchment-lined tray.",
       "Dry in the oven on its lowest setting (70–80 °C / 160–175 °F), door slightly open, for 4–6 hrs until completely dry and crumbly.",
       "Cool, then blend to a fine powder.", "Add all the spices and blend again until even.",
       "Store in an airtight jar in the fridge for up to 1 month, or freeze for 3 months. Use 1–2 tsp wherever a recipe says “seasoning”."],
      why="Real chicken or beef flavour like a stock cube — without the hidden wheat, corn starch, MSG or sugar.",
      tip="Make a chicken jar and a beef jar. Chicken for soups and rice, beef for stews and egusi.", tip_label="Good idea",
      label="Basic"),
    R("Soft Cassava Flatbread (wraps, pizza & pinwheels)", "20 min · makes 6",
      ["1 cup (130 g) cassava flour", "¾ cup warm water", "2 tbsp olive oil", "½ tsp salt"],
      ["Mix everything into a soft dough. Rest 5 min.", "Divide into 6 balls (or 2 for pizza bases).",
       "Press thin between two sheets of parchment paper.",
       "Cook in a dry hot pan 1–2 min each side until spotty.", "Stack under a clean towel to stay soft."],
      why="A gluten-free, corn-free, egg-free wrap you can trust.", label="Basic"),
    R("Easy Buckwheat Bread (no yeast, no egg)", "1 hr 10 min · 1 loaf",
      ["2 cups (240 g) buckwheat flour", "½ cup (60 g) tapioca flour", "2 tbsp psyllium husk powder",
       "1 tsp baking soda, 1 tsp salt", "1½ cups warm water", "2 tbsp olive oil", "1 tbsp apple cider vinegar"],
      ["Heat oven to 180 °C / 350 °F. Line a loaf tin with parchment.", "Whisk the dry ingredients together.",
       "Add water, oil and vinegar. Mix to a thick, sticky dough. Rest 5 min.",
       "Smooth into the tin with wet hands. Bake 55–60 min.", "Cool completely before slicing — it firms up as it cools."],
      why="Buckwheat bread is on the author's speech-support list. Psyllium holds it together instead of egg.",
      tip="Slice, then freeze. Toast straight from the freezer.", tip_label="Time saver", label="Basic"),
    R("Crunchy Nut-Free Granola", "30 min",
      ["2 cups certified gluten-free oats", "½ cup pumpkin seeds", "½ cup sunflower seeds", "¼ cup coconut flakes",
       "3 tbsp melted coconut oil", "3 tbsp maple syrup or honey", "1 tsp cinnamon"],
      ["Heat oven to 160 °C / 320 °F. Line a tray with parchment.", "Mix everything and spread thin.",
       "Bake 20 min, stirring halfway.", "Cool completely — it crisps as it cools. Store in a jar."],
      why="Seeds give zinc and magnesium — step 2 of healing the gut.", label="Basic"),
]

# ---------------------------------------------------------------- family days
okro = R("Okro Soup with Chicken & Pounded Yam", "40 min",
         ["500 g chicken pieces", "15 fresh okro, chopped", "1 cup ugu or spinach", "1 onion, 2 ata rodo peppers",
          "1 tbsp ground crayfish", "2 tbsp red palm oil, 1 tsp seasoning mix", "Pounded yam or amala, to serve"],
         ["Season chicken with onion and seasoning. Cook in 2 cups water for 20 min.",
          "Add palm oil, pepper and crayfish. Cook 5 min.",
          "Add okro and cook only 3–4 min so it stays green.",
          "Stir in the greens and turn off the heat.", "Serve with pounded yam."],
         why="Okro is soft and gentle on the gut and helps keep things moving.",
         tip="Picky eater? Blend the okro smooth so there are no “slimy bits” to see.", tip_label="Kid tip")

DAYS = [
 dict(quote="“Small changes, one plate at a time. You are doing better than you think.”",
  b=R("Fluffy Banana Buckwheat Pancakes", "20 min",
      ["1 cup buckwheat flour", "1 ripe banana, mashed", "1 flax egg (see Basics)", "1 cup coconut milk",
       "1 tsp baking soda + 1 tsp lemon juice", "½ tsp cinnamon, pinch of salt", "Coconut oil, for the pan"],
      ["Mix the banana, flax egg and coconut milk.", "Stir in the flour, cinnamon, salt and baking soda, then the lemon juice.",
       "Heat a little oil in a pan on medium-low.", "Cook small pancakes 2 min until bubbles appear, flip, 1 more min.",
       "Top with berries and a drizzle of maple syrup."],
      why="Buckwheat is naturally gluten-free and full of magnesium.",
      tip="Baking soda + lemon makes pancakes rise without corn-starch baking powder.", tip_label="Good to know"),
  l=okro,
  d=R("Mama's Pasta with Meat & Tomato Sauce", "40 min",
      ["400 g rice pasta or gluten-free pasta (or lentil pasta)", "500 g beef mince", "1 onion, 2 garlic cloves",
       "1 carrot, finely grated (hidden veg)", "2 tins chopped tomatoes or 6 fresh tomatoes, blended",
       "1 tsp dried thyme or oregano, 1 tsp seasoning mix", "1 tbsp olive oil, salt"],
      ["Soften onion and garlic in olive oil, 3 min.", "Add the mince and brown it, breaking it up.",
       "Stir in the carrot, tomatoes and herbs. Simmer 20 min.",
       "Cook the pasta as the pack says. Drain.", "Toss the pasta through the sauce and serve."],
      why="A dinner my child asks for again and again — simple, filling and completely safe.",
      tip="Blend the sauce smooth if your child doesn't like to see “bits”.", tip_label="Kid tip",
      region="Author's family favourite")),
 dict(quote="Today's habit: 10 minutes of bouncing or dancing — it gets the lymph system moving.",
  b=R("Blueberry Banana Breakfast Cookies", "25 min · makes 12",
      ["3 ripe bananas, mashed", "2 cups certified gluten-free oats", "1 flax egg (see Basics)",
       "¾ cup blueberries", "2 tbsp pumpkin seeds", "2 tbsp melted coconut oil", "1 tsp cinnamon, pinch of salt"],
      ["Heat oven to 180 °C / 350 °F. Line a tray with parchment.",
       "Mash bananas with flax egg, coconut oil, cinnamon and salt.",
       "Stir in oats, blueberries and pumpkin seeds. Rest 5 min.",
       "Scoop 12 mounds onto the tray and flatten slightly.",
       "Bake 15–18 min until golden. Serve warm with coconut yogurt."],
      why="Cookies for breakfast — made only from fruit, oats and seeds. Slow energy, fibre and zinc.",
      tip="Make a double batch and freeze. Warm for 20 seconds on busy mornings.", tip_label="Time saver"),
  l=R("Chicken Burrito Bowl", "35 min",
      ["2 cups rice", "600 g chicken thighs", "1 tsp each cumin & paprika, ½ tsp garlic powder", "1 tin black beans, rinsed",
       "2 avocados, sliced", "3 tomatoes + ½ red onion + coriander (salsa)", "2 limes, olive oil, salt"],
      ["Cook the rice.", "Rub chicken with the spices, oil and salt. Bake at 200 °C / 400 °F for 25 min, then slice.",
       "Warm the beans with a pinch of salt.", "Chop tomatoes, onion and coriander with lime juice for salsa.",
       "Build bowls: rice, beans, chicken, avocado, salsa."],
      why="Beans and avocado bring fibre and healthy fats that keep little tummies full.",
      tip="Shop-bought bowls usually add corn — this one leaves it out.", tip_label="Allergy note"),
  d=R("Coriander Pepper Fish & Green Plantain", "35 min",
      ["4 small mackerel (titus) or tilapia", "3 green (unripe) plantains", "1 handful fresh coriander",
       "2 garlic cloves, 1 small onion", "1 scotch bonnet (skip for kids)", "1 tbsp olive oil, juice of 1 lemon, salt"],
      ["Blend coriander, garlic, onion, pepper, oil, lemon and salt to a paste.",
       "Rub the paste over the fish. Rest 15 min.",
       "Bake on parchment at 200 °C / 400 °F for 20–25 min (no foil).",
       "Meanwhile, peel and boil the plantains for 20 min.", "Serve with sliced cucumber."],
      why="Small fish carry far less mercury than tuna. Coriander is a traditional cleansing herb.")),
 dict(quote="“Healing is not a straight line. Celebrate every small win.”",
  b=R("Mango Chia Overnight Oats", "5 min + overnight",
      ["2 cups certified gluten-free oats", "2 cups coconut milk", "2 tbsp chia seeds", "1 mango, diced",
       "1 tsp cinnamon", "1 tbsp maple syrup (optional)"],
      ["Stir oats, coconut milk, chia, cinnamon and maple together.", "Spoon into 4 jars or cups.",
       "Cover and chill overnight.", "In the morning, top with mango and eat cold."],
      why="Chia and oats are gentle fibre for regular, easy bowels.",
      tip="Can't have oats? Use millet or buckwheat flakes instead."),
  l=R("Jollof Rice with Baked Chicken", "1 hr",
      ["3 cups long-grain parboiled rice", "1 kg chicken pieces", "6 tomatoes, 3 red peppers, 1 onion, 1 scotch bonnet",
       "2 tbsp tomato paste, 3 tbsp olive oil", "1 tsp thyme, 1 tsp pure curry powder, 2 bay leaves",
       "2 tsp seasoning mix, salt", "3 cups chicken stock or water"],
      ["Season chicken and bake at 200 °C / 400 °F for 40 min.", "Blend tomatoes, peppers, onion and scotch bonnet.",
       "Fry tomato paste in oil 3 min, add the blend and cook 15 min until thick.",
       "Add spices, stock and rinsed rice. Cover tightly and cook on low 25–30 min.",
       "Fluff and serve with the chicken and a fresh salad."],
      why="A home favourite made without stock cubes — all flavour, no hidden wheat or MSG."),
  d=R("Crispy Baked Chicken Nuggets & Sweet Potato Wedges", "35 min",
      ["600 g chicken breast, cut into bite pieces", "1 cup cassava flour", "1 tsp paprika, ½ tsp garlic powder, salt",
       "3 tbsp olive oil", "3 sweet potatoes, cut into wedges", "Frozen peas, to serve"],
      ["Heat oven to 220 °C / 425 °F. Line 2 trays with parchment.", "Toss the wedges with 1 tbsp oil and salt. Bake 30 min.",
       "Toss chicken in the remaining oil, then roll in flour mixed with the spices.",
       "Bake the nuggets 15–18 min, turning once, until golden.", "Serve with peas and Sunshine Ketchup (Lunch Box book)."],
      why="All the fun of fast food — with no egg, no wheat crumb and no deep frying.",
      tip="Let them dip! Children try more food when they can dip it.", tip_label="Picky eater trick")),
 dict(quote="Today's habit: eat breakfast near a sunny window or outside — morning light helps sleep later.",
  b=R("Creamy Millet Porridge (Hausa Koko Style)", "15 min",
      ["1 cup pure millet flour (no corn added)", "4 cups water", "1 thumb ginger, grated", "Pinch of cloves",
       "1 cup coconut milk", "3 dates, chopped (to sweeten)"],
      ["Mix the millet flour with 1 cup cold water until smooth.", "Boil the rest of the water with ginger, cloves and dates.",
       "Pour in the millet mix, stirring all the time.", "Cook 8–10 min on low until thick. Stir in coconut milk."],
      why="Millet is a gluten-free ancient grain that is gentle on the stomach.",
      tip="Many “koko” and “uji” mixes contain maize — buy pure millet flour.", tip_label="Allergy note"),
  l=R("Creamy Butternut “Mac & Cheese”", "30 min",
      ["400 g lentil or chickpea pasta", "3 cups butternut squash, cubed", "1 cup coconut milk",
       "3 tbsp nutritional yeast (optional — cheesy taste)", "1 garlic clove, ½ tsp turmeric, salt", "1 cup small broccoli florets"],
      ["Boil the squash and garlic 12 min until soft. Drain.", "Blend with coconut milk, nutritional yeast, turmeric and salt.",
       "Cook the pasta, adding the broccoli for the last 3 minutes.", "Stir the golden sauce through the pasta."],
      why="Squash is a root-vegetable carb from the author's “foods to eat” list — and kids love the colour.",
      tip="Bake leftovers in a muffin tin for 15 min to make mac bites for lunch boxes.", tip_label="Leftover magic"),
  d=R("Egusi Soup with Beef & Amala", "50 min",
      ["1 cup ground egusi", "500 g beef, cubed", "3 tbsp red palm oil", "1 onion + 2 red peppers + 1 scotch bonnet, blended",
       "1 tbsp ground crayfish", "2 cups ugu or spinach", "Amala (yam flour), to serve"],
      ["Cook beef with onion and seasoning mix until tender, 30 min. Keep the stock.",
       "Mix egusi with a little water to a thick paste.",
       "Warm palm oil, add the pepper blend and cook 5 min. Add egusi in lumps and cook 10 min.",
       "Add beef, stock and crayfish. Simmer 10 min.", "Stir in the greens. Serve with amala."],
      why="Egusi (melon seeds) is a gut-repairing food from step 3 — rich in protein and zinc.")),
 dict(quote="“You are not behind. You are exactly where your family needs you to be.”",
  b=R("Sweet Potato & Spinach Breakfast Hash", "25 min",
      ["3 sweet potatoes, diced small", "1 red pepper, 1 onion, diced", "250 g turkey mince (or 1 tin beans)",
       "2 handfuls spinach", "1 tsp paprika, salt", "2 tbsp avocado oil", "1 avocado, to serve"],
      ["Cook sweet potato in oil, covered, 10 min, stirring now and then.", "Add onion, pepper and turkey. Cook 8 min.",
       "Add paprika, salt and spinach. Stir until wilted.", "Serve topped with sliced avocado."],
      why="A savoury, protein-rich breakfast that keeps energy steady until lunch."),
  l=R("Thai Coconut Chicken Noodle Soup", "30 min",
      ["500 g chicken thighs, thinly sliced", "1 tin coconut milk + 3 cups stock", "1 stalk lemongrass, bashed",
       "1 thumb ginger, 2 garlic cloves, sliced", "1 tbsp coconut aminos (instead of soy sauce)",
       "200 g rice noodles", "Lime, fresh coriander"],
      ["Simmer stock, lemongrass, ginger and garlic 5 min.", "Add chicken and cook 8 min.",
       "Pour in coconut milk and coconut aminos. Heat gently.", "Cook the noodles, divide into bowls and ladle soup over.",
       "Finish with lime and coriander."],
      why="Warm, mild and soothing — garlic and ginger support step 4 of healing the gut.",
      tip="Soy sauce contains wheat. Coconut aminos tastes similar and is safe.", tip_label="Allergy note"),
  d=R("Egg-Free Moi Moi with Avocado Salad", "1 hr 15 min",
      ["2 cups black-eyed beans, soaked & peeled", "1 red pepper, 1 scotch bonnet, 1 onion", "3 tbsp red palm oil",
       "1 tbsp crayfish, 1 tsp seasoning mix, salt", "About 1 cup warm water",
       "Avocado, tomato & cucumber salad"],
      ["Blend beans, pepper and onion with water until very smooth.", "Stir in oil, crayfish, seasoning and salt.",
       "Pour into greased ramekins or silicone cups (no foil).", "Steam 45–50 min until firm.", "Serve with the salad."],
      why="Beans set perfectly on their own — no egg needed. Packed with plant protein.")),
 dict(quote="It's Friday — Sweet Treat Day! See the sweet treats page.",
  b=R("Ripe Plantain Pancakes", "20 min",
      ["2 very ripe (black) plantains", "½ cup cassava flour", "1 flax egg", "½ cup coconut milk",
       "½ tsp cinnamon, pinch salt", "½ tsp baking soda + squeeze of lemon", "Coconut oil, for the pan"],
      ["Blend everything until smooth.", "Heat a little oil in a pan on medium-low.",
       "Cook small pancakes 2–3 min each side.", "Serve with berries or coconut yogurt."],
      why="Naturally sweet from the plantain — no sugar needed."),
  l=R("Kenyan Beef Pilau & Kachumbari", "1 hr",
      ["3 cups basmati rice", "600 g beef, cubed", "2 onions, 4 garlic cloves, 1 thumb ginger", "2 potatoes, cubed",
       "1 tsp each cumin, cinnamon, cardamom, black pepper; 4 cloves", "2 tomatoes, salt",
       "Kachumbari: tomato, red onion, cucumber, coriander, lime"],
      ["Boil beef with salt until tender, 30 min. Keep 5 cups of stock.",
       "Brown onions in oil, add garlic, ginger and spices, 2 min.", "Add beef, potatoes, tomatoes and rinsed rice; stir.",
       "Pour in stock, cover and cook on low 20 min.", "Serve with the fresh chopped kachumbari."],
      why="Warm spices like cinnamon and ginger are gentle on digestion."),
  d=R("Family Pizza Night", "30 min",
      ["2 cassava flatbread pizza bases (see Basics)", "1 cup tomato passata", "1 tsp oregano",
       "1 cup dairy-free cheese, grated", "Cooked chicken, peppers, mushrooms", "Olive oil"],
      ["Heat oven to 220 °C / 425 °F.", "Spread passata over the bases, sprinkle oregano.",
       "Add cheese and toppings.", "Bake 10–12 min until bubbling.", "Slice and serve with a green salad."],
      why="Pizza night is back on the menu — no gluten, dairy or corn.",
      tip="Let each child top their own slice. Kids eat what they make.", tip_label="Picky eater trick")),
 dict(quote="Sunday: batch-cook day. See next week's plan and prep ahead.",
  b=R("Coconut Yogurt Berry Parfait", "5 min",
      ["2 cups coconut yogurt", "2 cups mixed berries", "1 cup Crunchy Nut-Free Granola (see Basics)",
       "1 tbsp honey or maple syrup (optional)"],
      ["Layer yogurt, berries and granola in glasses.", "Repeat the layers.", "Drizzle with honey and eat straight away."],
      why="Coconut yogurt feeds good gut bacteria — step 4 of healing the gut."),
  l=R("Sunday Roast Chicken & Vegetables", "1 hr 30 min",
      ["1 whole chicken (1.5 kg)", "1 kg potatoes, halved", "4 carrots, 2 sweet potatoes", "1 lemon, 1 garlic bulb",
       "Fresh rosemary & thyme", "3 tbsp avocado oil, salt", "1 tbsp tapioca flour (for gravy)"],
      ["Rub chicken with oil, salt and herbs; put lemon and garlic inside. Roast at 190 °C / 375 °F for 1 hr 20 min.",
       "Boil potatoes 8 min, drain, toss in oil and roast 45 min with the carrots.",
       "Rest the chicken 10 min.", "Stir pan juices with tapioca mixed in a little water until thick — gravy!",
       "Serve with steamed broccoli."],
      why="Rosemary, thyme and garlic are all on the author's gut-friendly list.",
      tip="Gravy granules often contain wheat and corn starch. Tapioca makes a safe gravy.", tip_label="Allergy note"),
  d=R("Mama's Chicken, Potato & Carrot Soup", "45 min",
      ["500 g chicken (breast or thighs)", "4 Irish potatoes, peeled & cubed", "4 carrots, sliced",
       "1 onion, 2 garlic cloves", "1 tsp dried thyme, 1 tsp seasoning mix, salt", "5 cups water",
       "Homemade buckwheat bread, to serve"],
      ["Boil the chicken with onion, garlic, thyme and seasoning for 25 min. Lift out and shred.",
       "Boil the potatoes and carrots in the same stock for 15 min until soft.",
       "Blend the vegetables smooth — or blend half and chop the rest very tiny.",
       "Stir the shredded chicken back in. Simmer 5 min.", "Serve warm with buckwheat bread."],
      why="My child's favourite. Blending the vegetables means all the goodness goes in — without them seeing it.",
      tip="Some days blend it all, some days leave tiny pieces — a gentle way to get used to new textures.",
      tip_label="Kid tip", region="Author's family favourite")),
]
for i, d in enumerate(DAYS):
    d.update(week=1, day=i + 1)

WEEK1_NAMES = [
    ("Banana buckwheat pancakes", "Okro soup & pounded yam", "Mama's pasta & meat sauce"),
    ("Banana breakfast cookies", "Chicken burrito bowl", "Coriander pepper fish"),
    ("Mango overnight oats", "Jollof rice & chicken", "Chicken nuggets & wedges"),
    ("Millet porridge", "Butternut mac & cheese", "Egusi soup & amala"),
    ("Sweet potato hash", "Thai coconut noodle soup", "Egg-free moi moi"),
    ("Ripe plantain pancakes", "Kenyan beef pilau", "Family pizza night"),
    ("Coconut yogurt parfait", "Sunday roast chicken", "Mama's chicken & potato soup"),
]

GROCERY = [
    ("Vegetables & greens", ["Ugu or spinach — 4 big bunches", "Okro — 15", "Tomatoes — 16", "Red peppers — 6",
                             "Scotch bonnet / ata rodo — 5", "Onions — 10, red onion — 1", "Garlic — 2 bulbs, ginger — 1 large piece",
                             "Carrots — 10", "Courgette — 1", "Butternut squash — 1", "Broccoli — 2 heads",
                             "Sweet potatoes — 8", "Irish potatoes — 2 kg", "Cucumber — 3", "Mushrooms — 200 g",
                             "Lemongrass — 1 stalk", "Avocados — 5", "Frozen peas — 1 bag"]),
    ("Fruit & plantain", ["Green plantains — 3", "Very ripe plantains — 2", "Ripe bananas — 5",
                          "Mangoes — 2", "Mixed berries — 3 punnets", "Lemons — 3, limes — 4"]),
    ("Protein", ["Chicken pieces — 1.5 kg", "Chicken thighs — 1.1 kg", "Chicken breast — 1.1 kg", "Whole chicken — 1.5 kg",
                 "Beef mince — 750 g", "Beef cubes — 1.1 kg", "Turkey mince — 250 g", "Mackerel or tilapia — 4 small",
                 "Black-eyed beans — 2 cups", "Black beans — 1 tin"]),
    ("Grains & flours", ["Rice or gluten-free pasta — 400 g", "Lentil pasta — 400 g", "Long-grain rice + basmati — 3 cups each", "Rice noodles — 200 g",
                         "Buckwheat flour", "Cassava flour", "Pure millet flour", "Certified gluten-free oats",
                         "Amala & pounded yam flour", "Ground egusi — 1 cup"]),
    ("Dairy-free & pantry", ["Coconut milk — 5 tins", "Coconut yogurt — 1 large tub", "Dairy-free cheese — 1 pack",
                             "Chopped tomatoes — 2 tins, passata — 1 jar, tomato paste", "Red palm, olive, avocado & coconut oil",
                             "Chia seeds, ground flaxseed", "Pumpkin & sunflower seeds, coconut flakes",
                             "Coconut aminos", "Maple syrup or raw honey, dates", "Baking soda, tapioca flour", "Psyllium husk powder, apple cider vinegar"]),
    ("Herbs & spices", ["Fresh coriander — 2 bunches", "Fresh rosemary & thyme", "Dried thyme, oregano, basil, bay leaves",
                        "Pure curry powder, paprika, cumin, turmeric", "Cinnamon, cloves, cardamom, black pepper",
                        "Garlic & onion powder, ground ginger", "Ground crayfish", "Sea salt"]),
]

# ---------------------------------------------------------------- celebration cake & party guide
CAKE = R("Celebration Vanilla Berry Cake", "1 hr + cooling · one 20 cm / 8 in cake",
         ["1 cup (140 g) brown rice flour", "½ cup (60 g) tapioca flour + ½ cup (80 g) potato starch",
          "1 tsp psyllium husk powder", "½ cup pure maple syrup", "1 tsp baking soda, ¼ tsp salt",
          "¾ cup coconut milk or water", "⅓ cup light olive or avocado oil", "1 tbsp apple cider vinegar + 1 tsp pure vanilla powder"],
         ["Heat oven to 180 °C / 350 °F. Line a round tin with parchment.",
          "Whisk all the dry ingredients together.", "Add the milk, oil, vinegar and vanilla. Mix just until smooth.",
          "Bake 30–35 min until a skewer comes out clean. Cool completely.",
          "Frost with chilled whipped coconut cream + 1 tbsp maple syrup. Top with berries and candles!"],
         why="No egg, dairy, gluten, corn, nuts or processed sugar — every child at the party can have a slice.",
         tip="Many vanilla extracts use corn alcohol. Pure vanilla powder or seeds are safe.", tip_label="Allergy note",
         label="Birthday",
         ) | dict(tip="Makes 12 cupcakes too — bake 18–20 min. Many vanilla extracts use corn alcohol, so use pure vanilla powder.",
                  tip_label="Cupcakes")

PARTY_HTML = """
<p class="lead">Parties, owambes, church events and school trips can feel scary. With a little planning, your child can join in — and feel included.</p>
<div class="grid2">
 <div class="box"><h3>Before the party</h3><ul>
  <li>Message the host early. Share the allergy card from the Printables pack.</li>
  <li>Ask what will be served — then offer to bring one safe dish to share.</li>
  <li>Feed your child a proper meal first, so they're never hungry and tempted.</li></ul></div>
 <div class="box"><h3>Pack a “party box”</h3><ul>
  <li>A slice of the Celebration Cake, frozen ahead in portions.</li>
  <li>Nuggets, plantain chips, fruit kebabs, a juice from Healing Sips.</li>
  <li>Make it look special — a bright box, a sticker, a party napkin.</li></ul></div>
 <div class="box"><h3>At the party</h3><ul>
  <li>Stay close to the food table for younger children.</li>
  <li>Teach a simple line: “No thank you, I have my own special snack.”</li>
  <li>Watch for shared bowls of sweets, chin chin and puff-puff.</li></ul></div>
 <div class="box"><h3>Eating out</h3><ul>
  <li>Choose grilled chicken or fish, plain rice, boiled potatoes, salad.</li>
  <li>Ask: “Is there wheat, milk, butter, egg or corn starch in this?”</li>
  <li>Avoid sauces, gravies, batters and anything deep-fried in shared oil.</li></ul></div>
</div>
<div class="callout"><div class="t">Sensory overwhelm is real</div>
<p>Loud music and crowds can be a lot. Arrive early when it's quiet, find a calm corner, and plan a gentle exit time. Leaving happy is a win.</p></div>
"""

CAKE_TIPS = """
<div class="grid2">
 <div class="box"><h3>Fluffy coconut frosting</h3><ul>
  <li>Chill 2 tins of full-fat coconut milk overnight.</li>
  <li>Scoop out only the thick cream on top.</li>
  <li>Whisk 2 min with 1 tbsp maple syrup until fluffy.</li>
  <li>Keep the cake in the fridge until party time.</li></ul></div>
 <div class="box"><h3>Decorate without food colouring</h3><ul>
  <li><b>Pink:</b> a spoon of beetroot juice or blended strawberries.</li>
  <li><b>Yellow:</b> a pinch of turmeric.</li>
  <li><b>Purple:</b> blended blueberries.</li>
  <li>Top with fresh berries, mango stars and coconut flakes.</li></ul></div>
</div>
<div class="sweetnote">Freeze slices for school birthdays — your child will always have their own cake when classmates celebrate.</div>
"""

PARTY = [
    R("Baked Plantain Puff-Puff Bites", "30 min · makes 24",
      ["2 very ripe plantains", "1 cup cassava flour", "½ cup coconut milk", "½ tsp nutmeg, pinch of salt",
       "½ tsp baking soda + 1 tsp lemon juice", "Coconut oil, for the tin", "Cinnamon, for dusting"],
      ["Heat oven to 200 °C / 400 °F. Oil a mini muffin tin well.", "Blend plantain and coconut milk until smooth.",
       "Stir in flour, nutmeg, salt and baking soda, then the lemon juice.",
       "Spoon into the tin. Bake 15–18 min until golden.", "Dust with a little cinnamon while warm — the plantain is sweet enough."],
      why="Puff-puff without wheat, egg or deep frying — so your child can join the party plate.",
      label="Party"),
    R("Zobo Party Punch", "20 min + chilling",
      ["1 cup dried hibiscus (zobo) leaves", "8 cups water", "1 thumb ginger, sliced, 4 cloves",
       "½ pineapple, peeled (keep the peel too)", "6 dates (to sweeten)", "Orange slices, to serve"],
      ["Rinse the zobo. Boil with water, ginger, cloves and pineapple peel for 15 min.",
       "Add the dates, turn off the heat and steep 30 min.", "Strain well. Blend the pineapple flesh and stir it in.",
       "Chill and serve with orange slices and ice."],
      why="Bright red, fruity and naturally caffeine-free — a party drink everyone can share.", label="Party"),
    R("Nut-Free Chicken Suya Skewers", "30 min + marinating",
      ["600 g chicken breast, cut into strips", "2 tsp paprika, 1 tsp ground ginger", "1 tsp garlic powder, 1 tsp onion powder",
       "½ tsp cayenne (less for kids), 1 tsp salt", "2 tbsp olive oil", "Sliced onion, tomato & cucumber"],
      ["Mix spices, salt and oil. Rub over the chicken. Rest 30 min.", "Thread onto soaked wooden skewers.",
       "Bake at 220 °C / 425 °F for 12–15 min, turning once.", "Serve with fresh onion, tomato and cucumber."],
      why="Classic suya spice uses groundnut (kuli kuli). This version is nut-free and party-safe.", label="Party"),
    R("Rainbow Fruit Wands", "15 min",
      ["Strawberries, pineapple, mango, kiwi, grapes, blueberries", "Watermelon slices",
       "Paper straws or blunt skewers", "Star cookie cutter"],
      ["Cut fruit into chunks, in rainbow order.", "Cut stars from the watermelon slices.",
       "Thread the fruit onto straws and top each with a star.", "Chill until party time."],
      why="Children who won't touch a fruit bowl will happily eat a magic wand.", label="Party"),
]

TRACK_ROWS = "".join
SWAPS = [("Wheat flour", "Cassava, buckwheat, tapioca or rice flour"), ("Bread", "Easy Buckwheat Bread, cassava flatbread"),
         ("Pasta", "Rice, lentil or chickpea pasta"), ("Semovita, wheat swallow", "Pounded yam, amala, plantain fufu"),
         ("Pap / ogi / akamu", "Pure millet porridge"), ("Cow's milk", "Coconut, rice or tiger nut milk"),
         ("Butter", "Coconut oil or olive oil"), ("Cheese", "Dairy-free cheese, nutritional yeast"),
         ("Yogurt", "Coconut yogurt"), ("Egg", "Flax egg (1 tbsp ground flax + 3 tbsp water)"),
         ("Baking powder", "Baking soda + lemon juice or vinegar"), ("Cornflour (to thicken)", "Tapioca flour"),
         ("Stock cubes", "Healing Seasoning Mix"), ("Soy sauce", "Coconut aminos"),
         ("Tea, coffee, energy drinks", "Rooibos, ginger, lemon balm, zobo"), ("Chocolate, Milo", "Carob"),
         ("Sugar, sweets", "Dates, ripe banana or plantain, pure maple syrup, honey (age 1+)"), ("Tuna", "Mackerel, sardines, salmon, tilapia"),
         ("Pork, bacon, ham", "Chicken, turkey, beef"), ("Peanut butter (school)", "Sunflower-seed butter"),
         ("Deep frying", "Baking, steaming, boiling"), ("Foil", "Parchment paper")]
SWAP_HTML = ('<table class="tbl"><tr><th style="width:38%">Instead of…</th><th>Use…</th></tr>'
             + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in SWAPS) + "</table>")


def tracker(first, last):
    rows = "".join(f"<tr><td>{d}</td><td></td><td></td><td></td><td></td><td></td></tr>" for d in range(first, last + 1))
    return f"""<p class="muted small">Tick or score 1–5. After 2 weeks, look back — patterns jump out.</p>
<table class="track tall"><tr><th style="width:9%">Day</th><th>Sleep</th><th>Mood</th><th>Tummy &amp; poo</th><th>New food tried</th><th style="width:28%">Notes</th></tr>{rows}</table>"""


REWARD_HTML = """<p class="lead">Every time your child tries a new food — even one tiny lick — they get a sticker or a star. 30 tries = a big celebration!</p>
<div class="reward">""" + "".join(f'<div class="cell"><b>{i}</b><span>Food:</span></div>' for i in range(1, 31)) + """</div>
<p class="sign" style="text-align:center;font-size:15pt">Every try counts! ★</p>"""

PLANNER_HTML = """<p class="muted small">Plan the week, then write your shopping list on the next page.</p>
<table class="track tall plan"><tr><th style="width:12%">Day</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th><th>Snack / lunch box</th></tr>""" + "".join(
    f"<tr><td>{d}</td><td></td><td></td><td></td><td></td></tr>" for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]) + "</table>"

SHOP_HTML = '<div class="groc blank">' + "".join(
    f'<div class="cat"><h3>{c}</h3><ul>' + "<li></li>" * 7 + "</ul></div>"
    for c in ["Vegetables", "Fruit", "Protein", "Grains & flours", "Dairy-free", "Pantry & spices"]) + "</div>"

SAFE_HTML = """<p class="lead">Write down the foods your child loves today — and the ones you're working on. Share it with anyone who cooks for them.</p>
<div class="grid2"><div class="box"><h3>Safe foods — always yes</h3><div class="lines" style="height:150mm"></div></div>
<div class="box"><h3>Foods we're trying</h3><div class="lines" style="height:150mm"></div></div></div>"""

# ---------------------------------------------------------------- lunch box book
LUNCH_RULES = """
<p class="lead">A good lunch box is safe, simple and fun. Follow these 7 golden rules and lunchtime gets easier for everyone.</p>
<div class="step"><div class="n">1</div><div><h3>Pack the night before</h3><p>Mornings are busy. Pack everything except hot food the evening before.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>One safe food + one new food</h3><p>Always include a food your child already loves. Put the new food beside it — no pressure.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Keep it cold — or hot</h3><p>Use an ice pack for cold boxes and a thermos for warm food like jollof or soup.</p></div></div>
<div class="step"><div class="n">4</div><div><h3>Every box is nut-free</h3><p>Most schools are nut-free. We use sunflower-seed butter instead of peanut butter.</p></div></div>
<div class="step"><div class="n">5</div><div><h3>Tell the teacher</h3><p>Give the school a copy of the allergy card from the Printables pack.</p></div></div>
<div class="step"><div class="n">6</div><div><h3>Small and colourful wins</h3><p>Small portions, bright colours and fun shapes. Cookie cutters are your best friend.</p></div></div>
<div class="step"><div class="n">7</div><div><h3>Let them choose</h3><p>Offer two choices: “Nuggets or pinwheels tomorrow?” Children eat what they choose.</p></div></div>
"""

LUNCHBOXES = [
    R("Chicken Nugget Happy Box", "Prep the night before",
      ["6 homemade chicken nuggets", "Handful of sweet potato wedges", "Apple slices + squeeze of lemon", "Cucumber sticks",
       "2 tbsp Sunshine Ketchup"],
      ["Coat chicken pieces in olive oil, then cassava flour, paprika and salt.",
       "Bake with the wedges at 220 °C / 425 °F for 15–18 min.",
       "Sunshine Ketchup: simmer 1 cup passata, 2 chopped dates, pinch of salt and a splash of apple cider vinegar for 10 min; blend.",
       "Morning: pack everything, ketchup in a little pot for dipping."],
      why="A homemade “happy meal” with no egg, no wheat and no added sugar.",
      tip="Cut apple slices with a heart cookie cutter. Shapes make food fun.", tip_label="Picky eater trick", label="Day 1"),
    R("Mini Pizza Pinwheels", "15 min",
      ["1 cassava flatbread or tortilla", "2 tbsp tomato passata + pinch oregano", "2 tbsp dairy-free cheese, grated",
       "A few shreds of cooked chicken", "Grapes (halved for under-5s)", "Carrot sticks"],
      ["Spread passata over the flatbread. Sprinkle oregano, cheese and chicken.",
       "Roll up tightly and slice into 6 rounds.", "Bake at 200 °C / 400 °F for 8 min — or pack cold.",
       "Pack with the grapes and carrots."],
      why="All the pizza flavour kids love, in a fun swirl shape.", label="Day 2"),
    R("Rainbow Rice Ball Bento", "15 min",
      ["1 cup cooked short-grain rice", "½ cup shredded cooked chicken", "Pinch of salt", "Cucumber coins",
       "Strawberries & mango cubes", "Coconut yogurt dip"],
      ["Mix the warm rice with chicken and salt.", "With wet hands, roll into 6 small balls.",
       "Pack each food in its own section, sorted by colour.", "Add the dip in a small pot."],
      why="Separate sections are perfect for children who don't like foods touching.",
      tip="Ask your child to “eat the rainbow” — one bite of every colour.", tip_label="Fun idea", label="Day 3"),
    R("Turkey & Avocado Roll-Ups", "10 min",
      ["1 cassava flatbread or tortilla", "½ avocado, mashed", "3 slices homemade roast turkey or chicken",
       "Lettuce leaf, grated carrot", "Blueberries", "Baked plantain chips"],
      ["Spread avocado over the flatbread.", "Layer turkey, lettuce and carrot.",
       "Roll tightly and cut into 2-bite pieces.", "Pack with blueberries and plantain chips."],
      why="Homemade meat avoids the nitrates found in most deli slices.", label="Day 4"),
    R("Mini Meatball Skewers", "30 min",
      ["250 g beef mince", "1 flax egg", "2 tbsp cassava flour", "2 tbsp grated courgette (hidden veg!)",
       "½ tsp garlic powder, salt", "Cherry tomatoes, cucumber", "Tomato dip"],
      ["Mix mince, flax egg, flour, courgette and seasoning.", "Roll into 12 small balls.",
       "Bake at 200 °C / 400 °F for 15 min. Cool.",
       "Thread onto paper straws or blunt picks with halved tomatoes and cucumber."],
      why="Food on a stick is fun — and the courgette is hidden inside.",
      tip="Make a double batch and freeze half for next week.", tip_label="Time saver", label="Day 5"),
    R("Jollof Rice & Chicken Thermos", "Use leftovers",
      ["1 cup leftover jollof rice", "3–4 pieces baked chicken", "Watermelon cubes", "Carrot sticks"],
      ["Heat the jollof and chicken until piping hot in the morning.",
       "Fill the thermos with boiling water for 5 min, empty it, then add the food — it stays warm until lunch.",
       "Pack the watermelon and carrots separately."],
      why="A familiar home favourite makes lunchtime feel safe for sensitive eaters.", label="Day 6"),
    R("DIY “Lunchable” Box", "10 min",
      ["6 plain rice crackers (check: no corn)", "4 slices homemade roast chicken", "6 cubes dairy-free cheese",
       "Cucumber coins, grapes", "2 Sunshine Bliss Balls"],
      ["Bliss balls: blitz 1 cup dates, ½ cup sunflower seeds and 2 tbsp coconut; roll into balls.",
       "Arrange crackers, chicken, cheese and cucumber in rows.", "Add grapes and bliss balls."],
      why="Kids build their own “cracker stacks” — and feel in charge of their food.",
      tip="Shop-bought lunch kits contain dairy, wheat and nitrates. This one is clean.", tip_label="Allergy note",
      label="Day 7"),
]

SNACKS_HTML = """
<p class="lead">Bright, crunchy, dippable and fun. These snacks are made for even the pickiest eaters — nut-free, processed-sugar-free and free from every food in this book.</p>
<div class="grid2">
 <div class="box"><h3>1. Veggie Tots</h3><p>Mash 1 sweet potato with ½ grated courgette and 3 tbsp tapioca flour. Shape into little logs, bake 20 min at 200 °C.</p></div>
 <div class="box"><h3>2. Fruit Nachos</h3><p>Thin apple slices on a plate, drizzled with warm sunflower-seed butter and carob syrup. Sprinkle coconut.</p></div>
 <div class="box"><h3>3. Banana Sushi</h3><p>Spread coconut yogurt on a banana, roll in crushed pumpkin seeds, slice into “sushi” rounds.</p></div>
 <div class="box"><h3>4. Frozen Yogurt Bark</h3><p>Spread coconut yogurt on parchment, dot with berries, freeze 3 hours and snap into pieces.</p></div>
 <div class="box"><h3>5. Apple “Donuts”</h3><p>Slice apples into rings, core them, spread with sunflower-seed butter and add coconut “sprinkles”.</p></div>
 <div class="box"><h3>6. Baked Plantain Chips</h3><p>Very thin green plantain slices, olive oil and salt. Bake 15–20 min at 190 °C until crisp.</p></div>
 <div class="box"><h3>7. Crunchy Chickpeas</h3><p>Dry a tin of chickpeas, toss with oil, paprika and salt. Bake 30 min at 200 °C.</p></div>
 <div class="box"><h3>8. Sunshine Bliss Balls</h3><p>Blitz dates, sunflower seeds and coconut. Roll into balls. No nuts, no sugar added.</p></div>
 <div class="box"><h3>9. Pancake Skewers</h3><p>Leftover mini pancakes and strawberries threaded onto paper straws.</p></div>
 <div class="box"><h3>10. Cucumber Pizza Coins</h3><p>Thick cucumber rounds topped with a dab of hummus and chopped tomato.</p></div>
</div>
<div class="callout gold"><div class="t">Carob instead of chocolate</div><p>Chocolate and cocoa contain caffeine. Carob tastes chocolatey, is naturally sweet and caffeine-free.</p></div>
"""

NAIJA_HTML = """
<p class="lead">Our favourite Nigerian snacks — made gluten-free, egg-free, nut-free, processed-sugar-free and baked instead of deep-fried. Familiar tastes from home that are safe for school.</p>
<div class="grid2">
 <div class="box"><h3>1. Ipekere (Plantain Chips)</h3><p>Thin green plantain slices, a little oil and salt. Bake 15–20 min at 190 °C until crisp.</p></div>
 <div class="box"><h3>2. Baked Dodo Bites</h3><p>Ripe plantain cubes tossed in a little coconut oil. Bake 20 min at 200 °C, turning once.</p></div>
 <div class="box"><h3>3. Cassava Chin Chin</h3><p>Crunchy, egg-free and wheat-free — baked, not fried. Full recipe over the page.</p></div>
 <div class="box"><h3>4. Baked Akara Bites</h3><p>Fluffy bean balls baked in a mini muffin tin. Full recipe over the page.</p></div>
 <div class="box"><h3>5. Mini Moi Moi Cups</h3><p>Egg-free moi moi steamed in silicone cupcake cases — the perfect lunch box size.</p></div>
 <div class="box"><h3>6. Nut-Free Chicken Suya Sticks</h3><p>Chicken strips rubbed with ginger, paprika, garlic and onion powder (no groundnut). Bake 15 min at 220 °C.</p></div>
 <div class="box"><h3>7. Gizdodo Bites</h3><p>Cooked gizzard and ripe plantain cubes in a light pepper sauce. Pack in a small thermos.</p></div>
 <div class="box"><h3>8. Dundun Fries</h3><p>Yam sticks tossed in oil and salt, baked 25 min at 200 °C. Crispy outside, soft inside.</p></div>
 <div class="box"><h3>9. Ofio &amp; Coconut Mix</h3><p>Soaked tiger nuts with toasted coconut chips. Tiger nuts are tubers, not nuts — school-safe.</p></div>
 <div class="box"><h3>10. Zobo Ice Pops</h3><p>Hibiscus zobo with pineapple and ginger, sweetened with dates. Freeze in moulds — no sugar, no caffeine.</p></div>
</div>
<div class="callout terra"><div class="t">Watch out for</div><p>Shop-bought chin chin, puff-puff, meat pie and doughnuts (wheat &amp; egg), kokoro and popcorn (corn), and kuli kuli (groundnut).</p></div>
"""

NAIJA_RECIPES = [
    R("Crunchy Cassava Chin Chin", "40 min",
      ["2 cups cassava flour", "3 tbsp pure maple syrup", "½ tsp ground nutmeg, pinch of salt",
       "⅓ cup solid coconut oil", "About ⅓ cup coconut milk"],
      ["Heat oven to 180 °C / 350 °F. Line 2 trays with parchment.",
       "Mix flour, nutmeg and salt. Rub in the coconut oil with your fingers.",
       "Add the maple syrup, then coconut milk a little at a time, to make a firm dough.",
       "Roll out 5 mm thick and cut into small squares.",
       "Bake 15–20 min, stirring once, until golden. They crisp as they cool."],
      why="The chin chin every Nigerian child knows — with no wheat, no egg, no processed sugar and no deep frying.",
      tip="Let your child cut the squares with a blunt knife. Kids eat what they make.", tip_label="Picky eater trick",
      label="Naija snack"),
    R("Baked Akara Bites", "35 min + soaking",
      ["2 cups black-eyed beans, soaked & peeled", "1 small onion", "½ scotch bonnet (skip for young kids)",
       "½ tsp salt", "2–3 tbsp water", "Olive oil, for the tin"],
      ["Heat oven to 200 °C / 400 °F. Oil a mini muffin tin well.",
       "Blend beans, onion, pepper and salt with very little water to a thick paste.",
       "Whisk hard for 3 min until light and fluffy.",
       "Spoon into the tin and bake 20–25 min until golden.", "Cool and pack with a tomato dip."],
      why="Akara is naturally gluten-free and egg-free — full of plant protein.",
      tip="Bake a big batch on Sunday and freeze. Warm for 5 min before packing.", tip_label="Time saver",
      label="Naija snack"),
]

ALLERGY_CARD = """
<p class="muted">Print, cut out and give one to the teacher, nanny, grandparents or party host.</p>
""" + """<div class="cutcard">
<div class="kicker" style="margin-bottom:3mm">My allergy card</div>
<p><b>My name:</b> <span class="fill"></span></p>
<p><b>I cannot eat:</b> &nbsp;☐ Gluten (wheat) &nbsp;☐ Dairy (milk) &nbsp;☐ Corn &nbsp;☐ Egg &nbsp;☐ Caffeine &nbsp;☐ Tuna &nbsp;☐ Pork &nbsp;☐ Nuts</p>
<p><b>Other:</b> <span class="fill" style="min-width:120mm"></span></p>
<p><b>Safe snacks I can have:</b> <span class="fill" style="min-width:100mm"></span></p>
<p><b>If I eat something unsafe, please call:</b> <span class="fill" style="min-width:70mm"></span></p>
<p class="small muted" style="margin:0">Thank you for keeping me safe! ♥</p>
</div>""" * 2

# ---------------------------------------------------------------- detox book
DETOX_RULES = """
<p class="lead">Detox should be gentle. Our bodies — especially little bodies — clean themselves best when we go slowly and support them every day.</p>
<div class="grid2">
 <div class="box"><h3>Go slowly</h3><ul>
  <li>Children start with ¼–½ cup. Adults, 1 cup.</li>
  <li>One new drink at a time.</li>
  <li>Tummy ache, rash, poor sleep or crankiness? Use less and go slower.</li></ul></div>
 <div class="box"><h3>Every day</h3><ul>
  <li>Drink plenty of water.</li>
  <li>Add seeds for fibre: chia, flax, pumpkin, sunflower, psyllium.</li>
  <li>Bounce on a trampoline or dance — it moves the lymph system.</li>
  <li>Lemon balm 2 hours before bed for better sleep.</li></ul></div>
 <div class="box"><h3>Keep it fresh</h3><ul>
  <li>Wash fruit and vegetables well — pesticides are something we reduce.</li>
  <li>Drink juices within 30 minutes of making them.</li>
  <li>Use glass or stainless-steel cups.</li></ul></div>
 <div class="box"><h3>Safety first</h3><ul>
  <li>No honey for babies under 1 year.</li>
  <li>Ask your doctor before herbs or supplements, especially with medication, pregnancy or breastfeeding.</li>
  <li>Sea moss is rich in iodine — check first if there is a thyroid condition.</li></ul></div>
</div>
<div class="callout"><div class="t">Smoothie or juice?</div>
<p><b>Smoothies</b> keep the fibre — more filling and great for bowels. <b>Juices</b> remove the fibre — lighter and quickly absorbed. No juicer? Blend, then strain through a clean cloth or sieve.</p></div>
"""

DETOX = [
    R("The Daily Detox Smoothie", "5 min",
      ["1 celery stick", "½ green apple", "Handful of blueberries", "1 tbsp fresh coriander (cilantro)",
       "1 tbsp fresh parsley", "1 cup water (or more)"],
      ["Wash everything well.", "Blend until smooth.", "Drink fresh, in the morning."],
      goodfor=["Gentle daily cleanse", "Bowels", "Hydration", "Antioxidants"],
      why="Celery is the foundation. Apple adds binding fibre. Coriander and parsley are traditional cleansing herbs.",
      tip="Children: start with half a cup. Detox should be slow and gentle.", tip_label="Go slowly",
      label="Day 1", region="Author's recipe"),
    R("Boosted Detox Smoothie", "5 min",
      ["Everything from Day 1", "¼ tsp spirulina powder", "¼ tsp lion's mane powder", "Brahmi (bacopa) — adults only"],
      ["Make the Day 1 smoothie.", "Add the spirulina and lion's mane.", "Blend again and drink fresh."],
      goodfor=["Brain & focus", "Mould & yeast support", "Energy"],
      why="Spirulina is rich in iron and protein. Lion's mane is a mushroom traditionally used for focus.",
      tip="Ask your child's doctor before adding any herb or supplement, especially with medication.",
      tip_label="Safety first", label="Day 2", region="Author's recipe"),
    R("Sea Moss & Black Seed Gut Soother", "5 min",
      ["1 tsp sea moss gel (children) or 1 tbsp (adults)", "1 ripe banana", "½ cup pineapple",
       "1 cup coconut water", "½ tsp black seed oil (age 3+, 3 times a week)"],
      ["Blend everything until creamy.", "Drink straight away.", "Use black seed oil only 3 times a week."],
      goodfor=["Gut", "Skin & eczema", "Immunity"],
      why="Sea moss and black seed oil are the author's go-to pair for gut troubles.",
      tip="Sea moss is rich in iodine. If there's a thyroid condition, ask your doctor first.",
      tip_label="Safety first", label="Day 3", region="Author's recipe"),
    R("Lemon Balm Bedtime Tea", "10 min",
      ["1 tbsp dried lemon balm (or 6 fresh leaves)", "1 cup hot water", "Slice of lemon",
       "1 tsp honey (optional — not under age 1)"],
      ["Pour hot water over the lemon balm.", "Cover and steep 5–7 min, then strain.",
       "Cool until warm. Add lemon and honey.", "Drink about 2 hours before bedtime."],
      goodfor=["Sleep", "Calm", "Tummy"],
      why="Lemon balm is the author's favourite herb for sleep — calming and naturally caffeine-free.",
      label="Day 4", region="Author's recipe"),
    R("Morning Celery Juice", "10 min",
      ["1 bunch celery (makes about 1 cup)", "½ green apple (optional, for children)"],
      ["Wash the celery well and chop.", "Juice — or blend with ¼ cup water and strain.",
       "Drink on an empty stomach, 15–30 min before breakfast."],
      goodfor=["Digestion", "Hydration", "Liver support"],
      why="Celery is the foundation of the author's daily detox.",
      tip="Children: start with ¼ cup mixed with apple. Build up slowly.", tip_label="Go slowly", label="Day 5"),
    R("Watermelon Cucumber Cooler", "5 min",
      ["2 cups watermelon, cubed", "½ cucumber", "4 fresh mint leaves", "Squeeze of lime"],
      ["Blend everything until smooth.", "Strain if you like it smooth.", "Serve over ice."],
      goodfor=["Constipation", "Hydration", "Kidneys"],
      why="Watermelon and cucumber are on the author's constipation list — full of water and gentle fibre.",
      label="Day 6"),
    R("Broccoli Sprout Mango Smoothie", "5 min",
      ["Small handful of broccoli sprouts", "1 cup mango, fresh or frozen", "½ ripe banana",
       "1 cup coconut water", "Squeeze of lime"],
      ["Rinse the sprouts well.", "Blend everything until smooth.", "Drink fresh."],
      goodfor=["Antioxidants", "Brain support", "Cell repair"],
      why="Broccoli sprouts are top of the author's greens list. Mango hides the green taste.",
      tip="Grow your own: soak broccoli seeds in a jar, rinse twice a day — ready in 5 days.", tip_label="Fun idea",
      label="Day 7"),
]


def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def pages():
    # ---------------- Healing Plates
    yield BOOK1, "cover", dict(series="The 30-Day Allergy-Free Family Meal Plan", title=BOOK1, logo="plates",
        subtitle="Breakfast, lunch & dinner free from gluten, dairy, corn, egg, caffeine, tuna & processed sugar",
        tagline="Finally… food the whole family can eat.", free=FREE, badge=("90", "family<br>meals"), author=AUTHOR)
    yield BOOK1, "text", WELCOME
    yield BOOK1, "text", dict(kicker="Know before you shop", title="Where allergens hide", html=FREE_FROM_HTML)
    yield BOOK1, "text", dict(kicker="Restoring the gut", title="5 steps to healing the gut", html=GUT_HTML)
    yield BOOK1, "cards", dict(kicker="Make once, use all month", title="Kitchen basics", recipes=BASICS[:3], kind="breakfast")
    yield BOOK1, "cards", dict(recipes=BASICS[3:], kind="breakfast")
    yield BOOK1, "calendar", dict(kicker="Your week at a glance", title="Week 1",
        weeks=[[dict(day=i + 1, meals=[("b", "B", w[0]), ("l", "L", w[1]), ("d", "D", w[2])]) for i, w in enumerate(WEEK1_NAMES)]])
    yield BOOK1, "grocery", dict(kicker="Tick as you shop", title="Week 1 shopping list",
        intro="Everything for Days 1–7. Cross off what you already have.", cats=GROCERY)
    for d in DAYS:
        yield BOOK1, "day", d
    yield BOOK1, "two", dict(kind="treat", recipes=treats,
        note="Every Friday is <b>Sweet Treat Day</b> — because healing food should still feel like a celebration.")
    yield BOOK1, "brands", dict(kicker="Make shopping easier", title="Allergy-friendly brands near you",
        intro="Always read the label — brands can change their recipes. Many gluten-free products still contain corn or egg.",
        regions=BRANDS)

    # ---------------- Healing Lunch Box
    yield BOOK2, "cover", dict(series="Bonus Book 1", title=BOOK2, logo="box",
        subtitle="30 Days of Allergy-Free School Lunches & Snacks Kids Will Actually Eat",
        tagline="Nut-free and school-safe.", free=FREE + ["Nut"], badge=("30", "lunch<br>boxes"), author=AUTHOR)
    yield BOOK2, "text", dict(kicker="Before you start", title="7 golden lunch box rules", html=LUNCH_RULES)
    for pair in chunks(LUNCHBOXES, 2):
        yield BOOK2, "two", dict(kind="lunchbox", recipes=pair)
    yield BOOK2, "text", dict(kicker="Snack attack", title="10 snacks kids can't say no to", html=SNACKS_HTML)
    yield BOOK2, "text", dict(kicker="Taste of home", title="Naija snack corner", html=NAIJA_HTML)
    yield BOOK2, "two", dict(kind="lunchbox", recipes=NAIJA_RECIPES)

    # ---------------- Healing Sips
    yield BOOK3, "cover", dict(series="Bonus Book 2", title=BOOK3, logo="sips",
        subtitle="The 30-Day Gentle Detox & Juicing Plan for the Whole Family",
        tagline="One gentle glass a day.", free=FREE, badge=("30", "detox<br>recipes"), author=AUTHOR)
    yield BOOK3, "text", dict(kicker="Before you start", title="The gentle way to detox", html=DETOX_RULES)
    for pair in chunks(DETOX, 2):
        yield BOOK3, "two", dict(kind="detox", recipes=pair)

    # ---------------- Healing Printables
    yield BOOK4, "cover", dict(series="Bonus Book 3", title=BOOK4, logo="print",
        subtitle="Allergy cards, trackers, charts & planners to make every day easier",
        tagline="Print. Stick on the fridge. Breathe.", free=FREE, badge=("8", "pages<br>to print"), author=AUTHOR)
    yield BOOK4, "text", dict(kicker="Printable 1", title="Allergy cards", html=ALLERGY_CARD, white=True)
    yield BOOK4, "text", dict(kicker="Printable 2", title="Food & mood tracker · Days 1–15", html=tracker(1, 15), white=True)
    yield BOOK4, "text", dict(kicker="Printable 2", title="Food & mood tracker · Days 16–30", html=tracker(16, 30), white=True)
    yield BOOK4, "text", dict(kicker="Printable 3 · Stick it on the fridge", title="Smart swaps cheat sheet", html=SWAP_HTML, white=True)
    yield BOOK4, "text", dict(kicker="Printable 4", title="I tried it!", html=REWARD_HTML, white=True)
    yield BOOK4, "text", dict(kicker="Printable 5", title="Weekly meal planner", html=PLANNER_HTML, white=True)
    yield BOOK4, "text", dict(kicker="Printable 6", title="My shopping list", html=SHOP_HTML, white=True)
    yield BOOK4, "text", dict(kicker="Printable 7", title="My child's safe foods", html=SAFE_HTML, white=True)

    # ---------------- Healing Celebrations
    yield BOOK5, "cover", dict(series="Bonus Book 4", title=BOOK5, logo="party",
        subtitle="A real birthday cake, party food & a survival guide for parties, church events and eating out",
        tagline="Every child deserves a slice.", free=FREE + ["Nut"], badge=("5", "party<br>recipes"), author=AUTHOR)
    yield BOOK5, "cards", dict(kicker="The star of the party", title="A real birthday cake", kind="treat", recipes=[CAKE],
        intro="Every child deserves to blow out candles on a cake they can actually eat.", after=CAKE_TIPS)
    for pair in chunks(PARTY, 2):
        yield BOOK5, "two", dict(kind="treat", recipes=pair)
    yield BOOK5, "text", dict(kicker="Be prepared", title="Party survival guide", html=PARTY_HTML)
