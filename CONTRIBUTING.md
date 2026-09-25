# Contributing a Jev resource

[Start here](README.md) · [Curation policy](docs/CURATION.md) · [Editorial workflow](docs/EDITORIAL_WORKFLOW.md)

Submit a public project where Jev has a concrete role, or a clearly labeled independent reproduction/evaluation. Include the repository, original creator, companion demo, actual skill/code link where available, and a short explanation of the typed-decision step. Disclose affiliation. Avoid empty repositories, generic type-safety libraries, duplicate links, and unsupported performance claims.

For a primary-source-reviewed project, add an entry to `data/curated.json`:

```json
{
  "name": "Project name",
  "repo": "owner/repository",
  "category": "demos",
  "description": "What state Jev judges and how the application uses the answer.",
  "evidence": "https://github.com/owner/repository/blob/main/README.md",
  "reviewed": "YYYY-MM-DD"
}
```

Replace the placeholders with real source details and a real review date. A repository-less project uses `url` instead of `repo`. Optional fields: `demo`, `skill`, `code`, `post`, `license`, `notes`, `kind`. Use only links and licenses actually found; disclose access requirements, mock/replay modes, private data handling, and paid APIs.

Categories: `official`, `skills`, `games`, `demos`, `browser`, `agents`, `apps`, `sdks`, `integrations`, `research`, `lists`, `articles`.

Use `data/x_demos.json` for canonical X references and `data/media.json` for visual selections. Preserve the distinction between a retrieved primary post and an indexed reference. Do not upload unlicensed social recordings. For removal, follow the [persistent-exclusion process](docs/CURATION.md#correct-demote-or-remove) so imports cannot restore the item.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
```

Edit root `README.md` directly when proposing a front-page selection. Use `- [Project](URL) - Description.` with a concise, objective description beginning with a capital and ending in a period. Keep `Contents` first, use its existing categories, and leave `Contributing` and `Footnotes` out of the contents list. Do not add archived, undocumented, or deprecated projects to the front page; preserve useful historical material in the supporting catalog with clear notes.

Commit source changes and generated supporting views together. `scripts/build.py` checks the editorial README against `data/curated.json` and exclusions, but never rewrites it. `templates/README.md` controls `docs/DIRECTORY.md`, which retains the original demo gallery and quick-start. The builder also maintains reviewed evidence, the catalog, viewer, freshness, and X/media indexes. Do not recreate `.github/README.md` or use the disabled legacy publishing CLIs.

Run the upstream formatting checker separately with Node.js 20+ and Git:

```sh
npx --yes --ignore-scripts awesome-lint@2.3.0 README.md
```

Use the complete default rule set without local suppressions and record actual diagnostics. Version 2.3.0 disables its age rule upstream; the separate 30-day requirement still applies. A successful lint does not establish maturity, non-AI authorship, or acceptance. See [Awesome submission status](docs/AWESOME_SUBMISSION.md). AI assistance must be disclosed honestly; direct editing does not make past AI-assisted work human-authored.

For new original list text contributed under these guidelines, apply CC0 to the rights you own. Original code contributions remain MIT. Existing contributions, imported metadata, and media keep their original terms; see [licensing scope](LICENSING.md).

Primary-source review is not a security audit, execution test or benchmark reproduction. Preserve provenance and distinguish independent implementations from the official Jev model. No third-party project needs to be installed or executed to contribute a listing.

### Test portability

Repository text files are UTF-8; pass `encoding='utf-8'` when using `Path.read_text` or `Path.write_text`. Run `python -m unittest discover -s tests -v` for the full suite. Publisher integration tests also require Git and Bash; they are skipped explicitly when either is unavailable. The codec regression simulates a cp1252 default rather than claiming a native Windows run.

Issues and PRs are reviewed on a separate four-hour schedule. An author submission is a lead, not automatic acceptance; see [maintenance notes](docs/MAINTENANCE.md).
