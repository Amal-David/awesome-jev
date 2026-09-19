# Awesome Jev

A living directory of **Jev demos, repositories, skills, reusable code, integrations, and independent reproductions**.

**705 catalog entries · 622 repository links · 119 companion demo/site links · 17 primary-source-reviewed selections**

[Full categorized catalog](docs/CATALOG.md) · [Machine-readable data](data/catalog.json) · [Code examples](examples/README.md) · [Agent skill](skills/jev-curator/SKILL.md) · [Refresh history](https://github.com/Amal-David/awesome-jev/actions/workflows/curate.yml)

Jev is TypeSafe AI's typed-decision model, not a text generator. Start with the [official skill](https://github.com/typesafe-ai/skills), [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python), and [live docs](https://docs.typesafe.ai). Independent reproductions are not official Jev weights or evidence of equivalent quality. This directory is unofficial and is not endorsed by TypeSafe AI.

## How to use this directory

The selections below were reviewed against primary public sources. The **full catalog** also contains attributed community-indexed entries and automatically README-matched discoveries. These evidence levels are not interchangeable. Source review is not a successful execution test, security audit, benchmark replication, or endorsement. Companion sites may require login, API keys, credits, or local setup.

Missing licenses are marked **not-checked**, **not-detected**, or **NOASSERTION**, rather than assumed open source. Always inspect the project's own license, data rights, and usage terms before reuse. API credentials must stay server-side. Do not run downloaded code or install a skill simply because it appears here.

## Official resources

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| TypeSafe JavaScript SDK | Official JavaScript and TypeScript client with answer types inferred from named questions. | [repo](https://github.com/typesafe-ai/typesafe-sdk-js) · [code](https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/src/types.ts) · [evidence](https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/README.md) | primary-source-reviewed / 2026-09-18 | MIT |
| TypeSafe Python SDK | Official Python client; its quickstart routes a support ticket using a typed Choice. | [repo](https://github.com/typesafe-ai/typesafe-sdk-python) · [demo](https://docs.typesafe.ai/sdk/python) · [code](https://github.com/typesafe-ai/typesafe-sdk-python/blob/main/README.md#quickstart) · [evidence](https://github.com/typesafe-ai/typesafe-sdk-python/blob/main/README.md) | primary-source-reviewed / 2026-09-18 | MIT |

## Skills and reusable agent workflows

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| Jev Logs | Scores log records with typed questions to route selected records for deeper analysis while preserving the archive. | [repo](https://github.com/reachjalil/jevlogs) · [skill](https://github.com/reachjalil/jevlogs/blob/main/skills/jevlogs/SKILL.md) · [evidence](https://github.com/reachjalil/jevlogs/blob/main/skills/jevlogs/SKILL.md) | primary-source-reviewed / 2026-09-18 | MIT |
| Jevify | Reusable discovery skill that finds Jev opportunities, designs question packs, and proposes comparison experiments. Independent skill, not the model or an official SDK. | [repo](https://github.com/altryne/jevify) · [demo](https://thursdai.news) · [skill](https://github.com/altryne/jevify/blob/main/SKILL.md) · [evidence](https://github.com/altryne/jevify/blob/main/README.md) | primary-source-reviewed / 2026-09-18 | MIT |
| Official TypeSafe skill | Official agent skill for choosing primitives, composing typed decisions, and evaluating integrations. | [repo](https://github.com/typesafe-ai/skills) · [demo](https://typesafe.ai) · [skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) · [evidence](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) | primary-source-reviewed / 2026-09-18 | MIT |
| Skillbox | Self-hosted versioned skill library with optional Jev-based task-aware recommendations and deterministic fallback. Jev is an optional recommender, not required for the core library. | [repo](https://github.com/kitze/skillbox) · [skill](https://github.com/kitze/skillbox/blob/main/bootstrap/SKILL.md) · [evidence](https://github.com/kitze/skillbox) | primary-source-reviewed / 2026-09-18 | MIT |

## Games and simulations

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| Jev Plays Snake | Code computes legal moves and board facts; Jev chooses one direction per game tick. Useful separation of legal-action generation, model choice, deadlines, and local execution. | [repo](https://github.com/sorrycc/typesafe-snake) · [code](https://github.com/sorrycc/typesafe-snake/blob/main/src/jev/prompt.ts) · [evidence](https://github.com/sorrycc/typesafe-snake) | primary-source-reviewed / 2026-09-18 | not-detected |
| JevPilot | Three.js driving simulation where Jev selects from locally generated steering and speed candidates. Simulation only; not an autonomous-driving safety system. The hosted demo may require login. | [repo](https://github.com/standardagents/jevpilot) · [evidence](https://github.com/standardagents/jevpilot) | primary-source-reviewed / 2026-09-18 | not-detected |
| PROMPT FPS / Jev Doom | Chocolate Doom WASM instances expose structured state; Jev chooses tactical macros executed by local controllers. Ships Freedoom, not commercial Doom assets. Engine and content have separate GPL/BSD notices; inspect licenses/. | [repo](https://github.com/lukaske/jev-doom-agent) · [evidence](https://github.com/lukaske/jev-doom-agent/blob/main/README.md) | primary-source-reviewed / 2026-09-18 | not-detected |
| TypeSafe Mario | An emulator-state parser supplies structured telemetry; Jev selects bounded NES controller inputs. Requires a lawful local game setup; repository does not include Nintendo ROMs. | [repo](https://github.com/fhshaik/typesafe-mario) · [evidence](https://github.com/fhshaik/typesafe-mario) | primary-source-reviewed / 2026-09-18 | not-detected |

## Demos and playgrounds

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| Jev Music Playground | Jev selects composition enums; deterministic code expands them into notation, playback, and MIDI. Includes an explicitly labeled offline heuristic mode; Jev does not directly generate audio. | [repo](https://github.com/wustep/jev-playground) · [demo](https://jev-playground.vercel.app) · [code](https://github.com/wustep/jev-playground/blob/main/src/planner/JevPlanner.ts) · [evidence](https://github.com/wustep/jev-playground/blob/main/README.md) | primary-source-reviewed / 2026-09-18 | not-detected |

## Browser and computer use

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| Jev Ultrafast | Selects browser operation and observed DOM target with Jev; a separate model generates typing text. Published timing is a narrow author-run demonstration, not a general reliability guarantee. | [repo](https://github.com/browser-use/jev-ultrafast) · [demo](https://browser-use.com) · [code](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/jev_ultrafast/model.py) · [post](https://x.com/gregpr07/status/2100411066966749359) · [evidence](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md) | primary-source-reviewed / 2026-09-18 | MIT |

## Agent tooling and MCP

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| Foreman | Uses independent Noul checks to supervise a coding worker while deterministic policy decides interventions. Architectural experiment; its README provides an offline deterministic demo. | [repo](https://github.com/thruwire/foreman) · [demo](https://thruwire.ai) · [post](https://x.com/JoshARosen/status/2100573432089866717) · [evidence](https://github.com/thruwire/foreman) | primary-source-reviewed / 2026-09-18 | MIT |
| Jev MCP | MCP tools use Jev to verify claims against evidence, screen incoming content, and rank candidates. Review tool permissions and environment handling before installation. | [repo](https://github.com/jkudish/jev-mcp) · [post](https://x.com/0xLogicrw/status/2100478725393686556) · [evidence](https://github.com/jkudish/jev-mcp) | primary-source-reviewed / 2026-09-18 | MIT |
| TypeSafe MCP | Go MCP server exposing typed Jev judgments to coding agents, with documented client setup and retries. | [repo](https://github.com/itsmostafa/typesafe-mcp) · [post](https://x.com/0xLogicrw/status/2100478725393686556) · [evidence](https://github.com/itsmostafa/typesafe-mcp) | primary-source-reviewed / 2026-09-18 | MIT |

## Integrations

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| Home Assistant Jev | Turns Jev probability, choice, and score answers into Home Assistant entities and automation results. Inspect the example automations and keep consequential actions behind explicit policy. | [repo](https://github.com/AboveColin/HA-Jev) · [evidence](https://github.com/AboveColin/HA-Jev) | primary-source-reviewed / 2026-09-18 | MIT |

## Research and independent reproductions

| Project | Jev role / reuse notes | Links | Evidence | License / status |
|---|---|---|---|---|
| OpenJev SGLang | Independent API-compatible typed-decision server using open-model label probabilities through SGLang. Not official Jev weights; no requests go to TypeSafe. Review deployment authentication and GPU costs. | [repo](https://github.com/ekzhang/openjev-sglang) · [code](https://github.com/ekzhang/openjev-sglang/tree/main/examples) · [evidence](https://github.com/ekzhang/openjev-sglang) | primary-source-reviewed / 2026-09-18 | not-detected |

## Continuous refresh

The repository-native [GitHub Actions workflow](.github/workflows/curate.yml) runs every four hours at **00:23, 04:23, 08:23, 12:23, 16:23, and 20:23 UTC** (**05:53, 09:53, 13:53, 17:53, 21:53, and 01:53 IST**). It can also be run manually from Actions.

It imports the attributed CC0 community directory, independently searches GitHub, checks up to 30 candidate READMEs, rotates up to 100 repository metadata checks, deduplicates canonical links, refreshes the catalog and README, and commits only changed files. It preserves prior records when sources fail. It does not execute third-party code, install third-party skills, spend model credits, or promote automatic discoveries into editorially reviewed selections. No extra API key is needed beyond the built-in repository-scoped GITHUB_TOKEN.

This is a scheduled discovery and metadata pipeline, **not an always-running research agent or a claim to cover every demo on the internet**. Private Discord channels, login-only posts, deleted links, and undiscovered projects may be absent. Searches are bounded and unfinished candidates persist for later runs. GitHub may delay or drop scheduled jobs and disables inactive public-repository schedules after 60 days; consult [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). The Actions history is the source of truth for actual executions.

## Contribute and reuse

Edit [data/curated.json](data/curated.json) for primary-source-reviewed additions. See [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), and [SOURCES.md](SOURCES.md). Generated files are rebuilt with `python3 scripts/curate.py`. Validate with `python3 -m unittest discover -s tests -v` and `python3 scripts/curate.py --check`.

Original scripts, examples, and writing are MIT licensed. Imported metadata retains its stated source license. Linked projects retain their own licenses.
