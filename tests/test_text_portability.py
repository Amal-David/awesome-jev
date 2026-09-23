"""UTF-8 repository files must not depend on the host's default text codec."""
import ast
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('portability_build', ROOT / 'scripts/build.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def implicit_text_calls(source):
    missing = []
    for call in ast.walk(ast.parse(source)):
        if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Attribute):
            continue
        method = call.func.attr
        if method not in ('read_text', 'write_text'):
            continue
        positional = 1 if method == 'read_text' else 2
        codec = (call.args[positional - 1] if len(call.args) >= positional else
                 next((k.value for k in call.keywords if k.arg == 'encoding'), None))
        if codec is None or (isinstance(codec, ast.Constant) and codec.value is None):
            missing.append((call.lineno, method))
    return missing


class TextPortabilityTests(unittest.TestCase):
    def test_repository_path_text_io_has_an_explicit_encoding(self):
        for folder in ('scripts', 'tests', 'examples'):
            for path in (ROOT / folder).rglob('*.py'):
                with self.subTest(path=str(path.relative_to(ROOT))):
                    self.assertEqual(implicit_text_calls(path.read_text(encoding='utf-8')), [])

    def test_encoding_guard_detects_missing_arguments(self):
        self.assertEqual(implicit_text_calls('p.read_text()'), [(1, 'read_text')])
        self.assertEqual(implicit_text_calls('p.read_text(encoding=None)'), [(1, 'read_text')])
        self.assertEqual(implicit_text_calls("p.write_text('text')"), [(1, 'write_text')])
        self.assertEqual(implicit_text_calls("p.read_text(encoding='utf-8')"), [])
        self.assertEqual(implicit_text_calls("p.write_text('text', encoding='utf-8')"), [])

    def test_utf8_fixture_reads_and_legacy_codec_negative_control(self):
        for relative in ('templates/catalog.html', 'docs/OPENROUTER_SHOWCASE.md'):
            path = ROOT / relative
            self.assertEqual(path.read_text(encoding='utf-8').splitlines(),
                             path.read_bytes().decode('utf-8').splitlines())
        payload = 'Jev “yes”'.encode('utf-8')
        with self.assertRaises(UnicodeDecodeError):
            payload.decode('cp1252')

    def test_full_offline_build_with_simulated_cp1252_default(self):
        original_open = Path.open
        def cp1252_open(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
            if 'b' not in mode and encoding is None:
                encoding = 'cp1252'
            return original_open(path, mode, buffering, encoding, errors, newline)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            for folder in ('data', 'templates'):
                shutil.copytree(ROOT / folder, target / folder)
            with patch.object(Path, 'open', cp1252_open):
                b.build(target)
                b.build(target, check=True)
                self.assertEqual(
                    (target / 'README.md').read_text(encoding='utf-8'),
                    (target / '.github/README.md').read_text(encoding='utf-8'),
                )

    def test_publisher_tests_report_missing_bash_as_a_skip(self):
        original_which = shutil.which
        def without_bash(name):
            return None if name == 'bash' else original_which(name)
        location = ROOT / 'tests/test_publish.py'
        spec = importlib.util.spec_from_file_location('publisher_without_bash', location)
        module = importlib.util.module_from_spec(spec)
        with patch('shutil.which', side_effect=without_bash):
            spec.loader.exec_module(module)
        self.assertTrue(module.PublishTests.__unittest_skip__)
        self.assertIn('bash', module.PublishTests.__unittest_skip_why__)


if __name__ == '__main__':
    unittest.main()
