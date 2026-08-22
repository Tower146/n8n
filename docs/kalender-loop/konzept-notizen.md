# Alltags- und Lebensplaner — Brainstorming-Notizen

Stand: 2026-08-22 · Rohnotizen aus der Konzeptphase.
Status je Punkt: **[E]** entschieden · **[V]** Vorschlag, offen · **[?]** ungeklärt

---

## 1. Was es werden soll

**[E]** Kein To-do-Tool, sondern ein **Lebens- und Alltagsplaner**.
Termine, To-dos, Prioritäten, Medikamente, Arbeitszeiten, Haushalt — alles zusammen in *einer* App.

**[E]** Grundaufbau:
- Großer **Kalender**, umschaltbar Monat / Woche
- **To-do-Liste** separat daneben, zum Abhaken
- **Kurzliste** mit den wichtigsten Terminen und To-dos für den Blick auf einen Schlag
- Alles farblich, übersichtlich, mit Prioritäten

**[E]** Harte Anforderung: **darf nicht überfordern.** Zielgruppe zuerst ich selbst — Konzentrationsschwierigkeiten.

---

## 2. Nutzungskontext

### Arbeitsmodell
- Freie Zeiteinteilung, es zählt nur die **40-Stunden-Woche**
- Egal *wann*: nachts, früh, nachmittags
- Auch fragmentiert: arbeiten → privat → arbeiten → privat
- Sporadisch offline sein möglich, um Stunden zu strecken
- **[E] Kein 9-to-5-Raster.** Das bringt hier gar nichts.

### Die realen Probleme
1. Termine werden nicht eingehalten
2. Hausarbeit passiert unregelmäßig
3. Geburtstage / Feierlichkeiten werden vergessen
4. Arbeit und Privat lassen sich nicht künstlich trennen
5. Verbrauchsgüter (v. a. Medikamente) laufen leer, bevor bestellt wird

### Warum Termine konkret scheitern
**[E]** Vier verschiedene Ursachen, die aufeinander folgen:

1. **Ich vergesse sie ganz.**
2. **Ich habe sie im Kopf — bis zu dem Tag, an dem der Termin ist. Dann vergesse ich ihn.**
3. **Ich muss mich mit einem Termin beschäftigen, damit er sich einprägt.** Reines Eintragen reicht nicht.
4. **Losgehen fällt schwer** — die Überwindung zum Aufbrechen ist ein eigenes Problem, unabhängig vom Erinnern.

**[E]** Daraus folgt: Der Termin muss **vor Augen sein** und es muss eine **Beschäftigung** mit ihm geben, nicht nur eine Benachrichtigung. Genau dafür ist dieses Projekt da.

### Feste Rahmenbedingungen
- Auf Arbeit: feste Termine und Deadlines, nicht verhandelbar
- Privat: ebenfalls Termine, die eingehalten werden müssen
- Beides muss unter einen Hut, im selben Kalender
- Arbeitszeit splitten ist ausdrücklich in Ordnung

---

## 3. Datentypen

**[E]** Sortierregel — eine Frage, drei Schubladen:

| Frage | landet in |
|---|---|
| Hat es eine **Uhrzeit**? | Kalender |
| Habe ich es mir **vorgenommen**? | To-do / Vorhaben |
| Will ich es nur **aufbewahren**? | Memo |

