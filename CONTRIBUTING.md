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

Commit source changes and generated changes together. The unified builder keeps both READMEs, reviewed picks, catalog, local viewer, freshness, X and media pages consistent. Edit `templates/README.md` for hierarchy or menu changes; do not edit generated READMEs. Do not run the older component scripts' standalone CLIs for publication.

Primary-source review is not a security audit, execution test or benchmark reproduction. Preserve provenance and distinguish independent implementations from the official Jev model. No third-party project needs to be installed or executed to contribute a listing.
