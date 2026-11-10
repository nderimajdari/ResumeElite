"""Render a static WebP image of every template into /img/templates/.

The template previews on the site are drawn by app.js at runtime, which means
search engines see an empty <div role="img">. These files give the generated
pages a real <img> (indexable in Google Images, usable as og:image) and spare
the browser from building the markup of every card.

Needs Playwright + Pillow:  pip install playwright pillow && playwright install chromium
Run from the repo root:      python build/render_thumbs.py   (then python build/build.py)
Re-run whenever a template's design changes.
"""
import functools
import http.server
import io
import os
import sys
import threading

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "templates")
SIZES = {"": 1000, "-400": 400}   # suffix -> pixel width
OG_W, OG_H = 1200, 630


def main(only):
    os.makedirs(OUT, exist_ok=True)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    handler.log_message = lambda *a: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d" % srv.server_address[1]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 1300}, device_scale_factor=1000 / 794)
        page.goto(base + "/editor.html")          # the template picker lists every id
        page.wait_for_function("document.querySelectorAll('.tmpl-btn').length > 0")
        ids = page.evaluate("getTemplateIds()")
        page.goto(base + "/ats-resume-templates/")
        page.wait_for_function("typeof buildTemplateThumbnailHtml === 'function'")
        if only:
            ids = [i for i in ids if i in only]
        page.evaluate("""() => {
          document.body.innerHTML = '<div id="shot" data-live-thumb="x" data-thumb-painted="1" '
            + 'style="position:absolute;left:0;top:0;width:794px;height:1122px;overflow:hidden;background:#fff"></div>';
          document.body.style.margin = '0';
        }""")
        for tid in ids:
            page.evaluate("""(t) => {
              const el = document.getElementById('shot');
              el.innerHTML = thumbnailPageHtml(t, buildTemplateThumbnailHtml(t));
              el.style.setProperty('--thumb-scale', '1');
            }""", tid)
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(150)
            png = page.locator("#shot").screenshot()
            img = Image.open(io.BytesIO(png)).convert("RGB")
            for suffix, width in SIZES.items():
                h = round(width * 1122 / 794)
                img.resize((width, h), Image.LANCZOS).save(
                    os.path.join(OUT, "%s%s.webp" % (tid, suffix)), "WEBP", quality=82, method=6)
            # Social card: the top of the resume on a soft backdrop, 1200x630.
            card = Image.new("RGB", (OG_W, OG_H), (226, 232, 240))
            w = 560
            top = img.resize((w, round(w * 1122 / 794)), Image.LANCZOS).crop((0, 0, w, OG_H - 50))
            card.paste(top, ((OG_W - w) // 2, 50))
            card.save(os.path.join(OUT, "%s-og.jpg" % tid), "JPEG", quality=84, optimize=True)
            print(tid)
        browser.close()
    srv.shutdown()


if __name__ == "__main__":
    main(sys.argv[1:])
