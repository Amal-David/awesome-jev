# Awesome Jev

**Watch the demo. Find the code. Understand the decision.**

A community directory of **TypeSafe Jev demos, repositories, agent skills, reusable code, and practical integrations** — with a dedicated collection of demos shared on X.

[Curated X demos](https://github.com/Amal-David/awesome-jev/blob/main/docs/X_DEMOS.md) · [Reviewed projects](https://github.com/Amal-David/awesome-jev/blob/main/README.md) · [Full catalog](https://github.com/Amal-David/awesome-jev/blob/main/docs/CATALOG.md) · [Code examples](https://github.com/Amal-David/awesome-jev/tree/main/examples) · [Contribute a demo](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml)

## Start here

**Want to build?** Start with the [official TypeSafe skill](https://github.com/typesafe-ai/skills), [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python), [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js), and [live documentation](https://docs.typesafe.ai).

**Want ideas?** Browse the X demos below, then follow each implementation. The [full directory](https://github.com/Amal-David/awesome-jev/blob/main/docs/CATALOG.md) also covers games, applications, MCP servers, SDKs, integrations, and independent reproductions.

**Want reusable patterns?** Read the [offline-first examples](https://github.com/Amal-David/awesome-jev/blob/main/examples/README.md) and [curator skill](https://github.com/Amal-David/awesome-jev/blob/main/skills/jev-curator/SKILL.md). A useful pattern is: observed state → bounded candidates → typed judgment → validated action.

## Curated X demos

Inspired by [Moritz Kremb's Jev project roundup](https://x.com/moritzkremb/status/2100895894287839255). This is a growing, separately researched selection, **not a claim that every reply in that thread has been captured**.

| Demo | What Jev does | Watch / inspect |
|---|---|---|
| **Voice-controlled browser** — @moritzkremb | Maps partial speech transcripts to typed intents and observed page targets; Playwright executes the selected action. | [X demo](https://x.com/moritzkremb/status/2100577979021832365) · [repo](https://github.com/moritzkremb/jev-voice-browser) · [source](https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md#how-a-decision-is-made) |
| **Browser Use × Jev Ultrafast** — @gregpr07 | Chooses an operation and compatible DOM target in one decision cycle; a separate model supplies typing text. | [X demo](https://x.com/gregpr07/status/2100411066966749359) · [repo](https://github.com/browser-use/jev-ultrafast) · [source](https://github.com/browser-use/jev-ultrafast/blob/main/README.md#the-action-space) |
| **macOS computer use** — @awlevin | Selects desktop actions from OCR and accessibility-derived state, with a separate writer for free text. | [X demo](https://x.com/awlevin/status/2100262612428894676) · [repo](https://github.com/awlevin/typesafe-computer-use) · [source](https://github.com/awlevin/typesafe-computer-use/blob/main/README.md#how-a-step-works) |
| **Foreman coding-agent supervisor** — @JoshARosen | Assesses coding-worker progress and verification needs while deterministic policy decides interventions. | [X demo](https://x.com/JoshARosen/status/2100573432089866717) · [repo](https://github.com/thruwire/foreman) · [source](https://github.com/thruwire/foreman/blob/main/README.md#what-is-foreman) |
| **Jev trading-loop demonstration** — @jarrodwatts | Uses typed buy/sell judgments in an order-book loop, while code owns quoting, limits, and execution. | [X demo](https://x.com/jarrodwatts/status/2100356151468585346) · [repo](https://github.com/jarrodwatts/jev-trader) · [source](https://github.com/jarrodwatts/jev-trader/blob/main/README.md#run) |

**Evidence matters:** the linked project documentation was inspected. X URLs are indexed social references where the original post could not be fully retrieved. No demo was executed and no timing, cost, or trading claim was independently reproduced. [Read the source-access notes and reuse patterns](https://github.com/Amal-David/awesome-jev/blob/main/docs/X_DEMOS.md).

## What makes this directory useful

Every editorial selection should answer three questions: **what does Jev decide, where is the implementation, and what can you reuse?** Missing source code stays missing; a social video is not an open-source license; a mock or replay is not a live model result.

The larger catalog separates **primary-source-reviewed**, **community-indexed**, and **automatically README-matched** entries. Those labels describe evidence, not a security certification or an endorsement. Independent reproductions are not official Jev weights or proof of equivalent quality.

## About Jev

Jev is TypeSafe AI's typed-decision model: application code supplies state and questions, and consumes typed judgments rather than generated prose. The surrounding code still owns permissions, exact calculations, legal actions, validation, and consequences. Consult the [official docs](https://docs.typesafe.ai) for the current API and model behavior.

This repository is maintained by [Amal-David](https://github.com/Amal-David) and community contributors. It is **unofficial** and not endorsed by TypeSafe AI. Original directory scripts, examples, and writing use the repository's [MIT terms](https://github.com/Amal-David/awesome-jev/blob/main/LICENSE); imported metadata and linked projects retain their own licenses.

## Updated every four hours

The [repository-native refresh workflow](https://github.com/Amal-David/awesome-jev/actions/workflows/curate.yml) searches public GitHub sources, refreshes the broad catalog, and validates this editorial page. It does not run discovered projects, install skills, trade, or spend model credits. GitHub can delay scheduled starts; the run history shows actual executions.

X curation is an editorial input, not an authenticated X scraper. New selections go into [data/x_demos.json](https://github.com/Amal-David/awesome-jev/blob/main/data/x_demos.json); the generator keeps the homepage and X index consistent without replacing them with bulk discoveries.

## Contribute

Found a good demo? [Submit its X post, repository, and concrete Jev role](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml), or open a PR. Include the original creator, direct evidence, any mock/offline mode, privacy requirements, and license information. See [CONTRIBUTING.md](https://github.com/Amal-David/awesome-jev/blob/main/CONTRIBUTING.md) and [SECURITY.md](https://github.com/Amal-David/awesome-jev/blob/main/SECURITY.md).

**Star this repository to bookmark the collection.** A useful contribution is even better: one working source link, one corrected claim, or one well-explained demo.
