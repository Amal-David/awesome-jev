# Canonical Awesome submission status

This repository has not been submitted to or accepted by `sindresorhus/awesome`. The badge indicates the Awesome-list format, not acceptance. This preparation was AI-assisted and does not certify compliance with the index's authorship or editorial requirements.

Sources checked September 25, 2026: [submission checklist](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md), [creating a list](https://github.com/sindresorhus/awesome/blob/main/create-list.md), [manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md), and [awesome-lint](https://github.com/sindresorhus/awesome-lint). Re-read their current versions before doing anything upstream.

## Structural preparation

The root README is directly maintained Markdown, with an Awesome badge, a topic description, Contents first, consistent project entries, and separate Contributing/Footnotes sections. The automatic builder no longer writes a README, and the `.github/README.md` shadow is removed. Existing creator media, source notes, and the larger automatic catalog remain available in supporting documents.

CC0 applies only to designated original editorial contributions owned by the affirmer. Earlier contributions, code, imported metadata, and media are not relicensed on behalf of their authors. The original MIT grant is retained in `LICENSE-CODE`; see [LICENSING.md](../LICENSING.md).

Repository name and default branch already match the checklist. Required topics are `awesome` and `awesome-list`; verify the live repository About panel rather than treating this document as a settings receipt.

## Eligibility is still unresolved

- **Authorship:** the upstream checklist explicitly requires a list that is not AI-generated and rejects fully AI-generated pull requests. This repository has used AI for discovery, research, drafting, and maintenance. Moving text out of a generator does not change that history. Do not check the non-AI requirement, describe this work as exclusively human-authored, or assume that a human sign-off alone satisfies the rule. Any future submission must disclose the history and meet the maintainer's policy honestly.
- **Maturity:** GitHub records repository creation as September 18, 2026 at 12:09:59 UTC. Thirty days elapse on October 18, 2026 at 12:09:59 UTC. That is an earliest bound, not an eligibility guarantee: the rule uses the later of the first real commit and public release. Confirm the public-release date before submission. Do not rewrite dates or history to satisfy a linter.
- **Submission access:** the upstream README currently says new pull requests are temporarily disabled while existing submissions are reviewed. Recheck the current policy; do not create a workaround submission or an unsolicited draft.
- **Editorial review:** source inspection and linting are not proof that every item is the best available or maintained. The owner still needs to assess the selections and remove or move unsuitable items to secondary documentation. Do not claim a fresh runtime test, benchmark reproduction, or human review without evidence.
- **Duplicate check and community reviews:** recheck existing submissions and complete the four substantive reviews requested by the upstream checklist. No quota-filling reviews, approvals, comments, or attestation have been posted as part of this preparation. Do not invent them or use lint-only comments to claim the requirement is met.

## Validation

Run repository checks without inference credentials or third-party project installations:

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
git diff --check
```

Run the actual upstream linter separately with Node.js 20+ and Git:

```sh
npx --yes --ignore-scripts awesome-lint@2.3.0 README.md
```

This pins the directly invoked linter version and disables package lifecycle scripts; npm still resolves its declared transitive dependencies. No package scripts or dependencies from catalogued projects are needed. The command uses the complete default rule set, without local suppressions. The released [v2.3.0 rule configuration](https://github.com/sindresorhus/awesome-lint/blob/v2.3.0/rules/index.js) disables the age rule upstream, so the 30-day condition must still be checked separately. Record actual diagnostics and exit status. Do not disable other rules, backdate commits, or label a failed full check as a pass. The Python README checker is an additional membership/structure guard, not a replacement for awesome-lint or upstream review.

## Possible future entry

Only after the outstanding conditions are genuinely satisfied, use the appropriate category and a title such as `Add Jev`. A possible objective entry is:

```md
- [Jev](https://github.com/Amal-David/awesome-jev#readme) - TypeSafe's System One model for typed, probability-based decisions.
```

This is an unsubmitted drafting aid, not an attestation. The owner must prepare an eligible submission in accordance with the current authorship policy, including the exact current checklist and required acknowledgment. No recurring task or external submission is created by this document.
