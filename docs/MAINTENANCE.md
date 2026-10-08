# Issue and pull request reviews

The owner has scheduled a contribution-review pass every four hours. This is separate from the GitHub Actions discovery job: finding a repository does not approve it, and a green build does not automatically merge a PR.

Each pass reads open issues, PR diffs, new comments, previous reviews, and current checks. Useful submissions get source review. Repository fixes get tests. A merge uses the reviewed head SHA and preserves changes already on main. Recheck a blocked submission when its source or PR changes; do not repeat unchanged comments.

Keep the README short. Preserve existing X gallery entries and attribution while adding useful demos after source inspection. Do not run submitted projects, install their dependencies or skills, use real inference keys, or enable privileged fork workflows to perform a review.

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
