# -*- coding: utf-8 -*-
"""
Guide pages for resume formats and styles people search for by name
("functional resume template", "federal resume template", "latex resume
template" ...). Each one answers the search: who the format is for, how to fill it
in, and when to use something else. Same shape as content.TEMPLATE_PAGES;
content.py appends FORMAT_PAGES to that list.
"""

ATS = ("/ats-resume-templates/", "ATS resume templates")
PRO = ("/professional-resume-templates/", "Professional templates")
MODERN = ("/modern-resume-templates/", "Modern CV templates")
CREATIVE = ("/creative-resume-templates/", "Creative templates")
TECH = ("/tech-resume-templates/", "Developer resume templates")
ACADEMIC = ("/academic-cv-templates/", "Academic CV templates")


def _page(tid, slug, cat, title, h1, description, intro, facts, alternatives, body, faq,
          kicker="Template guide"):
    return {
        "id": tid,
        "path": "/templates/%s/" % slug,
        "category_path": cat[0],
        "category_name": cat[1],
        "kicker": kicker,
        "title": title,
        "title_h1": h1,
        "description": description,
        "intro": intro,
        "facts": facts,
        "alternatives": alternatives,
        "body": body,
        "faq": faq,
    }


FORMAT_PAGES = [
    # ------------------------------------------------------------------ simple
    _page(
        "simple", "simple-resume-template", ATS,
        "Simple Resume Template, Free and ATS-Friendly | ResumeElite",
        "The Simple resume template",
        "A free simple resume template: centred name, hairline rules and one column that any applicant tracking system reads. Edit online and download a PDF, no signup.",
        """
A resume with nothing in it that is not information. Your name is centred, sections
are separated by a hairline rule, and everything runs in one column from top to
bottom. No photo, no icons, no sidebar.
""",
        [
            ("Best for", "Any job, any industry, online application portals"),
            ("Structure", "One column, centred header, ruled sections"),
            ("Length", "One page for most people; two for long careers"),
            ("ATS", "Safest choice: single text flow, standard headings"),
        ],
        ["minimal", "ats-friendly", "classic"],
        """
## Why simple works

A recruiter spends seconds on the first pass. On a simple layout their eye goes
straight down the page: name, title, summary, the most recent job. Nothing competes
for attention, so your content does all the work.

It is also the layout that survives every system it passes through. Applicant
tracking systems, the "upload your resume" box on LinkedIn, a PDF opened on a phone,
a page printed in black and white: one column of text in reading order comes through
all of them unchanged.

## What to put in it

In this order, which is the order a recruiter reads in:

1. **Header**: name, the job title you want, email, phone, city, LinkedIn.
2. **Professional summary**: two or three lines. What you do, for how long, and one
   result you are proud of.
3. **Work experience**: most recent first. Title, employer, city, dates, then two to
   five bullets that start with a verb and end with a result.
4. **Education**: degree, school, year. Move it above experience only if you
   graduated in the last two years.
5. **Skills**: the ones the job posting asks for, in the posting's own words.

Languages, certifications and projects go at the end if they help this application.

## When to choose something else

Simple is never the wrong answer, but it can be a missed chance. If you are a
designer, a portfolio-led layout says more about you; if you are changing careers,
a skills-first layout hides less well-matched job titles. You can switch at any time
and your content moves with you.
""",
        [
            ("What is the best simple resume template?",
             "One with a single column, standard section headings (Experience, Education, Skills) and no text inside images or tables. This template follows all three, which is why it reads correctly in applicant tracking systems."),
            ("Is a simple resume better than a creative one?",
             "For most jobs, yes: it is faster to scan and parses reliably. A creative layout helps mainly in design, marketing and other roles where the resume itself shows your taste."),
            ("Should a simple resume have a photo?",
             "Not in the US, UK, Canada or Australia. This template has no photo slot; if you apply in a country that expects one, Classic and Professional have a photo header."),
            ("Can I download this simple resume template as a PDF?",
             "Yes. Fill it in online and download a PDF with real, selectable text. It is free, with no account and no watermark."),
        ],
    ),

    # -------------------------------------------------------------- functional
    _page(
        "functional", "functional-resume-template", ATS,
        "Functional Resume Template for Career Changers | ResumeElite",
        "The Functional resume template",
        "A free functional (skills-based) resume template for career changers and employment gaps: core competencies first, employment history below. Edit online, PDF download.",
        """
A skills-first resume. **Core Competencies** sit at the top of the page in a
two-column checklist, followed by your strengths and achievements; **Employment
History** comes after, kept short. Built for people whose job titles do not tell the
story on their own.
""",
        [
            ("Best for", "Career changers, gaps in employment, returners, freelancers"),
            ("Structure", "Competencies and achievements first, jobs below"),
            ("Length", "One page"),
            ("ATS", "Single column with standard headings; still list every job"),
        ],
        ["chronological", "simple", "entry-level"],
        """
## Who a functional resume is for

A reverse-chronological resume makes your latest job title the headline. That is a
problem when the title is the wrong one: a teacher applying for instructional design,
a parent returning after five years, a soldier moving into logistics management. A
functional resume puts what you can do first and lets the job history support it.

## How to fill it in

**Core Competencies.** Six to nine skills, taken from the job posting you are
applying to. "Stakeholder communication" beats "good communicator".

**Achievements.** This is the section that makes a functional resume credible. Group
two or three results under each competency, wherever you earned them:

> Training design: built a 6-week onboarding course for 40 new staff; time to full
> productivity fell from 10 weeks to 7.
>
> Budgeting: managed a $120,000 department budget and closed two years under plan.

**Employment History.** Every job, with employer, title and dates. Keep each one to
a line or two. Leaving jobs out is what gave functional resumes a bad name; recruiters
read missing dates as something to hide.

## The honest trade-off

Many recruiters prefer chronological resumes because they can see what you did when.
A functional resume is the right tool when chronology works against you, not a
default. A useful middle ground: keep this layout but write two good bullets under
each recent job, so the history carries weight too.
""",
        [
            ("What is a functional resume?",
             "A resume organised around skills and achievements instead of job-by-job history. The skills come first; employment history follows in a short list."),
            ("Are functional resumes ATS-friendly?",
             "The layout is: this template is one column with standard headings. The risk is content, not format. Always include employers, titles and dates, because many systems and recruiters look for them."),
            ("When should I use a functional resume?",
             "When you are changing careers, returning after a gap, or have many short or unrelated jobs. If your recent titles match the job you want, a chronological resume is stronger."),
            ("Can I explain an employment gap on a functional resume?",
             "Yes. Add the period to Employment History with a short honest label, such as 'Career break: full-time carer' or 'Relocation and retraining', and list any course you took in that time."),
        ],
    ),

    # ----------------------------------------------------------- chronological
    _page(
        "chronological", "chronological-resume-template", ATS,
        "Chronological Resume Template, Free | ResumeElite",
        "The Chronological resume template",
        "A free reverse-chronological resume template with dates in a left column and a timeline connector on every entry. The format recruiters prefer. Edit online, download PDF.",
        """
The format most recruiters expect: your most recent job first, then back in time.
Dates sit in their own left column and a dotted connector joins each entry, so
progression is visible before anyone reads a word.
""",
        [
            ("Best for", "Steady career progression in one field"),
            ("Structure", "Single column, date column on the left, timeline dots"),
            ("Length", "One page; two after about ten years"),
            ("ATS", "Real text in reading order; standard headings"),
        ],
        ["simple", "functional", "professional"],
        """
## Why recruiters like chronological resumes

They answer the recruiter's first three questions immediately: what are you doing
now, how long have you done it, and is your career moving upward. The left-hand date
column in this template makes the third one visible at a glance: promotions read as
a staircase.

## Writing each entry

Title, employer, city and dates on the first lines. Then two to five bullets, most
impressive first:

> Promoted from analyst to senior analyst in 18 months, ahead of the usual three years.
>
> Rebuilt the monthly reporting pack; preparation time fell from four days to one.

Give recent jobs more bullets than older ones. Anything more than ten to fifteen years
back can shrink to a single line, or go.

## Dates

Use month and year ("Mar 2021 - Present") for recent roles. Years alone are fine for
jobs over five years ago. If you held two roles at one employer, list the employer
once and both titles under it with their own dates; it shows the promotion.

## When chronological is not the right choice

If your last few titles do not match the job you want, or there is a long gap at the
top of the page, look at the Functional template. If you have no work history yet,
Entry Level and Student put education first.
""",
        [
            ("What is a reverse-chronological resume?",
             "A resume that lists your work experience starting with the current or most recent job and moving backwards. It is the most common format and the one most recruiters prefer."),
            ("Is a chronological resume ATS-friendly?",
             "Yes. This template is one column with real text, standard headings and dates in a consistent format, which is what applicant tracking systems read best."),
            ("How far back should a chronological resume go?",
             "Usually ten to fifteen years. Older roles can be cut or summarised in one line unless they are directly relevant to the job."),
            ("Should education go before experience?",
             "Only if you graduated within the last two years or the job asks for a specific degree. Otherwise experience goes first."),
        ],
    ),

    # ---------------------------------------------------------------- federal
    _page(
        "federal-style", "federal-resume-template", ATS,
        "Federal Resume Template (USAJOBS), Free | ResumeElite",
        "The Federal resume template",
        "A free federal resume template for USAJOBS and government jobs: labelled personal details, boxed sections and room for the details federal HR checks. Edit online, PDF.",
        """
A government-style resume: no photo, a boxed block of labelled personal details under
your name, and clearly separated sections with heavy headings. It is designed for the
extra detail federal and public-sector applications ask for.
""",
        [
            ("Best for", "US federal jobs (USAJOBS), state and public-sector roles"),
            ("Structure", "Labelled contact block, single column, boxed headings"),
            ("Length", "Two pages maximum on USAJOBS since September 2025"),
            ("ATS", "Plain text in one column, no graphics, no photo"),
        ],
        ["ats-friendly", "simple", "chronological"],
        """
## How a federal resume differs

Federal HR specialists check your resume against the qualifications in the job
announcement, line by line. If a requirement is not visibly on the page, it does not
count, however obvious it is from your job title. So a federal resume is more explicit
than a private-sector one.

For each job, include:

```
Job title, series and grade (if federal)    e.g. Program Analyst, GS-0343-11
Employer and city, state
Start and end dates                         month and year
Hours per week                              e.g. 40
```

Then describe the duties and results that match the announcement's **specialized
experience** paragraph, using its wording where it is true for you.

## Length

Federal resumes used to run four or five pages. Since September 2025, under OPM's
Merit Hiring Plan, USAJOBS only accepts resumes of two pages or less, so the detail has to be precise
rather than long. Always check the "How to apply" section of the announcement you are
applying to, as requirements vary.

## What to leave out

No photo, no date of birth, no Social Security number. Salary history is not needed
for most announcements. Keep references off the resume unless asked.

## State and local government

The same habits help: match the posting's language, give dates and hours, and make
every required qualification easy to find.
""",
        [
            ("What is a federal resume?",
             "A resume for US government jobs. It includes more detail than a private-sector resume, such as hours per week and month-and-year dates for each job, so HR can confirm you meet the announcement's qualifications."),
            ("How long can a federal resume be?",
             "Two pages. Since September 2025, USAJOBS accepts only resumes of two pages or less for federal job announcements. Check each announcement's 'How to apply' section for anything else it requires."),
            ("Can I use this template for USAJOBS?",
             "Yes. Download it as a PDF and upload it to your USAJOBS profile. The text is real and selectable, which the system needs."),
            ("Do I need to include hours per week?",
             "Yes, for each job. It is how HR calculates whether you have the required length of specialized experience, and missing hours can make an application ineligible."),
        ],
    ),

    # ------------------------------------------------------------------ latex
    _page(
        "latex-style", "latex-resume-template", ACADEMIC,
        "LaTeX Resume Template Look, No Code Needed | ResumeElite",
        "The LaTeX Style resume template",
        "The classic LaTeX resume look, without writing LaTeX: Times-style serif, dates in the margin and ruled section headings. Edit in your browser and download a PDF free.",
        """
The look of a resume written in LaTeX, with none of the setup. A Times-style serif,
dates hung in the left margin and quiet ruled headings, the style familiar from
computer science departments and academic CVs. You type into a form; there is no
code, no compiler and no Overleaf project.
""",
        [
            ("Best for", "Computer science, engineering, research, quant and academia"),
            ("Structure", "Single column, dates in the margin, serif type"),
            ("Length", "One page for industry; longer for academic CVs"),
            ("ATS", "Real text in one column; no photo"),
        ],
        ["harvard-style", "academic-cv", "software-engineer"],
        """
## Why people want the LaTeX look

In technical fields the LaTeX resume has become a signal of its own: clean
typography, dense but readable, no decoration. Hiring managers in software,
research and finance see hundreds of them and read them quickly.

Getting that look usually means learning a document class, fixing compile errors and
fighting with spacing. This template gives you the same typographic result in a
regular editor, with a live preview.

## Filling it in for a technical role

**Education first** if you are a student or recent graduate: university, degree,
expected graduation, GPA if it is strong, and relevant coursework.

**Experience and projects** with one-line bullets that lead with a verb and include
a number or a technology:

> Cut p95 API latency from 480 ms to 120 ms by adding a Redis read-through cache.
>
> Built a CUDA kernel for sparse attention; 3.1x faster than the PyTorch baseline.

**Skills** as plain lists: languages, frameworks, tools. Skip rating bars; they mean
nothing to the reader.

## For academic CVs

Add Publications, Teaching, Grants and Conferences as sections. The margin date
column keeps a long list of entries easy to scan. For a full research CV, the Academic
CV template has hanging-indent publication entries.
""",
        [
            ("Do I need to know LaTeX to use this template?",
             "No. You fill in a form in your browser and download a PDF. The template reproduces the typographic style of a LaTeX resume without any code."),
            ("Is a LaTeX-style resume ATS-friendly?",
             "This one is: it exports real text in a single column with standard headings. Some LaTeX-compiled PDFs break ligatures or column order; this export does not rely on LaTeX."),
            ("Is this like Jake's resume or the Overleaf templates?",
             "It is in the same tradition: a serif, single-column, information-dense layout. It is an original template, edited in a browser instead of in Overleaf."),
            ("Can I use it for a PhD or faculty application?",
             "Yes, for a short CV. For a long research CV with many publications, the Academic CV template is better suited."),
        ],
    ),

    # ---------------------------------------------------------------- student
    _page(
        "student", "student-resume-template", ACADEMIC,
        "Student Resume Template, Free (High School and College) | ResumeElite",
        "The Student resume template",
        "A free student resume template for high school and college students: education, courses and projects first, in friendly colour-coded cards. Edit online, download a PDF.",
        """
For students applying to part-time jobs, internships, scholarships and first
graduate roles. **Education**, **Courses** and **Projects** come first in rounded,
colour-coded cards, so the page is full of real material before work experience
even starts.
""",
        [
            ("Best for", "High school, college and university students"),
            ("Structure", "Gradient header, education and projects first, card sections"),
            ("Length", "One page"),
            ("ATS", "Real text; use Simple for large corporate portals"),
        ],
        ["entry-level", "graduate", "simple"],
        """
## What to put on a student resume

You have more than you think. Anything that shows you can show up, learn and finish
things counts:

- **Education**: school, programme, expected graduation, grades if they help.
- **Courses**: three to six that relate to the job.
- **Projects**: class projects, a science fair, a website, a club event you ran.
- **Experience**: part-time jobs, babysitting, tutoring, volunteering, internships.
- **Skills and languages**: software you use, languages you speak.

## Make every line specific

The difference between a weak and a strong student resume is detail:

> Weak: Member of the debate club.
>
> Strong: Captain of the debate team; led 12 members to the regional semi-final.

> Weak: Worked at a café.
>
> Strong: Served 150+ customers a shift at a busy café; trusted to open and close the
> store alone after three months.

## High school vs college

**High school students** can include GPA, honours, school clubs, sports and
volunteering. **College students** should drop high school once they have a semester
or two of university, and lead with major, relevant courses and internships.

## Keep it to one page

One page is the rule for students. If it does not fit, cut older or less relevant
items before you shrink the font.
""",
        [
            ("How do I write a resume as a student with no experience?",
             "Lead with education, relevant courses and projects, then add part-time work, volunteering, clubs and responsibilities. Describe each with a specific detail or number."),
            ("Should a high school student put GPA on a resume?",
             "If it is 3.5 or higher (or the equivalent in your system), yes. Otherwise leave it off and let projects and activities speak."),
            ("How long should a student resume be?",
             "One page. Recruiters expect it, and it forces you to keep only your strongest material."),
            ("Is this student resume template free?",
             "Yes. Fill it in online, preview it as you type and download a PDF, with no signup and no watermark."),
        ],
    ),

    # -------------------------------------------------------------- executive
    _page(
        "executive", "executive-resume-template", PRO,
        "Executive Resume Template for Senior Leaders | ResumeElite",
        "The Executive resume template",
        "A free executive resume template for directors, VPs and C-suite: serif nameplate, a two-column body and room for scope, P&L and board-level results. Edit online, PDF.",
        """
For directors, vice presidents and C-suite candidates. A centred serif nameplate
sets a formal tone; the main column carries your leadership experience, and a narrow
side column holds expertise, languages and board or certification credentials.
""",
        [
            ("Best for", "Director, VP, C-suite, general manager, partner"),
            ("Structure", "Serif nameplate, wide main column, narrow side column"),
            ("Length", "Two pages is normal at this level"),
            ("ATS", "Real text; use Simple for strict portals"),
        ],
        ["modern-executive", "elite", "professional"],
        """
## What an executive resume has to prove

At senior level the question is no longer "can you do the job" but "what will be
different after you arrive". Every entry should show **scope** and **outcome**.

Scope, on the first line under each title:

```
VP Operations, Northwind Logistics                     2019 - Present
Led 1,200 staff across 9 sites; P&L $340M; reported to the CEO.
```

Then three or four outcomes, with the numbers a board would care about:

> Turned a $12M operating loss into a $9M profit in two years.
>
> Led the integration of two acquisitions; retained 94% of key staff.

## The executive summary

Three or four lines at the top that position you: your function, the size of
organisations you have led, and the kind of problem you are known for solving
(turnarounds, scale-ups, international expansion). Avoid adjectives such as
"visionary" or "results-driven" and let the numbers say it.

## Two pages is fine

Recruiters expect two pages from senior candidates. Keep the last fifteen years in
detail and summarise earlier roles in a short "Earlier career" line.

## Board roles and education

Board seats, advisory roles and executive education (an MBA or an executive
programme) go in the side column, where they are visible without taking space from
your results.
""",
        [
            ("How long should an executive resume be?",
             "Two pages is standard. One page can work for a focused application, but cutting results to fit one page is usually a mistake at this level."),
            ("What should an executive summary include?",
             "Your function, the size of teams and budgets you have led, your industries, and the kind of challenge you are known for. Three or four lines, no generic adjectives."),
            ("Should an executive resume include a photo?",
             "Not for the US, UK or Canada. This template shows a photo only if you add one, and the header rebalances without it."),
            ("Is this template suitable for C-suite roles?",
             "Yes. For an even more premium look, the Elite and Modern Executive templates are designed for senior leadership too, and your content carries across when you switch."),
        ],
    ),

    # ---------------------------------------------------------------- minimal
    _page(
        "minimal", "minimalist-resume-template", ATS,
        "Minimalist Resume Template, Free | ResumeElite",
        "The Minimal resume template",
        "A free minimalist resume template: light type, generous whitespace, section labels in the margin and no decoration at all. ATS-friendly. Edit online, download a PDF.",
        """
A type-only resume. A light, wide-set name, section labels in small capitals in the
left margin, and plenty of white space. There are no lines, colours or icons, so it
looks considered rather than plain.
""",
        [
            ("Best for", "Design-aware roles, consulting, tech, anyone who wants calm"),
            ("Structure", "Labels in the margin, content in a wide column"),
            ("Length", "One page"),
            ("ATS", "Parses cleanly: real text, no graphics"),
        ],
        ["simple", "zen", "elegant"],
        """
## Minimal is not the same as empty

A minimalist resume removes decoration, not information. The space it saves goes to
white space, which makes every line easier to read. It works best when your content
is already strong: clear titles, specific results, short bullets.

## Make the content as clean as the layout

- **One idea per bullet.** If a bullet needs "and" twice, split it.
- **Consistent dates.** Same format everywhere, aligned to the right.
- **Short summary.** Two lines at most.
- **Fewer, better skills.** Six relevant skills look stronger than twenty.

## Why the labels sit in the margin

Putting the section names in a left column creates a clean vertical line the eye can
follow down the page, so the reader finds Experience or Education without hunting.
The content column stays wide enough for full-length bullets.

## Minimal vs Simple

Both are ATS-safe single-flow layouts. Simple has a centred name and ruled headings
and feels conventional; Minimal has margin labels and light type and feels more
designed. Try both in the editor; your content stays when you switch.
""",
        [
            ("What is a minimalist resume?",
             "A resume that uses typography and white space instead of colour, icons or graphics to organise information. It keeps all the content of a standard resume."),
            ("Are minimalist resumes ATS-friendly?",
             "Usually more than any other style, because there are no graphics or text boxes. This template exports real text in reading order."),
            ("Is a minimalist resume too plain?",
             "Not if the content is strong. The layout makes specific results easier to see; it only looks plain when the bullets are vague."),
            ("Can I add a photo to the minimalist template?",
             "This template has no photo slot, by design. If you need a photo, Minimal Formal keeps the same restraint with an optional photo."),
        ],
    ),

    # ------------------------------------------------------------- two column
    _page(
        "two-column", "two-column-resume-template", MODERN,
        "Two Column Resume Template, Free | ResumeElite",
        "The Two Column resume template",
        "A free two-column resume template: experience in a wide main column, skills, languages and certifications in a side column. Fits more on one page. Edit online, PDF.",
        """
The classic two-column resume done properly. A bold nameplate with an optional
photo, then experience, education and projects in a wide main column, with skills,
language levels and certifications in a narrower column beside them.
""",
        [
            ("Best for", "Mid-career professionals with lots of skills to show"),
            ("Structure", "Wide main column plus a side column"),
            ("Length", "One page, which is the point of two columns"),
            ("ATS", "Real text; for strict portals pick a one-column template"),
        ],
        ["modern", "professional", "simple"],
        """
## Why use two columns

Short items such as skills, languages, tools and certifications waste space in a
single column, each taking a full line. A side column stacks them neatly, which
usually saves a third of a page and lets a strong career fit on one page.

## What goes where

**Main column**: things a recruiter reads in full, such as summary, work experience,
education and projects.

**Side column**: things a recruiter scans, such as skills, languages with their
level, certifications and short lists like tools or interests.

## Two columns and applicant tracking systems

Modern parsers handle two-column PDFs far better than they used to, and this
template exports real, selectable text. Some older systems still read across both
columns line by line. If you are applying through a large corporate portal and want
no risk at all, switch to Simple or ATS Friendly before downloading. Your content
moves with you, so it takes one click.

## Keep the side column short

If the side column runs longer than the main column, move something such as
certifications into the main column, or cut skills down to the ones in the job
posting.
""",
        [
            ("Is a two-column resume ATS-friendly?",
             "Most current applicant tracking systems read it correctly, and this template exports real text. For older or very strict systems, a one-column layout is the safest choice."),
            ("What goes in the side column of a resume?",
             "Short, scannable items: skills, languages, certifications, tools and contact details. Experience and education belong in the main column."),
            ("Are two-column resumes professional?",
             "Yes. They are common in corporate, tech and marketing roles and let you fit more relevant information on one page."),
            ("Can I remove the photo from the two-column template?",
             "Yes. Leave the photo empty and the header adjusts automatically."),
        ],
    ),

    # ---------------------------------------------------------------- compact
    _page(
        "compact", "one-page-resume-template", ATS,
        "One Page Resume Template, Free and Compact | ResumeElite",
        "The Compact one-page resume template",
        "A free one-page resume template built to fit a long career on a single sheet: tight spacing, small type that stays readable, one column. Edit online, download a PDF.",
        """
A high-density layout for people who need to fit a lot onto one page. Tighter
spacing, a compact header and inline skills and languages, while keeping the type
large enough to read comfortably and the structure ATS-friendly.
""",
        [
            ("Best for", "Applications that require one page; long careers"),
            ("Structure", "Single column, compact header, inline lists"),
            ("Length", "One page, by design"),
            ("ATS", "Single text flow with standard headings"),
        ],
        ["simple", "minimal", "chronological"],
        """
## When one page is required

Many employers and programmes ask for a one-page resume: consulting firms, banks,
graduate schemes, career fairs and most roles in the US for candidates with under
ten years of experience. A compact layout gives you room without resorting to
8-point type.

## How to fit more without cramming

The layout saves space; your editing should too.

1. **Cut old roles to one line.** Title, employer, years. No bullets.
2. **Two to four bullets per job,** most recent jobs getting the most.
3. **One line per bullet** where possible. If a bullet wraps by two words, rewrite it.
4. **Inline lists.** Skills and languages on a single line each, not as columns.
5. **Drop what everyone assumes:** "References available on request", a full street
   address, and objective statements.

## How to know if it fits

The editor shows page breaks live. If your content spills to a second page, the
preview shows it immediately; cut until it fits. If it still spills after honest
editing, two pages are fine for most experienced candidates, and the Professional or
Chronological templates use the space well.
""",
        [
            ("How do I fit my resume on one page?",
             "Cut roles older than ten to fifteen years to one line, keep two to four bullets per job, write one-line bullets, and put skills and languages on a single line. A compact layout like this one helps."),
            ("Should my resume be one page?",
             "Yes if you have under about ten years of experience or the employer asks for it. Senior candidates can usually use two pages."),
            ("Will the compact template make my text too small?",
             "No. It saves space through tighter spacing and inline lists, not tiny type, so it stays readable when printed."),
            ("Is the one-page resume template ATS-friendly?",
             "Yes. It is a single column with standard headings and real, selectable text in the PDF."),
        ],
    ),

    # ------------------------------------------------------------- consulting
    _page(
        "consulting-style", "consulting-resume-template", PRO,
        "Consulting Resume Template (MBB Style), Free | ResumeElite",
        "The Consulting resume template",
        "A free consulting resume template in the dense one-page style McKinsey, BCG and Bain recruiters expect: employer first, results in every bullet. Edit online, PDF.",
        """
The high-density format used in management consulting and banking recruiting. One
page, a serif name over a burgundy rule, employers listed first with your title in
italics beneath, and dates right-aligned so the page reads as a tidy grid.
""",
        [
            ("Best for", "Management consulting, strategy, investment banking, MBA"),
            ("Structure", "Single column, employer-first entries, right-aligned dates"),
            ("Length", "One page, strictly"),
            ("ATS", "Real text in one column; no photo"),
        ],
        ["harvard-style", "compact", "simple"],
        """
## What consulting recruiters screen for

Firms screen hundreds of resumes per role, against the same few signals:
**academic strength, quantified impact, leadership,** and what consultants call a
"spike", one thing you are clearly exceptional at. The format puts these where a
screener looks: education at the top for students, employers in bold, and results in
every bullet.

## Bullets that pass a consulting screen

Each bullet is a small case: what you did, how, and the measurable result.

> Built a pricing model across 2,400 SKUs that raised gross margin 3.2 points in
> two quarters.
>
> Led a team of 4 analysts on a cost diagnostic; client adopted 11 of 14
> recommendations, saving $18M a year.

Avoid "responsible for" and "assisted with". If you cannot put a number on it, show
scale instead: team size, budget, number of markets or users.

## Order of sections

For students and MBA candidates, **Education** comes first, with test scores or
honours if they are strong. Experienced hires put **Experience** first. End with a
short **Additional** line: languages, technical skills and two or three genuine
interests. Interviewers do ask about them.

## One page

Consulting and banking applications expect one page. No exceptions until you are
very senior.
""",
        [
            ("What format do McKinsey, BCG and Bain expect?",
             "A one-page, single-column resume with education, experience and an additional section, where every bullet shows a quantified result. This template follows that convention."),
            ("Should a consulting resume have a summary?",
             "Usually not for students and MBA candidates; the space is better used for results. Experienced hires can add a two-line summary."),
            ("Should I include GMAT or GPA on a consulting resume?",
             "If they are strong, yes, on the education line. Consulting screens weigh academic performance heavily, especially for graduate hires."),
            ("Can I use this template for investment banking?",
             "Yes. Banking resumes use the same dense, one-page, employer-first format."),
        ],
    ),

    # ------------------------------------------------------------ qa engineer
    _page(
        "qa-engineer", "qa-engineer-resume-template", TECH,
        "QA Engineer Resume Template (Tester, SDET), Free | ResumeElite",
        "The QA Engineer resume template",
        "A free QA engineer resume template for manual testers, automation engineers and SDETs: test tooling, frameworks and certifications in a side card. Edit online, PDF.",
        """
For manual testers, QA analysts, automation engineers and SDETs. A checklist style
runs through the headings, test tools and frameworks sit in a side card, and each role
has room for what you tested, how, and what quality improved.
""",
        [
            ("Best for", "QA analyst, test automation engineer, SDET, QA lead"),
            ("Structure", "Main column plus a side card for tools and certifications"),
            ("Length", "One page; two for leads with long histories"),
            ("ATS", "Real text; use Simple for strict portals"),
        ],
        ["software-engineer", "tech", "simple"],
        """
## What hiring managers look for in a QA resume

Three things: **what you tested** (web, mobile, APIs, embedded, data pipelines),
**how** (manual, automated, performance, security) and **what changed** because of
it. Most QA resumes stop at a list of tools. The result is what gets the interview.

## Writing QA experience

Name the product, the stack and the testing scope, then results:

> Built a Playwright suite of 640 end-to-end tests running in CI on every pull
> request; escaped defects fell 45% in two quarters.
>
> Cut regression time from 3 days of manual testing to 40 minutes by automating
> the top 200 test cases.
>
> Introduced contract tests for 14 microservices with Pact; broke the release-day
> outage cycle.

## Tools and skills in the side card

Group them so a scan finds them fast:

```
Automation    Playwright, Cypress, Selenium, Appium
Languages     TypeScript, Python, Java
API / perf    Postman, REST Assured, k6, JMeter
CI / tools    GitHub Actions, Jenkins, Jira, TestRail
```

Certifications such as ISTQB go just below.

## Manual testers moving into automation

List automation work even if it was a side project or a small part of your job, and
add a Projects entry linking to a public test repository. It is the strongest evidence
you can offer.
""",
        [
            ("What should a QA engineer resume include?",
             "The products and platforms you tested, the types of testing, your automation tools and languages, CI experience, certifications such as ISTQB, and measurable results like fewer escaped defects or shorter regression cycles."),
            ("How do I show automation skills on a QA resume?",
             "Name the framework, the size of the suite, where it runs (CI) and its impact. Link a public repository in Projects if you have one."),
            ("Is ISTQB worth putting on a resume?",
             "Yes, especially for QA analyst roles and in Europe, where many postings list it. Put it in the certifications section with the level."),
            ("Is this QA resume template ATS-friendly?",
             "It exports real, selectable text. For very strict portals you can switch to Simple with one click and keep all your content."),
        ],
    ),

    # ------------------------------------------------------------- freelancer
    _page(
        "freelancer", "freelance-resume-template", CREATIVE,
        "Freelance Resume Template, Free | ResumeElite",
        "The Freelancer resume template",
        "A free freelance resume template: an 'Available for projects' tag, selected work before job history, and a side rail listing your services. Edit online, PDF.",
        """
For independent contractors, consultants and freelancers. An **Available for
projects** tag sits above your name, **Selected Work** comes before job history, and a
warm side rail lists your services, contact details and languages, so a client sees
what you offer before anything else.
""",
        [
            ("Best for", "Freelancers, contractors, consultants, agency-side specialists"),
            ("Structure", "Selected work first, services rail on the right"),
            ("Length", "One page"),
            ("ATS", "Real text; clients rarely use ATS, agencies sometimes do"),
        ],
        ["portfolio", "functional", "professional"],
        """
## A freelance resume sells a service

An employer asks "can this person do the job?". A client asks "can this person solve
my problem, and have they done it before?". The layout is built for the second
question: work first, then the services you offer, then your history.

## Selected Work

Three to five projects, each with the client (or "a fintech start-up" if under NDA),
what you delivered and the result:

> Redesigned onboarding for a meal-kit app; trial-to-paid conversion rose from 9%
> to 14%.
>
> Wrote and produced 12 product videos for a B2B SaaS launch; 220k views in the first
> month.

## Services

List what clients can hire you for, in their language: "Brand identity", "Shopify
store builds", "Technical SEO audits". Avoid internal jargon.

## How to list freelance work as experience

Treat your freelance practice as one job:

```
Freelance Product Designer                         2021 - Present
Clients include a fintech start-up, a national retailer and two agencies.
```

That avoids a page of short contracts, and recruiters read it as continuous
employment, which it is.
""",
        [
            ("How do I list freelance work on a resume?",
             "As one continuous entry, such as 'Freelance Product Designer, 2021 - Present', with your strongest client projects as bullets. List major clients by name or by description if under NDA."),
            ("Should a freelancer have a resume or a portfolio?",
             "Both. The portfolio shows the work; the resume gives the summary that agencies, larger clients and job applications ask for. Link the portfolio in your header."),
            ("What does 'Available for projects' mean on the template?",
             "It is an optional tag that tells clients you are taking new work. You can change the text or remove it."),
            ("Can I use the freelance template for a full-time job application?",
             "Yes. Selected Work and Services read well to employers, too. For a conventional corporate application, the Professional template may be a better fit."),
        ],
    ),

    # -------------------------------------------------------------- portfolio
    _page(
        "portfolio", "graphic-designer-resume-template", CREATIVE,
        "Graphic Designer Resume Template, Free | ResumeElite",
        "The Portfolio resume template for graphic designers",
        "A free graphic designer resume template: a deep navy sidebar with your photo, projects before experience and editorial serif headings. Edit online, download a PDF.",
        """
A resume for graphic designers, illustrators, art directors and other portfolio-led
creatives. A deep navy sidebar carries your photo, contact details, tools and
languages; the main column opens with **Projects**, in italic serif headings, before
work experience.
""",
        [
            ("Best for", "Graphic, brand and visual designers, illustrators, art directors"),
            ("Structure", "Dark left sidebar, projects-first main column"),
            ("Length", "One page; the portfolio does the rest"),
            ("ATS", "Real text; agencies rarely screen by ATS"),
        ],
        ["ux-designer", "creative", "freelancer"],
        """
## Your resume is a design sample

A design lead will judge the resume itself before reading it: hierarchy, spacing,
type pairing, alignment. That is why a designer's resume can be more expressive than
an accountant's, but it still has to be easy to read in thirty seconds.

## Link your portfolio first

The most important line on the page is your portfolio URL. Put it in the contact
block on its own line, short and readable (yourname.design rather than a long
platform link). The downloaded PDF keeps links clickable.

## Projects before experience

List three or four projects you want to be asked about in the interview:

> Rebrand for a regional coffee chain: identity, packaging and signage for 34 stores.
> Sales of the new seasonal range were up 18%.
>
> Editorial illustration for a national magazine's annual report issue; shortlisted
> for a D&AD award.

Name the client, the scope and, when you have one, a result.

## Tools and skills

Keep tools in the sidebar (Figma, Adobe Illustrator, Photoshop, InDesign, After
Effects) and put skills that describe judgement, such as typography, brand systems
and art direction, in the main column or summary.

## Photo

Optional. Many European studios expect one; in the US and UK it is your choice. The
sidebar looks complete without it.
""",
        [
            ("What should a graphic designer put on a resume?",
             "A portfolio link, three or four strong projects with client and scope, work experience, design tools, and skills such as typography and brand systems. Keep it to one page."),
            ("Should a graphic designer resume be creative?",
             "Yes, within reason. It should show good typography and hierarchy, but it must still be easy to scan. This template uses a strong sidebar and serif headings without sacrificing readability."),
            ("Do I need a photo on a design resume?",
             "No. It is common in parts of Europe and optional elsewhere. The template works with or without one."),
            ("Can recruiters' systems read this design resume?",
             "Yes. The PDF contains real, selectable text. Agencies and studios usually review resumes by hand, but large in-house teams may use an ATS."),
        ],
    ),

    # -------------------------------------------------------------- corporate
    _page(
        "corporate", "finance-resume-template", PRO,
        "Finance and Banking Resume Template, Free | ResumeElite",
        "The Corporate resume template for finance and banking",
        "A free finance resume template for banking, insurance and corporate finance: conservative ruled header, serif headings, one clean column. Edit online, download a PDF.",
        """
A conservative resume for banking, corporate finance, insurance and other
traditional industries. A ruled header with an optional photo, small-capital serif
section headings and a single column. It looks the way a finance hiring manager
expects a resume to look, which is exactly the point.
""",
        [
            ("Best for", "Banking, financial analysis, insurance, audit, corporate roles"),
            ("Structure", "Ruled header, single column, serif headings"),
            ("Length", "One page early career; two when senior"),
            ("ATS", "Single column with real text and standard headings"),
        ],
        ["consulting-style", "accountant", "harvard-style"],
        """
## What finance recruiters look for

Accuracy, judgement and numbers. A finance resume that has vague bullets or a
typo is read as a preview of your work. Keep the layout conservative and let precise,
quantified results do the talking.

## Bullets with financial impact

Name the model, the deal or the process, and the money or time it moved:

> Built a three-statement model for a $450M acquisition; the board approved the
> deal at the valuation range recommended.
>
> Automated month-end variance analysis in Python and Power BI; close shortened from
> 8 days to 5.
>
> Covered 22 mid-cap industrials as part of a 3-person equity research team.

## Certifications and licences

CFA (with level), CPA, ACCA, FRM and regulatory licences go in their own section near
the top. For many roles they are a filter, so do not bury them.

## Technical skills

Be specific: Excel (financial modelling, VBA), SQL, Python, Power BI, Bloomberg,
Capital IQ, SAP. "Advanced Excel" on its own says little.

## Banking applications

For investment banking analyst roles, use one page and put education first if you are
a student. The Consulting template is a good alternative: the same dense,
employer-first format the industry uses.
""",
        [
            ("What is the best resume format for finance?",
             "A conservative, single-column, reverse-chronological layout with quantified bullets and certifications easy to find. This template is built for that."),
            ("Should I put CFA Level 1 on my resume?",
             "Yes, if you have passed it, as 'CFA Level I candidate (passed)' or with the level you are sitting. It shows commitment to the field."),
            ("How long should a finance resume be?",
             "One page early in your career and for banking applications; two pages are acceptable for senior finance roles."),
            ("Is this finance resume template ATS-friendly?",
             "Yes. It is one column with standard headings, and the PDF contains real text that applicant tracking systems read."),
        ],
    ),
]
