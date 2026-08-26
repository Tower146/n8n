# Token-Auswertung fuer Claude-Code-Routinen

Ermittelt, wie viele Token die taeglichen Routinen (Second Brain, Maverick, ...)
tatsaechlich verbrauchen - aus den lokalen Transcript-Dateien, nicht geschaetzt.

## Ausfuehren

Auf dem Rechner, auf dem die Routinen laufen:

```bash
python3 claude-usage/token_report.py                        # Uebersicht pro Routine
python3 claude-usage/token_report.py --match "second brain" # nur Second Brain
python3 claude-usage/token_report.py --by day --days 14     # Tagesverlauf
python3 claude-usage/token_report.py --by model             # welches Modell kostet was
python3 claude-usage/token_report.py --csv kosten.csv       # Export
```

Keine Abhaengigkeiten, nur Python 3.

## Woher die Daten kommen

Claude Code schreibt jeden Turn nach `~/.claude/projects/**/*.jsonl`, inklusive
`message.usage`. Das Skript summiert daraus vier Token-Arten:

| Feld                          | Bedeutung                          | Preis      |
|-------------------------------|------------------------------------|------------|
| `input_tokens`                | frisch gesendeter Kontext          | 1x         |
| `output_tokens`               | erzeugter Text                     | ~5x Input  |
| `cache_creation_input_tokens` | Kontext in den Cache geschrieben   | 1,25x Input|
| `cache_read_input_tokens`     | Kontext aus dem Cache gelesen      | 0,1x Input |

Preise (USD je 1 Mio. Token, Stand 2026-06):
Sonnet 5 $2 / $10, Opus 5 $5 / $25, Opus 4.8/4.7/4.6 $5 / $25,
Sonnet 4.6 $3 / $15, Haiku 4.5 $1 / $5, Fable 5 $10 / $50.
Anpassbar im Dict `PRICING` in `token_report.py`.

## Wichtig zur Interpretation

Bei einem Pro-/Max-Abo zahlen Sie die ausgewiesenen Betraege **nicht in Euro**.
Die Token laufen gegen das 5-Stunden- und das 7-Tage-Kontingent. Der USD-Wert ist
der Vergleichsmassstab "was dieselbe Arbeit ueber die API gekostet haette" - und
damit die brauchbare Groesse, um Routinen untereinander zu vergleichen.

## Der wichtigste Hebel

In agentischen Sessions dominieren die **Cache-Reads**: jeder Turn liest den
gesamten bisherigen Kontext erneut. Bei langen Laeufen sind das 80-90 Prozent
aller Token. Das heisst:

- Die Laenge einer Session kostet mehr als die Anzahl der Sessions.
- Eine Routine, die frisch startet und in 10 Turns fertig ist, ist deutlich
  guenstiger als eine, die 40 Turns lang Kontext mitschleppt.
- Modellwahl skaliert alles linear mit: Opus 5 kostet je Token das 2,5-fache
  von Sonnet 5.
