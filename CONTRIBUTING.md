# Contributing a Jev resource

Submit a public project where Jev has a concrete role, or a clearly labeled independent reproduction or evaluation. Include the repository, companion demo, actual skill/code link where available, and a short explanation of the typed-decision step. Avoid empty repositories, generic type-safety libraries, duplicate links, and unsupported performance claims.

Add a primary-source-reviewed entry to `data/curated.json`:

```json
{
  "name": "Project name",
  "repo": "owner/repository",
  "category": "demos",
  "description": "What state Jev judges and what the application does with its answer.",
  "evidence": "https://github.com/owner/repository/blob/main/README.md",
  "reviewed": "YYYY-MM-DD"
}
```

For a project without a repository use `url` instead of `repo`. Optional fields: `demo`, `skill`, `code`, `post`, `license`, `notes`, and `kind`. Use only links and license information you actually found. A companion website need not be a working unauthenticated live demo; state access limits when known.

Allowed categories: `official`, `skills`, `games`, `demos`, `browser`, `agents`, `apps`, `sdks`, `integrations`, `research`, `lists`, `articles`.

```sh
python3 scripts/curate.py
python3 -m unittest discover -s tests -v
python3 scripts/curate.py --check
```

Commit the seed and generated changes together. Primary-source review does not mean the demo was executed or its benchmark reproduced. Preserve provenance and clearly distinguish independent implementations from the official Jev model.
