# Alltags- und Lebensplaner — Projektplan

Stand: 2026-08-22 · Projektleitersicht
**Zeitliche Einordnung:** startet, wenn *Aktenkrake* läuft. Bis dahin: planen, nicht bauen.
**Lebensdauer:** **[E]** Kein Drei-Jahres-Projekt. Es soll dauerhaft laufen und gepflegt
werden. Wenn es funktioniert, wird es lange benutzt — danach richtet sich die Bauweise.

---

## 1. Die sechs Grundentscheidungen

### E1 · Nur für mich, oder für andere? — **[E] entschieden**
**Erst nur für mich. Später wäre eine Bereitstellung für andere schön.**

Konsequenz für die Bauweise:
- **Jetzt:** keine Fremdkonten, keine Store-Veröffentlichung, Haushaltsausnahme greift
- **Aber:** das Datenmodell wird von Anfang an **profilfähig** gebaut (siehe E6),
  damit der Schritt später möglich ist, ohne alles neu zu schreiben
- Was **nicht** vorgebaut wird: Bezahlung, Support, Mehrbenutzer-Rechte. Das kostet
  jetzt nur Zeit und ist später nachrüstbar, wenn das Fundament stimmt

### E2 · Ersetzen oder anbinden? — **[E] entschieden**
**Ersatz.** Mit den bisherigen Kalendern kam es nie klar.
**Zusätzlich eine Anbindung für den Fall der Fälle** — importieren und exportieren
können, ohne davon abhängig zu sein.

### E3 · Welche Geräte? — **[E] entschieden**
**Alle drei: Handy, Tablet, Rechner.** Keine Einschränkung auf ein Gerät.

**[E] Kein Apple.** Zielplattformen sind **Android** (Handy und Tablet) und **Windows**.
Das streicht die Apple-Gebühren, das App-Store-Verfahren und ausgerechnet die
strengsten Benachrichtigungs-Beschränkungen.
→ Zwingt zu einer Technologie, die alle drei aus einer Codebasis bedient.
→ Zwingt Synchronisation früher in den Plan als ursprünglich vorgesehen.

### E4 · Zeitbudget — **[E] entschieden**
**5 Stunden pro Woche oder mehr**, sobald Aktenkrake läuft.
Aktenkrake hat bis dahin Vorrang. Rechnung dazu in Abschnitt 7.

### E5 · Was ist die kleinste nützliche Version? — **[E] angepasst**
Ursprünglich „nur Handy" — verworfen.

**MVP:** Kalender (Woche) + To-do-Liste mit Eskalation + Benachrichtigungen mit Aktionen
+ Widget — **auf allen drei Geräten, mit einem gemeinsamen Profil.**
Ohne Fachmodule (T7–T9), ohne KI.

### E6 · Wo liegen die Daten? — **[E] Richtung entschieden: Profil**
Das Profil ist das tragende Konzept:

- Ein **Profil** enthält alle persönlichen Daten — Kalender, To-dos, Memos, Vorräte
- Es wird auf jedem Gerät **geladen** und dort **abgeglichen**
- Profile lassen sich **zusammenführen**
- Auf Handy, Tablet und Rechner ist es dasselbe Profil

Konsequenz: Es braucht eine Ablage außerhalb des einzelnen Geräts.
Da Gesundheitsdaten enthalten sind (Medikamente): **verschlüsselt ablegen**, auch
solange nur eine Person es benutzt.

---

## 2. Blinde Flecken und ihr Stand

### B1 · Medikamentendaten sind Gesundheitsdaten — **entschärft, aber nicht erledigt**
Solange rein privat genutzt: Haushaltsausnahme, unkritisch.
Da laut E1 eine spätere Bereitstellung gewünscht ist, gilt trotzdem ab sofort:
**verschlüsselte Ablage, Löschmöglichkeit, keine unnötige Datensammlung.**
Das kostet jetzt fast nichts und spart später die komplette Nachrüstung.

### B2 · Benachrichtigungen — **Anforderung präzisiert**
**[E]** Es reicht, wenn die Benachrichtigung auf **einem** Gerät ankommt —
Handy oder Tablet. Der Rechner (Windows) hat ebenfalls Benachrichtigungen.

**[E]** Die Benachrichtigung braucht **Aktionen direkt darin**:
- **Schlummern / verschieben**
- **Erledigt**
- mit Bild / Symbol

