# Alltags- und Lebensplaner — Projektplan

Stand: 2026-08-22 · Erstellt aus Projektleitersicht
**Zeitliche Einordnung:** startet, wenn *Aktenkrake* läuft. Bis dahin: planen, nicht bauen.

Zweck dieses Dokuments: die Dinge festhalten, die im Brainstorming **nicht** vorkamen
und die darüber entscheiden, ob daraus ein tragfähiges Werkzeug wird oder ein Billig-Tool.

---

## 1. Sechs Entscheidungen, die VOR T1 fallen müssen

Ohne diese sechs Antworten ist jede weitere Planung Spekulation.
Sie kosten je 5 Minuten Nachdenken und sparen später Monate.

### E1 · Nur für mich, oder für andere?
Das ist die folgenschwerste Frage im ganzen Projekt.

| | nur für mich | auch für andere |
|---|---|---|
| Konten / Login | nicht nötig | Pflicht |
| DSGVO | **Haushaltsausnahme greift** | volle Pflicht, inkl. Gesundheitsdaten |
| App Stores | nicht nötig | Apple + Google, Review-Prozesse |
| Support / Updates | wenn ich Lust habe | dauerhaft, verbindlich |
| Aufwand | ×1 | ×3 bis ×5 |

**Empfehlung:** Erst für dich bauen. Der Schritt zum Produkt ist später möglich,
wenn das Datenmodell sauber ist. Umgekehrt geht es nicht.

### E2 · Ersetzt es deinen bestehenden Kalender, oder arbeitet es mit ihm?
Arbeitstermine liegen vermutlich schon irgendwo (Outlook/Google).
Ein Planer, der die nicht sieht, ist wertlos.

- **Ersetzen** — sauberer, aber du musst alles umziehen und Kollegen erreichen dich nicht mehr über den Kalender
- **Anbinden** — realistischer, aber Zweiwege-Sync ist technisch anspruchsvoll
- **Nur lesen** — fremde Termine erscheinen, sind aber nicht bearbeitbar. Guter Kompromiss.

**Empfehlung:** Nur lesen im ersten Schritt.

### E3 · Welches Gerät zuerst?
Alles gleichzeitig ist der sicherste Weg, nie fertig zu werden.

**Empfehlung:** **Handy zuerst.** Dort sitzt dein Kernbedarf („genervt werden", Widget,
Startbildschirm). Tablet läuft mit derselben App. Rechner als Letztes.

### E4 · Wer baut es, in welcher Zeit?
Noch nicht beantwortet. Realistische Größenordnung für eine Person mit KI-Unterstützung:

| Umfang | Aufwand |
|---|---|
| Skelett auf einem Gerät | 4–8 Wochen |
| MVP mit Eskalation + Widget | 3–5 Monate |
| + Synchronisation über 3 Geräte | + 2–4 Monate |
| + alle Fachmodule (T7–T9) | + 3–6 Monate |

Das ist kein Wochenendprojekt. Wenn diese Zahlen nicht passen, muss der Umfang schrumpfen —
nicht die Qualität.

### E5 · Was ist die kleinste Version, die dir schon hilft?
Ohne diese Definition wird nie etwas fertig.

**Vorschlag MVP:** Kalender (Woche) + To-do-Liste mit Eskalation + Heute-Widget.
Auf dem Handy. Ohne Sync, ohne Module, ohne KI.
Wenn das drei Wochen lang deinen Alltag verbessert, ist der Rest gerechtfertigt.

### E6 · Wo liegen die Daten?
- **Nur auf dem Gerät** — maximal privat, kein Sync, kein Backup
- **Eigener Server** — volle Kontrolle, dauerhafte Kosten und Pflege
- **Fertiger Dienst** (Firebase o. ä.) — schnell, aber Gesundheitsdaten bei Dritten

**Empfehlung:** lokal-zuerst, mit verschlüsseltem Abgleich. Die App muss ohne Netz voll funktionieren.

---

## 2. Blinde Flecken im bisherigen Konzept

Was bisher nirgends vorkam, aber das Projekt zum Kippen bringen kann.

### B1 · Medikamentendaten sind Gesundheitsdaten
Nach DSGVO **besondere Kategorie** (Art. 9). Solange du es rein privat für dich nutzt,
greift die Haushaltsausnahme und es ist unkritisch. **Sobald es andere nutzen**, brauchst du:
Rechtsgrundlage, Verschlüsselung, Löschkonzept, Datenschutzerklärung, Auftragsverarbeitungsverträge.

