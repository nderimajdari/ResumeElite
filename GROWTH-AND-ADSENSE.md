# ResumeElite — traffic growth and AdSense readiness

Last updated: 2026-08-24

Two things happened in this pass: the site went from 7 pages to 32 and from
~4,800 words to ~31,500, and the monetisation and consent infrastructure AdSense
reviews against was built. This document covers what exists, the exact steps to
apply, and what to do next.

---

## Part 1 — Do these before you apply

Six steps. Nothing else on this page is blocking.

### 1. Deploy and let Google crawl it (wait ~1–2 weeks)

**This is the step people skip and it is the most common cause of rejection.**
AdSense reviews the live site. A site published yesterday with no indexed pages
looks like a site with no content, regardless of how good the content is.

```bash
git add -A && git commit -m "Content build: categories, blog, template guides, consent" && git push
```

Then in [Google Search Console](https://search.google.com/search-console):

1. Verify `resume-elite.com` (DNS TXT is the most durable method)
2. Submit `https://resume-elite.com/sitemap.xml`
3. Use URL Inspection → Request Indexing on `/`, `/blog/`, and two or three
   category pages to prime the crawl
4. Wait until **Pages → Indexed** shows at least 15–20 URLs

That wait is not optional. Apply before it and you are likely to get
"Low value content" and then have to wait out a re-application anyway.

### 2. Apply to AdSense

[google.com/adsense](https://www.google.com/adsense/start/) → add
`resume-elite.com`. Google gives you a verification snippet; the site already has
the plumbing, so you only need to fill in one value:

```python
# build/sitecfg.py
ADSENSE_CLIENT = "ca-pub-0000000000000000"   # your real publisher ID
```

Then:

```bash
python build/build.py
```

Every page picks it up, because `head_common()` is injected through the
`HEADSCRIPTS` marker on all 32 pages.

### 3. Fill in ads.txt

`ads.txt` currently contains only comments, on purpose — a placeholder publisher
ID would declare an invalid seller, which is worse than an absent file. Once
approved, AdSense shows you one line under **Sites → Ads.txt**. Replace the whole
file with it:

```
google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0
```

Or just set `ADSENSE_CLIENT` and re-run the build — it generates this file
automatically from that value.

### 4. Turn on Google's certified CMP for EEA/UK

**Important and frequently misunderstood.** Serving ads to visitors in the EEA,
UK or Switzerland requires a *Google-certified* Consent Management Platform. The
consent bar in `consent.js` is a correct Consent Mode v2 implementation, but a
self-hosted banner is not certified and cannot substitute for one there.

In AdSense: **Privacy & messaging → GDPR → Create message**. It is free and takes
about five minutes.

`consent.js` is built to cooperate rather than conflict: it detects the TCF API
(`window.__tcfapi`) and, when Google's CMP is present, it suppresses its own
banner and takes consent signals from the CMP instead. So enabling the Google
message is safe — you will not get two banners.

The built-in bar keeps handling non-EEA traffic, where it is sufficient.

### 5. Add Google Analytics (optional but recommended)

```python
# build/sitecfg.py
GA4_ID = "G-XXXXXXXXXX"
```

It loads only after consent, with `anonymize_ip` on. Without it you are flying
blind on which guides earn traffic.

### 6. Re-verify

```bash
python build/build.py
node --check app.js
python -c "import io;s=io.open('styles.css',encoding='utf-8').read();print('braces balanced:', s.count('{')==s.count('}'))"
```

Then check `/` and `/blog/how-to-write-a-resume/` in the
[Rich Results Test](https://search.google.com/test/rich-results) and confirm the
FAQ and Article blocks are eligible.

---

## Part 2 — What AdSense checks, and where it now stands

| Requirement | Status | Where |
|---|---|---|
| Substantial original content | **31,500 words over 32 pages** | 6 category pages, 10 guides, 8 template guides |
| Privacy policy naming AdSense | Done | `privacy.html`, 14 sections |
| Cookie policy with named cookies | Done | `cookies.html` (new) |
| Real About page | Done — 900 words, states the business model | `about.html` |
| Working Contact page | Done — form plus what we can and cannot help with | `contact.html` |
| Terms and disclaimer | Already present | `terms.html`, `disclaimer.html` |
| Clear navigation | Done — nav, collections strip, breadcrumbs, footer | every page |
| Consent Mode v2, denied by default | Done | `consent.js` + inline head block |
| ads.txt | Ready, inert until you paste the line | `ads.txt` |
| No prohibited content | Reviewed | — |
| Site works on mobile | Verified 360/390/820/1440/1920, zero overflow | — |
| Placeholder text removed | Fixed | see below |

Two specific things that would likely have caused a rejection and are now fixed:

**The privacy policy contained boilerplate placeholder text.** It read "to serve
ads to our site visitors based upon their visit to `www.website.com`" — an
unedited template left in place. A reviewer reading the privacy policy would have
seen it immediately. The policy has been rewritten to describe what this site
actually does.

**The site was too thin.** 4,800 words across 7 pages, of which three were legal
boilerplate and one was a JavaScript app shell. That is the profile that gets
"Low value content".

---

## Part 3 — How the monetisation is set up

### Ad placement

| Page type | Slots | Position |
|---|---|---|
| Homepage | 1 | Below the guides grid, above the FAQ |
| Category pages | 2 | After the intro, and after the body copy |
| Blog articles | 2 | Above the article body, and before the related links |
| Blog hub | 1 | Below the intro |
| Template guides | 2 | After the hero, and after the alternatives grid |
| **Editor** | **0** | **Deliberately none** |
| Legal pages | 0 | Not worth it, and looks bad next to a privacy policy |

**The editor is intentionally ad-free.** An ad next to the buttons someone is
clicking while working on a resume produces accidental clicks, and accidental
clicks are invalid traffic — which is an account risk, not just a UX problem. It
is enforced in CSS (`body.editor-page .ad-slot { display: none !important }`), so
it cannot be undone by adding a slot to the markup.

### No layout shift, and no empty boxes

Each slot reserves its height by position (`.ad-slot-leaderboard`,
`.ad-slot-footer`), so filling one shifts nothing — CLS is a Core Web Vitals
metric and therefore a ranking input.

While `ADSENSE_CLIENT` is empty the slots have no children and
`.ad-slot:not(.is-live) { display: none }` collapses them entirely. A visitor
never sees an empty box labelled "Advertisement". Verified: `adVisible = 0` on
all 32 pages in the current build.

### The consent sequence

1. Every page sets Consent Mode v2 defaults to **denied** inline in `<head>`,
   before any Google tag can run. The first paint is already compliant.
2. `consent.js` reads a stored choice and calls `gtag('consent','update')`.
3. Only then does anything Google load.

Verified in a browser: with **Reject non-essential** selected, requests to
`googlesyndication`, `googletagmanager` and `google-analytics` = **0**.

Choices persist for 13 months, then re-prompt. **Cookie settings** in the footer
of every page reopens the banner.

---

## Part 4 — What was built for traffic

### 6 category pages

Each has unique copy, its filtered subset of live template previews, FAQ and
breadcrumb schema, and links to sibling collections.

| URL | Target intent |
|---|---|
| `/ats-resume-templates/` | "ats resume template", "ats friendly resume" |
| `/professional-resume-templates/` | "professional resume template" |
| `/modern-resume-templates/` | "modern cv template", "resume templates 2026" |
| `/creative-resume-templates/` | "creative resume template" |
| `/tech-resume-templates/` | "software engineer resume template" |
| `/academic-cv-templates/` | "academic cv template" |

### 10 guides at `/blog/`

Roughly 1,000–1,800 words each, `Article` + `FAQPage` schema, table of contents,
cross-links, and a template CTA. Written to be specific: where a claim is
contested — the one-page rule, the "ATS rejects 75% of resumes" statistic — the
copy says so rather than repeating it, because thin regurgitated advice is
exactly what does not rank any more.

### 8 template guides at `/templates/`

For the highest-intent templates. Deliberately **not** all 50: without genuinely
distinct copy per page, 50 near-identical pages is a doorway pattern and gets
treated as one.

### Internal linking

- A **Collections** strip on the homepage above the gallery, with generated counts
- **Collections** and **Blog** added to the main nav on every page
- A guides grid on the homepage linking six articles
- Breadcrumbs on all 25 new pages
- Contextual links from guide copy into templates and categories
- A four-column footer covering collections, guides and legal

### Technical

- Favicon set: `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`,
  `icon-192.png`, `icon-512.png`, `site.webmanifest`
- **OG image 456 KB → 87 KB** (`og-image.jpg`). The old `.png` URL still resolves,
  downscaled to 65 KB, so previously shared links do not break
- RSS feed at `/blog/rss.xml`
- Sitemap: 6 URLs → **32**
- One `<h1>` per page. Several templates mark the person's name as `<h1>`, which
  gave gallery pages up to 21 competing `<h1>`s once thumbnails painted;
  thumbnails now render those as `<div>` (styling is class-based, so nothing
  changed visually)
- All 32 titles ≤ 60 characters, all descriptions 119–165

---

## Part 5 — Adding content later

The site is still plain static files. `build/` generates the content pages so the
shared chrome lives in one place.

```bash
python build/build.py
```

**To add a blog post:** append a dict to `build/articles_b.py` and rebuild. Body
copy is Markdown (headings, lists, tables, blockquotes, fenced code, links,
bold/italic). The table of contents, reading time, schema, sitemap entry and RSS
item are all derived automatically.

**To change the nav or footer:** edit `build/sitecfg.py`. The generator rewrites
the `NAV`, `FOOTER`, `HEADSCRIPTS` and `COLLECTIONS` marker blocks inside the
hand-written pages, so all 32 pages stay in sync.

**Template counts in prose** are written as `{count}` and substituted from the
catalogue at build time. Four of them had already drifted before this was
introduced, which is what typing numbers into prose reliably produces.

**What the generator does not touch:** `app.js`, `styles.css`, the 50 resume
templates, and everything in the hand-written pages outside the markers.

---

## Part 6 — Next, in priority order

### 1. Publish consistently for three months ★★★★★

This is the whole game now. The infrastructure is done; what is missing is
authority, and authority comes from a body of work plus time.

Two posts a month, each targeting one long-tail question. Candidates, roughly by
search volume:

- Cover letter format and examples
- Resume for a career change
- How to explain an employment gap
- LinkedIn profile vs resume
- Resume for internships
- How to list certifications
- Nursing / teacher / accountant resume examples (occupation pages convert well)
- Interview questions about your resume
- References: who to ask and how to list them

Occupation-specific pages are the strongest remaining opportunity, because intent
is unambiguous and competition is per-occupation rather than site-wide.

### 2. Get the first few backlinks ★★★★☆

Content without links plateaus. Realistic sources for a free tool:

- University careers services list free resume builders — email them, the tool
  genuinely qualifies
- Subreddits where the question is asked directly (r/resumes, r/jobs) — answer
  the question properly and link only where relevant
- Free-tool roundups and directories
- The occupation guides above are what other sites cite

### 3. Split the CSS ★★★☆☆

`styles.css` is now ~333 KB and every page loads all of it. Roughly 70% is resume
template CSS that only the editor and the live thumbnails need.

```
styles.css      → reset, tokens, landing, content pages   (~60 KB)
editor.css      → editor chrome                           (~35 KB)
templates.css   → the 50 .tmpl-* blocks                   (~235 KB)
```

Articles and legal pages need only the first. Category, template and homepage
pages need `templates.css` for their live previews — load it there with
`media="print" onload="this.media='all'"` so it does not block first paint.

Worth doing after approval, not before; it is a Core Web Vitals win, not a
content one.

### 4. Build a real resume score ★★★☆☆

The hero used to claim "Resume score 96%" for a feature that does not exist; it
now reads "Structure / ATS ready", which is true. A genuine score is very
achievable from data the editor already holds — section completeness, bullet
count per role, presence of quantified achievements, summary length, keyword
density against a pasted job description — and it would be a real
differentiator, a reason to link to the site, and a reason to return.

### 5. Do not do these ★☆☆☆☆

- **Fake reviews or `aggregateRating` schema.** Ratings must come from real
  visible reviews. Inventing them risks a manual action, which costs far more
  than a star snippet earns.
- **AI-generated bulk posts.** Fifty thin posts is the fastest route to a
  helpful-content problem and an AdSense rejection.
- **Ads in the editor.** Covered above: invalid-click risk.
- **Per-template pages for all 50.** Without distinct copy it is a doorway
  pattern.

---

## Part 7 — Verification commands

```bash
# generate everything
python build/build.py

# JS parses
node --check app.js

# CSS braces balance
python -c "import io;s=io.open('styles.css',encoding='utf-8').read();print(s.count('{')==s.count('}'))"

# every JSON-LD block parses; canonical present
python -c "
import io,json,re,glob
for f in sorted(glob.glob('**/*.html', recursive=True)):
    s=io.open(f,encoding='utf-8').read(); n=0
    for m in re.finditer(r'<script type=\"application/ld\+json\">(.*?)</script>', s, re.S):
        json.loads(m.group(1)); n+=1
    print(f, 'ld+json:', n, 'canonical:', 'rel=\"canonical\"' in s)
"

# sitemap and feed are well-formed
python -c "import xml.dom.minidom as m;m.parse('sitemap.xml');m.parse('blog/rss.xml');print('ok')"

# word count per page
python -c "
import io,re,glob
t=0
for f in sorted(glob.glob('**/*.html', recursive=True)):
    s=io.open(f,encoding='utf-8').read().split('<body',1)[-1]
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    w=len(re.findall(r\"[A-Za-z][A-Za-z'-]+\", re.sub(r'<[^>]+>',' ',s)))
    t+=w; print('%6d  %s'%(w,f))
print('TOTAL', t)
"
```

Then externally: Rich Results Test, PageSpeed Insights on mobile and desktop, and
Search Console URL Inspection on `/` and one article.
