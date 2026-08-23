# Alltags- und Lebensplaner — Projektaufteilung

Stand: 2026-08-22

Das Projekt ist zu groß für einen Durchgang. Aufgeteilt in **9 Teilprojekte**,
jedes für sich abschließbar. Reihenfolge unten.

---

## Gruppe 1 — Fundament

Muss zuerst stehen. Alles andere baut darauf auf.

### T1 · Datenmodell
Was für Dinge gibt es überhaupt, und welche Felder haben sie?

- Objekttypen festlegen: **Termin · Vorhaben · Memo · Vorrat · Arbeitszeit**
- Felder je Typ
- Wie hängen sie zusammen (Memo klebt an Termin, Vorhaben wird zu Termin)
- Übergänge: wann wird aus einem Memo ein Vorhaben?

**Ergebnis:** eine Liste von Objekten mit ihren Feldern.
**Blockiert:** alles.

### T2 · Kategorien und Typen
Die zwei Ebenen aus dem Farbkonzept endgültig festlegen.

- **Kategorienliste** (= Farben): privat, beruflich, Geburtstag, Haushalt, Medikamente, Deadline, Hobby/Freizeit — vollständig?
- **Typenliste** (= Symbole): telefonischer Gesprächstermin, Abarbeitungstermin, … — *muss noch erarbeitet werden*

**Ergebnis:** zwei fertige Listen.
**Blockiert:** T3, T4.

---

## Gruppe 2 — Regeln und Aussehen

### T3 · Dringlichkeits-Engine
Die Logik, die von allein hochzählt.

- Die drei Kurventypen: Verderb · Deadline · Vorsatz
- **Tempo** und **Deckel** je Eintrag
- Zurücksetzen beim Erledigen
- Vorlagen mit Standardwerten (Müll 3–4 Tage, Eier per Datum, Buch manuell)
- Entscheidung bei Rot: terminieren / abgeben / verschieben
- Einfrieren (Urlaub, Krankheit)

**Ergebnis:** eine beschriebene Rechenregel, ohne Oberfläche.
**Braucht:** T1.

### T4 · Visuelles System
Das Aussehen, einmal festgelegt und dann überall gleich.

- Farbpalette: gedämpfte Grundtöne + einige kräftige, kontrastreiche
- Symbolbibliothek
- Doppelkodierung: Sortierung + Zahl + Form, nie Farbe allein
- Bausteine: Listenzeile (Streifen links, Dringlichkeit rechts), Kalendereintrag, Balken

**Ergebnis:** Farbwerte, Symbolsatz, drei bis vier Bausteine.
**Braucht:** T2.

---

## Gruppe 3 — Die Oberfläche

### T5 · Ansichten
- Kalender Monat / Woche
- To-do-Liste zum Abhaken
- Kurzliste „das Wichtigste heute"
- Balkendiagramm (abrufbar, nicht dauerhaft sichtbar)
- Drag & Drop auf Tage und Listen
- Erfassen in einem Feld, ohne Sortieren

**Braucht:** T1, T3, T4.

### T6 · Geräte und Widgets
Drei Geräte, drei Rollen.

- **Tablet** — hält den Tag präsent
- **Handy** — nervt, vor allem über Widgets auf dem Startbildschirm
- **Rechner** — verwalten und pflegen
- Welche Widgets es gibt und was sie zeigen

**Braucht:** T5.

---

## Gruppe 4 — Fachmodule

Jedes eigenständig, jedes einzeln nachrüstbar. Gute Stellen zum Anfangen,
weil jedes für sich schon nützlich ist.

### T7 · Zeit und Wege
- Terminhülle: Fertigmachen → Hinweg → Termin → Rückweg
- Verkehrsmittel **wählbar**, nicht automatisch
- Bahnverbindung übernehmen
- Arbeitszeit-Zähler pro Tag und Woche, Arbeit und Privat getrennt gezählt

### T8 · Vorräte und Gesundheit
- Medikamenten-Countdown aus Verbrauch und Vorlaufzeit
- Alarm als Kalendertermin, nicht als Notification
- Medikamentenliste drucken, EU-Standard
- Gleiches Prinzip für Kaffee, Waschmittel usw.

### T9 · Haushalt und wiederkehrende Termine
- Takt „alle X Tage", Zähler startet beim Erledigen neu
- Müllabfuhr-Kopplung (Magdeburg: MagdeApp / Abfuhrkalender), raus **vor** der Abfuhr
- Geburtstage zweistufig: Geschenk 14 Tage vorher, Anruf am Tag

---

## Gruppe 5 — Technik

### T10 · Plattform und Synchronisation
- Eine Codebasis für PC, Tablet, Handy
- **Sync:** Abhaken, bestätigte Benachrichtigungen, gestoppte Timer — überall gleich
- Benachrichtigungen auf allen Geräten
- Offline-Verhalten

### T11 · KI / Sprachmodell
- Erinnern per Sprachmodell
- Erfassen per Sprache
- Wo die KI eingreift und wo ausdrücklich nicht

---

## Reihenfolge

```
T1 Datenmodell
 └─ T2 Kategorien + Typen
     ├─ T3 Dringlichkeits-Engine
     └─ T4 Visuelles System
         └─ T5 Ansichten
             └─ T6 Geräte + Widgets

T7 / T8 / T9  ← unabhängig, jederzeit einschiebbar
T10 / T11     ← zuletzt, brauchen eine laufende Oberfläche
```

**Vorschlag zum Anfangen:** T2 (Kategorien- und Typenliste).
Klein, abgeschlossen, und es ist ohnehin der letzte offene Punkt aus den Notizen.

**Faustregel:** immer nur *ein* Teilprojekt offen. Fertig heißt aufgeschrieben, nicht „im Kopf".
