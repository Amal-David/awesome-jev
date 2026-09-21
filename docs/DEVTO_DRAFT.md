---
title: "The interesting part of Jev demos is the code around the model"
published: false
description: "Three implementation patterns for typed-decision agents: candidate generation, speculative questions, and validated execution."
tags: ai, programming, architecture, python
---

> AI-assisted draft based on public project documentation inspected on September 21, 2026. The linked demos and their performance claims were not independently reproduced. Before publishing, the human author should verify the explanation, add their own experience, and check DEV's current AI-content guidelines. This is not a promotional or backlink-placement article.

A fast browser demo is easy to appreciate and easy to misunderstand. The model returns a decision, a button gets clicked, and the animation looks like the whole story.

The more useful question is: **what work did the program do before and after that decision?**

Three public Jev projects make that boundary worth studying. They do not establish that typed-decision agents outperform all alternatives. They illustrate different ways to structure a program when a model is useful for a narrow judgment, but should not own arbitrary execution.

## 1. Generate the candidate space in code

[Browser Use's Jev Ultrafast](https://github.com/browser-use/jev-ultrafast/blob/main/README.md#the-action-space) observes a page and produces an indexed table of controls. The model selects an operation and an appropriate target. The program does not ask it to invent JavaScript, CSS selectors, or screen coordinates.

That is an important separation. Candidate generation answers “what exists and is supported?” The model answers a narrower question: “which of these fits the goal?” The executor must still check that the candidate exists when it acts.

This structure gives you at least three distinct failure classes to test. The right control may be missing from the candidate set. The model may pick the wrong valid candidate. Or the page may change after a correct selection. Increasing model quality addresses only part of that problem.

The project's README also distinguishes Jev's decisions from a separate text-generating model used for typing. A hybrid system can use different components for judgment and generation without pretending one model does everything.

## 2. Ask speculative questions without executing every answer

The same browser implementation asks compatible target questions alongside the operation question. The program consumes only the target corresponding to the selected operation. A returned click target does not authorize a click when the operation selected is typing.

[TypeSafe's fan-out documentation](https://docs.typesafe.ai/patterns/fan-out) describes the general pattern: ask independent questions over shared state, then let code choose which results apply. Independent questions do not get to read one another's answers.

This distinction matters when writing prompts. A question such as “is the action you chose safe?” can be underspecified when asked independently of the choice. Supply the candidate action explicitly, evaluate each relevant candidate, or make a subsequent request once the action is known. Do not treat simultaneous answers as a hidden multi-step conversation.

Speculation is a trade-off, not free reasoning. It can remove a sequential network dependency, but unused questions still have a cost. Measure the complete application, including observation, debounce, validation, and browser execution, rather than reporting inference time as total task latency.

## 3. Separate interpretation from permission

[Moritz Kremb's voice browser](https://github.com/moritzkremb/jev-voice-browser/blob/main/README.md#how-a-decision-is-made) turns partial speech into typed questions about intent, targets, whether the command is complete, and whether it requires confirmation. The program can act, wait, ask for clarification, or ignore an utterance.

The interesting part is not just recognizing “click.” It is deciding whether the user has finished specifying what to click. An early partial transcript may be sufficient for a closed-set command such as “go back,” but insufficient for an unfinished search query.

The repository documents a persistent browser profile and warns about exposing its control server or using sensitive logged-in accounts. A probabilistic judgment that an action is non-destructive is not an authorization system. Permission to purchase, send, delete, or disclose information should come from explicit policy and the user, not from the confidence value of a classifier.

A useful design question is: **what is the least consequential action available when this answer is wrong?** Depending on the application, the answer might be highlighting a candidate, asking a question, showing a preview, or doing nothing.

## 4. Treat supervision as another fallible component

[Foreman](https://github.com/thruwire/foreman/blob/main/README.md#what-is-foreman) separates a coding worker from a supervisory loop. It assesses bounded evidence about progress and verification needs while the worker remains active. Deterministic policy interprets those assessments.

The project calls itself an architectural experiment, not a proven replacement for conventional harnesses. That qualification is useful. A supervisor saying “tests are sufficient” is not the same as running tests, checking their exit status, or establishing that they cover the requirement.

For a supervisor, evaluate both false alarms and missed interventions. Also inspect privacy boundaries: bounded diffs and output tails can still contain sensitive information. “We do not send the whole repository” is a reduction in exposure, not the absence of exposure.

## A testing checklist for your own implementation

Start with deterministic tests before using a live model. Supply a candidate ID that does not exist. Supply a valid ID from an older page snapshot. Return malformed probabilities or a missing question. Make the API time out. Change the user's request while a decision is in flight. Include an action that requires permission even when the model is highly confident.

For each case, assert the actual effect, not just the selected label. Was a click emitted? Was text sent? Was a file changed? A safe fallback that is calculated but not enforced is not a fallback.

Then evaluate the model with representative inputs and a clear success criterion. Keep observations, decisions, validation failures, and effects distinguishable in the trace. Report the test boundary honestly: one task in one browser profile does not establish reliability across arbitrary sites.

## The reusable idea

The most interesting part of these demos is not a particular latency number. It is the division of responsibility:

**Code describes the world and the available actions. The model contributes a bounded judgment. Code checks whether that judgment is still applicable and permitted before acting.**

That structure is worth testing even when a different model, a local heuristic, or no model at all turns out to be the better implementation.

Sources: [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast), [voice browser](https://github.com/moritzkremb/jev-voice-browser), [Foreman](https://github.com/thruwire/foreman), and [TypeSafe's fan-out guide](https://docs.typesafe.ai/patterns/fan-out). These are primary project descriptions, not independent validation of their claims.
