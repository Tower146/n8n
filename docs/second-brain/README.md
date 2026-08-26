# Second Brain

Verfahren und Protokoll für die Pflege des Second Brain.

| Datei | Inhalt |
|---|---|
| [`intensiv-lauf.md`](intensiv-lauf.md) | Verbindliche Arbeitsanweisung für einen Lauf |
| [`laufprotokoll.md`](laufprotokoll.md) | Was wann gelaufen ist, Startpunkt des nächsten Laufs |

## Kurzfassung

- Der Lauf ist **immer intensiv** — vollständig lesen, nie überfliegen.
- **Wöchentlich** automatisch, zusätzlich **auf Zuruf** über den Input.
- Auf Zuruf genügt: `Second Brain intensiv` — optional mit Umfang, etwa
  `Second Brain intensiv, letzte 14 Tage`.

Reduziert wurde die Häufigkeit, nicht die Tiefe. Die Begründung dazu steht am Ende
von `intensiv-lauf.md`.

## Takt umstellen

Der wöchentliche Lauf wird **nicht** von einer Claude-Routine gestartet, sondern
von einem Zeitplan auf dem eigenen Rechner. Nachgeprüft:

| Prüfung | Ergebnis |
|---|---|
| Routinen im Konto | keine (`list_triggers` leer, auch mit erledigten) |
| Sessions der Läufe | `bridge` / `claude_code_cli` — laufen auf dem eigenen Rechner |
| Verfügbare Umgebungen | nur `anthropic_cloud` — keine Bridge-Umgebung |

Daraus folgt: Eine reine Cloud-Routine käme **nicht** an die lokalen Dateien heran.
Der Zeitplan bleibt deshalb sinnvollerweise auf dem Rechner.

### Änderung

Nur das **Wochentag-Feld** anpassen, die Uhrzeit unangetastet lassen:

```cron
# vorher — täglich
16 5 * * *   <bisheriger Befehl>
#        ^ jeden Tag

# nachher — sonntags
16 5 * * 0   <bisheriger Befehl>
#        ^ nur Sonntag
```

Der Befehl selbst bleibt unverändert.

### Warum das die günstigere Bauform ist

Ein Cron-Eintrag startet bei jedem Lauf eine **frische** Session. Eine Claude-Routine,
die in eine bestehende Session feuert, setzt dagegen dieselbe Unterhaltung immer fort —
der Kontext wächst über Wochen, und genau dieses Mitschleppen ist laut Kostenanalyse
der teuerste Posten. Der Cron-Weg vermeidet das dauerhaft und ohne Pflegeaufwand.

### Ändern lässt sich das weiterhin vom Handy

Der Zeitplan liegt auf dem Rechner, ist aber nicht an ihn gefesselt: Ein Chat vom Handy
steuert per Remote Control eine Session auf dem Computer — derselbe Weg, auf dem der
Eintrag ursprünglich entstanden ist. Voraussetzung ist nur, dass der Rechner erreichbar
ist.
