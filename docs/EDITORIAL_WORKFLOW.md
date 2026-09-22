# Maintain the directory's navigation and content

[Start here](../README.md) · [Contribute](../CONTRIBUTING.md) · [Curation rules](CURATION.md)

## One homepage, not two competing READMEs

Root `README.md` and `.github/README.md` are generated identically from `templates/README.md`, reviewed catalog data, X sources and media. GitHub prefers the `.github` README, so synchronizing both also fixes the view reached through direct root links. [GitHub README precedence](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).

The hierarchy is: reviewed-first summary and evidence legend → plain explanation → tiny quick-start → one visual → three task paths → reviewed links → search/filter help → purpose and inclusion policy → contribution/freshness → collapsible safety detail → full media gallery and compact X index.

## Source and generated views

| Source | Generated surface |
|---|---|
| `templates/README.md` plus source catalogs | Both READMEs |
| `data/curated.json` | `docs/REVIEWED.md` |
| Merged catalog plus `templates/catalog.html` | `docs/CATALOG.md` and the local searchable `docs/catalog.html` |
| `data/x_demos.json` | `docs/X_DEMOS.md` and the homepage's compact X index |
| `data/media.json` and access receipts | Preserved homepage gallery and `docs/MEDIA.md` |
| Completed discovery receipt and rolling check metadata | `docs/STATUS.md` and the top freshness line |
| `data/exclusions.json` | Excluded from future generated/imported listings |

The unified `scripts/build.py` invokes the existing component functions in the correct order. The older component CLIs retain legacy output layouts; do not use them to publish. Templates remain editorial inputs, not files rewritten by network refresh.

## Add an X demo or visual

Keep canonical status URLs, correct creator/repository attribution, direct primary evidence, a concrete Jev role, reuse pattern, limitations and an accurate review date. `indexed-reference` means the source post was not fully retrieved; only use `primary-post-reviewed` after inspecting it. Roundups have a separate array and do not establish coverage of all replies.

A media check means a bounded request succeeded, not that the video was watched or its claims reproduced. Keep known mock/fixture/archived/illustration labels and original source links. Do not install discovered skills or copy social videos without permission.

## Regenerate and verify

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
```

Everything above is offline. `--refresh` explicitly discovers public GitHub sources and records a completion time; `--refresh-media` explicitly checks public media. The four-hour workflow runs both, validates all surfaces, and publishes an allowlisted set of generated files without force-pushing.

`DEVTO_DRAFT.md` remains an unpublished draft. `REPOSITORY_SETTINGS.md` remains prepared sidebar metadata unless a settings action actually succeeds. The local HTML viewer is not a deployed website. Keep these distinctions explicit in updates.
