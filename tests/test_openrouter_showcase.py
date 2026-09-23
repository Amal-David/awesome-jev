"""Offline regression tests for the publisher showcase and website-only X entries."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('showcase_x', ROOT / 'scripts/curate_x.py')
x = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x)
POSTS = {
    '2102125765773144286', '2102125782219075865', '2102125798371283444',
    '2102125815031071157', '2102125830185075060',
}
ROUNDUP = 'https://x.com/OpenRouter/status/2102125748723339774'


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


class OpenRouterShowcaseTests(unittest.TestCase):
    def setUp(self):
        self.data = load('data/x_demos.json')
        self.winners = [e for e in self.data['demos'] if e['post'].rsplit('/', 1)[-1] in POSTS]
        self.website = next(e for e in self.winners if e.get('url') == 'https://jevchess.com/')

    def test_five_unique_winner_posts(self):
        x.validate(self.data)
        self.assertEqual(len(self.winners), 5)
        self.assertEqual({x.post_id(e['post']) for e in self.winners}, POSTS)
        self.assertEqual(sum(e['post'] == ROUNDUP for e in self.data['roundups']), 1)

    def test_all_winners_in_reviewed_source(self):
        selected = [e for e in load('data/curated.json') if e.get('post', '').rsplit('/', 1)[-1] in POSTS]
        self.assertEqual(len(selected), 5)
        self.assertTrue(all(e['reviewed'] == '2026-09-22' for e in selected))
        self.assertEqual(sum(bool(e.get('repo')) for e in selected), 3)

    def test_all_winners_have_publisher_stills(self):
        media = [e for e in load('data/media.json')['items'] if e['watch'].rsplit('/', 1)[-1] in POSTS]
        self.assertEqual(len(media), 5)
        for item in media:
            self.assertEqual(item['group'], 'x')
            self.assertTrue(item['image'].startswith('https://pbs.twimg.com/media/'))
            self.assertIn('screenshot published by OpenRouter', item['creator'])
            self.assertIn('screenshot', item['note'].lower())
        self.assertEqual(sum(bool(e.get('repo')) for e in media), 3)

    def test_website_entries_do_not_invent_repositories(self):
        self.assertEqual(sum(bool(e.get('url')) for e in self.winners), 2)
        label, url = x.project_link(self.website)
        self.assertEqual((label, url), ('project', 'https://jevchess.com/'))
        rendered = x.table([self.website])
        self.assertIn('[project](https://jevchess.com/)', rendered)
        self.assertNotIn('[repo]', rendered)

    def test_requires_exactly_one_project_identity(self):
        for edit in ({'repo': 'a/b'}, {'url': None}):
            data = copy.deepcopy(self.data)
            item = next(e for e in data['demos'] if e['id'] == self.website['id'])
            item.update(edit)
            with self.assertRaises(ValueError): x.validate(data)

    def test_website_evidence_must_match_project(self):
        for source in ('https://evil.test/', 'https://jevchess.com.evil.test/',
                       'http://jevchess.com/', 'https://u:p@jevchess.com/',
                       'https://jevchess.com:444/'):
            data = copy.deepcopy(self.data)
            item = next(e for e in data['demos'] if e['id'] == self.website['id'])
            item['source'] = source
            with self.subTest(source=source), self.assertRaises(ValueError): x.validate(data)

    def test_project_path_boundary_is_not_a_prefix_guess(self):
        data = copy.deepcopy(self.data)
        item = next(e for e in data['demos'] if e['id'] == 'vibe-domain')
        item['source'] = 'https://obstudio.org/tools/vibe-domain-spoof/'
        with self.assertRaises(ValueError): x.validate(data)
        item['source'] = item['url'] + '#details'
        x.validate(data)

    def test_repository_identity_stays_strict(self):
        for repo in ('../bad', 'owner/..', 'owner/project/tree/main', 4):
            with self.subTest(repo=repo), self.assertRaises(ValueError):
                x.project_link({'repo': repo})

    def test_mirror_access_is_disclosed(self):
        for item in self.winners:
            self.assertEqual(item['post_status'], 'primary-post-reviewed')
            self.assertIn('public X mirror', item['post_access'])
        _, index = x.render(self.data, x.MARKER)
        self.assertIn('public X mirror', index)
        self.assertIn('not fully retrievable', index)

    def test_access_notes_are_escaped(self):
        data = copy.deepcopy(self.data)
        data['demos'][0]['post_access'] = '<img src=x onerror=bad>'
        _, index = x.render(data, x.MARKER)
        self.assertNotIn('<img', index)
        self.assertIn('&lt;img', index)
        data['demos'][0]['post_access'] = []
        with self.assertRaises(ValueError): x.validate(data)

    def test_showcase_is_linked_without_replacing_navigation(self):
        template = (ROOT / 'templates/README.md').read_text()
        self.assertIn('[OpenRouter winners](#openrouter-community-winners)', template)
        self.assertIn('## OpenRouter community winners', template)
        self.assertLess(template.index('## Reviewed picks'), template.index('## OpenRouter community winners'))
        self.assertIn('<!-- MEDIA_GALLERY:START -->', template)
        doc = (ROOT / 'docs/OPENROUTER_SHOWCASE.md').read_text(encoding='utf-8')
        self.assertIn(ROUNDUP, doc)
        for ident in POSTS:
            self.assertIn('https://x.com/OpenRouter/status/' + ident, doc)

    def test_renderer_is_deterministic_and_preserves_sources(self):
        before = copy.deepcopy(self.data)
        first = x.render(self.data, x.MARKER)
        self.assertEqual(first, x.render(self.data, x.MARKER))
        self.assertEqual(before, self.data)
        for entry in self.winners:
            self.assertIn(entry['post'], first[0])
            self.assertIn(entry['source'], first[1])


if __name__ == '__main__': unittest.main()
