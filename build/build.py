# -*- coding: utf-8 -*-
"""
Static site generator for ResumeElite.

Run from the repository root:

    python build/build.py

It writes the category pages, the blog, the per-template pages, sitemap.xml and
the RSS feed, and it refreshes the shared nav/footer/head blocks inside the
hand-written pages (index.html, editor.html, the legal pages) through HTML
comment markers. Nothing else in those files is touched.
"""

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import mdlite                                    # noqa: E402
import sitecfg as S                              # noqa: E402
import content                                   # noqa: E402


# --------------------------------------------------------------------------- io
def write(rel_path, text):
    path = os.path.join(ROOT, rel_path)
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    io.open(path, "w", encoding="utf-8", newline="\n").write(text)
    return rel_path


def read(rel_path):
    return io.open(os.path.join(ROOT, rel_path), encoding="utf-8").read()


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


# ------------------------------------------------------------------------- head
def head(title, description, url, *, schema=None, image=None, extra="",
         robots="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"):
    image = image or (S.SITE + "/og-image.jpg")
    blocks = ""
    for obj in (schema or []):
        blocks += ('\n  <script type="application/ld+json">\n%s\n  </script>'
                   % json.dumps(obj, indent=2, ensure_ascii=False))

    return '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />

  <title>%(title)s</title>
  <meta name="description" content="%(desc)s" />
  <meta name="robots" content="%(robots)s" />
  <meta name="author" content="%(name)s" />
  <meta name="theme-color" content="#f7fbff" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#0b1120" media="(prefers-color-scheme: dark)" />

  <link rel="canonical" href="%(url)s" />

  <meta property="og:site_name" content="%(name)s" />
  <meta property="og:title" content="%(title)s" />
  <meta property="og:description" content="%(desc)s" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:url" content="%(url)s" />
  <meta property="og:image" content="%(image)s" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="%(title)s" />
  <meta name="twitter:description" content="%(desc)s" />
  <meta name="twitter:image" content="%(image)s" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;800&family=Cormorant+Garamond:wght@300;400;500;600;700&display=swap" />
  <link rel="stylesheet" href="/styles.css?%(v)s" />
%(scripts)s%(schema)s%(extra)s
</head>
''' % {
        "title": esc(title), "desc": esc(description), "url": url, "name": S.NAME,
        "image": image, "v": S.ASSET_V, "robots": robots,
        "scripts": S.head_common(), "schema": blocks, "extra": extra,
    }


def tail():
    return '''
%(footer)s

  <script defer src="/app.js?%(v)s"></script>
</body>

