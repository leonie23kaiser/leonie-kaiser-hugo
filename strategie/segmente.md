# Segmente & Schirm — Zielgruppen-Schärfung

*Stand: 2026-07-06. Verfeinert die Zielgruppe gegenüber `brand_position.md` und
`strategie-konzept.md`: breiterer, aber weiterhin scharfer Schirm, „Wahlarzt/privat/
Selbstzahler" statt nur Selbstzahler, Mischpraxen drin. **Website-Session bitte mitziehen.**
Silicon-Sampling-Datenbasis bleibt gültig (auf Praxen kalibriert, synthetisch/ESOMAR).*

## Der Schirm (ändert sich nie)

> Ich helfe **kleinen, inhabergeführten Gesundheits- und Behandlungsbetrieben**
> (Wahlarzt / privat / Selbstzahler), die mit **sensiblen Gesundheitsdaten** arbeiten und
> **keine IT-Abteilung** haben, ihren Alltag zu entlasten – damit wieder Zeit bleibt für
> das, worum es wirklich geht.

**Das ist die interne Strategie-Formel** — sie erklärt, wen wir meinen und warum. In der
**externen Kurz-Copy** (LinkedIn-Headline, Banner, GBP-Beschreibung) wird daraus bewusst
**„Privatpraxen in Gesundheit & Wohlbefinden"**: „Praxis" ist im Deutschen dehnbar genug für
alle 3 Start-Segmente (auch Ernährungsberatung läuft als „Privatpraxis für Ernährungsberatung"
in `branchen.yaml`), konkreter/griffiger als „Betriebe", und nennt keine Einzelsegmente — so
muss bei einem Segment-Wechsel (Scheinwerfer-Prinzip) nichts umgeschrieben werden. Der volle
Schirm-Wortlaut bleibt für längere Fließtexte (About-Section, Website-Unterseiten) reserviert.
Details/Wording: `strategie/linkedin-profil.md`.

**5 Anker-Kriterien (alle müssen passen):**
1. inhabergeführt
2. klein (ca. 2–15, max ~30 Mitarbeitende)
3. sensible **Gesundheitsdaten** (DSGVO Art. 9) ← der Burggraben, **nie** weglassen
4. keine IT-Abteilung
5. lebt (auch) von **Wahlarzt-/Privat-/Selbstzahler**-Kundschaft und konkurriert übers Erlebnis

**Mischpraxen:** drin, wenn Privatanteil **und** Veränderungsbereitschaft da sind.
**Raus:** reine Hochvolumen-Kassen-Akutmedizin (kein Budget, keine Erlebnis-Motivation),
Zahnärzte, Kliniken, Apotheken, Pflege, klinische Psychotherapie/Psychiatrie, große Pharma.

**Filter neu gedacht:** nicht die *Zahlform* entscheidet, sondern *Haltung + Privatanteil*.
Eine Mischpraxis mit Wahlarzt-Anteil und Änderungswillen ist ein besserer Kunde als eine
reine Privatordination ohne Veränderungswillen.

## Erlebnis als Kaufgrund (Kommunikations-Anker)

Wer privat / Wahlarzt zahlt, erwartet ein **Premium-Erlebnis**. Genau da zieht das
Nutzenversprechen „reibungsloses, professionelles Kundenerlebnis". Bei zugewiesenen, voll
ausgelasteten Kassenpatienten ist der Erlebnis-Hebel schwächer. → In der Copy den
**Erlebnis-Gewinn immer zusammen mit dem Zeit-Gewinn** nennen.

## Der homogene Kern-Schmerz (einmal bauen, überall wiederverwenden)

~90 % identisch über alle Behandlungs-/Therapiebetriebe:
1. **Termin-Engpass** – Anfragen bleiben liegen, No-Shows, Lücken kosten Umsatz
2. **Doku frisst die Abende**
3. **Nachsorge/Recall fällt hinten runter** – Stammkundschaft geht verloren
4. **Die Leitung ist der Flaschenhals** (Behandlung + Führung + Verwaltung in einer Person)
5. **Sensible Gesundheitsdaten** (DSGVO Art. 9)

→ Jede Unterseite/jeder Post = **dieser Kern + ein segment-spezifischer Twist** (die letzten 10 %).
Das ist das „Rad", das du nur einmal baust.

## Scheinwerfer-Prinzip (Flexibilität ohne Rebranding)

Der **Schirm bleibt stabil** (Bio, GBP, Startseite). Im Content rotiert der **Scheinwerfer**
über Segmente (diesen Monat Physio, nächsten Longevity, dann Ernährung …). Läuft ein Segment
nicht → Scheinwerfer schwenken, **ohne** Positionierung/Bio/GBP anzufassen.

## Segment-Landkarte

**A. Kern-Cluster „Behandlung & Therapie" (homogen):**
Physio, Ergo, Logopädie, Osteopathie, Podologie, Heilpraktiker/Naturheilkunde/TCM,
Hebammen, Ernährungsberatung/Diätologie.

