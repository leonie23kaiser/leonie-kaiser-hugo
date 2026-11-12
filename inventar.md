# Inventar (Sicherheits-Wachhund)

**Stand:** 2026-11-02 · **Status:** Entwurf, wartet auf Leonies Ergänzungen und OK
**Quelle:** Cloud-Container der Claude-Session + Repo. NICHT Leonies Laptop.

## A. Website (leoniekaiser.com)

| Komponente | Version | Quelle / Bemerkung |
|---|---|---|
| Hugo Extended | 0.135.0 (CI, `deploy-pages.yml`: HUGO_VERSION) | Live-Build. `vm-setup.sh` nennt noch 0.123.7 (Drift, nur für die VM relevant); im Cloud-Container nicht installiert |
| web-vitals | 4.2.4 (selbst gehostet, `static/js/`) | seit 2026-11-12; vorher unpkg `@4`, nur aktiv wenn `vitalsEndpoint` gesetzt (aktuell nicht gesetzt) |
| GitHub Pages Deploy | – | `.github/workflows/deploy-pages.yml` |
| actions/checkout | v4 | CI |
| actions/configure-pages | v5 | CI |
| actions/upload-pages-artifact | v3 | CI |
| actions/deploy-pages | v4 | CI |
| Domain / DNS | leoniekaiser.com | `static/CNAME`; Registrar/DNS-Anbieter: **offen** |
| Schriften | Cabinet Grotesk, Satoshi | self-hosted, kein Google Fonts |
| Calendly | Embed/Links | externer Dienst (calendly.com) |
| Formular-Dienste | web3forms.com, formspree.io | externe Dienste (Welcher ist aktiv? **offen**) |
| Google Tag Manager | – | `googletagmanager.com` in Layouts; Container-ID/Tags **offen** |
| unpkg.com | keine Referenz mehr in Layouts | war web-vitals; jetzt selbst gehostet |
| cdn.jsdelivr.net | `static/analyse/index.html`: pptxgenjs 3.12.0 | eigene Unterseite, lädt Skript von extern (Version gepinnt) |

Keine `package.json`, `go.mod`, Hugo-Module oder Theme-Submodule im Repo. Auf der Website liegen keine npm- oder Go-Abhängigkeiten.

## B. Cloud-Container (Claude-Session, flüchtig)

| Komponente | Version |
|---|---|
| Ubuntu | 24.04.5 LTS, Kernel 6.18.44 |
| bash | 5.2.21 |
| git | 2.43.0 |
| curl | 8.5.0 (OpenSSL 3.0.13) |
| openssl | 3.0.13-0ubuntu3.16 |
| libc6 | 2.39-0ubuntu8.9 |
| Python | 3.13.18 (System-Paket python3: 3.12.3) |
| Node.js | 22.23.4 |
| Go | 1.24.7 |
| Ruby | 3.3.6 |
| gh | 2.89.0 |
| npm global | claude-code 2.1.42, npm 10.9.9, pnpm 10.28.0, yarn 1.22.22, playwright 1.63.0, eslint 10.1.0, prettier 3.8.1, typescript 6.0.2, serve 14.2.6, http-server 14.1.1, nodemon 3.1.14, docx 9.7.1, chromedriver 147.0.0, ts-node 10.9.2 |
| pip (Auswahl) | cryptography 50.0.1, lxml 6.1.3, jinja2 3.1.6, httpx2 2.13.1, mcp 2.3.0, claude-agent-sdk 0.2.172, beautifulsoup4 4.15.0 |

Hinweis: Der Container wird nach der Session verworfen. Hier gefundene Lücken sind für Leonies echte Systeme zweitrangig.

## C. Entwicklungs-Werkzeuge laut Repo (`.mcp.json`, `vm-setup.sh`)

- MCP-Server per `npx ...@latest`: context7 (HTTP), playwright, angular-cli, azure-deploy und weitere. `@latest` heißt: ungepinnt, die Version ändert sich unbemerkt. → Hinweis fürs Scan-Ergebnis
- VM-Setup: Node 20 (NodeSource), Claude Code, tmux, Hugo 0.123.7

## D. Das sehe ich nicht, bitte Leonie ergänzen

Siehe Fragenliste im Chat. Sobald beantwortet, trage ich es hier ein:

- [ ] Leonies Rechner (Betriebssystem + Version, Browser + Erweiterungen, Hugo/Git/Node lokal, Claude Code)
- [ ] Weitere Rechner / Handy / Tablet
- [ ] Server / VM (`vm-setup.sh` deutet auf eine VM hin, wo läuft sie?)
- [ ] Domain-Registrar, DNS, E-Mail-Anbieter für @leoniekaiser.com
- [ ] Shop / Zahlungsdienst (falls vorhanden)
- [ ] Router, NAS, Smart-Home
- [ ] Passwort-Manager, 2-Faktor-Setup
- [ ] Newsletter-/CRM-/Buchungs-Tools (Calendly-Konto, Formular-Dienst, Tag Manager)
- [ ] Weitere Websites/Plugins
