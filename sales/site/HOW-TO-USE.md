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
