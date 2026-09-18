# Sources, provenance, and coverage

## Independently reviewed selections

The initial `data/curated.json` contains 17 selections inspected against their public primary README, skill, or SDK source on September 18, 2026. Each entry records its evidence URL. Descriptions and reuse notes in that file are original summaries. This means source review, not a successful live execution, security audit, or benchmark replication.

Official API examples were checked against [TypeSafe's JavaScript request/response types](https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/src/types.ts), the [official Python SDK quickstart](https://github.com/typesafe-ai/typesafe-sdk-python/blob/main/README.md), and the [official agent skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md). The live documentation host could not be fetched from the initial research environment, so version-sensitive code was grounded in these official repository sources instead. Future changes should recheck live docs.

## Attributed community metadata

The broad initial discovery source is [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev), specifically [data/projects.json](https://github.com/hellogumbo/awesome-jev/blob/main/data/projects.json). Its [license](https://github.com/hellogumbo/awesome-jev/blob/main/LICENSE) is CC0 1.0 Universal. Its public README reported 410 entries when inspected on September 18, 2026; the imported count can change on every refresh.

The scheduled importer verifies the CC0 license header before fetching metadata. Community summaries are attributed in each generated record's `sources`, retained under CC0, and explicitly labeled `community-indexed`. They are not represented as original research or independent verification. Links, stars, and public code availability do not establish an open-source license. No third-party code, media, model weights, or game assets are vendored.

Additional directories useful for manual discovery include [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev), [yibie/awesome-jev](https://github.com/yibie/awesome-jev), [OmniJev/awesome-jev](https://github.com/OmniJev/awesome-jev), [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh), and [Dropday](https://www.dropday.ai/). Their content is not bulk copied by this importer.

## Independent recurring discovery

The workflow also searches GitHub's repository API using three explicit queries in `scripts/curate.py`, with two pages of up to 100 results per query. It checks up to 30 previously pending/new READMEs per run for both Jev and TypeSafe/System One references. It labels these `readme-matched`, not editorially reviewed, and persists unchecked/rejected candidates for later inspection. Default automatic categories are provisional.

Up to 100 repository metadata records are refreshed per run, oldest first. `metadata_checked` dates show actual GitHub metadata lookup dates. API errors retain old records; 404/410 responses are marked unavailable rather than deleted. Hosted demo health and benchmark accuracy are not tested by this workflow. Repository status is not demo status.

This is broad discovery, not exhaustive internet coverage. Private communities, inaccessible posts, deleted sources, and search-ranking/pagination limits create gaps. Scheduled GitHub jobs can be delayed, dropped, or disabled; [Actions history](https://github.com/Amal-David/awesome-jev/actions/workflows/curate.yml) records actual runs. No ChatGPT recurring app-access task was saved; the scheduler lives in GitHub Actions.

## Licensing

Original scripts, skill, examples, and documentation: MIT, see [LICENSE](LICENSE). Imported community metadata: CC0 1.0 Universal as above. Linked projects, dependencies, datasets, and assets retain their own licenses and terms. `not-detected`, `not-checked`, and `NOASSERTION` must not be interpreted as permission for commercial reuse.
