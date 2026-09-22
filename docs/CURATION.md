# Curation, deduplication and removal

[Start here](../README.md) · [Reviewed picks](REVIEWED.md) · [Contribute](../CONTRIBUTING.md) · [Freshness](STATUS.md)

## What belongs here

A concrete TypeSafe Jev demo, project, skill, SDK, integration, reusable code example, technical explanation or explicitly labeled independent reproduction. Each editorial entry must explain what Jev decides and link to primary evidence. Prefer the original creator's repository and post. Include privacy/setup limits and available license information without inventing missing code or rights.

Exclude unrelated projects named Jev, generic type-safety libraries, content without an identifiable Jev role, duplicates, misleading mock-as-live claims, and unsupported quantitative claims. An entry can be useful without a large star count. Listing a project is not an endorsement.

## Evidence is not a score

| Label | Meaning | How it gets there |
|---|---|---|
| Reviewed | Primary source inspected; not an execution test or security audit | Maintainer edits `data/curated.json` with evidence and a real review date |
| Indexed | Attributed community discovery | Community import; not independently reviewed here |
| Auto-discovered | Explicit Jev and TypeSafe/System One README match | Bounded automatic search; not editorial approval |

Media has separate access receipts: a reachable image or video does not prove that the demo ran live. Benchmark claims need attribution and measurement boundaries. Independent reproductions are not official Jev model releases.

## Canonical links and duplicates

Repository keys use lowercase `owner/name`, ignoring a `.git` suffix. For URL-only entries, retain meaningful query parameters and normalize the host/trailing slash using the catalog's canonicalization function. Multiple posts about one project can be evidence for the same entry rather than duplicate projects. A multi-tool repository should describe subprojects clearly and link to their actual paths.

## Correct, demote or remove

For a factual correction, edit the editorial entry and its evidence. To stop presenting a project as reviewed, remove it from `data/curated.json`; the unified builder demotes a retained cached copy to Indexed, rather than leaving an orphaned Reviewed badge.

For complete removal, also add a record to `data/exclusions.json`. Exclusions are applied after every import/discovery pass, so the automatic updater cannot reintroduce the entry. Each requires a canonical `key`, `reason`, public `source`, and ISO `date`. For example, the key for a repository is `repo:owner/project`; use a real public correction, successor or issue URL as the source. Do not put private vulnerability details or personal data into this public log.

An entry cannot be both curated and excluded: validation fails until the conflict is resolved. To restore an entry, remove its exclusion after source review and add it to the appropriate catalog source. Source/license/access changes can justify a correction or exclusion. A transient media check failure alone is not proof that a project should disappear.

## Rebuild and review

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
```

The four-hour workflow runs the same unified builder with explicit network flags and only publishes validated outputs. It does not execute discovered projects or install their skills. Review the diff, including generated pages, before merging a contribution.
