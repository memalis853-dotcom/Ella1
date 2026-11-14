// Builds the Dairy-Free & Gluten-Free Swap Guide (.docx)
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  HeadingLevel, AlignmentType, BorderStyle, LevelFormat, Footer, PageNumber } = require('docx');

const RED = 'B3261E', GREEN = '2E7D4F', FONT = 'Calibri';
const W = 9360; // content width (Letter, 1" margins)

const p = (text, o = {}) => new Paragraph({ spacing: { after: 100 }, ...o.para,
  children: [].concat(text).map(t => typeof t === 'string' ? new TextRun({ text: t, ...o.run }) : t) });
const b = t => new TextRun({ text: t, bold: true });
const bullet = (runs) => new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 60 },
  children: [].concat(runs).map(t => typeof t === 'string' ? new TextRun(t) : t) });

const border = { style: BorderStyle.SINGLE, size: 4, color: 'D9CABD' };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(text, width, head, free) {
  const runs = [].concat(text).map(t => typeof t === 'string'
    ? new TextRun({ text: t, bold: head || free, color: head ? 'FFFFFF' : (free ? GREEN : undefined) }) : t);
  return new TableCell({ borders, width: { size: width, type: WidthType.DXA },
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    shading: head ? { fill: RED, type: ShadingType.CLEAR, color: 'auto' } : undefined,
    children: [new Paragraph({ children: runs })] });
}
function table(headers, rows, widths = [3600, 5760]) {
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths, rows: [
    new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, widths[i], true)) }),
    ...rows.map(r => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i], false, i === 1 && /^Already/.test(c))) })),
  ] });
}
const gap = () => new Paragraph({ spacing: { after: 120 }, children: [] });
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const FREE = 'Already DF & GF';

