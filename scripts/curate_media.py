#!/usr/bin/env python3
"""Build source-attributed README media. Never run projects or copy their media files."""
from __future__ import annotations
import argparse
import datetime as dt
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlencode, urlsplit
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- MEDIA_GALLERY:START -->', '<!-- MEDIA_GALLERY:END -->'
GROUPS = {'x', 'projects', 'youtube', 'videos'}
IMAGE_HOSTS = {'raw.githubusercontent.com', 'github.com', 'pbs.twimg.com', 'i.ytimg.com'}
FETCH_HOSTS = IMAGE_HOSTS | {'api.fxtwitter.com', 'www.youtube.com',
    'github-production-user-asset-6210df.s3.amazonaws.com',
    'github-production-user-asset-6210df.s3.us-east-1.amazonaws.com'}
TODAY = dt.datetime.now(dt.timezone.utc).date().isoformat()


def safe_url(value: object, hosts: set[str] | None = None) -> bool:
    if not isinstance(value, str) or not value or any(ord(c) < 33 or ord(c) == 127 for c in value):
        return False
    try:
        u = urlsplit(value)
        return (u.scheme == 'https' and bool(u.hostname) and u.port in (None, 443)
                and not u.username and not u.password and '\\' not in value
                and (hosts is None or u.hostname in hosts))
    except ValueError:
        return False


def esc(value: object) -> str:
    return html.escape(' '.join(str(value).split()), quote=True)


def anchor(label: str, url: str) -> str:
    if not safe_url(url):
        raise ValueError('Unsafe media link')
    return '<a href="' + esc(url) + '">' + esc(label) + '</a>'


def validate(data: dict, cache: dict) -> None:
    if not isinstance(data, dict) or data.get('version') != 1:
        raise ValueError('Expected media catalog version 1')
    items = data.get('items')
    if not isinstance(items, list) or not 1 <= len(items) <= 40 or not isinstance(cache, dict):
        raise ValueError('Invalid media collection')
    seen = set()
    for item in items:
        for field in ('id', 'group', 'title', 'creator', 'watch', 'source', 'caption', 'note'):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError('Missing media field: ' + field)
        ident = item['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', ident) or ident in seen:
            raise ValueError('Invalid or duplicate media ID')
        seen.add(ident)
        if item['group'] not in GROUPS:
            raise ValueError('Unknown media group')
        for field in ('watch', 'source', 'repo'):
            if item.get(field) and not safe_url(item[field]):
                raise ValueError('Unsafe source link')
        for image in (item.get('image'), cache.get(ident, {}).get('image')):
            if image and not safe_url(image, IMAGE_HOSTS):
                raise ValueError('Unapproved image host')
        watch = item['watch']
        if item['group'] == 'x' and not re.fullmatch(r'https://x\.com/[A-Za-z0-9_]{1,15}/status/[0-9]+', watch):
            raise ValueError('Expected canonical X post')
        if item['group'] == 'youtube' and not re.fullmatch(r'https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}', watch):
            raise ValueError('Expected canonical YouTube video')
        if item['group'] == 'videos' and not re.fullmatch(r'https://github\.com/user-attachments/assets/[0-9a-f-]{36}', watch):
            raise ValueError('Native videos must be original GitHub attachments')
    if set(cache) - seen:
        raise ValueError('Cache contains unknown media IDs')
    for record in cache.values():
        if not isinstance(record, dict):
            raise ValueError('Invalid media cache entry')
        if 'checked' in record:
            date = dt.date.fromisoformat(record['checked'])
            if date.isoformat() != record['checked'] or record['checked'] > TODAY:
                raise ValueError('Invalid media check date')


class RestrictedRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not safe_url(newurl, FETCH_HOSTS):
            raise ValueError('Unapproved media redirect')
        out = super().redirect_request(req, fp, code, msg, headers, newurl)
        if out is not None:
            out.remove_header('Authorization')
            out.remove_header('Cookie')
        return out


def fetch(url: str, *, json_response: bool = False):
    if not safe_url(url, FETCH_HOSTS):
        raise ValueError('Unapproved media request')
    # This code deliberately never reads GITHUB_TOKEN or any other credential.
    request = urllib.request.Request(url, headers={'User-Agent': 'awesome-jev-media/1.0'})
    limit = 1_000_000 if json_response else 16_384
    with urllib.request.build_opener(RestrictedRedirect()).open(request, timeout=12) as response:
        body = response.read(limit + 1)
        mime = response.headers.get('Content-Type', '').split(';')[0].lower()
    if json_response:
        if len(body) > limit:
            raise ValueError('Metadata exceeds size limit')
        return json.loads(body.decode('utf-8'))
    return mime, body[:limit]


def media_kind(mime: str, body: bytes) -> str:
    if mime.startswith('image/') or body.startswith((b'\x89PNG', b'GIF87a', b'GIF89a', b'\xff\xd8\xff')):
        return 'image'
    if mime.startswith('video/') or b'ftyp' in body[:32] or body.startswith(b'\x1aE\xdf\xa3'):
        return 'video'
    return 'unknown'


