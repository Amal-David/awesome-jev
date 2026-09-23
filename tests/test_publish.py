"""Offline integration tests using temporary bare repositories; no network or credentials."""
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/publish.sh'
GIT = shutil.which('git')
BASH = shutil.which('bash')


@unittest.skipUnless(GIT and BASH, 'git and bash are required for publisher integration tests')
class PublishTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.remote = self.root / 'origin.git'
        self.work = self.root / 'work'
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', HOME=str(self.root), DEFAULT_BRANCH='main')
        for name in ('GIT_DIR', 'GIT_WORK_TREE', 'GITHUB_STEP_SUMMARY'):
            self.env.pop(name, None)
        self.run_git('init', '--bare', '--initial-branch=main', str(self.remote), cwd=self.root)
        self.run_git('clone', str(self.remote), str(self.work), cwd=self.root)
        self.run_git('config', 'user.name', 'Test')
        self.run_git('config', 'user.email', 'test@example.invalid')
        for path in ('README.md', 'data/catalog.json', 'docs/CATALOG.md', 'data/discoveries.json'):
            target = self.work / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('initial\n', encoding='utf-8')
        self.run_git('add', '.')
        self.run_git('commit', '-m', 'initial')
        self.run_git('push', 'origin', 'main')

    def run_git(self, *args, cwd=None):
        return subprocess.run([GIT, *args], cwd=cwd or self.work, env=self.env, check=True, capture_output=True, text=True).stdout.strip()

    def publish(self, *, env=None):
        return subprocess.run([BASH, str(SCRIPT)], cwd=self.work, env=env or self.env, capture_output=True, text=True, timeout=20)

    def change(self):
        (self.work / 'README.md').write_text('updated catalog\n', encoding='utf-8')

    def install_wrapper(self, body):
        directory = self.root / 'bin'
        directory.mkdir()
        wrapper = directory / 'git'
        wrapper.write_text('#!/usr/bin/env bash\nset -e\n' + body + '\nexec ' + shlex.quote(GIT) + ' "$@"\n', encoding='utf-8')
        wrapper.chmod(0o755)
        return dict(self.env, PATH=str(directory) + os.pathsep + self.env.get('PATH', ''))

    def test_publish_and_noop(self):
        self.change()
        first = self.publish()
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        local = self.run_git('rev-parse', 'HEAD')
        self.assertEqual(local, self.run_git('rev-parse', 'main', cwd=self.remote))
        second = self.publish()
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertIn('No directory changes', second.stdout)
        self.assertEqual(local, self.run_git('rev-parse', 'HEAD'))

    def test_successful_push_with_false_transport_error(self):
        self.change()
        env = self.install_wrapper('if [[ "$1" == push ]]; then\n  ' + shlex.quote(GIT) + ' "$@"\n  exit 1\nfi')
        result = self.publish(env=env)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('verified directory update', result.stdout)
        self.assertEqual(self.run_git('rev-parse', 'HEAD'), self.run_git('rev-parse', 'main', cwd=self.remote))

    def test_true_push_failure_not_hidden(self):
        self.change()
        before = self.run_git('rev-parse', 'main', cwd=self.remote)
        env = self.install_wrapper('if [[ "$1" == push ]]; then exit 1; fi')
        result = self.publish(env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('failed after three', result.stdout)
        self.assertEqual(before, self.run_git('rev-parse', 'main', cwd=self.remote))

    def test_concurrent_nonconflicting_commit_preserved(self):
        other = self.root / 'other'
        self.run_git('clone', str(self.remote), str(other), cwd=self.root)
        self.run_git('config', 'user.name', 'Other', cwd=other)
        self.run_git('config', 'user.email', 'other@example.invalid', cwd=other)
        (other / 'manual-note.txt').write_text('preserve this\n', encoding='utf-8')
        self.run_git('add', '.', cwd=other)
        self.run_git('commit', '-m', 'concurrent manual contribution', cwd=other)
        concurrent = self.run_git('rev-parse', 'HEAD', cwd=other)
        self.run_git('push', 'origin', 'main', cwd=other)
        self.change()
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.run_git('merge-base', '--is-ancestor', concurrent, 'main', cwd=self.remote)
        self.assertEqual(self.run_git('show', 'main:manual-note.txt', cwd=self.remote), 'preserve this')

    def test_unexpected_staged_file_rejected(self):
        self.change()
        (self.work / 'private.txt').write_text('not part of the catalog', encoding='utf-8')
        self.run_git('add', 'private.txt')
        before = self.run_git('rev-parse', 'main', cwd=self.remote)
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('unexpected staged file', result.stderr)
        self.assertEqual(before, self.run_git('rev-parse', 'main', cwd=self.remote))


if __name__ == '__main__':
    unittest.main()