</html>
''' % {"footer": S.footer_html(), "v": S.ASSET_V}


# ---------------------------------------------------------------------- schema
def breadcrumbs(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": S.SITE + path}
            for i, (path, name) in enumerate(trail)
        ],
    }


def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in pairs
        ],
    }


def crumb_html(trail):
    parts = []
    for i, (path, name) in enumerate(trail):
        last = i == len(trail) - 1
        if last:
            parts.append('<span aria-current="page">%s</span>' % esc(name))
        else:
            parts.append('<a href="%s">%s</a>' % (path, esc(name)))
    return ('<nav class="crumbs" aria-label="Breadcrumb">%s</nav>'
            % '<span class="crumb-sep" aria-hidden="true">/</span>'.join(parts))


# ----------------------------------------------------------------- components
def template_card(tid, *, heading="h3"):
    tpl = S.TEMPLATE_BY_ID[tid]
    _, name, cats, badge, badge_text, desc = tpl
    return '''        <article class="template-card" data-template="%(id)s" data-cat="%(cats)s" data-name="%(name)s">
          <div class="template-preview" data-live-thumb="%(id)s" role="img" aria-label="%(name)s resume template preview"></div>
          <div class="template-info">
            <%(h)s class="template-name">%(name)s</%(h)s>
            <span class="template-badge %(badge)s">%(badge_text)s</span>
          </div>
          <p class="template-desc">%(desc)s</p>
          <a href="/editor.html?template=%(id)s" class="btn-template">Use this template<span aria-hidden="true"> &rarr;</span></a>
        </article>''' % {
        "id": tid, "cats": cats, "name": esc(name), "badge": badge,
        "badge_text": esc(badge_text), "desc": esc(desc), "h": heading}


def faq_block(pairs, title="Frequently asked questions"):
    items = ""
    for q, a in pairs:
        items += '''
          <div class="faq-item">
            <h3><button class="faq-q" type="button" aria-expanded="false">%s<span class="faq-mark" aria-hidden="true"></span></button></h3>
            <div class="faq-a"><p>%s</p></div>
          </div>''' % (esc(q), a)
    return '''
    <section class="faq-section" id="faq" aria-labelledby="faq-title">
      <div class="container">
        <div class="section-head">
          <p class="section-label">FAQ</p>
          <h2 class="section-title" id="faq-title">%s</h2>
        </div>
        <div class="faq-list">%s
        </div>
      </div>
    </section>''' % (esc(title), items)


def related_links(items, title="Keep reading"):
    if not items:
        return ""
    lis = "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for h, t in items)
    return ('<section class="related" aria-labelledby="related-title">'
            '<h2 id="related-title">%s</h2><ul>%s</ul></section>'
            % (esc(title), lis))


# ------------------------------------------------------------- category pages
def build_categories():
    written = []
    for cat in content.CATEGORIES:
        tpls = S.templates_in(cat["filter"])
        # Every {count} in the copy resolves from the catalogue, so a template
        # moving between categories can never leave a stale number in prose.
        cat = {k: (v.replace("{count}", str(len(tpls))) if isinstance(v, str) else v)
               for k, v in cat.items()}
        cards = "\n".join(template_card(t[0]) for t in tpls)
        url = S.SITE + cat["path"]
        trail = [("/", "Home"), (cat["path"], cat["crumb"])]

        body_html = mdlite.render(cat["body"])
        intro_html = mdlite.render(cat["intro"])

        schema = [
            breadcrumbs(trail),
            {
                "@context": "https://schema.org",
                "@type": "CollectionPage",
                "name": cat["h1"],
                "url": url,
                "description": cat["description"],
                "inLanguage": "en",
                "isPartOf": {"@type": "WebSite", "@id": S.SITE + "/#website"},
                "about": {"@type": "Thing", "name": cat["about"]},
                "mainEntity": {
                    "@type": "ItemList",
                    "numberOfItems": len(tpls),
                    "itemListElement": [
                        {"@type": "ListItem", "position": i + 1, "name": t[1],
                         "url": "%s/editor.html?template=%s" % (S.SITE, t[0])}
                        for i, t in enumerate(tpls)
                    ],
                },
            },
            faq_schema(cat["faq"]),
        ]

        siblings = [(c["path"], c["nav"]) for c in content.CATEGORIES
                    if c["path"] != cat["path"]]

        page = head(cat["title"], cat["description"], url, schema=schema) + '''
<body class="landing-page category-page">

%(nav)s

  <main id="main">
    <section class="cat-hero">
      <div class="container">
        %(crumbs)s
        <p class="section-label">%(kicker)s</p>
        <h1 class="cat-title">%(h1)s</h1>
        <div class="cat-intro">%(intro)s</div>
        <div class="cat-hero-actions">
          <a href="/editor.html?template=%(first)s" class="btn-primary btn-xl">Start with %(first_name)s</a>
          <a href="#templates" class="btn-ghost btn-xl">See all %(count)d templates</a>
        </div>
      </div>
    </section>

    <div class="container">%(ad_top)s</div>

    <section class="templates-section" id="templates" aria-labelledby="grid-title">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title" id="grid-title">%(grid_title)s</h2>
          <p class="section-subtitle">%(grid_sub)s</p>
        </div>
        <div class="templates-grid" id="templates-grid">
%(cards)s
        </div>
      </div>
    </section>

    <section class="cat-body-section">
      <div class="container">
        <div class="prose">%(body)s</div>
        %(siblings)s
      </div>
    </section>

    <div class="container">%(ad_bottom)s</div>

%(faq)s

    <section class="cta-section" aria-labelledby="cta-title">
      <div class="container cta-content">
        <h2 id="cta-title">%(cta_h)s</h2>
        <p>%(cta_p)s</p>
        <a href="/editor.html?template=%(first)s" class="btn-primary btn-xl">Open the builder</a>
      </div>
    </section>
  </main>
