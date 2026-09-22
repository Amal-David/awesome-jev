# Curated X demos

[Repository homepage](https://github.com/Amal-David/awesome-jev#readme) · [JSON source](../data/x_demos.json)

Watch the original post, then inspect the implementation. The project descriptions below are based on the linked authors' repository documentation. They are not live execution tests or security endorsements.

## Roundup that seeded this collection

[Moritz Kremb's Jev project roundup](https://x.com/moritzkremb/status/2100895894287839255)

User-supplied discovery seed. The root post introduces a roundup of Jev projects; not all replies were accessible. The demos below were researched separately and must not be represented as a complete extraction of this thread.

## Demos and code

| Demo | What Jev does | Watch / inspect |
|---|---|---|
| **Voice-controlled browser** — @moritzkremb | Maps partial speech transcripts to typed intents and observed page targets; Playwright executes the selected action. | [X demo](https://x.com/moritzkremb/status/2100577979021832365) · [repo](https://github.com/moritzkremb/jev-voice-browser) · [source](https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md#how-a-decision-is-made) |
| **Browser Use × Jev Ultrafast** — @gregpr07 | Chooses an operation and compatible DOM target in one decision cycle; a separate model supplies typing text. | [X demo](https://x.com/gregpr07/status/2100411066966749359) · [repo](https://github.com/browser-use/jev-ultrafast) · [source](https://github.com/browser-use/jev-ultrafast/blob/main/README.md#the-action-space) |
| **macOS computer use** — @awlevin | Selects desktop actions from OCR and accessibility-derived state, with a separate writer for free text. | [X demo](https://x.com/awlevin/status/2100262612428894676) · [repo](https://github.com/awlevin/typesafe-computer-use) · [source](https://github.com/awlevin/typesafe-computer-use/blob/main/README.md#how-a-step-works) |
| **Foreman coding-agent supervisor** — @JoshARosen | Assesses coding-worker progress and verification needs while deterministic policy decides interventions. | [X demo](https://x.com/JoshARosen/status/2100573432089866717) · [repo](https://github.com/thruwire/foreman) · [source](https://github.com/thruwire/foreman/blob/main/README.md#what-is-foreman) |
| **Jev trading-loop demonstration** — @jarrodwatts | Uses typed buy/sell judgments in an order-book loop, while code owns quoting, limits, and execution. | [X demo](https://x.com/jarrodwatts/status/2100356151468585346) · [repo](https://github.com/jarrodwatts/jev-trader) · [source](https://github.com/jarrodwatts/jev-trader/blob/main/README.md#run) |

## Reuse patterns and evidence

### Voice-controlled browser

**Pattern:** Speech recognition → structured page state → parallel typed questions → explicit act, wait, clarify, or confirm policy.

**Source review:** 2026-09-21. [Primary project source](https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md#how-a-decision-is-made).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review.

**Limitations:** The project documents a loopback control server, a persistent browser profile, and external speech processing. Do not expose the control port or use sensitive logged-in accounts. Published timings are author measurements, not reproduced here.

### Browser Use × Jev Ultrafast

**Pattern:** Regenerate the legal action space from observations; ask speculative target questions together; execute only the chosen branch.

**Source review:** 2026-09-21. [Primary project source](https://github.com/browser-use/jev-ultrafast/blob/main/README.md#the-action-space).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review.

**Limitations:** The author's flight-search video is a narrow task demonstration, not general browser reliability. Real runs use paid APIs and an existing browser profile; the documented flight example stops at results, not booking.

### macOS computer use

**Pattern:** Convert screen observations into indexed choices; keep deterministic parsing and execution outside the model.

**Source review:** 2026-09-21. [Primary project source](https://github.com/awlevin/typesafe-computer-use/blob/main/README.md#how-a-step-works).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review.

**Limitations:** Requires macOS screen-recording and accessibility permissions. The project documents a dry-run default and an explicit --act switch. Screen text can contain private information; listed cost and speed comparisons are not independently reproduced.

### Foreman coding-agent supervisor

**Pattern:** Separate the generative worker from an independent, bounded semantic-supervision loop.

**Source review:** 2026-09-21. [Primary project source](https://github.com/thruwire/foreman/blob/main/README.md#what-is-foreman).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review.

**Limitations:** An architectural experiment, not a demonstrated replacement for tests or code review. Bounded diffs, worker output, and repository instructions may enter inference requests; review data handling and worker permissions first.

### Jev trading-loop demonstration

**Pattern:** Bound one decision cycle, reject late answers, and distinguish simulated outcomes from live execution.

**Source review:** 2026-09-21. [Primary project source](https://github.com/jarrodwatts/jev-trader/blob/main/README.md#run).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review.

**Limitations:** The README says the default model is mock and no PRIVATE\_KEY means dry-run; its documented deployment is dry-run/mock. A dashboard is not proof of live Jev inference, profitable trading, or safe custody. No wallet, deployment, or paid call was used for this review.

## Curation rules

Edit `data/x_demos.json`, not the generated tables. Keep canonical X status URLs and direct author/project evidence. Distinguish a post reference from a fully reviewed post; never infer that every entry belongs to the same thread. Do not invent repositories, copy unlicensed media, or treat reported timing, cost, or profit as independently reproduced.

Run `python3 scripts/build.py` and `python3 scripts/build.py --check`. The four-hour workflow validates and preserves this section; it does not authenticate to X or autonomously scrape every thread reply. New editorial selections require source review.