const children = [
  new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('Dairy-Free & Gluten-Free Swap Guide')] }),
  p('How to make every dish on the menu dairy-free (DF) and gluten-free (GF)', { run: { italics: true, color: '6B5A4E', size: 26 } }),
  p(['Good news: ', b('more than half of the menu is already dairy-free and gluten-free.'),
     ' Only dishes with flour, bread, pasta, butter, cream, cheese or soy sauce need changes. Dishes marked ',
     new TextRun({ text: FREE, bold: true, color: GREEN }), ' need no changes at all.']),

  h1('Basic Swap Chart'),
  p('These swaps work for any recipe.'),
  table(['Instead of', 'Use'], [
    ['Wheat flour (frying, coating)', 'Rice flour, cornstarch, cassava flour'],
    ['Wheat flour (baking)', 'GF all-purpose flour blend (with xanthan gum), cassava or plantain flour'],
    ['Flour to thicken sauces', 'Cornstarch or arrowroot (mix with cold water first)'],
    ['Breadcrumbs', 'GF breadcrumbs, crushed GF crackers, GF-labelled cornflakes'],
    ['Pasta / noodles', 'GF pasta (rice, corn, chickpea, lentil), rice noodles'],
    ['Bread, wraps, naan', 'GF bread, GF wraps, corn tortillas'],
    ['Soy sauce', 'Tamari (GF) or coconut aminos'],
    ['Butter', 'Dairy-free butter (e.g. Violife), olive oil, coconut oil'],
    ['Milk', 'Oat, almond, soy or coconut milk'],
    ['Cream', 'Coconut cream or blended cashew cream'],
    ['Buttermilk', 'Oat milk + 1 tbsp lemon juice per cup'],
    ['Cheese', 'Dairy-free cheese (Daiya, Violife) or nutritional yeast for a "cheesy" taste'],
    ['Yogurt', 'Coconut or oat yogurt'],
    ['Cream cheese', 'Dairy-free cream cheese (Kite Hill, Violife)'],
    ['Whipped cream', 'Whipped coconut cream'],
  ]),
  gap(),
  p([b('Watch for hidden gluten and dairy: '), 'some seasoning cubes, curry powders, BBQ sauce, Worcestershire sauce, sausages, frozen hash browns and suya spice blends contain wheat or milk. Always read the label.'],
    { para: { shading: { fill: 'FBEFE7', type: ShadingType.CLEAR, color: 'auto' }, border: { left: { style: BorderStyle.SINGLE, size: 18, color: RED, space: 8 } } } }),

  h1('Stews & Sauces'),
  table(['Dish', 'Change needed'], [
    ['Buka Stew, Curry Goat, Nigerian Turkey Sauce, Ofada Sauce, Ofe Akwu, Vegetable Sauce', FREE + ' (check seasoning cubes and curry powder)'],
    ['Oxtail Sauce', 'Usually free. If you dust the oxtail in flour, use cornstarch'],
    ['Fish in Chilli Sauce', 'Coat the fish in rice flour or cornstarch instead of flour'],
    ['Beef Goulash', 'Thicken with cornstarch; sour cream → coconut yogurt'],
    ['Bolognese Sauce', 'Usually free. Skip the parmesan or use nutritional yeast'],
    ['Butter Chicken Curry', 'Butter → coconut oil or DF butter; cream → coconut cream; yogurt marinade → coconut yogurt'],
    ['Casserole Sauce', 'Thicken with cornstarch, not flour'],
    ['Sweet and Sour Beef', 'Soy sauce → tamari; batter → cornstarch'],
  ]),

  h1('Pasta & Noodles'),
  p([b('For all pasta dishes: '), 'use GF pasta (rice, corn or chickpea). Cook it 1–2 minutes less than the packet says, because it goes soft quickly.']),
  table(['Dish', 'Change needed'], [
    ['Asun Pasta, Prawn Native Pasta, Spicy Beef Penne', 'GF pasta only; the rest is already free'],
    ['Singapore Noodles, Spicy Chili Garlic Noodles', 'Rice noodles + tamari instead of soy sauce'],
    ['Creamy Chicken Alfredo', 'Cream → coconut or cashew cream; parmesan → nutritional yeast; butter → olive oil'],
    ['Creamy Jollof Pasta', 'Cream → coconut milk'],
    ['Seafood Pasta', 'GF pasta; if creamy, use coconut cream'],
    ['Pesto Pasta', 'Pesto without parmesan (add nutritional yeast)'],
    ['Spaghetti and Meatballs', 'Meatballs: GF breadcrumbs or cooked rice instead of breadcrumbs; no cheese'],
    ['Lasagna', 'GF lasagna sheets; white sauce from GF flour + oat milk + DF butter; DF cheese on top'],
    ['Mac and Cheese', 'GF macaroni; "cheese" sauce from DF cheese, or blended boiled potato + carrot + nutritional yeast + oat milk'],
    ['Pasta (from scratch)', 'GF flour blend + eggs + a little xanthan gum (cassava flour also works)'],
  ]),

  h1('Rice'),
  table(['Dish', 'Change needed'], [
    ['Asun Jollof, Asun Rice, Banga Rice, Caribbean Rice and Peas, Coconut Jollof, Dirty Rice, Local Rice, Native Rice, Signature Coconut Rice, Smokey Jollof, Suya Rice', FREE],
    ['Jambalaya Rice', 'Free if the sausage is GF (check the label)'],
    ['Flavoured Herb Rice', 'Butter → olive oil or DF butter'],
    ['Chinese Rice, Special Fried Rice, Pineapple Fried Rice', 'Soy sauce → tamari or coconut aminos'],
    ['Chicken Biryani', 'Yogurt marinade → coconut yogurt; ghee → oil'],
  ]),

  h1('Soups'),
  p([new TextRun({ text: 'All soups are already DF & GF: ', bold: true, color: GREEN }),
     'Afang, Banga, Black Soup, Edikang-Ikong, Editan, Efo Riro, Egusi, Ewedu, Fisherman, Gbegiri, Groundnut, Nsala, Ogbono, Oha, Seafood Okra, Waterleaf.']),
  p([b('Watch the swallow: '), 'semolina and wheat swallow contain gluten. Serve with eba (garri), pounded yam, amala, fufu or plantain fufu instead.']),

  h1('Porridges'),
  p([new TextRun({ text: 'All already DF & GF: ', bold: true, color: GREEN }),
     'Adalu (Beans and Corn), Ekpang Nkukwo, Ewa Agoyin, Fried Beans Porridge, Ikokore, Oxtail and Plantain Porridge.']),
  p('Ewa Agoyin is usually eaten with bread: serve it with GF bread or dodo.', { run: { italics: true } }),

  h1('Grills'),
  table(['Dish', 'Change needed'], [
    ['Grilled Fish, Rotisserie Chicken', FREE],
    ['T-bone Beef Steak', 'Baste with olive oil instead of butter'],
    ['Honey BBQ Chicken Wings', 'Use a GF BBQ sauce, or make your own with honey, tomato paste, tamari and spices'],
  ]),

  h1('Sides'),
  table(['Dish', 'Change needed'], [
    ['Fish Pepper Soup, Fluffy Moimoi, Grilled Prawns, Grilled Turkey, Hummus, Kelewele, Nkwobi, Peppered Goat Meat, Sorbet, Suya', FREE + ' (check the suya spice label)'],
    ['Hash Browns', 'Homemade is free; some frozen brands contain wheat'],
    ['Stuffed Masa', 'Use only rice flour, no wheat flour'],
    ['Nigerian Full Salad', 'Use dairy-free mayo or salad cream (check the label)'],
    ['Chicken Caesar Salad', 'DF Caesar dressing (DF mayo, lemon, mustard, garlic, nutritional yeast); croutons → roasted chickpeas or GF croutons'],
    ['Naan Bread', 'GF naan: GF flour + coconut yogurt + baking powder'],
    ['Sushi', 'Tamari instead of soy sauce; no imitation crab (it contains wheat); no cream cheese'],
  ]),

  h1('Breakfast'),
  table(['Dish', 'Change needed'], [
    ['Akara', FREE],
    ['Yamarita', 'Coat in egg + rice flour or cornstarch instead of wheat flour'],
    ['Buttered Potatoes', 'Olive oil or DF butter'],
    ['Creamy Mashed Potatoes', 'Oat milk + DF butter or olive oil'],
    ['Chicken and Chips, Crispy Fried Chicken', 'Rice flour + cornstarch coating; "buttermilk" from oat milk + lemon; fry in clean oil not used for wheat items'],
    ['Potato Balls', 'No milk; bind with egg and coat in GF breadcrumbs or cornstarch'],
    ['Frittata', 'No cheese; use oat milk instead of milk'],
    ['Flavoured Pancakes, Waffles', 'GF flour blend + oat milk + DF butter or oil'],
    ['Garlic Bread', 'GF bread + olive oil or DF butter + garlic'],
    ['Cream Cheese Bread, Milk Bread', 'GF bread recipe with oat milk; DF cream cheese'],
    ['Grilled Cheese Sandwich', 'GF bread + DF cheese'],
    ['Shawarma', 'GF wraps; garlic sauce made with DF mayo, or toum (garlic + oil + lemon, naturally DF)'],
    ['Sub Sandwich, Turkey Sandwich, Tortilla Vegetable Wrap', 'GF bread or wraps; DF cheese and DF mayo'],
  ]),

  h1('Desserts & Iced Treats'),
  table(['Dish', 'Change needed'], [
    ['Berry Mix Popsicles', FREE],
    ['Apple Pie', 'GF crust: GF flour + DF butter or coconut oil'],
    ['Blueberry, Chocolate Chip and Cookies & Cream Ice Cream', 'Coconut-milk or oat-milk ice cream base; GF chocolate sandwich cookies'],
    ['Cookies & Cream Crumble', 'GF chocolate sandwich cookies + DF butter (check the cookie label for milk)'],
    ['Panna Cotta', 'Coconut milk + agar-agar or gelatin'],
    ['Parfait', 'Coconut or oat yogurt + GF granola + fruit'],
    ['Velvet Cheesecake', 'Filling: DF cream cheese or soaked cashews; base: GF biscuits + DF butter'],
    ['Eggnog', 'Oat or almond milk + coconut cream'],
    ['Cookies & Cream Milkshake', 'Oat milk + DF ice cream + GF cookies'],
    ['Waffles and Ice Cream', 'GF waffles + DF ice cream'],
    ['Irish Cream Milkshake', 'Use a DF Irish-cream-flavour syrup instead of the alcoholic liqueur'],
  ]),

  h1('Drinks & Mocktails'),
  p([new TextRun({ text: 'All free, or easy to make free: ', bold: true, color: GREEN }),
     'Zobo, Tigernut (Kunun Aya), Tropical Juice, Kiwi Fizz and Wavy are naturally DF & GF. Make Blue Pina Colada with coconut cream.']),
  p([b('Cocktails: '), 'most spirits and wines are gluten-free. Make Whipped Cream Mimosa with whipped coconut cream. Selling alcohol in Ontario needs a licence, so keep cocktails off food ads.']),

  h1('Summary'),
  bullet([new TextRun({ text: 'Already DF & GF (no changes): ', bold: true, color: GREEN }), 'all soups, all porridges, most rice dishes, most Nigerian stews, grilled fish and chicken, suya, moimoi, akara, kelewele, zobo, tigernut.']),
  bullet([b('Easy swaps: '), 'pasta, fried rice, fried chicken, breakfast items, desserts.']),
  bullet([b('Harder to make free: '), 'bread-based items (milk bread, cream cheese bread, naan). Buy good GF bread instead of baking it.']),
  p([b('Business tip: '), 'the "already free" list is a selling point. Advertise a "Dairy-Free & Gluten-Free Naija Menu" right away with soups, jollof, suya, moimoi, porridges and grills, and add the swapped dishes as you test them.'], { para: { spacing: { before: 160 } } }),
];

const doc = new Document({
  creator: 'Ella', title: 'Dairy-Free & Gluten-Free Swap Guide',
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: FONT, size: 48, bold: true, color: RED }, paragraph: { spacing: { before: 0, after: 80 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 30, bold: true, color: RED },
        paragraph: { spacing: { before: 320, after: 120 }, keepNext: true, outlineLevel: 0,
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'E7D9CD', space: 2 } } } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 24, bold: true }, paragraph: { spacing: { before: 200, after: 80 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: 'Dairy-Free & Gluten-Free Swap Guide  ·  Page ', size: 18, color: '8A776A' }),
      new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '8A776A' })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(__dirname + '/df-gf-swap-guide.docx', buf); console.log('ok'); });
