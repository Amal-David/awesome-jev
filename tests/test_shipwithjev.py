"""Offline checks for selected Ship with Jev sources, not upstream execution."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ('bartlomein/oko', 'simota/tenbin', 'ttlequals0/MinusPodJev')


class ShipWithJevTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = json.loads((ROOT / 'data/curated.json').read_text(encoding='utf-8'))
        cls.entries = {e.get('repo', '').lower(): e for e in cls.seed if e.get('repo')}

    def test_selected_sources_are_unique_and_pinned_to_the_project(self):
        for repo in PROJECTS:
            with self.subTest(repo=repo):
                matches = [e for e in self.seed if e.get('repo', '').lower() == repo.lower()]
                self.assertEqual(len(matches), 1)
                entry = matches[0]
                prefix = 'https://github.com/' + repo + '/blob/'
                for field in ('evidence', 'code'):
                    self.assertTrue(entry[field].startswith(prefix))
                    self.assertRegex(entry[field][len(prefix):], r'^[0-9a-f]{40}/.+')
                self.assertEqual(entry['license'], 'MIT')
                self.assertIn('reviewed', entry)

    def test_directory_is_attributed_but_not_substituted_for_primary_evidence(self):
        for repo in PROJECTS:
            entry = self.entries[repo.lower()]
            self.assertIn('shipwithjev.com', entry['notes'])
            self.assertNotIn('shipwithjev.com', entry['evidence'])
        sources = (ROOT / 'SOURCES.md').read_text(encoding='utf-8')
        self.assertIn('## Ship with Jev', sources)
        self.assertIn('not bulk imported', sources)

    def test_tenbin_links_the_actual_skill_and_keeps_inference_optional(self):
        entry = self.entries['simota/tenbin']
        self.assertTrue(entry['skill'].endswith('/skills/tenbin/SKILL.md'))
        self.assertEqual(entry['kind'], 'optional-integration')
        self.assertIn('offline', entry['notes'])
        self.assertIn('not a guaranteed', entry['notes'])

    def test_review_notes_distinguish_source_reading_from_execution(self):
        note = (ROOT / 'docs/SHIPWITHJEV_REVIEW.md').read_text(encoding='utf-8')
        self.assertIn('not an audit of every listing', note)
        self.assertIn('No upstream code', note)
        self.assertIn('## Not promoted in this pass', note)
        self.assertIn('existing exclusions', note)


if __name__ == '__main__':
    unittest.main()