**[E]** Trennlinie Vorhaben ↔ Memo: **Vorhaben hat einen Takt und steigt. Memo liegt einfach da.**
(Nicht mehr „eskaliert / eskaliert nicht" — das war die frühere, verworfene Fassung.)

**[E]** Verhalten:
- **Termine eskalieren nicht.** Stehen fest, Ende der Diskussion.
- **To-dos eskalieren.** Sie wachsen, solange sie liegen bleiben.

**[E]** Haushalt und persönliche Vorsätze sind **derselbe Datentyp**: ein Takt („alle X Tage"), der beim Erledigen zurückgesetzt wird. Unterschied nur in Farbe und Deckel.

### Memo-Ebene
**[V]** Memos nörgeln nicht — sie warten. Das ist der Ort für Wunschliste, Ideen, Telefonnummern.
**[V]** Zwei Wege, wie ein Memo zurückkommt:
- **an einen Termin geklebt** — „beim Zahnarzt nach der Schiene fragen" taucht auf, wenn der Termin ansteht
- **Wiedervorlage** — „zeig mir das in 3 Monaten wieder"

---

## 4. Dringlichkeit / Eskalation

### Grundgedanke
**[E]** Priorität ist **eine Funktion der Zeit**, nicht ein statisches Feld. Die App zählt selbst hoch.

Leitbeispiel Müll: heute grün → morgen Fliegen → übermorgen Eier → dann Maden.
**[E]** Müll eskaliert **doppelt**: Gammel *und* Menge.

### Drei Kurventypen
```
Verderb      ▁▂▃▅▇█    die Welt wird schlechter   (Müll, Abwasch, Wäsche)
Deadline     ▁▁▁▁▁█    ein Stichtag kommt          (Rechnung, Rezept)
Vorsatz      ▁▁▂▂▃▃    nur der Vorsatz zerfällt    (Buch, Gitarre)
```

### Zwei Parameter pro Aufgabe
**[E]** **Tempo** und **Deckel** sind getrennt:

| | Tempo | Deckel |
|---|---|---|
| Müll | schnell | darf bis Rot |
| Rechnung | Stichtag | darf bis Rot |
| Bad | mittel | bis Orange |
| Buch | langsam | **maximal Gelb** |

Alles steigt — aber nicht alles darf schreien. Sonst verliert Rot seine Bedeutung.

### Der Takt ist die Priorität
**[E]** Kein separates Prioritätsfeld nötig. „alle 4 Wochen" sagt bereits alles.
```
Ein Buch lesen     alle 4 Wochen
Gitarre üben       alle 3 Tage
Eltern anrufen     alle 10 Tage
Fensterputzen      2× im Jahr
```
Der Unterschied zwischen „ein Buch im Monat" und „ein Buch in zehn Jahren" ist genau diese Zahl.

**[E]** Der Takt wird **individuell pro Termin/To-do** eingestellt — über Vorgaben und Vorlagen. Keine 20 globalen Regler.

**[E]** Zeiten teils vordefiniert, teils manuell:
- Müll → vordefiniert, ca. 3–4 Tage
- Eier / Kühlschrank → automatisch oder Datum eintippen
- Buch lesen → manuell

### Obergrenze
**[V]** Rot ist Endstation und erzwingt **einmal** eine Entscheidung.
**[E]** Optionen: **heute terminieren / abgeben / verschieben**

- **„Zerlegen" entfällt** — geht bei solchen Aufgaben nicht.
- **„Loslassen" gibt es grundsätzlich nicht.** Es gibt nur *Erledigen*. Die Dinge müssen letztendlich gemacht werden, sonst schaut man irgendwann aus dem Karton nicht mehr raus.
- (Fensterputzen war nur ein Beispiel für die Liste, kein Sonderfall.)

**[V]** Begrenzte Plätze für persönliche Vorsätze (z. B. 5), damit keine Schuldmaschine entsteht. Haushalt und Termine davon unberührt.

**[E]** Ab wann die Uhr läuft, wird **individuell pro Eintrag** hinterlegt. Bei regelmäßig wiederkehrenden Dingen ein fester Rhythmus, bei neu angelegten wird es beim Erstellen vordefiniert.

---

## 5. Farb- und Anzeigekonzept

**[E]** **Räumlich trennen, nicht mischen** (Weg A).
- **Links:** Streifen / Balken = **Kategorie**
- **Rechts:** Farbcode = **Dringlichkeit**

```
▌🗑  Müll runterbringen              🔴 4 Tage
▌🍽  Spülmaschine ausräumen         🟠 2 Tage
▌👕  Wäsche aufhängen               🟡 1 Tag
▌📄  Rechnung Stadtwerke            🟢 heute
```

**[E]** Trennung nach Ansicht:
- **Kalender** → Farbe = Kategorie
- **To-do-Liste** → Farbe / Balken = Dringlichkeit

**[E]** Kategorien mit je eigener Farbe:
Termine privat · Termine Arbeit · Geburtstage · Haushalt · Medikamente · Deadlines · Hobby/Freizeit

**[E]** **Hobby/Freizeit kommt mit in den Kalender** — bewusst, um sich einen leichten, gewollten Zeitdruck zu verschaffen.

**[E]** Farbwahl nach Recherche angepasst:
- **Grundpalette gedämpft** (Kategorien, immer sichtbar) — reduziert die Reizlast
- **Zusätzlich einige kräftige, kontrastreiche Töne** (helles Grün, helles Blau o. ä.)

**[V]** Alternative zum Streifen: die **Schriftfarbe** trägt die Kategorie.

### Farbe und Symbol sind zwei Ebenen
**[E]** Geklärt:

- **Farbe = Kategorie** — privat, beruflich, Termin, To-do, Geburtstag usw.
- **Symbol = Typ der Tätigkeit**, eine Ebene *unter* der Farbe

Beispiele innerhalb derselben Farbe:

| Typ | Symbol |
|---|---|
| Gesprächstermin, telefonisch | Telefon / Hörer / Handy |
| Abarbeitungstermin (nur abarbeiten) | anderes Symbol |

**[E]** **Symbolbibliothek** wünschenswert.
**[?]** **Die Typenliste selbst muss noch erarbeitet werden** — welche Tätigkeitstypen es überhaupt gibt.

**[E]** **Balkendiagramm** für die wichtigsten Sachen. Nicht dauerhaft sichtbar, aber jederzeit abrufbar. Farbig, ins Gesamtkonzept passend.

### Barrierefreiheit
**[V]** Farbe allein reicht nie — Grün→Gelb→Orange→Rot bricht bei Rot-Grün-Schwäche zusammen (ca. 8 % der Männer). Immer doppelt codieren:
1. **Sortierung** — Dringendstes oben (stärkster Hebel, kostet nichts)
2. **Zahl** — „4 Tage überfällig"
3. **Form** — Größe / leichte Bewegung

**[V]** Aus der UX-Forschung zu Neurodivergenz: viel Weißraum, keine Animationen, keine Pop-ups, kurze Labels ohne Fachbegriffe.

---

## 6. Module

### Wegzeit
**[E]** Muss im Vorfeld sichtbar sein. Beispiel: ab Magdeburg ca. 1,5 Std einfach, plus Rückweg, plus eventuelle Pause.

**[E]** **Nicht automatisch lösbar** — das Verkehrsmittel wechselt (Auto, Bahn, zu Fuß). Google Maps weiß nicht, womit man unterwegs ist. → Verkehrsmittel muss **wählbar / manuell** sein.

**[V]** Ein Termin ist keine Zeit, sondern eine Hülle aus vier Teilen:
```
09:45  Fertigmachen
10:15  Hinweg
11:00  TERMIN
11:45  Rückweg
12:30  zurück
```
Der Rückweg wird fast überall vergessen. Das Fertigmachen ebenso — oft der größere Zeitfresser.

**[V]** Bahnfahrten: Zugverbindung direkt übernehmen können.

### Medikamente
**[E]** Countdown mit rein, obwohl es das schon fertig gibt. Rechnerisch simpel (war schon mal eine Excel-Lösung).
```
Packung 100 Stück · Verbrauch 2/Tag → reicht 50 Tage
Vorlauf: Rezept 5 Tage + Apotheke 2 Tage
→ Alarm bei ca. 14 Tagen Rest
```
**[E]** Der Alarm ist ein **Kalendertermin**, keine wegwischbare Notification.
**[E]** **Neu: Medikamentenliste drucken**, im EU-Standard.
**[V]** Prinzip überträgt sich auf Kaffee, Waschmittel, Kontaktlinsen usw.

### Haushalt
**[E]** Eigener Typ mit einem Feld: **„alle X Tage"**. Zähler startet neu, **wenn du es machst** — nicht an einem festen Wochentag. So baut sich kein Rückstand auf.

### Müllabfuhr
**[E]** Kopplung an den Abfuhrkalender: Abfuhr z. B. 2× pro Woche → Müll muss kurz **vor** der Abfuhr raus.
**[V]** Für Magdeburg: **MagdeApp** hat den Abfuhrkalender mit Erinnerung, Termine sind in den eigenen Kalender übernehmbar. Machbar.

### Geburtstage
**[V]** Zweistufig: 14 Tage vorher „Geschenk besorgen", am Tag selbst „anrufen". Einmal angelegt, läuft jedes Jahr.

### Arbeitszeit
**[E]** Aufrechnung **pro Tag und pro Woche**. Arbeit und Privat getrennt gezählt, aber beides in derselben Ansicht.
**[V]** Darstellung als Kontingent statt Zeitfenster:
```
Diese Woche:  ████████████░░░░  31 / 40 h
```
**[!]** Marktlücke: In keiner untersuchten Planer-App gefunden.

---

## 7. Einstellungen

**[E]** Keine 20 globalen Regler. Jedes To-do / jeder Termin ist individuell einstellbar, über Vorgaben und Vorlagen.

**[V]** Alles hat einen sinnvollen Standardwert — Einstellungen sind Korrektur, nicht Voraussetzung.
**[V]** Presets statt Zahlen beim Anlegen: schnell / langsam / irgendwann / nie.
**[V]** Eskalation muss **einfrierbar** sein (Urlaub, Krankheit) — sonst kommt man zu einer roten Wand zurück.
**[V]** Nicht einstellbar: die Farben selbst, die Anzahl der Stufen, ob Termine eskalieren.

---

## 8. Bedienung

**[E]** **Drag & Drop** von Aufgaben auf Kalendertage und Listen — vor allem für wiederkehrende Dinge.
**[E]** Nicht Geschafftes **wandert** auf einen anderen Tag.
**[V]** **Wander-Zähler**: nach mehrfachem Verschieben wird einmal eine Entscheidung erzwungen, statt endlos weiterzuschieben.
**[V]** Erfassen muss kostenlos sein: ein Feld, Text rein, Enter, unsortiert. Sortiert wird später.

---

## 9. Plattform & Technik

**[E]** Muss laufen auf **PC, Tablet, Handy**.
**[E]** Inklusive **Widget(s)**.
**[E]** **Benachrichtigungen auf allen Geräten.**
**[E]** **Synchronisation ist ein großes Thema:**
- Abhaken am Handy → überall weg
- Benachrichtigung bestätigt / ausgestellt → überall
- Timer am Handy gestoppt → auch auf Tablet und Rechner gestoppt

**[E]** **KI- / Sprachmodell-Zugang**, um erinnert zu werden.

### Die drei Geräte haben verschiedene Rollen
**[E]** Das ist kein „läuft überall gleich", sondern drei unterschiedliche Aufgaben:

| Gerät | Rolle |
|---|---|
| **Tablet** | Termin **über den Tag präsent halten** — steht sichtbar herum |
| **Handy** | **Genervt werden.** Vor allem über **Widgets auf dem Startbildschirm** — der Startbildschirm organisiert mit |
| **Rechner** | **Verwalten.** Hier lässt sich am besten pflegen und ordnen — aber man sitzt nicht ständig davor |

**[V]** Startbildschirm zeigt nur **heute**, und wenig:
```
┌─────────────────────────┐
│  Heute                  │
│  🦷 10:15  Zahnarzt     │
│  🎯 Das Eine            │
│  🏠 15 Min: Bad         │
│  Arbeit ███░░  31/40h   │
└─────────────────────────┘
```
Alles andere einen Wisch entfernt. Vollständigkeit im Hintergrund, Sichtbarkeit rationiert.

---

## 10. Marktrecherche (Aug 2026)

| App | Kalender+To-do | Wegzeit | Medikamente | Arbeitszeit | Plattformen |
|---|---|---|---|---|---|
| Structured | stark | – | – | – | iOS-lastig |
| Tiimo | ja | – | – | – | iOS/Android |
| Morgen | ja | **auto, hin+zurück** | – | – | alle 3 |
| Amie | ja, Drag&Drop | – | – | – | alle 3 |
| Motion / Sunsama | ja | – | – | teilweise | alle 3 |
| Pill-Apps | – | – | **Restbestand + Alarm** | – | separat |

**Fazit: Die Kombination gibt es nicht.** Jedes Einzelteil existiert, aber verteilt auf fünf Apps.
Dünnste Stelle im Markt: **Arbeitszeit-Zähler bei freier Zeiteinteilung.**

Quellen:
- https://super-productivity.com/blog/best-adhd-task-management-apps-2026/
- https://aisotools.com/compare/structured-vs-tiimo
- https://www.morgen.so/guides/auto-schedule-travel-time
- https://www.addtraveltime.com/
- https://apps.apple.com/us/app/pill-reminder-all-in-one/id816347839
- https://www.magdeburg.de/Start/B%C3%BCrger-Stadt/System/Abfuhrkalender/
- https://www.accessibilitychecker.org/blog/neurodivergent-ux-design/
- https://www.designmonks.co/blog/ui-ux-and-adhd

---

## 11. Offene Punkte

- **[?]** **Typenliste erarbeiten** — welche Tätigkeitstypen bekommen ein eigenes Symbol (telefonischer Gesprächstermin, Abarbeitungstermin, …)

### Vorgehen
**[E]** Das Projekt muss in **mehreren Unterkategorien** bearbeitet werden. Das wird nicht so einfach wie das bisher Gesammelte.

### Inzwischen geklärt
- Ab wann die Uhr läuft → individuell pro Eintrag (Abschnitt 4)
- Entscheidung bei Rot → terminieren / abgeben / verschieben, **kein Loslassen** (Abschnitt 4)
- Hobby / Freizeit → kommt in den Kalender (Abschnitt 5)
- Symbole → Farbe = Kategorie, Symbol = Typ darunter (Abschnitt 5)
- Woran Termine scheitern → vier Ursachen (Abschnitt 2)
