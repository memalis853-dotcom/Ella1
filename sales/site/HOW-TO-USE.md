# How to put the sales page online

The page is `index.html`. The pictures are in the `img` folder.

## Step 1: Add your Selar link (required)
Open `index.html` in any text editor (Notepad, TextEdit or VS Code).
Use **Find & Replace** to change every `https://selar.co/YOUR-LINK` to your real Selar product link. There are 5 buttons.

## Option A: Elementor (WordPress)
1. In WordPress, go to **Media → Add New** and upload all 14 pictures from the `img` folder.
2. Click one uploaded picture and copy its URL. It will look like
   `https://yoursite.com/wp-content/uploads/2026/11/hc-bundle.jpg`.
   Keep the part **before** the file name, e.g. `https://yoursite.com/wp-content/uploads/2026/11/`.
3. In `index.html`, use Find & Replace to change `img/` to that address.
4. Create a new page and choose **Elementor Canvas** (Page Attributes → Template) so the page is full-width with no theme header.
5. Edit with Elementor and drag in an **HTML** widget.
6. Copy everything from `<link rel="preconnect"` down to the last `</div>` before `</body>`, and paste it into the HTML widget.
7. Click **Update** and preview on your phone.

## Option B: No WordPress
Upload the whole `site` folder (index.html + img) to any simple host: Netlify Drop (drag and drop), GitHub Pages or your web host's file manager. The page works as it is.

## Before you go live
- Replace the 3 testimonial boxes with **real** parent reviews (first name and country), or delete that section until you have some.
- If you offer a money-back promise, add a line above the final button.
- Test every button. Each one should open your Selar checkout at $14.99.

---

# Thank-you page & sales tracking

`thank-you.html` is the page buyers see straight after paying. It welcomes them, explains how to download, gives 5 first steps, and **counts the sale** in Meta (Facebook/Instagram) and Google Analytics.

## 1. Fill in your details
Open `thank-you.html` and use Find & Replace:
- `YOUR_PIXEL_ID` → your Meta Pixel ID (Meta Events Manager → Data sources → your Pixel)
- `G-XXXXXXXXXX` → your Google Analytics 4 ID (or delete the Google script block if you don't use it)
- `YOUR-EMAIL@hindsfeetglobal.com` → your support email
- `https://chat.whatsapp.com/YOUR-GROUP-LINK` → your WhatsApp group link (or delete that box)
- `https://YOUR-SALES-PAGE-LINK` → your sales page address

Do the same `YOUR_PIXEL_ID` and `G-XXXXXXXXXX` replacements in `index.html`, the sales page.

## 2. Put the thank-you page online
Same as the sales page: in Elementor, create a page called “Thank You” with **Elementor Canvas** and paste the code into an **HTML** widget. Copy everything from `<link rel="preconnect"` to the last `</div>`, including the `<script>` tracking blocks. Then, in the page settings, hide the page from search engines and menus.

## 3. Connect it to Selar
In your Selar product settings, find the option to **redirect buyers after purchase** (sometimes called “Redirect URL” or “Thank-you page”) and paste your thank-you page link. Then only buyers will land on it, so every visit equals one sale.
If you can't find this option, ask Selar support. Selar also has its own Facebook Pixel setting. **Use only one** (Selar's pixel *or* this thank-you page), or each sale will be counted twice.

## 4. Test it
Use Meta's **Test Events** tool (Events Manager → Test events), open your thank-you page, and check that “Purchase $14.99” appears. A refresh will not count a second sale.

## What you'll see
| Event | Where it fires | What it tells you |
|---|---|---|
| PageView / ViewContent | Sales page | How many people saw the page from each ad |
| InitiateCheckout | Click on any Buy button | How many wanted to buy |
| Purchase ($14.99) | Thank-you page | Real sales, linked to the ad that brought them |

In Meta Ads Manager, set your campaign goal to **Sales → Purchase**, so Meta shows your ads to people most likely to buy.
