# -*- coding: utf-8 -*-
"""
A deliberately small Markdown-to-HTML converter.

Why not a library: the site ships as plain static files with no toolchain, and
pulling in a dependency would mean anyone editing content also has to manage a
Python environment. This handles exactly the subset the content uses and fails
loudly on anything it does not recognise, which is safer than silently emitting
half-converted markup.

Supported: h2-h4, paragraphs, unordered/ordered lists, blockquotes, fenced code,
tables, horizontal rules, and inline **bold**, *italic*, `code`, [links](url).
Headings get id attributes so the table of contents can link to them.
"""

import re
import unicodedata

__all__ = ["render", "collect_headings", "slugify", "plain_text"]


def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def _esc(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))


# ---------------------------------------------------------------- inline pass
def _inline(text):
    out = _esc(text)

    # `code` first so its contents are never re-processed as emphasis
    holds = []

    def hold(match):
        holds.append(match.group(1))
        return "\x00%d\x00" % (len(holds) - 1)

    out = re.sub(r"`([^`]+)`", hold, out)

    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", out)
    out = out.replace(" -- ", " &mdash; ")

    for i, held in enumerate(holds):
        out = out.replace("\x00%d\x00" % i, "<code>%s</code>" % held)
    return out


# ----------------------------------------------------------------- block pass
def render(markdown):
    lines = markdown.replace("\r\n", "\n").split("\n")
    html = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # fenced code
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            body = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            cls = ' class="lang-%s"' % lang if lang else ""
            html.append("<pre><code%s>%s</code></pre>" % (cls, _esc("\n".join(body))))
            continue

        # horizontal rule
        if re.fullmatch(r"-{3,}|\*{3,}", stripped):
            html.append("<hr />")
            i += 1
            continue

        # headings
        m = re.match(r"^(#{2,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            html.append('<h%d id="%s">%s</h%d>'
                        % (level, slugify(text), _inline(text), level))
            i += 1
            continue

        # table
        if "|" in stripped and i + 1 < n and re.fullmatch(r"[\s|:-]+", lines[i + 1].strip()):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head = "".join("<th>%s</th>" % _inline(c) for c in header)
            body = "".join(
                "<tr>%s</tr>" % "".join("<td>%s</td>" % _inline(c) for c in r)
                for r in rows)
            html.append('<div class="table-scroll"><table><thead><tr>%s</tr></thead>'
                        "<tbody>%s</tbody></table></div>" % (head, body))
            continue

        # blockquote
        if stripped.startswith("> "):
            body = []
            while i < n and lines[i].strip().startswith("> "):
                body.append(lines[i].strip()[2:])
                i += 1
            html.append("<blockquote><p>%s</p></blockquote>" % _inline(" ".join(body)))
            continue

        # lists
        bullet = re.match(r"^[-*]\s+(.*)$", stripped)
        number = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if bullet or number:
            tag = "ul" if bullet else "ol"
            pattern = r"^[-*]\s+(.*)$" if bullet else r"^\d+[.)]\s+(.*)$"
            items = []
            while i < n:
                s = lines[i].strip()
                m2 = re.match(pattern, s)
                if m2:
                    items.append(m2.group(1))
                    i += 1
                elif s and (lines[i].startswith("  ") or lines[i].startswith("\t")) and items:
                    items[-1] += " " + s          # continuation of the last item
                    i += 1
                else:
                    break
            html.append("<%s>%s</%s>"
                        % (tag, "".join("<li>%s</li>" % _inline(it) for it in items), tag))
            continue

        # paragraph
        body = []
        while i < n and lines[i].strip() and not re.match(
                r"^(#{2,4}\s|[-*]\s|\d+[.)]\s|>\s|```|-{3,}$)", lines[i].strip()):
            body.append(lines[i].strip())
            i += 1
        html.append("<p>%s</p>" % _inline(" ".join(body)))

    return "\n".join(html)


def collect_headings(markdown, levels=(2,)):
    """Headings for a table of contents, in document order."""
    found = []
    in_code = False
    for line in markdown.replace("\r\n", "\n").split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m and len(m.group(1)) in levels:
            text = m.group(2).strip()
            found.append((slugify(text), re.sub(r"[*`]", "", text)))
    return found


def plain_text(markdown):
    """Rough word-count / meta-description source."""
    text = re.sub(r"```.*?```", " ", markdown, flags=re.S)
    text = re.sub(r"[#>*`|-]", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()