''' % {
            "nav": S.nav_html(),
            "crumbs": crumb_html(trail),
            "kicker": esc(cat["kicker"]),
            "h1": esc(cat["h1"]),
            "intro": intro_html,
            "first": tpls[0][0],
            "first_name": esc(tpls[0][1]),
            "count": len(tpls),
            "grid_title": esc(cat["grid_title"]),
            "grid_sub": esc(cat["grid_sub"]),
            "cards": cards,
            "body": body_html,
            "siblings": related_links(siblings, "Other template collections"),
            "faq": faq_block(cat["faq"]),
            "cta_h": esc(cat["cta_h"]),
            "cta_p": esc(cat["cta_p"]),
            "ad_top": S.ad_slot("leaderboard"),
            "ad_bottom": S.ad_slot("footer"),
        } + tail()

        written.append(write(cat["path"].strip("/") + "/index.html", page))
    return written


# ------------------------------------------------------------------ blog posts
def build_blog():
    written = []
    posts = content.POSTS

    for post in posts:
        url = S.SITE + post["path"]
        trail = [("/", "Home"), ("/blog/", "Blog"), (post["path"], post["crumb"])]
        body = mdlite.render(post["body"])
        toc = mdlite.collect_headings(post["body"], levels=(2,))
        words = len(mdlite.plain_text(post["body"]).split())
        minutes = max(2, round(words / 210.0))

        toc_html = ""
        if len(toc) > 2:
            lis = "".join('<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in toc)
            toc_html = ('<nav class="toc" aria-labelledby="toc-title">'
                        '<h2 id="toc-title">On this page</h2><ol>%s</ol></nav>' % lis)

        schema = [
            breadcrumbs(trail),
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": post["title_h1"],
                "description": post["description"],
                "inLanguage": "en",
                "mainEntityOfPage": {"@type": "WebPage", "@id": url},
                "datePublished": post["published"],
                "dateModified": post.get("modified", post["published"]),
                "wordCount": words,
                "articleSection": post["section"],
                "keywords": ", ".join(post["keywords"]),
                "author": {"@type": "Organization", "name": S.NAME, "url": S.SITE + "/about.html"},
                "publisher": {
                    "@type": "Organization", "name": S.NAME,
                    "logo": {"@type": "ImageObject", "url": S.SITE + "/icon-512.png"},
                },
                "image": S.SITE + "/og-image.jpg",
            },
        ]
        if post.get("faq"):
            schema.append(faq_schema(post["faq"]))

        page = head(post["title"], post["description"], url, schema=schema) + '''
<body class="landing-page article-page">

%(nav)s

  <main id="main">
    <article class="article">
      <div class="container article-shell">
        <header class="article-head">
          %(crumbs)s
          <p class="section-label">%(section)s</p>
          <h1>%(h1)s</h1>
          <p class="article-standfirst">%(standfirst)s</p>
          <p class="article-meta">
            <time datetime="%(published)s">Updated %(nice_date)s</time>
            <span aria-hidden="true">&middot;</span>
            <span>%(minutes)d min read</span>
          </p>
        </header>

        %(toc)s

        <div class="container-narrow">%(ad_top)s</div>

        <div class="prose">%(body)s</div>

        <aside class="article-cta">
          <h2>%(cta_h)s</h2>
          <p>%(cta_p)s</p>
          <a href="%(cta_href)s" class="btn-primary btn-xl">%(cta_label)s</a>
        </aside>

        <div class="container-narrow">%(ad_bottom)s</div>

        %(related)s
      </div>
    </article>
%(faq)s
  </main>
''' % {
            "nav": S.nav_html(),
            "crumbs": crumb_html(trail),
            "section": esc(post["section"]),
            "h1": esc(post["title_h1"]),
            "standfirst": esc(post["standfirst"]),
            "published": post.get("modified", post["published"]),
            "nice_date": content.nice_date(post.get("modified", post["published"])),
            "minutes": minutes,
            "toc": toc_html,
            "body": body,
            "cta_h": esc(post["cta"]["h"]),
            "cta_p": esc(post["cta"]["p"]),
            "cta_href": post["cta"]["href"],
            "cta_label": esc(post["cta"]["label"]),
            "related": related_links(
                [(p["path"], p["title_h1"]) for p in posts
                 if p["path"] in post.get("related", [])]),
            "faq": faq_block(post["faq"], "Common questions") if post.get("faq") else "",
            "ad_top": S.ad_slot("leaderboard"),
            "ad_bottom": S.ad_slot("footer"),
        } + tail()

        written.append(write(post["path"].strip("/") + "/index.html", page))

    # ---- hub ----
    cards = ""
    for post in posts:
        words = len(mdlite.plain_text(post["body"]).split())
        cards += '''        <article class="post-card">
          <p class="post-card-kicker">%s</p>
          <h2 class="post-card-title"><a href="%s">%s</a></h2>
          <p class="post-card-desc">%s</p>
          <p class="post-card-meta"><time datetime="%s">%s</time> &middot; %d min read</p>
        </article>
