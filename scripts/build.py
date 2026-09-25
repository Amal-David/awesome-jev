#!/usr/bin/env python3
"""Build the complete directory; offline by default. This is the public build entrypoint."""
from __future__ import annotations
import argparse
import datetime as dt
import html
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/Amal-David/awesome-jev'
DOC = BASE + '/blob/main/docs/'
LEVELS = ('primary-source-reviewed', 'community-indexed', 'readme-matched')
LABELS = dict(zip(LEVELS, ('Reviewed', 'Indexed', 'Auto-discovered')))
MARKERS = ('DIRECTORY_STATS', 'FEATURED_DEMO', 'REVIEWED_PICKS')


def esc(value: object) -> str:
    return html.escape(' '.join(str(value).split()), quote=True)


def safe_url(value: object) -> bool:
    if not isinstance(value, str) or any(ord(c) < 33 or ord(c) == 127 for c in value) or '\\' in value:
        return False
    try:
        u = urlsplit(value)
        return u.scheme in ('https', 'http') and bool(u.hostname) and not u.username and not u.password
    except ValueError:
        return False


def anchor(label: str, url: str) -> str:
    if not safe_url(url):
        raise ValueError('Unsafe navigation link')
    return '<a href="' + esc(url) + '">' + esc(label) + '</a>'


