# Maintain the homepage and X collection

The two README surfaces have different jobs:

| Surface | Source of truth | Generator |
|---|---|---|
| `.github/README.md` — GitHub's repository landing page | `templates/README.md` and `data/x_demos.json` | `scripts/curate_x.py` |
| Root `README.md` — reviewed-project inventory | `data/curated.json` plus the merged catalog | `scripts/curate.py` |
| `docs/X_DEMOS.md` — social demo evidence and reuse notes | `data/x_demos.json` | `scripts/curate_x.py` |
| `docs/CATALOG.md` — broad categorized directory | `data/catalog.json` | `scripts/curate.py` |

GitHub displays the `.github` README before the root README. This deliberate separation keeps a short, useful editorial homepage without deleting or fighting the existing automated inventory. See [GitHub's README documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).

## Add an X demo

Add a record to `data/x_demos.json`. Use a canonical status URL, the correct creator and repository, a direct primary project source, a concrete Jev role, a reusable pattern, limitations, and an accurate source-review date. Keep `post_status` as `indexed-reference` when only a secondary index or existing attribution identifies the social post. Use `primary-post-reviewed` only after actually inspecting the original post. Source-code review, social-post review, and live execution are different things.

Roundups belong in the separate `roundups` array. Do not treat the root of a thread as proof that all its replies have been captured, or assume separately discovered demos are members of that thread.

```sh
python3 scripts/curate_x.py
python3 scripts/curate_x.py --check
python3 -m unittest discover -s tests -v
```

Commit the source data/template and both generated editorial files. The four-hour refresh runs the same generator and commits only explicitly allowed generated outputs. It does not log into X, scrape hidden replies, install third-party projects, or spend inference credits. The broader catalog's independent discovery continues separately.

## Publish writing responsibly

`DEVTO_DRAFT.md` is a draft, not a live DEV post. Do not auto-publish it, claim an account was created, or imply human experimentation that has not happened. `REPOSITORY_SETTINGS.md` contains prepared sidebar metadata, not proof that the GitHub About fields were changed. Keep work status accurate in subsequent updates.
