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
| 01 | Alpenpass | Asphalt | 13,0 km | Regen, nasse Fahrbahn, Leitplanken |
| 02 | Schotterwald | Schotter | 15,0 km | Loser Belag, Abendsonne, Staub |
| 03 | Nordlicht | Schnee | 17,0 km | Nachtetappe, Eis, Schneestangen |

Dazu der **Meisterschaftsmodus**: alle drei am Stück, Zeiten addiert, ein Ausfall beendet den Lauf.

Jede Etappe hat ihren eigenen **Tagesverlauf**: der Alpenpass reißt gegen Ende auf und der Regen
lässt nach, der Schotterwald kippt aus dem Abendlicht in die Dämmerung, und über dem Nordlicht
zieht zum Ziel hin die erste Morgenhelligkeit auf. Himmel, Nebelfarbe, Sonnenstand und
Gesamtstimmung interpolieren dabei über die Streckenlänge.

Auf jeder Etappe fahren **fünf Gegner** vor dir los. Du startest als Sechster; jeder Überholvorgang
zählt, jeder Rempler kostet Tempo. Der vorderste trägt einen gelben Pfeil: das ist dein
**Duellgegner**. Er fährt ein festes, schnelles Tempo mit leichter Gummiband-Korrektur, damit das
Duell offen bleibt, und der Abstand zu ihm steht laufend im Display. Wer ihn bis zum Ziel hinter
sich lässt, bekommt 3000 Punkte.

Ab dem zweiten Lauf fährt zusätzlich dein **Bestzeit-Geist** mit — ein halbtransparentes Auto
auf der Ideallinie deines Rekords, mit laufendem Zeitabstand im Display.

## Drei Fahrzeuge

Unter der Etappenliste steht die Fahrzeugwahl. Die beiden hinteren Wagen sind zu Beginn gesperrt.

| Wagen | Antritt | Tempo | Grip | Freischaltung |
|---|---|---|---|---|
| Gruppe B | mittel | mittel | mittel | von Anfang an |
| Kompakt | hoch | niedrig | sehr hoch | eine Etappe beenden |
| Turbo Allrad | sehr hoch | sehr hoch | niedrig | einmal Gold fahren |

Die Werte greifen direkt in die Fahrphysik: Beschleunigung, Höchstgeschwindigkeit,
Haftungsrückstellung und Lenkautorität. Jeder Wagen hat seine eigene Lackierung und Startnummer.

## Was auf der Strecke passiert

Neben Kurven und Kuppen liegen ein paar Dinge, auf die es sich zu zielen lohnt:

- **Turbo-Pfeile** — amberne Pfeile auf der Fahrbahn, oft abseits der Ideallinie. Wer drüberfährt,
  bekommt sofort Schub. Jeder Pfeil zündet nur einmal pro Lauf.
- **Wasserdurchfahrten** — eine Furt pro Etappe. Über 52 % Tempo bremst das Wasser hart,
  die Haftung fällt, das Heck wird unruhig, und es spritzt gewaltig.
- **Perfekte Kurven** — wer eine Kurve der Schärfe 4 oder enger durchfährt, ohne die Straße
  zu verlassen und ohne unter das Grenztempo zu fallen, bekommt Punkte und eine Ansage.

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

Im Menü wählen ↑ ↓ die Etappe und ← → den Wagen.

Auf Touchgeräten erscheinen Bildschirmtasten; der Schub zündet dort automatisch, sobald der Balken voll ist.

## Kurvenvorhersage

Die zentrale Anzeige über dem Horizont zeigt die nächste Kurve, bevor du sie siehst:

- **Zahl** — Schärfe nach Rallye-Konvention: `1` ist eine Haarnadel, `6` ist fast geradeaus
- **Winkel** — der Bogen zeichnet den Richtungswechsel maßstäblich nach
- **Meterangabe** und ein schrumpfender Balken für die Restdistanz
- **Roter Ring plus rotes Band auf der Fahrbahn**, sobald du zu schnell für die Kurve bist —
  das Band markiert den spätesten Bremspunkt, berechnet aus Tempo, Verzögerung und Untergrund

