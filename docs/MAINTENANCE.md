# Issue and pull request reviews

The owner has scheduled a contribution-review pass every four hours. This is separate from the GitHub Actions discovery job: finding a repository does not approve it, and a green build does not automatically merge a PR.

Each pass reads open issues, PR diffs, new comments, previous reviews, and current checks. Useful submissions get source review. Repository fixes get tests. A merge uses the reviewed head SHA and preserves changes already on main. Recheck a blocked submission when its source or PR changes; do not repeat unchanged comments.

Keep the README short. Preserve existing X gallery entries and attribution while adding useful demos after source inspection. Do not run submitted projects, install their dependencies or skills, use real inference keys, or enable privileged fork workflows to perform a review.

## October 9: official n8n integration review

The live issue and pull-request queues remain empty. A fresh X search surfaced n8n's October 1 [TypeSafe AI for n8n post](https://x.com/n8n_io/status/2105609243827077164), which was not in the existing social index. It is newly indexed on October 9, not described as a new launch. Direct X retrieval returned 403; the publisher text, creator, date and canonical status URL were recovered through a public X index, then checked against the [official repository at `c12537bb`](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/tree/c12537bbd9ed7159b7bbe23678ca128c7b2fb52b) and [n8n's community announcement](https://community.n8n.io/t/typesafes-jev-is-now-in-n8n-free-on-cloud-via-gateway-credits-until-october-10/317957). The durable entry omits the temporary cloud-credit promotion.

The TypeSafe-maintained community node can annotate each input item or route it through Choice confidence, Noul uncertainty bands and Score outputs. It can send selected text, JSON or the entire item plus questions to the configured endpoint, with one hosted request per input item. Source inspection covered validation, error/fallback routing, credential handling, the support-ticket example, mocked tests, pinned CI/publish workflows and the MIT license. The bearer token is blocked from crossing origins on redirects; custom endpoints still need to be trusted HTTPS destinations. The exact reviewed head's [CI run 36393420371](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/actions/runs/36393420371) succeeded. No package, dependency, n8n instance, credential, project test or hosted call was used.

This review adds one visible integration, one reviewed record and one link-only X gallery entry without copying social media. The previously held iKev and jev-max heads remain unchanged, so their existing holds were not repeated. The separate discovery workflow's latest completed run, [37864640008](https://github.com/Amal-David/awesome-jev/actions/runs/37864640008), is green.

## October 9: SDK, perception and benchmark review

The live issue and pull-request queues remained empty. Delayed discovery run [37846390036](https://github.com/Amal-David/awesome-jev/actions/runs/37846390036) completed successfully and exposed four concrete projects that were selected after exact-revision source review: [TypeSafe Go SDK `c18752f4`](https://github.com/kisshan13/typesafe-ai-go/tree/c18752f466fff7dd8eaebc3810e49121bfa40e1a), [gut `d3db14e2`](https://github.com/Kungie/gut/tree/d3db14e242312393e4f2f9f90422131357084468), [jev-eyes `9ae9a6dc`](https://github.com/LeddoEngano/jev-eyes/tree/9ae9a6dc2088359a52d7092891bbf7c8f2030936), and [Jev benchmark `a254d371`](https://github.com/Kumzha/jev-benchmark/tree/a254d3716e7b87f4ad6c017da910378b960857e4).

The Go project is an explicitly community-maintained client with request builders, typed response fields, configurable transport and retry tests. gut is a broader decision interface: Jev is a first-class backend, while documented local and OpenAI-compatible backends remain distinct alternatives; its exact head had a successful upstream CI run. jev-eyes performs OCR, layout reconstruction and optional zero-shot labeling locally, then exposes the resulting plain state; only its optional `ask` path sends that state to hosted Jev. Its exact-head CI also passed. The benchmark publishes its harness, scoring-policy tests and per-item raw measurements for two 200-item classification samples, with separate 60-item sequential latency runs. Its September 19 prices, geography and results are author-run observations, not current guarantees or an independent reproduction.

All four licenses, core implementations, examples and available test source were inspected. No candidate dependencies, project tests, OCR or model code, datasets, API keys, paid inference or benchmark lanes were run. The previously held iKev and jev-max revisions have not changed, so their existing license and data-flow holds were not repeated. A fresh X search did not surface a distinct source-backed creator demo, and existing gallery entries remain unchanged.

The canonical Awesome policy was rechecked on October 9. Its 30-day, non-AI, four-substantive-review and full-lint requirements remain, submissions are still advertised as temporarily disabled, and no open or closed Jev submission was found. The live awesome-jev repository now has both required topics, resolving the earlier missing `awesome-list` topic; the remaining blockers still prevent submission.

## October 8: Cloudflare Clef model review

Cloudflare's October 1 release of [Clef](https://huggingface.co/Cloudflare/clef/tree/ed3eed331870db2eff4b0db01237128ede8a00ce) and [Clef-flash](https://huggingface.co/Cloudflare/clef-flash/tree/fde727a287004204b7518dcc983fe64379776712) is added as one independent-model family. Both public, ungated repositories identify Apache-2.0 terms and ship model cards, safetensor weights, tokenizer/processor assets, a joint schema head and the same Jev/SystemOne adapter source. Clef is based on Qwen3.8-27B; Clef-flash is based on Qwen3.5-9B. They are Cloudflare-trained models, not TypeSafe Jev weights, and compatible request and response shapes do not establish identical calibration or quality.

The inspected adapter accepts noul, choice and score questions, returns per-option probabilities, and truncates long state input to its configured token budget. Local use keeps inference under the operator's control but requires downloading large model artifacts and executing publisher code. The optional [Workers AI route](https://developers.cloudflare.com/workers-ai/models/clef/) instead sends state, questions and optional media to Cloudflare; Cloudflare's [data-usage documentation](https://developers.cloudflare.com/workers-ai/platform/data-usage/) says customer content is not used to train models or improve services without explicit consent and may be stored when a storage service is used.

Source inspection covered the two exact model-card revisions, the identical adapter files, license texts and hosted API/data documentation. No model weights, custom code or dependencies were downloaded; no local or hosted inference ran; and Cloudflare's benchmark, latency and compatibility results were not reproduced. A fresh X search did not yield a distinct creator demo suitable for the gallery, so existing gallery and media records remain unchanged.

## October 8: discovery review after the backlog

The live issue and pull-request queues remained empty, and scheduled discovery run [37802969559](https://github.com/Amal-David/awesome-jev/actions/runs/37802969559) completed successfully. Its refresh exposed several same-day repositories for editorial review. Three distinct, source-backed projects were selected at their exact heads: [pi-jev-governor `6e3e1594`](https://github.com/qianyuxiang-369/pi-jev-governor/tree/6e3e1594e2b5468bc40543e5d8e468e3d28dfe69), [pen-find `fb95edaf`](https://github.com/adelghaenian/pen-find/tree/fb95edaf5c01eeeb3e0d460d76d8877524ea37d4), and [Chirp `1bffd5f7`](https://github.com/Noctivoro/tern-chirp/tree/1bffd5f7138f471bdb72e992a895ee2387237df9).

The governor combines hosted Jev judgments with deterministic read-only and hard-deny gates, human confirmation, fail-closed unattended permissions, response validation, and extensive mocked/recorded acceptance evidence. pen-find gives a concrete semantic-search role to Jev while explicitly disclosing that Pen node names, paths, text, and structure leave the machine. Chirp bounds Jev to mood/voice parameters and performs deterministic audio synthesis locally, with a no-key/API-error fallback. None of the three projects, their dependencies, skills, audio commands, design files, agent models, or paid inference endpoints was executed.

Two promising leads were deliberately held from editorial promotion. [iKev](https://github.com/gtokman/iKev/tree/93a0965099cd0e90961cdec6e94430fab1d8cfc4) has a substantial Swift implementation and parity fixtures but no license declaration in the inspected tree. [jev-max](https://github.com/saloni-garg/jev-max/tree/1fea15516af1bca6cf60010a729241776496948a) has useful shadow-DOM and same-origin-frame code, but its current documentation does not clearly enumerate the page text, goals, screenshots, and generated field data sent to multiple hosted providers; its broad action-space claims also exceed the narrow inspected test surface. These are revision-specific holds, not permanent exclusions.

## October 8: backlog review and monitoring recovery

The assistant contribution-review task was found disabled, with its last run on September 28. The earlier maintenance session recorded blocked GitHub write access as the reason for pausing it. The separate discovery job continued: its latest run inspected in this pass, [37736840008](https://github.com/Amal-David/awesome-jev/actions/runs/37736840008), completed successfully on October 8, as did the preceding eleven inspected runs. Discovery success did not mean that contribution review was still active.

The existing assistant task was re-enabled on October 8 at its original four-hour cadence after a GitHub write succeeded. Its instructions now include X demo curation and require keeping read-only inspection active and reporting the exact blocker if future writes fail. No duplicate task was created. A configured schedule is not proof of a later successful run; verify execution separately.

The live backlog at the start of this pass contained five PRs and one issue. These are the source-review decisions; the linked GitHub threads show their final publication and closure state.

| Submission | Reviewed revision | Decision |
| --- | --- | --- |
| [#22: 1 Million Emojis](https://github.com/Amal-David/awesome-jev/pull/22) by cwdx | PR `9725968e5b9d6079d99de18d838c9d21bd97cec8`; [source](https://github.com/cwdx/1-million-emojis/tree/f0e8273ebcedee466c0302f2a8fdb30c7964c29b) | Accept the Choice/Noul canvas example. Pin source links and distinguish reusable package inspection from the hosted site's unverified limits. |
| [#25: jevotron](https://github.com/Amal-David/awesome-jev/pull/25) by Chris Mungall | PR `36930f157a2423e2a76899f4156977524e24187a`; [source](https://github.com/cmungall/jevotron/tree/300a67b332dbb6bb6a18fc39532dffcb18fe8055) | Accept with the missing curated metadata and a more specific description. Field selection limits scoring, not the full parsed entry sent to TypeSafe; disclose the local request/response cache. |
| [#26: WaterSheep](https://github.com/Amal-David/awesome-jev/pull/26) by Samrat Dutta | PR `2549a7d28621262fbbc09684b14fe37dbdc68094`; [source](https://github.com/SamratDuttaOfficial/WaterSheep/tree/3ccf02b3839fd2d72e6fb29750488010c7d76360) | Accept as an independent model. Disclose English scope, truncation and multiple passes for large option sets; calibration and SDK compatibility were not execution-tested here. |
| [#21: TetraJev](https://github.com/Amal-David/awesome-jev/issues/21) by Fei Liu | [Source `2ee296af`](https://github.com/FeiLiuEM/tetrajev/tree/2ee296af7bcf731ecb9a1d3613fad4defaf49a2a) | Accept as independent research recipes using separately obtained local models, not a packaged decision service or new weights. Separate local inference from the optional paid TypeSafe reference runner. |
| [#13: Codex Jev Router](https://github.com/Amal-David/awesome-jev/pull/13) by suenot | PR `644d9415485911269d06f0408563965d85f481f2`; [current source](https://github.com/suenot/codex-jev-router/blob/1d4790bbd70413bca476c65070c26a1ee88888f9/README.md) | Close as superseded. The author now recommends deterministic evidence selection and explicitly retires the submitted Jev routing workflow. Retain its separate historical/indexed catalog status. |
| [#24: jev-bouncer](https://github.com/Amal-David/awesome-jev/pull/24) by gherardo200-glitch | PR `9f0754145edc21508d7dc40784a89cb45b06e395`; [client](https://github.com/gherardo200-glitch/jev-bouncer/blob/4afb20e0783301c64d3f9db48edaae455e164bb6/src/jev-client.ts) | Close pending API compatibility fixes. The request uses an array of questions and string Score criteria, and the parser requires an undocumented `ok: true` success flag. The offline heuristic demo does not verify this adapter. |

The jev-bouncer comparison uses TypeSafe's [quick start](https://docs.typesafe.ai/introduction/quickstart) and [Score contract](https://docs.typesafe.ai/primitives/score). This is an advertised-feature correctness concern, not a demand for production-security certification. Its existing tests mock the client interface; offline HTTP contract fixtures can demonstrate the needed correction without a paid call. The withdrawn CodeRabbit mirror comment is not a blocker.

Accepted source edits are applied on current main with contributor credit and regenerated supporting files, rather than importing stale generated snapshots or asking authors to rebase again. Fork workflows requiring approval are not treated as successful tests or approved to execute submitted code. The repository's reviewed offline build and tests validate the intended integrated result; no discovered project, model, installer or paid inference is executed.

### Newly curated X demos

Seven references were added: JevPDF, softlint, Jev Dreaming, ASIMOV Jev output filtering, Cua Driver + jev-use, fast-jev-compaction, and Jev dev. The X collection grows from 16 to 23 records and the media collection from 31 to 38. The original entries remain. Six projects become new reviewed selections; Cua retains a single canonical project entry. Together with the four accepted submissions, this update has 68 reviewed selections.

These are newly curated September posts, not claimed October launches. Source implementations and available example/test code were inspected at pinned revisions; X playback and performance claims were not independently reproduced. JevPDF and softlint use original author-hosted repository GIFs. The Cua form fixture is separate from the creator's earlier 2048 recording. The fast-compaction repository animation is scripted, while its actual API client is a separate source-backed implementation. Jev dev's browser preview is demo-only.

The [X index](X_DEMOS.md) records creator links and access limits; [reviewed source notes](REVIEWED.md) record setup, data flow and license boundaries. JevPDF is also a visible README highlight. No third-party recording was copied or rehosted.

Two discovery leads were not promoted: [jev-sec-audit](https://github.com/DhanushNehru/jev-sec-audit/blob/b61fe1b7d7b928156dbfe64d75dd9fd4ef800f22/index.js) has no actual Jev call in the inspected entry point, and [semantic-jev](https://github.com/johnnymakhoul/semantic-jev/blob/f25611a4ebe289f0268a43eec73536c42adabe2e/src/jevClient.ts) has hardcoded date/confidence behavior and mock adapter fallbacks that do not support an unqualified production description. These are dated source judgments, not blanket exclusions of future corrected revisions.

### Verified completion

The integrated update is published in [6052f23](https://github.com/Amal-David/awesome-jev/commit/6052f2304fe21f9e6c2a45fd6e4a45688d54b163). All 159 repository tests, `scripts/build.py --check`, and `git diff --check` passed on the intended tree. The [push workflow](https://github.com/Amal-David/awesome-jev/actions/runs/37749546917) also completed successfully. All previous curated projects, catalog records, X references and media entries were preserved; the viewer's executable/markup content outside the embedded catalog JSON is unchanged. The offline update did not advance the discovery receipt.

The three accepted PRs were closed as applied, with co-author credit in the commit and individual completion comments. Issue #21 was closed as completed after its entry was verified on main. PRs #13 and #24 were closed with the reasons above. A fresh read of both open-issue and open-PR collections returned zero items. The two addressed/outdated inline threads on #25 and #26 were resolved. The existing assistant maintenance task was rechecked as enabled.

The separate `awesome-lint@2.3.0` invocation could not start successfully in this environment: an initial network-configuration failure was followed by npm `ECOMPROMISED` / `Lock compromised` errors, including with an isolated fresh cache. No formatting pass is claimed, and this update makes no upstream Awesome-index eligibility claim. This did not affect the completed repository tests or the successful GitHub publication workflow.

## September 30: proportional contribution review

The owner asked for a more developer-friendly approach. Routine list maintenance belongs to us; optional hardening is not automatically a blocking requirement. Review the risk in the project's expected use, keep limitations explicit, and do not treat a directory entry as a security certification. Required checks, source evidence, licensing clarity and material safety concerns still apply.

### Spliit Cloud — PR #3

The [submission](https://github.com/Amal-David/awesome-jev/pull/3) is accepted as an **optional integration** with a trusted-HTTPS usage boundary. The earlier nonnumeric-confidence issue is addressed by the current [response checks](https://github.com/antonio-ivanovski/spliit-cloud/blob/02d2d135c68f2035a350025c48d3fff51cccd36d/apps/api/src/lib/ai/system-one-categorize.ts); [test source](https://github.com/antonio-ivanovski/spliit-cloud/blob/02d2d135c68f2035a350025c48d3fff51cccd36d/apps/api/src/lib/ai/system-one-categorize.test.ts) covers invalid answer types, confidence and probability payloads. This is source inspection, not execution of those tests or a claim of fully calibrated distributions. The [MIT license](https://github.com/antonio-ivanovski/spliit-cloud/blob/02d2d135c68f2035a350025c48d3fff51cccd36d/LICENSE) was inspected.

The [URL guard](https://github.com/antonio-ivanovski/spliit-cloud/blob/02d2d135c68f2035a350025c48d3fff51cccd36d/apps/api/src/lib/ai/system-one-base-url.ts) still accepts hostnames beginning with `127.`, and the request follows redirects. These remain real limitations, not claimed fixes. Their relevance here is an operator-configured optional endpoint, rather than a demonstrated exposure in the default TypeSafe HTTPS route. The listing therefore instructs operators to use trusted HTTPS and removes the overly broad transport-security claim. The hostname correction and redirect rejection are non-blocking hardening for this scoped listing, not prerequisites for another author push. This supersedes the earlier request to hold the listing solely for that edge case.

The maintainer handles the current-main integration and regenerated views. Original contributor credit is retained. No project code, account, expense data or paid inference is used for curation; the hosted instance's active engine and performance are not verified.

## September 23 review

| Item | Outcome |
|---|---|
| [PR #6](https://github.com/Amal-David/awesome-jev/pull/6) | Merged the contributor's two UTF-8 fixture-read fixes after all 130 repository tests passed on the merged tree. |
| [Issue #5](https://github.com/Amal-David/awesome-jev/issues/5) | Closed by PR #6. Follow-up fixes make the remaining repository text reads/writes explicit about UTF-8 and skip publisher integration tests when Bash is unavailable. |
| [Issue #2](https://github.com/Amal-David/awesome-jev/issues/2) | Confirmed that llm-typesafe was already published; replied and closed the submission. |
| [Issue #4](https://github.com/Amal-David/awesome-jev/issues/4) | Selected jevrs after inspecting its client, typed response validation, retry tests, example source, and license files. No Rust build or WASI runtime was run. |
| [PR #3](https://github.com/Amal-David/awesome-jev/pull/3#pullrequestreview-5285530289) | Changes requested: runtime response validation, server-log privacy disclosure, and regeneration against current main. The application actually defaults to a 0.5 confidence floor; the earlier review note is corrected. |
| [PR #1](https://github.com/Amal-David/awesome-jev/pull/1#pullrequestreview-5263902992) | Partially accepted on current main: jev-belay and jev-plays-pokemon-red are now reviewed picks from pinned sources. The PR stays open because jev-commit, jev.nvim, and jev-skip still have the unchanged credential/privacy blockers, and its generated files are based on the old layout. Both accepted clients allow a custom `JEV_BASE_URL` without forcing HTTPS; use trusted HTTPS endpoints with real credentials. |

This table is a dated record, not a substitute for checking the live issue or PR.

## Validation boundaries

The UTF-8 follow-up includes an offline full-build check with a simulated cp1252 default and a regression check for text I/O without an explicit encoding. It does not claim a native Windows execution. Bash publishing tests run when their prerequisites are present; a missing prerequisite is an explicit skip, not a passing execution.

The jevrs listing describes the default TypeSafe HTTPS route. Its custom endpoint builder checks URI syntax, not mandatory HTTPS; applications must use trusted HTTPS endpoints with real credentials and configure transport timeouts and retry budgets. Source review is not a security certification.
