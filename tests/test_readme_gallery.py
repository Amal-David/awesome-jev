"""Offline checks for the manual README gallery; no fetching or demo execution."""
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


class ReadmeGalleryTests(unittest.TestCase):
    def setUp(self):
        self.readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.gallery = self.readme.split('\n## Demos\n', 1)[1].split('\n## ', 1)[0]
        self.media = {item['id']: item for item in load_json('data/media.json')['items']}
        self.curated = {item['repo'].lower() for item in load_json('data/curated.json') if item.get('repo')}
        self.excluded = {item['key'] for item in load_json('data/exclusions.json')['entries']}
        self.cards = list(re.finditer(r'<!-- demo:([a-z0-9-]+) -->\n(.*?)(?=\n<!-- demo:|\Z)',
                                      self.gallery, re.S))

    def test_gallery_is_visible_early_and_linked_from_contents(self):
        self.assertIn('- [Demos](#demos)', self.readme)
        self.assertLess(self.readme.index('\n## Demos\n'),
                        self.readme.index('\n## SDKs and Skills\n'))
        self.assertNotIn('<details>', self.gallery)
        self.assertNotIn('<iframe', self.gallery.lower())
        self.assertGreaterEqual(len(self.cards), 3)

    def test_highlights_have_registered_sources_and_reviewed_projects(self):
        ids = [card.group(1) for card in self.cards]
        self.assertEqual(len(ids), len(set(ids)), 'A gallery item appears twice')
        for card in self.cards:
            item_id, body = card.groups()
            with self.subTest(item=item_id):
                self.assertIn(item_id, self.media)
                item = self.media[item_id]
                self.assertIn(item['source'], body)
                self.assertIn(item['watch'], body)
                self.assertIn(item['creator'], body)
                repo_url = urlsplit(item['repo'])
                self.assertEqual(repo_url.hostname, 'github.com')
                repo = '/'.join(repo_url.path.strip('/').split('/')[:2]).lower()
                self.assertIn(repo, self.curated)
                self.assertNotIn('repo:' + repo, self.excluded)

    def test_image_links_reuse_editorial_assets_and_have_explanatory_alt_text(self):
        for card in self.cards:
            item_id, body = card.groups()
            item = self.media[item_id]
            images = re.findall(r'\[!\[([^\]]+)\]\((https://[^\s)]+)\)\]\((https://[^\s)]+)\)', body)
            for alt, image, watch in images:
                with self.subTest(item=item_id):
                    self.assertEqual(watch, item['watch'])
                    self.assertGreater(len(alt), 20)
                    self.assertIn(urlsplit(image).hostname,
                                  {'raw.githubusercontent.com', 'pbs.twimg.com', 'github.com', 'i.ytimg.com'})
                    if item.get('image'):
                        self.assertEqual(image, item['image'])
                    else:
                        # Cached X posters can be refreshed independently of this editorial file.
                        self.assertEqual(urlsplit(image).hostname, 'pbs.twimg.com')
                        self.assertIn('still preview', alt.lower())

    def test_native_videos_are_standalone_and_stills_are_not_claimed_as_video(self):
        native = []
        for card in self.cards:
            item_id, body = card.groups()
            item = self.media[item_id]
            if item['group'] == 'videos':
                self.assertIn('\n' + item['watch'] + '\n', body)
                self.assertTrue(item['watch'].startswith('https://github.com/user-attachments/assets/'))
                native.append(item_id)
        self.assertTrue(native, 'Keep an actual creator video, not only screenshot links')
        self.assertIn('not independent benchmarks', self.gallery)
        if '<!-- demo:or-tisco -->' in self.gallery:
            self.assertIn('This is a screenshot, not a video', self.gallery)

    def test_full_gallery_and_ranking_limits_remain_available(self):
        self.assertIn('docs/DIRECTORY.md#watch-jev-in-action', self.gallery)
        self.assertIn('docs/README_GALLERY.md', self.readme)
        notes = (ROOT / 'docs/README_GALLERY.md').read_text(encoding='utf-8')
        self.assertIn('not daily growth, X video views', notes)
        self.assertIn('not a new comparative benchmark', notes)
        self.assertFalse((ROOT / '.github/README.md').exists())


if __name__ == '__main__':
    unittest.main()
