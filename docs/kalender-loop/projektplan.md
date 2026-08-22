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

### E3 · Welches Gerät zuerst? — **[E] entschieden**
**Alle drei: Handy, Tablet, Rechner.** Keine Einschränkung auf ein Gerät.
→ Zwingt zu einer Technologie, die alle drei aus einer Codebasis bedient.
→ Zwingt Synchronisation früher in den Plan als ursprünglich vorgesehen.

### E4 · Zeitbudget — **[?] offen**
Gemeint ist: **wieviele Stunden pro Woche** realistisch in die Entwicklung fließen.
Nur zur Terminrechnung — 5 Stunden gegen 20 Stunden ist der Unterschied zwischen
etwa 8 Monaten und etwa 2 Jahren bis zur vollen Ausbaustufe.

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

Das bleibt das größte technische Risiko (Doze-Modus, Batterieoptimierung,
Widget-Budgets) und wird in Phase 0 geprüft. Dass ein Gerät genügt, entschärft es
deutlich — fällt eines aus, greifen die anderen.

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
Ablage/Server für das Profil · Karten-API pro Abfrage · später ggf. Store-Gebühren.

### B10 · Das Projekt als Ersatzhandlung
**Gegenmaßnahme (Tor 2), zur Klarstellung:**
Wenn die erste brauchbare Version läuft, wird sie **drei Wochen im echten Alltag
benutzt, ohne dass am Code gearbeitet wird.** Erst danach wird entschieden, was
als Nächstes gebaut wird — und zwar aus dem, was in diesen drei Wochen wirklich
gefehlt hat. Ohne diese Pause entstehen Funktionen nach Bauchgefühl statt nach Bedarf,
und das Projekt wird nie fertig.

---

## 3. Phasenplan mit Toren

### Phase 0 · Entscheiden und prüfen (2–4 Wochen)
Offen ist nur noch **E4**. Dazu sechs Machbarkeitsprüfungen:

| | Prüfung | klärt |
|---|---|---|
| S1 | Erinnerung feuert zuverlässig nach 3 Tagen Ruhe (Android/iOS/Windows) | B2 |
| S2 | Benachrichtigung mit Aktionen „Schlummern / Erledigt" auf allen drei Systemen | B2 |
| S3 | Widget aktualisiert sich mehrfach täglich | B2 |
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

**Tor 2:** **Drei Wochen tägliche Eigennutzung ohne Weiterentwicklung.**

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
| R1 | Benachrichtigungen unzuverlässig | **hoch** | S1–S3 in Phase 0; ein Gerät genügt |
| R2 | Sync verliert Daten | **mittel** (war hoch) | letzte Änderung gewinnt + Papierkorb + Backup |
| R3 | Umfang wächst unkontrolliert | **hoch** | feste Tore, ein Teilprojekt |
| R4 | Projekt wird Ersatzhandlung | **hoch** | Tor 2: drei Wochen nur nutzen |
| R5 | Wiederholungsregeln falsch | mittel | Standard + Bibliothek |
| R6 | Fremd-API fällt weg | niedrig | Module optional halten |
| R7 | Gesundheitsdaten rechtlich | **niedrig, solange privat** | verschlüsselt ablegen, E1 im Blick |
| R8 | Motivation bricht ein | mittel | kleine Tore, früh nutzbar |
| R9 | Drei Plattformen ab MVP | **neu, mittel** | eine Codebasis, Technologiewahl in Phase 0 |

---

## 6. Offen

- **E4** — Stunden pro Woche
- Technologiewahl (nach E4, in Phase 0)
- Typenliste für die Symbole (T2)