''' % (esc(post["section"]), post["path"], esc(post["title_h1"]),
       esc(post["standfirst"]), post.get("modified", post["published"]),
       content.nice_date(post.get("modified", post["published"])),
       max(2, round(words / 210.0)))

    hub_url = S.SITE + "/blog/"
    hub_trail = [("/", "Home"), ("/blog/", "Blog")]
    hub_schema = [
        breadcrumbs(hub_trail),
        {
            "@context": "https://schema.org",
            "@type": "Blog",
            "@id": hub_url,
            "name": "%s resume blog" % S.NAME,
            "description": content.BLOG_HUB["description"],
            "url": hub_url,
            "inLanguage": "en",
            "publisher": {"@type": "Organization", "name": S.NAME, "url": S.SITE + "/"},
            "blogPost": [
                {"@type": "BlogPosting", "headline": p["title_h1"],
                 "url": S.SITE + p["path"], "datePublished": p["published"]}
                for p in posts
            ],
        },
    ]

    hub = head(content.BLOG_HUB["title"], content.BLOG_HUB["description"],
               hub_url, schema=hub_schema) + '''
<body class="landing-page blog-hub">

%(nav)s

  <main id="main">
    <section class="cat-hero">
      <div class="container">
        %(crumbs)s
        <p class="section-label">Resume blog</p>
        <h1 class="cat-title">%(h1)s</h1>
        <div class="cat-intro">%(intro)s</div>
      </div>
    </section>

    <div class="container">%(ad_top)s</div>

    <section class="posts-section">
      <div class="container">
        <div class="posts-grid">
%(cards)s
        </div>
      </div>
    </section>

    <section class="cta-section" aria-labelledby="cta-title">
      <div class="container cta-content">
        <h2 id="cta-title">Stop reading, start building</h2>
        <p>Every guide here links back to a template that already has the structure baked in.</p>
        <a href="/editor.html" class="btn-primary btn-xl">Open the resume builder</a>
      </div>
    </section>
  </main>
''' % {
        "nav": S.nav_html(),
        "crumbs": crumb_html(hub_trail),
        "h1": esc(content.BLOG_HUB["h1"]),
        "intro": mdlite.render(content.BLOG_HUB["intro"]),
        "cards": cards,
        "ad_top": S.ad_slot("leaderboard"),
    } + tail()

    written.append(write("blog/index.html", hub))
    return written


# -------------------------------------------------------------- template pages
def build_template_pages():
    written = []
    for tp in content.TEMPLATE_PAGES:
        tid = tp["id"]
        tpl = S.TEMPLATE_BY_ID[tid]
        url = S.SITE + tp["path"]
        trail = [("/", "Home"), (tp["category_path"], tp["category_name"]),
                 (tp["path"], tpl[1])]

        schema = [
            breadcrumbs(trail),
            {
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": tp["title_h1"],
                "url": url,
                "description": tp["description"],
                "inLanguage": "en",
                "isPartOf": {"@type": "WebSite", "@id": S.SITE + "/#website"},
                "primaryImageOfPage": {"@type": "ImageObject", "url": S.SITE + "/icon-512.png"},
            },
            faq_schema(tp["faq"]),
        ]

        siblings = [(p["path"], S.TEMPLATE_BY_ID[p["id"]][1] + " template")
                    for p in content.TEMPLATE_PAGES if p["id"] != tid][:6]

        page = head(tp["title"], tp["description"], url, schema=schema) + '''
<body class="landing-page template-page">

