"""The front page is editorial source, never generated or automatically published."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('readme_checks', ROOT / 'scripts/check_readme.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)
spec = importlib.util.spec_from_file_location('readme_build', ROOT / 'scripts/build.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def fixture(section='Agent Tools'):
    slug = section.lower().replace(' ', '-')
    return (r.HEADING + '\n\nA model for typed decisions.\n\n## Contents\n\n'
            f'- [{section}](#{slug})\n\n## {section}\n\n'
            '- [Example](https://github.com/owner/project) - Chooses an option.\n\n'
            '## Contributing\n\nRead the guidelines.\n\n## Footnotes\n\nSource notes.\n')


def record(**changes):
    return dict(repo='owner/project', evidence='https://github.com/owner/project', **changes)


class ReadmeSourceTests(unittest.TestCase):
    def test_current_front_page_has_source_backing_and_is_not_shadowed(self):
        seed = json.loads((ROOT / 'data/curated.json').read_text(encoding='utf-8'))
        excluded = b.exclusion_keys(json.loads((ROOT / 'data/exclusions.json').read_text(encoding='utf-8')))
        before = (ROOT / 'README.md').read_bytes()
        selected = r.validate_file(ROOT / 'README.md', seed, excluded)
        self.assertTrue(selected)
        self.assertEqual((ROOT / 'README.md').read_bytes(), before)

    def test_valid_markdown_and_subset_selection(self):
        selected = r.validate_text(fixture(), [record(), record(repo='owner/other')], set())
        self.assertEqual(selected, {'https://github.com/owner/project'})

    def test_unknown_project_rejected(self):
        with self.assertRaisesRegex(ValueError, 'no current curated'):
            r.validate_text(fixture(), [], set())

    def test_duplicate_project_rejected(self):
        row = '- [Example](https://github.com/owner/project) - Chooses an option.\n'
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            r.validate_text(fixture().replace(row, row + row), [record()], set())

    def test_excluded_project_rejected(self):
        with self.assertRaisesRegex(ValueError, 'excluded'):
            r.validate_text(fixture(), [record()], {'repo:owner/project'})

    def test_generated_markers_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Generated markers'):
            r.validate_text(fixture() + '<!-- DIRECTORY_STATS -->\n', [record()], set())

    def test_contents_matches_headings_and_excludes_contributing(self):
        text = fixture().replace('- [Agent Tools](#agent-tools)', '- [Contributing](#contributing)')
        with self.assertRaisesRegex(ValueError, 'Contents must match'):
            r.validate_text(text, [record()], set())

    def test_invalid_entry_format_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Capitalized description'):
            r.validate_text(fixture().replace('Chooses an option.', 'chooses an option'), [record()], set())

    def test_independent_model_and_driver_sections_are_distinct(self):
        for kind, section in [('independent-reproduction', 'Independent Models'),
                              ('adjacent-infrastructure', 'Supporting Drivers')]:
            with self.subTest(kind=kind):
                r.validate_text(fixture(section), [record(kind=kind)], set())
                with self.assertRaises(ValueError):
                    r.validate_text(fixture(), [record(kind=kind)], set())

    def test_shadow_readme_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text(fixture(), encoding='utf-8')
            (root / '.github').mkdir()
            (root / '.github/README.md').write_text('shadow', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'shadow'):
                r.validate_file(root / 'README.md', [record()], set())

    def test_writer_refuses_readme_before_writing_any_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for check in (False, True):
                with self.assertRaisesRegex(ValueError, 'editorial source'):
                    b.write_outputs({root / 'other.md': 'one', root / 'README.md': 'bad'}, check)
                self.assertFalse((root / 'other.md').exists())
                self.assertFalse((root / 'README.md').exists())

    def test_legacy_publication_commands_fail_without_modifying_readme(self):
        before = (ROOT / 'README.md').read_bytes()
        for name in ('curate.py', 'curate_media.py', 'curate_x.py'):
            result = subprocess.run([sys.executable, str(ROOT / 'scripts' / name), '--check'],
                                    cwd=ROOT, capture_output=True, text=True, timeout=10)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Legacy publication is disabled', result.stderr)
        self.assertEqual((ROOT / 'README.md').read_bytes(), before)

    def test_project_urls_keep_queries_and_reject_credentials(self):
        self.assertEqual(r.canonical_url('https://Example.org/path/?id=1#part'), 'https://example.org/path?id=1')
        self.assertEqual(r.canonical_url('https://github.com/Owner/Project.git/'), 'https://github.com/owner/project')
        for url in ('http://example.org', 'https://user:secret@example.org', 'javascript:bad', 'https://example.org/a\\b'):
            with self.assertRaises(ValueError):
                r.canonical_url(url)


if __name__ == '__main__':
    unittest.main()
