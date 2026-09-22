# Curated X demos

[Repository homepage](https://github.com/Amal-David/awesome-jev#readme) · [JSON source](../data/x_demos.json) · [OpenRouter winner context](OPENROUTER_SHOWCASE.md)

Open the publisher post, then inspect the linked repository or project page. Website-only demos are labeled project, not source code. These are not live execution tests or security endorsements.

## Roundups and publisher showcases

[Moritz Kremb's Jev project roundup](https://x.com/moritzkremb/status/2100895894287839255)

User-supplied discovery seed. The root post introduces a roundup of Jev projects; not all replies were accessible. The demos below were researched separately and must not be represented as a complete extraction of this thread.

[OpenRouter community winners — 21 September 2026](https://x.com/OpenRouter/status/2102125748723339774)

All five winner posts (2–6) were inspected through the public X mirror, with the narrative cross-checked against OpenRouter's public LinkedIn page. The announcement attributes judging to Jev. This covers the five announced winners, not every submission; it is OpenRouter's designation, not this directory's ranking, security audit, or reproduced benchmark.

## Demos and code

| Demo | What Jev does | Watch / inspect |
|---|---|---|
| **Voice-controlled browser** — @moritzkremb | Maps partial speech transcripts to typed intents and observed page targets; Playwright executes the selected action. | [X demo](https://x.com/moritzkremb/status/2100577979021832365) · [repo](https://github.com/moritzkremb/jev-voice-browser) · [source](https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md#how-a-decision-is-made) |
| **Browser Use × Jev Ultrafast** — @gregpr07 | Chooses an operation and compatible DOM target in one decision cycle; a separate model supplies typing text. | [X demo](https://x.com/gregpr07/status/2100411066966749359) · [repo](https://github.com/browser-use/jev-ultrafast) · [source](https://github.com/browser-use/jev-ultrafast/blob/main/README.md#the-action-space) |
| **macOS computer use** — @awlevin | Selects desktop actions from OCR and accessibility-derived state, with a separate writer for free text. | [X demo](https://x.com/awlevin/status/2100262612428894676) · [repo](https://github.com/awlevin/typesafe-computer-use) · [source](https://github.com/awlevin/typesafe-computer-use/blob/main/README.md#how-a-step-works) |
| **Foreman coding-agent supervisor** — @JoshARosen | Assesses coding-worker progress and verification needs while deterministic policy decides interventions. | [X demo](https://x.com/JoshARosen/status/2100573432089866717) · [repo](https://github.com/thruwire/foreman) · [source](https://github.com/thruwire/foreman/blob/main/README.md#what-is-foreman) |
| **Jev trading-loop demonstration** — @jarrodwatts | Uses typed buy/sell judgments in an order-book loop, while code owns quoting, limits, and execution. | [X demo](https://x.com/jarrodwatts/status/2100356151468585346) · [repo](https://github.com/jarrodwatts/jev-trader) · [source](https://github.com/jarrodwatts/jev-trader/blob/main/README.md#run) |
| **JevAI for XMage** — ShiftSad · featured by @OpenRouter | XMage supplies legal plays; pure and hybrid players use Jev for bounded decisions and selection among searched lines. | [X demo](https://x.com/OpenRouter/status/2102125765773144286) · [repo](https://github.com/ShiftSad/mage) · [source](https://github.com/ShiftSad/mage/blob/master/Mage.Server.Plugins/Mage.Player.JevAI/README.md) |
| **Jev Chess** — sliday · featured by @OpenRouter | A shared internet-versus-Jev chess game visualizes probabilities over legal move candidates. | [X demo](https://x.com/OpenRouter/status/2102125782219075865) · [project](https://jevchess.com/) · [source](https://jevchess.com/) |
| **tisco** — cairodavila · featured by @OpenRouter | Jev searches transcript meaning; code previews and applies approved clip moves and renames. | [X demo](https://x.com/OpenRouter/status/2102125798371283444) · [repo](https://github.com/cairodavila/tisco) · [source](https://github.com/cairodavila/tisco/blob/main/README.md) |
| **Vibe Domain** — OB Studio / Oliver · featured by @OpenRouter | Ranks domain candidates against vibe and keyword preferences, separately from registry and availability checks. | [X demo](https://x.com/OpenRouter/status/2102125815031071157) · [project](https://obstudio.org/tools/vibe-domain/) · [source](https://obstudio.org/tools/vibe-domain/) |
| **jev\_search** — caio0452 · featured by @OpenRouter | Keyword-density code prioritizes files and chunks; Jev judges passages in a fast first pass and a broader second pass. | [X demo](https://x.com/OpenRouter/status/2102125830185075060) · [repo](https://github.com/caio0452/jev_search) · [source](https://github.com/caio0452/jev_search/blob/main/README.md) |

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

### JevAI for XMage

**Pattern:** Separate legal-action generation, deterministic search, semantic choice, and network fallback.

**Source review:** 2026-09-22. [Primary project source](https://github.com/ShiftSad/mage/blob/master/Mage.Server.Plugins/Mage.Player.JevAI/README.md).

**Post access:** Original post text inspected. Publisher post text and screenshot metadata inspected through the public X mirror; narrative cross-checked with OpenRouter's public LinkedIn page. No live execution verified..

**Limitations:** OpenRouter community winner. Plugin inside an XMage fork, not the entire upstream engine. The reported 11-6-3 record belongs to the hybrid across 20 author-run games with turn-cap draws. Hybrid pruning is off by default. No game or benchmark was run here.

### Jev Chess

**Pattern:** Enforce the move set in game code; let a typed model select from observed legal options.

**Source review:** 2026-09-22. [Primary project source](https://jevchess.com/).

**Post access:** Original post text inspected. Publisher post text and screenshot metadata inspected through the public X mirror; public project metadata independently read. No live execution verified..

**Limitations:** OpenRouter community winner. Public project-page metadata inspected; no public source repository or code license verified. No shared game move submitted or result reproduced.

### tisco

**Pattern:** Transcribe separately, judge relevance, surface uncertainty, then require approval for exact file changes.

**Source review:** 2026-09-22. [Primary project source](https://github.com/cairodavila/tisco/blob/main/README.md).

**Post access:** Original post text inspected. Publisher post text and screenshot metadata inspected through the public X mirror; project README and MIT license independently read. No live execution verified..

**Limitations:** OpenRouter community winner. Transcript-based, not visual video understanding. Approved audio uploads and transcript judgments use OpenRouter; the project also documents a synthetic offline demo. No clips, keys, or paid calls were used here.

### Vibe Domain

**Pattern:** Check external facts in code; judge semantic fit only among supplied candidates.

**Source review:** 2026-09-22. [Primary project source](https://obstudio.org/tools/vibe-domain/).

**Post access:** Original post text inspected. Publisher post text and screenshot metadata inspected through the public X mirror; public product page independently read. No live execution verified..

**Limitations:** OpenRouter community winner. Public page inspected; no public source repository or code license verified. The documented no-key heuristic mode is not live Jev. Recheck availability with a registrar and inspect key handling; no scan, purchase, or model call was made.

### jev\_search

**Pattern:** Keep retrieval heuristics separate from model judging and publish useful partial results before the complete scan finishes.

**Source review:** 2026-09-22. [Primary project source](https://github.com/caio0452/jev_search/blob/main/README.md).

**Post access:** Original post text inspected. Publisher post text and screenshot metadata inspected through the public X mirror; README and entry-point code independently read. No live execution verified..

**Limitations:** OpenRouter community winner. Current primary source attributes file prioritization to code rather than Jev. The author marks it fully AI-generated and not for production. Source text reaches OpenRouter; favor environment variables over command-line secrets. No project code was executed.

## Curation rules

Edit `data/x_demos.json`, not the generated tables. Use exactly one `repo` or public project `url`, plus direct evidence from that repository or project. Keep canonical X status URLs and original creator attribution. Record mirror access in `post_access`; a readable publisher post is not live-demo verification. Missing code stays missing. Do not infer that unrelated entries belong to the same thread, copy unlicensed media, or present reported timings as reproduced.

Run `python3 scripts/build.py` and `python3 scripts/build.py --check`. The four-hour workflow preserves and validates this section; it does not authenticate to X or autonomously scrape every reply. New editorial selections require source review.
