import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('curate_media', ROOT / 'scripts/curate_media.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MediaTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'data/media.json').read_text())

    def test_seed_valid(self):
        m.validate(self.data, {})

    def test_gallery_has_many_real_media_references(self):
        rendered = m.render(self.data, {})
        self.assertGreaterEqual(rendered.count('<img '), 13)
        self.assertEqual(rendered.count('loading="lazy"'), rendered.count('<img '))
        self.assertNotIn('<iframe', rendered)
        self.assertNotIn('<script', rendered)
        for item in self.data['items']:
            self.assertIn(item['source'].replace('&', '&amp;'), rendered)

    def test_native_players_outside_tables(self):
        rendered = m.render(self.data, {})
        depth = 0
        found = 0
        for line in rendered.splitlines():
            if line == '<table>': depth += 1
            if line == '</table>': depth -= 1
            if line.startswith('https://github.com/user-attachments/assets/'):
                found += 1
                self.assertEqual(depth, 0)
        self.assertEqual(found, 3)
        self.assertEqual(depth, 0)

    def test_deterministic_and_no_data_mutation(self):
        before = copy.deepcopy(self.data)
        self.assertEqual(m.render(self.data, {}), m.render(self.data, {}))
        self.assertEqual(before, self.data)

    def test_duplicate_id_rejected(self):
        self.data['items'][1]['id'] = self.data['items'][0]['id']
        with self.assertRaises(ValueError): m.validate(self.data, {})

    def test_bad_group_rejected(self):
        self.data['items'][0]['group'] = 'script'
        with self.assertRaises(ValueError): m.validate(self.data, {})

    def test_media_hosts_controls_and_credentials(self):
        for value in ('javascript:alert(1)', 'http://pbs.twimg.com/a.png',
                      'https://u:p@pbs.twimg.com/a.png', 'https://pbs.twimg.com:444/a.png',
                      'https://pbs.twimg.com.evil.test/a.png', 'https://127.0.0.1/a.png',
                      'https://pbs.twimg.com/\x00', 'https://pbs.twimg.com/a\\b'):
            self.assertFalse(m.safe_url(value, m.IMAGE_HOSTS))

    def test_cached_poster_cannot_introduce_arbitrary_host(self):
        with self.assertRaises(ValueError):
            m.validate(self.data, {'voice-browser': {'image': 'https://evil.test/track.png'}})

    def test_x_url_must_be_canonical(self):
        self.data['items'][0]['watch'] += '?s=20'
        with self.assertRaises(ValueError): m.validate(self.data, {})

    def test_cache_unknown_id_rejected(self):
        with self.assertRaises(ValueError): m.validate(self.data, {'invented': {}})

    def test_native_video_host_rejected(self):
        self.data['items'][-1]['watch'] = 'https://evil.test/movie.mp4'
        with self.assertRaises(ValueError): m.validate(self.data, {})

    def test_escaping_in_all_gallery_text(self):
        self.data['items'][0]['title'] = '<script>bad</script> "test"'
        self.data['items'][-1]['caption'] = '<img src=x onerror=bad>'
        rendered = m.render(self.data, {})
        self.assertNotIn('<script>', rendered)
        self.assertNotIn('src=x onerror', rendered.split('<p>')[-1])
        self.assertIn('&lt;script&gt;', rendered)
        self.assertIn('&lt;img src=x onerror=bad&gt;', rendered)

    def test_marker_replacement_preserves_editorial_content(self):
        value = 'before\n' + m.START + '\nold\n' + m.END + '\nafter'
        result = m.replace_block(value, 'new')
        self.assertEqual(result, 'before\n' + m.START + '\n\nnew\n\n' + m.END + '\nafter')
        self.assertEqual(m.replace_block(result, 'new'), result)

    def test_bad_marker_pairs_rejected(self):
        for value in ('none', m.END + m.START, m.START + m.END + m.END):
            with self.assertRaises(ValueError): m.replace_block(value, 'gallery')

    def test_mime_and_magic_detection(self):
        self.assertEqual(m.media_kind('image/png', b'x'), 'image')
        self.assertEqual(m.media_kind('application/octet-stream', b'GIF89a'), 'image')
        self.assertEqual(m.media_kind('video/mp4', b'x'), 'video')
        self.assertEqual(m.media_kind('application/octet-stream', b'\x00\x00\x00\x20ftypisom'), 'video')
        self.assertEqual(m.media_kind('text/html', b'not an image'), 'unknown')

    def test_x_metadata_must_match_requested_post(self):
        with self.assertRaises(ValueError): m.x_poster({'tweet': {'id': '321'}}, '123')
        self.assertEqual(m.x_poster({'tweet': {'id': '123', 'media': {'all': [
            {'type': 'video', 'thumbnail_url': 'https://pbs.twimg.com/preview.jpg'}]}}}, '123'),
            'https://pbs.twimg.com/preview.jpg')

    def test_x_metadata_rejects_unapproved_image(self):
        self.assertIsNone(m.x_poster({'tweet': {'id': '123', 'media': {'all': [
            {'type': 'photo', 'url': 'https://evil.test/pixel'}]}}}, '123'))

    def test_preserve_previous_image_on_network_failure(self):
        data = {'version': 1, 'items': [self.data['items'][1]]}
        cache = {'voice-browser': {'image': 'https://pbs.twimg.com/old.jpg'}}
        with patch.object(m, 'fetch', side_effect=OSError('offline')):
            out = m.refresh(data, cache)
        self.assertEqual(out['voice-browser']['image'], cache['voice-browser']['image'])
        self.assertEqual(out['voice-browser']['error'], 'OSError')
        self.assertNotIn('error', cache['voice-browser'])

    def test_same_day_refresh_makes_no_requests(self):
        data = {'version': 1, 'items': [self.data['items'][0]]}
        cache = {'ultrafast': {'checked': m.TODAY}}
        with patch.object(m, 'fetch') as request:
            self.assertEqual(m.refresh(data, cache), cache)
            request.assert_not_called()

    def test_x_poster_is_rendered_when_resolved(self):
        cache = {'voice-browser': {'image': 'https://pbs.twimg.com/example.jpg'}}
        self.assertIn('https://pbs.twimg.com/example.jpg', m.render(self.data, cache))

    def test_redirect_off_host_and_downgrade_rejected(self):
        handler = m.RestrictedRedirect()
        request = urllib.request.Request('https://raw.githubusercontent.com/a/b/main/image.png')
        for url in ('http://raw.githubusercontent.com/a', 'https://evil.test/a', 'https://127.0.0.1/'):
            with self.assertRaises(ValueError): handler.redirect_request(request, None, 302, '', {}, url)

    def test_fetch_rejects_unapproved_hosts_before_network(self):
        with self.assertRaises(ValueError): m.fetch('https://evil.test/image.png')

    def test_atomic_write_check_and_idempotence(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'index.md'
            with self.assertRaises(ValueError): m.write(path, 'test', True)
            m.write(path, 'test')
            before = path.stat().st_mtime_ns
            m.write(path, 'test')
            self.assertEqual(path.stat().st_mtime_ns, before)
            m.write(path, 'test', True)
            with self.assertRaises(ValueError): m.write(path, 'changed', True)


if __name__ == '__main__': unittest.main()
