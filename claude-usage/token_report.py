#!/usr/bin/env python3
"""
Token- und Kostenauswertung fuer Claude-Code-Routinen.

Liest die lokalen Transcript-Dateien (~/.claude/projects/**/*.jsonl), summiert
die tatsaechlich abgerechneten Token pro Session/Tag/Routine und rechnet sie in
API-Aequivalentkosten um.

Beispiele:
    python3 token_report.py                          # alles, Uebersicht pro Routine
    python3 token_report.py --match "second brain"   # nur Second-Brain-Laeufe
    python3 token_report.py --by day --days 14       # Tagesverlauf der letzten 2 Wochen
    python3 token_report.py --by session --csv out.csv

Hinweis: Bei einem Abo (Pro/Max) zahlen Sie diese Betraege nicht in Euro - die
Token laufen gegen Ihr 5-Stunden- bzw. 7-Tage-Kontingent. Die Geldbetraege sind
der Vergleichswert "was das ueber die API gekostet haette".
"""

import argparse
import collections
import csv
import datetime as dt
import json
import os
import pathlib
import re
import sys

# Preise in USD pro 1 Mio. Token (Anthropic First-Party-API).
# cache_write = 1.25x Input, cache_read = 0.1x Input.
PRICING = {
    "claude-fable-5":     {"in": 10.00, "out": 50.00},
    "claude-opus-5":      {"in":  5.00, "out": 25.00},
    "claude-opus-4-8":    {"in":  5.00, "out": 25.00},
    "claude-opus-4-7":    {"in":  5.00, "out": 25.00},
    "claude-opus-4-6":    {"in":  5.00, "out": 25.00},
    "claude-sonnet-5":    {"in":  2.00, "out": 10.00},
    "claude-sonnet-4-6":  {"in":  3.00, "out": 15.00},
    "claude-haiku-4-5":   {"in":  1.00, "out":  5.00},
}
FALLBACK = {"in": 3.00, "out": 15.00}


def rates(model):
    """Preis-Tupel (input, output, cache_write, cache_read) je Mio. Token."""
    if not model:
        p = FALLBACK
    else:
        key = model.strip()
        p = PRICING.get(key)
        if p is None:
            # Datums-Suffixe wie -20251001 abschneiden und erneut versuchen.
            p = PRICING.get(re.sub(r"-\d{8}$", "", key), FALLBACK)
    return p["in"], p["out"], p["in"] * 1.25, p["in"] * 0.10


class Bucket:
    __slots__ = ("inp", "out", "cw", "cr", "cost", "calls", "sessions", "models")

    def __init__(self):
        self.inp = self.out = self.cw = self.cr = 0
        self.cost = 0.0
        self.calls = 0
        self.sessions = set()
        self.models = collections.Counter()

    def add(self, inp, out, cw, cr, model, session):
        r_in, r_out, r_cw, r_cr = rates(model)
        self.inp += inp
        self.out += out
        self.cw += cw
        self.cr += cr
        self.cost += (inp * r_in + out * r_out + cw * r_cw + cr * r_cr) / 1_000_000
        self.calls += 1
        self.sessions.add(session)
        if model:
            self.models[model] += 1

    @property
    def total(self):
        return self.inp + self.out + self.cw + self.cr


def iter_records(root):
    """Liefert (timestamp, session_id, model, usage, first_user_text) je Assistant-Turn."""
    for path in sorted(pathlib.Path(root).rglob("*.jsonl")):
        label = None
        try:
            lines = path.read_text(errors="replace").splitlines()
        except OSError:
            continue
        # Erste echte User-Nachricht als Routine-Bezeichner.
        for line in lines:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("type") == "user":
                content = (rec.get("message") or {}).get("content")
                if isinstance(content, list):
                    content = " ".join(
                        b.get("text", "") for b in content if isinstance(b, dict)
                    )
                if isinstance(content, str):
                    text = " ".join(content.split())
                    # Tool-Ergebnisse und Systemhinweise ueberspringen.
                    if text and not text.startswith("<"):
                        label = text[:70]
                        break
        for line in lines:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            msg = rec.get("message")
            if not isinstance(msg, dict):
                continue
            usage = msg.get("usage")
            if not isinstance(usage, dict):
                continue
            yield (
                rec.get("timestamp"),
                rec.get("sessionId") or path.stem,
                msg.get("model"),
                usage,
                label or path.stem,
            )