%(nav)s

  <main id="main">
    <section class="tpl-hero">
      <div class="container tpl-hero-grid">
        <div class="tpl-hero-copy">
          %(crumbs)s
          <p class="section-label">%(kicker)s</p>
          <h1 class="cat-title">%(h1)s</h1>
          <div class="cat-intro">%(intro)s</div>
          <ul class="tpl-facts">
%(facts)s
          </ul>
          <div class="cat-hero-actions">
            <a href="/editor.html?template=%(id)s" class="btn-primary btn-xl">Use this template free</a>
            <a href="%(cat_path)s" class="btn-ghost btn-xl">More %(cat_lower)s</a>
          </div>
        </div>
        <div class="tpl-hero-preview">
          <div class="template-preview tpl-preview-large" data-live-thumb="%(id)s" role="img"
            aria-label="Full preview of the %(name)s resume template"></div>
        </div>
      </div>
    </section>

    <div class="container">%(ad_top)s</div>

    <section class="cat-body-section">
      <div class="container">
        <div class="prose">%(body)s</div>
      </div>
    </section>

    <section class="templates-section" aria-labelledby="alt-title">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title" id="alt-title">If this one is not right</h2>
          <p class="section-subtitle">Three close alternatives, and every one carries your content across
            untouched when you switch.</p>
        </div>
        <div class="templates-grid" id="templates-grid">
%(alts)s
        </div>
      </div>
    </section>

    <div class="container">%(ad_bottom)s</div>

%(faq)s

    <section class="cat-body-section">
      <div class="container">%(siblings)s</div>
    </section>
  </main>
''' % {
            "nav": S.nav_html(),
            "crumbs": crumb_html(trail),
            "kicker": esc(tp["kicker"]),
            "h1": esc(tp["title_h1"]),
            "intro": mdlite.render(tp["intro"]),
            "facts": "\n".join("            <li><strong>%s</strong><span>%s</span></li>"
                               % (esc(k), esc(v)) for k, v in tp["facts"]),
            "id": tid,
            "name": esc(tpl[1]),
            "cat_path": tp["category_path"],
            "cat_lower": esc(tp["category_name"].lower()),
            "body": mdlite.render(tp["body"]),
            "alts": "\n".join(template_card(a) for a in tp["alternatives"]),
            "faq": faq_block(tp["faq"]),
            "siblings": related_links(siblings, "Other template guides"),
            "ad_top": S.ad_slot("leaderboard"),
            "ad_bottom": S.ad_slot("footer"),
        } + tail()

        written.append(write(tp["path"].strip("/") + "/index.html", page))
    return written


# ------------------------------------------------------------------- crawl files
def build_sitemap():
    urls = [("/", "1.0", "weekly"), ("/blog/", "0.9", "weekly")]
    urls += [(c["path"], "0.9", "monthly") for c in content.CATEGORIES]
    urls += [(p["path"], "0.8", "monthly") for p in content.POSTS]
    urls += [(t["path"], "0.7", "monthly") for t in content.TEMPLATE_PAGES]
    urls += [("/about.html", "0.5", "yearly"), ("/contact.html", "0.5", "yearly"),
             ("/privacy.html", "0.3", "yearly"), ("/cookies.html", "0.3", "yearly"),
             ("/terms.html", "0.3", "yearly"), ("/disclaimer.html", "0.3", "yearly")]

    body = "".join('''
  <url>
    <loc>%s%s</loc>
    <lastmod>%s</lastmod>
    <changefreq>%s</changefreq>
    <priority>%s</priority>
  </url>''' % (S.SITE, path, S.TODAY, freq, pri) for path, pri, freq in urls)

    write("sitemap.xml", '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s
</urlset>
''' % body)
    return len(urls)


