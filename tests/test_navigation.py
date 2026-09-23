import copy
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('directory_build', ROOT / 'scripts/build.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def example(**changes):
    item = {'name': 'Fixture', 'repo': 'owner/demo', 'url': 'https://github.com/owner/demo',
            'description': 'A browser decision', 'category': 'browser', 'evidence_level': b.LEVELS[0],
            'sources': ['https://github.com/owner/demo'], 'reviewed': '2026-09-18'}
    return dict(item, **changes)


def key(item):
    return 'repo:' + item['repo'].lower()


class NavigationTests(unittest.TestCase):
    def test_summary_leads_with_reviewed_not_total(self):
        stats = b.statistics([example(), example(repo='owner/b', evidence_level=b.LEVELS[1])], {}, {})
        text = b.summary(stats)
        self.assertTrue(text.startswith('**1 reviewed picks**'))
        self.assertNotIn('2 catalog entries', text)
        self.assertIn('Source notes and licenses', text)
        self.assertIn('Auto-discovered', (ROOT / 'templates/README.md').read_text(encoding='utf-8'))

    def test_statistics_distinguish_errors_and_unavailable(self):
        stats = b.statistics([example(repository_status='unavailable', metadata_checked='2026-09-18'),
                              example(repo='owner/b')], {'video': {'error': 'HTTPError'}}, {})
        self.assertEqual(stats['unavailable_repositories'], 1)
        self.assertEqual(stats['checked_repositories'], 1)
        self.assertEqual(stats['media_check_errors'], 1)
        self.assertIsNone(stats['completed_at'])

    def test_offline_statistics_do_not_invent_refresh(self):
        self.assertIsNone(b.statistics([example(metadata_checked='2026-09-18')], {}, {})['completed_at'])

    def test_statistics_preserve_recorded_refresh(self):
        receipt = {'completed_at': '2026-09-18T12:34:56Z'}
        self.assertEqual(b.statistics([example()], {}, receipt)['completed_at'], receipt['completed_at'])

    def test_receipt_rejects_non_utc(self):
        with self.assertRaises(ValueError): b.statistics([], {}, {'completed_at': '2026-09-18T12:00:00'})

    def test_receipt_rejects_unrelated_run_link(self):
        with self.assertRaises(ValueError): b.statistics([], {}, {'run_url': 'https://evil.test/receipt'})

    def test_status_does_not_claim_every_link_is_healthy(self):
        records = [example()]
        out = b.status_page(records, {}, b.statistics(records, {}, {}), set())
        self.assertIn('complete dead-link count is unknown', out)
        self.assertIn('not an all-links health certificate', out)

    def test_status_separates_media_failure_from_dead_link(self):
        cache = {'clip': {'error': 'HTTPError', 'checked': '2026-09-18'}}
        out = b.status_page([], cache, b.statistics([], cache, {}), set())
        self.assertIn('transient failures, not dead links', out)
        self.assertIn('clip', out)

    def test_removed_pick_loses_reviewed_status(self):
        out = b.editorial_snapshot([example()], [], key)
        self.assertEqual(out[0]['evidence_level'], b.LEVELS[1])
        self.assertNotIn('reviewed', out[0])

    def test_current_pick_keeps_reviewed_status(self):
        entry = example()
        self.assertEqual(b.editorial_snapshot([entry], [entry], key), [entry])

    def test_demotion_does_not_mutate_original(self):
        entry = example(); original = copy.deepcopy(entry)
        b.editorial_snapshot([entry], [], key)
        self.assertEqual(entry, original)

    def test_exclusions_empty_valid(self):
        self.assertEqual(b.exclusion_keys({'version': 1, 'entries': []}), set())

    def test_exclusions_require_public_reason(self):
        with self.assertRaises(ValueError): b.exclusion_keys({'version': 1, 'entries': [{'key': 'repo:a/b'}]})

    def test_exclusions_canonical_key(self):
        e = {'key': 'repo:owner/demo', 'reason': 'Moved', 'source': 'https://github.com/owner/demo', 'date': '2026-09-18'}
        self.assertEqual(b.exclusion_keys({'version': 1, 'entries': [e]}), {'repo:owner/demo'})
        e['key'] = 'repo:Owner/Demo'
        with self.assertRaises(ValueError): b.exclusion_keys({'version': 1, 'entries': [e]})

    def test_exclusions_duplicate_rejected(self):
        e = {'key': 'repo:owner/demo', 'reason': 'Moved', 'source': 'https://github.com/owner/demo', 'date': '2026-09-18'}
        with self.assertRaises(ValueError): b.exclusion_keys({'version': 1, 'entries': [e, e]})

    def test_safe_navigation_links(self):
        for value in ('javascript:alert(1)', 'https://a:b@host.test', 'https://host.test/\x00', 'https://host.test/a\\b'):
            self.assertFalse(b.safe_url(value))
            with self.assertRaises(ValueError): b.anchor('link', value)

    def test_json_cannot_break_out_of_script(self):
        value = [{'name': '</script><img src=x onerror=bad>', 'text': '\u2028&'}]
        out = b.script_json(value)
        self.assertNotIn('<', out)
        self.assertNotIn('&', out)
        self.assertEqual(json.loads(out), value)

    def test_nonfinite_viewer_data_rejected(self):
        with self.assertRaises(ValueError): b.script_json({'bad': float('nan')})

    def test_template_requires_exactly_one_marker(self):
        for value in ('none', '<!-- A --><!-- A -->'):
            with self.assertRaises(ValueError): b.replace_once(value, 'A', 'new')
        self.assertEqual(b.replace_once('x<!-- A -->y', 'A', 'n'), 'xny')

    def test_featured_media_has_a_fallback(self):
        self.assertIn('gallery', b.featured({'items': []}, {}))
        data = {'items': [{'id': 'ultrafast', 'watch': 'https://x.com/a/status/123', 'image': 'https://raw.githubusercontent.com/a/b/main/demo.gif', 'repo': 'https://github.com/a/b'}]}
        self.assertNotIn('<img', b.featured(data, {'ultrafast': {'error': 'HTTPError'}}))
        self.assertIn('<img', b.featured(data, {}))

    def test_picks_do_not_include_unreviewed_items(self):
        out = b.picks([example(), example(name='Unreviewed', evidence_level=b.LEVELS[2])])
        self.assertNotIn('Unreviewed', out)
        self.assertIn('All 1 reviewed picks', out)

    def test_viewer_keeps_evidence_and_escapes_source_data(self):
        template = '<script><!-- CATALOG_JSON --></script>'
        out = b.viewer(template, [example(name='</script><img src=x>')])
        self.assertEqual(out.count('</script>'), 1)
        self.assertIn('primary-source-reviewed', out)

    def test_viewer_has_no_unsafe_dom_html_assignment(self):
        text = (ROOT / 'templates/catalog.html').read_text(encoding='utf-8')
        self.assertNotIn('.innerHTML', text)
        self.assertNotIn('fetch(', text)
        self.assertIn('textContent', text)
        self.assertIn('connect-src \'none\'', text)
        self.assertIn('value="primary-source-reviewed"', text)

    def test_readme_hierarchy_and_markers(self):
        text = (ROOT / 'templates/README.md').read_text(encoding='utf-8')
        self.assertLess(text.index('20-second quick-start'), text.index('MEDIA_GALLERY:START'))
        self.assertLess(text.index('## Reviewed picks'), text.index('MEDIA_GALLERY:START'))
        for name in (*b.MARKERS, 'FRESHNESS', 'X_DEMOS'):
            self.assertEqual(text.count('<!-- ' + name + ' -->'), 1)
        self.assertIn('<summary><strong>Safety, licensing, and evidence limits', text)

    def test_sdk_quickstart_with_fake_client_only(self):
        text = (ROOT / 'templates/README.md').read_text(encoding='utf-8')
        code = re.search(r'```python\n(.*?)\n```', text, re.S).group(1)
        calls = []
        class Choice:
            def __init__(self, **kwargs): self.__dict__.update(kwargs)
        class Client:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def system_one(self, **kwargs):
                calls.append(kwargs)
                return type('Response', (), {'choices': {'team': type('Answer', (), {'choice': 'billing'})()}})()
        fake = type('SDK', (), {'Choice': Choice, 'TypeSafeClient': Client})
        with patch.dict('sys.modules', {'typesafe_sdk': fake}), patch('builtins.print') as output:
            exec(compile(code, 'readme_quickstart', 'exec'), {})
        self.assertEqual(len(calls), 1)
        self.assertEqual(set(calls[0]['questions']['team'].criteria), {'billing', 'technical', 'other'})
        output.assert_called_once_with('billing')

    def test_write_check_idempotence(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'a.md'
            with self.assertRaises(ValueError): b.write_outputs({path: 'one'}, True)
            self.assertFalse(path.exists())
            b.write_outputs({path: 'one'}); before = path.stat().st_mtime_ns
            b.write_outputs({path: 'one'}); b.write_outputs({path: 'one'}, True)
            self.assertEqual(path.stat().st_mtime_ns, before)
            with self.assertRaises(ValueError): b.write_outputs({path: 'two'}, True)
            self.assertEqual(path.read_text(encoding='utf-8'), 'one')

    def test_check_and_refresh_mutually_exclusive(self):
        with self.assertRaises(ValueError): b.build(check=True, refresh=True)
        with self.assertRaises(ValueError): b.build(check=True, refresh_media=True)

    @unittest.skipUnless((ROOT / 'scripts/curate.py').exists(), 'Repository source modules are required')
    def test_full_offline_build_from_repository_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for directory in ('data', 'templates'):
                shutil.copytree(ROOT / directory, root / directory)
            before = (root / 'data/refresh.json').read_text(encoding='utf-8') if (root / 'data/refresh.json').exists() else None
            b.build(root)
            self.assertEqual((root / 'README.md').read_text(encoding='utf-8'), (root / '.github/README.md').read_text(encoding='utf-8'))
            b.build(root, check=True)
            if before is not None:
                self.assertEqual(json.loads(before), json.loads((root / 'data/refresh.json').read_text(encoding='utf-8')))
            else:
                self.assertEqual(json.loads((root / 'data/refresh.json').read_text(encoding='utf-8')), {})
            self.assertIn('Reviewed Jev picks', (root / 'docs/REVIEWED.md').read_text(encoding='utf-8'))
            self.assertNotIn('<!-- DIRECTORY_STATS -->', (root / 'README.md').read_text(encoding='utf-8'))


if __name__ == '__main__': unittest.main()
