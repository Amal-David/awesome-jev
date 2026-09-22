"""Offline checks for computer-use coverage and the driver/model boundary."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('cua_coverage_core', ROOT / 'scripts/curate.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


class CuaCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = json.loads((ROOT / 'data/curated.json').read_text())
        cls.entries = {e.get('repo') or e.get('url'): e for e in cls.seed}
        cls.guide = (ROOT / 'docs/CUA.md').read_text()

    def test_previously_missing_resources_are_in_editorial_seed(self):
        for target in ('trycua/cua', 'Eronmmer/jev-cua',
                       'stoopid-computers/jev-bot', 'browser-use/browser-harness',
                       'https://huggingface.co/cua-ai/cua-s1-forms'):
            with self.subTest(target=target):
                self.assertIn(target, self.entries)
                self.assertIn('reviewed', self.entries[target])
                self.assertIn('evidence', self.entries[target])

    def test_six_indexed_resources_have_reviewed_source_entries(self):
        for repo in ('awlevin/typesafe-computer-use', 'moritzkremb/jev-voice-browser',
                     'zurfyx/jev-browser-skill', 'jkudish/jev-browser',
                     'wy-coliney/jev-browser-use', 'vinnylarouge/jevlike'):
            self.assertIn(repo, self.entries)
            self.assertIn('evidence', self.entries[repo])

    def test_supporting_driver_is_not_claimed_as_a_jev_model(self):
        entry = self.entries['browser-use/browser-harness']
        self.assertEqual(entry['kind'], 'adjacent-infrastructure')
        self.assertIn('not a Jev model', entry['notes'])
        self.assertIn('Supporting drivers and runtimes', self.guide)
        self.assertIn('browser-use/jev-ultrafast/blob/main/pyproject.toml', self.guide)

    def test_monorepo_dedup_keeps_the_recipe_deep_link(self):
        matches = [e for e in self.seed if e.get('repo', '').lower() == 'trycua/cua']
        self.assertEqual(len(matches), 1)
        self.assertIn('/libs/cua-driver/examples/jev-use/', matches[0]['evidence'])
        self.assertIn('outside Driver', self.guide)

    def test_optional_jev_and_independent_models_remain_distinct(self):
        for repo in ('Eronmmer/jev-cua', 'stoopid-computers/jev-bot'):
            self.assertEqual(self.entries[repo]['kind'], 'optional-integration')
            self.assertIn('TypeSafe', self.entries[repo]['notes'])
        for target in ('https://huggingface.co/cua-ai/cua-s1-forms', 'vinnylarouge/jevlike'):
            self.assertEqual(self.entries[target]['kind'], 'independent-reproduction')
            self.assertEqual(self.entries[target]['category'], 'research')
        self.assertIn('local runtime is not a local Jev model', self.guide)
        self.assertIn('https://huggingface.co/datasets/cua-ai/cua-s1-forms', self.guide)
        self.assertIn('source-only research profile', self.guide)

    def test_navigation_preserves_quickstart_and_existing_media(self):
        template = (ROOT / 'templates/README.md').read_text()
        self.assertIn('[CUA & drivers](#computer-use-and-drivers)', template)
        self.assertIn('## Computer use and drivers', template)
        self.assertIn('/docs/CUA.md', template)
        self.assertIn('## OpenRouter community winners', template)
        self.assertIn('<!-- MEDIA_GALLERY:START -->', template)
        self.assertLess(template.index('## 20-second quick-start'),
                        template.index('## Computer use and drivers'))

    def test_seed_normalizes_without_duplicates(self):
        records = [core.normalize(e, e['evidence'], 'primary-source-reviewed') for e in self.seed]
        core.validate(records)
        self.assertEqual(len({core.key(e) for e in records}), len(records))

    def test_audit_limits_and_dependency_instructions_are_explicit(self):
        self.assertIn('not a claim to have enumerated every CUA project', self.guide)
        self.assertIn('not promoted or security-reviewed by this pass', self.guide)
        self.assertIn('Computer-use dependency coverage', (ROOT / 'AGENTS.md').read_text())


if __name__ == '__main__':
    unittest.main()