def build_rss():
    items = ""
    for p in content.POSTS:
        items += '''
    <item>
      <title>%s</title>
      <link>%s%s</link>
      <guid isPermaLink="true">%s%s</guid>
      <pubDate>%s</pubDate>
      <description>%s</description>
    </item>''' % (esc(p["title_h1"]), S.SITE, p["path"], S.SITE, p["path"],
                  content.rfc822(p["published"]), esc(p["standfirst"]))

    write("blog/rss.xml", '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>%s resume blog</title>
    <link>%s/blog/</link>
    <atom:link href="%s/blog/rss.xml" rel="self" type="application/rss+xml" />
    <description>%s</description>
    <language>en</language>
    <lastBuildDate>%s</lastBuildDate>%s
  </channel>
</rss>
''' % (S.NAME, S.SITE, S.SITE, esc(content.BLOG_HUB["description"]),
       content.rfc822(S.TODAY), items))


def build_robots():
    write("robots.txt", '''User-agent: *
Allow: /

# editor.html (and its ?template= variants) must stay crawlable so the
# "noindex, follow" meta tag on it can actually be read and obeyed.
# Do not add a Disallow for it: a blocked URL can still be indexed as a bare link.

# Assets crawlers need in order to render pages correctly
Allow: /styles.css
Allow: /app.js
Allow: /consent.js
Allow: /og-image.jpg
Allow: /og-image.png

Sitemap: %s/sitemap.xml
''' % S.SITE)


def build_manifest():
    write("site.webmanifest", json.dumps({
        "name": "%s — Free Resume Builder" % S.NAME,
        "short_name": S.NAME,
        "description": "Build an ATS-friendly resume with 50 free templates and instant PDF export.",
        "start_url": "/?utm_source=pwa",
        "display": "standalone",
        "background_color": "#f7fbff",
        "theme_color": "#0b1120",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }, indent=2) + "\n")


def build_ads_txt():
    if S.ADSENSE_CLIENT:
        pub = S.ADSENSE_CLIENT.replace("ca-", "")
        write("ads.txt", "google.com, %s, DIRECT, f08c47fec0942fa0\n" % pub)
    else:
        write("ads.txt", '''# Authorized Digital Sellers for resume-elite.com
#
# This file is intentionally inert until AdSense approves the site.
# After approval, replace everything below with the single line Google shows you
# under AdSense > Sites > Ads.txt, which looks exactly like this:
#
# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0
#
# Then set ADSENSE_CLIENT in build/sitecfg.py to "ca-pub-0000000000000000" and run
# python build/build.py so every page starts loading ads.
''')


# ------------------------------------------------- chrome sync in static pages
MARKERS = {
    "NAV": S.nav_html,
    "FOOTER": S.footer_html,
    "HEADSCRIPTS": S.head_common,
    "COLLECTIONS": S.collections_html,
}


def sync_chrome():
    touched = []
    found = []
    for name in ("index.html", "editor.html", "about.html", "contact.html",
                 "privacy.html", "cookies.html", "terms.html", "disclaimer.html"):
        path = os.path.join(ROOT, name)
        if not os.path.isfile(path):
            continue
        text = io.open(path, encoding="utf-8").read()
        before = text
        for marker, fn in MARKERS.items():
            pattern = re.compile(
                r"(<!-- %s:START -->)(.*?)(<!-- %s:END -->)" % (marker, marker), re.S)
            if pattern.search(text):
                found.append(name)
                text = pattern.sub(
                    lambda m: m.group(1) + "\n" + fn() + "\n  " + m.group(3), text)
        if text != before:
            io.open(path, "w", encoding="utf-8", newline="").write(text)
            touched.append(name)
    return touched, sorted(set(found))


# --------------------------------------------------------------------------- run
def main():
    cats = build_categories()
    blog = build_blog()
    tpls = build_template_pages()
    n = build_sitemap()
    build_rss()
    build_robots()
    build_manifest()
    build_ads_txt()
    touched, found = sync_chrome()

    print("categories      %d" % len(cats))
    print("blog pages      %d" % len(blog))
    print("template pages  %d" % len(tpls))
    print("sitemap urls    %d" % n)
    if not found:
        print("chrome synced   WARNING: no NAV/FOOTER/HEADSCRIPTS markers found")
    else:
        print("chrome synced   %d pages carry markers; rewritten: %s"
              % (len(found), ", ".join(touched) or "none (already current)"))

    words = 0
    for c in content.CATEGORIES:
        words += len(mdlite.plain_text(c["intro"] + c["body"]).split())
    for p in content.POSTS:
        words += len(mdlite.plain_text(p["body"]).split())
    for t in content.TEMPLATE_PAGES:
        words += len(mdlite.plain_text(t["intro"] + t["body"]).split())
    print("new copy        %d words" % words)


if __name__ == "__main__":
    main()
