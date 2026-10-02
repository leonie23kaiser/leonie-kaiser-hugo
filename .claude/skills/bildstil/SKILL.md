---
name: bildstil
description: >-
  Greift bei jedem Auftrag, ein Bild, Foto oder Schaubild für leoniekaiser.com
  (Blog, Website, LinkedIn) zu beschreiben, einen Bildprompt zu schreiben oder
  Referenzbilder einzuordnen. Gilt ausdrücklich nicht für Texte, Videos, Layout-
  oder Code-Aufgaben und nicht für Bilder anderer Marken.
---

# bildstil — Bild-Designsystem von Leonie Kaiser

Bei jedem Bildauftrag den Stilblock (A) an das Motiv hängen, eine Vorlage aus B
nutzen und bei mitgegebenen Referenzbildern die Zeilen und Regeln aus C anwenden.
Der Stilblock wird ohne Änderung angehängt.

## Block A, Stilblock

Erzeuge ein ruhiges, dokumentarisches Foto aus dem Alltag einer kleinen Physiotherapie-Praxis. Verlangt das Motiv ein Schaubild, erzeuge stattdessen eine flache Vektorgrafik. Licht beim Foto: weiches, warmes Tageslicht seitlich vom Fenster, keine harten Schatten, geringe Schärfentiefe, Ausschnitt halbnah bis halbtotal. Personen sind erfunden, Anfang bis Mitte 40, mit ruhigem, freundlichem Ausdruck und schlichter Kleidung in Petrol, Weiß und Beige. Farbwelt: Petrol #086584, Salbei-Türkis #5FA2A0, Beige #FAF0E9, Senfgold #CF982B als sparsamer Akzent, Dunkelgrau #1D2228 für Linien. Violett #6B2C8C kommt nur als kleiner Akzent in Grafiken vor. Grafiken bestehen aus flachen Flächen ohne Verlauf, gleichmäßig dicken Linien, abgerundeten Ecken und drei bis vier einfachen Symbolen. Der Hintergrund ist hell und aufgeräumt: helle Wände, helles Holz, Grünpflanzen, bei Grafiken Beige oder Weiß. Ein Drittel des Bildes bleibt ruhige, leere Fläche für eine später aufgesetzte Überschrift. Motivfelder: 1. Inhaberin oder Therapeut:in am Empfang oder Schreibtisch, 2. Behandlungsraum mit Therapeut:in und Patient:in, 3. Schaubild mit Symbolen. Standardformat: Querformat 16 zu 9.

Nicht im Bild: Schrift und Text (auch Logos und Beschriftungen), Roboter, Hologramme, abstrakte Technik, Neonfarben, medizinische Geräte wie Spritzen, Stethoskop, Schloss, Schutzschild, Sternenkranz, Hacker-Hoodie, Panik-Mimik, Zettelstapel-Chaos.

## Block B, drei Vorlagen

1. Titelbild: Foto: {MOTIV}. Das linke Drittel bleibt eine ruhige, leere Wandfläche für eine Überschrift. Querformat 16 zu 9.
2. Schaubild: Flache Vektorgrafik ohne jeden Text: {MOTIV}, drei bis vier einfache Symbole, mit dünnen Linien verbunden, auf Beige. Unter den Symbolen bleibt Platz frei. Querformat 16 zu 9.
3. Detail- oder Personenbild: Foto im Nahbereich: {MOTIV}, Fokus auf Hände oder Gesicht, Hintergrund weich unscharf. Hochformat 4 zu 5.

## Block C, Referenzbilder

- Bild 1 liefert das Motiv: Übernimm Szene und Anordnung, nicht die abgebildete Person.
- Bild 2 liefert die Farben: Übernimm Farbstimmung und Licht.
- Bild 3 liefert den Bildausschnitt: Übernimm Abstand und Perspektive.

Regel Gesicht (gilt nur, wenn Leonies eigenes Gesicht vorkommen soll; aktuell zeigen die Bilder nur erfundene Praxispersonen): Soll das Gesicht über mehrere Bilder wiederkehren, braucht es drei bis fünf Porträts aus verschiedenen Winkeln. Sind die Fotos erkennbar aus einer Sitzung (gleiche Kleidung, gleiches Licht, gleicher Winkel), zählen sie zusammen als eine Referenz, und das ist dem Nutzer zu sagen. Im Repo liegen drei Sitzungen, fast alle frontal: `leonie-kaiser-portrait`, `Bild-1`, `leonie-portrait-hero` und `leonie-portrait-smile` (eine Sitzung), `leonie-portrait-soft` und `leonie-portrait-plant` (eine Sitzung), `leonie-about-thoughtful` (eine Sitzung). Seitliche Winkel fehlen.

Regel Ausschlussliste: Zeigt ein Referenzbild etwas von der Ausschlussliste, ist es beim Namen zu nennen, und die Referenzzeile muss sagen, welcher Teil übernommen wird und welcher ausdrücklich nicht. Bekannte Fälle: `leonie-portrait-globe-mix.png` und `background.png` zeigen Globus, Wolken- und Handy-Symbole in glühenden Farben (technisch-abstrakt, neonartig). Formulierung: "Übernimm nur die Person links (Gesicht, Kleidung). Den Globus rechts ausdrücklich nicht übernehmen." Bei `background.png` wird nichts übernommen, auch nicht die Farbstimmung.
