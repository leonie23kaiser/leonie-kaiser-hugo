# Phase 3 – SEO/GEO-Ausbau (Mai 2026)

Frontend (Design, Komponenten, Tokens) bleibt unangetastet. Phase 3 erweitert
ausschließlich Inhalte, Layouts für neue Seitentypen und Schema-Markup.

## Neue Bestandteile

| Bereich | Pfad | Zweck |
|---|---|---|
| Brand-Voice-Guard | `AGENTS.md` | Kanonische Voice-Regeln für alle KI-Assistenten |
| Referenzen | `/referenzen/` | Drei bestehende Coaching-Stimmen sichtbar, Vorbereitung für KI-Cases |
| EU-AI-Act-Pillar | `/eu-ai-act/` | Authority-Seite, Backlink-Magnet, FAQ-Schema |
| Journal (Blog) | `/journal/`, `/journal/<slug>/` | Wochenrhythmus, Article-Schema automatisch |
| Branchen-Pages | `/ki-fuer-physiotherapie-praxen/`, `/ki-fuer-psychotherapie-praxen/`, `/ki-fuer-ernaehrungsberatung/`, `/ki-fuer-coaches/` | Programmatic SEO aus `data/branchen.yaml` |

## Workflow neuer Journal-Beitrag

1. In `content/journal/` neue `.md` anlegen (oder `archetypes/journal.md` als Vorlage nutzen).
2. Front-Matter ausfüllen, **draft: true** lassen, Inhalt schreiben.
3. Brand-Voice-Check gegen `AGENTS.md` (Sie-Form, keine Buzzwords, Aufbau Problem→Lösung→Schritt).
4. Wenn fertig: `draft: false` setzen, Datum anpassen (Hugo übernimmt es für Sort + Schema).
5. Commit + Push → GitHub Actions baut automatisch.

## Vorhandene Beitrags-Skelette

Im `content/journal/` liegen 7 Drafts mit Outlines aus dem Briefing-Themenplan:

- `wo-fange-ich-mit-ki-an.md` (heute, Draft)
- `chatgpt-dsgvo-konform-nutzen.md` (Woche 2, Draft)
- `wissensverlust-mitarbeitende-ki.md` (Woche 3, Draft)
- `5-prozesse-sofort-automatisieren.md` (Woche 4, Draft)
- `eu-ai-act-kleine-unternehmen.md` (Woche 5, Draft)
- `ki-im-gesundheitswesen.md` (Woche 6, Draft)
- `warum-chatgpt-ausprobieren-scheitert.md` (Woche 7, Draft)

Leonie befüllt sie nacheinander via claude.ai mit dem System-Prompt aus `AGENTS.md`.

## Neue Branche hinzufügen

1. Eintrag in `data/branchen.yaml` ergänzen (slug, branche, zielperson, schmerz, 3 usecases, 1–2 FAQs).
2. Content-Stub anlegen: `content/ki-fuer-<slug>/_index.md` mit `type: branche`, `branche_slug: <slug>`, eigene Title + Description.
3. Hugo build – fertig.

## Schema-Markup

`layouts/partials/schema.html` rendert automatisch:

- Person + Organization + WebSite (überall)
- AboutPage (auf `/ueber-mich/`)
- FAQPage (bei `faqs:` im Front-Matter)
- Article (auf jedem Journal-Post)
- BreadcrumbList (drei Stufen bei Journal-Posts, sonst zwei)
- Speakable (Home + Über-mich)

## Was nicht in Phase 3 enthält ist

- Voice-Skill (Voice-Memo → Blog-Entwurf) – separat, später
- Performance-Audit / Web-Vitals-Messung – nach Cutover auf leoniekaiser.com
- GSC/Bing-Setup für growthtogether.at – separater Schritt mit Emanuel
