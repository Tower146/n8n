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
von einem Scheduler auf dem eigenen Rechner (cron, launchd oder Aufgabenplanung) —
die bisherigen Läufe erscheinen als Bridge-Sessions.

Zum Umstellen von täglich auf wöchentlich dort den Eintrag anpassen, z. B. bei cron:

```cron
# vorher: täglich 05:16
16 5 * * *   <bisheriger Befehl>

# nachher: sonntags 05:16
16 5 * * 0   <bisheriger Befehl>
```

Der Befehl selbst bleibt unverändert; es ändert sich nur das Tagesfeld.
