# -*- coding: utf-8 -*-
"""
Site-wide constants and the shared page chrome (head, nav, footer, ad slots).

Everything that appears on more than one page is defined here exactly once. The
existing hand-written pages pick the same chrome up through the NAV/FOOTER
markers that build.py rewrites, so there is a single source of truth.
"""

SITE = "https://resume-elite.com"
NAME = "ResumeElite"
ASSET_V = "v=growth-2026-08"
TODAY = "2026-08-24"
YEAR = "2026"

# ---------------------------------------------------------------------------
# Monetisation configuration
#
# Leave ADSENSE_CLIENT empty until Google approves the site. While it is empty
# the loader is inert: no request is made, and every reserved ad slot collapses
# so visitors never see blank boxes. Fill it in once and every page picks it up.
# ---------------------------------------------------------------------------
ADSENSE_CLIENT = ""          # e.g. "ca-pub-1234567890123456"
GA4_ID = ""                  # e.g. "G-XXXXXXXXXX"

# ---------------------------------------------------------------------------
# Template catalogue — the single source for names, categories and copy.
# Mirrors the data-cat attributes already on the homepage cards.
# ---------------------------------------------------------------------------
TEMPLATES = [
    ("professional", "Professional", "professional trending", "popular", "Editor's pick",
     "Two-column layout with a timeline spine and photo header — the all-round favourite for corporate applications."),
    # ---- 2026 trend set ----
    ("bento", "Bento", "trending creative", "new", "New",
     "Bento-grid resume: every section in its own rounded tile, with a dark name card. The look of 2026 product sites."),
    ("glass", "Glass", "trending creative tech", "new", "New",
     "Glassmorphism on a night-blue page: frosted cards, a soft colour glow and bright accents."),
    ("notion", "Notion Style", "trending professional tech", "new", "New",
     "Reads like a tidy workspace page: callout summary, property-style contacts and colourful tag chips."),
    ("docs-style", "Docs Style", "trending ats professional", "new", "New",
     "The clean shared-document resume everyone recognises: serif name, coral labels, one plain column."),
    ("simple", "Simple", "trending ats professional", "new", "New",
     "A genuinely simple resume: centred name, hairline rules, one column. Nothing to distract, nothing to break."),
    ("pastel", "Pastel", "trending creative", "new", "New",
     "Soft peach-to-lilac header, pill headings and a lilac side card. Friendly without looking young."),
    ("midnight", "Midnight", "trending tech creative", "new", "New",
     "Full dark-mode resume with a glowing accent and a deep side rail. Stands out in any inbox."),
    ("retro", "Retro", "creative", "new", "New",
     "Seventies stripes, cream paper and Fraunces italics. Warm, characterful and still easy to read."),
    ("gradient", "Gradient", "trending creative", "new", "New",
     "A colour-wash sidebar that carries your name and photo, with a clean white main column."),
    ("two-column", "Two Column", "professional", "new", "New",
     "The classic two-column resume done properly: centred nameplate, ruled columns, square markers."),
    ("bauhaus", "Bauhaus", "creative", "new", "New",
     "Primary-colour shapes, heavy black rules and stacked uppercase type. Design-school confident."),
    ("zen", "Zen", "creative professional", "new", "New",
     "Japanese-minimal: one red sun, wide margins and quiet serif type. Calm and very senior."),
    ("gazette", "Gazette", "creative", "new", "New",
     "Broadsheet masthead, ruled columns and a drop cap. Your career as front-page news."),
    ("blueprint", "Blueprint", "tech", "new", "New",
     "Drafting-grid header, mono labels and numbered sections for engineers and technical roles."),
    ("profile", "Profile", "trending professional", "new", "New",
     "Social-profile layout: cover banner, overlapping photo and card sections everyone already knows how to read."),
    # ---- Job-specific set ----
    ("nurse", "Nurse", "jobs professional", "new", "Healthcare",
     "Nursing resume with a clinical teal rail: licences and clinical skills up front, experience named the way hospitals expect."),
    ("teacher", "Teacher", "jobs professional", "new", "Education",
     "Chalkboard header and highlighter headings, with sections for teaching experience, licensure and classroom skills."),
    ("sales", "Sales", "jobs professional", "new", "Sales",
     "Numbers first: a Key Wins block of KPI cards sits above experience, under a dark growth-arrow header."),
    ("marketing", "Marketing", "jobs creative", "new", "Marketing",
     "Brand-voice headings, campaign cards with a hard accent shadow, and a tinted skills rail."),
    ("data-analyst", "Data Analyst", "jobs tech", "new", "Data",
     "Dark data rail with skill bars, chart-mark headings and analytics projects ahead of experience."),
    ("product-manager", "Product Manager", "jobs tech professional", "new", "Product",
     "Product Impact metric cards, a timeline of roles and a role pill under your name."),
    ("accountant", "Accountant", "jobs professional ats", "new", "Finance",
     "Ledger-style section rows, tabular dates and a double rule. Conservative, exact and ATS-safe."),
    ("customer-service", "Customer Service", "jobs professional", "new", "Support",
     "Chat-bubble headings and a warm rail for service skills, soft skills and languages."),
    ("project-manager", "Project Manager", "jobs professional", "new", "PMP",
     "A phase bar under the header, Gantt-style date tags and room for PMP and PRINCE2 certifications."),
    ("ux-designer", "UX Designer", "jobs creative tech", "new", "Design",
     "A design-tool frame around your name and case-study cards ahead of experience."),
    ("engineering", "Engineering", "jobs tech", "new", "Engineering",
     "Safety-yellow title label, hazard-stripe headings and a dark rail for technical skills."),
    ("legal", "Legal", "jobs professional ats", "new", "Law",
     "Garamond, a centred caption and employer-first entries: the conventions law firms read for."),
    ("hospitality", "Hospitality", "jobs professional", "new", "Hotels",
     "Hotel-menu elegance: italic serif name, a sand side rail and guest-service skills."),
    ("entry-level", "Entry Level", "jobs academic", "new", "First job",
     "For a first job: education, internships and projects lead, with numbered section badges."),
    ("admin-assistant", "Admin Assistant", "jobs professional ats", "new", "Office",
     "Folder-tab header and a checkbox skills grid for executive and administrative assistants."),
    ("aurora", "Aurora", "trending creative", "new", "New",
     "Gradient mesh masthead with a glass side rail. Built for design, marketing and product roles."),
    ("spectrum", "Spectrum", "trending creative", "new", "New",
     "Colour-spine layout with gradient section rules and a soft card rail for skills."),
    ("impact", "Impact", "trending professional tech", "new", "New",
     "Recruiter-first layout: oversized role titles, heavy accent bars and a highlighted summary block."),
    ("metro", "Metro", "trending professional", "new", "New",
     "Diagonal two-tone header with ribbon section titles — confident and easy to scan."),
    ("terminal", "Terminal", "trending tech", "new", "New",
     "Dark IDE aesthetic in monospace with a code-comment section style. Made for developers."),
    ("brutalist", "Brutalist", "trending creative", "new", "New",
     "Neo-brutalist blocks, thick rules and hard offset shadows for portfolios that need to stand out."),
    ("swiss", "Swiss", "trending creative", "new", "New",
     "International Typographic Style: numbered sections, hairline rules and a huge uppercase name."),
    ("vogue", "Vogue", "trending creative", "new", "New",
     "Editorial fashion masthead with a two-column body and drop-cap profile."),
    ("luxe", "Luxe", "trending creative", "new", "New",
     "Ivory and gold minimal serif with wide letter-spacing for senior and luxury-sector roles."),
    ("atelier", "Atelier", "trending creative", "new", "New",
     "Vertical name spine with an asymmetric editorial content column and small-caps section labels."),
    ("elite", "Elite Flagship", "trending professional", "premium", "Top 1%",
     "Ultra-premium asymmetric layout with a dark gold-accented header band and sidebar."),
    ("modern-executive", "Modern Executive", "trending professional", "premium", "C-Suite",
     "Premium C-suite columns with a divided contact grid and a quiet, authoritative tone."),
    ("infographic", "Infographic", "creative", "premium", "Visual",
     "Dual-column premium grid with a tinted sidebar for visual, data-led profiles."),
    ("classic", "Classic", "professional ats", "free", "Free",
     "Clean single-column structure with a photo header. Safe, readable and ATS-friendly."),
    ("modern", "Modern", "professional", "popular", "Popular",
     "Sidebar layout with strong hierarchy — the most-used modern CV structure."),
    ("creative", "Creative", "creative", "free", "Free",
     "Colour-blocked header with playful section markers for creative and agency roles."),
    ("minimal", "Minimal", "ats professional", "free", "Free",
     "Type-only layout with generous whitespace and no decoration. Parses perfectly."),
    ("executive", "Executive", "professional", "free", "Free",
     "Serif nameplate with a two-column body for senior management applications."),
    ("tech", "Tech", "tech", "free", "Free",
     "Two-column technical layout that puts your stack and projects up front."),
    ("software-engineer", "Software Engineer", "tech", "popular", "Popular",
     "Skills-forward engineering layout with a tinted sidebar for tooling and certifications."),
    ("qa-engineer", "QA Engineer", "tech", "free", "Free",
     "Quality-assurance layout with room for test tooling, frameworks and coverage detail."),
    ("elegant", "Elegant", "creative professional", "free", "Free",
     "Thin serif headings with hairline rules — understated and refined."),
    ("bold", "Bold", "creative", "popular", "Popular",
     "High-contrast filled header with solid icons for confident, senior profiles."),
    ("startup", "Startup", "creative tech", "free", "Free",
     "Fast-scan layout for founders and early-stage teams, projects before history."),
    ("corporate", "Corporate", "professional", "free", "Free",
     "Conservative structure with a ruled header for banking, legal and insurance."),
    ("modern-dark", "Modern Dark", "professional creative", "premium", "Premium",
     "Dark-panel header with solid icons and a bright accent for standout digital roles."),
    ("classic-blue", "Classic Blue", "professional", "free", "Free",
     "Traditional structure with a blue accent band — familiar and dependable."),
    ("minimal-formal", "Minimal Formal", "professional ats", "free", "Free",
     "Formal minimal layout with an optional photo and a tightly ruled section grid."),
    ("traditional-serif", "Traditional Serif", "ats academic", "free", "Free",
     "Book-typography serif CV for academia, law and public institutions."),
    ("europass", "Europass", "ats academic", "free", "Free",
     "Europass-style structured CV with labelled personal-detail rows for EU applications."),
    ("modern-right", "Modern Right", "professional", "free", "Free",
     "Right-hand dark sidebar with icon contact rows and a wide main column."),
    ("nordic", "Nordic", "creative", "free", "Free",
     "Scandinavian layout: hairline boxed section blocks in two columns on warm paper."),
    ("timeline", "Timeline", "creative", "popular", "Popular",
     "Connected timeline spine that makes career progression obvious at a glance."),
    ("mono", "Mono", "creative ats", "free", "Free",
     "Typewriter monospace on warm paper with a dashed rule — distinctive but still plain-text safe."),
    ("compact", "Compact", "professional ats", "free", "Free",
     "High-density single page for long careers that must still fit one sheet."),
    ("portfolio", "Portfolio", "creative", "premium", "Premium",
     "Deep navy sidebar with a rounded avatar for portfolio-led creative applications."),
    ("graduate", "Graduate", "academic", "free", "Free",
     "Education-first academic layout with a double-rule header for new graduates."),
    ("student", "Student", "academic", "free", "Free",
     "Rounded-card layout with colour-coded sections that foregrounds coursework and projects."),
    ("freelancer", "Freelancer", "creative", "free", "Free",
     "Warm light studio sheet with a right service rail for independent contractors."),
    ("clean-sidebar", "Clean Sidebar", "professional", "free", "Free",
     "Quiet grey right sidebar with a large name block and roomy main column."),
    ("editorial", "Editorial", "creative", "free", "Free",
     "Magazine layout with a rotated section label and a wide serif nameplate."),
    ("ats-friendly", "ATS Friendly", "ats", "popular", "ATS",
     "Strict monochrome, single column, no graphics. Built to pass applicant tracking systems."),
    ("latex-style", "LaTeX Style", "academic ats", "free", "Academic",
     "Crisp Times-set academic layout that reads like a LaTeX CV class."),
    ("harvard-style", "Harvard Style", "academic ats", "free", "Classic",
     "Centred Garamond header with a double rule — the Ivy League finance standard."),
    ("federal-style", "Federal Style", "ats", "free", "Government",
     "Boxed government layout with an explicit personal-details block for federal applications."),
    ("functional", "Functional", "ats professional", "free", "Skills-First",
     "Skills-first functional CV for career changers and gaps in employment history."),
    ("chronological", "Chronological", "ats professional", "popular", "Trending",
     "Reverse-chronological layout with a dotted connector on every entry."),
    ("consulting-style", "Consulting", "professional", "popular", "McKinsey",
     "High-density consulting format with a burgundy rule and right-aligned contact stack."),
    ("academic-cv", "Academic CV", "academic", "free", "Scholar",
     "Spacious research CV with hanging-indent entries for publications and grants."),
]

