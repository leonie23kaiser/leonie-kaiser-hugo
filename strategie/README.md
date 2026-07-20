# strategie/ — zentrale Strategie-Ablage (Single Source of Truth)

**Das hier ist die zentrale Ablage für die gesamte Strategie.** Alle Claude-Threads und
alle Personen greifen auf *diese* Dateien auf dem `main`-Branch zu — es gibt keine zweite
Kopie irgendwo. Wer die aktuelle Strategie braucht, findet sie hier.

> **Word-Dokumente (.docx) liegen NICHT im Repo.** Sie werden bei Bedarf aus diesen
> `.md`-Dateien erzeugt (Download). Die `.md` sind immer die Wahrheit, das Word-Doc ist nur
> eine Momentaufnahme zum Verschicken/Ausdrucken.

---

## Wo anfangen

👉 **[`strategie-konzept.md`](strategie-konzept.md) ist die Master-Datei — „lies das zuerst".**
Sie konsolidiert alles: Positionierung, Zielgruppe (inkl. Zwei-Track), Angebot, Preise,
Startplan. Alle anderen Dateien sind entweder **Detail-Quellen**, die sie speisen, oder
**fertige Copy** für einen bestimmten Kanal.

Für ein Gesamt-Word-Dokument (Konzept + Positionierung + Service-Katalog in einem): auf
Anfrage generierbar, nicht dauerhaft im Repo.

---

## Inhalt (nach Rolle)

### Master
| Datei | Zweck |
|---|---|
| **[`strategie-konzept.md`](strategie-konzept.md)** | **Konsolidiertes Gesamt-Konzept.** Stand 2026-07-20. Hier zuerst nachschauen. |

### Detail-Quellen (speisen das Konzept)
| Datei | Zweck |
|---|---|
| [`segmente.md`](segmente.md) | Schirm, Anker-Kriterien, homogener Kern-Schmerz, Zielsegment-Landkarte (Tier 1/2/3). |
| [`silicon-sampling.md`](silicon-sampling.md) | Synthetische Marktforschung, alle Runden (Scores, Preise, O-Töne). ESOMAR. |
| [`zielgruppen-zwei-track.md`](zielgruppen-zwei-track.md) | Zwei-Track-Herleitung (Praxen + Pharma-/Gesundheits-KMU), Netzwerkaufbau. |
| [`brand_position.md`](brand_position.md) | Haltung: Mission/Anti-Mission, wen wir (nicht) bedienen. |
| [`angebotsvorschlaege.md`](angebotsvorschlaege.md) | Angebots-Architektur, Preis-Korridore, Einwandbehandlung. |
| [`service-katalog.md`](service-katalog.md) | Konkreter Service-Katalog, Retainer-Abdeckung, Beispiel-Szenarien. |
| [`pilot-akquise.md`](pilot-akquise.md) | Operativ: Pilot-Akquise, Anschreiben, 3 Messfragen, Einwilligung. |
| [`brand_data.md`](brand_data.md) | Belege, Methodik, Quellen-Hierarchie, Erfolgsmetriken. |
| [`story_bank.md`](story_bank.md) | Zitierbare Mini-Geschichten (Situation→Konflikt→Lösung→Beweis). |

### Fertige Copy (pro Kanal)
| Datei | Zweck |
|---|---|
| [`linkedin-profil.md`](linkedin-profil.md) · [`linkedin-profil-en.md`](linkedin-profil-en.md) | LinkedIn-Headline, Info, Positionen (DE/EN). |
| [`unternehmensbeschreibung.md`](unternehmensbeschreibung.md) | Verzeichnisse/Canva/Social + Farbpalette. |
| [`google-business-profile.md`](google-business-profile.md) | GBP: Kategorien, Beschreibung, Leistungen, Q&A. |
| [`empfehlungs-stories.md`](empfehlungs-stories.md) | Spiegelgeschichten in 3 Längen + Kanal-Plan. |

### Audits & Betrieb
| Datei | Zweck |
|---|---|
| [`trust_audit.md`](trust_audit.md) · [`citation_audit.md`](citation_audit.md) | Trust- & Citation-Audits mit Maßnahmen. |
| [`update-plan.md`](update-plan.md) | Wann was aktualisieren (Ereignis-/Zeit-getriggert). |

### Archiv / überholt
| Datei | Zweck |
|---|---|
| [`strategie-briefing-gesundheitsbetriebe.md`](strategie-briefing-gesundheitsbetriebe.md) | **Überholt** (Stand 01.07.) — ersetzt durch `strategie-konzept.md`. Nur noch historisch. |

---

## So arbeiten mehrere Threads sauber auf denselben Dateien

Damit nichts verloren geht (es gab schon einmal einen Merge-Datenverlust), gelten drei Regeln:

1. **Immer erst holen, dann bearbeiten, direkt danach pushen.**
   `git fetch origin main && git merge --no-edit origin/main` **vor** dem Editieren,
   `git push` **sofort** nach dem Commit. Nicht lange mit uncommitteten Änderungen sitzen.
2. **Bereichs-Ownership — nicht zwei Threads gleichzeitig dieselbe Datei.**
   - Strategie-Thread → `strategie/` (dieser Ordner).
   - Website-Thread → `src/growthtogether.at/` (Layouts, Content, `data/branchen.yaml`, Tool).
   Braucht ein Thread etwas im anderen Bereich, per Prompt an den zuständigen Thread geben,
   statt selbst reinzuschreiben.
3. **Eine Wahrheit pro Thema.** Neue Erkenntnis → in die passende bestehende Datei
   einarbeiten (und im Master `strategie-konzept.md` kurz spiegeln), **keine neue
   Parallel-Datei** zum selben Thema anlegen. So bleibt die Dateizahl stabil.

---

*Brand Voice (kanonisch): [`../AGENTS.md`](../AGENTS.md). Marktzahlen synthetisch
(ESOMAR ICC Code 2025) — vor größeren Entscheidungen mit echten Gesprächen validieren.*