def x_poster(payload: dict, expected_id: str) -> str | None:
    tweet = payload.get('tweet') or {}
    if str(tweet.get('id')) != expected_id:
        raise ValueError('X metadata does not match the requested post')
    media = tweet.get('media') or {}
    for part in media.get('all', []) + media.get('videos', []) + media.get('photos', []):
        candidate = part.get('thumbnail_url') or (part.get('url') if part.get('type') == 'photo' else None)
        if candidate and safe_url(candidate, {'pbs.twimg.com'}):
            return candidate
    return None


def refresh(data: dict, cache: dict) -> dict:
    validate(data, cache)
    result = json.loads(json.dumps(cache))
    for item in data['items']:
        ident = item['id']
        previous = result.get(ident, {})
        if previous.get('checked') == TODAY:
            continue
        updated = dict(previous)
        try:
            if item['group'] == 'x' and not item.get('image'):
                path = urlsplit(item['watch']).path
                poster = x_poster(fetch('https://api.fxtwitter.com' + path, json_response=True), path.rsplit('/', 1)[-1])
                if poster:
                    updated['image'] = poster
                updated['metadata_status'] = 'public-mirror-metadata' if poster else 'no-poster-returned'
            elif item['group'] == 'youtube':
                url = 'https://www.youtube.com/oembed?' + urlencode({'url': item['watch'], 'format': 'json'})
                response = fetch(url, json_response=True)
                if response.get('type') != 'video' or not isinstance(response.get('title'), str):
                    raise ValueError('Unexpected YouTube metadata')
                updated['title'] = response['title'][:250]
                updated['creator'] = str(response.get('author_name', item['creator']))[:150]
                updated['metadata_status'] = 'youtube-oembed'
            target = item['watch'] if item['group'] == 'videos' else item.get('image') or updated.get('image')
            if target:
                kind = media_kind(*fetch(target))
                expected = 'video' if item['group'] == 'videos' else 'image'
                if kind != expected:
                    raise ValueError('Unexpected media content type')
                updated['media_status'] = 'reachable-' + kind
            else:
                updated['media_status'] = 'link-only-no-poster'
            updated['checked'] = TODAY
            updated.pop('error', None)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            # Preserve last-known image and successful receipts when a platform is down.
            updated['checked'] = TODAY
            updated['error'] = type(exc).__name__
            print('Media check unavailable for ' + ident + ': ' + type(exc).__name__)
        result[ident] = updated
    validate(data, result)
    return result


def card(item: dict, cache: dict) -> str:
    state = cache.get(item['id'], {})
    image = item.get('image') or state.get('image')
    title = item['title']
    creator = state.get('creator') or item['creator']
    content = '<td width="50%" valign="top">\n'
    if image:
        content += '<a href="' + esc(item['watch']) + '"><img src="' + esc(image) + '" alt="' + esc(title + ' — creator preview; click to watch or inspect') + '" width="480" loading="lazy"></a>\n'
    content += '<h4>' + esc(title) + '</h4>\n'
    content += '<p>' + esc(item['caption']) + '</p>\n'
    labels = {'x': '▶ Watch on X', 'youtube': '▶ Watch on YouTube', 'projects': 'Open demo / recording'}
    links = [anchor(labels[item['group']], item['watch'])]
    if item.get('repo'):
        links.append(anchor('Code', item['repo']))
    links.append(anchor('Source', item['source']))
    content += '<p>' + ' · '.join(links) + '</p>\n'
    content += '<p><sub>' + esc(creator) + ' — ' + esc(item['note']) + '</sub></p>\n'
    if not image:
        content += '<p><sub>No reliable preview image was returned. The original watch link is retained.</sub></p>\n'
    return content + '</td>'


def grid(items: list[dict], cache: dict) -> str:
    lines = ['<table>']
    for offset in range(0, len(items), 2):
        lines += ['<tr>'] + [card(item, cache) for item in items[offset:offset+2]] + ['</tr>']
    return '\n'.join(lines + ['</table>'])