TEMPLATE_BY_ID = {t[0]: t for t in TEMPLATES}
TOTAL = len(TEMPLATES)

CATEGORY_ORDER = ["all", "trending", "jobs", "professional", "ats", "creative", "tech", "academic"]
CATEGORY_LABELS = {
    "all": "All templates",
    "trending": "Trending 2026",
    "jobs": "By job",
    "professional": "Professional",
    "ats": "ATS / Plain",
    "creative": "Creative",
    "tech": "Tech",
    "academic": "Academic",
}


def templates_in(cat):
    if cat == "all":
        return list(TEMPLATES)
    return [t for t in TEMPLATES if cat in t[2].split()]


# ---------------------------------------------------------------------------
# Chrome
# ---------------------------------------------------------------------------
NAV_LINKS = [
    ("/#templates", "Templates"),
    ("/#collections", "Collections"),
    ("/blog/", "Blog"),
    ("/#guide", "Guide"),
    ("/#faq", "FAQ"),
]

FOOTER_CATEGORIES = [
    ("/ats-resume-templates/", "ATS resume templates"),
    ("/professional-resume-templates/", "Professional templates"),
    ("/modern-resume-templates/", "Modern CV templates"),
    ("/creative-resume-templates/", "Creative templates"),
    ("/tech-resume-templates/", "Developer resume templates"),
    ("/academic-cv-templates/", "Academic CV templates"),
]

