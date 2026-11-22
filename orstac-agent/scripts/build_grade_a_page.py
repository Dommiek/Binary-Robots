"""Build grade-a.html at the repo root from the generated audit CSV.

Usage (from the repo root):
    python orstac-agent/scripts/build_grade_a_page.py

Re-run after regenerating knowledge/repo_audit_*.csv with `orstac-agent audit-repo`.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "orstac-agent" / "knowledge" / "repo_audit_2026-11.csv"
TEMPLATE = Path(__file__).with_name("grade_a_template.html")
OUT = ROOT / "grade-a.html"


def main() -> int:
    rows = []
    with CSV.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["risk_grade"] != "A" or not (ROOT / r["file"]).is_file():
                continue
            rows.append({
                "name": Path(r["file"]).stem,
                "href": quote(r["file"]),
                "symbol": r["symbol"] or "?",
                "type": r["trade_type"] or "?",
                "duration": r["duration"],
                "indicators": r["indicators"].replace("|", ", "),
                "target": r["profit_target"] == "1",
            })
    rows.sort(key=lambda x: x["name"].lower())
    data = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8")
    html = html.replace("__COUNT__", str(len(rows))).replace("__DATA__", data)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(rows)} bots")
    return 0


if __name__ == "__main__":
    sys.exit(main())
