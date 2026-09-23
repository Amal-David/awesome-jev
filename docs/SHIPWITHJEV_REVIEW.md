# Ship with Jev: selected additions

Source review: September 23, 2026. [Directory](https://www.shipwithjev.com/) · [Reviewed collection](REVIEWED.md) · [Source credits](../SOURCES.md#ship-with-jev).

The site is useful for finding projects that are easy to miss in GitHub search, especially skills and projects shared first on X. Its homepage displayed 551 mixed records when inspected. That is not 551 unique, tested applications. This was a selective source review, not an audit of every listing or a complete overlap count against our discovery catalog.

## Added to the reviewed list

| Project | Why it belongs | Source inspected |
|---|---|---|
| [Oko](https://github.com/bartlomein/oko) | A usable code-search interface for agents: local candidate search, optional Jev ranking, and MCP or CLI output. Its ranking code checks answer types and finite probabilities instead of trusting an arbitrary provider value. | [README](https://github.com/bartlomein/oko/blob/8ab56f869899974d2641b824da2fb1cf04fe0395/README.md), [ranking and transport tests](https://github.com/bartlomein/oko/blob/8ab56f869899974d2641b824da2fb1cf04fe0395/src/ranking.rs), MIT license. [Discovery entry](https://www.shipwithjev.com/builds/oko-code-search). |
| [Tenbin](https://github.com/simota/tenbin) | Adds design-time evaluation and threshold selection, not just another API wrapper. The skill also works without its MCP server for several offline tasks. | [Skill](https://github.com/simota/tenbin/blob/1ba0aa9646a559e6086d1488dedf9bd0a1f1c96e/skills/tenbin/SKILL.md), [SDK gateway](https://github.com/simota/tenbin/blob/1ba0aa9646a559e6086d1488dedf9bd0a1f1c96e/tenbin/src/client.ts), [ranking/batch-budget tests](https://github.com/simota/tenbin/blob/1ba0aa9646a559e6086d1488dedf9bd0a1f1c96e/tenbin/src/rank.test.ts), MIT license. Found in the [skills directory](https://www.shipwithjev.com/type/skill). |
| [MinusPodJev](https://github.com/ttlequals0/MinusPodJev) | A concrete podcast integration: transcript-level decisions, code-owned span assembly, and an adapter for an existing app. It includes tests for malformed responses and poisoned cache entries. | [Request flow](https://github.com/ttlequals0/MinusPodJev/blob/ee24adf3874987b57b2d45db4448f0d110aa2f7d/docs/how-it-works.md), [service](https://github.com/ttlequals0/MinusPodJev/blob/ee24adf3874987b57b2d45db4448f0d110aa2f7d/backend/app/services/jev.py), [hardening tests](https://github.com/ttlequals0/MinusPodJev/blob/ee24adf3874987b57b2d45db4448f0d110aa2f7d/backend/tests/test_review_hardening.py), [security notes](https://github.com/ttlequals0/MinusPodJev/blob/ee24adf3874987b57b2d45db4448f0d110aa2f7d/docs/security-and-storage.md), MIT license. Found on the directory homepage. |

All three are new to this reviewed selection. They may have appeared in the larger automatic discovery index; no claim of complete catalog absence is made.

## Limits worth keeping in the entries

**Oko:** `--no-jev` uses local keyword ranking. Jev ranking sends the query and selected source text to TypeSafe. Its setup can change agent/project configuration. The custom provider URL is caller-controlled; use trusted HTTPS for real credentials. Published retrieval and speed numbers were not reproduced.

**Tenbin:** design and lint can be offline, but model evaluation sends the supplied state to TypeSafe. The host agent generates code; Jev does not. Token estimates and in-flight reservations help bound a session but are not a guaranteed billing cap. Thresholds still need validation on separate labeled data.

**MinusPodJev:** this is a proof-of-concept transcript adapter, not an audio model. It forwards a caller bearer key to TypeSafe. Keep it behind a trusted connection and add deployment request-size/rate controls; concurrency limits alone are not enough. Chapter generation needs a separate chat model. The root MIT license does not replace the terms of every vendored component or evaluation asset.

No upstream code, test suite, skill, installer, model, or live demo was executed for this review. No keys, private source files, audio, or paid inference calls were supplied. The repository's own validation tests check the directory, not the quality of these projects.

## Not promoted in this pass

**jevsearch** has a useful React/shadcn search component and a readable benchmark. Its inspected [server](https://github.com/kylemclaren/jevsearch/blob/main/src/lib/jev-search-server.ts) casts the provider response and uses probability fields without runtime type/range checks. Stronger malformed-response handling and regression coverage would make it easier to recommend. This is a deferral, not a claim of an exploited vulnerability.

**JevQL** has a substantial [documented SQL interface](https://github.com/kylemclaren/jevql/blob/main/README.md), but this pass did not inspect enough of its parser, database execution, or shared-server access control to select it. It is a client-side SQL layer, not a native Postgres extension. Database disclosure and execution permissions deserve their own review.

Other directory entries remain discovery leads. Presence in this directory does not override our existing exclusions or unresolved PR concerns.

## Maintenance

The directory is credited in `SOURCES.md`, the README's browsing section, and the new entries' notes. It is a source for future selective passes, not a bulk-import target. The existing X/media data and gallery renderer are unchanged. Continue using `scripts/build.py` so the README, reviewed page, and catalog agree.
