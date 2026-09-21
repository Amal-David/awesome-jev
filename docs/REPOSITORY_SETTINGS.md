# Repository About settings

The editorial homepage is generated at `.github/README.md`; GitHub prioritizes that location over the root README. The existing root README remains the continuously generated reviewed-project inventory. [GitHub's README precedence documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).

The following sidebar metadata is prepared, **not automatically applied by committing this file**. Applying it requires a repository-settings write action, which is separate from pushing files.

**Description**

> Curated TypeSafe Jev demos from X, repositories, agent skills, code examples, and integrations. Source-linked, evidence-labeled, and refreshed every four hours.

**Topics**

`awesome`, `awesome-list`, `jev`, `typesafe-ai`, `system-one`, `ai-agents`, `ai-demos`, `browser-automation`, `mcp`, `agent-skills`

**Homepage**

Leave this blank until an actual project website is published; do not invent a GitHub Pages deployment.

From an authenticated maintainer terminal, the description/topics can be applied without replacing unrelated settings:

```sh
gh repo edit Amal-David/awesome-jev \
  --description 'Curated TypeSafe Jev demos from X, repositories, agent skills, code examples, and integrations. Source-linked, evidence-labeled, and refreshed every four hours.' \
  --add-topic awesome --add-topic awesome-list --add-topic jev \
  --add-topic typesafe-ai --add-topic system-one --add-topic ai-agents \
  --add-topic ai-demos --add-topic browser-automation --add-topic mcp \
  --add-topic agent-skills
```

Reference: [GitHub CLI `repo edit`](https://cli.github.com/manual/gh_repo_edit). Do not put credentials in this repository or its workflow files. Do not grant a scheduled discovery job administration permissions merely to set the About text.
