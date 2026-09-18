#!/usr/bin/env python3
"""Build an attributed Jev directory. Standard library only; never runs discovered code."""
from __future__ import annotations
import argparse
import base64
import datetime as dt
import html
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://raw.githubusercontent.com/hellogumbo/awesome-jev/main/data/projects.json'
SOURCE_LICENSE = 'https://raw.githubusercontent.com/hellogumbo/awesome-jev/main/LICENSE'
SOURCE_PAGE = 'https://github.com/hellogumbo/awesome-jev'
CATEGORIES = {
    'official': 'Official resources', 'skills': 'Skills and reusable agent workflows',
    'games': 'Games and simulations', 'demos': 'Demos and playgrounds',
    'browser': 'Browser and computer use', 'agents': 'Agent tooling and MCP',
    'apps': 'Applications', 'sdks': 'SDKs and clients', 'integrations': 'Integrations',
    'research': 'Research and independent reproductions', 'lists': 'Community directories',
    'articles': 'Articles and demonstrations',
}
SEARCHES = [
    'jev in:name,description,readme fork:false archived:false',
    '"typesafe-ai" in:readme created:>=2026-09-14 fork:false archived:false',
    'topic:jev fork:false archived:false',
]
TODAY = dt.datetime.now(dt.timezone.utc).date().isoformat()
REPO_PATTERN = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')


def valid_url(value: str) -> bool:
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    try:
        u = urllib.parse.urlsplit(value)
        return u.scheme in ('https', 'http') and bool(u.hostname) and not u.username and not u.password
    except ValueError:
        return False