FOOTER_LEGAL = [
    ("/about.html", "About us"),
    ("/contact.html", "Contact us"),
    ("/privacy.html", "Privacy policy"),
    ("/cookies.html", "Cookie policy"),
    ("/terms.html", "Terms of service"),
    ("/disclaimer.html", "Disclaimer"),
]


def nav_html():
    links = "\n".join(
        '        <a href="%s">%s</a>' % (href, label) for href, label in NAV_LINKS)
    return '''  <a class="skip-link" href="#main">Skip to main content</a>

  <!-- Navbar -->
  <header class="navbar">
    <div class="nav-inner">
      <a href="/" class="logo" aria-label="%(name)s home">
        <span class="logo-icon" aria-hidden="true">RE</span>
        <span class="logo-text">%(name)s</span>
      </a>
      <nav class="nav-links" id="nav-links" aria-label="Main navigation">
%(links)s
        <a href="/editor.html" class="btn-nav-cta">Open Builder</a>
      </nav>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links"
        aria-label="Toggle navigation menu">
        <span class="nav-toggle-bars" aria-hidden="true"><i></i><i></i><i></i></span>
      </button>
    </div>
  </header>''' % {"name": NAME, "links": links}


def footer_html():
    cats = "\n".join('            <li><a href="%s">%s</a></li>' % (h, l)
                     for h, l in FOOTER_CATEGORIES)
    legal = "\n".join('            <li><a href="%s">%s</a></li>' % (h, l)
                      for h, l in FOOTER_LEGAL)
    return '''  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col footer-brand">
          <a href="/" class="logo" aria-label="%(name)s home">
            <span class="logo-icon" aria-hidden="true">RE</span>
            <span class="logo-text">%(name)s</span>
          </a>
          <p>Create professional, ATS-friendly resumes in minutes with %(total)d clean, modern templates. Free, private, and no
            signup required.</p>
        </div>
        <nav class="footer-col" aria-labelledby="footer-cat-title">
          <h2 class="footer-col-title" id="footer-cat-title">Browse templates</h2>
          <ul class="footer-links">
%(cats)s
          </ul>
        </nav>
        <nav class="footer-col" aria-labelledby="footer-learn-title">
          <h2 class="footer-col-title" id="footer-learn-title">Learn</h2>
          <ul class="footer-links">
            <li><a href="/blog/">Resume blog</a></li>
            <li><a href="/blog/how-to-write-a-resume/">How to write a resume</a></li>
            <li><a href="/blog/how-ats-works/">How ATS software works</a></li>
            <li><a href="/blog/resume-with-no-experience/">Resume with no experience</a></li>
            <li><a href="/blog/professional-summary-examples/">Professional summary examples</a></li>
            <li><a href="/blog/resume-action-verbs/">Resume action verbs</a></li>
          </ul>
        </nav>
        <nav class="footer-col" aria-labelledby="footer-legal-title">
          <h2 class="footer-col-title" id="footer-legal-title">Site</h2>
          <ul class="footer-links">
%(legal)s
          </ul>
        </nav>
      </div>
      <div class="footer-bottom">
        <p class="footer-copy">&copy; %(year)s %(name)s. All rights reserved.</p>
        <p class="footer-note">Your resume data never leaves your browser.
          <button type="button" class="footer-link-btn" data-open-consent>Cookie settings</button>
        </p>
      </div>
    </div>
  </footer>''' % {"name": NAME, "cats": cats, "legal": legal, "year": YEAR, "total": TOTAL}


