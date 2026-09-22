## What this adds or fixes

Describe the concrete Jev role and link the original creator's source. Disclose affiliation.

## Evidence and safety

- [ ] I separated source inspection, live execution, and author-reported results.
- [ ] I disclosed missing licenses/code, mock/replay modes, paid APIs and sensitive data handling.
- [ ] I did not include credentials, copied social videos, game ROMs, or instructions to run untrusted projects during curation.
- [ ] I edited the right source: `data/curated.json`, `data/x_demos.json`, `data/media.json`, or the editorial templates.
- [ ] A full removal uses `data/exclusions.json` so later imports cannot restore it.

## Validation

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
```

Regenerate on current main. Commit the source and generated outputs, not an old snapshot. Both READMEs must match. The quick-start, reviewed-first navigation, evidence labels, freshness coverage and media attribution must remain intact.
