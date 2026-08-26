# -*- coding: utf-8 -*-
"""
All page copy lives here (plus the blog posts, imported from posts.py).

Editing copy means editing this file and re-running python build/build.py.
Nothing here contains markup beyond the small Markdown subset mdlite supports.
"""

import datetime

from posts import POSTS, BLOG_HUB          # noqa: F401  (re-exported for build.py)

_MONTHS = ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"]


def nice_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return "%d %s %d" % (d, _MONTHS[m - 1], y)


def rfc822(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return datetime.datetime(y, m, d, 9, 0, 0).strftime("%a, %d %b %Y %H:%M:%S +0000")


# ===========================================================================
# CATEGORY PAGES
# ===========================================================================

CATEGORIES = [
    # ---------------------------------------------------------------- ATS
    {
        "path": "/ats-resume-templates/",
        "filter": "ats",
        "crumb": "ATS resume templates",
        "nav": "ATS resume templates",
        "kicker": "ATS templates",
        "title": "{count} Free ATS Resume Templates That Parse | ResumeElite",
        "h1": "ATS resume templates that parsing software can actually read",
        "description": "Free ATS-friendly resume templates with single-column text flow, standard headings and no graphics. Pick one, fill it in, download a PDF that parses cleanly.",
        "about": "Applicant tracking system resume formatting",
        "grid_title": "Every ATS-safe layout on the site",
        "grid_sub": "All {count} of them keep a single readable text flow. Each preview below is the real template rendering live.",
        "cta_h": "Build an ATS resume in about ten minutes",
        "cta_p": "No signup, no watermark, and the PDF keeps real selectable text.",
        "intro": """
An applicant tracking system does not look at your resume. It reads it -- as one long
stream of text, top to bottom, left to right. Anything that interrupts that stream is
where parsing goes wrong: text boxes, tables used for layout, headers and footers,
graphics with words inside them, or two columns that interleave into nonsense.

Every template in this collection is built for that reading order. Single column,
standard section headings, real text in the PDF, and no decoration that carries
meaning. They are plain on purpose.
""",
        "body": """
## What actually breaks an ATS parse

Most "ATS-friendly" advice online is folklore. These are the failure modes that show
up repeatedly when you run resumes through real parsers:

- **Two columns that the parser reads as one line.** A sidebar with skills next to
  your job history can come out as "Python Senior Engineer SQL Northwind Analytics".
  This is the single most common cause of a mangled parse.
- **Text inside an image.** Your name in a logo, a skills chart, a headshot with your
  title baked into it. The parser sees an image and moves on.
- **Layout tables.** A table used to line up dates and titles often parses row-first,
  which scrambles the relationship between a role and its employer.
- **Non-standard headings.** "Where I've Been" instead of "Work Experience" means the
  parser cannot classify the block that follows it.
- **Headers and footers.** Many parsers skip them entirely. If your phone number is
  only in the header, it may be the one thing the system never captures.
- **Fancy bullet glyphs.** Decorative characters sometimes come through as question
  marks or get concatenated into the line above.

## What these templates do differently

| Choice | Why it matters |
|---|---|
| One text column | Reading order is unambiguous |
| Standard headings | Work Experience, Education, Skills, Certifications |
| Real PDF text | Selectable, searchable, and parseable |
| No layout tables | Every entry is a normal block of text |
| Plain bullets | Standard hyphen or bullet characters only |
| Contact in the body | Never only in a header or footer |

## Picking between them

**[ATS Friendly](/templates/ats-friendly-resume-template/)** is the strictest: black
on white, Arial, no accent colour at all. Use it when the posting mentions a
specific ATS by name, when you are applying through a large-company portal, or when
you have been rejected silently more than a few times and want to remove formatting
as a variable.

**Chronological** adds a light dotted connector down the left of each entry. It is
still a single column and still parses cleanly, but it looks less like a fax.

**Functional** leads with a grouped skills block before employment history. That is
the right shape for career changers and for anyone with a gap they would rather not
put at the top of page one.

**Harvard Style** and **LaTeX Style** are the serif academic conventions -- centred
name, ruled section headings. Common in finance, consulting, law and academia, and
both parse well because the structure underneath is still one column.

**Federal Style** exists because US federal applications ask for things a normal
resume omits: citizenship, series and grade, hours per week, supervisor contact. It
has an explicit personal-details block for exactly that.

**Compact** and **Minimal** are for people with long histories who still need one
page. Compact is the densest layout on the site.

## Do you actually need a plain template?

Not always, and this is worth being honest about. A plain resume is insurance against
a machine, and insurance has a cost: it looks like everyone else's.

If a human reads first -- an agency, a studio, a startup, a referral, a small company
where the founder opens the inbox -- a designed resume helps you. Every template on
this site exports real selectable text, so a
[creative layout](/creative-resume-templates/) is not unreadable, just less
predictable.

The practical rule: if you cannot see who reads it first, send the plain one. If you
know a person opens it, send the good-looking one. And if you are applying at scale,
keep both and switch templates per application -- your content carries across
untouched.

## Before you send it

1. Open the PDF and try to select your name with the cursor. If you cannot, something
   has gone wrong.
2. Copy the whole PDF and paste it into a plain text editor. Read it top to bottom.
   That is roughly what the parser sees. If the order is wrong, the parse is wrong.
3. Check your phone and email survived the copy-paste.
4. Name the file `firstname-lastname-resume.pdf`. That filename is what a recruiter
   sees in their inbox.

That paste test takes twenty seconds and catches almost everything.
""",
        "faq": [
            ("Which resume format is best for ATS?",
             "Reverse-chronological in a single column, with standard headings such as Work Experience, Education and Skills. It is the format parsers were built around and the one recruiters expect, so it costs you nothing to use it."),
            ("Do ATS systems reject resumes with columns?",
             "They do not reject them outright, but a two-column layout can be read across rather than down, which interleaves your sidebar into your job history. Since you cannot tell which parser will handle it, a single column removes the risk entirely."),
            ("Should my resume be a PDF or a Word document?",
             "PDF, unless the posting explicitly asks for .doc or .docx. Modern parsers read PDF text reliably and PDF preserves your layout everywhere. Never send a resume as an image or a scan."),
            ("Will a photo stop my resume from parsing?",
             "The photo itself is ignored, so it does no parsing harm. Whether to include one is a regional question: normal in much of Europe and Asia, usually left off in the US, UK and Canada, where it can raise bias concerns."),
            ("How many keywords should I put in my resume?",
             "Enough to describe what you genuinely did, using the posting's own wording. Keyword stuffing and white-text keyword lists are detectable and will end an application when a human reads it. Mirror the vocabulary, do not pad it."),
            ("Are these ATS templates really free?",
             "Yes. All 50 templates, every editor feature and PDF export are free, with no signup, no trial and no watermark."),
        ],
    },

    # ------------------------------------------------------- PROFESSIONAL
    {
        "path": "/professional-resume-templates/",
        "filter": "professional",
        "crumb": "Professional resume templates",
        "nav": "Professional templates",
        "kicker": "Professional templates",
        "title": "Professional Resume Templates, Free | ResumeElite",
        "h1": "Professional resume templates for corporate applications",
        "description": "Free professional resume templates for corporate, finance, legal and management roles. Conservative structure, clear hierarchy, instant PDF download.",
        "about": "Professional resume design for corporate roles",
        "grid_title": "Professional layouts",
        "grid_sub": "All {count} of them: restrained, well-spaced, and built to look considered rather than decorated.",
        "cta_h": "Send something that looks considered",
        "cta_p": "Pick a layout, fill in your details, export a clean PDF.",
        "intro": """
A professional resume is not a plain resume. Plain means stripped of everything;
professional means every choice looks deliberate. Consistent spacing, one accent
colour used sparingly, a clear hierarchy that lets someone find your current role
in about two seconds.

These are the layouts for corporate applications: finance, law, insurance,
consulting, operations, management. They are conservative without being dull.
""",
        "body": """
## What "professional" means in practice

Recruiters describe the same handful of things when asked what a good resume looks
like, and none of them are creative decisions:

- **The current role is findable instantly.** Top of page one, clearly the most
  prominent entry.
- **Dates line up.** In a column, same format throughout. Ragged dates read as
  carelessness even when the content is strong.
- **One typeface, two or three weights.** Mixing typefaces almost never helps.
- **Colour appears two or three times, not everywhere.** Section headings and a rule.
  That is enough.
- **Whitespace is even.** Uneven gaps between sections are the most common thing that
  makes a resume feel amateur, and almost nobody notices they have done it.

Every template here handles that last point for you, because the spacing is set in
the layout rather than typed in by hand.

## Which one to pick

**[Professional](/templates/professional-resume-template/)** is the default
recommendation and the most-used layout on the site. Two columns with a timeline
spine down the middle, photo header, dates on the left. It reads as organised
immediately and it holds a lot of content without feeling crowded.

**[Modern](/templates/modern-resume-template/)** is the sidebar structure most people
picture when they think "modern CV" -- contact and skills in a narrow rail, history
in the wide column. Strong hierarchy, very easy to scan.

**Executive** and **Modern Executive** are for senior applications. Serif nameplate,
more air, fewer entries with more said about each. Do not use these early in a career
-- the extra space just makes a short history look shorter.

**Corporate** and **Classic Blue** are the conservative end: ruled header, no photo
by default, nothing that could be read as a flourish. Banking, insurance, legal,
public sector.

**Consulting** is the McKinsey-style density convention -- Garamond, tight leading, a
burgundy rule, contact stack aligned right. It fits a lot on one page on purpose.

**Compact** and **Clean Sidebar** solve the two-page problem from opposite
directions: Compact tightens everything, Clean Sidebar moves the short items into a
quiet right rail so the main column stays readable.

**Impact** is the newest of these and the most aggressive about hierarchy: oversized
role titles, a heavy accent bar per entry, and the summary in a tinted block. Good
when your job titles are the strongest thing you have.

## The two-page question

One page for early career. Two once you have several roles worth real detail.

The mistake is not length, it is what fills it. A second page of skills lists,
hobbies and "references available on request" is worse than a tight single page. A
second page of specific, quantified work is fine.

If you are one or two lines over, do not shrink the font below about 10pt. Cut a
bullet from your oldest role instead. Nobody has ever been rejected for saying less
about a job they left nine years ago.

## Writing to fill these layouts

The layout will not save weak content. Two things move the needle most:

**Lead with the outcome.** "Responsible for the onboarding flow" is a job
description. "Cut onboarding drop-off 34% by rebuilding the first-run flow" is a
result. Same work, completely different signal.

**Say how big.** A number gives scale and scale gives credibility. Team size, budget,
user count, transaction volume, percentage change. If you cannot share a real figure,
give the shape: "a team of eleven", "a seven-figure portfolio".

Three to five bullets for your current role, one or two for anything more than five
years old. There is more on this in our guide to
[writing a resume](/blog/how-to-write-a-resume/) and the list of
[action verbs that actually land](/blog/resume-action-verbs/).
""",
        "faq": [
            ("What is the best resume format for a corporate job?",
             "Reverse-chronological, one or two columns, with your current role at the top of page one. It is what recruiters in corporate roles expect, and deviating from it costs you attention you could have spent on your content."),
            ("Should a professional resume include a photo?",
             "In the US, UK, Canada and Australia, usually not -- it introduces bias risk and many companies strip it. Across much of continental Europe, Latin America and Asia a photo is normal and sometimes expected. Check the convention where you are applying."),
            ("How long should a professional resume be?",
             "One page early in a career, two pages once you have several relevant roles worth detail. Two pages of specific, quantified work is fine; two pages padded with skills lists and hobbies is worse than one tight page."),
            ("Do I need a summary section?",
             "It helps when you are changing direction, when your job titles do not describe what you actually did, or when you are senior enough that positioning matters. Three or four lines maximum, and no adjectives you cannot evidence."),
            ("Can I switch templates after I have written everything?",
             "Yes. Content is stored separately from the design, so you can move between all 50 templates and every section, date and bullet carries across instantly."),
        ],
    },

    # ------------------------------------------------------------ MODERN
    {
        "path": "/modern-resume-templates/",
        "filter": "trending",
        "crumb": "Modern CV templates",
        "nav": "Modern CV templates",
        "kicker": "Modern templates",
        "title": "Modern CV Templates for 2026, Free | ResumeElite",
        "h1": "Modern CV templates that look like this year, not 2014",
        "description": "Free modern resume and CV templates for 2026: gradient headers, colour spines, editorial grids and dark developer layouts. Live preview, instant PDF.",
        "about": "Contemporary resume and CV design",
        "grid_title": "The 2026 collection",
        "grid_sub": "{count} layouts built on current design conventions rather than the sidebar template everyone has been sending since 2014.",
        "cta_h": "Try the newest layout on the site",
        "cta_p": "Switch between all thirteen without retyping a word.",
        "intro": """
Resume design has a lag problem. The layouts most builders still ship -- a coloured
left sidebar, a circular photo, a row of skill rating dots -- were fresh around 2014
and have been the default ever since. They now read as dated, and the skill dots in
particular tell a recruiter nothing (what is four out of five at SQL?).

This collection is the current set: soft gradients, generous type scales, editorial
grids, hairline rules, and one genuinely dark layout for developers.
""",
        "body": """
## What changed

**Gradients came back, but soft.** Not the hard two-colour splits of a decade ago --
wide, low-contrast mesh blends. **Aurora** and **Spectrum** use them in the masthead
and the spine while keeping the body plain white so the content stays readable.

**Type got bigger and tighter.** Names at 40-50px with negative letter-spacing. It
sounds loud and reads as confident, because the size is doing the hierarchy work
instead of colour.

**Grids got honest.** **Swiss** numbers its sections and hangs the labels in a left
column on hairline rules. **Atelier** runs your name vertically down a black spine.
These are typographic decisions, not decorations.

**Skill dots died.** None of these templates rate your skills out of five, because a
recruiter cannot use that number and a hiring manager will ask you about it.

**Dark mode arrived on paper.** **Terminal** is a full dark IDE aesthetic in
monospace with `//` section comments. It is a strong signal and a narrow one -- see
below.

## The collection, briefly

- **Aurora** -- gradient mesh masthead, glass side rail. Design, marketing, product.
- **Spectrum** -- rainbow spine down the left, gradient section rules, card rail.
- **Impact** -- oversized role titles and heavy accent bars. Recruiter-first.
- **Metro** -- diagonal two-tone header with ribbon section titles. Confident, corporate-safe.
- **Terminal** -- dark, monospace, code-comment headings. Developers only.
- **Brutalist** -- thick borders and hard offset shadows. Portfolios that need to interrupt.
- **Swiss** -- numbered sections, hairline rules, huge uppercase name.
- **Vogue** -- editorial fashion masthead, two-column body, drop-cap profile.
- **Luxe** -- ivory and gold, wide-tracked serif. Senior and luxury sectors.
- **Atelier** -- vertical name spine, asymmetric content column.
- **Elite Flagship** -- dark gold-accented header band with a sidebar.
- **Modern Executive** -- premium C-suite columns, divided contact grid.
- **Professional** -- the two-column timeline. Modern but completely safe.

## How much personality is too much

This is the real question, and the answer is about who opens the file.

**Safe almost everywhere:** Professional, Impact, Metro, Modern Executive. Contemporary
without being a statement. If you are unsure, pick from these four.

**Right when a human reads first:** Aurora, Spectrum, Vogue, Brutalist, Atelier,
Swiss. Agencies, studios, startups, referrals, anywhere a person opens the inbox.

**Narrow but powerful:** Terminal. A developer applying to an engineering team will
get a smile from it. The same file sent to a bank's HR portal is a mistake. It also
prints a lot of dark ink, which matters if anyone puts it on paper.

**Senior only:** Luxe, Elite Flagship. The wide spacing needs content to justify it.

## The honest trade-off

A designed resume is a bet that a person reads it before a machine does. That bet pays
well when it lands and costs you when it does not.

None of these templates hide your text -- everything exports as real selectable text,
so a parser can read them. But the multi-column ones carry the reading-order risk
described on the [ATS templates page](/ats-resume-templates/), and that risk is not
zero.

The practical approach is to keep two versions. Your content lives independently of
the design here, so switching is one click: send the modern one to people, send
**ATS Friendly** or **Chronological** to portals. That is not indecision, it is just
matching the file to the reader.
""",
        "faq": [
            ("What makes a CV look modern in 2026?",
             "Large tight-tracked type doing the hierarchy work, generous even whitespace, soft low-contrast colour used two or three times, and the absence of dated devices like skill rating dots and circular photo badges."),
            ("Are modern resume templates ATS-friendly?",
             "The single-column ones are. Multi-column layouts export real selectable text but carry a reading-order risk in some parsers. If a machine screens first, use a plain single-column template and keep the modern one for human readers."),
            ("Is a creative resume risky?",
             "It depends entirely on who opens it first. For agencies, studios, startups and referrals it helps you stand out. For large-company portals it adds risk without adding much upside."),
            ("Can I use a dark resume template?",
             "For developer and design roles where a human reviews it, yes -- Terminal is built for exactly that. Avoid it for corporate portals, and remember it uses a lot of ink if anyone prints it."),
            ("Which modern template should I start with?",
             "Professional if you want modern and completely safe, Impact if your job titles are your strongest asset, and Aurora or Spectrum if you are applying somewhere design-literate."),
        ],
    },

    # ---------------------------------------------------------- CREATIVE
    {
        "path": "/creative-resume-templates/",
        "filter": "creative",
        "crumb": "Creative resume templates",
        "nav": "Creative templates",
        "kicker": "Creative templates",
        "title": "Creative Resume Templates for Designers | ResumeElite",
        "h1": "Creative resume templates for people whose work is visual",
        "description": "Free creative resume templates for designers, writers, marketers and freelancers. Editorial grids, bold blocks and portfolio layouts with real selectable PDF text.",
        "about": "Creative resume and portfolio CV design",
        "grid_title": "Creative layouts",
        "grid_sub": "{count} designs that treat the resume as a piece of work rather than a form to fill in.",
        "cta_h": "Make the resume part of the portfolio",
        "cta_p": "Pick a layout, set your accent colour, export the PDF.",
        "intro": """
If you are applying for a job where taste is part of the assessment, a plain resume
is a wasted opportunity. The document is the first sample of your work anyone sees.
Sending a Times New Roman single column to an art director is its own kind of answer.

These layouts are for designers, art directors, writers, marketers, photographers,
architects and freelancers -- people whose resume is read by a human with an eye.
""",
        "body": """
## Choosing by what your work actually is

**Typographic and restrained** -- when you want the craft to show in the setting
rather than the colour. **Swiss** (numbered sections, hairline rules), **Editorial**
(rotated section label, wide serif nameplate), **Vogue** (fashion masthead, two
columns, drop cap), **Luxe** (ivory and gold, wide tracking), **Atelier** (vertical
name spine).

**Bold and interruptive** -- when the brief is to be noticed. **Brutalist** (thick
borders, hard offset shadows), **Bold** (high-contrast filled header),
**Creative** (colour-blocked header with playful section markers).

**Portfolio-shaped** -- when the work matters more than the chronology.
**Portfolio** (deep navy sidebar, rounded avatar), **Freelancer** (warm light sheet
with a service rail), **Infographic** (dual-column tinted grid), **Startup**
(projects before history).

**Colourful but calm** -- contemporary without shouting. **Aurora** (gradient mesh
masthead), **Spectrum** (colour spine, gradient rules), **Nordic** (hairline boxes on
warm paper), **Timeline** (connected career spine), **Mono** (typewriter on warm
paper).

## Five rules that keep a creative resume employable

**One idea, executed properly.** A gradient masthead *or* a vertical name spine *or*
thick brutalist borders. Two of those in one document reads as indecision, and the
templates here each commit to one.

**Restrict the palette.** One accent, applied two or three times. The accent colour
control in the editor changes every template at once, so try your portfolio colour
and see it land in the right places.

**Never put words inside a graphic.** Not your name, not your title, not your skills.
If a parser ever touches it, that text does not exist. This is also why none of these
templates render text as an image.

**Do not rate your own skills.** Four-out-of-five dots for Illustrator is unverifiable
and slightly odd. Name the tools, then show the work.

**Give it somewhere to go.** A portfolio URL on a creative resume is the whole point.
The editor keeps links live and clickable in the exported PDF, so put the real URL in
rather than "portfolio available on request".

## Where creative layouts backfire

Two situations, and both are about the reader.

**Large-company application portals.** If you upload to a system rather than email a
person, a sidebar layout can be read across instead of down. See the
[ATS templates](/ats-resume-templates/) page for what that actually looks like.

**In-house recruiting at a non-design company.** A marketing role at an insurer is
still an insurer. Something like **Elegant** or **Impact** gets you contemporary
without asking anyone to have taste.

The workable pattern: your content is stored separately from the design here, so keep
the creative version for people and switch to a plain one for portals. Same content,
one click.

## What to include that a normal resume would not

- **Two or three named projects with the outcome.** Not "redesigned the website" --
  "rebuilt the checkout, cut abandonment 22%".
- **The tools, named plainly.** Figma, After Effects, Blender, InDesign. No ratings.
- **Clients or brands, if you can name them.** Recognition does work here.
- **A live link.** Portfolio, Behance, Dribbble, GitHub, personal site.
- **What you actually want to do next**, in one line, if your history is varied.

Leave out: hobbies unless they are relevant, "references on request", and any personal
logo or monogram. That last one is the most common self-inflicted wound on a creative
resume -- branding yourself with a mark nobody knows reads as a student exercise.
""",
        "faq": [
            ("Should designers use a creative resume template?",
             "Yes, when a person reviews it -- the document is a work sample. Keep a plain single-column version for large-company upload portals, where a multi-column layout can be parsed in the wrong reading order."),
            ("Do creative resume templates pass ATS checks?",
             "Every template here exports real selectable text, so nothing is invisible to a parser. The multi-column ones still carry a reading-order risk, so use a single-column layout when software screens first."),
            ("How much colour is too much on a resume?",
             "One accent colour applied two or three times is the working limit. More than that and the reader stops seeing hierarchy, which is the only job colour is doing."),
            ("Should I put my portfolio link on my resume?",
             "Always, for any creative role. Links stay clickable in the exported PDF, so use the real URL rather than saying a portfolio is available on request."),
            ("Are skill rating dots a bad idea?",
             "Yes. Four out of five at Photoshop is unverifiable and invites a question you cannot answer well. Name the tools and let the work carry the claim."),
        ],
    },

    # -------------------------------------------------------------- TECH
    {
        "path": "/tech-resume-templates/",
        "filter": "tech",
        "crumb": "Developer resume templates",
        "nav": "Developer resume templates",
        "kicker": "Tech templates",
        "title": "Software Engineer Resume Templates | ResumeElite",
        "h1": "Software engineer resume templates built around the stack",
        "description": "Free resume templates for software engineers, QA, DevOps and data roles. Stack and projects up front, real PDF text, and a dark terminal layout. No signup.",
        "about": "Software engineering resume formatting",
        "grid_title": "Templates for engineering roles",
        "grid_sub": "{count} layouts that give the stack, the projects and the impact somewhere sensible to live.",
        "cta_h": "Ship the resume",
        "cta_p": "Pick a layout, paste in your work, export the PDF.",
        "intro": """
Engineering resumes have a specific failure mode: a wall of technologies at the top,
then job entries that describe the team's roadmap rather than what you built. The
reader learns your stack and nothing about your judgement.

These templates give the stack a proper home so the experience section can be about
work. Two of them -- Software Engineer and Terminal -- were designed for this
specifically.
""",
        "body": """
## What an engineering hiring manager is looking for

Roughly in order:

1. **Can they do the job we are hiring for?** Stack overlap, and how recent it is.
2. **Have they shipped something that ran in production?** Scale, traffic, uptime,
   data volume -- anything that implies real constraints.
3. **Did they make decisions or execute tickets?** The difference between "worked on
   the payments service" and "moved payments off the monolith, cut p99 from 900ms to
   210ms".
4. **Can they write?** The resume is the sample. Vague bullets read as vague thinking.

The templates handle the layout; that list is what the words have to do.

## Which template

**[Software Engineer](/templates/software-engineer-resume-template/)** is the default.
Tinted sidebar for languages, frameworks, tooling and certifications, wide main column
for experience and projects. Everything has a place, which is the main thing.

**Tech** is a two-column variant that puts projects higher. Good early-career, when
side projects are doing more work than employment history.

**Terminal** is the dark one -- monospace, `// section` headings, a window chrome bar
at the top. Sending it to an engineering team where a person reads it is a good
signal. Sending it to a large-company HR portal is not, and it uses a lot of ink on
paper.

**Impact** is worth considering if your titles and numbers are strong. Oversized role
titles, heavy accent bars, summary in a tinted block.

**QA Engineer** has room for test tooling, frameworks and coverage detail, which a
generic template makes awkward.

**Startup** puts projects before employment entirely. Right for founders, bootcamp
graduates and anyone whose best work was not a job.

For plain-parse insurance, **ATS Friendly** and **Chronological** from the
[ATS collection](/ats-resume-templates/) are the safe pair.

## Writing the skills section

The most common mistake is one undifferentiated list of thirty items, which forces the
reader to guess what you are actually good at.

Group it and order it by strength:

```
Languages     Python, Go, TypeScript, SQL
Frameworks    Django, FastAPI, React, Next.js
Data          Postgres, Redis, Kafka, dbt, Snowflake
Infra         AWS, Docker, Kubernetes, Terraform, GitHub Actions
```

Four or five groups, five or six items each. Leave out anything you would not want to
be interviewed on -- a listed skill is an invitation. And drop the version numbers
unless they matter (Python 3 is not a differentiator; Java 8 versus 21 sometimes is).

## Writing the experience bullets

Structure that works: **what you built, the constraint, the measured result.**

Weak:

> Worked on the payments service. Used Go and Kafka. Participated in code reviews.

Strong:

> Extracted payments from the Rails monolith into a Go service handling 4k req/s,
> keeping a zero-downtime cutover across 11 regions. Cut p99 latency from 900ms to
> 210ms and dropped failed-charge retries 38%.

Same job. The second one shows scale, a real constraint, and two numbers. It is also
harder to write, which is why most resumes do not.

If you genuinely cannot share numbers, give shape instead: "a service used by every
internal team", "a migration across eleven regions", "a codebase of about 400k lines".

## Projects, and how many

Two or three, with the same structure as a job entry: what it is, what it is built
with, why it exists, what happened. A link if it is public.

Early career, projects can be your strongest section and should sit above education.
Ten years in, one project is enough and only if it is genuinely interesting -- a
to-do app on a senior resume actively works against you.

More on phrasing in the [action verbs guide](/blog/resume-action-verbs/) and
[how to write a resume](/blog/how-to-write-a-resume/).
""",
        "faq": [
            ("How long should a software engineer resume be?",
             "One page for under about eight years of experience, two after that. Engineering hiring managers skim fast, and a tight page reads as better judgement than a padded two."),
            ("Should I list every technology I have used?",
             "No. Group four or five categories with five or six items each, and only include things you would happily be interviewed on. A listed skill is an invitation to be tested on it."),
            ("Do I need a GitHub link on my resume?",
             "Only if the profile shows something. An active repository or a project with a readable README helps; an empty profile with three forks is worse than no link at all."),
            ("Where do side projects go on an engineering resume?",
             "Above employment if you are early-career or changing direction, below it once you have shipped production work professionally. Two or three, described like job entries."),
            ("Is a dark or terminal-style resume a good idea for developers?",
             "For an engineering team where a person reads it, it lands well. For a large-company application portal use a plain single-column template instead, and remember dark layouts use a lot of ink if printed."),
            ("How do I show impact without sharing confidential numbers?",
             "Give the shape rather than the figure: request volume in orders of magnitude, team size, number of regions, relative improvement as a percentage. Relative change is almost never confidential."),
        ],
    },

    # ---------------------------------------------------------- ACADEMIC
    {
        "path": "/academic-cv-templates/",
        "filter": "academic",
        "crumb": "Academic CV templates",
        "nav": "Academic CV templates",
        "kicker": "Academic templates",
        "title": "Academic CV Templates, Free | ResumeElite",
        "h1": "Academic CV templates for research, teaching and study",
        "description": "Free academic CV and student resume templates with hanging-indent publication lists, Europass structure and education-first layouts. Live preview, instant PDF.",
        "about": "Academic CV and student resume formatting",
        "grid_title": "Academic and student layouts",
        "grid_sub": "{count} templates for research CVs, graduate applications and first resumes.",
        "cta_h": "Build the CV",
        "cta_p": "Publication lists, coursework, funding, teaching -- all sections you can add and reorder.",
        "intro": """
An academic CV is a different document from a resume, and treating them the same is
the usual mistake. A resume argues that you can do a job in one or two pages. A CV
records a scholarly record completely -- publications, funding, teaching, service,
conferences -- and it grows for your whole career.

This collection covers both ends: full research CVs, and the education-first layouts
that make sense when your degree is the strongest thing you have.
""",
        "body": """
## CV or resume?

| | Academic CV | Resume |
|---|---|---|
| Length | As long as the record requires | One or two pages |
| Goal | Complete scholarly record | Argument for one job |
| Publications | Full list, formatted citations | Selected, or omitted |
| Teaching | Courses, levels, enrolment | Rarely |
| Funding | Grants, amounts, role | Rarely |
| Ordering | Education first | Experience first, usually |

If you are applying for a postdoc, a fellowship, a lectureship or a PhD place, you
want a CV. If you are a graduate applying to industry, you want a resume -- and
industry recruiters do get put off by an eight-page CV for a junior role.

## Which template

**[Academic CV](/templates/academic-cv-template/)** is the research layout. Georgia
serif, small-caps section headings with rules that only span the heading, and hanging
indents on every entry -- the shape a publication list is supposed to have, where the
first line sits out and continuations tuck under. It runs to as many pages as you
need.

**Harvard Style** is the centred Garamond convention with a double rule under the
name. Standard for finance, consulting and law, and common for academic job letters
in the US.

**LaTeX Style** looks like a CV set in a LaTeX class -- Times, thin section rules,
light name weight. Familiar in maths, physics and CS, and it parses cleanly.

**Traditional Serif** is book typography for the humanities, law and public
institutions.

**Europass** follows the EU structured convention with labelled personal-detail rows.
Some European institutions and public bodies still ask for it specifically. Use it
when asked for, not by default -- it is verbose.

**Graduate** is education-first with a double-rule header, for a first or second job
after a degree.

**Student** is the friendliest layout on the site: rounded cards with colour-coded
sections, built to make coursework, projects and activities look substantial when
employment history is thin.

## Sections a normal resume does not have

The editor lets you add and reorder sections, which matters more for academic CVs
than anything else. The ones you are likely to want:

- **Publications** -- reverse-chronological, consistent citation style, your name
  bolded so a reader can find you in a nine-author list. Split peer-reviewed from
  preprints and chapters if there are enough of them.
- **Conferences** -- talks and posters separately; note invited talks explicitly.
- **Funding** -- grant, funder, amount, your role, dates. Do not be shy about amounts.
- **Teaching** -- course, level, your role, enrolment size.
- **Supervision** -- students supervised, level, completion year.
- **Service** -- reviewing, committees, editorial roles.
- **Courses** -- for students, relevant modules with grades if they are good.

## Ordering, for students

Whatever is strongest goes first, and early on that is almost never employment.

A sensible order for a recent graduate: Education, Projects, Relevant Coursework,
Internships, Skills, Activities, Employment. If a summer job is genuinely relevant,
move it up. If it was retail and you are applying to a lab, it belongs at the bottom
as evidence you can hold a job, not as a headline.

Two things students under-use: **a specific project section** (a dissertation with a
one-line result is stronger than three bullets about a supermarket job), and
**numbers** (a cohort rank, a grade average, a society you grew from 12 to 60
members).

More in our guide to writing a
[resume with no experience](/blog/resume-with-no-experience/).

## Formatting the publication list

Pick one style -- APA, Chicago, Vancouver, whatever your field uses -- and be
consistent to the punctuation. Inconsistent citations are the fastest way to look
careless to an academic reader.

Bold your own name in the author list. In a nine-author paper, that one detail is the
difference between a reader finding you and giving up.

Number entries if the list is long: a hiring committee referring to "publication 14"
is a good sign, and it is impossible without numbers.
""",
        "faq": [
            ("How long should an academic CV be?",
             "As long as the record needs. Two to four pages early on, ten or more for an established researcher. Unlike a resume there is no page limit, but every line still has to be information rather than filler."),
            ("What is the difference between a CV and a resume?",
             "A CV is a complete scholarly record with no length limit, ordered education-first. A resume is a one or two page argument for a specific job, ordered experience-first. Applying to industry with a long CV usually hurts you."),
            ("Should a student resume include a GPA?",
             "Include it if it is strong -- roughly a 3.5 out of 4 or a UK 2:1 and above -- and leave it off otherwise. A cohort rank or a specific module grade is often more persuasive than an average."),
            ("What order should sections go in for a recent graduate?",
             "Education, then projects, then relevant coursework, then internships, then skills. Put whatever is genuinely strongest first, and keep unrelated part-time work at the bottom."),
            ("Do I need a Europass CV for European applications?",
             "Only when an institution or public body asks for it by name. It is a verbose format, and for private-sector applications in Europe a normal well-formatted CV is usually received better."),
            ("How do I list publications where I am not first author?",
             "Keep the real author order and bold your own name so a reader can find you. Never reorder authors to move yourself up -- it is checkable and it ends the application."),
        ],
    },
]


# ===========================================================================
# PER-TEMPLATE PAGES
# ===========================================================================

TEMPLATE_PAGES = [
    {
        "id": "professional",
        "path": "/templates/professional-resume-template/",
        "category_path": "/professional-resume-templates/",
        "category_name": "Professional templates",
        "kicker": "Template guide",
        "title": "Professional Resume Template, Free | ResumeElite",
        "title_h1": "The Professional resume template",
        "description": "A free two-column professional resume template with a timeline spine, photo header and left-aligned dates. Live preview, accent colours, instant PDF download.",
        "intro": """
The most-used layout on the site, and the one to pick if you do not want to think
about it. Two columns with a timeline spine down the middle, dates in a left rail, a
soft photo header, and section headings in your accent colour.
""",
        "facts": [
            ("Best for", "Corporate, management, operations, finance"),
            ("Structure", "Two columns, timeline spine, photo header"),
            ("Length", "Holds one to three pages comfortably"),
            ("ATS", "Exports real text; use a plain layout for portals"),
        ],
        "alternatives": ["modern", "impact", "compact"],
        "body": """
## Why this one is the default

It solves the problem most resumes have, which is that a reader cannot tell where one
role ends and the next begins. The timeline spine does that work visually: dates on
the left, a marker on the spine, content on the right. You can see the shape of a
career in about two seconds without reading a word.

It also holds a lot. Three roles with four bullets each, education, skills, languages,
projects and certifications fit without feeling crowded, because the spacing is set by
the layout rather than typed by hand.

## What it looks like filled in

- **Header** -- name in the accent colour at around 34px, job title under it, contact
  row with icons, optional photo top-right.
- **Left rail** -- date ranges, right-aligned so they form a clean column.
- **Spine** -- a thin vertical rule with a square marker at each entry.
- **Main column** -- role title in bold, employer and location in the accent colour,
  then description text.
- **Skills and languages** -- a two-column grid rather than a tag cloud, so long skill
  names do not wrap awkwardly.

## Filling it well

**Use the summary.** Three or four lines at the top, and make them about direction
rather than adjectives. "Product leader with nine years in data-heavy B2B, twice from
zero to eight figures of ARR" is worth reading. "Motivated self-starter with excellent
communication skills" is not.

**Keep the date format consistent.** The rail only looks clean if every entry uses the
same shape -- `2021 - Present` and `2018 - 2021`, not one of them as `Jan 2018`.

**Three to five bullets on your current role, one or two on older ones.** The spine
makes uneven entries obvious, which is useful: if your 2016 job has more detail than
your current one, you can see it immediately.

**Turn the photo off for US, UK, Canada and Australia.** The header rebalances
automatically. In much of Europe and Asia, leave it on.

## Accent colour

The default blue is safe everywhere. If you want to change it, the six presets are
picked to stay readable in print:

- **Blue** -- default, safe in every sector.
- **Teal** -- softer, common in health, education and non-profit.
- **Violet** -- tech and product.
- **Coral** -- creative and marketing. Slightly warm for finance.
- **Gold** -- senior, luxury, hospitality.
- **Ink** -- near-black. Effectively the conservative choice, and the best pick for
  law, banking and anywhere a resume gets printed in mono.

## When to pick something else

- Applying through a large-company portal where software screens first -- use
  **ATS Friendly** or **Chronological** from the
  [ATS collection](/ats-resume-templates/).
- Long career that must fit one page -- **Compact** or **Consulting**.
- Want the same structure but more contemporary -- **Impact** or **Metro** from the
  [modern collection](/modern-resume-templates/).
- Design or creative role where a person reads first -- see the
  [creative templates](/creative-resume-templates/).

Switching costs nothing. Your content is stored separately from the design, so every
section, date and bullet carries across.
""",
        "faq": [
            ("Is the Professional template ATS-friendly?",
             "It exports real selectable text, so nothing is hidden from a parser. It is a two-column layout though, so for large-company upload portals a single-column template such as ATS Friendly is the safer choice."),
            ("Can I remove the photo?",
             "Yes. Leave the photo field empty and the header rebalances automatically. Leave it off for the US, UK, Canada and Australia; keep it for much of Europe and Asia."),
            ("How many pages does it hold?",
             "One to three comfortably. Page breaks are shown live in the editor, and sections are kept from splitting awkwardly across a break."),
            ("Can I reorder the sections?",
             "Yes, by dragging them in the editor. You can also hide any section you do not need and add internships, courses, references, achievements or a custom section."),
        ],
    },
    {
        "id": "ats-friendly",
        "path": "/templates/ats-friendly-resume-template/",
        "category_path": "/ats-resume-templates/",
        "category_name": "ATS resume templates",
        "kicker": "Template guide",
        "title": "ATS-Friendly Resume Template, Free | ResumeElite",
        "title_h1": "The ATS Friendly resume template",
        "description": "A strict single-column ATS resume template: Arial, black on white, standard headings, no graphics. Built to parse cleanly in applicant tracking systems.",
        "intro": """
The strictest layout on the site, and deliberately the plainest. One column, Arial,
black on white, standard headings, comma-separated skills, no accent colour and no
graphics at all. It exists to remove formatting as a variable.
""",
        "facts": [
            ("Best for", "Large-company portals, high-volume applications"),
            ("Structure", "Single column, no graphics, standard headings"),
            ("Length", "One or two pages"),
            ("ATS", "The safest layout here"),
        ],
        "alternatives": ["chronological", "minimal", "functional"],
        "body": """
## What it deliberately does not do

No sidebar. No colour. No icons. No photo. No tables. No text inside images. No
decorative bullet glyphs. Nothing in a header or footer.

Every one of those absences is a parsing failure mode removed. The result is a
document that looks like everyone else's -- which is the trade you are making.

## Why plain still matters

Applicant tracking systems read a resume as a single stream of text. The most common
way that goes wrong is a two-column layout being read across instead of down, so your
skills rail interleaves with your job history and comes out as
"Python Senior Engineer SQL Northwind Analytics".

You cannot tell which parser a company runs, and you get no feedback when it goes
wrong -- just silence. This template removes the possibility.

## When to use it

- The posting names a specific ATS, or you are uploading through Workday, Taleo,
  Greenhouse, iCIMS or SuccessFactors.
- You are applying at volume and cannot tailor the format per company.
- You have sent thirty applications with a designed resume and heard nothing, and want
  to eliminate formatting as the cause.
- A recruiter has asked for a "plain" or "text" version.

## When not to

If a person opens your file first -- an agency, a studio, a startup, a referral, a
small company -- this template spends none of the goodwill a good-looking document
buys you. Use something from the
[professional](/professional-resume-templates/) or
[modern](/modern-resume-templates/) collections instead, and keep this one for portals.

Keeping both costs nothing here: switch template, same content.

## Filling it in

**Use the expected headings.** Work Experience, Education, Skills, Certifications.
The template supplies them; do not rename them to something clever.

**Front-load each bullet.** With no visual hierarchy to help, the first four or five
words of every line carry the whole weight. Start with the verb and the outcome.

**Spell out acronyms once.** "Search Engine Optimisation (SEO)" catches both the
spelled-out and abbreviated keyword. After that, use whichever the posting uses.

**Keep skills as a comma list.** The template renders them inline on purpose -- it is
the most reliably parsed shape.

**Put contact details in the body.** Already handled: nothing lives in a header or
footer, because many parsers skip those entirely.

## The paste test

Before you send any resume, do this:

1. Open the exported PDF.
2. Select all, copy.
3. Paste into a plain text editor.
4. Read it top to bottom.

That is approximately what the parser sees. If the order is wrong, or your phone
number vanished, or two sections have run together, fix it before you apply. On this
template the paste test comes out clean, which is the entire point of it.

There is more detail on parsing behaviour in
[how ATS software actually works](/blog/how-ats-works/).
""",
        "faq": [
            ("Will this template guarantee my resume passes ATS?",
             "No template can guarantee that, because parsers differ and the content still has to match the role. What it does is remove formatting as a cause of failure, which is the part you control."),
            ("Can I add a photo to this template?",
             "You can, but do not. The whole design intent is to remove anything a parser ignores or mishandles, and for US, UK and Canadian applications a photo carries bias risk as well."),
            ("Should I use this for every application?",
             "Only where software screens first. When a person opens your file, a plain document wastes an easy advantage -- keep a designed version for those and switch between them."),
            ("Does it work for two pages?",
             "Yes. Page breaks are shown live in the editor and sections avoid splitting mid-entry, so a two-page version stays readable."),
            ("Is Arial the right font for ATS?",
             "Any common system font parses fine -- Arial, Helvetica, Calibri, Times New Roman, Georgia. The font is almost never the problem; layout is."),
        ],
    },
    {
        "id": "modern",
        "path": "/templates/modern-resume-template/",
        "category_path": "/modern-resume-templates/",
        "category_name": "Modern CV templates",
        "kicker": "Template guide",
        "title": "Modern Resume Template, Free Sidebar CV | ResumeElite",
        "title_h1": "The Modern resume template",
        "description": "A free modern resume template with a sidebar for contact and skills, strong section hierarchy and a wide main column. Live preview and instant PDF export.",
        "intro": """
The sidebar structure most people picture when they think "modern CV": contact
details and short items in a narrow rail, employment history in the wide column, with
section labels hanging in the left margin.
""",
        "facts": [
            ("Best for", "Most industry roles, mid-career applications"),
            ("Structure", "Left label column, wide content column"),
            ("Length", "One to two pages"),
            ("ATS", "Exports real text; prefer a plain layout for portals"),
        ],
        "alternatives": ["professional", "clean-sidebar", "impact"],
        "body": """
## The idea

Section labels sit in a left column, content in a wider right column. Your eye runs
down the labels to find the section it wants, then across into the detail. It is the
same principle as a well-set reference book, and it is why this shape has lasted.

Compared with **Professional**, this layout is quieter -- no timeline spine, no
markers -- and slightly more spacious. It suits a history where the roles speak for
themselves.

## Filling it well

**The label column is narrow, so keep headings short.** "Work Experience" fits;
renaming it to something longer will wrap.

**Write the summary as positioning, not personality.** Two or three lines that say
what you do and at what level.

**Group skills instead of listing everything.** Because they sit in the sidebar,
around 12-18 items is the readable limit. Pick the ones relevant to the specific
application rather than everything you have touched.

**Watch the widow lines.** With a wide main column, a bullet that spills to a second
line by two words is visible. Cut two words.

## Accent colour

The accent lands on section labels, employer names and the job title. That is three
appearances -- enough for hierarchy, not enough to be loud. All six presets work; Ink
turns it into a mono document suitable for printing.

## When to pick something else

- Portal application where software screens first --
  [ATS Friendly or Chronological](/ats-resume-templates/).
- Long career that must fit one page -- **Compact**.
- You want the sidebar on the right instead -- **Clean Sidebar** or **Modern Right**.
- You want more visual force -- **Impact** or **Metro**.
""",
        "faq": [
            ("Is a sidebar resume template ATS-safe?",
             "It exports real selectable text, but any multi-column layout can be read in the wrong order by some parsers. For large-company portals use a single-column template and keep this one for human readers."),
            ("How many skills should I list?",
             "Around 12 to 18 in this layout, chosen for the specific role. Beyond that the sidebar gets crowded and the reader stops distinguishing between them."),
            ("Can I move the sidebar to the right?",
             "Use the Clean Sidebar or Modern Right templates -- both are right-rail layouts, and your content carries across when you switch."),
            ("Does this template support a photo?",
             "Yes, and it is optional. Leave it off for US, UK, Canadian and Australian applications."),
        ],
    },
    {
        "id": "software-engineer",
        "path": "/templates/software-engineer-resume-template/",
        "category_path": "/tech-resume-templates/",
        "category_name": "Developer resume templates",
        "kicker": "Template guide",
        "title": "Software Engineer Resume Template | ResumeElite",
        "title_h1": "The Software Engineer resume template",
        "description": "A free software engineer resume template with a tinted sidebar for stack and tooling, plus a wide column for shipped work and projects. Instant PDF export.",
        "intro": """
Built for engineering applications specifically. A tinted sidebar holds languages,
frameworks, tooling and certifications; the wide main column is left for experience
and projects, so the stack stops eating the top of page one.
""",
        "facts": [
            ("Best for", "Backend, frontend, full-stack, DevOps, data"),
            ("Structure", "Tinted sidebar for stack, wide column for work"),
            ("Length", "One page under ~8 years, two after"),
            ("ATS", "Exports real text; pair with a plain version for portals"),
        ],
        "alternatives": ["terminal", "impact", "tech"],
        "body": """
## The problem it solves

Most engineering resumes open with a thirty-item technology list, and by the time the
reader reaches your work they have already spent their attention. Moving the stack
into a sidebar means the first thing in the main column is something you built.

## Filling the sidebar

Group by category and order by strength:

```
Languages     Go, Python, TypeScript, SQL
Frameworks    FastAPI, React, Next.js
Data          Postgres, Redis, Kafka, dbt
Infra         AWS, Docker, Kubernetes, Terraform
```

Four or five groups, five or six items each. Only list things you would happily be
interviewed on -- everything in that sidebar is an invitation. Drop version numbers
unless they carry real signal.

Certifications go underneath: AWS, GCP, Kubernetes, security. Skip the ones that are
a day of clicking through videos.

## Writing the main column

The pattern that works is **what you built, the constraint, the measured result.**

Weak:

> Worked on the payments service using Go and Kafka. Participated in code reviews and
> sprint planning.

Strong:

> Extracted payments from the Rails monolith into a Go service handling 4k req/s, with
> a zero-downtime cutover across 11 regions. Cut p99 latency 900ms to 210ms and
> reduced failed-charge retries 38%.

The second one shows scale, a real constraint, and two numbers. Aim for three to five
bullets like that on your current role, one or two on older ones.

If the numbers are confidential, give the shape instead: request volume in orders of
magnitude, number of regions, team size, or a relative percentage change. Relative
change is almost never sensitive.

## Projects

Two or three, described like job entries: what it is, the stack, why it exists, what
happened. A link if it is public and worth opening.

Early career, put projects above employment. Once you have shipped production work
professionally, one strong project is plenty -- and a tutorial to-do app on a senior
resume works against you.

## When to pick something else

- **Terminal** if a person definitely reads it and you want the file itself to signal
  developer. Dark, monospace, `//` headings. Not for portals, and heavy on ink.
- **Impact** if your titles and numbers are the strongest thing you have.
- **Startup** if your best work was not a job.
- **ATS Friendly** or **Chronological** for portal uploads.

See the whole [developer collection](/tech-resume-templates/) for the rest.
""",
        "faq": [
            ("How long should a software engineer resume be?",
             "One page under roughly eight years of experience, two after that. Engineering managers skim quickly, and a tight page reads as better judgement than a padded two."),
            ("Should the skills section go at the top?",
             "It should be easy to find, which is what the sidebar achieves, but it should not be the first thing in the main reading column. Lead with what you shipped."),
            ("What if I cannot share performance numbers?",
             "Give the shape rather than the figure: orders of magnitude for traffic, number of regions or services, team size, or a relative percentage improvement. Relative change is rarely confidential."),
            ("Do I need to list every framework I have used?",
             "No, and it hurts. Anything in the sidebar is fair game in an interview, so list what you can defend and leave the rest out."),
        ],
    },
    {
        "id": "harvard-style",
        "path": "/templates/harvard-resume-template/",
        "category_path": "/academic-cv-templates/",
        "category_name": "Academic CV templates",
        "kicker": "Template guide",
        "title": "Harvard Resume Template, Free | ResumeElite",
        "title_h1": "The Harvard Style resume template",
        "description": "A free Harvard-style resume template: centred Garamond header, double rule, small-caps sections. The classic format for finance, consulting, law and academia.",
        "intro": """
The centred serif convention: name in Garamond small caps, a double rule beneath it,
contact details centred, section headings ruled across the full measure. Traditional,
restrained, and instantly recognisable to anyone who has recruited in finance, law or
academia.
""",
        "facts": [
            ("Best for", "Finance, consulting, law, academic applications"),
            ("Structure", "Single column, centred header, ruled sections"),
            ("Length", "One or two pages"),
            ("ATS", "Single column and plain -- parses cleanly"),
        ],
        "alternatives": ["latex-style", "academic-cv", "consulting-style"],
        "body": """
## Why this format persists

It signals that you know the convention. In sectors where the resume is a formal
document rather than a piece of design -- investment banking, corporate law, academic
job applications -- following the expected shape is itself information. It says you
have seen how this is done.

It is also genuinely readable: a single column, generous rules that separate sections
without ornament, and a serif that holds up at 10 or 11pt in print.

## The conventions that go with it

**No photo.** Not in this format, in any market.

**No colour, or almost none.** The accent applies only to the job title line. Ink is
the right preset here.

**Education can go first.** For students, recent graduates and academic applications,
education above experience is the expected order in this format. Once you have several
years of relevant work, flip it.

**Institutions and employers in full.** "Goldman Sachs & Co." not "GS". This format is
formal throughout.

**Dates right-aligned and consistent.** The ruled sections make ragged dates very
obvious.

## Filling it in

**Keep the summary short or leave it out.** This convention traditionally has no
summary at all. If you include one, three lines maximum.

**Quantify without jargon.** "Built a discounted cash-flow model covering 14
comparables for a $340m carve-out" -- specific, and readable by a generalist.

**Use the Honours section.** Awards, scholarships, dean's list, cohort rank. In these
sectors those signals are read carefully, and this format has room for them.

**Leave out hobbies** unless genuinely notable -- a national-level sport, a published
novel. "Reading and travel" is worse than nothing.

## Harvard, LaTeX or Academic CV?

All three are single-column serif layouts, and they are genuinely different documents:

- **Harvard Style** -- centred header, double rule, uppercase name. Finance,
  consulting, law, US academic job applications.
- **LaTeX Style** -- centred but lighter, Times, thin rules, no uppercase. Maths,
  physics, computer science.
- **[Academic CV](/templates/academic-cv-template/)** -- left-aligned, small caps,
  hanging indents on every entry. For a full research record with publications, and it
  runs to as many pages as needed.

Pick Harvard for job applications, Academic CV for a scholarly record.
""",
        "faq": [
            ("Is the Harvard resume format still used?",
             "Yes, particularly in investment banking, consulting, corporate law and US academic job applications, where following the expected convention is itself a signal."),
            ("Should I include a photo on a Harvard-style resume?",
             "No. This format has no photo in any market, and adding one undermines the convention it is signalling."),
            ("Does education go before experience?",
             "For students, recent graduates and academic applications, yes -- that is the expected order here. Once you have several years of relevant work, put experience first."),
            ("Is this template ATS-friendly?",
             "Yes. It is a single column with standard headings and real selectable text, which is what parsers handle most reliably."),
        ],
    },
    {
        "id": "academic-cv",
        "path": "/templates/academic-cv-template/",
        "category_path": "/academic-cv-templates/",
        "category_name": "Academic CV templates",
        "kicker": "Template guide",
        "title": "Academic CV Template With Publications | ResumeElite",
        "title_h1": "The Academic CV template",
        "description": "A free academic CV template with hanging-indent entries for publications, funding and teaching. Small-caps headings, unlimited length, instant PDF export.",
        "intro": """
A research CV, not a resume. Georgia serif, left-aligned small-caps section headings
with rules that stop at the heading, and hanging indents on every entry -- so the
first line of a citation sits out and the continuation tucks under it.
""",
        "facts": [
            ("Best for", "Postdocs, fellowships, lectureships, PhD applications"),
            ("Structure", "Single column, hanging indents, small-caps headings"),
            ("Length", "As long as the record requires"),
            ("ATS", "Single column and plain -- parses cleanly"),
        ],
        "alternatives": ["harvard-style", "latex-style", "traditional-serif"],
        "body": """
## Hanging indents, and why they matter

A publication list set as ordinary paragraphs is hard to scan: every line starts at
the same place, so your eye cannot find where one citation ends and the next begins.
With a hanging indent the first line starts at the margin and continuations tuck in,
so each entry reads as a unit.

That is the whole design decision here, and it is why this template exists separately
from Harvard Style.

## Sections to add

Use the editor's section controls -- the default set is not enough for a real CV.
Reordering is drag-and-drop.

- **Publications** -- reverse-chronological, one citation style throughout, your own
  name bolded. Split peer-reviewed articles, chapters and preprints if there are
  enough of each to warrant it.
- **Conferences** -- talks and posters separately. Mark invited talks explicitly.
- **Funding** -- grant title, funder, amount, your role, dates. Include the amounts.
- **Teaching** -- course, level, your role, enrolment.
- **Supervision** -- students, level, completion year.
- **Service** -- reviewing, committee work, editorial roles.
- **Custom section** -- for anything discipline-specific: fieldwork, languages,
  archival access, software released, datasets published.

## Citation formatting

Pick your field's style -- APA, Chicago, Vancouver, MLA -- and hold it to the
punctuation. Inconsistent citations are the fastest way to look careless to an
academic reader, and it is the thing a committee notices without trying.

**Bold your own name.** In a nine-author paper this is the difference between a reader
finding your contribution and giving up.

**Number long lists.** A committee member saying "publication 14" is a good sign, and
impossible without numbers.

**Do not inflate.** Listing a paper as "in press" when it is under review, or padding
with "manuscript in preparation", is checkable and it is the kind of thing that ends
an application.

## Length

There is no page limit on an academic CV, and trying to force one onto a real record
looks like you have less than you do. Two to four pages early on; ten or more is
normal for an established researcher.

That is not licence to pad. Every line still has to be information. "Attended the
2023 conference" is not a line.

## When you need a resume instead

If you are applying to industry -- a data science role, a research position in a
company, consulting -- send a two-page resume, not this. Industry recruiters do get
put off by a long CV for a role with a page limit, and it reads as not having
understood the audience.

**Graduate** or **Professional** are the right shapes for that, and your content
carries across when you switch.

There is more on the distinction in the
[academic collection overview](/academic-cv-templates/).
""",
        "faq": [
            ("How long should an academic CV be?",
             "As long as the record requires. Two to four pages early in a career, ten or more for an established researcher. There is no page limit, but every line still has to carry information."),
            ("How do I format a publication list on a CV?",
             "Reverse-chronological, one citation style held consistently throughout, your own name bolded so a reader can find you, and numbered if the list is long."),
            ("Should I use this template to apply for industry jobs?",
             "No. For industry, send a one or two page resume such as Professional or Graduate. A long research CV for a role with a page limit reads as misjudging the audience."),
            ("Can I add sections for funding and teaching?",
             "Yes. Sections can be added, hidden and reordered by dragging, and there is a custom section for anything discipline-specific."),
        ],
    },
    {
        "id": "europass",
        "path": "/templates/europass-cv-template/",
        "category_path": "/academic-cv-templates/",
        "category_name": "Academic CV templates",
        "kicker": "Template guide",
        "title": "Europass CV Template, Free EU Format | ResumeElite",
        "title_h1": "The Europass CV template",
        "description": "A free Europass-style CV template with labelled personal-detail rows and structured sections for EU applications. Live preview and instant PDF download.",
        "intro": """
The EU structured convention: labelled rows for personal details, clearly separated
sections, and an explicit, slightly verbose layout that makes every field findable.
Some European institutions and public bodies still ask for this format by name.
""",
        "facts": [
            ("Best for", "EU institutions, public sector, mobility schemes"),
            ("Structure", "Labelled detail rows, structured sections"),
            ("Length", "Two to three pages typically"),
            ("ATS", "Single column with explicit labels -- parses cleanly"),
        ],
        "alternatives": ["traditional-serif", "minimal-formal", "professional"],
        "body": """
## When to use it

Use Europass when it is **asked for by name**: EU institution vacancies, national
public-sector applications in several member states, Erasmus and mobility programmes,
some university administrative posts.

Do not use it as a default for private-sector applications in Europe. It is a verbose
format, and a well-formatted normal CV is usually received better by a company. That
is worth stating plainly, because a lot of advice implies Europass is the European
standard for everything. It is not.

## The fields it expects

This is where Europass differs most from a normal resume, and the editor has the
optional personal fields for all of it:

- Date of birth
- Place of birth
- Nationality
- Gender
- Civil status
- Driving licence category

Those fields are hidden by default and you switch on only the ones the application
asks for. Which ones are appropriate varies by country and by post -- include what is
requested and leave the rest off.

**A note worth being clear about:** if you are applying anywhere in the US, UK,
Canada or Australia, do not add date of birth, gender or civil status to any CV.
Employers there generally cannot consider them, and including them creates a problem
rather than solving one.

## Filling it in

**Language skills matter here more than anywhere else.** EU applications read this
section carefully. Use the Common European Framework levels -- A1 to C2 -- rather than
"fluent" or "good", and separate them if your levels genuinely differ.

**Be explicit about dates.** Month and year, consistently, including short posts.
Public-sector screening often checks continuity.

**Name institutions and qualifications in full,** with the awarding country. "Licence
en droit, Université de Strasbourg, France" rather than an abbreviation.

**Use the custom section for anything the call for applications asks for** that is not
a standard field -- security clearance, professional registration, publication list,
mobility experience.

## Length

Two to three pages is normal and expected. Europass trades brevity for completeness on
purpose, so a one-page Europass CV usually means fields were left out.

## Alternatives for Europe

If Europass is not specifically requested:

- **Minimal Formal** -- formal, tightly ruled, optional photo. Works well across
  continental Europe.
- **Traditional Serif** -- book typography for law, academia and public institutions.
- **[Professional](/templates/professional-resume-template/)** -- the standard
  two-column layout, with the photo switched on for markets where that is normal.
""",
        "faq": [
            ("Is the Europass CV format required in Europe?",
             "No. It is required only where a specific institution or programme asks for it. For private-sector applications across Europe, a well-formatted normal CV is usually received better."),
            ("Should I include my date of birth on a Europass CV?",
             "Include it when the application asks for it, which many EU public-sector calls do. Never include it for US, UK, Canadian or Australian applications, where employers generally cannot consider it."),
            ("How should I describe language levels?",
             "Use the Common European Framework levels A1 to C2 rather than words like fluent or good, and separate the levels if your reading, writing and speaking genuinely differ."),
            ("How long should a Europass CV be?",
             "Two to three pages is normal. The format trades brevity for completeness, so an unusually short one often means required fields were left out."),
        ],
    },
    {
        "id": "graduate",
        "path": "/templates/graduate-resume-template/",
        "category_path": "/academic-cv-templates/",
        "category_name": "Academic CV templates",
        "kicker": "Template guide",
        "title": "Graduate Resume Template, Free | ResumeElite",
        "title_h1": "The Graduate resume template",
        "description": "A free graduate resume template that leads with education, coursework and projects. Built for first jobs and internships. Live preview, instant PDF download.",
        "intro": """
Education-first, with a double-rule header and a serif nameplate. Built for the case
where your degree, your dissertation and your projects are genuinely the strongest
things you have -- which is most people's first two applications.
""",
        "facts": [
            ("Best for", "First jobs, internships, graduate schemes"),
            ("Structure", "Single column, education first, double-rule header"),
            ("Length", "One page"),
            ("ATS", "Single column -- parses cleanly"),
        ],
        "alternatives": ["student", "classic", "chronological"],
        "body": """
## The order

Education, then projects, then relevant coursework, then internships, then skills,
then activities, then any unrelated employment.

That last point is the one people get wrong. A summer in retail is not a headline when
you are applying to a lab or an agency, but it is not worthless either -- at the bottom
it quietly says you have held a job and turned up. Put it there, keep it to one line,
and do not give it three bullets.

## Making a thin history look substantial

You have less material than an experienced applicant. The answer is specificity, not
padding.

**Give your dissertation a result.** Not "wrote a dissertation on urban transport
policy" but "analysed 12 years of bus punctuality data across 4 UK cities; found
timetable padding accounted for 60% of reported improvement". That is a research
finding, and it reads like professional work.

**Turn coursework into projects.** A group assignment where you built something is a
project. Name it, say what it did, say what you contributed.

**Quantify anything you can.** Cohort rank, grade average if it is strong, a society
you grew from 12 to 60 members, a fundraiser total, a shift you scheduled for nine
people. Numbers are what turn "was involved in" into evidence.

**Include the near-misses.** A hackathon you did not win, a competition shortlist, a
paper accepted at a student conference. They are real.

## What to leave out

- **"References available on request."** Everyone knows. It wastes a line.
- **Secondary school results,** once you have a degree -- unless applying somewhere
  that asks specifically.
- **A skills section listing Microsoft Word.** It reads as filler.
- **An objective statement** saying you are seeking a challenging role in a dynamic
  organisation. If you use the summary, make it say something only you could write.
- **Hobbies with no relevance.** "Reading, music, socialising" is worse than the
  whitespace it replaces.

## Grades

Include your average if it is strong -- roughly 3.5 out of 4, or a UK 2:1 and above.
Leave it off otherwise; nobody will ask why it is missing.

Often better than an average: a cohort rank ("top 5% of 240"), or a specific module
grade that is relevant to the job ("Econometrics: 82%").

## One page

For a first application, one page. Not because of a rule, but because two pages of
undergraduate material means padding, and padding is visible.

The editor shows page breaks live, so you can see immediately when you have gone over
and cut rather than shrink the font.

## When to pick something else

- **Student** if you want a friendlier, more contemporary look -- rounded cards with
  colour-coded sections. Same content, warmer feel.
- **Chronological** or **ATS Friendly** for graduate-scheme portals, which are usually
  automated and high-volume.
- **[Professional](/templates/professional-resume-template/)** once you have a year or
  two of real work, at which point experience should move above education.

There is a fuller walkthrough in
[how to write a resume with no experience](/blog/resume-with-no-experience/).
""",
        "faq": [
            ("Should a graduate resume be one page?",
             "Yes. Two pages of undergraduate material almost always means padding, and padding is easy to spot. One tight page reads as better judgement."),
            ("Should I put education above experience?",
             "While your degree is your strongest asset, yes. Once you have a year or two of relevant work, move experience above it."),
            ("Do I include my GPA or grade average?",
             "Include it if it is strong -- around 3.5 out of 4 or a UK 2:1 and above. Otherwise leave it off. A cohort rank or a relevant module grade is often more persuasive."),
            ("What if I have no work experience at all?",
             "Lead with your dissertation and projects, described with real outcomes, then coursework and activities. Specificity does the work that experience normally would."),
            ("Should I list part-time retail or hospitality work?",
             "Yes, at the bottom and in one line. It shows you have held a job. Do not give it more space than your degree or your projects."),
        ],
    },
]
