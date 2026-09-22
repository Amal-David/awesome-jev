# OpenRouter community winners

[README collection](../README.md#openrouter-community-winners) · [X demo index](X_DEMOS.md) · [Media and access receipts](MEDIA.md) · [Reviewed projects](REVIEWED.md)

## Source and scope

OpenRouter announced five winning community projects on **21 September 2026**. The [original X thread](https://x.com/OpenRouter/status/2102125748723339774) is the discovery source; the publisher also shared the narrative in its [official LinkedIn post](https://www.linkedin.com/posts/openrouter_last-week-jev-typesafe-ais-system-one-activity-7507891467219050497-CySu).

The five winner posts were read through the public X mirror, and the publisher narrative was cross-checked against OpenRouter's public LinkedIn page. Repository documentation or public project pages were inspected separately on **22 September 2026**. This covers posts 2–6, not every competition submission. “Winner” is **OpenRouter's designation**, not a ranking produced by this directory.

The [judging post](https://x.com/OpenRouter/status/2102125842470232373) describes using Jev Score judgments and a Choice over entries. Those are the publisher's evaluation procedure, not independent validation, a security audit, or proof that one implementation is generally superior. Scores and performance claims are not reproduced here as our own results.

## Five projects, five implementation patterns

| Project | What Jev decides | Primary source | Original winner post |
|---|---|---|---|
| **JevAI for XMage** — ShiftSad | Select legal game actions or choose among lines already explored by XMage search. | [Plugin README](https://github.com/ShiftSad/mage/blob/master/Mage.Server.Plugins/Mage.Player.JevAI/README.md) · [code directory](https://github.com/ShiftSad/mage/tree/master/Mage.Server.Plugins/Mage.Player.JevAI/src) | [OpenRouter post](https://x.com/OpenRouter/status/2102125765773144286) |
| **Jev Chess** — sliday | Choose among legal chess moves and display the decision distribution in a shared game. | [Public project page](https://jevchess.com/) — no public repository verified | [OpenRouter post](https://x.com/OpenRouter/status/2102125782219075865) |
| **tisco** — cairodavila | Judge transcript relevance before the user approves clip organization. | [README](https://github.com/cairodavila/tisco/blob/main/README.md) · [MIT license](https://github.com/cairodavila/tisco/blob/main/LICENSE) | [OpenRouter post](https://x.com/OpenRouter/status/2102125798371283444) |
| **Vibe Domain** — OB Studio / Oliver | Rank domain candidates against a requested vibe, separately from availability checks. | [Public project page](https://obstudio.org/tools/vibe-domain/) — no public repository verified | [OpenRouter post](https://x.com/OpenRouter/status/2102125815031071157) |
| **jev_search** — caio0452 | Evaluate text chunks in two passes, after code prioritizes the files. | [README](https://github.com/caio0452/jev_search/blob/main/README.md) · [entry point](https://github.com/caio0452/jev_search/blob/main/jev_search.py) | [OpenRouter post](https://x.com/OpenRouter/status/2102125830185075060) |

## Details that matter before reuse

**JevAI has two distinct players.** The pure player delegates bounded decisions to Jev; the hybrid inherits XMage search. Its README associates the advertised 11–6–3 record with **20 hybrid games**, and draws include a turn cap. It also says pre-search pruning measured worse and is off by default. Do not attribute the record to the pure player or treat it as general playing strength. No games were run here. [Source](https://github.com/ShiftSad/mage/blob/master/Mage.Server.Plugins/Mage.Player.JevAI/README.md#measured-strength).

**Jev Chess is a hosted demonstration, not a verified code release.** Its public metadata describes a shared internet-versus-model game and a legal move set. We inspected that page without submitting a move. No backend implementation or code license was verified. [Source](https://jevchess.com/).

**tisco searches words, not pictures.** A separate transcription model handles speech; Jev judges transcript context. The app previews exact moves/renames and documents separate approval for uploads and file changes. Its offline demonstration uses synthetic clips. Live audio and transcript requests can disclose content and incur charges. [Source](https://github.com/cairodavila/tisco/blob/main/README.md#privacy).

**Vibe Domain has a heuristic mode.** Its page distinguishes no-key, in-browser heuristic evaluation from the live OpenRouter route. A displayed score does not by itself demonstrate Jev inference. We did not run domain scans or submit keys. Availability must be checked again at a registrar; the page's guarantees are not adopted as verified facts. [Source](https://obstudio.org/tools/vibe-domain/).

**jev_search prioritizes with code.** The announcement's shorthand suggests model-led file selection, but the current README explains keyword-density file/chunk ordering followed by Jev passage judgments. The author also labels the project fully AI-generated and unsuitable for production. Review outbound source-text handling, output paths, and concurrent request costs; favor environment variables over command-line secrets. [Source](https://github.com/caio0452/jev_search/blob/main/README.md#overview).

## Screenshots and maintenance

All five preview images are **screenshots published by OpenRouter**, linked to the corresponding winner post. They remain on the original platform and are not copied or relicensed here. A screenshot is not a video or a successful live test. The [README gallery](../README.md#watch-jev-in-action) and [media receipts](MEDIA.md) distinguish presentation from URL-access checks.

The maintained sources are `data/curated.json`, `data/x_demos.json`, and `data/media.json`; regenerate all views with `python3 scripts/build.py`. The X schema now permits a verified repository **or** a public project URL so missing source code stays explicitly missing. `post_access` records mirror-based inspection rather than implying an authenticated X session. The original direct-TypeSafe quick-start is unchanged; follow each project's source and the [OpenRouter model page](https://openrouter.ai/~typesafe/jev-latest) for its provider setup. No inference, installation, domain purchase, or shared-game action was performed during this curation.
