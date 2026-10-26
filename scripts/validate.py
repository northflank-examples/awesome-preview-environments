#!/usr/bin/env python3
"""Validate data/platforms.json and data/databases.json: required fields, categories and sources.

Exit code 1 on any failure. Runs in CI.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CATEGORIES = {"full-stack", "kubernetes", "frontend", "self-hosted-paas", "open-source-tool", "ci-native"}
REQUIRED = ["id", "name", "website", "summary", "summary_short", "last_verified", "facts"]
PLATFORM_FACTS = ["scope", "hosting", "git", "trigger", "databases", "cleanup", "access", "license", "pricing"]
CAPABILITY_KEYS = {"backend", "database", "own_cloud", "pr_close", "expiry", "protection",
                   "on_demand_triggers", "data_copy", "teardown_hooks", "multi_repo"}
# Capabilities that are backed by a fact of the same name, which must then be sourced.
CAPABILITY_FACTS = ["on_demand_triggers", "data_copy", "teardown_hooks", "multi_repo"]
CAPABILITY_VALUES = {"yes", "partial", "no", None}
DATABASE_FACTS = ["engine", "method", "per_pr_automation", "cleanup", "data", "hosting", "license", "pricing"]


def check_entries(entries: list[dict], facts: list[str], label: str, errors: list[str], categories=None) -> None:
    ids = set()
    for e in entries:
        eid = e.get("id", "?")
        for k in REQUIRED:
            if not e.get(k):
                errors.append(f"{label} {eid}: missing {k}")
        if eid in ids:
            errors.append(f"{label} {eid}: duplicate id")
        ids.add(eid)
        if not re.fullmatch(r"[a-z0-9-]+", eid):
            errors.append(f"{label} {eid}: id must be lowercase letters, digits and dashes")
        if categories is not None and e.get("category") not in categories:
            errors.append(f"{label} {eid}: unknown category {e.get('category')!r}")
        if not DATE.match(e.get("last_verified", "")):
            errors.append(f"{label} {eid}: last_verified must be YYYY-MM-DD")
        if len(e.get("summary_short", "")) > 120:
            errors.append(f"{label} {eid}: summary_short is over 120 characters")
        for k in facts:
            f = e.get("facts", {}).get(k)
            if f is None:
                errors.append(f"{label} {eid}: missing fact {k} (use value null if not published)")
                continue
            # A sourceless value is allowed only when a note explains it (e.g. "Proprietary" for a
            # closed-source service that publishes no licence text to quote).
            if f.get("value") not in (None, "") and not f.get("source") and not f.get("note"):
                errors.append(f"{label} {eid}: fact {k} has a value but no source or note")
            if f.get("source") and not str(f["source"]).startswith("https://"):
                errors.append(f"{label} {eid}: fact {k} source must be an https URL")
            if f.get("value") in (None, "") and not f.get("note"):
                errors.append(f"{label} {eid}: fact {k} is null; add a note saying why")
        caps = e.get("capabilities")
        if caps is not None:
            if set(caps) != CAPABILITY_KEYS:
                errors.append(f"{label} {eid}: capabilities must have exactly {sorted(CAPABILITY_KEYS)}")
            for k, v in caps.items():
                if v not in CAPABILITY_VALUES:
                    errors.append(f"{label} {eid}: capability {k} must be yes, partial, no or null")
            for k in CAPABILITY_FACTS:
                f = e.get("facts", {}).get(k)
                if f is None:
                    errors.append(f"{label} {eid}: capability {k} needs a fact of the same name")
                elif caps.get(k) is not None and not f.get("source"):
                    errors.append(f"{label} {eid}: capability {k} is marked but its fact has no source")
        elif e.get("category") in {"full-stack", "kubernetes", "frontend", "self-hosted-paas"}:
            errors.append(f"{label} {eid}: platforms need a capabilities block")


def main() -> int:
    errors: list[str] = []
    platforms = json.loads((ROOT / "data" / "platforms.json").read_text())
    databases = json.loads((ROOT / "data" / "databases.json").read_text())
    check_entries(platforms["platforms"], PLATFORM_FACTS, "platform", errors, CATEGORIES)
    check_entries(databases["tools"], DATABASE_FACTS, "database", errors)
    for data in (platforms, databases):
        for x in data.get("excluded", []):
            if not x.get("reason") or not x.get("source"):
                errors.append(f"excluded {x.get('name')}: needs a reason and a source")
    for e in errors:
        print(e)
    n = len(platforms["platforms"]) + len(databases["tools"])
    print(f"{n} entries, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
