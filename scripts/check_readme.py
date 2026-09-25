#!/usr/bin/env python3
"""Read-only editorial membership/structure checks; not a substitute for awesome-lint."""
from __future__ import annotations

import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
HEADING = '# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)'
EXTRA_SECTIONS = {'Contents', 'Getting Started', 'Demos', 'Contributing', 'Footnotes'}
ENTRY = re.compile(r'^- \[([^\]\n]+)\]\((https://[^\s)]+)\) - ([A-Z0-9][^\n]*\.)$')
TOC_ENTRY = re.compile(r'^- \[([^\]\n]+)\]\(#([a-z0-9-]+)\)$')


def canonical_url(value: str) -> str:
    """Compare front-page project links without losing meaningful query parameters."""
    if not isinstance(value, str) or any(ord(c) < 33 or ord(c) == 127 for c in value) or '\\' in value:
        raise ValueError('Invalid project URL')
    try:
        parsed = urlsplit(value)
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Project URLs must use HTTPS without embedded credentials')
        path = parsed.path.rstrip('/')
        if parsed.hostname.lower() == 'github.com':
            path = path.removesuffix('.git').lower()
        return urlunsplit((parsed.scheme, parsed.netloc.lower(), path, parsed.query, ''))
    except (TypeError, ValueError) as exc:
        raise ValueError('Invalid project URL') from exc


def project_url(entry: dict) -> str:
    return canonical_url('https://github.com/' + entry['repo'] if entry.get('repo') else entry['url'])


def validate_text(text: str, curated: list[dict], excluded: set[str]) -> set[str]:
    """Reject unsourced/duplicate entries and structural drift without generating prose."""
    lines = text.splitlines()
    if not lines or lines[0] != HEADING:
        raise ValueError('Use the Awesome Jev heading and official Awesome badge')
    if not text.endswith('\n'):
        raise ValueError('README must end with a newline')
    for marker in ('<!-- DIRECTORY_STATS -->', '<!-- REVIEWED_PICKS -->', '<!-- MEDIA_GALLERY:', '<!-- X_DEMOS -->'):
        if marker in text:
            raise ValueError('Generated markers belong in the supporting directory, not README.md')
    headings = re.findall(r'^## (.+)$', text, re.M)
    if not headings or headings[0] != 'Contents' or len(headings) != len(set(headings)):
        raise ValueError('Contents must be the first section and section names must be unique')
    if 'Footnotes' not in headings or headings[-1] != 'Footnotes':
        raise ValueError('Keep supplementary material in a final Footnotes section')
    expected_toc = [(name, re.sub(r'[^a-z0-9 -]', '', name.lower()).replace(' ', '-'))
                    for name in headings if name not in {'Contents', 'Contributing', 'Footnotes'}]
    toc, section = [], None
    allowed = {project_url(item): item for item in curated}
    seen: set[str] = set()
    for number, line in enumerate(lines, 1):
        if line.startswith('## '):
            section = line[3:]
            continue
        if not line.startswith(('- ', '* ', '+ ')):
            continue
        if section == 'Contents':
            match = TOC_ENTRY.fullmatch(line)
            if not match:
                raise ValueError(f'Line {number}: use a flat Markdown contents list')
            toc.append(match.groups())
            continue
        if section in EXTRA_SECTIONS:
            continue
        if section is None:
            raise ValueError(f'Line {number}: project entry appears before Contents')
        match = ENTRY.fullmatch(line)
        if not match:
            raise ValueError(f'Line {number}: expected - [Project](URL) - Capitalized description.')
        url = canonical_url(match.group(2))
        if url not in allowed:
            raise ValueError(f'Line {number}: project has no current curated source record: {url}')
        if url in seen:
            raise ValueError(f'Line {number}: duplicate project: {url}')
        entry = allowed[url]
        key = 'repo:' + entry['repo'].lower() if entry.get('repo') else project_url(entry)
        if key in excluded:
            raise ValueError(f'Line {number}: project is excluded: {url}')
        kind = entry.get('kind')
        if (section == 'Independent Models') != (kind == 'independent-reproduction'):
            raise ValueError(f'Line {number}: keep independent models in their own section')
        if (section == 'Supporting Drivers') != (kind == 'adjacent-infrastructure'):
            raise ValueError(f'Line {number}: keep supporting drivers in their own section')
        seen.add(url)
    if toc != expected_toc:
        raise ValueError('Contents must match the section headings and omit Contributing/Footnotes')
    if not seen:
        raise ValueError('README must contain source-backed project selections')
    return seen


def validate_file(path: Path, curated: list[dict], excluded: set[str]) -> set[str]:
    if (path.parent / '.github/README.md').exists():
        raise ValueError('.github/README.md must not shadow the editorial README')
    return validate_text(path.read_text(encoding='utf-8'), curated, excluded)


def main() -> None:
    curated = json.loads((ROOT / 'data/curated.json').read_text(encoding='utf-8'))
    exclusions = json.loads((ROOT / 'data/exclusions.json').read_text(encoding='utf-8'))
    selected = validate_file(ROOT / 'README.md', curated, {entry['key'] for entry in exclusions['entries']})
    print(f'Editorial README: {len(selected)} source-backed entries; no files written.')


if __name__ == '__main__':
    main()
