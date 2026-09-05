# Rallye Nordlicht

Eine Arcade-Rallye im Browser. Eine einzige HTML-Datei, keine Abhängigkeiten,
keine Assets — Strecken, Sprites, Musik und Motorsound entstehen zur Laufzeit im Code.

**[▶ Spielen](https://madd1in.github.io/rallye-nordlicht/)**

## Was es ist

Ein Pseudo-3D-Racer in der Tradition von *Sega Rally* und *Out Run*: die Straße wird
segmentweise projiziert, Kuppen verdecken die Sicht, die Fliehkraft schiebt dich nach außen.
Dazu ein Beifahrer, der die Strecke vorliest, und eine Uhr, die nur an Kontrollpunkten
nachgefüllt wird.

### Drei Wertungsprüfungen

| # | Etappe | Untergrund | Länge | Charakter |
|---|--------|-----------|-------|-----------|
| 01 | Alpenpass | Asphalt | 13,0 km | Griffig, Leitplanken, kein Auslauf |
| 02 | Schotterwald | Schotter | 15,0 km | Loser Belag, Abendsonne, Staub |
| 03 | Nordlicht | Schnee | 17,0 km | Nachtetappe, Eis, Schneestangen |

Dazu der **Meisterschaftsmodus**: alle drei am Stück, Zeiten addiert, ein Ausfall beendet den Lauf.

## Steuerung

| Taste | Funktion |
|-------|----------|
| ← → | Lenken |
| ↑ | Gas |
| ↓ | Bremse |
| Leertaste | Handbremse — bricht das Heck aus und lädt den Drift-Schub |
| Shift | Drift-Schub abrufen |
| R | Etappe neu starten |
| Esc | Zurück ins Menü |

Auf Touchgeräten erscheinen Bildschirmtasten; der Schub zündet dort automatisch, sobald der Balken voll ist.

## Kurvenvorhersage

Die zentrale Anzeige über dem Horizont zeigt die nächste Kurve, bevor du sie siehst:

- **Zahl** — Schärfe nach Rallye-Konvention: `1` ist eine Haarnadel, `6` ist fast geradeaus
- **Winkel** — der Bogen zeichnet den Richtungswechsel maßstäblich nach
- **Meterangabe** und ein schrumpfender Balken für die Restdistanz
- **Roter Ring plus rotes Band auf der Fahrbahn**, sobald du zu schnell für die Kurve bist —
  das Band markiert den spätesten Bremspunkt, berechnet aus Tempo, Verzögerung und Untergrund

Der Beifahrer sagt dieselbe Kurve an ("links drei, zieht zu"), per Sprachausgabe und als
Roadbook-Karte mit Tulip-Symbol.

## Technik

Alles in `src/game.html`, rund 2000 Zeilen ohne Framework:

- **Renderer** — segmentbasierte Pseudo-3D-Projektion mit Kuppenverdeckung, Distanznebel und
  parallaxen Hintergrundebenen. Sprites (Bäume, Felsen, Leitplanken, Zuschauer, Torbögen)
  werden beim Start prozedural auf Offscreen-Canvas gezeichnet.
- **Strecken** — pro Etappe aus einem festen Seed erzeugt. Gleiche Etappe, gleiche Strecke,
  vergleichbare Bestzeiten.
- **Fahrwerk** — Seitenschlupf mit Trägheit, untergrundabhängiger Grip, Untersteuern mit
  steigendem Tempo, Handbremse löst die Haftung. Sprungkuppen heben Kamera und Auto ab;
  schief gelandet kostet Tempo und Blech.
- **Streckenanalyse** — nach dem Bau werden Kurven zu Ansagen und zur Vorhersage verdichtet
  (Schärfe, Winkel, "lang" / "kurz" / "zieht zu"), Kuppen und Sprünge separat erkannt.
- **Audio** — Motor als drehzahlgekoppelte Oszillatoren, Untergrund als gefiltertes Rauschen,
  Musik als 16tel-Sequencer mit eigener Tonart und Tempo je Etappe. Das Tempo steigt mit
  deiner Geschwindigkeit.

Bestzeiten und Sektionszeiten liegen im `localStorage`.

## Bauen

`index.html` wird aus `src/game.html` erzeugt — die Quelldatei ist im Artifact-Format
(ohne Dokumentgerüst), der Build ergänzt Doctype, Charset und Metadaten:

```bash
python build.py
```

## Lizenz

MIT — siehe [LICENSE](LICENSE).
