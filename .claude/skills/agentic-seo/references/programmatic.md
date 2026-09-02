# Programmatic SEO

Building SEO-optimized pages at scale using templates and data. For when you want to create many similar pages targeting different keywords, locations, or audience segments.

---

## Core Principles

1. **Unique value per page** — Every page provides value specific to that page, not just swapped variables
2. **Proprietary data wins** — Hierarchy: Proprietary > Product-derived > User-generated > Licensed > Public
3. **Subfolder structure** — `yoursite.com/services/vienna/` not `vienna.yoursite.com/services/` (subfolders consolidate authority)
4. **Quality over quantity** — 100 great pages beats 10,000 thin ones; thin content triggers manual actions
5. **Match search intent** — Pages must actually answer what people are searching for

---

## The 12 Playbooks

| # | Playbook | Pattern | Example |
|---|----------|---------|---------|
| 1 | **Templates** | "[Type] template" | "project proposal template" |
| 2 | **Curation** | "best [category]" | "best integration tools" |
| 3 | **Conversions** | "[X] to [Y]" | "$100 USD to EUR" |
| 4 | **Comparisons** | "[X] vs [Y]" | "Zapier vs Make" |
| 5 | **Examples** | "[type] examples" | "API integration examples" |
| 6 | **Locations** | "[service] in [location]" | "SAP consultants in Vienna" |
| 7 | **Personas** | "[product] for [audience]" | "integration platform for logistics" |
| 8 | **Integrations** | "[product A] [product B]" | "Salesforce SAP integration" |
| 9 | **Glossary** | "what is [term]" | "what is an API gateway" |
| 10 | **Translations** | Same content, multiple languages | Localized content |
| 11 | **Directory** | "[category] tools" | "ETL tools comparison" |
| 12 | **Profiles** | "[entity name]" | "Mulesoft overview" |

### Match Playbook to Your Assets

| If you have... | Consider... |
|----------------|-------------|
| Product with integrations | Integrations, Comparisons |
| Multi-segment audience | Personas |
| Local presence or clients | Locations |
| Expertise in a domain | Glossary, Curation |
| Competitors to compare against | Comparisons |
| Proprietary data | Directory, Profiles |
| Design/creative output | Templates, Examples |

**Combine playbooks** for more specificity: "Best SAP integration partners in Vienna" = Curation + Locations

---

## Playbook Deep Dives

### Templates
URL: `/templates/[type]/`
Value requirements: Actually usable, multiple variations, quality comparable to paid options, easy download/use

### Comparisons
URL: `/compare/[x]-vs-[y]/`
Value requirements: Honest balanced analysis, actual feature data, recommendation by use case, updated when products change

### Locations
URL: `/[service]/[city]/`
Value requirements: Actual local data (not just city name swapped), local providers listed, location-specific insights (pricing, regulations, timezone)

### Personas
URL: `/for/[persona]/` or `/solutions/[industry]/`
Value requirements: Genuine persona-specific content, relevant features highlighted, testimonials from that segment, use cases specific to audience

### Integrations
URL: `/integrations/[product]/`
Value requirements: Real integration details, setup instructions, use cases for the combination, working integration (not vaporware)

### Glossary
URL: `/glossary/[term]/` or `/learn/[term]/`
Value requirements: Clear accurate definitions, examples and context, related terms linked, more depth than a dictionary

---

## Implementation Framework

### 1. Keyword Pattern Research

Identify the repeating pattern:
- What's the variable? (city, product name, industry, comparison target)
- How many unique combinations have real search demand?
- What's the volume distribution — head vs. long tail?
- Trend direction (growing or declining)?

Validate with Search Console, Ahrefs, or Semrush before building.

### 2. Data Requirements

| Data Type | Source | Strength |
|-----------|--------|---------|
| Proprietary (you created it) | Internal | Strongest |
| Product-derived (from your users) | Product analytics | Strong |
| User-generated (community content) | Reviews, submissions | Medium |
| Licensed (exclusive access) | Data vendors | Medium |
| Public (scraped, open data) | APIs, datasets | Weakest |

Questions to answer before building:
- What data populates each page uniquely?
- How is it updated — automated or manual?
- How defensible is it? (Can competitors copy it in a day?)

### 3. Template Design

