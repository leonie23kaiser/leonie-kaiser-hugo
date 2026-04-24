#!/usr/bin/env python3
"""Extract structure (not text content) from memominds.de scrape.

Outputs JSON with per-page: url, title, description, h1, h2s, h3s, categories, tags, date, hero_img.
We only use this as a *blueprint* for the Hugo site — real text must come from Leonie.
"""
import json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
RAW = ROOT / "raw"
OUT = ROOT / "structure.json"

def meta(soup, name=None, prop=None):
    if prop:
        tag = soup.find("meta", attrs={"property": prop})
    else:
        tag = soup.find("meta", attrs={"name": name})
    return tag.get("content") if tag else None

def extract(path: Path, url: str):
    html = path.read_text(errors="ignore")
    soup = BeautifulSoup(html, "lxml")
    title = (soup.title.string.strip() if soup.title and soup.title.string else None)
    desc = meta(soup, name="description") or meta(soup, prop="og:description")
    og_img = meta(soup, prop="og:image")
    h1 = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]
    h2 = [h.get_text(" ", strip=True) for h in soup.find_all("h2")]
    h3 = [h.get_text(" ", strip=True) for h in soup.find_all("h3")]
    # Rank Math often puts JSON-LD; also article:published_time
    published = meta(soup, prop="article:published_time")
    modified = meta(soup, prop="article:modified_time")
    section = meta(soup, prop="article:section")
    # categories from rel=category links
    cats = sorted({a.get_text(strip=True) for a in soup.select("a[rel~=category]") if a.get_text(strip=True)})
    tags = sorted({a.get_text(strip=True) for a in soup.select("a[rel~=tag]") if a.get_text(strip=True)})
    return {
        "url": url,
        "file": path.name,
        "title": title,
        "description": desc,
        "og_image": og_img,
        "published": published,
        "modified": modified,
        "section": section,
        "categories": cats,
        "tags": tags,
        "h1": h1,
        "h2": h2,
        "h3": h3,
    }

def main():
    urls = {}
    for f in (ROOT / "pages.txt", ROOT / "posts.txt"):
        for line in f.read_text().splitlines():
            url = line.strip()
            if not url:
                continue
            slug = url.replace("https://memominds.de/", "").rstrip("/").replace("/", "_") or "_home"
            urls[slug] = url
    out = []
    for slug, url in urls.items():
        p = RAW / f"{slug}.html"
        if not p.exists():
            continue
        out.append(extract(p, url))
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {OUT} ({len(out)} pages)")

if __name__ == "__main__":
    main()
