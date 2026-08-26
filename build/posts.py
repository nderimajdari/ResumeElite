# -*- coding: utf-8 -*-
"""Blog index copy, and the assembled post list."""

import articles_a
import articles_b

BLOG_HUB = {
    "title": "Resume Writing Guides and Advice | ResumeElite",
    "h1": "Resume guides worth the reading time",
    "description": "Practical guides to writing a resume: ATS parsing, summaries that are not filler, action verbs, keywords, resume length and the mistakes that cost interviews.",
    "intro": """
Ten guides, each one written to be specific enough to act on. No listicles about being
a team player, and every one links back to a template that already has the structure
set up.
""",
}

POSTS = articles_a.ARTICLES + articles_b.ARTICLES

# Publishing order on the hub: newest first, then by path for stability.
POSTS.sort(key=lambda p: (p.get("modified", p["published"]), p["path"]), reverse=True)
