# -*- coding: utf-8 -*-
"""
Guide pages for the job-specific templates (nurse, teacher, sales ...).

People search for "<job> resume template" far more than for a style name, so each
of these pages answers that search: what the role's reader looks for, which
sections to use and in what order, and what a strong line looks like. The same
shape as content.TEMPLATE_PAGES; content.py appends ROLE_PAGES to that list.
"""

PRO = ("/professional-resume-templates/", "Professional templates")
CREATIVE = ("/creative-resume-templates/", "Creative templates")
TECH = ("/tech-resume-templates/", "Developer resume templates")
ACADEMIC = ("/academic-cv-templates/", "Academic CV templates")


def _page(tid, slug, cat, title, h1, description, intro, facts, alternatives, body, faq):
    return {
        "id": tid,
        "path": "/templates/%s/" % slug,
        "category_path": cat[0],
        "category_name": cat[1],
        "kicker": "Job template",
        "title": title,
        "title_h1": h1,
        "description": description,
        "intro": intro,
        "facts": facts,
        "alternatives": alternatives,
        "body": body,
        "faq": faq,
    }


ROLE_PAGES = [
    _page(
        "nurse", "nurse-resume-template", PRO,
        "Nurse Resume Template, Free (RN, ICU, New Grad) | ResumeElite",
        "The Nurse resume template",
        "A free nursing resume template with licences and clinical skills in a side rail and experience titled the way hospitals expect. Edit online, download a PDF, no signup.",
        """
A resume for registered nurses, new graduates and specialist nurses. Your licence,
certifications and clinical skills sit in a teal rail where a nurse manager looks for
them first; the main column is titled **Clinical Experience** and leaves room for
unit, acuity and patient load.
""",
        [
            ("Best for", "RN, LPN, ICU, ER, Med-Surg, new graduates"),
            ("Structure", "Side rail for licences and skills, wide experience column"),
            ("Length", "One page; two with long specialist experience"),
            ("ATS", "Exports real text; use Simple for strict hospital portals"),
        ],
        ["simple", "modern", "professional"],
        """
## What a nurse manager checks first

Licence, then specialty, then unit. Before anyone reads a bullet they want to know
that you are licensed where the job is, that your certifications are current, and
whether you have worked a unit like theirs. The side rail puts all three in one place:
**Licenses & Certifications** sits directly under your contact details.

List each one with its issuer and, where it matters, the expiry:

```
Registered Nurse      State Board of Nursing, #RN123456
BLS / ACLS            American Heart Association, exp. 2027
PALS / TNCC           where relevant to the unit
```

## Writing clinical experience

Every entry needs the same four facts: **unit type, bed count, ratio, and acuity.**
"ICU, 32 beds, 1:2, ventilated and post-surgical patients" tells a manager more than a
paragraph of duties.

Then two to four bullets about outcomes, not tasks. Everyone on a med-surg floor
administers medication; not everyone cut falls on their unit.

> Precepted 9 new graduate nurses; all passed orientation on schedule.
>
> Led a CLABSI bundle audit that took central-line infections to zero for 14 months.

## New graduates

Put clinical placements in **Experience** with the hospital, unit and hours, and list
your NCLEX status in the rail ("NCLEX-RN passed, June 2026" or "scheduled"). Your
capstone placement is your strongest material -- describe it like a job.

## Photo or no photo

Leave it off for the US, UK, Canada and Australia; the header rebalances on its own.
Much of Europe and the Middle East still expect one.
""",
        [
            ("What should a nursing resume include?",
             "Contact details, licence number and state, current certifications such as BLS and ACLS, clinical experience with unit type, bed count and patient ratio, education, and a short list of clinical skills. A two-line summary helps if you are changing specialty."),
            ("Should a new grad nurse resume be one page?",
             "Yes. Clinical placements, your capstone, certifications and any healthcare job you held during school fit comfortably on one page."),
            ("Do I list my nursing licence number?",
             "Listing the licence type and state is standard; many applicants add the number because employers verify it anyway. Never include your Social Security number."),
            ("Is this nurse resume template ATS-friendly?",
             "It exports real, selectable text that parsers read. For a strict hospital portal you can switch to the Simple or ATS Friendly template with one click and keep all your content."),
        ],
    ),

    _page(
        "teacher", "teacher-resume-template", PRO,
        "Teacher Resume Template, Free | ResumeElite",
        "The Teacher resume template",
        "A free teacher resume template with a chalkboard header and sections for teaching experience, licensure and classroom skills. Live preview and PDF download.",
        """
For classroom teachers, teaching assistants and tutors. The header is a chalkboard
green, headings get a highlighter stroke, and the sections are renamed for schools:
**Teaching Experience**, **Certification & Licensure**, **Classroom Skills**.
""",
        [
            ("Best for", "Primary, secondary, ESL, special education, TAs"),
            ("Structure", "Full-width header, main column plus a side card"),
            ("Length", "One to two pages"),
            ("ATS", "Real text; use Simple for district portals"),
        ],
        ["simple", "graduate", "student"],
        """
## What a head teacher reads for

Three things: **what and who you have taught, whether you can run a room, and whether
your pupils improved.** The first is easy and most resumes stop there. The last one is
what gets you an interview.

## Writing teaching experience

For each school give the subject, the year groups or grades, and class sizes. Then
bullets that show results:

> Raised the Year 11 English pass rate from 61% to 79% in two years.
>
> Designed the department's Key Stage 3 reading curriculum, now used by 6 teachers.
>
> Introduced restorative behaviour routines; exclusions in my form group fell by half.

If you do not have exam data, use what you do have: reading ages, attendance,
assessment growth, clubs started, parent feedback.

## Certification and licensure

State licence or QTS, endorsements, and the date. Add safeguarding, first aid, SEN or
ESL qualifications here too -- schools filter on them.

## The teaching profile

The summary is titled **Teaching Profile**. Two or three lines on your subject, the
age range you teach best, and one thing you are known for. Avoid "passionate
educator"; every applicant is.

## Student teachers

Put each placement under Teaching Experience with the school, subject and weeks, and
lead with your strongest lesson sequence.
""",
        [
            ("How long should a teacher resume be?",
             "One page for new teachers, two pages for experienced teachers with leadership roles. Schools read the whole thing, so cut anything that does not relate to teaching."),
            ("Should I include a teaching philosophy?",
             "Not as a long statement on the resume. Put two or three concrete lines in the Teaching Profile and save the full philosophy for the cover letter or interview."),
            ("What skills should a teacher list?",
             "Curriculum design, differentiation, classroom management, assessment for learning, safeguarding and any technology you use daily, such as Google Classroom or interactive whiteboards."),
        ],
    ),

    _page(
        "sales", "sales-resume-template", PRO,
        "Sales Resume Template, Free (Account Executive, SDR) | ResumeElite",
        "The Sales resume template",
        "A free sales resume template that puts quota attainment and key wins above experience. For account executives, SDRs and sales managers. PDF download, no signup.",
        """
Sales hiring managers want one thing first: your numbers. This template gives them a
**Key Wins** block of KPI cards directly under your summary, before a single job title,
on a dark header with a small growth arrow.
""",
        [
            ("Best for", "AEs, SDRs, BDRs, account managers, sales leaders"),
            ("Structure", "Key Wins cards, then experience, single column"),
            ("Length", "One page, two for sales leadership"),
            ("ATS", "Single column, real text"),
        ],
        ["impact", "professional", "simple"],
        """
## Lead with attainment

Fill **Key Wins** (the Achievements section) with two to four numbers that would
survive a reference check:

```
142% of annual quota          2025, ranked 1 of 28 AEs
$3.4M new ARR                 41 mid-market logos
President's Club ×2           2024, 2025
```

Use the headline as the number and the description for context. A recruiter should be
able to read only the cards and know whether to call you.

## Every role needs four facts

Segment, deal size, cycle length, and quota against attainment. "Mid-market SaaS,
$40-80K ACV, 60-day cycle, 118% of a $900K quota" reads like someone who knows their
book.

Then bullets about how you got there: pipeline you built yourself, a territory you
turned around, a process you introduced.

## SDRs and new sellers

Meetings booked, conversion to opportunity, pipeline sourced in dollars, and
promotion speed. "Promoted to AE in 11 months" is a strong line on its own.

## Skills

Keep them specific: Salesforce, HubSpot, Outreach, Gong, MEDDICC, Challenger. "Strong
communicator" belongs in your interview, not your skills list.
""",
        [
            ("What should be at the top of a sales resume?",
             "Your numbers. Quota attainment, revenue closed and rankings belong above your work history, which is why this template places Key Wins directly under the summary."),
            ("How do I show sales results without exact figures?",
             "Use percentages of quota, rank among peers, growth over the previous holder of the territory, or deal counts. Relative numbers are rarely confidential."),
            ("Should I list every sales tool I have used?",
             "List the CRM and sales-engagement tools named in the job post that you have genuinely used. Five specific tools beat fifteen vague ones."),
        ],
    ),

    _page(
        "marketing", "marketing-resume-template", CREATIVE,
        "Marketing Resume Template, Free | ResumeElite",
        "The Marketing resume template",
        "A free marketing resume template with campaign cards, brand-voice headings and a skills rail. For growth, content, brand and digital marketers. PDF download.",
        """
A resume that looks like someone with taste made it, without becoming a portfolio.
Headings end in an accent full stop, your best campaigns appear as cards above your
experience, and channel skills sit in a tinted rail.
""",
        [
            ("Best for", "Growth, digital, content, brand, social, PMM"),
            ("Structure", "Right rail for skills, campaign cards first"),
            ("Length", "One page, two for heads of marketing"),
            ("ATS", "Real text; keep a Simple version for portals"),
        ],
        ["aurora", "impact", "modern"],
        """
## Campaigns before job titles

Marketing managers hire on work. Use the Projects section -- it is titled
**Campaigns** here -- for two or three pieces with a result:

> **Spring relaunch** -- Paid social, CRM. Integrated campaign that lifted trial
> sign-ups 41% in six weeks on a flat budget.

Name the channel and the budget scale if you can. A link to the live work or a case
study belongs in the project URL.

## Metrics that marketers trust

CAC, ROAS, conversion rate, pipeline sourced, organic traffic, email revenue share.
Pick the ones your role actually owned. "Increased brand awareness" is not a metric.

## Skills by channel

Group them: paid (Meta, Google, TikTok), lifecycle (Klaviyo, Braze), analytics (GA4,
Looker), content and SEO (Ahrefs, Webflow). The bars give a quick read of where your
depth is -- be honest, because you will be asked.

## Colour

The default rose suits consumer and creative brands. For B2B or fintech, switch the
accent to ink or blue; the layout stays the same.
""",
        [
            ("Should a marketing resume be creative?",
             "Considered rather than decorated. A clear hierarchy and one confident accent colour show taste; illustrations and charts usually just take space from your results."),
            ("What metrics should I put on a marketing resume?",
             "The ones you owned: customer acquisition cost, return on ad spend, conversion rate, pipeline or revenue sourced, organic traffic growth. Always pair the number with the timeframe."),
            ("Can I include a portfolio link?",
             "Yes. Add it in the website field of your contact details and on individual campaigns, and make sure the link opens without a login."),
        ],
    ),

    _page(
        "data-analyst", "data-analyst-resume-template", TECH,
        "Data Analyst Resume Template, Free | ResumeElite",
        "The Data Analyst resume template",
        "A free data analyst resume template with a dark skills rail, analytics projects before experience and room for SQL, Python and BI tools. Live preview, PDF download.",
        """
For analysts, BI developers and junior data scientists. A dark navy rail holds your
tools with skill bars; the main column leads with **Analytics Projects** so the first
thing a hiring manager reads is a problem you solved with data.
""",
        [
            ("Best for", "Data, BI, product and marketing analysts"),
            ("Structure", "Dark left rail, projects before experience"),
            ("Length", "One page"),
            ("ATS", "Real text; projects parse as normal entries"),
        ],
        ["software-engineer", "blueprint", "simple"],
        """
## The question in every analyst interview

"What decision changed because of your work?" Write your resume so it already answers
it. For each project or role: the question, the method, the decision, the value.

> **Churn prediction dashboard** -- SQL, Python, Tableau. Flagged at-risk accounts
> two months earlier; customer success saved an estimated $400K ARR in the first
> quarter.

## Tools and methods

The rail is titled **Tools & Methods**. Order by how often you use them:

```
SQL (Postgres, BigQuery)      daily
Python (pandas, scikit-learn) weekly
Tableau / Power BI / Looker   dashboards
Statistics                    A/B testing, regression
```

Skill bars are a visual cue, not a test score -- keep them honest and relative.

## Career changers

If you are moving into data, two or three solid portfolio projects using real public
datasets beat any certificate. Link the notebook or dashboard.

## What to leave out

Lists of every Python library, MOOCs completed in a weekend, and screenshots of
charts. A recruiter has seconds; spend them on outcomes.
""",
        [
            ("What skills should a data analyst resume include?",
             "SQL first, then a scripting language such as Python or R, a BI tool such as Tableau, Power BI or Looker, spreadsheet modelling and basic statistics like A/B testing. List the ones in the job description that you can use today."),
            ("Should projects come before experience?",
             "For junior analysts and career changers, yes. Once you have a few years of analyst work, experience can lead and one or two projects are enough."),
            ("Is a two-column resume OK for data jobs?",
             "For most analyst roles it is fine, because the text exports cleanly. If you apply through a strict portal, switch to Simple or ATS Friendly before exporting."),
        ],
    ),

    _page(
        "product-manager", "product-manager-resume-template", TECH,
        "Product Manager Resume Template, Free | ResumeElite",
        "The Product Manager resume template",
        "A free product manager resume template with Product Impact metric cards and a timeline of roles. For PMs, senior PMs and product owners. PDF download, no signup.",
        """
Product hiring managers read for outcomes and judgement. This template opens with
**Product Impact** cards -- two to four numbers you moved -- and then a clean
timeline of roles with a small role pill under your name.
""",
        [
            ("Best for", "PM, senior PM, product owner, group PM"),
            ("Structure", "Impact cards, timeline experience, side card"),
            ("Length", "One page, two for group PM and above"),
            ("ATS", "Real text"),
        ],
        ["impact", "notion", "modern"],
        """
## Impact cards

Use the Achievements section. Put the result in the title and the context in the
description:

```
+31% activation          rebuilt onboarding around the first key action
$2.1M new ARR            usage-based pricing, launched Q2
-40% support tickets     self-serve billing flows
```

Choose numbers you can explain in depth, because the interview will go there.

## Writing PM experience

One line of scope (product area, team size, users), then bullets in the shape
**problem, decision, result.** Show the decision -- what you chose not to build is
often more convincing than what you shipped.

> Cut the onboarding flow from 9 steps to 4 after interviews showed setup, not
> pricing, was the blocker. Activation +31% in a quarter.

## Launches

The Projects section is titled **Launches**. Use it for zero-to-one products or big
releases, with the date and adoption figure.

## Moving into product

From engineering, design or analytics: frame past work in product terms -- users,
trade-offs, metrics -- and put any product-facing project first.
""",
        [
            ("What should a product manager resume focus on?",
             "Outcomes you influenced, the decisions behind them, and the scope you owned. Feature lists without results read as project management rather than product management."),
            ("How many metrics should a PM resume have?",
             "Two to four headline numbers in the impact cards and roughly one per bullet in experience. Every number should be one you can explain in an interview."),
            ("Should I list frameworks like RICE or Jobs to Be Done?",
             "A few in the skills list is fine, but it is stronger to show them in action in a bullet than to name them."),
        ],
    ),

    _page(
        "accountant", "accountant-resume-template", PRO,
        "Accountant Resume Template, Free (CPA, ACCA) | ResumeElite",
        "The Accountant resume template",
        "A free, ATS-friendly accountant resume template with ledger-style sections, tabular dates and space for CPA, ACCA and CIMA. Edit online and download a PDF.",
        """
Conservative, exact and easy to scan -- the way finance teams like documents. Section
headings sit in shaded ledger rows, dates line up in a tabular left column, and every
entry is separated by a hairline.
""",
        [
            ("Best for", "Staff and senior accountants, auditors, controllers"),
            ("Structure", "Single column, dates in a left column"),
            ("Length", "One page, two for controllers and up"),
            ("ATS", "ATS-safe single column"),
        ],
        ["harvard-style", "simple", "consulting-style"],
        """
## What finance managers look for

Qualifications, systems, and scale. Put your designation in the job title line
("Senior Accountant, CPA") so it is the first thing read, and repeat it with the
issuer under **Certifications & Licences.**

## Give every role a scale

Revenue, number of entities, close timeline, team size:

> Own the month-end close for three entities and $90M revenue; reduced close from 8
> days to 4 by automating accruals in NetSuite.

Audit roles: client sectors, revenue range, and whether you led fieldwork.

## Systems and standards

The skills grid works well here: GAAP, IFRS, SOX, NetSuite, SAP, Oracle, Excel
(modelling, Power Query), BlackLine. List the ERP from the job posting if you have
used it -- it is usually a filter.

## Students and trainees

List exam progress precisely: "ACCA -- 9 of 13 papers passed" or "CPA -- FAR and AUD
passed, REG scheduled". Specific progress reads as momentum.
""",
        [
            ("Is this accountant resume template ATS-friendly?",
             "Yes. It is a single column with standard section names and real text, which applicant tracking systems parse reliably."),
            ("Where should I put my CPA on a resume?",
             "After your name or in your job title line, and again in the certifications section with the issuing state or body and year."),
            ("What skills should an accountant list?",
             "Accounting standards such as GAAP or IFRS, the ERP systems you have used, month-end close, reconciliations, audit, tax where relevant, and advanced Excel."),
        ],
    ),

    _page(
        "customer-service", "customer-service-resume-template", PRO,
        "Customer Service Resume Template, Free | ResumeElite",
        "The Customer Service resume template",
        "A free customer service resume template with chat-bubble headings, a service-skills rail and soft skills. For support agents, call centre and customer success roles.",
        """
Friendly without being casual. Section headings look like chat bubbles, a warm side
rail holds your **Service Skills**, **Soft Skills** and languages, and the main
column has room for the metrics support teams care about.
""",
        [
            ("Best for", "Support agents, call centre, retail, customer success"),
            ("Structure", "Left rail for skills and languages, wide main column"),
            ("Length", "One page"),
            ("ATS", "Real text; Simple for strict portals"),
        ],
        ["simple", "modern", "entry-level"],
        """
## Use the numbers your team already tracks

Customer service is one of the most measured jobs there is, so use that:

- **CSAT** or satisfaction score
- **First-contact resolution** rate
- **Average handle time** and volume per day
- **NPS** or review mentions

> Handled 60+ chats and calls a day across billing and technical queries with a 97%
> CSAT over 9,000 tickets.

## Show that you fix causes

The difference between good and great support is noticing patterns. One bullet like
"Spotted a recurring billing error and wrote the macro that cut those tickets by 30%"
is worth more than any list of duties.

## Languages

If you speak more than one, they go high in the rail with the level shown by dots.
Bilingual agents are often hired on that alone.

## Coming from retail or hospitality

Those jobs are customer service. Use the same metrics where you can -- complaints
resolved, upsell rate, mystery-shopper scores.
""",
        [
            ("What should I put on a customer service resume?",
             "Your volume and quality metrics such as CSAT, first-contact resolution and handle time, the support tools you have used, languages, and one or two examples of solving a recurring problem."),
            ("What are good soft skills for customer service?",
             "Patience, clear writing, de-escalation, empathy and ownership. Show them in a bullet with a result rather than only listing them."),
            ("Can I use this template with no experience?",
             "Yes. Put retail, hospitality or volunteer roles that involved customers in Experience and lead with your soft skills and languages."),
        ],
    ),

    _page(
        "project-manager", "project-manager-resume-template", PRO,
        "Project Manager Resume Template, Free (PMP) | ResumeElite",
        "The Project Manager resume template",
        "A free project manager resume template with a phase bar, Gantt-style date tags and room for PMP, PRINCE2 and Scrum certifications. Live preview and PDF.",
        """
A layout that thinks like a plan. A three-phase bar runs under your name, dates appear
as small Gantt-style tags above each role, and the side card puts **Core
Competencies** and certifications where they are seen first.
""",
        [
            ("Best for", "Project, programme and delivery managers"),
            ("Structure", "Main column with date tags, side card"),
            ("Length", "One to two pages"),
            ("ATS", "Real text"),
        ],
        ["consulting-style", "professional", "two-column"],
        """
## Scope first, then delivery

Each role under **Project Leadership** should open with the shape of the work:
budget, team size, number of concurrent projects, methodology.

> Run four concurrent infrastructure projects up to $8M with teams of up to 25,
> hybrid Agile and stage-gate.

Then show delivery: on time, on budget, risks caught early, a stakeholder win.

## Certifications that filter

PMP, PRINCE2, CAPM, PMI-ACP, CSM or PSM. Put them in the side card with issuer and
year. Many postings filter on PMP specifically, so spell it out as well as
abbreviating it once.

## Tools

Jira, MS Project, Smartsheet, Asana, Confluence, Power BI. Name the ones you planned
and reported in, not every tool you have logged into.

## Avoid the duty list

"Responsible for managing timelines and stakeholders" describes every project
manager. "Recovered a CRM rollout running 6 weeks late and delivered on the original
date" describes you.
""",
        [
            ("What should a project manager resume include?",
             "Project scope (budget, team size, methodology), delivery results, certifications such as PMP or PRINCE2, tools you plan and report in, and a short summary of the kind of projects you run best."),
            ("Do I need a PMP to use this template?",
             "No. Leave the certifications section out or list courses in progress; the layout rebalances automatically."),
            ("How do I show results as a project manager?",
             "On-time and on-budget delivery, schedule recovered, cost saved, risks avoided, and adoption after go-live. Use the original plan as the baseline."),
        ],
    ),

    _page(
        "ux-designer", "ux-designer-resume-template", CREATIVE,
        "UX Designer Resume Template, Free (UX/UI) | ResumeElite",
        "The UX Designer resume template",
        "A free UX/UI designer resume template with a design-tool frame header and case-study cards before experience. Edit online and download a PDF, no signup.",
        """
Your name sits inside a selected frame, the way it would on a design canvas, and your
**Case Studies** appear as cards before your experience. It signals design fluency in
one glance and then gets out of the way of the work.
""",
        [
            ("Best for", "UX, UI, product and interaction designers"),
            ("Structure", "Single column, case-study cards first"),
            ("Length", "One page plus your portfolio"),
            ("ATS", "Real text"),
        ],
        ["portfolio", "aurora", "notion"],
        """
## The resume's only job

For designers, the resume gets someone to open your portfolio. So it needs a
portfolio link in the header and two case studies good enough to make the click
obvious.

## Writing a case-study card

Use the Projects section. Title, a one-line context (tool, type), and a single
outcome:

> **Checkout redesign** -- Case study, Figma. Cut checkout drop-off 23% after five
> rounds of usability testing.

Two cards fit side by side. Add the case-study URL so it is clickable in the PDF.

## Experience

For each role: product, platform, team you worked with, and one or two outcomes.
Name research methods you actually ran -- interviews, usability tests, card sorts --
rather than a generic "user-centred design".

## Skills

Figma, prototyping, design systems, user research, accessibility (WCAG), basic
HTML/CSS. Keep it to what a hiring manager would test you on.

## Colour

The default pink suits consumer products. Pick the accent closest to your own
portfolio so the two feel like a set.
""",
        [
            ("Should a UX designer resume be designed?",
             "Yes, but lightly. It should show hierarchy, spacing and restraint. The portfolio is where the visual work lives."),
            ("How many case studies should I put on my resume?",
             "Two or three, each with a one-line outcome and a link. More than that turns the resume into a second portfolio."),
            ("Do recruiters use ATS for design roles?",
             "Many companies do, and this template exports real text that parsers can read. Keep job titles and section names standard so they are recognised."),
        ],
    ),

    _page(
        "engineering", "engineering-resume-template", TECH,
        "Engineering Resume Template, Free (Mechanical, Civil, Electrical) | ResumeElite",
        "The Engineering resume template",
        "A free engineering resume template for mechanical, civil and electrical engineers, with a technical-skills rail and engineering projects. Live preview and PDF download.",
        """
For engineers who build physical things. A bold condensed name, a safety-yellow title
label, hazard-stripe section markers and a dark rail for **Technical Skills**,
software and certifications.
""",
        [
            ("Best for", "Mechanical, civil, electrical, manufacturing engineers"),
            ("Structure", "Full-width header, dark left rail"),
            ("Length", "One to two pages"),
            ("ATS", "Real text; Simple for large-employer portals"),
        ],
        ["blueprint", "software-engineer", "two-column"],
        """
## Engineering managers read for evidence

What did you design, under what constraints, and how do we know it worked? Every entry
should answer at least two of those.

> Designed drive assemblies for a 40,000-unit production run; FEA-led redesign cut
> bracket weight 18% with no change to fatigue life.

## Technical skills rail

Group by type: CAD (SolidWorks, CATIA, AutoCAD, Revit), analysis (ANSYS, MATLAB),
manufacturing (GD&T, DFM, lean), and codes and standards relevant to your discipline
(ASME, Eurocodes, NEC).

## Licences and chartership

PE, EIT, CEng or IEng belong in your title line and in certifications. If you are
working towards chartership, say so with the expected date.

## Engineering projects

The Projects section is titled **Engineering Projects**. Use it for capstone or
competition work (Formula Student, robotics) early in your career, and for
significant designs later on.
""",
        [
            ("What should an engineering resume include?",
             "Technical skills and software, designs or projects with measurable results, licences such as PE or CEng, relevant standards, and education with any honours or capstone."),
            ("Should engineers use a one-page resume?",
             "One page for graduates and early-career engineers. Two pages is normal once you have several substantial projects to describe."),
            ("Is this template suitable for software engineers?",
             "It works, but the Software Engineer and Blueprint templates are designed around code, stack and shipped products."),
        ],
    ),

    _page(
        "legal", "legal-resume-template", PRO,
        "Lawyer Resume Template, Free (Attorney, Associate) | ResumeElite",
        "The Legal resume template",
        "A free, ATS-friendly lawyer resume template in Garamond with employer-first entries, a centred caption and sections for bar admissions. For attorneys and law students.",
        """
Law firms read resumes conservatively, so this one is quiet and exact: EB Garamond,
a centred caption, ruled section headings, and entries that lead with the firm or
court -- the convention legal recruiters expect.
""",
        [
            ("Best for", "Associates, attorneys, clerks, law students"),
            ("Structure", "Single column, employer first"),
            ("Length", "One page for students and juniors"),
            ("ATS", "ATS-safe, no photo"),
        ],
        ["harvard-style", "traditional-serif", "consulting-style"],
        """
## Conventions that matter

- **Employer first.** The firm, court or agency, then your title in italics.
- **Education near the top** for students and juniors, with journal, moot court and
  honours. The section is titled **Education & Admissions** so bar admission sits
  with your JD.
- **No photo, no colour blocks.** The accent is a muted gold used only for rules.

## Describing legal work

Say what kind of matters, your role, and the scale:

> Drafted and negotiated purchase agreements on 20+ M&A transactions from $5M to
> $400M; led due diligence teams of up to six associates.

Litigators: motions drafted, depositions taken, trials or arbitrations supported, and
outcomes where they are public.

## Bar admissions

List each jurisdiction and year: "Admitted, New York (2023); Massachusetts (2024)".
Pending admission is fine to include with the exam date.

## Law students

Summer associate roles, clerkships, clinics and journal work go in Legal Experience.
Grades and class rank go with education if they help you.
""",
        [
            ("Is a one-page resume required for law firms?",
             "For law students and junior associates, yes. Senior lawyers often use a two-page resume or a separate deal or case list."),
            ("Where do bar admissions go on a lawyer resume?",
             "Directly under education, or in their own short section. This template's Education and Admissions section is designed to hold both."),
            ("Is this lawyer resume template ATS-friendly?",
             "Yes. It is a single column with standard headings, no photo and real text."),
        ],
    ),

    _page(
        "hospitality", "hospitality-resume-template", PRO,
        "Hospitality Resume Template, Free (Hotel, Restaurant) | ResumeElite",
        "The Hospitality resume template",
        "A free hospitality resume template for hotel, restaurant and front-of-house roles, with an elegant serif header and a guest-service skills rail. PDF download.",
        """
Designed like a good hotel menu: an italic serif name, a quiet sand-coloured side rail,
and plenty of white space. It suits front office, guest relations, food and beverage,
and events.
""",
        [
            ("Best for", "Hotels, restaurants, front office, events, concierge"),
            ("Structure", "Centred header, right side rail"),
            ("Length", "One page"),
            ("ATS", "Real text"),
        ],
        ["luxe", "elegant", "customer-service"],
        """
## What hospitality managers look for

Presentation, reliability and guest outcomes. The design handles presentation; your
content needs to cover the other two.

## Guest outcomes you can quote

Review scores, mystery-shopper results, upsell revenue, repeat-guest rate, covers per
night, events delivered:

> Raised the property's review score from 8.6 to 9.3 by redesigning the arrival
> experience and training 22 front-desk staff.

## Systems

Opera, Mews, Cloudbeds, Micros, Toast, SevenRooms -- property and point-of-sale
systems are a real filter for supervisor roles.

## Languages

International hotels hire on languages. They sit in the rail with a level indicator;
keep the levels honest.

## Photo

Hospitality is one of the sectors where a professional photo is common outside the
US and UK. Use a plain background and the uniform-level smartness of the role.
""",
        [
            ("What should a hospitality resume include?",
             "Guest-facing experience with measurable results such as review scores or upsell revenue, the property and POS systems you know, languages, and any food safety or licensing certificates."),
            ("Should I add a photo to a hotel resume?",
             "In much of Europe, the Middle East and Asia a professional photo is normal. In the US, UK and Canada leave it off."),
            ("Can I use this template for restaurant jobs?",
             "Yes. It suits front-of-house, sommelier, restaurant manager and events roles equally well."),
        ],
    ),

    _page(
        "entry-level", "entry-level-resume-template", ACADEMIC,
        "Entry Level Resume Template, Free (First Job) | ResumeElite",
        "The Entry Level resume template",
        "A free entry-level resume template for a first job: education, internships and projects lead, with friendly numbered sections. Edit online, download a PDF.",
        """
For your first real job. Education, internships and projects are pulled to the top
automatically, sections are numbered with small badges, and a soft card header keeps
the page warm without looking young.
""",
        [
            ("Best for", "Graduates, school leavers, first jobs"),
            ("Structure", "Single column, education and projects first"),
            ("Length", "One page"),
            ("ATS", "Single column, real text"),
        ],
        ["graduate", "student", "simple"],
        """
## You have more material than you think

Coursework, group projects, part-time work, volunteering, societies, competitions.
The problem is usually that it is described too vaguely to count.

> Weak: Member of the marketing society.
>
> Strong: Ran social media for the 400-member marketing society; grew Instagram
> followers from 900 to 2,600 in one year.

## The order this template uses

1. **Profile** -- two lines: what you studied, what you want to do, one strength.
2. **Education** -- degree, institution, dates, relevant modules, grade if strong.
3. **Internships** and **Projects** -- described like jobs.
4. **Experience** -- part-time work, briefly.
5. **Skills** and languages.

Once you have a year of real work, switch experience above education in the
section order.

## Skills

Specific and checkable: Excel (pivot tables, VLOOKUP), Canva, Python basics, a second
language. Leave out "hard-working" and "team player".
""",
        [
            ("What do I put on a resume with no experience?",
             "Education, projects, internships, part-time jobs, volunteering and societies, each described with a concrete result. A short profile at the top explains what you are looking for."),
            ("Should an entry-level resume be one page?",
             "Yes. One tight page reads as good judgement; two thin pages read as padding."),
            ("Should I include part-time jobs?",
             "Yes, briefly. They show reliability and customer skills, but should not take more space than your education or projects."),
        ],
    ),

    _page(
        "admin-assistant", "administrative-assistant-resume-template", PRO,
        "Administrative Assistant Resume Template, Free | ResumeElite",
        "The Admin Assistant resume template",
        "A free administrative and executive assistant resume template with a folder-tab header and a checkbox skills grid. ATS-friendly, live preview, PDF download.",
        """
Organised-looking because the job is about being organised. A folder-tab header, a
checklist-style **Office & Software Skills** grid, and a single column that parses
cleanly in any portal.
""",
        [
            ("Best for", "Executive, administrative and office assistants"),
            ("Structure", "Single column, skills grid"),
            ("Length", "One page"),
            ("ATS", "ATS-safe single column"),
        ],
        ["simple", "classic", "minimal-formal"],
        """
## Who you supported, and how much

The scale of support is the headline. Who (CEO, a team of 40, three partners), what
(calendar, travel, board packs, expenses), and how complex:

> Manage calendar, international travel and quarterly board materials for the CEO;
> coordinate 30+ meetings a week across four time zones.

## Show judgement, not just tasks

Executive assistants are trusted with priorities. One line about a decision you made
or a problem you prevented sets you apart:

> Rebuilt the meeting-request process, cutting the CEO's weekly meeting load by 20%.

## The skills grid

Microsoft 365 (Outlook, Excel, PowerPoint), Google Workspace, calendar and travel
tools, expense systems (Concur, Expensify), minute-taking, CRM. The checkbox grid
reads quickly -- list ten at most.

## Typing speed and certifications

Include typing speed only if the posting asks. Certifications such as CAP or a
Microsoft Office Specialist belong in Certifications.
""",
        [
            ("What skills should an administrative assistant list?",
             "Microsoft 365 or Google Workspace, calendar and travel management, minute-taking, expense and invoicing systems, CRM use, and clear written communication."),
            ("Is this executive assistant template ATS-friendly?",
             "Yes. It is a single column with standard section names and real text."),
            ("How do I make an admin resume stand out?",
             "Quantify the support you gave and add one example of judgement, such as a process you improved or a crisis you handled."),
        ],
    ),
]
