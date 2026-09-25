# Jev Project Directory

Generated supporting directory with source notes, the original demo gallery, and discovery status. [Back to the editorial list](../README.md).

Projects, demos, and tools built with [Jev](https://docs.typesafe.ai/).

Jev answers questions about data: pick an option, return a yes/no probability, or score something on a scale. It does not write text. The examples here show what people are using it for, with links to the code where available.

<!-- DIRECTORY_STATS -->

[Quick start](#20-second-quick-start) · [Projects](#reviewed-picks) · [Demos from X](#watch-jev-in-action) · [CUA & drivers](#computer-use-and-drivers) · [OpenRouter winners](#openrouter-community-winners) · [Contributing](#contribute)

> Check permissions and data handling before running a project. A listing here is not a security audit.

## 20-second quick-start

Install `typesafe-sdk` and set `TYPESAFE_API_KEY` in your environment. This example makes one paid request:

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

No key yet? `python3 examples/route_ticket.py` prints the request without calling the API. [SDK setup](https://github.com/typesafe-ai/typesafe-sdk-python#quickstart).

<a id="choose-your-path"></a>

Start with a [classifier](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#build-your-first-typed-classifier), [an agent](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#use-jev-in-an-agent), or [a local alternative](https://github.com/Amal-David/awesome-jev/blob/main/docs/START_HERE.md#explore-a-local-alternative).

For simple rules, parsing, or arithmetic, use code. A dedicated classifier may be a better fit for a fixed task. Jev is worth trying when the choices change or the input is messy; test it on your own examples rather than relying on a demo's timing.

<!-- FEATURED_DEMO -->

## Reviewed picks

<!-- REVIEWED_PICKS -->

## Computer use and drivers

[Compare the browser and desktop tools](https://github.com/Amal-David/awesome-jev/blob/main/docs/CUA.md). The guide separates Jev integrations from their drivers and from independent local models. Cua Driver and Browser Harness execute actions; neither is a Jev model. A locally installed tool may still send data to a hosted model.

<!-- MEDIA_GALLERY:START -->
<!-- MEDIA_GALLERY:END -->

## OpenRouter community winners

OpenRouter's [September 21 roundup](https://x.com/OpenRouter/status/2102125748723339774) features JevAI for XMage, Jev Chess, tisco, Vibe Domain, and jev_search. Their screenshots are in the gallery above. [Project links and implementation notes](https://github.com/Amal-David/awesome-jev/blob/main/docs/OPENROUTER_SHOWCASE.md). These are OpenRouter's picks, not a ranking by this list.

<details>
<summary>All curated X links</summary>

## Curated X demos

[Moritz's roundup](https://x.com/moritzkremb/status/2100895894287839255) started this collection. [OpenRouter's thread](https://x.com/OpenRouter/status/2102125748723339774) added five more projects. [Full index and source notes](https://github.com/Amal-David/awesome-jev/blob/main/docs/X_DEMOS.md).

<!-- X_DEMOS -->

</details>

## Find a project

The [full catalog](https://github.com/Amal-David/awesome-jev/blob/main/docs/CATALOG.md) includes community listings and automatic discoveries that have not been selected for this README. Use GitHub's outline or Cmd/Ctrl+F to browse it. For filters, clone the repo and open `docs/catalog.html` locally. [Viewer instructions](https://github.com/Amal-David/awesome-jev/blob/main/docs/BROWSE.md).

For more demos and skills, browse [Ship with Jev](https://www.shipwithjev.com/). We use it for discovery, then check the original projects. [Our selections from it](https://github.com/Amal-David/awesome-jev/blob/main/docs/SHIPWITHJEV_REVIEW.md).

`Reviewed` means the primary source was inspected. `Indexed` means it came from another directory. `Auto-discovered` means a README keyword match. These labels do not imply the project was tested here.

<details>
<summary>Refresh status</summary>

<!-- FRESHNESS -->

The four-hour job updates the discovery catalog and checks a rotating set of links. It does not choose projects for the README. [Check history and coverage](https://github.com/Amal-David/awesome-jev/blob/main/docs/STATUS.md).

</details>

## Contribute

[Suggest a project](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml) with a source link, what Jev does, and one reason it is useful. Small projects are welcome. A clear implementation or inspectable demo matters more than stars; screenshots and performance claims alone are not enough.

Found a broken link or a misleading description? Open an issue. [Contribution guide](https://github.com/Amal-David/awesome-jev/blob/main/CONTRIBUTING.md) · [Selection and removal policy](https://github.com/Amal-David/awesome-jev/blob/main/docs/CURATION.md).

<details>
<summary><strong>Safety, licensing, and evidence limits</strong></summary>

Some projects use paid APIs, logged-in browser sessions, or desktop permissions. Read their setup and privacy notes before connecting them. Reported benchmarks belong to their authors unless a separate reproduction is linked. Mock modes and independent models are labeled where known.

This is an unofficial list. Each linked project and media file keeps its own license. A missing license is not permission to reuse. [Security policy](https://github.com/Amal-David/awesome-jev/blob/main/SECURITY.md) · [Sources and credits](https://github.com/Amal-David/awesome-jev/blob/main/SOURCES.md).

</details>
