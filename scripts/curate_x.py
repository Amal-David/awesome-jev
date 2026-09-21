#!/usr/bin/env python3
"""Render the editorial homepage and X demo index offline; never fetch or execute links."""
from __future__ import annotations
import argparse
import datetime as dt
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKER = '<!-- X_DEMOS -->'
REPO = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+')
POST = re.compile(r'/[A-Za-z0-9_]{1,15}/status/[0-9]+')
STATUS = {'indexed-reference', 'primary-post-reviewed'}


def safe_url(value: object) -> bool:
    if not isinstance(value, str) or not value or any(ord(c) < 33 or ord(c) == 127 for c in value):
        return False
    try:
        u = urlsplit(value)
        return (u.scheme == 'https' and bool(u.hostname) and not u.username
                and not u.password and u.port in (None, 443) and '\\' not in value)
    except ValueError:
        return False


def post_id(url: str) -> str:
    if not safe_url(url):
        raise ValueError('Unsafe X URL')
    u = urlsplit(url)
    if u.netloc != 'x.com' or not POST.fullmatch(u.path) or u.query or u.fragment:
        raise ValueError('Use a canonical https://x.com/author/status/id URL')
    return u.path.rsplit('/', 1)[-1]


def text(value: object) -> str:
    out = html.escape(' '.join(str(value).split()), quote=False)
    for char in ('\\', '|', '[', ']', '*', '_', '`'):
        out = out.replace(char, '\\' + char)
    return out


def link(label: str, url: str) -> str:
    if not safe_url(url):
        raise ValueError('Unsafe link')
    return f'[{text(label)}]({quote(url, safe=":/?&=#%+@,;-._~")})'


def validate(data: dict) -> None:
    if not isinstance(data, dict) or data.get('version') != 1:
        raise ValueError('Expected X catalog version 1')
    if not isinstance(data.get('demos'), list) or not data['demos']:
        raise ValueError('Demos must be a nonempty array')
    if not isinstance(data.get('roundups'), list):
        raise ValueError('Roundups must be an array')
    seen_ids, seen_posts = set(), set()
    for item in data['demos']:
        if not isinstance(item, dict):
            raise ValueError('Each demo must be an object')
        for field in ('id', 'name', 'author', 'post', 'repo', 'source', 'description', 'pattern', 'notes', 'reviewed', 'post_status'):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError('Missing demo field: ' + field)
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', item['id']) or item['id'] in seen_ids:
            raise ValueError('Invalid or duplicate demo ID')
        seen_ids.add(item['id'])
        ident = post_id(item['post'])
        if ident in seen_posts:
            raise ValueError('Duplicate X post')
        seen_posts.add(ident)
        if not REPO.fullmatch(item['repo']) or any(p in ('.', '..') for p in item['repo'].split('/')):
            raise ValueError('Invalid repository')
        expected = 'https://github.com/' + item['repo'] + '/'
        if not safe_url(item['source']) or not item['source'].startswith(expected):
            raise ValueError('Evidence must belong to the linked repository')
        if item['post_status'] not in STATUS:
            raise ValueError('Unknown post verification status')
        date = dt.date.fromisoformat(item['reviewed'])
        if date.isoformat() != item['reviewed'] or date > dt.datetime.now(dt.timezone.utc).date():
            raise ValueError('Invalid source review date')
    for item in data['roundups']:
        if not isinstance(item, dict) or any(not isinstance(item.get(k), str) or not item[k].strip()
                                             for k in ('name', 'post', 'notes')):
            raise ValueError('Roundup needs name, post, and coverage notes')
        ident = post_id(item['post'])
        if ident in seen_posts:
            raise ValueError('Duplicate X post')
        seen_posts.add(ident)


def table(demos: list[dict]) -> str:
    lines = ['| Demo | What Jev does | Watch / inspect |', '|---|---|---|']
    for item in demos:
        urls = ' · '.join((link('X demo', item['post']), link('repo', 'https://github.com/' + item['repo']),
                            link('source', item['source'])))
        lines.append(f"| **{text(item['name'])}** — {text(item['author'])} | {text(item['description'])} | {urls} |")
    return '\n'.join(lines)


def render(data: dict, template: str) -> tuple[str, str]:
    validate(data)
    if template.count(MARKER) != 1:
        raise ValueError('Homepage template must contain exactly one X marker')
    rows = table(data['demos'])
    home = template.replace(MARKER, rows).rstrip() + '\n'
    lines = ['# Curated X demos', '',
             '[Repository homepage](https://github.com/Amal-David/awesome-jev#readme) · [JSON source](../data/x_demos.json)', '',
             'Watch the original post, then inspect the implementation. The project descriptions below are based on the linked authors\' repository documentation. They are not live execution tests or security endorsements.', '',
             '## Roundup that seeded this collection', '']
    for item in data['roundups']:
        lines += [link(item['name'], item['post']), '', text(item['notes']), '']
    lines += ['## Demos and code', '', rows, '', '## Reuse patterns and evidence', '']
    for item in data['demos']:
        status = ('Original post inspected' if item['post_status'] == 'primary-post-reviewed'
                  else 'X URL is an indexed social reference; the original post was not fully retrievable in this review')
        lines += ['### ' + text(item['name']), '',
                  '**Pattern:** ' + text(item['pattern']), '',
                  '**Source review:** ' + text(item['reviewed']) + '. ' + link('Primary project source', item['source']) + '.', '',
                  '**Post access:** ' + status + '.', '',
                  '**Limitations:** ' + text(item['notes']), '']
    lines += ['## Curation rules', '',
              'Edit `data/x_demos.json`, not the generated tables. Keep canonical X status URLs and direct author/project evidence. Distinguish a post reference from a fully reviewed post; never infer that every entry belongs to the same thread. Do not invent repositories, copy unlicensed media, or treat reported timing, cost, or profit as independently reproduced.', '',
              'Run `python3 scripts/curate_x.py` and `python3 scripts/curate_x.py --check`. The four-hour workflow validates and preserves this section; it does not authenticate to X or autonomously scrape every thread reply. New editorial selections require source review.', '']
    return home, '\n'.join(lines)


def outputs(root: Path) -> dict[Path, str]:
    data = json.loads((root / 'data/x_demos.json').read_text(encoding='utf-8'))
    template = (root / 'templates/README.md').read_text(encoding='utf-8')
    home, index = render(data, template)
    return {root / '.github/README.md': home, root / 'docs/X_DEMOS.md': index}


def build(root: Path, check: bool = False) -> None:
    for path, content in outputs(root).items():
        if check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise ValueError('Generated X file is stale: ' + str(path.relative_to(root)))
        elif not path.exists() or path.read_text(encoding='utf-8') != content:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(path.suffix + '.tmp')
            temporary.write_text(content, encoding='utf-8')
            temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated files without writing or networking')
    args = parser.parse_args()
    build(ROOT, args.check)
    print('Curated X data and editorial homepage are consistent.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
