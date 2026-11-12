# Cloudflare: Sicherheitsheader für leoniekaiser.com

**Stand:** 2026-11-12 · **Warum:** GitHub Pages kann keine eigenen HTTP-Header setzen. Ausgangslage: securityheaders.com = F, SSL Labs = B.
Alles wird im Cloudflare-Dashboard gemacht (Domain `leoniekaiser.com` wählen). Am Repo ändert sich dafür nichts.

## A. TLS und HTTPS (*SSL/TLS*)

1. *Overview*: Modus **Full (strict)**.
2. *Edge Certificates* → **Minimum TLS Version: TLS 1.2**.
3. *Edge Certificates* → **Always Use HTTPS** an, **Automatic HTTPS Rewrites** an.
4. *Edge Certificates* → **HSTS** aktivieren:
   - Max Age: **6 Monate**
   - Include subdomains: **aus** (erst an, wenn alle Subdomains HTTPS können)
   - Preload: **aus**
   - No-Sniff Header: **an** (setzt `X-Content-Type-Options: nosniff`)
5. GitHub-Repo → *Settings → Pages* → **Enforce HTTPS** angehakt.

Risiko: Sehr alte Geräte (z. B. Android 4, Windows XP) erreichen die Seite nicht mehr. HSTS lässt sich nur langsam zurücknehmen, deshalb die kurze Laufzeit ohne Preload.

## B. Sicherheitsheader (*Rules → Transform Rules → Modify Response Header*)

Neue Regel `Security Headers`, Bedingung: *Hostname equals* `leoniekaiser.com` oder `www.leoniekaiser.com`. Pro Zeile *Set static*:

| Header | Wert |
|---|---|
| `X-Frame-Options` | `SAMEORIGIN` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=()` |

`X-Content-Type-Options: nosniff` kommt bereits über HSTS (A.4). Wenn du die Option dort nicht aktivierst, trage ihn hier als vierten Header ein.

## C. Content-Security-Policy, zuerst nur Report-Only

In derselben Regel ein weiterer Header *Set static*:

- Name: `Content-Security-Policy-Report-Only`
- Wert (eine Zeile):

```
default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://*.google-analytics.com https://www.googletagmanager.com; font-src 'self'; connect-src 'self' https://api.web3forms.com https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com; form-action 'self' https://api.web3forms.com; base-uri 'self'; object-src 'none'; frame-ancestors 'self'
```

Herkunft der Einträge (Repo-Prüfung 2026-11-12):

| Eintrag | Grund |
|---|---|
| `googletagmanager.com`, `*.google-analytics.com`, `*.analytics.google.com` | Google Analytics, erst nach Einwilligung (Cookie-Banner) |
| `api.web3forms.com` | Kontaktformular (`scripts.html`, `home.html`) |
| kein `frame-src` | Der YouTube-Shortcode bettet nichts ein (nur ein lokales Vorschaubild) und wird im Content nicht verwendet. Frames sind damit über `default-src 'self'` auf die eigene Seite beschränkt |
| `'unsafe-inline'` bei Script/Style | Die Seite hat viele Inline-Skripte, Inline-Styles und Inline-Handler (`onclick` in `nav.html`, `faq/single.html`). Erst wenn die im Code auf externe Dateien umgezogen sind, kann es raus |
| kein Calendly-Eintrag | Calendly ist nur verlinkt, nicht eingebettet |
| kein unpkg | `web-vitals` liegt seit 2026-11-12 selbst gehostet unter `/js/web-vitals-4.2.4.js` |

Sonderfall `/analyse/` (`static/analyse/index.html`): Die Unterseite lädt `https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/...`. Im Report-Only-Modus erscheint das nur als Meldung. Vor dem Erzwingen: entweder `https://cdn.jsdelivr.net` in `script-src` aufnehmen oder die Datei selbst hosten.

## D. Beobachten, dann erzwingen

1. 1 bis 2 Wochen laufen lassen.
2. Im Chrome F12 → *Konsole*. Meldungen mit `[Report Only] Refused to …` zeigen, was die CSP blockieren würde. Durchklicken: Startseite, FAQ, Journal, Formular, Cookie-Banner (einmal "Alle akzeptieren"), `/analyse/`.
3. Sauber? Header in `Content-Security-Policy` umbenennen (Report-Only entfällt).
4. Kontrolle: securityheaders.com und SSL Labs (Erwartung: A oder besser).

## E. Zurücknehmen

Alle Regeln lassen sich im Dashboard einzeln löschen oder deaktivieren. Nur HSTS wirkt in Browsern bis zum Ablauf des Max-Age nach.
