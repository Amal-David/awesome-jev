# Reusable Jev examples

These are original, small examples, not copied application repositories. They implement request and policy shapes checked against the [official SDK types](https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/src/types.ts) and [Python quickstart](https://github.com/typesafe-ai/typesafe-sdk-python/blob/main/README.md), reviewed September 18, 2026. Recheck live documentation before a production integration.

## Offline first

Python 3.10 or newer. No dependency installation, API key, network connection, or model spend is needed:

```sh
python3 examples/question_packs.py
python3 examples/route_ticket.py 'The export button no longer works. Please help.'
python3 -m unittest discover -s tests -v
```

`ticket_questions(text)` builds a shared-state request containing Choice (department), Noul (whether help is requested), and Score (impact rubric). Questions are independent; none can read another answer from the same request.

`bounded_action(state, actions)` builds an allowlisted action Choice with an explicit `ask_human` fallback. Your code must generate only permitted actions. The function does not inspect a real browser or execute anything.

`accept_choice(...)` demonstrates application-side checks for stale answers, unexpected action sets, malformed probabilities, a minimum selected-option probability, and a probability margin. It returns a label or `ask_human`; it never executes a tool. Its default thresholds are examples, not evidence of accuracy or universal safety thresholds. Choice confidence is not the same as the selected option's probability, and neither grants permission to act.

## Optional live SDK call

Only this opt-in mode makes a real request; provider charges may apply. It sends the supplied ticket to TypeSafe. Do not use confidential or personal data without appropriate authorization.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install typesafe-sdk
# Set TYPESAFE_API_KEY in your local shell; do not commit it.
python examples/route_ticket.py --live 'I was billed twice for one invoice.'
```

The live example intentionally asks only the department Choice. API credentials stay in the local process. Live inference was not run during repository initialization; the unit suite and default CLI modes were tested offline. Do not describe passing schema/policy tests as a benchmark of Jev accuracy.

## Where to explore actual applications

The [curated selections](../README.md) and [full catalog](../docs/CATALOG.md) link directly to source, companion demos, and skill files where available. In particular, examine the browser action selection in Jev Ultrafast, the legal-action generator in typesafe-snake, Foreman's separate supervision loop, and the enum-to-music renderer in wustep/jev-playground. Follow each project's own license and setup requirements.
