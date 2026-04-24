#!/usr/bin/env python3
"""Generate Hugo content stubs from memominds.de structure.

RULES:
- Titles/slugs/categories/headings are kept as blueprint.
- Body text is ALWAYS a TODO placeholder — never paraphrased from memominds.
- Leonie fills the real copy later.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRAPE = Path(__file__).parent
CONTENT = ROOT / "content"
structure = json.loads((SCRAPE / "structure.json").read_text())

# Map memominds URL → Hugo path
URL_MAP = {
    "https://memominds.de/":                                ("_index.md", None),
    "https://memominds.de/geistige-fitness/":               ("geistige-fitness/_index.md", "section"),
    "https://memominds.de/leben-mit-demenz/":               ("leben-mit-demenz/_index.md", "section"),
    "https://memominds.de/blog/":                           ("blog/_index.md", "section"),
    "https://memominds.de/ressourcen/":                     ("ressourcen/_index.md", "section"),
    "https://memominds.de/ueber-mich/":                     ("ueber-mich.md", "page"),
    "https://memominds.de/arena/":                          ("arena.md", "page"),
    "https://memominds.de/newsletter/":                     ("newsletter.md", "page"),
    "https://memominds.de/impressum/":                      ("impressum.md", "page"),
    "https://memominds.de/datenschutzerklaerung/":          ("datenschutz.md", "page"),
    "https://memominds.de/cookie-richtlinie/":              ("cookie-richtlinie.md", "page"),
    "https://memominds.de/ressourcen/demenz-alltagshilfen/": ("ressourcen/demenz-alltagshilfen.md", "page"),
    "https://memominds.de/ressourcen/spiele-demenz/":        ("ressourcen/spiele-demenz.md", "page"),
    "https://memominds.de/ressourcen/spiele-demenz/sesseltanz/":  ("ressourcen/spiele-demenz-sesseltanz.md", "page"),
    "https://memominds.de/ressourcen/spiele-demenz/farbenzauber/":("ressourcen/spiele-demenz-farbenzauber.md", "page"),
    "https://memominds.de/ressourcen/spiele-demenz/duftreise/":   ("ressourcen/spiele-demenz-duftreise.md", "page"),
    "https://memominds.de/ressourcen/alltagsuebungen-geistige-fitness/": ("ressourcen/alltagsuebungen-geistige-fitness.md", "page"),
    "https://memominds.de/ressourcen/demenz-ratgeber/":      ("ressourcen/demenz-ratgeber.md", "page"),
    "https://memominds.de/ressourcen/digitale-helfer-apps/": ("ressourcen/digitale-helfer-apps.md", "page"),
    "https://memominds.de/ressourcen/gehirnjogging/":        ("ressourcen/gehirnjogging.md", "page"),
}

# Blog posts: slug from URL last segment, year 2025-placeholder
BLOG_DATES = {}  # could parse published ISO from scrape; use as-is

def toml_escape(s):
    return (s or "").replace('"', '\\"')

def write_stub(rel_path: str, fm: dict, body_sections: list):
    p = CONTENT / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---"]
    for k, v in fm.items():
        if v is None or v == "":
            continue
        if isinstance(v, list):
            items = ", ".join(f'"{toml_escape(x)}"' for x in v)
            lines.append(f'{k}: [{items}]')
        elif isinstance(v, bool):
            lines.append(f'{k}: {str(v).lower()}')
        else:
            lines.append(f'{k}: "{toml_escape(str(v))}"')
    lines.append("---")
    lines.append("")
    lines.append("> **TODO – Platzhalter.** Dieser Text stammt noch nicht von Leonie.")
    lines.append("> Struktur & Überschriften sind Blueprint von memominds.de als Referenz.")
    lines.append("> Alle Paragraphen müssen durch Leonies eigene Worte ersetzt werden.")
    lines.append("")
    for h2 in body_sections:
        lines.append(f"## {h2}")
        lines.append("")
        lines.append("TODO: eigener Text von Leonie.")
        lines.append("")
    p.write_text("\n".join(lines))

def category_slug(cat_display: str) -> str:
    m = {
        "LEBENSQUALITÄT": "lebensqualitaet",
        "GEDÄCHTNISTRAINING": "gedaechtnistraining",
        "PFLEGE UND ANGEHÖRIGE": "pflege-und-angehoerige",
        "VORSORGE UND PRÄVENTION": "vorsorge-und-praevention",
        "DEMENZ VERSTEHEN": "demenz-verstehen",
        "AKTIVES ALTERN": "aktives-altern",
    }
    return m.get(cat_display, cat_display.lower())

for page in structure:
    url = page["url"]
    title = (page["title"] or "").split(" | ")[0].split(" - ")[0].strip() or "Untitled"
    desc  = page["description"]
    h2s   = [h for h in page["h2"] if h and len(h) < 120][:8]

    if url in URL_MAP:
        rel, kind = URL_MAP[url]
        fm = {"title": title, "description": desc}
        if kind == "section":
            fm["cascade"] = None  # placeholder; skip
        write_stub(rel, fm, h2s)
    else:
        # blog post
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        rel = f"blog/{slug}.md"
        cats = [category_slug(c) for c in page["categories"]]
        cats_display = [c.title() if c.isupper() else c for c in page["categories"]]
        tags = [t for t in page["tags"] if t.lower() not in {c.lower() for c in page["categories"]}]
        fm = {
            "title": title,
            "description": desc,
            "date": page.get("published") or "2025-01-01T00:00:00+01:00",
            "lastmod": page.get("modified"),
            "categories": cats_display,
            "tags": tags,
            "draft": True,
        }
        write_stub(rel, fm, h2s)

print("done")
