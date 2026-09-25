# Choose your first Jev task

[Start here](../README.md) · [Reviewed picks](REVIEWED.md) · [Search and filters](BROWSE.md) · [Watch demos](https://github.com/Amal-David/awesome-jev/blob/main/docs/DIRECTORY.md#watch-jev-in-action)

## Build your first typed classifier

**Goal:** route a small JSON support ticket to one of three known teams.

Start with the [official Python SDK quick-start](https://github.com/typesafe-ai/typesafe-sdk-python#quickstart). Install `typesafe-sdk` in your project's environment, set `TYPESAFE_API_KEY` privately, and copy the short example in the [README](../README.md#20-second-quick-start). One `Choice` defines the allowed answers; `response.choices["team"].choice` returns the selected key. Live requests may incur charges. No API request was made to produce this directory's example.

For a free, offline first step after cloning this repository:

```sh
python3 examples/route_ticket.py
python3 -m unittest discover -s tests -v
```

The offline example prints a request for inspection; it is not model inference. Next, inspect [question_packs.py](../examples/question_packs.py) for Choice/Noul/Score request shapes and a bounded-action example. Read [the example notes](../examples/README.md) before opting into live calls.

**Next milestone:** test the classifier against tickets with known labels, including ambiguous and out-of-scope tickets. A model score is not a substitute for measuring errors on your own inputs.

## Use Jev in an agent

**Goal:** let Jev choose from actions your code already knows how to execute.

Read the [Browser Use implementation](https://github.com/browser-use/jev-ultrafast) or [the smaller browser skill](https://github.com/zurfyx/jev-browser-skill) alongside the [official TypeSafe skill](https://github.com/typesafe-ai/skills). Observe state, build eligible actions, ask bounded questions, validate the selected identifier and state freshness, then execute only an authorized action. Keep a deterministic fallback or human confirmation path.

For supervision rather than direct action selection, inspect [Foreman](https://github.com/thruwire/foreman). Its documented role is judging worker progress and verification needs; it does not replace your tests or security boundaries.

**Next milestone:** run your own offline fixtures first. Do not install hooks or connect a sensitive logged-in browser merely to try a directory entry. Source review and a demo recording are not permission to read private data or perform consequential actions.

## Explore a local alternative

**Goal:** inspect an independent implementation of a similar typed-decision interface.

Start with the reviewed [OpenJev SGLang project](https://github.com/ekzhang/openjev-sglang), and read its current model, hardware, authentication, and deployment requirements before installing it. The [research section](REVIEWED.md#research-and-independent-reproductions) distinguishes reproductions from official TypeSafe resources.

These are **not official Jev weights**, and interface compatibility does not establish equivalent accuracy, calibration, latency, or licensing. A “local” inference server can still have model-download, GPU, network, and authentication requirements. Do not expose it publicly by default.

**Next milestone:** compare one small labeled task using the same inputs and decision criteria, and record quality and cost separately. No GPU, model download, paid inference, or deployment is needed to browse this directory.