Der Beifahrer sagt dieselbe Kurve per Sprachausgabe an ("links drei, zieht zu") — die Anzeige
ist die einzige Stelle im Bild, an der die Kurve steht.

## Punkte

Neben der Uhr läuft eine Arcade-Wertung mit **Combo-Multiplikator**: jedes gelungene Ereignis
hebt ihn um eine Stufe, bis zu x8, und er verfällt nach vier Sekunden ohne Nachschub.
Ein Rempler setzt ihn auf x1 zurück.

| Ereignis | Punkte |
|---|---|
| Driften | laufend, je nach Winkel und Tempo |
| Knapp vorbei an Hindernis oder Gegner | 150 bzw. 200 + etwas Drift-Schub |
| Überholvorgang | 500 |
| Sauber gelandeter Sprung | 300 + 1,5 s |
| Perfekte Kurve (Tempo gehalten, auf der Straße geblieben) | 400 |
| Turbo-Pfeil getroffen | 200 + sofortiger Schub |
| Kontrollpunkt | 1000 |
| Duellgegner im Ziel geschlagen | 3000 |
| Kollision | −200 |

Am Ende gibt es zusätzlich zur Medaille einen **Rang** von S bis C aus Zeit und Punkten.

## Technik

Alles in `src/game.html`, rund 2000 Zeilen ohne Framework:

- **Renderer** — segmentbasierte Pseudo-3D-Projektion mit Kuppenverdeckung, Distanznebel und
  parallaxen Hintergrundebenen. Sprites (Bäume, Felsen, Leitplanken, Zuschauer, Torbögen)
  werden beim Start prozedural auf Offscreen-Canvas gezeichnet.
- **Strecken** — pro Etappe aus einem festen Seed erzeugt. Gleiche Etappe, gleiche Strecke,
  vergleichbare Bestzeiten.
- **Fahrwerk** — Seitenschlupf mit Trägheit, untergrundabhängiger Grip, leichtes Untersteuern mit
  steigendem Tempo, Handbremse löst die Haftung. Gegenlenken erhöht die Haftung, damit ein Rutscher
  fangbar bleibt. Sprungkuppen heben Kamera und Auto ab; schief gelandet kostet Tempo und Blech.
- **Kamera** — neigt sich in Kurven mit Tempo und Schräglauf, mit einem Zoomstoß beim Drift-Schub.
- **Streckenmöblierung** — Tunnelröhren aus gestapelten Portalringen (der Regen hört darin auf),
  Brückenabschnitte über einem Abgrund mit Fachwerkgeländer, Nebelbänke, Laternen mit Lichtinseln
  auf der Nachtetappe, Warnschraffur vor scharfen Kurven, eingefahrene Reifenspuren in der
  Ideallinie, Pfützen mit Gischt, Ortsdurchfahrten mit beidseitiger Bebauung und beleuchteten
  Fenstern, Wasserdurchfahrten mit bewegtem Glanz, Zuschauergruppen, Hütten, Holzstapel.
- **Effekte** — Blendung, wenn die Sonne in Fahrtrichtung steht, Laubwirbel im Schotterwald,
  Schlammspritzer und Risse in der Heckscheibe, die mit dem Schaden am Auto wachsen.
- **Horizont** — drei parallaxe Gebirgsebenen pro Etappe, die fernste mit Schneekappen auf den Gipfeln.
- **Streckenanalyse** — nach dem Bau werden Kurven zu Ansagen und zur Vorhersage verdichtet
  (Schärfe, Winkel, "lang" / "kurz" / "zieht zu"), Kuppen und Sprünge separat erkannt.
- **Audio** — Motor als drehzahlgekoppelte Oszillatoren mit Hall in den Tunneln,
  Untergrund als gefiltertes Rauschen,
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
