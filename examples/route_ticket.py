"""Print a request offline, or opt in to one paid TypeSafe SDK call with --live."""
import argparse
import json
import os
from question_packs import ticket_questions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ticket', nargs='?', default='I was billed twice for one invoice. Please investigate.')
    parser.add_argument('--live', action='store_true', help='Make a real API call using TYPESAFE_API_KEY; provider charges may apply')
    args = parser.parse_args()
    payload = ticket_questions(args.ticket)
    if not args.live:
        print(json.dumps(payload, indent=2))
        return
    if not os.environ.get('TYPESAFE_API_KEY'):
        parser.error('Set TYPESAFE_API_KEY locally; never commit it.')
    try:
        from typesafe_sdk import Choice, TypeSafeClient
    except ImportError:
        parser.error('Install the official SDK: python -m pip install typesafe-sdk')
    question = payload['questions']['department']
    # The live example intentionally makes just one narrow Choice call.
    with TypeSafeClient() as client:
        result = client.system_one(state=payload['state'], questions={
            'department': Choice(instructions=question['instructions'], criteria=question['criteria'])})
    print(result.choices['department'].choice)


if __name__ == '__main__':
    main()
