# bundle-repos

Daily-scraped list of ReVanced & Morphe patch bundle repository URLs, taken from the
[Patch Bundle Registry API](https://patch-bundles.jmancentral.com/api-docs/)
(`GET https://patch-bundles.api.jmancentral.com/sources` — every source record's
`url` field), which indexes more sources than the
[Jman-Github/ReVanced-Patch-Bundles](https://github.com/Jman-Github/ReVanced-Patch-Bundles#-patch-repositories-in-use)
README list this repo used before 2026-10-18.

- **`bundles.txt`** — one repo URL per line, sorted, deduped. ReVanced bundle sources
  are excluded. Refreshed automatically
  every day at 06:00 UTC (11:30 IST) by the `Refresh bundles.txt` workflow, and
  attached to the rolling [**latest** release](https://github.com/ShuhaibNC/bundle-repos/releases/tag/latest).
- **`scrape-bundle-repos.py`** — the scraper. Run it manually anytime:
  `python3 scrape-bundle-repos.py bundles.txt`
