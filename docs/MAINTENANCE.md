# Issue and pull request reviews

The owner has scheduled a contribution-review pass every four hours. This is separate from the GitHub Actions discovery job: finding a repository does not approve it, and a green build does not automatically merge a PR.

Each pass reads open issues, PR diffs, new comments, previous reviews, and current checks. Useful submissions get source review. Repository fixes get tests. A merge uses the reviewed head SHA and preserves changes already on main. Recheck a blocked submission when its source or PR changes; do not repeat unchanged comments.

Keep the README short and leave the existing X gallery alone unless a correction is needed. Do not run submitted projects, install their dependencies or skills, use real inference keys, or enable privileged fork workflows to perform a review.

## September 23 review

| Item | Outcome |
|---|---|
| [PR #6](https://github.com/Amal-David/awesome-jev/pull/6) | Merged the contributor's two UTF-8 fixture-read fixes after all 130 repository tests passed on the merged tree. |
| [Issue #5](https://github.com/Amal-David/awesome-jev/issues/5) | Closed by PR #6. Follow-up fixes make the remaining repository text reads/writes explicit about UTF-8 and skip publisher integration tests when Bash is unavailable. |
| [Issue #2](https://github.com/Amal-David/awesome-jev/issues/2) | Confirmed that llm-typesafe was already published; replied and closed the submission. |
| [Issue #4](https://github.com/Amal-David/awesome-jev/issues/4) | Selected jevrs after inspecting its client, typed response validation, retry tests, example source, and license files. No Rust build or WASI runtime was run. |
| [PR #3](https://github.com/Amal-David/awesome-jev/pull/3#pullrequestreview-5285530289) | Changes requested: runtime response validation, server-log privacy disclosure, and regeneration against current main. The application actually defaults to a 0.5 confidence floor; the earlier review note is corrected. |
| [PR #1](https://github.com/Amal-David/awesome-jev/pull/1#pullrequestreview-5263902992) | Still open and blocked. The head and earlier review are unchanged; the current linked source still contains the previously reported credential-handling patterns. No duplicate review was posted. |

This table is a dated record, not a substitute for checking the live issue or PR.

## Validation boundaries

The UTF-8 follow-up includes an offline full-build check with a simulated cp1252 default and a regression check for text I/O without an explicit encoding. It does not claim a native Windows execution. Bash publishing tests run when their prerequisites are present; a missing prerequisite is an explicit skip, not a passing execution.

The jevrs listing describes the default TypeSafe HTTPS route. Its custom endpoint builder checks URI syntax, not mandatory HTTPS; applications must use trusted HTTPS endpoints with real credentials and configure transport timeouts and retry budgets. Source review is not a security certification.
