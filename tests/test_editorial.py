"""Keep the README selective, readable, and separate from automated discovery."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('editorial_build', ROOT / 'scripts/build.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def entry(category='browser', **kwargs):
    return dict(name='Example', url='https://example.org', description='Chooses a page element.',
                category=category, evidence_level=b.LEVELS[0], **kwargs)


class EditorialTests(unittest.TestCase):
    def test_each_project_has_its_own_description(self):
        out = b.picks([entry()])
        rows = [line for line in out.splitlines() if line.startswith('- ')]
        self.assertEqual(len(rows), 1)
        self.assertIn('Chooses a page element.', rows[0])
        self.assertIn('### Browser and desktop tools', out)

    def test_supporting_runtime_is_listed_once_in_its_own_group(self):
        out = b.picks([entry('integrations', kind='adjacent-infrastructure')])
        self.assertIn('### Supporting drivers', out)
        self.assertEqual(out.count('https://example.org'), 1)

    def test_descriptions_and_names_are_escaped(self):
        e = entry()
        e.update(name='<script>x</script>', description='<img src=x>')
        out = b.picks([e])
        self.assertNotIn('<script>', out)
        self.assertNotIn('<img src=x>', out)
        self.assertIn('&lt;img', out)

    def test_all_existing_categories_are_covered(self):
        for category in b.module('curate').CATEGORIES:
            with self.subTest(category=category):
                self.assertIn('https://example.org', b.picks([entry(category)]))

    def test_unknown_category_cannot_silently_disappear(self):
        with self.assertRaises(ValueError):
            b.picks([entry('unknown')])

    def test_readme_keeps_the_gallery_without_the_old_slogans(self):
        template = (ROOT / 'templates/README.md').read_text(encoding='utf-8')
        for phrase in ('A compelling clip', 'From an interesting demo to code',
                       'Star to bookmark', '## Why this exists'):
            self.assertNotIn(phrase, template)
        self.assertEqual(template.count('<!-- MEDIA_GALLERY:START -->'), 1)
        self.assertEqual(template.count('<!-- X_DEMOS -->'), 1)
        self.assertIn('Auto-discovered', template)
        self.assertIn('A dedicated classifier may be a better fit', template)

    def test_selected_submissions_have_sources_and_deferred_extension_is_excluded(self):
        seed = json.loads((ROOT / 'data/curated.json').read_text(encoding='utf-8'))
        entries = {e.get('repo'): e for e in seed}
        for repo in ('simonw/llm-typesafe', 'suraj-phanindra/wellposed', 'riesvile/nospace'):
            self.assertIn('evidence', entries[repo])
            self.assertIn('code', entries[repo])
            self.assertIn('reviewed', entries[repo])
        self.assertNotIn('midplane/clean-twitter', entries)
        excluded = b.exclusion_keys(json.loads((ROOT / 'data/exclusions.json').read_text(encoding='utf-8')))
        self.assertIn('repo:midplane/clean-twitter', excluded)

    def test_editorial_pushes_do_not_run_network_discovery(self):
        workflow = (ROOT / '.github/workflows/curate.yml').read_text(encoding='utf-8')
        self.assertIn("cron: '23 */4 * * *'", workflow)
        self.assertIn("if: github.event_name == 'push'\n        run: python3 scripts/build.py", workflow)
        self.assertIn("name: Discover and build the complete directory\n        if: github.event_name != 'push'", workflow)


if __name__ == '__main__':
    unittest.main()
