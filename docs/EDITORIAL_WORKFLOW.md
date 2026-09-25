# Maintain the list and supporting directory

[Editorial list](../README.md) · [Contribute](../CONTRIBUTING.md) · [Curation rules](CURATION.md)

## Editorial source stays separate

Root `README.md` is directly maintained Markdown. Neither a build nor the scheduled discovery job rewrites it. There is no `.github/README.md` to shadow it. Update front-page selections deliberately, with primary-source evidence in `data/curated.json`; a source-reviewed record may remain only in the supporting catalog.

The original quick-start, task paths, curated X/media gallery, creator attribution, and discovery information remain in [DIRECTORY.md](DIRECTORY.md). Its template retains the historical path `templates/README.md` for existing maintenance instructions, but its output is no longer a README.

## Source and generated views

| Source | Generated surface |
|---|---|
| `templates/README.md` and catalog/media data | `docs/DIRECTORY.md` |
| `data/curated.json` | `docs/REVIEWED.md` and reviewed records in the catalog |
| Merged catalog and `templates/catalog.html` | `docs/CATALOG.md` and local `docs/catalog.html` |
| `data/x_demos.json` | `docs/X_DEMOS.md` and the supporting directory's X index |
| `data/media.json` and access receipts | Original gallery in `docs/DIRECTORY.md` and `docs/MEDIA.md` |
| Discovery receipt and rotating metadata checks | `docs/STATUS.md` and supporting-directory freshness |
| `data/exclusions.json` | Persistent exclusions applied after import/discovery |

The unified builder also validates README membership, formatting, contents links, and the independent-model/supporting-driver distinctions. It never selects a new front-page entry. Legacy component publication CLIs are disabled.

## Review and publication

Read implementation evidence and relevant examples/tests before selecting a project. Disclose affiliation, paid providers, observation/privacy boundaries, and author-reported benchmarks. Keep source inspection, runtime testing, and media access receipts distinct. Do not execute discovered projects or install their skills during curation.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
git diff --check
```

These commands are offline. `--refresh` and `--refresh-media` explicitly request bounded public discovery and media checks. The existing four-hour cadence remains unchanged. The publisher only stages generated supporting views; staged editorial source is rejected, not silently committed.

Maintain canonical X links and attribution in the existing source data. A successfully retrieved media URL does not establish that a demonstration ran live. Preserve prior media on transient access failures.

For upstream Awesome preparation, consult [AWESOME_SUBMISSION.md](AWESOME_SUBMISSION.md). Formatting checks cannot establish non-AI authorship, maturity, or editorial acceptance. Historical review notes remain dated records, not live approval checkpoints.