→ Hängt direkt an **E1**. Nicht später „mal eben" nachrüstbar.

### B2 · Benachrichtigungen sind das größte technische Risiko
Dein Kernbedarf ist „ich muss genervt werden". Genau das bekämpfen die Betriebssysteme:

- Android: Doze-Modus, App-Standby, exakte Alarme brauchen eine eigene Berechtigung
- iOS: begrenzte Hintergrundausführung, geplante Benachrichtigungen sind limitiert
- Widgets: feste Aktualisierungsbudgets, keine Sekundengenauigkeit

**Das muss in Woche 1 geprüft werden, nicht in Monat 8.** Wenn eine Erinnerung nach drei
Tagen Ruhe nicht zuverlässig kommt, ist die Grundidee betroffen.

### B3 · Wiederholungsregeln und Sommerzeit
Der klassische Killer jeder Kalender-App. „Jeden 2. Dienstag, außer dieser eine wurde
verschoben, über die Zeitumstellung hinweg" — daran scheitern reihenweise Projekte.

**Regel: nicht selbst erfinden.** Den Standard verwenden (RFC 5545 / RRULE) und eine
erprobte Bibliothek. Alles andere kostet dich Monate und produziert falsche Termine.

### B4 · Die Uhr muss testbar sein
Du kannst nicht drei Tage warten, um zu prüfen, ob etwas orange wird.
Die Zeit muss von Anfang an von außen setzbar sein („tu so, als wäre in 4 Tagen").
Wird das nachträglich eingebaut, ist die halbe Eskalations-Logik neu zu schreiben.

### B5 · Synchronisation ist kein Häkchen, sondern ein Teilprojekt
Zwei Geräte, beide offline, beide ändern denselben Eintrag. Wer gewinnt?
Wenn das schlecht gelöst ist, verlierst du Daten — und danach das Vertrauen in die App.
Das ist der Punkt, an dem Werkzeuge zu „Billig-Tools" werden.

### B6 · Export und Backup
Die App hält dann deinen Alltag, deine Medikamente, deine Termine.
- **Export** in ein offenes Format, jederzeit
- **Automatisches Backup**
- Was passiert, wenn du das Projekt in zwei Jahren nicht mehr weiterentwickelst?

Ohne Ausweg ist es eine Falle, kein Werkzeug.

### B7 · Umzug der Bestandsdaten
Du hast schon Daten: Kalender, Geburtstage in den Kontakten, Medikamente in Excel.
Ohne Import beginnst du bei null — und benutzt die App deshalb nicht.

### B8 · Fremdsysteme sind nicht garantiert
- **Abfuhrkalender Magdeburg** — ob maschinell lesbar (ICS/API), ist ungeprüft. Notfalls PDF oder manuell.
- **Bahnverbindungen** — API-Zugang und Bedingungen ungeprüft
- **Karten für Wegzeiten** — kostet ab Volumen Geld

Jede dieser drei Funktionen kann wegfallen. Das Konzept darf nicht davon abhängen.

### B9 · Laufende Kosten
Bisher nirgends erwähnt:

| Posten | Größenordnung |
|---|---|
| Apple Developer Program | ~99 $ / Jahr (nur bei Veröffentlichung) |
| Google Play | ~25 $ einmalig |
| Server / Sync | monatlich, falls eigener Server |
| Karten-API | pro Abfrage, Freikontingent begrenzt |

### B10 · Das Projekt als Ersatzhandlung
Ehrlich benannt, weil es die realistischste Gefahr ist: An einem Planungsprojekt zu
arbeiten fühlt sich produktiv an und ersetzt das Planen des eigenen Alltags.

**Gegenmaßnahme:** Nach dem MVP drei Wochen **nur benutzen, nicht entwickeln.**
Was dich dann noch stört, wird gebaut. Der Rest fällt weg.

---

## 3. Phasenplan mit Toren

Ein Tor wird nur passiert, wenn das Ergebnis vorliegt. Kein Vorgriff.

### Phase 0 · Entscheiden und prüfen (2–4 Wochen)
Antworten auf E1–E6, plus sechs kleine Machbarkeitsprüfungen:

| | Prüfung | Beantwortet |
|---|---|---|
| S1 | Erinnerung feuert zuverlässig nach 3 Tagen Ruhe (Android + iOS) | B2 |
| S2 | Widget aktualisiert sich mehrfach täglich | B2 |
| S3 | Zwei Geräte offline, gleicher Eintrag geändert — was passiert? | B5 |
| S4 | Wiederholung mit Ausnahme über die Zeitumstellung | B3 |
| S5 | Abfuhrkalender Magdeburg maschinell lesbar? | B8 |
| S6 | Kosten einer Wegzeit-Abfrage | B8/B9 |

**Tor 0:** Alle sechs beantwortet, E1–E6 entschieden.

### Phase 1 · Skelett (4–8 Wochen)
T1 Datenmodell · T2 Kategorien/Typen · lokale Speicherung · eine Ansicht · setzbare Uhr.
**Tor 1:** Ein Termin und ein To-do lassen sich anlegen, anzeigen, abhaken — auf einem Gerät.

### Phase 2 · MVP (3–5 Monate)
T3 Eskalation · T4 Visuelles System · T5 Ansichten · T6 Widget · Benachrichtigungen · Export.
**Tor 2:** **Drei Wochen tägliche Eigennutzung ohne Weiterentwicklung.**
Erst danach geht es weiter.

### Phase 3 · Synchronisation (2–4 Monate)
T10. Zweites Gerät.
**Tor 3:** Abhaken, Benachrichtigung, Timer — auf allen Geräten gleich, auch nach Offline-Phasen.

### Phase 4 · Fachmodule (3–6 Monate)
T7 Zeit/Wege · T8 Vorräte/Gesundheit · T9 Haushalt/Wiederkehrendes.
Einzeln, nacheinander, jedes für sich nutzbar.

### Phase 5 · KI
T11. Zuletzt, weil es ohne die anderen Teile keinen Nutzen hat.

---

## 4. Damit es kein Billig-Tool wird

Nicht verhandelbare Qualitätsregeln. Sie gelten ab Phase 1.

1. **Kein Datenverlust. Nie.** Wichtiger als jede Funktion.
2. **Offline voll funktionsfähig.** Netz ist Zusatz, nicht Voraussetzung.
3. **Start unter 1 Sekunde.** Ein träger Planer wird nicht benutzt.
4. **Export jederzeit möglich**, in einem offenen Format.
5. **Keine Funktion ohne Test der Zeitlogik.**
6. **Barrierefreiheit ist Abnahmekriterium, kein Extra** — Doppelkodierung, Kontraste, keine Animationen.
7. **Jede Entscheidung wird aufgeschrieben** (kurzer Eintrag: Was, Warum, Alternativen).
   Sonst wird in Monat 6 alles neu diskutiert.
8. **Ein Teilprojekt zur Zeit.** Fertig heißt aufgeschrieben und benutzbar.
9. **Fehlermeldungen in Klartext**, nie technische Kürzel.
10. **Keine Funktion, die nur „nice to have" ist**, solange eine Grundfunktion wackelt.

---

## 5. Risikoregister

| # | Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|---|
| R1 | Benachrichtigungen unzuverlässig | Kernnutzen weg | S1/S2 in Phase 0 |
| R2 | Sync verliert Daten | Vertrauen weg, Projekt tot | S3, lokal-zuerst, Backup |
| R3 | Umfang wächst unkontrolliert | nie fertig | feste Tore, ein Teilprojekt |
| R4 | Projekt wird Ersatzhandlung | Alltag unverändert | Tor 2: 3 Wochen nur nutzen |
| R5 | Wiederholungsregeln falsch | falsche Termine, Vertrauensverlust | Standard + Bibliothek |
| R6 | Fremd-API fällt weg | Funktion entfällt | Modul optional halten |
| R7 | Gesundheitsdaten rechtlich | rechtliches Problem | E1 klären, lokal halten |
| R8 | Motivation bricht ein | Stillstand | kleine Tore, früh nutzbar |

---

## 6. Was ich von dir brauche

In dieser Reihenfolge:

1. **E1** — nur für dich, oder später auch für andere?
2. **E2** — ersetzen, anbinden oder nur lesen?
3. **E4** — wieviel Zeit realistisch pro Woche?
4. **E5** — ist der MVP-Vorschlag (Kalender + To-do + Eskalation + Widget, nur Handy) für dich brauchbar?

E3 und E6 kann ich dir vorschlagen, sobald 1–4 stehen.
