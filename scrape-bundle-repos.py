#!/usr/bin/env python3
"""Fetch every patch-bundle GitHub repo URL from the Patch Bundle Registry API.

Reference docs: https://patch-bundles.jmancentral.com/api-docs/
OpenAPI spec:   https://patch-bundles.api.jmancentral.com/api.json

Endpoint used:
    GET https://patch-bundles.api.jmancentral.com/sources?limit=100&offset=N
Each source record carries a "url" field, e.g.
    {"id": "...", "host": "github.com", "namespace": "virzak",
     "repo": "morphe-patches", "url": "https://github.com/virzak/morphe-patches", ...}

Results are paged (max 100 rows per page via `limit`, pages skipped via
`offset`). This script walks every page, keeps only github.com URLs, dedupes,
sorts, and writes them to a text file (one URL per line).

curl is used for the HTTP calls (with retries) because plain urllib reads can
drop mid-response on some networks.

Usage: python3 scrape-bundle-repos.py [output.txt]
"""
import json
import subprocess
import sys

API = "https://patch-bundles.api.jmancentral.com"


def fetch(url):
    out = subprocess.run(
        ["curl", "-s", "--retry", "3", "--retry-all-errors", "-m", "60",
         "-H", "User-Agent: Mozilla/5.0", url],
        capture_output=True, text=True, timeout=120)
    out.check_returncode()
    return json.loads(out.stdout)


def is_revanced(src):
    """True for ReVanced bundle sources (repo name or owner contains 'revanced')."""
    return ("revanced" in (src.get("repo") or "").lower()
            or "revanced" in (src.get("namespace") or "").lower())


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "bundle-repos.txt"
    urls, offset = set(), 0
    while True:
        page = fetch(f"{API}/sources?limit=100&offset={offset}")
        rows = page.get("data", [])
        if not rows:
            break
        for src in rows:
            if is_revanced(src):
                continue
            url = (src.get("url") or "").rstrip("/")
            if url and src.get("host") == "github.com":
                urls.add(url)
        offset += 100
        if offset >= 10000 or len(rows) < 100:
            break

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(sorted(urls)) + "\n")
    print(f"fetched {len(urls)} unique github repo urls -> {out_path}")


if __name__ == "__main__":
    main()
