#!/usr/bin/env python3
"""Check that every quoted fact still appears, verbatim, on its source page.

Usage:
    python3 scripts/check_quotes.py                 # check data/*.json
    python3 scripts/check_quotes.py path/to.json    # check specific files
    python3 scripts/check_quotes.py --only vercel   # check one entry

A quote may be split with "..." into fragments; each fragment must appear on the page.
Matching ignores case, whitespace, Markdown/HTML markup and typographic quotes and dashes.

Pages that can't be fetched, or that render their text with JavaScript, are reported as
UNREACHABLE rather than as failures. Check those by hand. Exit code 1 only if a fetched page
doesn't contain its quote, which usually means the vendor changed the page.
Not run in CI: vendor sites rate-limit and block CI runners. Run it before updating last_verified.
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; awesome-preview-environments quote checker)"
_cache: dict[str, str | None] = {}


def normalise(text: str) -> str:
    text = html.unescape(text)
    for a, b in {"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-",
                 " ": " ", "→": "->"}.items():
        text = text.replace(a, b)
    text = re.sub(r"[*`#>|\[\]()\"']", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r" ([:,.;!?])", r"\1", text)
    return text.strip().lower()


def page_text(url: str) -> str | None:
    if url in _cache:
        return _cache[url]
    texts = []
    # Many docs sites also serve Markdown; try it when the HTML is a JS shell.
    candidates = [url] + ([url.split("#")[0].rstrip("/") + ".md"] if not url.endswith(".md") else [])
    for candidate in candidates:
        try:
            req = urllib.request.Request(candidate, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8", "replace")
        except Exception:
            continue
        raw = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
        # Keep attribute-free text and also text inside JSON blobs (Next.js data etc.)
        texts.append(re.sub(r"<[^>]+>", " ", raw))
        texts.append(raw.replace("\\n", " ").replace('\\"', '"'))
    _cache[url] = normalise(" ".join(texts)) if texts else None
    return _cache[url]


def facts(data: dict):
    for collection in ("platforms", "tools", "entries"):
        for entry in data.get(collection, []):
            for key, fact in (entry.get("facts") or {}).items():
                if isinstance(fact, dict) and fact.get("quote") and fact.get("source"):
                    yield entry["id"], key, fact


def check(item) -> tuple[str, str, str, str]:
    entry_id, key, fact = item
    text = page_text(fact["source"])
    if text is None:
        return "UNREACHABLE", entry_id, key, fact["source"]
    # Strip sentence punctuation left next to the "...", e.g. "account....You can".
    fragments = [normalise(f).strip(" .") for f in re.split(r"\.\.\.|…", fact["quote"])]
    fragments = [f for f in fragments if len(f) > 3]
    missing = [f for f in fragments if f not in text]
    if missing:
        return "MISMATCH", entry_id, key, f'{fact["source"]}\n      missing: "{missing[0][:120]}"'
    return "OK", entry_id, key, ""


def main(argv: list[str]) -> int:
    only = None
    if "--only" in argv:
        i = argv.index("--only")
        only = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    paths = [Path(p) for p in argv] or sorted((ROOT / "data").glob("*.json"))
    items = []
    for path in paths:
        for item in facts(json.loads(path.read_text())):
            if only is None or item[0] == only:
                items.append(item)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, items))
    counts: dict[str, int] = {}
    for status, entry_id, key, detail in results:
        counts[status] = counts.get(status, 0) + 1
        if status != "OK":
            print(f"{status:11} {entry_id}.{key}: {detail}")
    print(", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    return 1 if counts.get("MISMATCH") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
