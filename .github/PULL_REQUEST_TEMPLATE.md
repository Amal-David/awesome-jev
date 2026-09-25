## What this adds or fixes

Describe the concrete Jev role and link the original creator's source. Disclose affiliation.

## Evidence and safety

- [ ] I separated source inspection, live execution, and author-reported results.
- [ ] I disclosed missing licenses/code, mock/replay modes, paid APIs and sensitive data handling.
- [ ] I did not include credentials, copied social videos, game ROMs, or instructions to run untrusted projects during curation.
- [ ] For a front-page selection, I edited root `README.md` directly and included its evidence in `data/curated.json`.
- [ ] I used `data/x_demos.json` and `data/media.json` for gallery changes; `templates/README.md` controls the supporting `docs/DIRECTORY.md`, not the root README.
- [ ] A full removal uses `data/exclusions.json` so later imports cannot restore it.

## Validation

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
git diff --check
```

Regenerate supporting views on current main and commit source and generated changes together, not an old snapshot. The builder must leave root `README.md` untouched. Do not recreate `.github/README.md`. Preserve the quick-start, source notes, evidence labels, discovery receipts, and creator-attributed gallery in `docs/DIRECTORY.md`.

For README-format changes, also run the complete default `awesome-lint@2.3.0` check described in `CONTRIBUTING.md` and report its actual result. A formatting pass does not establish eligibility for the canonical Awesome index; see `docs/AWESOME_SUBMISSION.md`.
