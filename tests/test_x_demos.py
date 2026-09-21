import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('curate_x', ROOT / 'scripts/curate_x.py')
x = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x)


class XDemoTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'data/x_demos.json').read_text(encoding='utf-8'))
        self.template = (ROOT / 'templates/README.md').read_text(encoding='utf-8')

    def test_seed_is_valid(self):
        x.validate(self.data)

    def test_canonical_post(self):
        self.assertEqual(x.post_id('https://x.com/example/status/123'), '123')

    def test_invalid_posts(self):
        for value in ('http://x.com/a/status/1', 'https://twitter.com/a/status/1',
                      'https://x.com/a/status/1?s=20', 'https://x.com/a/status/1#x',
                      'https://x.com/a/status/not-a-number', 'https://x.com.evil.test/a/status/1',
                      'https://u:p@x.com/a/status/1', 'https://x.com:444/a/status/1'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                x.post_id(value)

    def test_safe_url_rejects_credentials_and_controls(self):
        for value in (None, 'javascript:alert(1)', 'https://user:pass@host.test',
                      'https://host.test/\x00', 'https://host.test/a\\b', 'https://host.test:bad'):
            self.assertFalse(x.safe_url(value))

    def test_duplicate_demo_id(self):
        self.data['demos'][1]['id'] = self.data['demos'][0]['id']
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_duplicate_post_even_with_different_author(self):
        a = self.data['demos'][0]['post'].rsplit('/', 1)[-1]
        self.data['demos'][1]['post'] = 'https://x.com/another/status/' + a
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_roundup_cannot_duplicate_demo(self):
        self.data['roundups'][0]['post'] = self.data['demos'][0]['post']
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_evidence_must_match_repo(self):
        self.data['demos'][0]['source'] = 'https://github.com/unrelated/repo/blob/main/README.md'
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_unknown_status(self):
        self.data['demos'][0]['post_status'] = 'fully-secure'
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_missing_field(self):
        del self.data['demos'][0]['notes']
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_future_date(self):
        self.data['demos'][0]['reviewed'] = '2999-01-01'
        with self.assertRaises(ValueError):
            x.validate(self.data)

    def test_html_and_markdown_are_escaped(self):
        value = x.text('<img src=x>\n[click](evil)|`code`')
        self.assertNotIn('<img', value)
        self.assertNotIn('\n', value)
        self.assertIn('\\|', value)
        self.assertIn('\\[', value)
        self.assertIn('%28', x.link('source', 'https://example.test/a(b)'))

    def test_template_needs_one_marker(self):
        for template in ('none', x.MARKER + x.MARKER):
            with self.assertRaises(ValueError):
                x.render(self.data, template)

    def test_render_is_deterministic_without_mutating_data(self):
        before = copy.deepcopy(self.data)
        a = x.render(self.data, self.template)
        self.assertEqual(a, x.render(self.data, self.template))
        self.assertEqual(before, self.data)
        self.assertIn('Curated X demos', a[0])
        self.assertIn('not fully retrievable', a[1])
        for item in self.data['demos']:
            self.assertIn(item['post'], a[0])
            self.assertIn(item['source'], a[1])

    def test_build_check_and_idempotence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data').mkdir()
            (root / 'templates').mkdir()
            (root / 'data/x_demos.json').write_text(json.dumps(self.data), encoding='utf-8')
            (root / 'templates/README.md').write_text(self.template, encoding='utf-8')
            with self.assertRaises(ValueError):
                x.build(root, check=True)
            x.build(root)
            target = root / '.github/README.md'
            before = target.stat().st_mtime_ns
            x.build(root)
            self.assertEqual(before, target.stat().st_mtime_ns)
            x.build(root, check=True)
            target.write_text('stale', encoding='utf-8')
            with self.assertRaises(ValueError):
                x.build(root, check=True)


if __name__ == '__main__':
    unittest.main()