def script_json(data: object) -> str:
    """JSON inside a script element must not permit HTML parser breakout."""
    value = json.dumps(data, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    for char, replacement in (('&', '\\u0026'), ('<', '\\u003c'), ('>', '\\u003e'),
                              ('\u2028', '\\u2028'), ('\u2029', '\\u2029')):
        value = value.replace(char, replacement)
    return value


def replace_once(template: str, name: str, value: str) -> str:
    marker = '<!-- ' + name + ' -->'
    if template.count(marker) != 1:
        raise ValueError('Expected exactly one template marker: ' + name)
    return template.replace(marker, value)


def exclusion_keys(data: dict) -> set[str]:
    if not isinstance(data, dict) or data.get('version') != 1 or not isinstance(data.get('entries'), list):
        raise ValueError('Expected exclusions version 1')
    keys = set()
    for item in data['entries']:
        if not isinstance(item, dict):
            raise ValueError('Invalid exclusion')
        k = item.get('key')
        if not isinstance(k, str) or not item.get('reason') or not safe_url(item.get('source')):
            raise ValueError('Exclusions require a key, reason and public source')
        if k.startswith('repo:'):
            repo = k[5:]
            if not re.fullmatch(r'[a-z0-9_.-]+/[a-z0-9_.-]+', repo) or any(p in ('.', '..') for p in repo.split('/')):
                raise ValueError('Use a canonical lowercase repo key')
        elif not safe_url(k):
            raise ValueError('Invalid exclusion key')
        date = dt.date.fromisoformat(item.get('date', ''))
        if date.isoformat() != item['date'] or date > dt.datetime.now(dt.timezone.utc).date():
            raise ValueError('Invalid exclusion date')
        if k in keys:
            raise ValueError('Duplicate exclusion')
        keys.add(k)
    return keys


def editorial_snapshot(old: list[dict], curated: list[dict], canonical_key) -> list[dict]:
    """Removing a seed entry must not leave an orphaned 'reviewed' cached entry."""
    active = {canonical_key(e) for e in curated}
    result = []
    for original in old:
        entry = dict(original)
        if entry.get('evidence_level') == LEVELS[0] and canonical_key(entry) not in active:
            entry['evidence_level'] = LEVELS[1]
            entry.pop('reviewed', None)
            entry['notes'] = 'Retained as a discovery; no longer in the current editorial selection.'
        result.append(entry)
    return result


def statistics(records: list[dict], cache: dict, refresh: dict) -> dict:
    counts = {level: sum(e.get('evidence_level') == level for e in records) for level in LEVELS}
    repositories = [e for e in records if e.get('repo')]
    checked = [e for e in repositories if e.get('metadata_checked')]
    unavailable = [e for e in checked if e.get('repository_status') == 'unavailable']
    latest = max((e['metadata_checked'] for e in checked), default=None)
    media_errors = sum(bool(e.get('error')) for e in cache.values())
    last_refresh = refresh.get('completed_at')
    if last_refresh:
        stamp = dt.datetime.fromisoformat(last_refresh.replace('Z', '+00:00'))
        if stamp.tzinfo is None or stamp.utcoffset() != dt.timedelta(0):
            raise ValueError('Refresh timestamp must be UTC')
    run = refresh.get('run_url')
    if run and not re.fullmatch(re.escape(BASE) + r'/actions/runs/[0-9]+', run):
        raise ValueError('Invalid refresh receipt URL')
    return {**counts, 'total': len(records), 'repositories': len(repositories),
            'checked_repositories': len(checked), 'unavailable_repositories': len(unavailable),
            'latest_metadata_check': latest, 'media_check_errors': media_errors,
            'completed_at': last_refresh, 'run_url': run}


def summary(stats: dict) -> str:
    reviewed = stats[LEVELS[0]]
    return (f'**{reviewed} reviewed picks**. '
            + anchor('Source notes and licenses', DOC + 'REVIEWED.md')
            + '. The larger discovery catalog is separate.')


def featured(media: dict, cache: dict) -> str:
    item = next((e for e in media['items'] if e['id'] == 'ultrafast'), None)
    if not item:
        return '[See the creator demo gallery](#watch-jev-in-action).'
    image = item.get('image') or cache.get(item['id'], {}).get('image')
    if not image or cache.get(item['id'], {}).get('error'):
        return anchor('Watch the original Browser Use demo', item['watch'])
    if not safe_url(image):
        raise ValueError('Unsafe featured preview')
    return ('<a href="' + esc(item['watch']) + '"><img src="' + esc(image) +
            '" width="680" alt="Browser Use author recording: Jev selects a browser action and target"></a>\n\n'
            '<sub>Browser Use / @gregpr07. Author recording, not our benchmark. '
            + anchor('Implementation', item['repo']) + ' · <a href="#watch-jev-in-action">More demos and videos</a>.</sub>')


def picks(records: list[dict]) -> str:
    chosen = [e for e in records if e.get('evidence_level') == LEVELS[0]]
    groups = [
        ('SDKs and skills', {'official', 'skills', 'sdks'}),
        ('Browser and desktop tools', {'browser'}),
        ('Agent tools', {'agents'}),
        ('Apps and integrations', {'apps', 'integrations'}),
        ('Games and creative projects', {'games', 'demos'}),
        ('Independent models', {'research'}),
        ('Reading and other lists', {'articles', 'lists'}),
    ]
    rows, included = [], set()
    for title, categories in groups:
        found = [e for e in chosen if e['category'] in categories
                 and e.get('kind') != 'adjacent-infrastructure']
        if found:
            rows.extend(['### ' + title, ''])
            for entry in found:
                rows.append('- ' + anchor(entry['name'], entry['url'])
                            + ' - ' + esc(entry['description']))
                included.add(entry['url'])
            rows.append('')
    supporting = [e for e in chosen if e.get('kind') == 'adjacent-infrastructure']
    if supporting:
        rows.extend(['### Supporting drivers', ''])
        for entry in supporting:
            rows.append('- ' + anchor(entry['name'], entry['url'])
                        + ' - ' + esc(entry['description']))
            included.add(entry['url'])
        rows.append('')
    if included != {e['url'] for e in chosen}:
        raise ValueError('A reviewed project has no README category')
    rows.append(anchor(f'All {len(chosen)} reviewed picks: source notes and licenses',
                       DOC + 'REVIEWED.md'))
    return '\n'.join(rows)


def status_page(records: list[dict], cache: dict, stats: dict, excluded: set[str]) -> str:
    completed = stats['completed_at'] or 'Not yet recorded by the unified builder; see Actions history.'
    lines = ['# Freshness and link health', '',
             '[Start here](../README.md) · [Reviewed picks](REVIEWED.md) · [Browse](BROWSE.md) · [Media receipts](MEDIA.md)', '',
             '## Snapshot', '',
             '| Measure | Recorded value |', '|---|---|',
             f'| Reviewed / indexed / auto-discovered | {stats[LEVELS[0]]} / {stats[LEVELS[1]]} / {stats[LEVELS[2]]} |',
             f'| Catalog entries (not all reviewed) | {stats["total"]} |',
             f'| Last completed discovery pass (UTC) | {esc(completed)} |',
             f'| Latest rotating repository metadata check | {esc(stats["latest_metadata_check"] or "Not recorded")} |',
             f'| Repositories with a recorded metadata check | {stats["checked_repositories"]} / {stats["repositories"]} |',
             f'| Repositories unavailable at their last check (404/410) | {stats["unavailable_repositories"]} |',
             f'| Media records with a latest-attempt error | {stats["media_check_errors"]} |',
             f'| Editorial exclusions | {len(excluded)} |', '',
             '## What the numbers mean', '',
             'Repository checks rotate: the newest check date does not mean every entry was checked then. '
             'A 404/410 is an unavailable-repository observation, not proof of permanent deletion. '
             'Media errors may be access restrictions or transient failures, not dead links. '
             '**A complete dead-link count is unknown:** arbitrary demo, skill, code and article URLs are not all crawled.', '',
             'The discovery timestamp advances only after a network discovery pass completes. '
             'An offline directory rebuild, test run or media-only refresh never advances it. '
             'The Actions result, not the cron expression, establishes that a workflow ran successfully.', '']
    if stats['run_url']:
        lines += [anchor('Discovery run receipt', stats['run_url']), '']
    lines += [anchor('All refresh runs', BASE + '/actions/workflows/curate.yml'), '',
              '## Unavailable repositories at their last check', '']
    unavailable = [e for e in records if e.get('repo') and e.get('repository_status') == 'unavailable']
    for entry in unavailable:
        lines += ['- ' + anchor(entry['repo'], entry['url']) + ' — last check ' + esc(entry.get('metadata_checked', 'unknown'))]
    if not unavailable:
        lines += ['No unavailable repositories recorded in this snapshot. This is not an all-links health certificate.']
    lines += ['', '## Media checks needing attention', '']
    failures = [(name, info) for name, info in cache.items() if info.get('error')]
    lines += ['- ' + esc(name) + ' — ' + esc(info['error']) + '; attempted ' + esc(info.get('checked', 'unknown'))
              for name, info in failures] or ['No latest-attempt errors recorded.']
    return '\n'.join(lines) + '\n'


def viewer(template: str, records: list[dict]) -> str:
    fields = ('name', 'repo', 'url', 'description', 'category', 'evidence_level', 'reviewed',
              'license', 'notes', 'kind', 'demo', 'code', 'skill', 'post', 'sources', 'repository_status')
    values = [{k: entry[k] for k in fields if k in entry} for entry in records]
    return replace_once(template, 'CATALOG_JSON', script_json(values))


def module(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def load(path: Path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def write_outputs(outputs: dict[Path, str], check: bool = False) -> None:
    # All render/validation happens before the first write. --check is strictly read-only.
    if any(path.name.lower() == 'readme.md' for path in outputs):
        raise ValueError('README.md is editorial source, not a generated output')
    for path, content in outputs.items():
        current = path.read_text(encoding='utf-8') if path.exists() else None
        if current == content:
            continue
        if check:
            raise ValueError('Generated file is stale: ' + str(path))
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + '.tmp')
        temporary.write_text(content, encoding='utf-8')
        temporary.replace(path)


def build(root: Path = ROOT, *, check: bool = False, refresh: bool = False, refresh_media: bool = False) -> dict:
    if check and (refresh or refresh_media):
        raise ValueError('--check cannot be combined with a network refresh')
    core, media, x = module('curate'), module('curate_media'), module('curate_x')
    seed = load(root / 'data/curated.json', [])
    if not seed:
        raise ValueError('Curated seed must not be empty')
    curated = [core.normalize(e, e.get('evidence') or e.get('url') or 'https://github.com/' + e['repo'], LEVELS[0]) for e in seed]
    core.validate(curated)
    excluded = exclusion_keys(load(root / 'data/exclusions.json', {'version': 1, 'entries': []}))
    if excluded & {core.key(e) for e in curated}:
        raise ValueError('An excluded entry is still in curated.json; resolve the editorial conflict')
    module('check_readme').validate_file(root / 'README.md', seed, excluded)
    old = editorial_snapshot(load(root / 'data/catalog.json', []), curated, core.key)
    records = core.merge(old, [], curated)
    queue = load(root / 'data/discoveries.json', [])
    receipt = load(root / 'data/refresh.json', {})
    if refresh:
        records, queue = core.refresh(records, curated, queue)
        receipt = {'version': 1, 'completed_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
                   'scope': 'bounded discovery and rotating repository metadata checks'}
        run_id = os.environ.get('GITHUB_RUN_ID', '')
        if re.fullmatch(r'[0-9]+', run_id):
            receipt['run_url'] = BASE + '/actions/runs/' + run_id
    records = [e for e in records if core.key(e) not in excluded]
    queue = [e for e in queue if 'repo:' + e['repo'].lower() not in excluded]
    core.validate(records)
    media_data, cache = load(root / 'data/media.json', {}), load(root / 'data/media_cache.json', {})
    media.validate(media_data, cache)
    if refresh_media:
        cache = media.refresh(media_data, cache)
    stats = statistics(records, cache, receipt)
    template = (root / 'templates/README.md').read_text(encoding='utf-8')
    template = media.replace_block(template, media.render(media_data, cache))
    for name, value in zip(MARKERS, (summary(stats), featured(media_data, cache), picks(records))):
        template = replace_once(template, name, value)
    template = replace_once(template, 'FRESHNESS',
        '**Last discovery:** ' + esc(stats['completed_at'] or 'not yet recorded') + ' (UTC). '
        '**Latest repository metadata date:** ' + esc(stats['latest_metadata_check'] or 'not recorded') + '. '
        f'**Unavailable repositories at last check:** {stats["unavailable_repositories"]}. '
        + anchor('Coverage, failures and run receipts', DOC + 'STATUS.md') + '.')
    home, x_index = x.render(load(root / 'data/x_demos.json', {}), template)
    x_index = x_index.replace('scripts/curate_x.py', 'scripts/build.py')
    media_index = media.source_index(media_data, cache).replace('scripts/curate_media.py --refresh', 'scripts/build.py --refresh-media').replace('scripts/curate_media.py', 'scripts/build.py').replace('Run it before `curate_x.py`.', 'The unified builder also regenerates the supporting directory and the local viewer.')
    _, catalog = core.render(records)
    catalog = catalog.replace('[Back to curated selections](../README.md)', '[Reviewed picks](REVIEWED.md) · [Start here](../README.md) · [Search and filters](BROWSE.md)')
    reviewed = [e for e in records if e['evidence_level'] == LEVELS[0]]
    review_page = '# Reviewed Jev picks\n\n[Start here](../README.md) · [Browse by task](START_HERE.md) · [Search and filters](BROWSE.md) · [Full catalog](CATALOG.md)\n\n'
    review_page += f'**{len(reviewed)} selections reviewed against primary public sources.** Source review is not a security audit or a reproduced benchmark.\n\n'
    for category, title in core.CATEGORIES.items():
        group = [e for e in reviewed if e['category'] == category]
        if group:
            review_page += core.section(title, group)
    # README.md is editorial source. Only the supporting directory is rendered.
    outputs = {
        root / 'docs/DIRECTORY.md': home,
        root / 'docs/REVIEWED.md': review_page, root / 'docs/CATALOG.md': catalog,
        root / 'docs/X_DEMOS.md': x_index, root / 'docs/MEDIA.md': media_index,
        root / 'docs/STATUS.md': status_page(records, cache, stats, excluded),
        root / 'docs/catalog.html': viewer((root / 'templates/catalog.html').read_text(encoding='utf-8'), records),
        root / 'data/catalog.json': core.dump(records), root / 'data/discoveries.json': core.dump(queue),
        root / 'data/media_cache.json': core.dump(cache), root / 'data/refresh.json': core.dump(receipt),
    }
    write_outputs(outputs, check)
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate all generated files offline, without writing')
    parser.add_argument('--refresh', action='store_true', help='Run bounded GitHub discovery and record its completion time')
    parser.add_argument('--refresh-media', action='store_true', help='Check public media; no API keys are read by the media checker')
    args = parser.parse_args()
    if args.check and (args.refresh or args.refresh_media):
        parser.error('--check cannot be combined with refresh flags')
    stats = build(check=args.check, refresh=args.refresh, refresh_media=args.refresh_media)
    print(f'Built directory: {stats[LEVELS[0]]} reviewed picks; {stats["total"]} catalog entries; editorial README left untouched.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
