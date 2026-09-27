#!/usr/bin/env python3
"""Scrape every patch-bundle repo URL from the README of
Jman-Github/ReVanced-Patch-Bundles.

The README's "Patch Repositories In Use" section lists each source as:
    #### <emoji> [Name-Bundle](https://github.com/owner/repo)
This script pulls the raw README from the repo's default branch, extracts
every link inside that section, dedupes, sorts, and writes them to a text
file (one URL per line).

Usage: python3 scrape-bundle-repos.py [output.txt]
"""
import re
import sys
import urllib.request

README_URL = (
    "https://raw.githubusercontent.com/"
    "Jman-Github/ReVanced-Patch-Bundles/bundles/README.md"
)
SECTION_START = "## 🩹 Patch Repositories In Use"
SECTION_END = "## 🖇 Integrations Repositories In Use"
LINK_RE = re.compile(r"\((https?://[^)]+)\)")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "bundle-repos.txt"
    readme = fetch(README_URL)

    start = readme.index(SECTION_START)
    end = readme.index(SECTION_END)
    section = readme[start:end]

    urls = sorted(set(LINK_RE.findall(section)))
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(urls) + "\n")
    print(f"scraped {len(urls)} unique repo urls -> {out_path}")


if __name__ == "__main__":
    main()
