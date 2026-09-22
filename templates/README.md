# Awesome Jev

**From an interesting demo to code you can actually understand.**

A curated starting point for TypeSafe Jev: reviewed projects, reusable skills, small code examples, and creator demos from X, GitHub, and YouTube.

<!-- DIRECTORY_STATS -->

<sub><!-- FRESHNESS --></sub>

**Navigate:** [Quick start](#20-second-quick-start) · [Choose a path](#choose-your-path) · [CUA & drivers](#computer-use-and-drivers) · [Reviewed picks](#reviewed-picks) · [OpenRouter winners](#openrouter-community-winners) · [Watch demos](#watch-jev-in-action) · [Search the catalog](#find-a-project) · [Contribute](#contribute)

> Source-reviewed does not mean security-audited. Keep credentials private and inspect permissions before running a project.

## What is Jev?

Jev is TypeSafe AI's model for answering typed questions about text or JSON: choose an option, estimate whether something is true, or score it against a rubric. Use it for bounded decisions such as routing, ranking, or selecting an agent's next action; use a generative LLM when you need new prose, code, or an open-ended plan. Your application still controls permissions, validation, and execution. [Official documentation](https://docs.typesafe.ai) · [Official Python quick-start source](https://github.com/typesafe-ai/typesafe-sdk-python#quickstart).

## 20-second quick-start

**JSON in → one typed decision out.** With `typesafe-sdk` installed and `TYPESAFE_API_KEY` set, this makes one billable API request:

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    result = client.system_one(
        state={"document": "I was charged twice."},
        questions={"team": Choice(
            instructions="Which team should handle this ticket?",
            criteria={"billing": None, "technical": None, "other": None},
        )},
    )
print(result.choices["team"].choice)  # e.g. billing; actual output can differ
```

**No key yet?** Clone this repository and run `python3 examples/route_ticket.py` to inspect an offline request without making an API call. [Setup and next steps](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#build-your-first-typed-classifier) · [More question packs](https://github.com/Amal-David/awesome-jev/blob/main/examples/README.md).

<!-- FEATURED_DEMO -->

## Choose your path

**Build your first typed classifier →** [JSON input, a Choice question, and your first response](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#build-your-first-typed-classifier).

**Use Jev in an agent →** [Select observed actions, validate them, and keep a fallback](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#use-jev-in-an-agent).

**Explore a local alternative →** [Independent implementations, hardware requirements, and important differences](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#explore-a-local-alternative).

## Computer use and drivers

[Computer-use map: integrations, drivers, skills, and local alternatives](https://github.com/Amal-David/awesome-jev/blob/main/docs/CUA.md).

**Native/desktop:** [Cua Driver + jev-use](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use), [Jev Cua](https://github.com/Eronmmer/jev-cua), and [jev-bot](https://github.com/stoopid-computers/jev-bot). **Browser:** compare Jev Ultrafast, the smaller browser skill, Jev Browser, and the existing-connection Codex skill in the map.

Keep the layers separate: **Jev selects; the driver executes; application code verifies.** Browser Harness and Cua Driver are supporting runtimes, not Jev models. CUA-S1-FORMS and Jevlike are independent local-model projects, not official Jev weights. A locally installed agent may still call hosted Jev.

## Reviewed picks

These are the editorial selections. Follow a project immediately, or open the full reviewed page for its concrete Jev role, source evidence, review date, and reuse notes.

<!-- REVIEWED_PICKS -->

## OpenRouter community winners

[OpenRouter's 21 September 2026 showcase](https://x.com/OpenRouter/status/2102125748723339774) named five projects: [JevAI for XMage](https://github.com/ShiftSad/mage/tree/master/Mage.Server.Plugins/Mage.Player.JevAI), [Jev Chess](https://jevchess.com/), [tisco](https://github.com/cairodavila/tisco), [Vibe Domain](https://obstudio.org/tools/vibe-domain/), and [jev_search](https://github.com/caio0452/jev_search).

Explore **game decisions, transcript search, domain ranking, and two-pass code search**. Each winner has its original post and publisher screenshot in the [visual gallery](#watch-jev-in-action), plus [source and implementation notes](https://github.com/Amal-David/awesome-jev/blob/main/docs/OPENROUTER_SHOWCASE.md). Three have linked source repositories; the other two are public project pages, not verified open-source releases. “Winner” is OpenRouter's designation, not our ranking or a security certification.

## Find a project

**On GitHub:** open the [categorized catalog](https://github.com/Amal-David/awesome-jev/blob/main/docs/CATALOG.md), choose a heading from its outline, and use **Cmd/Ctrl+F** for a project, creator, or keyword.

**Prefer filters?** The [local catalog viewer](https://github.com/Amal-David/awesome-jev/blob/main/docs/BROWSE.md) starts with reviewed picks. Search by keyword, then filter by evidence level, category, available code/skill/demo, and license. It runs without dependencies, sign-in, API keys, or a server; the viewer's data is embedded at build time. [Browse instructions](https://github.com/Amal-David/awesome-jev/blob/main/docs/BROWSE.md) · [Machine-readable catalog](https://github.com/Amal-David/awesome-jev/blob/main/data/catalog.json).

## Why this exists

A compelling clip often leaves the useful questions unanswered: **what did Jev decide, where is the implementation, and what can I reuse?** This directory connects the original demo to the code and separates inspected sources from the much larger discovery queue. A high raw entry count is not the goal; a shorter path to something useful is.

## What belongs here?

A concrete Jev integration, demo, skill, SDK, reusable snippet, tutorial, or clearly labeled independent reproduction—with a traceable primary source and a specific explanation of Jev's role. Generic type-safety libraries, unrelated projects named Jev, unsupported performance claims, and duplicate listings do not belong.

Repositories are deduplicated by canonical owner/name; renamed projects should point to their successor. Maintainers can correct an entry, remove it from the reviewed selection, or exclude it from future imports. [Inclusion, deduplication, and removal policy](https://github.com/Amal-David/awesome-jev/blob/main/docs/CURATION.md).

## Contribute

[Suggest a demo or correction](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml) with the original creator, a source link, what Jev decides, and any code, skill, or recording. For a PR, edit the relevant JSON source and run `python3 scripts/build.py`, then `python3 -m unittest discover -s tests -v` and `python3 scripts/build.py --check`. [Contributor guide](https://github.com/Amal-David/awesome-jev/blob/main/CONTRIBUTING.md).

The four-hour workflow performs bounded discovery and rotating checks; it does not continuously inspect every website. [Freshness, unavailable repositories, media errors, and run receipts](https://github.com/Amal-David/awesome-jev/blob/main/docs/STATUS.md) distinguish actual checks from scheduled intentions.

<details>
<summary><strong>Safety, licensing, and evidence limits</strong></summary>

Source review is not a security audit, successful execution test, benchmark replication, or endorsement. Inspect permissions and outbound data before installing hooks, browser extensions, or agent skills. Keep API credentials private; demos can use paid inference, privileged desktop access, or logged-in browser profiles.

Recordings, illustrations, fixtures, and mock modes are labeled where known. A live-looking dashboard is not evidence of real inference or profitable trading. Independent reproductions are not official Jev weights or proof of equivalent quality.

Missing licenses remain `not-checked`, `not-detected`, or `NOASSERTION`, not assumed permission to reuse. Original code and writing follow the repository's [license](https://github.com/Amal-David/awesome-jev/blob/main/LICENSE); imported metadata and linked media retain their original terms. This is an unofficial community directory, not endorsed by TypeSafe AI. [Security policy](https://github.com/Amal-David/awesome-jev/blob/main/SECURITY.md) · [Attribution](https://github.com/Amal-David/awesome-jev/blob/main/SOURCES.md).

</details>

<!-- MEDIA_GALLERY:START -->
<!-- MEDIA_GALLERY:END -->

<details>
<summary><strong>Curated X demos: compact source index</strong></summary>

## Curated X demos

Sources include [Moritz Kremb's roundup](https://x.com/moritzkremb/status/2100895894287839255) and [OpenRouter's five community winners](https://x.com/OpenRouter/status/2102125748723339774). The five OpenRouter winner posts are covered; Moritz's thread is not claimed complete. [Full X index and access notes](https://github.com/Amal-David/awesome-jev/blob/main/docs/X_DEMOS.md).

<!-- X_DEMOS -->

</details>

**Star to bookmark the reviewed collection.** A corrected source link or a well-explained contribution is just as valuable.
