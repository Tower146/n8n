# Second Brain — Intensiv-Lauf

Verbindliche Arbeitsanweisung für die Aktualisierung des Second Brain.
Gilt unverändert für den wöchentlichen Automatiklauf **und** für den Lauf auf Zuruf.

## Grundsatz

Ein Lauf ist **immer intensiv**. Es gibt keinen Schnelldurchlauf, keine
Sparvariante, keine Stichprobe. Reduziert wird die *Häufigkeit*, niemals die
*Tiefe*.

Konkret heißt intensiv:

- Jede Quelle im Arbeitsvorrat wird **vollständig** gelesen, von Anfang bis Ende.
- Nicht „die letzten N Nachrichten", nicht „reingucken", nicht „überfliegen".
- Ist eine Quelle zu groß für einen Durchgang, wird sie in Abschnitte geteilt und
  **jeder Abschnitt vollständig** gelesen — Abschnitte werden nicht übersprungen.
- Der Lauf ist erst fertig, wenn zu **jeder** Quelle aus dem Arbeitsvorrat ein
  Extrakt vorliegt. Fehlt einer, ist der Lauf unvollständig und wird als solcher
  protokolliert.

## Auslöser

| Weg | Auslöser | Umfang |
|---|---|---|
| automatisch | wöchentlich, per Scheduler | seit dem letzten protokollierten Lauf |
| auf Zuruf | „Second Brain intensiv" im Input | seit letztem Lauf, oder wie angegeben |

Beim Zuruf kann der Umfang mitgegeben werden, z. B.
„Second Brain intensiv, letzte 14 Tage" oder
„Second Brain intensiv, nur Projekt Kalender-Loop".
Ohne Angabe gilt: seit dem letzten Lauf laut `laufprotokoll.md`.

## Ablauf

### Phase 0 — Umfang bestimmen

1. Letzten Lauf aus `laufprotokoll.md` lesen (Datum + Stand).
2. Alle Quellen auflisten, die seither neu oder verändert sind.
3. Diese Liste **als Arbeitsvorrat festhalten, bevor gelesen wird**.

Der Arbeitsvorrat wird zuerst geschrieben, damit bei einem Abbruch nachvollziehbar
bleibt, was noch offen ist. Er wird während des Laufs nicht stillschweigend gekürzt.

### Phase 1 — Vollständiges Lesen, quellenweise

Pro Quelle **ein eigener Durchgang mit frischem Kontext**:

1. Quelle vollständig lesen.
2. Extrakt nach dem Schema unten erstellen.
3. Extrakt wegschreiben, **bevor** die nächste Quelle beginnt.

Warum getrennte Durchgänge: Wird alles in einem einzigen langen Durchgang gelesen,
wächst der Kontext mit jeder Quelle, und jeder weitere Schritt liest den gesamten
bisherigen Kontext erneut mit. Getrennte Durchgänge lesen **genauso vollständig**,
kosten aber einen Bruchteil. Die Tiefe bleibt, der Ballast fällt weg.

### Phase 2 — Zusammenführen

1. Nur die **Extrakte** laden — nicht das Rohmaterial.
2. Doppeltes zusammenführen.
3. Widersprüche zwischen Quellen ausdrücklich markieren, nicht stillschweigend auflösen.
4. Ergebnis ins Second Brain einsortieren.

### Phase 3 — Protokoll

`laufprotokoll.md` fortschreiben: Datum, Umfang, gelesene Quellen, Kernfunde,
offene Punkte, und ob der Lauf vollständig war.

## Extraktschema

Je Quelle festhalten:

- **Entscheidungen** — was wurde entschieden, warum, von wem
- **Fakten und Zahlen** — jeweils mit Herkunft
- **Offene Punkte** — Zusagen, Termine, Unerledigtes
- **Wiederkehrende Themen** — was mehrfach auftaucht
- **Wörtliche Zitate** — dort, wo die genaue Formulierung zählt
- **Bewusst aussortiert** — kurz, was gelesen und als unwichtig eingestuft wurde

Der letzte Punkt ist kein Beiwerk: Er ist der Nachweis, dass tatsächlich
vollständig gelesen wurde und nicht nur der Anfang.

## Qualitätsregeln

- Vollständiges Lesen ist Pflicht, nicht Ermessen.
- Nichts erfinden. Unklares wird als unklar markiert, nicht geglättet.
- Im Zweifel ein Extrakt zu viel als eine übersehene Entscheidung.
- Lücken werden benannt, nicht kaschiert. Ein ehrlich unvollständiger Lauf ist
  brauchbar; ein scheinbar vollständiger ist es nicht.

## Warum wöchentlich statt täglich

Die Kosten eines Laufs steigen vor allem mit seiner **Länge**, nicht mit seiner
Anzahl — in einer langen Session entfallen 80–90 % der Token darauf, den bereits
gelesenen Kontext bei jedem Schritt erneut mitzulesen.

Daraus folgt der Zuschnitt hier:

- **Häufigkeit runter** (täglich → wöchentlich) spart etwa sechs Siebtel.
- **Tiefe bleibt oben**, weil Phase 1 quellenweise mit frischem Kontext arbeitet
  und die Länge des einzelnen Durchgangs damit begrenzt bleibt.

Beides zusammen ergibt: gründlicher als vorher, und trotzdem deutlich günstiger.
