## What this adds or fixes

Describe the concrete Jev role and link the original creator's source. Disclose any affiliation.

## Evidence and safety

- [ ] I separated source inspection from live execution and author-reported benchmark results.
- [ ] I disclosed missing code/licenses, mock or replay modes, paid APIs, sensitive data handling, and important limitations.
- [ ] I did not include credentials, copied social videos, game ROMs, or instructions to execute untrusted code during curation.
- [ ] X additions use canonical post URLs in `data/x_demos.json`; primary project entries use `data/curated.json`.

## Validation

```sh
python3 -m unittest discover -s tests -v
python3 scripts/curate.py
python3 scripts/curate.py --check
python3 scripts/curate_x.py
python3 scripts/curate_x.py --check
```

Regenerate on current main; do not replace the catalog with an old generated snapshot. Edit `templates/README.md` for the editorial homepage, not the generated `.github/README.md`.
