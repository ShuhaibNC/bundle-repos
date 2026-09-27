# bundle-repos

Daily-scraped list of ReVanced & Morphe patch bundle repository URLs, taken from the
"Patch Repositories In Use" section of
[Jman-Github/ReVanced-Patch-Bundles](https://github.com/Jman-Github/ReVanced-Patch-Bundles#-patch-repositories-in-use).

- **`bundles.txt`** — one repo URL per line, sorted, deduped. Refreshed automatically
  every day at 06:00 UTC (11:30 IST) by the `Refresh bundles.txt` workflow.
- **`scrape-bundle-repos.py`** — the scraper. Run it manually anytime:
  `python3 scrape-bundle-repos.py bundles.txt`