# ---------------------------------------------------------------------------
# Consent + ads + analytics loader
#
# Consent Mode v2 defaults are set inline, before any Google tag can run, so the
# very first pageview is already denied by default. consent.js then reads the
# stored choice and upgrades. Ads only load after that.
# ---------------------------------------------------------------------------
def head_common():
    """
    Everything every page needs in <head> beyond its own metadata: icons, the
    manifest, the feed, and the consent bootstrap. Lives inside the
    HEADSCRIPTS marker so the hand-written pages get it too.
    """
    return '''  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="alternate" type="application/rss+xml" title="ResumeElite resume blog" href="/blog/rss.xml" />
  <script>
    // Consent Mode v2 defaults. Must run before any Google tag.
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('consent', 'default', {
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      analytics_storage: 'denied',
      functionality_storage: 'granted',
      security_storage: 'granted',
      wait_for_update: 500
    });
    window.RE_CONFIG = { adsenseClient: '%(ads)s', ga4Id: '%(ga4)s' };
  </script>
  <script defer src="/consent.js?%(v)s"></script>''' % {
        "ads": ADSENSE_CLIENT, "ga4": GA4_ID, "v": ASSET_V}


def ad_slot(position, label="Advertisement"):
    """
    A reserved ad container.

    The height is reserved in CSS by position so filling it causes no layout
    shift, and the whole block is hidden while ADSENSE_CLIENT is empty, so no
    visitor ever sees an empty labelled box.
    """
    return ('<aside class="ad-slot ad-slot-%s" data-ad-slot="%s" aria-hidden="true">'
            '<span class="ad-label">%s</span></aside>' % (position, position, label))