def parse_ts(value):
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=os.path.expanduser("~/.claude/projects"),
                    help="Verzeichnis mit den Transcript-Dateien")
    ap.add_argument("--by", choices=("routine", "day", "session", "model"),
                    default="routine", help="Gruppierung der Ausgabe")
    ap.add_argument("--match", help="nur Laeufe, deren Prompt dies enthaelt (case-insensitive)")
    ap.add_argument("--days", type=int, help="nur die letzten N Tage")
    ap.add_argument("--csv", help="Ergebnis zusaetzlich als CSV schreiben")
    args = ap.parse_args()

    if not os.path.isdir(args.root):
        sys.exit(f"Transcript-Verzeichnis nicht gefunden: {args.root}\n"
                 f"Auf dem Rechner ausfuehren, auf dem die Routinen laufen.")

    cutoff = None
    if args.days:
        cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)

    needle = args.match.lower() if args.match else None
    buckets = collections.defaultdict(Bucket)
    grand = Bucket()

    for ts, session, model, usage, label in iter_records(args.root):
        if needle and needle not in label.lower():
            continue
        stamp = parse_ts(ts)
        if cutoff and (stamp is None or stamp < cutoff):
            continue

        inp = usage.get("input_tokens", 0) or 0
        out = usage.get("output_tokens", 0) or 0
        cw = usage.get("cache_creation_input_tokens", 0) or 0
        cr = usage.get("cache_read_input_tokens", 0) or 0
        if not (inp or out or cw or cr):
            continue

        if args.by == "day":
            key = stamp.date().isoformat() if stamp else "unbekannt"
        elif args.by == "session":
            key = f"{stamp.date().isoformat() if stamp else '????'}  {label}"
        elif args.by == "model":
            key = model or "unbekannt"
        else:
            key = label

        buckets[key].add(inp, out, cw, cr, model, session)
        grand.add(inp, out, cw, cr, model, session)

    if not buckets:
        sys.exit("Keine passenden Eintraege gefunden.")

    rows = sorted(buckets.items(), key=lambda kv: kv[1].cost, reverse=True)

    head = f"{'Gruppe':<52}{'Laeufe':>7}{'Token ges.':>13}{'davon Cache':>13}{'USD-Aequiv.':>13}"
    print(head)
    print("-" * len(head))
    for key, b in rows:
        cache_share = (b.cr / b.total * 100) if b.total else 0
        print(f"{key[:52]:<52}{len(b.sessions):>7}{b.total:>13,}{cache_share:>12.0f}%{b.cost:>13.2f}")
    print("-" * len(head))
    print(f"{'SUMME':<52}{len(grand.sessions):>7}{grand.total:>13,}"
          f"{(grand.cr / grand.total * 100 if grand.total else 0):>12.0f}%{grand.cost:>13.2f}")

    print(f"\nAufschluesselung gesamt:")
    print(f"  Input (frisch)   {grand.inp:>14,}")
    print(f"  Output           {grand.out:>14,}")
    print(f"  Cache geschrieben{grand.cw:>14,}")
    print(f"  Cache gelesen    {grand.cr:>14,}")
    if grand.models:
        print("  Modelle: " + ", ".join(f"{m} ({n}x)" for m, n in grand.models.most_common()))

    if len(grand.sessions):
        print(f"\nDurchschnitt pro Lauf: {grand.total // len(grand.sessions):,} Token"
              f"  /  {grand.cost / len(grand.sessions):.2f} USD-Aequivalent")

    print("\nHinweis: Im Abo zahlen Sie diese Betraege nicht in Euro - die Token laufen\n"
          "gegen Ihr 5-Stunden- und 7-Tage-Kontingent. Der USD-Wert zeigt, was dieselbe\n"
          "Arbeit ueber die API gekostet haette.")

    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["gruppe", "laeufe", "input", "output",
                        "cache_write", "cache_read", "token_gesamt", "usd_aequivalent"])
            for key, b in rows:
                w.writerow([key, len(b.sessions), b.inp, b.out, b.cw, b.cr,
                            b.total, f"{b.cost:.4f}"])
        print(f"\nCSV geschrieben: {args.csv}")


if __name__ == "__main__":
    main()