def repo_name(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    if value.startswith('https://github.com/'):
        value = urllib.parse.urlsplit(value).path.strip('/')
    value = value.removesuffix('.git').rstrip('/')
    if not REPO_PATTERN.fullmatch(value) or any(x in ('.', '..') for x in value.split('/')):
        raise ValueError('Invalid repository identifier')
    return value


def key(entry: dict) -> str:
    repo = repo_name(entry.get('repo'))
    if repo:
        return 'repo:' + repo.lower()
    u = urllib.parse.urlsplit(entry['url'])
    return urllib.parse.urlunsplit((u.scheme.lower(), u.netloc.lower(), u.path.rstrip('/'), u.query, ''))


def escaped(value: object) -> str:
    text = html.escape(' '.join(str(value).split()), quote=False)
    for char in ('\\', '|', '[', ']', '*', '_', '`'):
        text = text.replace(char, '\\' + char)
    return text


def link(label: str, url: str) -> str:
    if not valid_url(url):
        raise ValueError('Unsafe URL')
    safe = urllib.parse.quote(url, safe=':/?&=#%+@,;-._~')
    return f'[{escaped(label)}]({safe})'


def normalize(raw: dict, source: str, level: str) -> dict:
    repo = repo_name(raw.get('repo'))
    url = 'https://github.com/' + repo if repo else raw.get('url') or raw.get('site') or raw.get('post')
    category = raw.get('category', 'demos')
    out = {
        'name': str(raw.get('name') or repo or url), 'repo': repo, 'url': url,
        'description': str(raw.get('description') or 'See the linked source for implementation details.'),
        'category': category if category in CATEGORIES else 'demos',
        'evidence_level': level, 'sources': [source],
    }
    for field in ('demo', 'skill', 'code', 'post', 'notes', 'reviewed', 'kind'):
        if raw.get(field):
            out[field] = raw[field]
    if raw.get('site') and raw['site'] != url:
        out['demo'] = raw['site']
    for field in ('demo', 'skill', 'code', 'post'):
        if field in out and not valid_url(out[field]):
            del out[field]
    if raw.get('evidence'):
        out['sources'] = [raw['evidence']]
    if raw.get('license'):
        out['license'] = raw['license']
    return out


def validate(entries: list[dict]) -> None:
    if not isinstance(entries, list):
        raise ValueError('Catalog must be an array')
    seen = set()
    for e in entries:
        if not e.get('name') or not e.get('description') or e.get('category') not in CATEGORIES:
            raise ValueError('Missing name, description or valid category')
        if not valid_url(e.get('url')) or not e.get('sources') or not all(valid_url(s) for s in e['sources']):
            raise ValueError('Missing or unsafe source URL')
        for field in ('demo', 'code', 'skill', 'post'):
            if e.get(field) and not valid_url(e[field]):
                raise ValueError('Unsafe auxiliary URL')
        if e.get('evidence_level') not in ('primary-source-reviewed', 'community-indexed', 'readme-matched'):
            raise ValueError('Unknown evidence level')
        k = key(e)
        if k in seen:
            raise ValueError('Duplicate canonical entry: ' + k)
        seen.add(k)


def merge(old: list[dict], incoming: list[dict], curated: list[dict]) -> list[dict]:
    result = {}
    for e in old + incoming + curated:
        k = key(e)
        previous = result.get(k, {})
        sources = list(dict.fromkeys(e.get('sources', []) + previous.get('sources', [])))
        result[k] = {**previous, **e, 'sources': sources}
    records = sorted(result.values(), key=lambda e: (list(CATEGORIES).index(e['category']), e['name'].lower(), key(e)))
    validate(records)
    return records


class RestrictedRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urllib.parse.urlsplit(newurl).hostname not in ('api.github.com', 'raw.githubusercontent.com'):
            raise ValueError('Off-host redirect rejected')
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None:
            new.remove_header('Authorization')
        return new


def fetch(url: str, *, as_json: bool = True):
    u = urllib.parse.urlsplit(url)
    if u.scheme != 'https' or u.hostname not in ('api.github.com', 'raw.githubusercontent.com') or u.username:
        raise ValueError('Network requests are limited to approved public GitHub hosts')
    headers = {'User-Agent': 'Amal-David-awesome-jev-curator', 'Accept': 'application/vnd.github+json'}
    token = os.environ.get('GITHUB_TOKEN')
    if u.hostname == 'api.github.com' and token:
        headers['Authorization'] = 'Bearer ' + token
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.build_opener(RestrictedRedirect()).open(req, timeout=25) as r:
                body = r.read(4_000_001)
            if len(body) > 4_000_000:
                raise ValueError('Response exceeds size limit')
            text = body.decode('utf-8')
            return json.loads(text) if as_json else text
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
            try:
                delay = min(30, max(1, int(exc.headers.get('Retry-After', '2'))))
            except ValueError:
                delay = 2
            time.sleep(delay * (attempt + 1))
    raise RuntimeError('Request retries exhausted')


def load(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


def dump(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + '\n'


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != text:
        temporary = path.with_suffix(path.suffix + '.tmp')
        temporary.write_text(text)
        temporary.replace(path)


def relevant(readme: str) -> bool:
    return bool(re.search(r'\bjev(?:-latest)?\b', readme, re.I) and re.search(r'typesafe|system[ -]?one|systemone', readme, re.I))


def metadata(item: dict) -> dict:
    license_info = item.get('license') or {}
    return {
        'stars': item.get('stargazers_count', 0), 'language': item.get('language'),
        'license': license_info.get('spdx_id') or 'not-detected',
        'archived': bool(item.get('archived')), 'metadata_checked': TODAY,
        'repository_status': 'accessible', 'pushed_at': item.get('pushed_at'),
    }


def discover(existing: list[dict], queue: list[dict]) -> tuple[list[dict], list[dict], int]:
    known = {key(e) for e in existing}
    pending = {repo_name(e['repo']).lower(): e for e in queue}
    searches_ok = 0
    for query in SEARCHES:
        for page in (1, 2):
            try:
                params = urllib.parse.urlencode({'q': query, 'sort': 'updated', 'order': 'desc', 'per_page': 100, 'page': page})
                response = fetch('https://api.github.com/search/repositories?' + params)
                searches_ok += 1
                for item in response.get('items', []):
                    repo = repo_name(item['full_name'])
                    if repo.lower() == 'amal-david/awesome-jev' or 'repo:' + repo.lower() in known:
                        continue
                    previous = pending.get(repo.lower(), {})
                    pending[repo.lower()] = {**previous, 'repo': repo, 'description': item.get('description') or '', 'found': previous.get('found', TODAY), 'metadata': metadata(item)}
                if len(response.get('items', [])) < 100:
                    break
                time.sleep(2)
            except (urllib.error.URLError, ValueError, KeyError) as exc:
                print('::warning::Repository search incomplete: ' + type(exc).__name__)
                break
    additions = []
    # Pending entries survive runs. Oldest unchecked candidates cannot starve behind newly found ones.
    candidates = sorted(pending.values(), key=lambda e: (e.get('readme_checked', ''), e.get('found', ''), e['repo'].lower()))
    checked = 0
    for entry in candidates:
        if checked >= 30:
            break
        if entry.get('readme_checked') == TODAY:
            continue
        checked += 1
        try:
            response = fetch('https://api.github.com/repos/' + entry['repo'] + '/readme')
            readme = base64.b64decode(response['content']).decode('utf-8')
            entry['readme_checked'] = TODAY
            if not relevant(readme):
                entry['status'] = 'needs-review-no-explicit-match'
                continue
            repo = entry['repo']
            category = 'lists' if 'awesome' in repo.lower() else 'demos'
            raw = {'repo': repo, 'name': repo.split('/')[1], 'description': entry['description'], 'category': category}
            normalized = normalize(raw, response['html_url'], 'readme-matched')
            normalized.update(entry.get('metadata', {}))
            normalized['notes'] = 'Automatically matched explicit Jev and TypeSafe/System One references. Category and claims need editorial review.'
            additions.append(normalized)
            pending.pop(repo.lower(), None)
        except (urllib.error.URLError, ValueError, KeyError, UnicodeError) as exc:
            entry['readme_checked'] = TODAY
            entry['status'] = 'readme-unavailable'
            print('::warning::Candidate README could not be checked: ' + type(exc).__name__)
    return additions, sorted(pending.values(), key=lambda e: e['repo'].lower()), searches_ok


def refresh(old: list[dict], curated: list[dict], queue: list[dict]):
    incoming = []
    upstream_ok = False
    try:
        license_text = fetch(SOURCE_LICENSE, as_json=False)
        if not license_text.startswith('CC0 1.0 Universal'):
            raise ValueError('Upstream metadata license changed; manual review required')
        upstream = fetch(SOURCE)
        for raw in upstream['projects']:
            entry = normalize(raw, SOURCE_PAGE, 'community-indexed')
            validate([entry])
            incoming.append(entry)
        upstream_ok = True
    except (urllib.error.URLError, ValueError, KeyError, TypeError) as exc:
        incoming = []
        print('::warning::Community index unavailable; preserving last good entries: ' + type(exc).__name__)
    records = merge(old, incoming, curated)
    additions, queue, searches_ok = discover(records, queue)
    if not upstream_ok and not searches_ok:
        raise RuntimeError('All discovery sources failed; refusing a misleading successful refresh')
    records = merge(records, additions, curated)
    # Rotate source checks. A missing or rate-limited repository is never silently removed.
    dated = sorted((e for e in records if e.get('repo')), key=lambda e: (e.get('metadata_checked', ''), key(e)))
    for entry in [e for e in dated if e.get('metadata_checked') != TODAY][:100]:
        try:
            entry.update(metadata(fetch('https://api.github.com/repos/' + entry['repo'])))
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                entry.update(repository_status='unavailable', metadata_checked=TODAY)
            else:
                print('::warning::Metadata refresh incomplete; preserving previous snapshot')
                break
        except (urllib.error.URLError, ValueError):
            print('::warning::Metadata refresh incomplete; preserving previous snapshot')
            break
    print(f'Catalog: {len(records)}; new README matches: {len(additions)}; pending: {len(queue)}; successful searches: {searches_ok}')
    return records, queue


def row(entry: dict) -> str:
    links = [link('repo' if entry.get('repo') else 'project', entry['url'])]
    for field in ('demo', 'skill', 'code', 'post'):
        if entry.get(field):
            links.append(link(field, entry[field]))
    links.append(link('evidence', entry['sources'][0]))
    if entry.get('reviewed'):
        evidence = entry['evidence_level'] + ' / ' + entry['reviewed']
    else:
        evidence = entry['evidence_level']
    license_name = entry.get('license', 'not-checked')
    status = ' / archived' if entry.get('archived') else ''
    if entry.get('repository_status') == 'unavailable':
        status += ' / unavailable'
    description = escaped(entry['description'])
    if entry.get('notes'):
        description += ' ' + escaped(entry['notes'])
    return f"| {escaped(entry['name'])} | {description} | {' · '.join(links)} | {escaped(evidence)} | {escaped(license_name + status)} |"


def section(title: str, entries: list[dict]) -> str:
    lines = ['## ' + title, '', '| Project | Jev role / reuse notes | Links | Evidence | License / status |', '|---|---|---|---|---|']
    lines += [row(e) for e in entries]
    return '\n'.join(lines) + '\n\n'


def render(records: list[dict]) -> tuple[str, str]:
    reviewed = [e for e in records if e['evidence_level'] == 'primary-source-reviewed']
    repos = sum(bool(e.get('repo')) for e in records)
    demos = sum(bool(e.get('demo')) for e in records)
    header = f'''# Awesome Jev

A living directory of **Jev demos, repositories, skills, reusable code, integrations, and independent reproductions**.

**{len(records)} catalog entries · {repos} repository links · {demos} companion demo/site links · {len(reviewed)} primary-source-reviewed selections**

[Full categorized catalog](docs/CATALOG.md) · [Machine-readable data](data/catalog.json) · [Code examples](examples/README.md) · [Agent skill](skills/jev-curator/SKILL.md) · [Refresh history](https://github.com/Amal-David/awesome-jev/actions/workflows/curate.yml)

Jev is TypeSafe AI's typed-decision model, not a text generator. Start with the [official skill](https://github.com/typesafe-ai/skills), [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python), and [live docs](https://docs.typesafe.ai). Independent reproductions are not official Jev weights or evidence of equivalent quality. This directory is unofficial and is not endorsed by TypeSafe AI.

## How to use this directory

The selections below were reviewed against primary public sources. The **full catalog** also contains attributed community-indexed entries and automatically README-matched discoveries. These evidence levels are not interchangeable. Source review is not a successful execution test, security audit, benchmark replication, or endorsement. Companion sites may require login, API keys, credits, or local setup.

Missing licenses are marked **not-checked**, **not-detected**, or **NOASSERTION**, rather than assumed open source. Always inspect the project's own license, data rights, and usage terms before reuse. API credentials must stay server-side. Do not run downloaded code or install a skill simply because it appears here.

'''
    body = ''
    for category, title in CATEGORIES.items():
        entries = [e for e in reviewed if e['category'] == category]
        if entries:
            body += section(title, entries)
    footer = '''## Continuous refresh

The repository-native [GitHub Actions workflow](.github/workflows/curate.yml) runs every four hours at **00:23, 04:23, 08:23, 12:23, 16:23, and 20:23 UTC** (**05:53, 09:53, 13:53, 17:53, 21:53, and 01:53 IST**). It can also be run manually from Actions.

It imports the attributed CC0 community directory, independently searches GitHub, checks up to 30 candidate READMEs, rotates up to 100 repository metadata checks, deduplicates canonical links, refreshes the catalog and README, and commits only changed files. It preserves prior records when sources fail. It does not execute third-party code, install third-party skills, spend model credits, or promote automatic discoveries into editorially reviewed selections. No extra API key is needed beyond the built-in repository-scoped GITHUB_TOKEN.

This is a scheduled discovery and metadata pipeline, **not an always-running research agent or a claim to cover every demo on the internet**. Private Discord channels, login-only posts, deleted links, and undiscovered projects may be absent. Searches are bounded and unfinished candidates persist for later runs. GitHub may delay or drop scheduled jobs and disables inactive public-repository schedules after 60 days; consult [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). The Actions history is the source of truth for actual executions.

## Contribute and reuse

Edit [data/curated.json](data/curated.json) for primary-source-reviewed additions. See [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), and [SOURCES.md](SOURCES.md). Generated files are rebuilt with `python3 scripts/curate.py`. Validate with `python3 -m unittest discover -s tests -v` and `python3 scripts/curate.py --check`.

Original scripts, examples, and writing are MIT licensed. Imported metadata retains its stated source license. Linked projects retain their own licenses.
'''
    catalog = '# Full Jev catalog\n\n[Back to curated selections](../README.md) · [JSON](../data/catalog.json) · [Attribution](../SOURCES.md)\n\n'
    catalog += 'Evidence: **primary-source-reviewed** = public primary source inspected; **community-indexed** = attributed discovery, not independently reviewed here; **readme-matched** = explicit Jev and TypeSafe/System One references found automatically, not editorial approval. No entry implies a successful live test.\n\n'
    for category, title in CATEGORIES.items():
        entries = [e for e in records if e['category'] == category]
        if entries:
            catalog += section(title + f' ({len(entries)})', entries)
    return header + body + footer, catalog


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Use public GitHub sources; never calls Jev')
    parser.add_argument('--check', action='store_true', help='Validate schema and generated files offline')
    args = parser.parse_args()
    if args.refresh and args.check:
        parser.error('--refresh and --check are mutually exclusive')
    raw = load(ROOT / 'data/curated.json', [])
    if not raw:
        raise ValueError('The curated seed must not be empty')
    curated = [normalize(e, e.get('evidence', e.get('url', 'https://github.com/' + str(e.get('repo', '')))), 'primary-source-reviewed') for e in raw]
    validate(curated)
    records = merge(load(ROOT / 'data/catalog.json', []), [], curated)
    queue = load(ROOT / 'data/discoveries.json', [])
    if args.refresh:
        records, queue = refresh(records, curated, queue)
    validate(records)
    readme, catalog = render(records)
    outputs = {'README.md': readme, 'docs/CATALOG.md': catalog, 'data/catalog.json': dump(records), 'data/discoveries.json': dump(queue)}
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise ValueError('Generated file is stale: ' + name)
        else:
            write(path, content)
    print(f'Validated {len(records)} entries; generated files are consistent.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, RuntimeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