# ---------------------------------------------------------------------------
# Homepage collections strip. Counts come from the catalogue.
# ---------------------------------------------------------------------------
COLLECTIONS = [
    ("/ats-resume-templates/", "ats", "ATS resume templates",
     "Single column, standard headings, nothing a parser can misread."),
    ("/professional-resume-templates/", "professional", "Professional templates",
     "Corporate, finance, legal and management. Restrained and considered."),
    ("/modern-resume-templates/", "trending", "Modern CV templates",
     "The 2026 set: soft gradients, editorial grids, big tight type."),
    ("/creative-resume-templates/", "creative", "Creative templates",
     "For designers, writers and freelancers, where taste is assessed."),
    ("/tech-resume-templates/", "tech", "Developer templates",
     "Stack and projects up front, including a dark terminal layout."),
    ("/academic-cv-templates/", "academic", "Academic CV templates",
     "Publication lists, Europass structure, education-first layouts."),
]


def collections_html():
    cards = []
    for href, cat, title, blurb in COLLECTIONS:
        cards.append(
            '        <a class="cat-strip-card" href="%s">\n'
            '          <strong>%s</strong>\n'
            '          <span>%s</span>\n'
            '          <em>%d templates &rarr;</em>\n'
            '        </a>' % (href, title, blurb, len(templates_in(cat))))
    return "\n".join(cards)


# ---------------------------------------------------------------------------
# Template pickers. The homepage gallery filters and the editor's template
# drawer are generated from TEMPLATES, so a new template needs one catalogue
# line (plus its CV_TEMPLATES entry and CSS) and nothing hand-copied.
# ---------------------------------------------------------------------------
def gallery_filters_html():
    return "\n".join(
        '          <button class="tfilter%s" type="button" data-cat="%s">%s</button>'
        % (" is-active" if c == "all" else "", c, CATEGORY_LABELS[c])
        for c in CATEGORY_ORDER)


def editor_cats_html():
    return "\n".join(
        '                            <button class="tcat%s" type="button" data-cat="%s">%s</button>'
        % (" is-active" if c == "all" else "", c, "All" if c == "all" else CATEGORY_LABELS[c])
        for c in CATEGORY_ORDER)


def editor_grid_html():
    return "\n".join(
        '                        <button class="tmpl-btn" type="button" data-tmpl="%(id)s" data-cat="%(cats)s" '
        'data-name="%(name)s" title="%(name)s"><span class="tmpl-thumb thumb-%(id)s"></span>'
        '<span class="tmpl-name">%(name)s</span></button>' % {"id": t[0], "name": t[1], "cats": t[2]}
        for t in TEMPLATES)