**Risiko deutlich gesunken**, seit Apple entfällt:
- **Android** erlaubt exakte Alarme mit einer eigenen Berechtigung; Doze-Modus und
  Batterieoptimierung bleiben zu beachten, sind aber lösbar
- **Windows** hat Benachrichtigungen mit Schaltflächen und Bild — unkompliziert

Offen bleibt die **Windows-Entsprechung zum Widget**: Ein Startbildschirm-Widget wie
auf Android gibt es dort nicht in gleicher Form. Realistisch wird es ein kleines,
immer sichtbares Fenster oder ein Eintrag im Infobereich. Wird in S3 geklärt.

### B3 · Wiederholungsregeln und Zeitumstellung — **[E] Standard verwenden**
RFC 5545 / RRULE plus erprobte Bibliothek. Nicht selbst erfinden.

### B4 · Die Uhr muss testbar sein — **[E] gilt**
Zeit von außen setzbar („tu so, als wäre in 4 Tagen"). Ab Phase 1, nicht später.

### B5 · Synchronisation — **Risiko neu bewertet**
Einwand aus der Praxis, und er ist berechtigt: Es ist **ein** Nutzer mit **einem**
Profil. Dass zwei Geräte gleichzeitig offline denselben Eintrag ändern, ist
äußerst unwahrscheinlich. Google Kalender und Google Tasks lösen genau das seit Jahren
unauffällig.

**Neue Bewertung:** Kein CRDT-Aufwand nötig. Es genügt:
- **Feldweise „letzte Änderung gewinnt"** mit Zeitstempel
- **Änderungsprotokoll**, damit nachvollziehbar bleibt, was passiert ist
- **Papierkorb statt echtem Löschen** — nichts verschwindet unwiederbringlich

Damit sinkt R2 von *kritisch* auf *beherrschbar*. Bleibt wichtig: **Backup**, weil
das eigentliche Verlustrisiko nicht der Konflikt ist, sondern ein verlorenes Gerät
oder ein Fehler beim Abgleich.

### B6 · Export und Backup — **[E] Pflicht**
Das Ding soll dauerhaft laufen. Also: Export in ein offenes Format, automatisches
Backup, und die Möglichkeit, das Profil komplett mitzunehmen.

### B7 · Umzug der Bestandsdaten
Import aus dem bisherigen Kalender, den Kontakten (Geburtstage) und der
Medikamenten-Excel. Ohne Import wird die App nicht in Betrieb genommen.

### B8 · Fremdsysteme sind nicht garantiert
Abfuhrkalender Magdeburg · Bahnverbindungen · Karten für Wegzeiten.
Alle drei ungeprüft. **Kein Fachmodul darf zur Voraussetzung werden.**

### B9 · Laufende Kosten
| Posten | Größenordnung |
|---|---|
| ~~Apple Developer Program~~ | **entfällt** — kein Apple |
| Google Play | ~25 $ einmalig, nur bei Veröffentlichung |
| Server für das Profil | monatlich, gering bei einem Nutzer |
| Karten-API | pro Abfrage, Freikontingent begrenzt |

### B10 · Das Projekt als Ersatzhandlung
**Gegenmaßnahme (Tor 2), zur Klarstellung:**
Wenn die erste brauchbare Version läuft, wird sie **drei Wochen im echten Alltag
benutzt, ohne dass am Code gearbeitet wird.** Erst danach wird entschieden, was
als Nächstes gebaut wird — und zwar aus dem, was in diesen drei Wochen wirklich
gefehlt hat. Ohne diese Pause entstehen Funktionen nach Bauchgefühl statt nach Bedarf,
und das Projekt wird nie fertig.

**[E]** Während der Testphase wird eine **Backlog-Liste** geführt. Kritisches wird sofort
repariert, alles andere gesammelt. Am Ende der drei bis vier Wochen wird die Liste
durchgesehen — erfahrungsgemäß fällt dabei die Hälfte weg, weil sie sich im Alltag
als unwichtig herausgestellt hat.

---

## 3. Phasenplan mit Toren

### Phase 0 · Entscheiden und prüfen (2–4 Wochen)
Offen ist nur noch **E4**. Dazu sechs Machbarkeitsprüfungen:

| | Prüfung | klärt |
|---|---|---|
| S1 | Erinnerung feuert zuverlässig nach 3 Tagen Ruhe (Android + Windows) | B2 |
| S2 | Benachrichtigung mit Aktionen „Schlummern / Erledigt" auf Android und Windows | B2 |
| S3 | Android-Widget aktualisiert sich mehrfach täglich; Windows-Entsprechung klären | B2 |
| S4 | Profil laden und abgleichen über drei Geräte | E6/B5 |
| S5 | Wiederholung mit Ausnahme über die Zeitumstellung | B3 |
| S6 | Abfuhrkalender Magdeburg maschinell lesbar? Kosten Wegzeit-Abfrage? | B8/B9 |

Zusätzlich: **Technologiewahl** — eine Codebasis für Handy, Tablet, Rechner.

**Tor 0:** E4 beantwortet, S1–S6 geklärt, Technologie festgelegt.

### Phase 1 · Skelett (6–10 Wochen)
T1 Datenmodell (profilfähig) · T2 Kategorien und Typen · lokale Ablage · eine Ansicht ·
setzbare Uhr · Papierkorb.
**Tor 1:** Termin und To-do anlegen, anzeigen, abhaken — auf einem Gerät.

### Phase 2 · MVP (4–6 Monate)
T3 Eskalation · T4 Visuelles System · T5 Ansichten · T6 Widgets ·
Benachrichtigungen mit Aktionen · **Profil-Abgleich über alle drei Geräte** ·
Import und Export.

Der Sync ist gegenüber der ersten Planung vorgezogen, weil E3 alle drei Geräte fordert.
Das verlängert Phase 2, spart aber eine spätere Umbauphase.

**Tor 2:** **Drei bis vier Wochen tägliche Eigennutzung ohne Weiterentwicklung.**

**[E]** Ausnahme: **kritische Fehler werden sofort behoben.** Alles andere —
jeder Wunsch, jede Idee, jedes Ärgernis — wandert in eine **Backlog-Liste** und wird
erst am Ende der Testphase bewertet und priorisiert.

### Phase 3 · Fachmodule (3–6 Monate)
T7 Zeit und Wege · T8 Vorräte und Gesundheit (inkl. Druckliste EU-Standard) ·
T9 Haushalt und Wiederkehrendes. Einzeln, nacheinander, jedes für sich nutzbar.

### Phase 4 · KI
T11. Erinnern und Erfassen per Sprachmodell.

### Dauerbetrieb
Da es dauerhaft laufen soll: feste Pflege einplanen — Systemaktualisierungen,
Bibliotheken, Backups prüfen. Etwa ein halber Tag im Quartal.

---

## 4. Damit es kein Billig-Tool wird

1. **Kein Datenverlust. Nie.** Papierkorb, Backup, Änderungsprotokoll.
2. **Offline voll funktionsfähig.** Netz ist Zusatz.
3. **Start unter 1 Sekunde.**
4. **Export jederzeit**, offenes Format.
5. **Keine Funktion ohne Test der Zeitlogik.**
6. **Barrierefreiheit ist Abnahmekriterium** — Doppelkodierung, Kontraste, keine Animationen.
7. **Jede Entscheidung wird aufgeschrieben** (Was, Warum, Alternativen).
8. **Ein Teilprojekt zur Zeit.**
9. **Fehlermeldungen in Klartext.**
10. **Keine Zusatzfunktion, solange eine Grundfunktion wackelt.**

---

## 5. Risikoregister

| # | Risiko | Stand | Gegenmaßnahme |
|---|---|---|---|
| R1 | Benachrichtigungen unzuverlässig | **mittel** (war hoch) | Apple entfällt; S1–S3 in Phase 0; ein Gerät genügt |
| R2 | Sync verliert Daten | **mittel** (war hoch) | letzte Änderung gewinnt + Papierkorb + Backup |
| R3 | Umfang wächst unkontrolliert | **hoch** | feste Tore, ein Teilprojekt |
| R4 | Projekt wird Ersatzhandlung | **hoch** | Tor 2: drei Wochen nur nutzen |
| R5 | Wiederholungsregeln falsch | mittel | Standard + Bibliothek |
| R6 | Fremd-API fällt weg | niedrig | Module optional halten |
| R7 | Gesundheitsdaten rechtlich | **niedrig, solange privat** | verschlüsselt ablegen, E1 im Blick |
| R8 | Motivation bricht ein | mittel | kleine Tore, früh nutzbar |
| R9 | Drei Plattformen ab MVP | **neu, mittel** | eine Codebasis, Technologiewahl in Phase 0 |

---

## 6. Zeitrechnung bei 5 Stunden pro Woche

Ehrliche Hochrechnung, damit später keine Enttäuschung entsteht.
5 Stunden pro Woche sind rund **22 Stunden im Monat**.

| Phase | Aufwand | Dauer bei 5 h/Woche |
|---|---|---|
| Phase 0 · Entscheiden und prüfen | 20–30 h | 1–1,5 Monate |
| Phase 1 · Skelett | 80–120 h | 4–5 Monate |
| Phase 2 · MVP inkl. Profil-Abgleich | 250–400 h | 12–18 Monate |
| Phase 3 · Fachmodule | 150–250 h | 7–11 Monate |
| Phase 4 · KI | 40–80 h | 2–4 Monate |

**Bis zum benutzbaren MVP: rund 1,5 bis 2 Jahre.**
**Voller Ausbau: 3 Jahre und mehr.**

### Warum das trotzdem in Ordnung sein kann
Diese Zahlen gelten für klassische Handarbeit. Wird der Code weitgehend KI-gestützt
geschrieben, verschiebt sich der Engpass: Deine 5 Stunden gehen dann nicht ins Tippen,
sondern ins **Entscheiden, Prüfen und Ausprobieren**. Realistisch liegt der
Beschleunigungsfaktor bei zwei bis drei — damit wird aus 1,5–2 Jahren bis zum MVP
eher **8 bis 12 Monate**.

Diese Beschleunigung gilt aber **nur**, wenn die Entscheidungen vorher stehen.
Genau dafür ist die jetzige Planungsphase da.

### Drei Stellschrauben, falls es zu lang wird
1. **Weniger Plattformen im MVP** — Rechner später nachziehen spart geschätzt 3–4 Monate
2. **Profil-Abgleich später** — spart 3–5 Monate, kostet aber einen Umbau
3. **Mehr Stunden** — jede zusätzliche Stunde pro Woche verkürzt spürbar

**Empfehlung:** nichts davon vorab ändern. Nach Tor 1 neu bewerten, dann sind die
Zahlen belastbar statt geschätzt.

---

## 7. Technologievorschlag

Anforderungen, die die Wahl bestimmen: **Handy + Tablet + Windows aus einer Codebasis**,
**Widgets auf dem Startbildschirm**, **Benachrichtigungen mit Aktionen**,
**offline voll funktionsfähig**, **verschlüsselte Profilablage**.

### Oberfläche: Flutter
| Kandidat | Bewertung |
|---|---|
| **Flutter** | **Empfehlung.** Deckt Android und Windows aus einer Codebasis. Ausgereifte Bibliotheken für Benachrichtigungen und Widgets. |
| React Native | Auf dem Handy stark, unter Windows schwach. |
| .NET MAUI | Unter Windows stark, kleineres Ökosystem. |
| Web / PWA / Electron | **Ungeeignet.** Startbildschirm-Widgets praktisch unmöglich, Benachrichtigungen schwach — trifft genau deinen Kernbedarf nicht. |

**Einschränkung, die für jede Wahl gilt:** Startbildschirm-Widgets sind pro System
immer etwas Eigenes. Ein kleiner nativer Anteil bleibt — jetzt aber nur noch für
Android und Windows statt für drei Systeme.

### Ablage und Abgleich: PocketBase oder Supabase
- **PocketBase** — eine einzige Programmdatei, sehr einfach zu betreiben, ideal für ein Profil
- **Supabase** — mehr Möglichkeiten, auch gemietet nutzbar, für spätere Bereitstellung an andere besser gerüstet

**Empfehlung:** **PocketBase** für den Eigenbedarf. Wenn E1 später Richtung „auch für
andere" kippt, ist der Wechsel auf Supabase überschaubar, sofern das Datenmodell sauber ist.

### Lokale Ablage
SQLite auf jedem Gerät. Die App arbeitet immer lokal, der Abgleich läuft im Hintergrund.
Damit ist die Offline-Anforderung baulich erfüllt statt nachträglich angeflanscht.

---

## 8. Offen

- Windows-Entsprechung zum Widget (S3 in Phase 0)
- Technologiewahl endgültig bestätigen (Phase 0)
- Typenliste für die Symbole (T2)

**Damit sind alle Grundentscheidungen E1–E6 getroffen.**
Nächster inhaltlicher Schritt: **T2 — Kategorien- und Typenliste.**