**Page structure for each template:**
- Header with target keyword (not just variable inserted)
- Unique intro (not just "Here are dentists in [city]")
- Data-driven sections with real unique content
- Related pages / internal links (hub → spokes → cross-links)
- CTAs appropriate to search intent

**Ensuring uniqueness per page:**
- Conditional content based on data attributes
- Original analysis or insights derived from the data
- Avoid identical paragraphs with just the variable swapped — Google classifies this as thin content

### 4. Internal Linking Architecture

**Hub and spoke:**
```
Hub:    /integrations/           (category page)
Spokes: /integrations/salesforce/
        /integrations/sap/
        /integrations/microsoft-365/
Cross:  /integrations/salesforce/ → /integrations/sap/ (if relevant)
```

Every page must be reachable from the main site — no orphan pages. Include all pages in XML sitemap with a separate sitemap per content type.

### 5. Indexation Strategy

- Prioritize high-volume patterns first
- `noindex` very thin or empty variations (e.g., locations with no real data)
- Separate sitemap for programmatic pages for easier monitoring
- Don't submit thin pages — wait until they have real content
- Monitor indexation rate in Search Console after each batch

---

## Quality Checks

### Pre-Launch Checklist

**Content quality:**
- [ ] Each page provides unique value (not just variable swaps)
- [ ] Answers the search intent — not just present, actually useful
- [ ] Readable and useful to a human, not just keyword-present

**Technical:**
- [ ] Unique titles and meta descriptions per page
- [ ] Proper heading structure (H1 contains primary variable)
- [ ] Schema markup implemented (BreadcrumbList at minimum; FAQPage where applicable)
- [ ] Page speed acceptable (< 3 seconds)
- [ ] Mobile-friendly

**Internal linking:**
- [ ] Connected to main site architecture
- [ ] Related pages linked from hub
- [ ] No orphan pages

**Indexation:**
- [ ] In XML sitemap
- [ ] No conflicting `noindex`
- [ ] Canonical set correctly (self-referencing)

### Post-Launch Monitoring

**Track:** Indexation rate, Rankings per page, Traffic per page, Engagement (time on page, bounce), Conversion rate

**Watch for:**
- Thin content manual actions in Search Console
- Ranking drops after Google quality updates
- Low indexation rate (< 50% indexed suggests quality issues)
- Crawl errors on programmatic pages

---

## Common Mistakes

| Mistake | Why It Hurts |
|---------|-------------|
| Just swapping variables | Thin content manual action |
| Same content in each page | Duplicate content, no indexation |
| No search demand validation | Building pages nobody searches for |
| Over-generation | Crawl budget waste, quality signal dilution |
| Ignoring UX | Pages that exist for Google but not users don't convert |
| Keyword cannibalization | Multiple pages competing for same keyword |
| Outdated or incorrect data | Users bounce, trust eroded |

---

## For Service Sites (like leoniekaiser.com)

Auf dieser Seite läuft das über `data/branchen.yaml` + `layouts/branche/single.html`.
Aktuell befüllt: die vier Leistungsseiten (Termine & Anfragen, Dokumentation &
Wissen, Nachsorge & Kundenbindung, Sichtbarkeit).

Denkbare weitere Muster:
- **Segmentseiten:** `/ki-fuer-physiotherapie-praxen/`, `/ki-fuer-longevity-praxen/`
  — waren angelegt und wurden bewusst zurückgestellt (Phase 2). Vor einer
  Wiederbelebung `strategie/segmente.md` gegenlesen: nur Tier 1 und Tier 2.
- **Fragenseiten** entlang echter Suchanfragen aus `strategie/keyword-*.md`.

Nicht anlegen:
- **Ortsseiten** (`/ki-beratung-graz/`) — Leonie arbeitet ortsunabhängig, es gäbe
  keine echte lokale Präsenz zu belegen. Dünne Ortsseiten ohne Substanz sind ein
  Ranking-Risiko, kein Hebel.
- **Vergleichsseiten** gegen namentlich genannte Mitbewerber — verstößt gegen die
  Abgrenzungs-Regel in `AGENTS.md` §9.
- Seiten zu Leistungen aus `strategie/service-katalog.md`, Abschnitt „Was ich
  ausdrücklich NICHT anbiete".
