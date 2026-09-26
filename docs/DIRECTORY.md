# Jev Project Directory

Generated supporting directory with source notes, the original demo gallery, and discovery status. [Back to the editorial list](../README.md).

Projects, demos, and tools built with [Jev](https://docs.typesafe.ai/).

Jev answers questions about data: pick an option, return a yes/no probability, or score something on a scale. It does not write text. The examples here show what people are using it for, with links to the code where available.

**54 reviewed picks**. <a href="https://github.com/Amal-David/awesome-jev/blob/main/docs/REVIEWED.md">Source notes and licenses</a>. The larger discovery catalog is separate.

[Quick start](#20-second-quick-start) · [Projects](#reviewed-picks) · [Demos from X](#watch-jev-in-action) · [CUA & drivers](#computer-use-and-drivers) · [OpenRouter winners](#openrouter-community-winners) · [Contributing](#contribute)

> Check permissions and data handling before running a project. A listing here is not a security audit.

## 20-second quick-start

Install `typesafe-sdk` and set `TYPESAFE_API_KEY` in your environment. This example makes one paid request:

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    result = client.system_one(
        state={"document": "I was charged twice."},
        questions={"team": Choice(
            instructions="Which team should handle this ticket?",
            criteria={"billing": None, "technical": None, "other": None},
        )},
    )
print(result.choices["team"].choice)  # e.g. billing; actual output can differ
```

No key yet? `python3 examples/route_ticket.py` prints the request without calling the API. [SDK setup](https://github.com/typesafe-ai/typesafe-sdk-python#quickstart).

<a id="choose-your-path"></a>

Start with a [classifier](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#build-your-first-typed-classifier), [an agent](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#use-jev-in-an-agent), or [a local alternative](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#explore-a-local-alternative).

For simple rules, parsing, or arithmetic, use code. A dedicated classifier may be a better fit for a fixed task. Jev is worth trying when the choices change or the input is messy; test it on your own examples rather than relying on a demo's timing.

<a href="https://x.com/gregpr07/status/2100411066966749359"><img src="https://raw.githubusercontent.com/browser-use/jev-ultrafast/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/docs/demo.gif" width="680" alt="Browser Use author recording: Jev selects a browser action and target"></a>

<sub>Browser Use / @gregpr07. Author recording, not our benchmark. <a href="https://github.com/browser-use/jev-ultrafast">Implementation</a> · <a href="#watch-jev-in-action">More demos and videos</a>.</sub>

## Reviewed picks

### SDKs and skills

- <a href="https://github.com/typesafe-ai/typesafe-sdk-js">TypeSafe JavaScript SDK</a> - Official JavaScript and TypeScript client.
- <a href="https://github.com/typesafe-ai/typesafe-sdk-python">TypeSafe Python SDK</a> - Official Python client, with a support-ticket routing example.
- <a href="https://github.com/reachjalil/jevlogs">Jev Logs</a> - Scores log entries with Jev to decide which need a closer look.
- <a href="https://github.com/altryne/jevify">Jevify</a> - Agent skill for finding places to use Jev and planning comparisons with existing code.
- <a href="https://github.com/typesafe-ai/skills">Official TypeSafe skill</a> - Official skill for writing Jev requests and choosing between Noul, Choice, and Score.
- <a href="https://github.com/kitze/skillbox">Skillbox</a> - Self-hosted skill library with optional Jev-based recommendations.
- <a href="https://github.com/simota/tenbin">Tenbin</a> - MCP server and skill for linting Jev questions, evaluating labeled examples, and choosing decision thresholds.
- <a href="https://github.com/suraj-phanindra/wellposed">wellposed</a> - Offline linter and agent skill for Jev requests: checks missing options, broken state references, and question types.
- <a href="https://github.com/luizribeiro/jevrs">jevrs</a> - Async Rust client with typed answers, derive macros, and native or WASI transports.

### Browser and desktop tools

- <a href="https://github.com/trycua/cua">Cua Driver + jev-use</a> - Cua Driver example in Python and TypeScript: Jev chooses an action, the driver runs it, and code checks the result.
- <a href="https://github.com/jkudish/jev-browser">Jev Browser (MCP, CLI, library)</a> - Playwright browser controlled by Jev, available as an MCP server, CLI, or library.
- <a href="https://github.com/zurfyx/jev-browser-skill">Jev Browser Skill</a> - Small browser-control reference showing how to build and execute Jev action choices.
- <a href="https://github.com/wy-coliney/jev-browser-use">Jev Browser Use (existing Codex connection)</a> - Skill that uses an existing Codex browser connection. Jev clicks and scrolls; Codex types and checks the result.
- <a href="https://github.com/Eronmmer/jev-cua">Jev Cua (Codex/Waku)</a> - Mac automation using Cua Driver, with optional Jev recommendations for saved workflows.
- <a href="https://github.com/socai-io/jev-social">Jev Social</a> - Read-only Instagram, TikTok, and LinkedIn research loop: Jev Choice questions pick the platform and each bounded search, read, inspect, or finish operation; socai CLI executes in the user&#x27;s Chrome and the app retains source-linked evidence.
- <a href="https://github.com/browser-use/jev-ultrafast">Jev Ultrafast</a> - Jev picks browser actions and page elements; a separate model writes text.
- <a href="https://github.com/moritzkremb/jev-voice-browser">Jev voice browser</a> - Voice-controlled Playwright browser. Jev chooses actions from partial speech and page controls.
- <a href="https://github.com/stoopid-computers/jev-bot">jev-bot (@compootor)</a> - Native Mac controls through a JavaScript MCP session, with optional Jev element selection.
- <a href="https://github.com/awlevin/typesafe-computer-use">TypeSafe computer use (macOS)</a> - Mac automation using local OCR and accessibility data, with Jev choosing the next action.

### Agent tools

- <a href="https://github.com/thruwire/foreman">Foreman</a> - Uses Jev to check a coding agent&#x27;s progress and decide when it needs intervention.
- <a href="https://github.com/jkudish/jev-mcp">Jev MCP</a> - MCP tools for checking claims against evidence, screening content, and ranking candidates.
- <a href="https://github.com/sutro-sh/jev-align">jev-align</a> - Improves Jev classifiers and scoring rubrics with human labels and GEPA-proposed definition changes.
- <a href="https://github.com/valentynkit/jev-belay">jev-belay</a> - Claude Code Stop hook that checks local run evidence before Jev judges an unverified completion claim.
- <a href="https://github.com/kevnk/jev-claude-statusline">jev-claude-statusline</a> - Claude Code hooks send task text, recent tool summaries, latest assistant message, and turn status to Jev (Score phase plus Noul done/waiting_on_user); answers are cached and shown as a progress segment on the Claude Code status line.
- <a href="https://github.com/libingzheren/Jev-Mem">Jev-Mem</a> - Research agent-memory system where Jev organizes graph memories and guides retrieval; a separate model writes answers.
- <a href="https://github.com/caio0452/jev_search">jev_search</a> - Ranks files by keyword, then checks their passages with Jev in two passes. Author marks it experimental.
- <a href="https://github.com/kyu1204/jgrep">jgrep (npm: jevgrep)</a> - Jev answers one Noul per code chunk, diff hunk, or CSV row (does this match the description?); code prints the probabilities as file:line hits, gates CI on an English rule with --diff, and lists the test files a diff can affect with --tests.
- <a href="https://github.com/bartlomein/oko">Oko</a> - Code-search CLI and MCP server that finds candidates locally and uses Jev to rank the source snippets.
- <a href="https://github.com/tyler-dot-earth/patdown">patdown</a> - Semantic linter that turns Markdown rules into Jev checks and maps flagged evidence back to source lines.
- <a href="https://github.com/itsmostafa/typesafe-mcp">TypeSafe MCP</a> - Go MCP server for making Jev requests from coding agents.
- <a href="https://github.com/GhalebDweikat/winnow">Winnow</a> - Claude Code context filter where Jev scores tool-output blocks and low-relevance blocks stay recallable from a local cache.

### Apps and integrations

- <a href="https://github.com/jerryjliu/docjev">DocJev</a> - Classifies documents and finds packet boundaries with Jev after local parsing or optional cloud OCR.
- <a href="https://github.com/riesvile/nospace">nospace</a> - Adds spaces while you type. Jev chooses between possible word splits; a separate model handles spelling corrections.
- <a href="https://github.com/cairodavila/tisco">tisco</a> - Searches video transcripts with Jev, then previews clip moves and renames for approval.
- <a href="https://obstudio.org/tools/vibe-domain/">Vibe Domain</a> - Ranks domain names by the requested style. Has a no-key heuristic mode and a hosted Jev option.
- <a href="https://github.com/AboveColin/HA-Jev">Home Assistant Jev</a> - Adds Jev decisions to Home Assistant entities and automations.
- <a href="https://github.com/simonw/llm-typesafe">llm-typesafe</a> - Use Jev from the LLM command line or Python, with stdin, templates, and sync/async calls.
- <a href="https://github.com/ttlequals0/MinusPodJev">MinusPodJev</a> - Podcast ad-detection adapter for MinusPod: Jev scores transcript segments and code assembles the ad spans.
- <a href="https://github.com/jexp/neo4jev">neo4jev</a> - Explores Neo4j graphs with Jev edge choices and goal checks inside a bounded beam search.

### Games and creative projects

- <a href="https://jevchess.com/">Jev Chess</a> - A shared chess game against Jev with move probabilities. Hosted demo; source code not verified.
- <a href="https://github.com/sorrycc/typesafe-snake">Jev Plays Snake</a> - Snake where code finds legal moves and Jev picks a direction.
- <a href="https://github.com/valentynkit/jev-plays-pokemon-red">jev-plays-pokemon-red</a> - Pokemon Red agent where code builds legal actions and route state; Jev chooses only at branch points.
- <a href="https://github.com/ShiftSad/mage">JevAI for XMage</a> - Magic: The Gathering bots that use Jev alone or alongside XMage search.
- <a href="https://github.com/standardagents/jevpilot">JevPilot</a> - Driving simulation where Jev chooses steering and speed. Not a real-world driving system.
- <a href="https://github.com/lukaske/jev-doom-agent">PROMPT FPS / Jev Doom</a> - Jev chooses actions in a browser-based Doom engine. Uses Freedoom assets.
- <a href="https://github.com/fhshaik/typesafe-mario">TypeSafe Mario</a> - Jev picks controller inputs from emulator state. Requires a lawful local game setup.
- <a href="https://github.com/wustep/jev-playground">Jev Music Playground</a> - Jev picks musical parameters; code turns them into notes and MIDI. Includes an offline mode.
- <a href="https://github.com/baronunread/leanest">Leanest</a> - Test selector that can use Jev to judge which Playwright or Vitest files are safe enough to skip for a code change.
- <a href="https://github.com/sharziki/semdecide">SemDecide</a> - Unix CLI for Jev predicates, choices, scores, JSONL filtering, and CI-friendly exit codes.

### Independent models

- <a href="https://github.com/nokia-applied-research/AnyJev">AnyJev</a> - Independent typed-decision readouts for open models, with option-order correction and per-question calibration. Not TypeSafe Jev weights.
- <a href="https://huggingface.co/cua-ai/cua-s1-forms">CUA-S1-FORMS (independent specialist)</a> - Cua&#x27;s independent form-filling model and dataset. Not a general desktop agent or official Jev weights.
- <a href="https://github.com/vinnylarouge/jevlike">Jevlike (independent option scorer)</a> - Independent one-pass option scorer with training code and game examples. Not TypeSafe Jev.
- <a href="https://github.com/ekzhang/openjev-sglang">OpenJev SGLang</a> - Independent typed-decision server using open models and SGLang. Not official Jev weights.

### Supporting drivers

- <a href="https://github.com/browser-use/browser-harness">Browser Harness (supporting driver)</a> - The CDP browser connection used by Jev Ultrafast. Model-neutral, not a Jev model.

<a href="https://github.com/Amal-David/awesome-jev/blob/main/docs/REVIEWED.md">All 54 reviewed picks: source notes and licenses</a>

## Computer use and drivers

[Compare the browser and desktop tools](https://github.com/Amal-David/awesome-jev/blob/main/docs/CUA.md). The guide separates Jev integrations from their drivers and from independent local models. Cua Driver and Browser Harness execute actions; neither is a Jev model. A locally installed tool may still send data to a hosted model.

<!-- MEDIA_GALLERY:START -->

## Watch Jev in action

**Original creator media, linked to the implementation.** Click a preview to watch the source. Animated GIFs play inline; original GitHub video attachments appear as players below. X and YouTube open on their own platforms.

### From X: demos and the original roundup

<table>
<tr>
<td width="50%" valign="top">
<a href="https://x.com/gregpr07/status/2100411066966749359"><img src="https://raw.githubusercontent.com/browser-use/jev-ultrafast/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/docs/demo.gif" alt="Browser Use × Jev Ultrafast — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Browser Use × Jev Ultrafast</h4>
<p>Watch a browser choose operations and DOM targets; a separate model writes text.</p>
<p><a href="https://x.com/gregpr07/status/2100411066966749359">▶ Watch on X</a> · <a href="https://github.com/browser-use/jev-ultrafast">Code</a> · <a href="https://github.com/browser-use/jev-ultrafast/blob/main/README.md">Source</a></p>
<p><sub>Browser Use · @gregpr07 — Animated author recording. This narrow flight-search demonstration is not a general reliability benchmark.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://x.com/moritzkremb/status/2100577979021832365"><img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" alt="Talk to a browser — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Talk to a browser</h4>
<p>Partial speech becomes typed intents and observed page targets; Playwright acts.</p>
<p><a href="https://x.com/moritzkremb/status/2100577979021832365">▶ Watch on X</a> · <a href="https://github.com/moritzkremb/jev-voice-browser">Code</a> · <a href="https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md">Source</a></p>
<p><sub>Moritz Kremb · @moritzkremb — Creator post preview when accessible. Keep its browser-control server private; a recording is not a security audit.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://x.com/awlevin/status/2100262612428894676"><img src="https://pbs.twimg.com/amplify_video_thumb/2100262350100246528/img/hRw0xfLBJpNNi3L9.jpg" alt="Jev on the Mac desktop — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Jev on the Mac desktop</h4>
<p>OCR and accessibility observations become choices for desktop actions.</p>
<p><a href="https://x.com/awlevin/status/2100262612428894676">▶ Watch on X</a> · <a href="https://github.com/awlevin/typesafe-computer-use">Code</a> · <a href="https://github.com/awlevin/typesafe-computer-use/blob/main/README.md">Source</a></p>
<p><sub>@awlevin — Creator post preview when accessible. Screen content may be private; real use needs screen-recording and accessibility permissions.</sub></p>
</td>
<td width="50%" valign="top">
<h4>An independent agent supervisor</h4>
<p>Jev assesses worker progress and verification needs; code decides interventions.</p>
<p><a href="https://x.com/JoshARosen/status/2100573432089866717">▶ Watch on X</a> · <a href="https://github.com/thruwire/foreman">Code</a> · <a href="https://github.com/thruwire/foreman/blob/main/README.md">Source</a></p>
<p><sub>Josh Rosen · @JoshARosen — Architectural experiment. Not a replacement for tests, review, or permission checks.</sub></p>
<p><sub>No reliable preview image was returned. The original watch link is retained.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://x.com/jarrodwatts/status/2100356151468585346"><img src="https://pbs.twimg.com/amplify_video_thumb/2100355999064379392/img/BiAbeDjN57avf2VK.jpg" alt="An order-book decision loop — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>An order-book decision loop</h4>
<p>Typed buy/sell judgments inside a bounded quoting and execution loop.</p>
<p><a href="https://x.com/jarrodwatts/status/2100356151468585346">▶ Watch on X</a> · <a href="https://github.com/jarrodwatts/jev-trader">Code</a> · <a href="https://github.com/jarrodwatts/jev-trader/blob/main/README.md">Source</a></p>
<p><sub>Jarrod Watts · @jarrodwatts — The documented default is mock/dry-run. A dashboard does not prove live inference, profitability, or safe custody.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://x.com/moritzkremb/status/2100895894287839255"><img src="https://pbs.twimg.com/media/HSfhrsxbMAEdHxj.png?name=large" alt="The community roundup — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>The community roundup</h4>
<p>The discovery thread that seeded this collection; follow the original creators.</p>
<p><a href="https://x.com/moritzkremb/status/2100895894287839255">▶ Watch on X</a> · <a href="https://x.com/moritzkremb/status/2100895894287839255">Source</a></p>
<p><sub>Moritz Kremb · @moritzkremb — Roundup image, not a separate working project. This directory does not claim to capture every reply.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://x.com/OpenRouter/status/2102125765773144286"><img src="https://pbs.twimg.com/media/HSxAPo7bwAAcSvf.jpg?name=orig" alt="OpenRouter winner: JevAI for XMage — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>OpenRouter winner: JevAI for XMage</h4>
<p>Legal game actions become Jev choices; the hybrid combines XMage search with model judgment.</p>
<p><a href="https://x.com/OpenRouter/status/2102125765773144286">▶ Watch on X</a> · <a href="https://github.com/ShiftSad/mage/tree/master/Mage.Server.Plugins/Mage.Player.JevAI">Code</a> · <a href="https://github.com/ShiftSad/mage/blob/master/Mage.Server.Plugins/Mage.Player.JevAI/README.md">Source</a></p>
<p><sub>ShiftSad · screenshot published by OpenRouter — Publisher screenshot, not a recording or our test. The reported 11-6-3 result belongs to the hybrid; pruning is off by default. Award announced 2026-09-21.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://x.com/OpenRouter/status/2102125782219075865"><img src="https://pbs.twimg.com/media/HSxAQhCbsAESKOn.png?name=orig" alt="OpenRouter winner: Jev Chess — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>OpenRouter winner: Jev Chess</h4>
<p>A shared chess game displays Jev probabilities over legal move candidates.</p>
<p><a href="https://x.com/OpenRouter/status/2102125782219075865">▶ Watch on X</a> · <a href="https://jevchess.com/">Source</a></p>
<p><sub>sliday · screenshot published by OpenRouter — Publisher screenshot; Source opens the project page. No public repository or code license verified. We did not play a move or reproduce the results. Award announced 2026-09-21.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://x.com/OpenRouter/status/2102125798371283444"><img src="https://pbs.twimg.com/media/HSxARhBaIAABItD.jpg?name=orig" alt="OpenRouter winner: tisco — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>OpenRouter winner: tisco</h4>
<p>Search spoken content, review transcript matches, and approve clip organization in a terminal.</p>
<p><a href="https://x.com/OpenRouter/status/2102125798371283444">▶ Watch on X</a> · <a href="https://github.com/cairodavila/tisco">Code</a> · <a href="https://github.com/cairodavila/tisco/blob/main/README.md">Source</a></p>
<p><sub>cairodavila · screenshot published by OpenRouter — Publisher screenshot. Jev judges transcripts, not video pixels. Audio uploads, live model calls, and file changes have separate data and approval implications. Award announced 2026-09-21.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://x.com/OpenRouter/status/2102125815031071157"><img src="https://pbs.twimg.com/media/HSxAScJawAAJ1Lu.jpg?name=orig" alt="OpenRouter winner: Vibe Domain — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>OpenRouter winner: Vibe Domain</h4>
<p>Separate candidate availability checks from ranking names against a requested vibe.</p>
<p><a href="https://x.com/OpenRouter/status/2102125815031071157">▶ Watch on X</a> · <a href="https://obstudio.org/tools/vibe-domain/">Source</a></p>
<p><sub>OB Studio / Oliver · screenshot published by OpenRouter — Publisher screenshot; Source opens the project. The page documents a no-key heuristic mode distinct from live Jev. No public repo verified; recheck availability at a registrar. Award announced 2026-09-21.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://x.com/OpenRouter/status/2102125830185075060"><img src="https://pbs.twimg.com/media/HSxATYraMAADchl.jpg?name=orig" alt="OpenRouter winner: jev_search — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>OpenRouter winner: jev_search</h4>
<p>Keyword-density code prioritizes files; Jev evaluates passages in two passes.</p>
<p><a href="https://x.com/OpenRouter/status/2102125830185075060">▶ Watch on X</a> · <a href="https://github.com/caio0452/jev_search">Code</a> · <a href="https://github.com/caio0452/jev_search/blob/main/README.md">Source</a></p>
<p><sub>caio0452 · screenshot published by OpenRouter — Publisher screenshot. The author labels the project AI-generated and not for production. Selected source text reaches OpenRouter; no project code was executed here. Award announced 2026-09-21.</sub></p>
</td>
</tr>
</table>

### Screenshots, animated demos, and implementation diagrams

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/thelau/jev-tetris"><img src="https://raw.githubusercontent.com/thelau/jev-tetris/9869b602965cf002afff766013f8c068846d36aa/docs/stills/states/3-decided-desktop.png" alt="Jev Tetris: see the decision — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Jev Tetris: see the decision</h4>
<p>Code enumerates reachable placements; Jev chooses and the board visualizes its preferences.</p>
<p><a href="https://github.com/thelau/jev-tetris">Open demo / recording</a> · <a href="https://github.com/thelau/jev-tetris">Code</a> · <a href="https://github.com/thelau/jev-tetris/blob/main/README.md">Source</a></p>
<p><sub>thelau — Author UI still. A mock mode also exists; the screenshot alone does not establish live inference.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/devagrawal09/jev-review"><img src="https://raw.githubusercontent.com/devagrawal09/jev-review/31f89602797fb7bea007f8a480bf368bf564954e/docs/dashboard.png" alt="A structured code-review dashboard — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>A structured code-review dashboard</h4>
<p>Follow staged risk checks, evidence selection, and severity judgments in a local UI.</p>
<p><a href="https://github.com/devagrawal09/jev-review">Open demo / recording</a> · <a href="https://github.com/devagrawal09/jev-review">Code</a> · <a href="https://github.com/devagrawal09/jev-review/blob/main/README.md">Source</a></p>
<p><sub>devagrawal09 — Author dashboard screenshot. Findings are review prompts, not proof of a defect or a security certification.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle"><img src="https://github.com/user-attachments/assets/1058589f-d686-4b3d-8873-5eb800ba35b3" alt="Needle: find by meaning — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Needle: find by meaning</h4>
<p>Score source passages and select the relevant sentence without generating a new answer.</p>
<p><a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle">Open demo / recording</a> · <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle">Code</a> · <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/advanced_llm_apps/needle/README.md">Source</a></p>
<p><sub>Shubhamsaboo / awesome-llm-apps — Author screenshot of the semantic-find interface. Live requests use Vercel AI Gateway and send selected text.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/cocktailpeanut/jevthoven"><img src="https://raw.githubusercontent.com/cocktailpeanut/jevthoven/main/docs/decision-pipeline.jpg" alt="How Jevthoven composes — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>How Jevthoven composes</h4>
<p>A prompt becomes a musical plan, bounded choices, editable notes, and MIDI.</p>
<p><a href="https://github.com/cocktailpeanut/jevthoven">Open demo / recording</a> · <a href="https://github.com/cocktailpeanut/jevthoven">Code</a> · <a href="https://github.com/cocktailpeanut/jevthoven/blob/main/README.md">Source</a></p>
<p><sub>cocktailpeanut — Author architecture illustration, not a screenshot or an audio-model result. The full recording appears below.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://jev-explained-repo.vercel.app/"><img src="https://raw.githubusercontent.com/davila7/jev-explained/5cbe35e04609112be77b1bd447bd79b3bde7980b/docs/jev-primitives.png" alt="Three primitives, made visible — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Three primitives, made visible</h4>
<p>Explore Noul, Choice, and Score through an interactive decision playground.</p>
<p><a href="https://jev-explained-repo.vercel.app/">Open demo / recording</a> · <a href="https://github.com/davila7/jev-explained">Code</a> · <a href="https://github.com/davila7/jev-explained/blob/main/README.md">Source</a></p>
<p><sub>davila7 — Explanatory illustration, not an actual response or timing result. Hosted live examples require a key.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/dabit3/jev-experiments/tree/main/jev-launcher"><img src="https://raw.githubusercontent.com/dabit3/jev-experiments/c469e5bfdc73eb3e1999bba2569e66b579a970fd/jev-launcher/docs/set-ambassador.png" alt="A meaning-based Mac launcher — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>A meaning-based Mac launcher</h4>
<p>Local search proposes files and history items; Jev ranks the intended targets.</p>
<p><a href="https://github.com/dabit3/jev-experiments/tree/main/jev-launcher">Open demo / recording</a> · <a href="https://github.com/dabit3/jev-experiments/tree/main/jev-launcher">Code</a> · <a href="https://github.com/dabit3/jev-experiments/blob/main/jev-launcher/README.md">Source</a></p>
<p><sub>dabit3 — Historical author screenshot from the archived experiment. Its README points to a successor; this is not the current UI.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/mrnugget/jev-shell-history"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/4b2b75d26c0ccf5726263904514a22a8e11659ea/demo/demo.gif" alt="Semantic shell suggestions — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Semantic shell suggestions</h4>
<p>Jev ranks a bounded set of previous commands; the user accepts a suggestion.</p>
<p><a href="https://github.com/mrnugget/jev-shell-history">Open demo / recording</a> · <a href="https://github.com/mrnugget/jev-shell-history">Code</a> · <a href="https://github.com/mrnugget/jev-shell-history/blob/main/README.md">Source</a></p>
<p><sub>mrnugget — Animated author demo uses fabricated history. Do not send sensitive real shell history without reviewing data handling.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/zurfyx/jev-browser-skill/blob/main/docs/demo.mp4"><img src="https://raw.githubusercontent.com/zurfyx/jev-browser-skill/7db9b4cf1cfca82f0742c75054e22cb8089ee908/docs/demo.gif" alt="A browser skill you can read — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>A browser skill you can read</h4>
<p>A recorded Hacker News walkthrough shows observed controls, typed choices, and execution.</p>
<p><a href="https://github.com/zurfyx/jev-browser-skill/blob/main/docs/demo.mp4">Open demo / recording</a> · <a href="https://github.com/zurfyx/jev-browser-skill">Code</a> · <a href="https://github.com/zurfyx/jev-browser-skill/blob/main/README.md">Source</a></p>
<p><sub>zurfyx — Animated author recording, plus an MP4. A deliberately bounded reference implementation, not a complete browser agent.</sub></p>
</td>
</tr>
</table>

### Full recordings — play inline

These are the creators' original GitHub-hosted uploads, not re-encoded copies. A direct watch link is retained for clients that do not render a player.

<p><strong>Abide — checking project rules during an agent session</strong> — the recording could not be verified by the latest public-access check. <a href="https://github.com/coldteadotai/abide/blob/master/README.md">View the creator source</a>.</p>

<h4>Jevthoven — from a prompt to editable music</h4>

<p>Watch typed musical decisions turn into an editable multitrack composition.</p>

https://github.com/user-attachments/assets/176c69e4-501e-4b71-8517-957cc692882a

<a href="https://github.com/user-attachments/assets/176c69e4-501e-4b71-8517-957cc692882a">Open recording</a> · <a href="https://github.com/cocktailpeanut/jevthoven">Repository</a> · <a href="https://github.com/cocktailpeanut/jevthoven/blob/main/README.md">Creator source</a>

<sub>cocktailpeanut — Code renders notes and audio. Fixture/manual modes are distinct from billable live Jev decisions.</sub>

<h4>jev-align — improve a decision with human labels</h4>

<p>Find uncertain examples, label them, and review proposed AI-function improvements.</p>

https://github.com/user-attachments/assets/81650587-e3f1-4655-8213-ed5f6e120e9a

<a href="https://github.com/user-attachments/assets/81650587-e3f1-4655-8213-ed5f6e120e9a">Open recording</a> · <a href="https://github.com/sutro-sh/jev-align">Repository</a> · <a href="https://github.com/sutro-sh/jev-align/blob/main/README.md">Creator source</a>

<sub>Sutro — Experimental active-learning CLI. Training improvement is not held-out quality; inference and reflection models may both bill.</sub>

### Longer walkthroughs on YouTube

<table>
<tr>
<td width="50%" valign="top">
<a href="https://www.youtube.com/watch?v=Nq_lu5QT-fI"><img src="https://i.ytimg.com/vi/Nq_lu5QT-fI/hqdefault.jpg" alt="A full Jev walkthrough — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>A full Jev walkthrough</h4>
<p>A longer introduction and practical demonstrations from Moritz.</p>
<p><a href="https://www.youtube.com/watch?v=Nq_lu5QT-fI">▶ Watch on YouTube</a> · <a href="https://www.youtube.com/watch?v=Nq_lu5QT-fI">Source</a></p>
<p><sub>Moritz | AI Systems — Linked video, not an independently reproduced tutorial. Title and creator metadata are checked through YouTube oEmbed when accessible.</sub></p>
</td>
<td width="50%" valign="top">
<a href="https://www.youtube.com/watch?v=9oWxrsRo4d8"><img src="https://i.ytimg.com/vi/9oWxrsRo4d8/hqdefault.jpg" alt="An email-classification walkthrough — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>An email-classification walkthrough</h4>
<p>A creator walkthrough of applying Jev to email classification.</p>
<p><a href="https://www.youtube.com/watch?v=9oWxrsRo4d8">▶ Watch on YouTube</a> · <a href="https://www.youtube.com/watch?v=9oWxrsRo4d8">Source</a></p>
<p><sub>vogel — Linked video, not an independently reproduced tutorial. Title and creator metadata are checked through YouTube oEmbed when accessible.</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://www.youtube.com/watch?v=zZNm4zP_lEE"><img src="https://i.ytimg.com/vi/zZNm4zP_lEE/hqdefault.jpg" alt="Practical ways to use Jev — creator preview; click to watch or inspect" width="480" loading="lazy"></a>
<h4>Practical ways to use Jev</h4>
<p>An overview of possible applications and implementation ideas.</p>
<p><a href="https://www.youtube.com/watch?v=zZNm4zP_lEE">▶ Watch on YouTube</a> · <a href="https://www.youtube.com/watch?v=zZNm4zP_lEE">Source</a></p>
<p><sub>Mark Kashef — Linked video, not an independently reproduced tutorial. Title and creator metadata are checked through YouTube oEmbed when accessible.</sub></p>
</td>
</tr>
</table>

**Source notes:** media remain hosted by their creators/platforms; this repository does not relicense them. Public X mirror metadata is used only to locate a poster, not to certify a demo. Reachable media is not proof of live inference, security, or benchmark performance. No project was executed for this gallery.

[Media sources and link-check receipts](https://github.com/Amal-David/awesome-jev/blob/main/docs/MEDIA.md) · [Suggest a visual demo](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml)

<!-- MEDIA_GALLERY:END -->

## OpenRouter community winners

OpenRouter's [September 21 roundup](https://x.com/OpenRouter/status/2102125748723339774) features JevAI for XMage, Jev Chess, tisco, Vibe Domain, and jev_search. Their screenshots are in the gallery above. [Project links and implementation notes](https://github.com/Amal-David/awesome-jev/blob/main/docs/OPENROUTER_SHOWCASE.md). These are OpenRouter's picks, not a ranking by this list.

<details>
<summary>All curated X links</summary>

## Curated X demos

[Moritz's roundup](https://x.com/moritzkremb/status/2100895894287839255) started this collection. [OpenRouter's thread](https://x.com/OpenRouter/status/2102125748723339774) added five more projects. [Full index and source notes](https://github.com/Amal-David/awesome-jev/blob/main/docs/X_DEMOS.md).

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

</details>

## Find a project

The [full catalog](https://github.com/Amal-David/awesome-jev/blob/main/docs/CATALOG.md) includes community listings and automatic discoveries that have not been selected for this README. Use GitHub's outline or Cmd/Ctrl+F to browse it. For filters, clone the repo and open `docs/catalog.html` locally. [Viewer instructions](https://github.com/Amal-David/awesome-jev/blob/main/docs/BROWSE.md).

For more demos and skills, browse [Ship with Jev](https://www.shipwithjev.com/). We use it for discovery, then check the original projects. [Our selections from it](https://github.com/Amal-David/awesome-jev/blob/main/docs/SHIPWITHJEV_REVIEW.md).

`Reviewed` means the primary source was inspected. `Indexed` means it came from another directory. `Auto-discovered` means a README keyword match. These labels do not imply the project was tested here.

<details>
<summary>Refresh status</summary>

**Last discovery:** 2026-09-26T13:13:52Z (UTC). **Latest repository metadata date:** 2026-09-26. **Unavailable repositories at last check:** 18. <a href="https://github.com/Amal-David/awesome-jev/blob/main/docs/STATUS.md">Coverage, failures and run receipts</a>.

The four-hour job updates the discovery catalog and checks a rotating set of links. It does not choose projects for the README. [Check history and coverage](https://github.com/Amal-David/awesome-jev/blob/main/docs/STATUS.md).

</details>

## Contribute

[Suggest a project](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml) with a source link, what Jev does, and one reason it is useful. Small projects are welcome. A clear implementation or inspectable demo matters more than stars; screenshots and performance claims alone are not enough.

Found a broken link or a misleading description? Open an issue. [Contribution guide](https://github.com/Amal-David/awesome-jev/blob/main/CONTRIBUTING.md) · [Selection and removal policy](https://github.com/Amal-David/awesome-jev/blob/main/docs/CURATION.md).

<details>
<summary><strong>Safety, licensing, and evidence limits</strong></summary>

Some projects use paid APIs, logged-in browser sessions, or desktop permissions. Read their setup and privacy notes before connecting them. Reported benchmarks belong to their authors unless a separate reproduction is linked. Mock modes and independent models are labeled where known.

This is an unofficial list. Each linked project and media file keeps its own license. A missing license is not permission to reuse. [Security policy](https://github.com/Amal-David/awesome-jev/blob/main/SECURITY.md) · [Sources and credits](https://github.com/Amal-David/awesome-jev/blob/main/SOURCES.md).

</details>
