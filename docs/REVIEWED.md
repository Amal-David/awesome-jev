# Reviewed Jev picks

[Start here](../README.md) · [Browse by task](START_HERE.md) · [Search and filters](BROWSE.md) · [Full catalog](CATALOG.md)

**17 selections reviewed against primary public sources.** Source review is not a security audit or a reproduced benchmark.

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