**B. Prävention & Wohlbefinden (homogen-nah):**
Longevity/Medical-Wellness, Massage/manuelle Therapie, medizinische Wellness.
*(Ästhetik/Medical-Beauty: nicht im Vordergrund — über Blog/Einzelanfragen erreichbar,
keine eigene Start-Seite.)*

## Start-Unterseiten (genau 3)

| Seite | deckt mit ab | Segment-Twist (die 10 %) |
|---|---|---|
| **Therapie- & Bewegungspraxen** *(Aushängeschild: Physio)* | Ergo, Osteo, Podo | Serientermine/Recall, Verordnung, Sport-Nachsorge |
| **Longevity & Medical-Wellness** | Präventionsmedizin | Multi-Tool-Kundenreise, Laborwerte, Retention (Premium) |
| **Ernährungsberatung / Diätologie** | — | wiederkehrende Protokolle/Pläne, Sichtbarkeit/Content |

*(Ästhetik ist bewusst **nicht** unter den Start-Seiten — läuft über Content, nicht als eigene Seite.)*

## Erweitern

Nur bei **echter Traktion** (Anfragen, Empfehlungen) eine vierte Seite dazunehmen — und die
Möglichkeiten dann neu prüfen. Kein Vorab-Ausbauplan.

## Fertiger Baustein: Ernährungsberatung / Diätologie (für `branchen.yaml`)

*Gleiches Format wie die bestehenden Physio-/Longevity-Einträge. Zum 1:1-Übernehmen in der
Website-Session. Basis: homogener Kern-Schmerz + Ernährungs-Twist (wiederkehrende
Protokolle/Pläne, Sichtbarkeit ohne Mehraufwand). Beispielszenario ist illustrativ, kein
realer Kundenfall.*

```yaml
- slug: ernaehrungsberatung
  url: /ki-fuer-ernaehrungsberatung-praxen/
  branche: Privatpraxis für Ernährungsberatung und Diätologie
  branche_kurz: Ernährungsberatung
  zielperson: "die Leitung einer Privatpraxis für Ernährungsberatung oder Diätologie mit 1–8 Mitarbeitenden"
  schmerz: "Beratungsprotokolle und wiederkehrende Pläne fressen die Abende, das Nachfassen nach der Erstberatung bleibt liegen, und für Sichtbarkeit fehlt schlicht die Zeit."
  usecases:
    - titel: "Beratungsprotokolle effizient erstellen"
      desc: "Aus Gesprächsnotizen wird ein strukturiertes Protokoll, das Sie nur noch gegenlesen – mit einem Setup, das Gesundheitsdaten von Grund auf richtig behandelt."
    - titel: "Wiederkehrende Pläne und Vorlagen automatisieren"
      desc: "Rezeptvorschläge, Wochenpläne und Standard-Aufklärungen als Vorlagen, die in Ihrer Sprache klingen – einmal aufgesetzt, immer wieder nutzbar."
    - titel: "Nachsorge und Sichtbarkeit ohne Mehraufwand"
      desc: "Follow-up nach der Erstberatung läuft strukturiert statt manuell. Aus einem Beratungsthema entstehen nebenbei Blog- oder Social-Inhalte."
  beispiel:
    ausgangssituation: "Eine Ernährungsberatungspraxis mit zwei Mitarbeitenden. Jedes Beratungsprotokoll wird von Hand nachgeschrieben, Rezeptvorschläge und Wochenpläne entstehen jedes Mal neu. Nach der Erstberatung hört die Praxis von vielen Klient:innen nichts mehr, und für Sichtbarkeit bleibt keine Zeit."
    vorgehen: "Wir fangen bei den Abläufen an, nicht beim Tool. Erster Quick-Win: eine datenschutzkonforme Vorlage für Beratungsprotokolle, die Notizen strukturiert und nur noch gegengelesen werden muss. Danach eine Bibliothek für Wochenpläne und Rezeptvorschläge sowie ein automatischer Recall für die Nachsorge. Das Team wird eingewiesen – Sie richten nichts selbst ein."
    ergebnis: "Weniger Zeit pro Protokoll, spürbar weniger Abendarbeit. Die Nachsorge läuft zuverlässig, und aus den Beratungsthemen entstehen nebenbei Inhalte für Sichtbarkeit – ohne zusätzlichen Aufwand."
  faq:
    - q: "Dürfen Ernährungs- und Gesundheitsdaten in ein KI-Tool?"
      a: "Nicht ohne saubere Konfiguration. Ernährungs- und Gesundheitsdaten sind besondere Daten nach DSGVO Art. 9. Wir setzen für Sie Werkzeuge auf, die das von Grund auf richtig machen – mit EU-Hosting, wo möglich, und klaren Datenflüssen."
    - q: "Verliert die Beratung durch Vorlagen ihre persönliche Note?"
      a: "Nein. Vorlagen übernehmen das Wiederkehrende – die Zeit, die Sie zurückbekommen, geht in die eigentliche Beratung und den persönlichen Kontakt."
```

---

*Quellen: `brand_position.md` (Haltung), `strategie-konzept.md` (Konsolidierung),
`silicon-sampling.md` (Markt). Brand Voice: `AGENTS.md`.*
