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
| **Shapeshift** — anishfn / @anishfn | Selects a prebuilt card and intent signals as you type; ordinary code handles dates, amounts, and calculations. | [X demo](https://x.com/anishfn/status/2102327334485557422) · [repo](https://github.com/anishfn/shapeshift) · [source](https://github.com/anishfn/shapeshift/blob/5e24166dcbde6e794f0bd5b1b4bd395aaee5fc19/src/lib/jev/client.ts) |
| **Jev Rubiks Coach** — Max Libin / @maxlibin | Chooses when a cube coach should stay quiet, warn, celebrate, or offer help; deterministic solvers find the moves. | [X demo](https://x.com/maxlibin/status/2102289217569337667) · [repo](https://github.com/maxlibin/jev-rubiks) · [source](https://github.com/maxlibin/jev-rubiks/blob/f888c8392c094907bffd976e99b98303d82c1ed1/src/app/coach.ts) |
| **Readwithjev** — Carl Aiau / @carlaiau | Scores sentence-level emotions while you read; a separate deterministic name-and-alias map navigates characters. | [X demo](https://x.com/carlaiau/status/2102519449517785191) · [repo](https://github.com/carlaiau/read-with-jev) · [source](https://github.com/carlaiau/read-with-jev/blob/e97c84ba6792ceae987f604b7571529110893ab6/src/server/reading-emotions.ts) |
| **jevyoumean** — syumai / @\_\_syumai | Suggests semantically related CLI subcommands from the command's documented choices rather than only matching typos. | [X demo](https://x.com/__syumai/status/2102297752810229800) · [repo](https://github.com/syumai/jevyoumean) · [source](https://github.com/syumai/jevyoumean/blob/f0bed70ebdcc6abda6b5f1984d050cadce3c5897/cmd/jym/main.go) |
| **jevsearch** — Kyle McLaren / @kylemclaren | Streams lexical site-search results first, then uses Jev to judge and rerank a bounded candidate set. | [X demo](https://x.com/kylemclaren/status/2102038326588878950) · [repo](https://github.com/kylemclaren/jevsearch) · [source](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/src/lib/jev-search-server.ts) |
| **JevQL** — Kyle McLaren / @kylemclaren | Adds typed semantic predicates and judgments around ordinary Postgres queries, with batching and cached row decisions. | [X demo](https://x.com/kylemclaren/status/2100953409973108759) · [repo](https://github.com/kylemclaren/jevql) · [source](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/internal/exec/judge.go) |
| **JevPDF** — Kyle McLaren / @kylemclaren | Highlights PDF lines that answer a natural-language query; pdf.js extracts text locally and Jev scores each candidate line. | [X demo](https://x.com/kylemclaren/status/2102703300302791055) · [repo](https://github.com/kylemclaren/jevpdf) · [source](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/src/lib/jev.ts) |
| **softlint** — Błażej Kustra / @blazejkustra\_ | Checks changed diff hunks against plain-English rules, then asks Jev which added line best locates each finding. | [X demo](https://x.com/blazejkustra_/status/2101616583424516392) · [repo](https://github.com/blazejkustra/softlint) · [source](https://github.com/blazejkustra/softlint/blob/b2aeb846eeeb7a88099852ded34df82d2e61dc02/src/jev.ts) |
| **Jev Dreaming** — Adnan Quazi / @\_itzadnan\_ | Filters incoming text for memorable information and judges relationships between memories; Gemini generates the memory text. | [X demo](https://x.com/_itzadnan_/status/2102717202663416049) · [repo](https://github.com/AdnanQuazi/jev-dreaming) · [source](https://github.com/AdnanQuazi/jev-dreaming/blob/f2dab2ebc666e4bc9e48f4103278c4ceda1f7630/lib/jev.ts) |
| **ASIMOV Jev output filter** — Arto Bendiken / @bendiken | Filters fetched or listed JSON records with a plain-language Jev question before optional jq projection. | [X demo](https://x.com/bendiken/status/2102377817459872084) · [repo](https://github.com/asimov-platform/asimov-cli) · [source](https://github.com/asimov-platform/asimov-cli/blob/db1c26c77060bfbfff5e6ca5b972b80e4d6c8973/src/shared.rs) |
| **Cua Driver + jev-use** — Cua / @trycua | Creator's computer-use demonstration, with a maintained recipe where Jev chooses bounded driver actions and local code checks fixture outcomes. | [X demo](https://x.com/trycua/status/2100649543079502213) · [repo](https://github.com/trycua/cua) · [source](https://github.com/trycua/cua/blob/49e924c4632882134b204b2e8a0ce8fae44418df/libs/cua-driver/examples/jev-use/python/jev_adapter.py) |
| **fast-jev-compaction** — Tamara Tran / @tamarajtran | Experimental context pruning: Jev scores tool-call/result pairs, and local code keeps, truncates or drops them while preserving retained text. | [X demo](https://x.com/tamarajtran/status/2100694549362553153) · [repo](https://github.com/tamaratran/fast-jev-compaction) · [source](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/compact.ts) |
| **Jev dev** — donvito / @melvindvivas | Desktop workbench for editing Jev requests, inspecting typed answers and keeping run history, with a separate demo mode. | [X demo](https://x.com/melvindvivas/status/2105347987098755186) · [repo](https://github.com/donvito/jev-dev) · [source](https://github.com/donvito/jev-dev/blob/5df666eb3223688a311e89edfb9278a82b1cc9e3/src-tauri/src/client.rs) |
| **TypeSafe AI for n8n** — n8n / @n8n\_io | Evaluates each n8n item with typed Jev questions or routes it using Choice confidence, Noul uncertainty bands, and Score outputs. | [X demo](https://x.com/n8n_io/status/2105609243827077164) · [repo](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai) · [source](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/blob/c12537bbd9ed7159b7bbe23678ca128c7b2fb52b/README.md) |

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

### Shapeshift

**Pattern:** Debounced typed classification plus a state machine changes the interface without generating UI code.

**Source review:** 2026-09-29. [Primary project source](https://github.com/anishfn/shapeshift/blob/5e24166dcbde6e794f0bd5b1b4bd395aaee5fc19/src/lib/jev/client.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and status URL were found in the public shipwithjev index. Direct X retrieval was unavailable; the recording was not independently watched. The linked implementation was inspected instead.

**Limitations:** Optional hosted Jev, not a general UI generator. The default keyword classifier and scripted demo mode can run without Jev. Online mode sends typed text to TypeSafe; the route logs a 40-character normalized prefix, and saved cards use browser localStorage. Use nonsensitive demo text. Source reviewed, not executed.

### Jev Rubiks Coach

**Pattern:** Compute exact game facts locally, ask bounded coaching questions, then apply thresholds and prewritten messages.

**Source review:** 2026-09-29. [Primary project source](https://github.com/maxlibin/jev-rubiks/blob/f888c8392c094907bffd976e99b98303d82c1ed1/src/app/coach.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and status URL were found in the public shipwithjev index. Direct X retrieval was unavailable; the recording was not independently watched. The linked implementation was inspected instead.

**Limitations:** Jev does not solve the cube or generate the coaching prose. Move/progress facts reach TypeSafe through a key-bearing local dev proxy; do not expose that proxy as an unrestricted public service. Solver timings and coaching quality were not reproduced. The preview is a repository screenshot, not an extracted X video frame.

### Readwithjev

**Pattern:** Viewport-driven classification adds an inspectable annotation layer to a long document.

**Source review:** 2026-09-29. [Primary project source](https://github.com/carlaiau/read-with-jev/blob/e97c84ba6792ceae987f604b7571529110893ab6/src/server/reading-emotions.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and status URL were found in the public shipwithjev index. Direct X retrieval was unavailable; the recording was not independently watched. The linked implementation was inspected instead.

**Limitations:** Research reading interface, not validated emotion measurement or proof of a character's presence. Target sentences and surrounding context reach TypeSafe; requests/responses and scores can persist in local/shared caches. No book text or assets are copied here, and this sweep makes no code-license claim. Source reviewed, not executed.

### jevyoumean

**Pattern:** Use help-derived candidates, typed Choice answers, and local policy to suggest a bounded command correction.

**Source review:** 2026-09-29. [Primary project source](https://github.com/syumai/jevyoumean/blob/f0bed70ebdcc6abda6b5f1984d050cadce3c5897/cmd/jym/main.go).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and status URL were found in the public shipwithjev index. Direct X retrieval was unavailable; the recording was not independently watched. The linked implementation was inspected instead.

**Limitations:** Command/context and help-derived choices reach the configured endpoint; optional context arguments may be sensitive. Hint, prompt, and auto-run modes differ: auto mode can execute a correction. Keep real keys/context on trusted HTTPS endpoints and do not assume the denylist is a security boundary. Client and decision-test source inspected, not run.

### jevsearch

**Pattern:** Stream local retrieval first, then add hosted relevance judgments without a vector database.

**Source review:** 2026-09-29. [Primary project source](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/src/lib/jev-search-server.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and status URL were found in the public shipwithjev index. Direct X retrieval was unavailable; the recording was not independently watched. The linked implementation was inspected instead.

**Limitations:** Jev cannot recover a document absent from the candidate pool. Queries, titles, descriptions, and excerpts reach TypeSafe; custom API URLs need trusted HTTPS. The streaming path retains its first-pass results when judging fails. Published accuracy, latency, and cost figures were not reproduced and are omitted here.

### JevQL

**Pattern:** Let SQL narrow the rows, use Jev for the semantic judgment, and keep query execution and thresholds in code.

**Source review:** 2026-09-29. [Primary project source](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/internal/exec/judge.go).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and status URL were found in the public shipwithjev index. Direct X retrieval was unavailable; the recording was not independently watched. The linked implementation was inspected instead.

**Limitations:** Selected row values leave the database for TypeSafe; the relation-alias form can include every column. Limit columns and use a read-only database role for exploration. Plain SQL passes through, so this is not a read-only sandbox. Paid inference, database access, and project tests were not run.

### JevPDF

**Pattern:** Extract text and page geometry locally, batch independent relevance questions, then stream probability-ranked highlights.

**Source review:** 2026-10-08. [Primary project source](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/src/lib/jev.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution, original post URL and date were inspected in the public X embed/index on shipwithjev.com. Direct X and public-mirror retrieval were unavailable. The linked primary implementation was inspected; no recording or live execution was independently reproduced..

**Limitations:** Original X post: 2026-09-23. Exact text search stays local; meaning search sends extracted page text and the query through the app server to TypeSafe. Optional user API keys also pass through that server. Text extraction is not OCR, and relevance scores do not establish factual correctness. Extraction/search/proxy source inspected; no PDF, key, paid call or benchmark used.

### softlint

**Pattern:** Code scopes rules and builds bounded batches; Noul judges violations, Choice selects a line, and local thresholds produce annotations.

**Source review:** 2026-10-08. [Primary project source](https://github.com/blazejkustra/softlint/blob/b2aeb846eeeb7a88099852ded34df82d2e61dc02/src/jev.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution, original post URL and date were inspected in the public X embed/index on shipwithjev.com. Direct X and public-mirror retrieval were unavailable. The linked primary implementation was inspected; no recording or live execution was independently reproduced..

**Limitations:** Original X post: 2026-09-20. Sends selected source diffs and rules to TypeSafe. Hunks are truncated to a fixed budget, so findings are limited to supplied context; this supplements code review and ordinary linting. The fake-shop example and injected-client test source were inspected. Advertised detection/cost results were not reproduced.

### Jev Dreaming

**Pattern:** Batch triage before generation, retrieve related memories locally, then classify append, extend, supersede or unrelated relationships.

**Source review:** 2026-10-08. [Primary project source](https://github.com/AdnanQuazi/jev-dreaming/blob/f2dab2ebc666e4bc9e48f4103278c4ceda1f7630/lib/jev.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution, original post URL and date were inspected in the public X embed/index on shipwithjev.com. Direct X and public-mirror retrieval were unavailable. The linked primary implementation was inspected; no recording or live execution was independently reproduced..

**Limitations:** Original X post: 2026-09-23. Experimental memory-graph comparison with a Gemini-only pipeline, not validated memory accuracy. Text and candidate memories reach hosted providers; applying a run can update browser IndexedDB. The Jev route uses a server-held key without application authentication, so keep self-hosted exploration local. No public code license was verified; no project code or benchmarks were run.

### ASIMOV Jev output filter

**Pattern:** Bound the record batch, validate all Noul answers, preserve matching original records and their order, then apply deterministic formatting.

**Source review:** 2026-10-08. [Primary project source](https://github.com/asimov-platform/asimov-cli/blob/db1c26c77060bfbfff5e6ca5b972b80e4d6c8973/src/shared.rs).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution, original post URL and date were inspected in the public X embed/index on shipwithjev.com. Direct X and public-mirror retrieval were unavailable. The linked primary implementation was inspected; no recording or live execution was independently reproduced..

**Limitations:** Original X post: 2026-09-22; current source reviewed through 2026-10-07. --jev is optional and uses TYPESAFE\_API\_TOKEN. Original records reach TypeSafe before jq projection, so selecting fewer output fields does not reduce data sent upstream. Current filtering keeps scores strictly above 0.80, validates responses and surfaces failures. Implementation and regression-test source inspected; no modules, accounts or live calls used.

### Cua Driver + jev-use

**Pattern:** Observe the page, offer named executable candidates plus reobserve/abstain, validate the returned ID, execute locally, and verify the result independently.

**Source review:** 2026-10-08. [Primary project source](https://github.com/trycua/cua/blob/49e924c4632882134b204b2e8a0ce8fae44418df/libs/cua-driver/examples/jev-use/python/jev_adapter.py).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. The creator thread, attribution, date and linked Cua repository were inspected through its public Zamantika mirror. Direct X retrieval was unavailable, and the video was not independently watched. The maintained jev-use adapter, runner and test source were inspected separately..

**Limitations:** Original X thread: 2026-09-17. The thread includes an author-measured 2048 run; the current companion recipe reviewed here uses a browser form fixture, not a reproduction of that recording. Live choices send compact page/region metadata to hosted TypeSafe; screenshot bytes are not sent by the inspected adapter. The default mock path still operates a browser. Adapter, fixture runner and fake-client test source inspected; no desktop/browser automation, live calls or benchmark run.

### fast-jev-compaction

**Pattern:** Use typed relevance judgments to select retained history, then apply deterministic pruning with recent-message preservation and a summary fallback.

**Source review:** 2026-10-08. [Primary project source](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/compact.ts).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. The creator's original text and source-link reply were inspected through a public Zamantika mirror. Direct X retrieval was unavailable and the recording was not independently watched. The linked primary implementation was inspected; its repository animation is documented as scripted..

**Limitations:** September 2026 creator post; the inspected mirror displays Sep 18, while the post ID encodes Sep 17 UTC. Conversation text and tool inputs reach TypeSafe, but tool-result bodies are omitted from the model's decision state. Pruning can discard useful evidence; the hook falls back to a normal summary on errors or insufficient reduction. The repository's animated demo is explicitly scripted; it is separate from the real API-backed library. Client, compaction, hook and fake-client test source inspected; no integration, quality/cost evaluation or paid inference run.

### Jev dev

**Pattern:** Keep saved questions and run evidence local while sending explicit live evaluations to the hosted decision model.

**Source review:** 2026-10-08. [Primary project source](https://github.com/donvito/jev-dev/blob/5df666eb3223688a311e89edfb9278a82b1cc9e3/src-tauri/src/client.rs).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Creator attribution and the canonical post URL were inspected in the public Jev Wiki tools index. Direct X and public-mirror retrieval returned HTTP 403, so the recording was not watched. The linked primary implementation, example and test source were inspected independently..

**Limitations:** Current source reviewed through 2026-10-05. Browser preview is demo-only; live desktop requests send request state and questions to TypeSafe. Local history retains request, response and error text. No code license was found in the reviewed source tree. Implementation, request example and test source inspected; no app, installer, project tests or inference run.

### TypeSafe AI for n8n

**Pattern:** Workflow item → bounded typed questions → deterministic n8n output routing or annotated result.

**Source review:** 2026-10-09. [Primary project source](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/blob/c12537bbd9ed7159b7bbe23678ca128c7b2fb52b/README.md).

**Post access:** X URL is an indexed social reference; the original post was not fully retrievable in this review. Original publisher post text, creator attribution, date and status URL were inspected through a public X index. Direct X retrieval returned 403. The official repository and n8n community announcement were inspected instead; no playback or live execution was reproduced.

**Limitations:** Original X post: 2026-10-01; newly indexed here on 2026-10-09, not presented as a new launch. Each input item can cause one hosted request containing selected or full workflow data. The temporary cloud-credit promotion is omitted from the durable listing. Source and mocked tests were inspected; no workflow or inference was run.

## Curation rules

Edit `data/x_demos.json`, not the generated tables. Use exactly one `repo` or public project `url`, plus direct evidence from that repository or project. Keep canonical X status URLs and original creator attribution. Record mirror access in `post_access`; a readable publisher post is not live-demo verification. Missing code stays missing. Do not infer that unrelated entries belong to the same thread, copy unlicensed media, or present reported timings as reproduced.

Run `python3 scripts/build.py` and `python3 scripts/build.py --check`. The four-hour workflow preserves and validates this section; it does not authenticate to X or autonomously scrape every reply. New editorial selections require source review.
