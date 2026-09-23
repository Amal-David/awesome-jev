# Computer use, drivers, and local alternatives

[Start here](../README.md#computer-use-and-drivers) · [Reviewed picks](REVIEWED.md) · [Search and filters](BROWSE.md) · [Original X demos](X_DEMOS.md)

**Source review: 22 September 2026.** This map separates the decision model, execution driver, adapter/skill, and independent local-model research. None of the linked applications was installed or executed for this review.

## Pick the layer you need

**A bounded Jev + Cua example:** start with [Cua's jev-use recipe](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use). **A browser implementation:** compare Jev Ultrafast, Jev Browser, and the smaller browser skill below. **An existing Codex browser:** inspect Jev Browser Use, which reuses the connection. **Native Mac tools:** compare jev-bot, Jev Cua, and TypeSafe computer use. **A local model rather than hosted Jev:** see the independent-model section.

The responsibility split is: observe the current page/window → construct allowed candidates → choose → authorize and execute through a driver → independently verify the result. A successful delivery receipt or a model's DONE answer is not by itself a verified outcome.

## Jev integrations and adapters

| Project | Execution backend and Jev role | Reuse / important boundary |
|---|---|---|
| [Cua Driver + jev-use](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) | Cua Driver's persistent MCP connection; Python/TypeScript adapters ask hosted TypeSafe Jev to select one bounded candidate ID. | Read the [recipe](https://github.com/trycua/cua/blob/main/libs/cua-driver/examples/jev-use/README.md) and [setup guide](https://cua.ai/docs/how-to-guides/driver/jev-use). Mock proof still operates a browser fixture. Snapshot-bound refs and optional capture-bound visual targets are not arbitrary coordinates. |
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | Browser Harness observes/acts through CDP; Jev selects the operation and compatible DOM target; another model can write text. | The [dependency declaration](https://github.com/browser-use/jev-ultrafast/blob/main/pyproject.toml) names Browser Harness. Browser automation, not a native-desktop driver. |
| [Jev Social](https://github.com/socai-io/jev-social) | The socai CLI operates an existing logged-in Chrome session for Instagram, TikTok, and LinkedIn; Jev selects bounded search, read, inspect, or finish operations from the current evidence. | [README](https://github.com/socai-io/jev-social/blob/46c0db23864b550dee8600b48a47d214eeaa251d/README.md) and [action construction](https://github.com/socai-io/jev-social/blob/46c0db23864b550dee8600b48a47d214eeaa251d/src/actions.js). OpenRouter receives the research goal and selected evidence snippets; socai owns browser execution. Media download is offered only after explicit user intent. |
| [TypeSafe computer use](https://github.com/awlevin/typesafe-computer-use) | Native macOS OCR/accessibility observations become indexed action choices; Jev selects, with separate writing help where configured. | [README](https://github.com/awlevin/typesafe-computer-use/blob/main/README.md). Requires desktop permissions; screen text can reach inference services. Author speed/cost comparisons were not reproduced. |
| [Jev voice browser](https://github.com/moritzkremb/jev-voice-browser) | Playwright Chromium; partial speech and page controls become typed intents, targets, and act/wait/confirm checks. | [README](https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md). Keep its control server on loopback and avoid sensitive persistent profiles. Not a Cua Driver binding. |
| [Jev Browser Skill](https://github.com/zurfyx/jev-browser-skill) | A small browser reference builds a control table and selects a compatible action/target using Jev. | [README and code pointers](https://github.com/zurfyx/jev-browser-skill/blob/main/README.md), [recorded step-through](https://jev-browser.vercel.app). Deliberately limited; a short successful demo is not universal support. |
| [Jev Browser](https://github.com/jkudish/jev-browser) | Its own Playwright Chromium through MCP, CLI, or library; Jev selects actions and judges progress. | [README](https://github.com/jkudish/jev-browser/blob/main/README.md). Installation can download Chromium. Live use sends page information and may use another text provider. |
| [Jev Browser Use](https://github.com/wy-coliney/jev-browser-use) | Reuses the existing Codex Computer Use connection; Jev handles navigation/clicks/scrolling while the host types and verifies. | [README](https://github.com/wy-coliney/jev-browser-use/blob/main/README.md). Installing the skill does not install a driver. Other-client browser execution is not yet supported in the inspected README; installability is not execution compatibility. |

## Local runtimes with optional hosted Jev

| Project | What remains local | Where Jev participates |
|---|---|---|
| [Eronmmer/jev-cua](https://github.com/Eronmmer/jev-cua) | Cua-backed native Mac actions and exact compiled workflows. The README describes opaque refs, approval gates, fresh rebinding, and exact postconditions. | Optional workflow routing sends a best-effort-redacted request and reviewed descriptions to TypeSafe. It recommends a workflow, not arbitrary executable arguments. [Data boundary](https://github.com/Eronmmer/jev-cua/blob/main/README.md#data-boundary). |
| [stoopid-computers/jev-bot](https://github.com/stoopid-computers/jev-bot) | Cua-backed native observations and direct element-number actions in a persistent JavaScript session. | Optional semantic control selection uses TypeSafe Jev. [README](https://github.com/stoopid-computers/jev-bot/blob/main/README.md). Package: `@compootor/jev-bot`, not the unrelated support-bot repository with the same short name. |

A **local runtime is not a local Jev model**. Jev Cua's screenshot fallback may disclose window pixels to the connected AI client/model even when no TypeSafe request is made. Its README pins a specific Driver build; recheck compatibility. jev-bot documents a narrower native-app surface: do not assume tabs, coordinate clicks, dragging, scrolling, or hotkeys exist because its underlying driver has more tools. These source-described safeguards are not an independent security audit.

## Supporting drivers and runtimes — not Jev models

| Component | Why it belongs here | Primary evidence |
|---|---|---|
| [Cua Driver](https://github.com/trycua/cua/tree/main/libs/cua-driver) | Model-neutral observation and input through MCP, CLI, and typed SDKs. jev-use, Jev Cua, and jev-bot compose it with different policies. | [Driver README](https://github.com/trycua/cua/blob/main/libs/cua-driver/README.md); [Jev recipe](https://github.com/trycua/cua/blob/main/libs/cua-driver/examples/jev-use/README.md). TypeSafe-specific code stays outside Driver. |
| [Browser Harness](https://github.com/browser-use/browser-harness) | Browser runtime used by Jev Ultrafast; includes an agent skill and an MCP surface. Not all uses involve Jev. | [README](https://github.com/browser-use/browser-harness/blob/main/README.md); [Ultrafast dependency](https://github.com/browser-use/jev-ultrafast/blob/main/pyproject.toml). |

Cua Driver and jev-use live in the **same monorepo**. Their deep links stay distinct here, while the main catalog keeps one canonical `trycua/cua` record rather than inflating the count with duplicate roots. Browser Harness is explicitly labeled `adjacent-infrastructure` in the catalog. A general-purpose library does not qualify merely because it could be used with Jev; require a documented relationship.

## Independent local-model research

| Project | Verified source surface | What must not be inferred |
|---|---|---|
| [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) | Cua-published model repository and paired [form-filling dataset](https://huggingface.co/datasets/cua-ai/cua-s1-forms). Publisher metadata labels both MIT. [GitHub research component](https://github.com/trycua/cua/tree/main/libs/cua-s1). | Not official TypeSafe Jev weights, not a general desktop agent, and no performance result was reproduced here. Check the exact artifact's card, terms, runtime, and evaluation scope. |
| [Jevlike](https://github.com/vinnylarouge/jevlike) | [README](https://github.com/vinnylarouge/jevlike/blob/main/README.md): independent one-pass option scoring, local training/evaluation, and optional visual game examples. | Similar interfaces do not establish equivalent architecture, calibration, or quality. Selected demo windows are not a typical-play benchmark. |
| [OpenJev SGLang](https://github.com/ekzhang/openjev-sglang) | Existing reviewed implementation in the [research section](REVIEWED.md#research-and-independent-reproductions). | Not an official Jev release; check model, hardware, and deployment requirements. Not re-audited in this pass. |

**Artifact-status nuance:** the inspected `libs/cua-s1/README.md` describes a source-only research profile, while the publisher's root README separately links the CUA-S1-FORMS model and dataset on Hugging Face. Both facts can hold. Do not infer that no Hub artifact exists or that every current source profile matches the Hub model. This pass inspected Hub metadata, not downloaded weights or inference.

## What the coverage audit found

At pre-update snapshot [`24e3aca`](https://github.com/Amal-David/awesome-jev/commit/24e3aca5aa470b04ab8978d77dd09e3fc5cf0d40), the directory had 1,275 catalog entries and 22 editorial selections. Exact repo/URL matches were checked, rather than trusting a partial search index.

**Absent from that catalog:** `trycua/cua`, `Eronmmer/jev-cua`, `stoopid-computers/jev-bot`, `browser-use/browser-harness`, and the CUA-S1-FORMS Hub model URL. They are now explicitly included.

**Already indexed, but not in the editorial seed:** TypeSafe computer use, Jev voice browser, Jev Browser Skill, Jev Browser, Jev Browser Use, and Jevlike. Their primary sources were inspected for this update; they now have reviewed entries. Jev Ultrafast was already reviewed.

Other discoveries such as `jcpsimmons/jev-macos-loop`, `paulsmith/computer-use-jev`, `NobleSpartan6/otto`, and `hitakshiA/solari-reflex` were already in the broader catalog. They are **not promoted or security-reviewed by this pass**. Use [the full catalog](CATALOG.md) for their existing labels. This is a targeted audit, not a claim to have enumerated every CUA project.

## Keep this coverage useful

Curated entries persist through the four-hour refresh independently of automatic keyword matches. Automated candidate checks remain bounded and queued; they do not guarantee immediate discovery or editorial review of every dependency. The curator instructions now explicitly follow execution-backend and monorepo example links.

Record the actual model/provider, driver, adapter/skill, observation/action surface, mock/optional paths, outbound-data boundary, and independent verification boundary. Keep the quick-start and original media gallery intact. Do not install drivers, grant permissions, operate a browser, spend inference credits, or download weights merely to curate a source link.
