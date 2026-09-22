# Search and filter the directory

[Start here](../README.md) · [Reviewed picks](REVIEWED.md) · [Build with Jev](START_HERE.md) · [Freshness](STATUS.md)

## Browse on GitHub

Open [the full catalog](CATALOG.md), choose a category from GitHub's Markdown outline, then use **Cmd+F** on macOS or **Ctrl+F** elsewhere. Search for a project name, creator, `MCP`, `browser`, `music`, or an evidence label. The reviewed-only page is much shorter.

Evidence labels mean different things: **Reviewed** = primary source inspected; **Indexed** = community listing; **Auto-discovered** = explicit README keyword match. None means security-audited or reproduced.

## Use the local viewer

The generated [catalog.html](catalog.html) embeds its data, styles and filtering code. GitHub shows its source rather than hosting it as a website. **After cloning, open `docs/catalog.html` in your browser.** No installation, web server, sign-in, external libraries, analytics or API key is required.

The viewer defaults to reviewed picks. Search across project names, repository owners, descriptions and notes, then narrow by evidence, category, resource type (repo/demo/skill/code/post/reproduction), or recorded license label. Several query words must all match. Reset returns to the reviewed selection. Results are displayed in pages of 60 to keep large collections responsive.

The fragment in the URL stores the filters locally; it is not sent to a server. For example, after opening the file, select **All evidence levels**, **browser**, and **Repository** to compare browser-related discoveries with the reviewed examples. Each result retains source links, review dates where available, and limitations.

The viewer is a build-time snapshot, not a live API. Its license labels are metadata, not a grant of rights. Use [the status page](STATUS.md) for check coverage and the workflow history for actual refreshes.

## Rebuild the snapshot

```sh
python3 scripts/build.py
python3 scripts/build.py --check
```

Both commands are offline. The first renders both READMEs, the reviewed page, catalog, local viewer, media index, X index and status page together. `--check` writes nothing. Network discovery is a separate explicit `--refresh` operation.
