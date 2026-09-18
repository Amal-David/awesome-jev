import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('curate', ROOT / 'scripts/curate.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
spec2 = importlib.util.spec_from_file_location('packs', ROOT / 'examples/question_packs.py')
p = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(p)


def entry(repo='owner/project', **overrides):
    raw = dict(repo=repo, name='Demo', description='Typed Jev example', category='demos', **overrides)
    return c.normalize(raw, 'https://github.com/owner/project', 'community-indexed')


class CatalogTests(unittest.TestCase):
    def test_repo_canonicalization(self):
        self.assertEqual(c.key(entry('OWNER/Project')), c.key(entry('owner/project.git')))
    def test_bad_repo(self):
        for value in ('../bad', 'owner/name/tree/main', 'bad', 'owner/..'):
            with self.subTest(value=value), self.assertRaises(ValueError): c.repo_name(value)
    def test_safe_urls(self):
        for value in ('javascript:alert(1)', 'https://user:pass@host.test', 'https://bad url', None):
            self.assertFalse(c.valid_url(value))
    def test_root_urls_deduplicate(self):
        self.assertEqual(c.key({'url':'https://example.com/'}), c.key({'url':'https://EXAMPLE.com'}))
    def test_preserve_meaningful_query(self):
        self.assertNotEqual(c.key({'url':'https://example.com/?id=1'}), c.key({'url':'https://example.com/?id=2'}))
    def test_bad_auxiliary_link_dropped(self):
        self.assertNotIn('demo', entry(site='javascript:alert(1)'))
    def test_merge_preserves_review_and_metadata(self):
        old = entry(); old['stars'] = 10
        reviewed = entry(); reviewed.update(description='Reviewed', evidence_level='primary-source-reviewed', sources=['https://primary.test'])
        out = c.merge([old], [entry()], [reviewed])
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]['description'], 'Reviewed')
        self.assertEqual(out[0]['stars'], 10)
        self.assertEqual(out[0]['sources'][0], 'https://primary.test')
        self.assertEqual(out, c.merge(out, [], [reviewed]))
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError): c.validate([entry(), entry()])
    def test_missing_sources(self):
        e = entry(); e['sources'] = []
        with self.assertRaises(ValueError): c.validate([e])
    def test_unknown_evidence(self):
        e = entry(); e['evidence_level'] = 'trust-me'
        with self.assertRaises(ValueError): c.validate([e])
    def test_markdown_escaping(self):
        rendered = c.escaped('<script>\n[bad]|ok')
        self.assertNotIn('<script>', rendered)
        self.assertNotIn('\n', rendered)
        self.assertIn('\\|', rendered)
        self.assertIn('\\[', rendered)
    def test_link_parentheses_escaped(self):
        self.assertIn('%28', c.link('test', 'https://example.test/a(b)'))
    def test_relevance_requires_both_concepts(self):
        self.assertTrue(c.relevant('Jev via TypeSafe'))
        self.assertTrue(c.relevant('An independent Jev-like System One reproduction'))
        self.assertFalse(c.relevant('Jev is my username'))
        self.assertFalse(c.relevant('Typesafe Scala types'))
    def test_write_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'a.json'; c.write(path, '{}\n'); before = path.stat().st_mtime_ns
            c.write(path, '{}\n'); self.assertEqual(before, path.stat().st_mtime_ns)
    def test_metadata_unknown_license(self):
        self.assertEqual(c.metadata({'license':None})['license'], 'not-detected')
    def test_fetch_rejects_unapproved_hosts(self):
        with self.assertRaises(ValueError): c.fetch('https://example.com')
        with self.assertRaises(ValueError): c.fetch('http://api.github.com')
    def test_refresh_never_erases_on_failure(self):
        with patch.object(c, 'fetch', side_effect=ValueError('offline')), patch.object(c, 'discover', return_value=([], [], 1)):
            out, _ = c.refresh([entry()], [], [])
            self.assertEqual(out[0]['repo'], 'owner/project')
    def test_total_discovery_failure_not_success(self):
        with patch.object(c, 'fetch', side_effect=ValueError('offline')), patch.object(c, 'discover', return_value=([], [], 0)):
            with self.assertRaises(RuntimeError): c.refresh([entry()], [], [])
    def test_seed_valid_and_render_deterministic(self):
        seed = c.load(ROOT / 'data/curated.json', [])
        entries = [c.normalize(e, e['evidence'], 'primary-source-reviewed') for e in seed]
        c.validate(entries)
        records = c.merge([], [], entries)
        self.assertEqual(c.render(records), c.render(records))
        self.assertIn('primary-source-reviewed', c.render(records)[0])


class ExampleTests(unittest.TestCase):
    def test_three_primitives(self):
        body = p.ticket_questions('Please fix my bill')
        self.assertEqual({q['type'] for q in body['questions'].values()}, {'choice','noul','score'})
        self.assertEqual(body['model'], 'jev-latest')
    def test_empty_ticket_rejected(self):
        with self.assertRaises(ValueError): p.ticket_questions(' ')
    def test_action_requires_human_fallback(self):
        with self.assertRaises(ValueError): p.bounded_action({}, {'a':'A','b':'B'})
    def test_action_request(self):
        self.assertIn('ask_human', p.bounded_action({}, {'continue':'Continue','ask_human':'Ask a person'})['questions']['next_action']['criteria'])
    def test_strong_choice(self):
        self.assertEqual(p.accept_choice('a', {'a':.95,'b':.05}, {'a','b'}), 'a')
    def test_ambiguous_choice(self):
        self.assertEqual(p.accept_choice('a', {'a':.55,'b':.45}, {'a','b'}), 'ask_human')
    def test_stale_choice(self):
        self.assertEqual(p.accept_choice('a', {'a':.95,'b':.05}, {'a','b'}, age_seconds=8), 'ask_human')
    def test_nonfinite_response(self):
        self.assertEqual(p.accept_choice('a', {'a':float('nan'),'b':0}, {'a','b'}), 'ask_human')
    def test_bad_probability_sum(self):
        self.assertEqual(p.accept_choice('a', {'a':.95,'b':.4}, {'a','b'}), 'ask_human')
    def test_wrong_action_set(self):
        self.assertEqual(p.accept_choice('a', {'a':.95,'x':.05}, {'a','b'}), 'ask_human')
    def test_bad_policy(self):
        with self.assertRaises(ValueError): p.accept_choice('a', {'a':1,'b':0}, {'a','b'}, min_probability=2)


if __name__ == '__main__': unittest.main()