def render(data: dict, cache: dict) -> str:
    validate(data, cache)
    lines = ['## Watch Jev in action', '',
        '**Original creator media, linked to the implementation.** Click a preview to watch the source. Animated GIFs play inline; original GitHub video attachments appear as players below. X and YouTube open on their own platforms.', '']
    for group, heading in [('x', '### From X: demos and the original roundup'),
                           ('projects', '### Screenshots, animated demos, and implementation diagrams')]:
        lines += [heading, '', grid([i for i in data['items'] if i['group'] == group], cache), '']
    lines += ['### Full recordings — play inline', '',
        'These are the creators\' original GitHub-hosted uploads, not re-encoded copies. A direct watch link is retained for clients that do not render a player.', '']
    for item in [i for i in data['items'] if i['group'] == 'videos']:
        if cache.get(item['id'], {}).get('error'):
            lines += ['<p><strong>' + esc(item['title']) + '</strong> — the recording could not be verified by the latest public-access check. ' + anchor('View the creator source', item['source']) + '.</p>', '']
            continue
        lines += ['<h4>' + esc(item['title']) + '</h4>', '', '<p>' + esc(item['caption']) + '</p>', '', item['watch'], '',
                  anchor('Open recording', item['watch']) + ' · ' + anchor('Repository', item['repo']) + ' · ' + anchor('Creator source', item['source']), '',
                  '<sub>' + esc(item['creator'] + ' — ' + item['note']) + '</sub>', '']
    lines += ['### Longer walkthroughs on YouTube', '',
        grid([i for i in data['items'] if i['group'] == 'youtube'], cache), '',
        '**Source notes:** media remain hosted by their creators/platforms; this repository does not relicense them. Public X mirror metadata is used only to locate a poster, not to certify a demo. Reachable media is not proof of live inference, security, or benchmark performance. No project was executed for this gallery.', '',
        '[Media sources and link-check receipts](https://github.com/Amal-David/awesome-jev/blob/main/docs/MEDIA.md) · [Suggest a visual demo](https://github.com/Amal-David/awesome-jev/issues/new?template=suggest-resource.yml)', '']
    return '\n'.join(lines)


def replace_block(template: str, gallery: str) -> str:
    if template.count(START) != 1 or template.count(END) != 1 or template.index(START) >= template.index(END):
        raise ValueError('Template needs one ordered media marker pair')
    before, tail = template.split(START)
    _, after = tail.split(END)
    return before + START + '\n\n' + gallery.rstrip() + '\n\n' + END + after


def source_index(data: dict, cache: dict) -> str:
    lines = ['# Media sources and check receipts', '',
        '[Visual README](https://github.com/Amal-David/awesome-jev#readme) · [Editorial source](../data/media.json) · [Machine-readable receipts](../data/media_cache.json)', '',
        'Checked means a bounded public metadata/media request succeeded, not that the video was watched or its claims independently reproduced. Preview files are embedded from upstream, never copied into this repository. GitHub images are pinned where a known source revision was available; other platform assets may change or disappear.', '']
    for item in data['items']:
        state = cache.get(item['id'], {})
        image = item.get('image') or state.get('image')
        lines += ['<h2>' + esc(item['title']) + '</h2>', '',
                  anchor('Original / watch', item['watch']) + ' · ' + anchor('Source context', item['source']), '',
                  '**Creator:** ' + esc(state.get('creator') or item['creator']), '',
                  '**Presentation:** ' + esc(item['note']), '']
        if image:
            lines += [anchor('Embedded preview source', image), '']
        if state:
            lines += ['**Last check:** ' + esc(state.get('checked', 'not checked')) + '; ' + esc(state.get('media_status', 'media unresolved')) + '; ' + esc(state.get('metadata_status', 'author-source reference')) + '.', '']
            if state.get('error'):
                lines += ['**Latest attempt:** ' + esc(state['error']) + '. The original source link and any previous preview are preserved.', '']
        else:
            lines += ['**Link check:** pending. Source reference reviewed; playback was not tested.', '']
    lines += ['## Maintenance', '',
        'Edit `data/media.json` for editorial changes. `python3 scripts/curate_media.py --refresh` performs bounded, unauthenticated requests to approved public hosts; it reads no API keys. `python3 scripts/curate_media.py` renders offline. Run it before `curate_x.py`. `--check` validates generated output without network access. Metadata checks rotate daily; the four-hour workflow preserves the gallery and last-known previews.', '',
        'Discovery leads included the attributed media index in [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill/blob/main/docs/media/README.md) and [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev). Each GitHub visual above is linked back to its original project README. YouTube metadata is checked directly using its public oEmbed endpoint when available. No third-party code, skill, or installation command is executed.', '']
    return '\n'.join(lines)


def write(path: Path, content: str, check: bool = False) -> None:
    if check:
        if not path.exists() or path.read_text(encoding='utf-8') != content:
            raise ValueError('Generated media output is stale: ' + path.name)
    elif not path.exists() or path.read_text(encoding='utf-8') != content:
        path.parent.mkdir(parents=True, exist_ok=True)
        temp = path.with_suffix(path.suffix + '.tmp')
        temp.write_text(content, encoding='utf-8')
        temp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--refresh', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/media.json').read_text())
    cache = json.loads((ROOT / 'data/media_cache.json').read_text())
    validate(data, cache)
    if args.refresh:
        cache = refresh(data, cache)
        write(ROOT / 'data/media_cache.json', json.dumps(cache, indent=2, ensure_ascii=False, sort_keys=True) + '\n')
    template = (ROOT / 'templates/README.md').read_text(encoding='utf-8')
    gallery = render(data, cache)
    write(ROOT / 'templates/README.md', replace_block(template, gallery), args.check)
    write(ROOT / 'docs/MEDIA.md', source_index(data, cache), args.check)
    players = sum(line.startswith('https://github.com/user-attachments/assets/') for line in gallery.splitlines())
    print(f'Media gallery validated: {len(data["items"])} source records, {gallery.count("<img ")} previews, {players} inline video references.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
