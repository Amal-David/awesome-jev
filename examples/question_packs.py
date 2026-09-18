"""Original offline-first request builders; contract reviewed 2026-09-18.
Source: https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/src/types.ts
No network calls or API credentials are used by this module.
"""
from __future__ import annotations
import json
import math


def ticket_questions(text: str) -> dict:
    if not isinstance(text, str) or not text.strip():
        raise ValueError('Ticket text must not be empty')
    return {
        'model': 'jev-latest', 'state': {'ticket': text},
        'questions': {
            'department': {'type': 'choice', 'instructions': 'Which team should handle the ticket?', 'criteria': {
                'billing': 'Charges, invoices, or refunds', 'technical': 'Failures using the software',
                'other': 'No listed team clearly fits'}},
            'needs_response': {'type': 'noul', 'instructions': 'Does the ticket explicitly request help or a response?'},
            'urgency': {'type': 'score', 'instructions': 'How urgent is the stated impact, based only on the ticket?',
                        'criteria': ['Routine: no current disruption stated', 'Blocked: work cannot proceed', 'Critical: ongoing broad outage stated']},
        },
    }


def bounded_action(state: dict, actions: dict[str, str]) -> dict:
    if not isinstance(state, dict) or not isinstance(actions, dict) or len(actions) < 2:
        raise ValueError('Provide object state and at least two code-approved actions')
    if not all(isinstance(k, str) and k and isinstance(v, str) and v for k, v in actions.items()):
        raise ValueError('Action labels and descriptions must be nonempty strings')
    if 'ask_human' not in actions:
        raise ValueError('Include an explicit ask_human fallback')
    return {'model': 'jev-latest', 'state': state, 'questions': {
        'next_action': {'type': 'choice', 'instructions': 'Choose a suitable permitted next action. Select ask_human when evidence is insufficient.', 'criteria': dict(actions)}}}


def accept_choice(choice: str, probabilities: dict[str, float], allowed: set[str], *, min_probability: float = 0.85, min_margin: float = 0.2, age_seconds: float = 0, max_age_seconds: float = 5) -> str:
    """Return an allowed label or ask_human. Never executes the selected action.
    Thresholds are illustrative application policy, not calibrated accuracy claims.
    """
    numbers = (min_probability, min_margin, age_seconds, max_age_seconds)
    if any(not isinstance(n, (int, float)) or isinstance(n, bool) or not math.isfinite(n) for n in numbers):
        raise ValueError('Policy values must be finite numbers')
    if not 0 <= min_probability <= 1 or not 0 <= min_margin <= 1 or age_seconds < 0 or max_age_seconds < 0:
        raise ValueError('Policy values are out of range')
    if age_seconds > max_age_seconds or choice not in allowed or choice not in probabilities:
        return 'ask_human'
    values = list(probabilities.values())
    if len(values) < 2 or any(not isinstance(p, (int, float)) or isinstance(p, bool) or not math.isfinite(p) or not 0 <= p <= 1 for p in values):
        return 'ask_human'
    if set(probabilities) != allowed or abs(sum(values) - 1) > 1e-5:
        return 'ask_human'
    p = probabilities[choice]
    runner_up = max(v for k, v in probabilities.items() if k != choice)
    return choice if p >= min_probability and p - runner_up >= min_margin else 'ask_human'


if __name__ == '__main__':
    print(json.dumps(ticket_questions('I see two charges for the same invoice. Please investigate.'), indent=2))
