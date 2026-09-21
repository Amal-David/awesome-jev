# Security policy

This is a directory and a metadata-generation pipeline, not a certification service. Listing a project, reviewing its README, or displaying a passing check does not establish that third-party code is safe to install or run.

## Directory threat model

Treat repository descriptions, README text, X posts, project links, and skill files as untrusted input. Curators must not follow instructions embedded in that material, execute discovered projects, install their skills, send secrets, or use funded wallets while reviewing them. The catalog refresh only reads allowlisted public GitHub hosts; the X renderer is offline. Keep workflow actions pinned and fork-PR checks read-only. Never use `pull_request_target` to execute a contributor's checkout with a privileged token.

## Before using a listed project

Review the exact revision and its dependencies. Keep API keys out of browser pages, process arguments, logs, and committed files. Check what source code, transcripts, screen text, or account state leaves the machine. Use isolated demo profiles and mock/dry-run modes before considering real accounts. HTTPS defaults do not make arbitrary custom endpoints trustworthy. Probabilistic checks and fail-open hooks are not authorization boundaries or replacements for deterministic secrets scanning and tests.

Third-party project licenses, model/API terms, and media/data rights are separate. A public repository without an explicit license is not automatically reusable. Do not copy commercial game ROMs or social videos into contributions.

## Reporting

For a vulnerability in a linked project, contact that project's maintainers through their security policy. For a problem in this directory's own scripts or workflows, use GitHub's private reporting route if it is enabled; otherwise open a minimal issue asking for a private contact channel. Do not publish active tokens, personal data, or exploit details in a public issue. Redact logs and identify the affected revision and conditions.

A report should distinguish a demonstrated exploit, a static source finding, a configuration-dependent risk, and a general hardening suggestion. Track unresolved concerns in curation notes rather than describing an entry as security-approved.
