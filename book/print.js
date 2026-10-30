// Print an HTML book to PDF, warn about overflowing pages, and save PNG previews.
// Usage: node print.js <in.html> <out.pdf> <png-dir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [inHtml, outPdf, pngDir] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 } });
  await page.goto('file://' + path.resolve(inHtml));
  await page.evaluate(() => document.fonts.ready);

  const overflow = await page.$$eval('.page', els => els.map((el, i) => {
    const inner = el.querySelector('.inner') || el;
    const footer = el.querySelector('.footer');
    const limit = footer ? footer.getBoundingClientRect().top : el.getBoundingClientRect().bottom;
    let bottom = 0;
    inner.querySelectorAll('*').forEach(c => { if (c.closest('.footer')) return; bottom = Math.max(bottom, c.getBoundingClientRect().bottom); });
    return bottom > limit + 1 ? i + 1 : null;
  }).filter(Boolean));
  if (overflow.length) console.log('OVERFLOW on pages:', overflow.join(', '));

  await page.pdf({ path: outPdf, preferCSSPageSize: true, printBackground: true });

  if (pngDir) {
    fs.mkdirSync(pngDir, { recursive: true });
    const pages = await page.$$('.page');
    for (let i = 0; i < pages.length; i++) {
      await pages[i].screenshot({ path: path.join(pngDir, `p${String(i + 1).padStart(2, '0')}.png`) });
    }
  }
  await browser.close();
  console.log('wrote', outPdf);
})();
