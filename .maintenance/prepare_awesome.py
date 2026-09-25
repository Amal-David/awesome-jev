"""One-time owner-authorized source migration; no project execution or network."""
from pathlib import Path
import hashlib

ROOT = Path.cwd()

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')

def replace(path, old, new, count=1):
    text = read(path)
    if text.count(old) != count:
        raise ValueError(f'{path}: expected {count} exact matches for {old!r}, found {text.count(old)}')
    write(path, text.replace(old, new))

EXPECTED = {
    'README.md': '464dbba0ba8c1ec754a98ffdec29163592b4af74',
    '.github/README.md': '464dbba0ba8c1ec754a98ffdec29163592b4af74',
    'AGENTS.md': '498de852ba43cc3d5ed181d49dee9abcb9695045',
    'CONTRIBUTING.md': 'd41643e4f2c55e42ec0fcf4f55b5a2003be6079c',
    'LICENSE': '3ecfb3f30d7015e313aa782c15674f70e90e098f',
    'scripts/build.py': '279bb9488690c61710c9287095a1a000281dab54',
    'scripts/curate.py': '4574002fa08a67746da60ca186c0456f8f766de0',
    'scripts/curate_media.py': 'c77859aa99ed3625f9fead7898dc70fcdc0b1f91',
    'scripts/curate_x.py': '9415767ddf923794e6ce0f6f2e41c0c8a2b7ebe7',
    'scripts/publish.sh': 'd4d2f62c2446f4accce66e46349aaf28aeb34e76',
    'tests/test_navigation.py': '842b3b05f30bd5ccbc1fd82a08055047966f1bb9',
    'tests/test_text_portability.py': '36db38048203be464cad3b3bedb5072b326c916f',
    'tests/test_publish.py': '6b2ab835eaba5a0e03e6ab1b854586718c322f58',
    'templates/README.md': '79bcc6c728fa02e6e0989b2cc0ea94e00621dca7',
    'data/curated.json': '10c3f4714424fd382a7ff83b377a3e8b8a627056',
    'data/exclusions.json': 'a66a902c73347db9519b843df0497d029f8fa7ec',
    '.github/workflows/test.yml': '5e0fb26c25aa518132cdb941ec6c0561abff3085',
}
for path, expected in EXPECTED.items():
    payload = (ROOT / path).read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(payload)).encode('ascii') + b'\0' + payload).hexdigest()
    if actual != expected:
        raise ValueError(f'Source changed: {path}')

old_home = read('README.md')
prefix = '# Awesome Jev\n\n'
directory_prefix = '# Jev Project Directory\n\nGenerated supporting directory with source notes, the original demo gallery, and discovery status. [Back to the editorial list](../README.md).\n\n'
assert old_home.startswith(prefix)
write('docs/DIRECTORY.md', old_home.replace(prefix, directory_prefix, 1))
replace('templates/README.md', prefix, directory_prefix)
(ROOT / '.github/README.md').unlink()

write('README.md', '''# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[Jev](https://docs.typesafe.ai) is TypeSafe's System One model for probability-based yes/no judgments, choices, and scores rather than generated text.

Check permissions and data handling before running a project. Source review is not a runtime test or a security audit.

## Contents

- [Getting Started](#getting-started)
- [SDKs and Skills](#sdks-and-skills)
- [Browser and Desktop Tools](#browser-and-desktop-tools)
- [Agent Tools](#agent-tools)
- [Apps and Integrations](#apps-and-integrations)
- [Games and Creative Projects](#games-and-creative-projects)
- [Independent Models](#independent-models)
- [Supporting Drivers](#supporting-drivers)
- [Demos](#demos)

## Getting Started

Start with the [quick-start example](docs/DIRECTORY.md#20-second-quick-start), then build a [typed classifier](docs/START_HERE.md#build-your-first-typed-classifier), use Jev in an [agent](docs/START_HERE.md#use-jev-in-an-agent), or explore a [local alternative](docs/START_HERE.md#explore-a-local-alternative). The [source notes](docs/REVIEWED.md) record setup, privacy, and evidence limits for the selections below.

## SDKs and Skills

- [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - Official JavaScript and TypeScript client.
- [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Official Python client with a support-ticket routing example.
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores log entries to decide which need a closer look.
- [Jevify](https://github.com/altryne/jevify) - Agent skill for finding places to use Jev and planning comparisons with existing code.
- [Official TypeSafe Skill](https://github.com/typesafe-ai/skills) - Request-writing guidance for Noul, Choice, and Score questions.
- [Skillbox](https://github.com/kitze/skillbox) - Self-hosted skill library with optional Jev-based recommendations.
- [Tenbin](https://github.com/simota/tenbin) - MCP server and skill for linting questions, evaluating labeled examples, and choosing thresholds.
- [wellposed](https://github.com/suraj-phanindra/wellposed) - Offline request linter for missing options, broken state references, and question types.
- [jevrs](https://github.com/luizribeiro/jevrs) - Async Rust client with typed answers, derive macros, and native or WASI transports.

## Browser and Desktop Tools

- [Cua Driver + jev-use](https://github.com/trycua/cua) - Python and TypeScript examples where Jev chooses an action, the driver runs it, and code checks the result.
- [Jev Browser](https://github.com/jkudish/jev-browser) - Playwright browser available as an MCP server, CLI, or library.
- [Jev Browser Skill](https://github.com/zurfyx/jev-browser-skill) - Small reference for building and executing browser-action choices.
- [Jev Browser Use](https://github.com/wy-coliney/jev-browser-use) - Skill using an existing Codex browser connection, with Jev choosing clicks and scrolls.
- [Jev Cua](https://github.com/Eronmmer/jev-cua) - Mac automation through Cua Driver, with optional hosted Jev workflow recommendations.
- [Jev Social](https://github.com/socai-io/jev-social) - Bounded social-research loop using Jev choices and socai in the user's Chrome session.
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser-action and element selection with a separate model for text entry.
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) - Voice-controlled Playwright browser that chooses actions from partial speech and page controls.
- [jev-bot](https://github.com/stoopid-computers/jev-bot) - Native Mac controls through a JavaScript MCP session, with optional hosted Jev element selection.
- [TypeSafe Computer Use](https://github.com/awlevin/typesafe-computer-use) - Mac automation using local OCR and accessibility data, with Jev choosing the next action.

## Agent Tools

- [Foreman](https://github.com/thruwire/foreman) - Checks coding-agent progress and decides when intervention may be needed.
- [Jev MCP](https://github.com/jkudish/jev-mcp) - Tools for checking claims against evidence, screening content, and ranking candidates.
- [jev-align](https://github.com/sutro-sh/jev-align) - Improves classifier definitions and scoring rubrics using labels and GEPA-proposed edits.
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that checks local run evidence before judging an unverified completion claim.
- [jev-claude-statusline](https://github.com/kevnk/jev-claude-statusline) - Claude Code hooks that estimate task progress with Jev and cache it for a status-line display.
- [Jev-Mem](https://github.com/libingzheren/Jev-Mem) - Research memory system where Jev organizes graph memories and guides retrieval while a separate model writes answers.
- [jev_search](https://github.com/caio0452/jev_search) - Experimental file search that ranks candidates by keyword and checks passages with Jev.
- [jgrep](https://github.com/kyu1204/jgrep) - Semantic matching over code chunks, diff hunks, and CSV rows, published on npm as jevgrep.
- [Leanest](https://github.com/baronunread/leanest) - Playwright and Vitest test selector with an optional Jev judge and run-tests fallback on uncertainty.
- [Oko](https://github.com/bartlomein/oko) - Code-search CLI and MCP server with local candidate retrieval and optional hosted Jev ranking.
- [patdown](https://github.com/tyler-dot-earth/patdown) - Semantic linter that turns Markdown rules into checks and maps flagged evidence to source lines.
- [SemDecide](https://github.com/sharziki/semdecide) - Unix CLI for predicates, choices, scores, JSONL filtering, and CI-friendly exit codes.
- [TypeSafe MCP](https://github.com/itsmostafa/typesafe-mcp) - Go MCP server for making Jev requests from coding agents.
- [Winnow](https://github.com/GhalebDweikat/winnow) - Claude Code context filter that scores tool-output blocks and keeps hidden text locally recallable.

## Apps and Integrations

- [DocJev](https://github.com/jerryjliu/docjev) - Document classification and packet-boundary detection after local parsing or optional cloud OCR.
- [nospace](https://github.com/riesvile/nospace) - Experimental word-spacing interface where Jev chooses splits and a separate model handles spelling.
- [tisco](https://github.com/cairodavila/tisco) - Video-transcript search with previews of proposed clip moves and renames for approval.
- [Vibe Domain](https://obstudio.org/tools/vibe-domain) - Domain-name ranking with a no-key heuristic mode and an optional hosted Jev mode.
- [Home Assistant Jev](https://github.com/AboveColin/HA-Jev) - Typed decisions for Home Assistant entities and automations.
- [llm-typesafe](https://github.com/simonw/llm-typesafe) - Jev access from the LLM command line or Python, including stdin, templates, and async calls.
- [MinusPodJev](https://github.com/ttlequals0/MinusPodJev) - Podcast ad-detection adapter that scores transcript segments and assembles ad spans in code.
- [neo4jev](https://github.com/jexp/neo4jev) - Neo4j graph exploration using edge choices and goal checks inside a bounded beam search.

## Games and Creative Projects

- [Jev Chess](https://jevchess.com) - Hosted shared chess game with move probabilities; public source code has not been verified.
- [Jev Plays Snake](https://github.com/sorrycc/typesafe-snake) - Snake agent where code finds legal moves and Jev picks a direction.
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - Branch-point action selection for a Pokemon Red agent requiring a lawful local game dump.
- [JevAI for XMage](https://github.com/ShiftSad/mage) - Magic: The Gathering bots using Jev alone or alongside XMage search.
- [JevPilot](https://github.com/standardagents/jevpilot) - Driving simulation with typed steering and speed choices, not a real-world driving system.
- [PROMPT FPS](https://github.com/lukaske/jev-doom-agent) - Action selection in a browser-based Doom engine using Freedoom assets.
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Controller-input selection from emulator state, requiring a lawful local game setup.
- [Jev Music Playground](https://github.com/wustep/jev-playground) - Musical-parameter selection with code-generated notes and MIDI, plus a labeled offline mode.

## Independent Models

These projects are not official TypeSafe Jev weights, and compatible outputs do not establish equivalent quality.

- [AnyJev](https://github.com/nokia-applied-research/AnyJev) - Typed-decision readouts for open models with option-order correction and per-question calibration.
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) - Independent form-filling specialist and dataset, not a general desktop agent.
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Independent option scorer with training code and game examples.
- [OpenJev SGLang](https://github.com/ekzhang/openjev-sglang) - Independent typed-decision server using open models and SGLang.

## Supporting Drivers

- [Browser Harness](https://github.com/browser-use/browser-harness) - Model-neutral CDP connection used by Jev Ultrafast, not a Jev model.

## Demos

The [original creator gallery](docs/DIRECTORY.md#watch-jev-in-action) retains the curated X videos, images, and attribution. Browse the [X index](docs/X_DEMOS.md), [OpenRouter roundup](docs/OPENROUTER_SHOWCASE.md), or [computer-use comparison](docs/CUA.md) for implementation links and limitations.

## Contributing

Suggest a project with a concrete Jev role, implementation evidence, and honest limitations. Read the [contribution guide](CONTRIBUTING.md) and [selection policy](docs/CURATION.md) first.

## Footnotes

The larger [discovery catalog](docs/CATALOG.md), [local viewer](docs/BROWSE.md), and [refresh history](docs/STATUS.md) are separate from this editorial file. Discovery, research, and drafting have used AI assistance; this project does not claim an exclusively human-authored history or admission to the canonical Awesome index. See [submission status](docs/AWESOME_SUBMISSION.md), [sources and credits](SOURCES.md), [reuse terms](LICENSING.md), and the [security policy](SECURITY.md).
''')

replace('scripts/build.py',
        '    # Both README locations intentionally match; GitHub prefers .github/README.md.\n',
        '    # README.md is editorial source. Only the supporting directory is rendered.\n')
replace('scripts/build.py',
        "        root / 'README.md': home, root / '.github/README.md': home,",
        "        root / 'docs/DIRECTORY.md': home,")
replace('scripts/build.py', 'both READMEs and the local viewer.', 'the supporting directory and the local viewer.')
replace('scripts/build.py', 'both READMEs match.', 'editorial README left untouched.')
replace('scripts/build.py', 'An offline README rebuild,', 'An offline directory rebuild,')
replace('scripts/build.py',
        '    # All render/validation happens before the first write. --check is strictly read-only.\n',
        "    # All render/validation happens before the first write. --check is strictly read-only.\n    if any(path.name.lower() == 'readme.md' for path in outputs):\n        raise ValueError('README.md is editorial source, not a generated output')\n")
replace('scripts/build.py',
        "    old = editorial_snapshot(load(root / 'data/catalog.json', []), curated, core.key)\n",
        "    module('check_readme').validate_file(root / 'README.md', seed, excluded)\n    old = editorial_snapshot(load(root / 'data/catalog.json', []), curated, core.key)\n")
replace('docs/MEDIA.md', 'both READMEs and the local viewer.', 'the supporting directory and the local viewer.')
replace('docs/STATUS.md', 'An offline README rebuild,', 'An offline directory rebuild,')

for name in ('curate.py', 'curate_x.py', 'curate_media.py'):
    path = 'scripts/' + name
    text = read(path)
    marker = "\nif __name__ == '__main__':"
    assert text.count(marker) == 1, path
    write(path, text.split(marker)[0] + marker + "\n    raise SystemExit('Legacy publication is disabled; use python3 scripts/build.py instead.')\n")

replace('scripts/publish.sh', 'git add -- README.md data/catalog.json docs/CATALOG.md data/discoveries.json',
        'git add -- docs/DIRECTORY.md data/catalog.json docs/CATALOG.md data/discoveries.json')
replace('scripts/publish.sh', 'for path in .github/README.md docs/X_DEMOS.md', 'for path in docs/X_DEMOS.md')
replace('scripts/publish.sh', 'README.md|data/catalog.json|docs/CATALOG.md|data/discoveries.json|.github/README.md|',
        'docs/DIRECTORY.md|data/catalog.json|docs/CATALOG.md|data/discoveries.json|')

replace('tests/test_readme_source.py', "return dict(repo='owner/project', evidence='https://github.com/owner/project', **changes)",
        "return {'repo': 'owner/project', 'evidence': 'https://github.com/owner/project', **changes}")
replace('tests/test_navigation.py',
        "            before = (root / 'data/refresh.json').read_text(encoding='utf-8') if (root / 'data/refresh.json').exists() else None\n",
        "            shutil.copy2(ROOT / 'README.md', root / 'README.md')\n            editorial_before = (root / 'README.md').read_bytes()\n            before = (root / 'data/refresh.json').read_text(encoding='utf-8') if (root / 'data/refresh.json').exists() else None\n")
replace('tests/test_navigation.py',
        "            self.assertEqual((root / 'README.md').read_text(encoding='utf-8'), (root / '.github/README.md').read_text(encoding='utf-8'))",
        "            self.assertEqual((root / 'README.md').read_bytes(), editorial_before)\n            self.assertFalse((root / '.github/README.md').exists())\n            self.assertTrue((root / 'docs/DIRECTORY.md').is_file())")
replace('tests/test_navigation.py',
        "            self.assertNotIn('<!-- DIRECTORY_STATS -->', (root / 'README.md').read_text(encoding='utf-8'))",
        "            self.assertNotIn('<!-- DIRECTORY_STATS -->', (root / 'docs/DIRECTORY.md').read_text(encoding='utf-8'))")
replace('tests/test_text_portability.py',
        "            with patch.object(Path, 'open', cp1252_open):\n",
        "            shutil.copy2(ROOT / 'README.md', target / 'README.md')\n            editorial_before = (target / 'README.md').read_bytes()\n            with patch.object(Path, 'open', cp1252_open):\n")
replace('tests/test_text_portability.py',
        "                self.assertEqual(\n                    (target / 'README.md').read_text(encoding='utf-8'),\n                    (target / '.github/README.md').read_text(encoding='utf-8'),\n                )",
        "                self.assertEqual((target / 'README.md').read_bytes(), editorial_before)\n                self.assertFalse((target / '.github/README.md').exists())\n                self.assertIn('Jev Project Directory', (target / 'docs/DIRECTORY.md').read_text(encoding='utf-8'))")
replace('tests/test_publish.py', "for path in ('README.md', 'data/catalog.json', 'docs/CATALOG.md', 'data/discoveries.json'):",
        "for path in ('README.md', 'docs/DIRECTORY.md', 'data/catalog.json', 'docs/CATALOG.md', 'data/discoveries.json'):")
replace('tests/test_publish.py', "(self.work / 'README.md').write_text('updated catalog\\n', encoding='utf-8')",
        "(self.work / 'docs/DIRECTORY.md').write_text('updated catalog\\n', encoding='utf-8')")
replace('tests/test_publish.py', '    def test_unexpected_staged_file_rejected(self):\n', '''    def test_editorial_readme_is_not_published(self):
        self.change()
        (self.work / 'README.md').write_text('editorial change\\n', encoding='utf-8')
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.run_git('show', 'main:README.md', cwd=self.remote), 'initial')
        self.assertEqual((self.work / 'README.md').read_text(encoding='utf-8'), 'editorial change\\n')

    def test_staged_editorial_readme_is_rejected(self):
        self.change()
        (self.work / 'README.md').write_text('editorial change\\n', encoding='utf-8')
        self.run_git('add', 'README.md')
        before = self.run_git('rev-parse', 'main', cwd=self.remote)
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('unexpected staged file: README.md', result.stderr)
        self.assertEqual(before, self.run_git('rev-parse', 'main', cwd=self.remote))

    def test_unexpected_staged_file_rejected(self):
''')

write('LICENSE-CODE', read('LICENSE'))
write('LICENSE', read('.maintenance/CC0.txt'))
(ROOT / '.maintenance/CC0.txt').unlink()
write('LICENSING.md', '''# Licensing scope and attribution

The CC0 dedication in `LICENSE` applies to the repository owner's original editorial selection, arrangement, and newly contributed list text designated under these terms. It waives only rights the affirmer actually owns, where such rights exist. It does not waive anyone else's rights.

Original repository code, tests, and executable examples remain under the MIT grant reproduced unchanged in [LICENSE-CODE](LICENSE-CODE), including the copyright notice for Amal-David and awesome-jev contributors. Previously contributed writing retains its existing grant; the license change is not a retroactive waiver on behalf of contributors. Preserve applicable MIT notices when reusing inherited material.

Imported community metadata, third-party descriptions, linked projects, screenshots, recordings, model weights, datasets, and other external material retain their original terms and attribution. [SOURCES.md](SOURCES.md) records the community and media sources. Missing licensing information is not permission to reuse. The Awesome badge does not mean this repository has been accepted into the canonical Awesome index.

New contributions of original list text under [CONTRIBUTING.md](CONTRIBUTING.md) use CC0; original code contributions use MIT. Identify any material covered by different terms rather than claiming to waive third-party rights. This file clarifies scope; it does not replace the full legal texts or any source-specific notices.
''')

replace('AGENTS.md', '## One build, all surfaces', '## Editorial README and generated supporting views')
replace('AGENTS.md',
        '**Use `scripts/build.py` for every publication and consistency check.** The older `curate.py`, `curate_media.py`, and `curate_x.py` modules supply implementation helpers; their standalone CLI layouts are legacy and must not be used to publish the new directory.',
        '**Edit root `README.md` directly; it is editorial source, not a build output.** Use `scripts/build.py` for supporting views and consistency checks. The `curate.py`, `curate_media.py`, and `curate_x.py` modules remain implementation helpers; their legacy publication CLIs are disabled. Never reintroduce `.github/README.md`, which would shadow the editorial root page.')
replace('AGENTS.md',
        '- `templates/README.md`: editorial information hierarchy and named placeholders. Do not put generated gallery HTML or counts into this source template.',
        '- `README.md`: directly maintained Markdown selections. Update it deliberately alongside relevant evidence in `data/curated.json`; the builder validates listed projects against that evidence but never writes this file.\n- `templates/README.md`: template for `docs/DIRECTORY.md`, not for the root README. Keep generated HTML and counts out of this template.')
replace('AGENTS.md',
        '- Root `README.md` and `.github/README.md`: generated identical landing pages. Reviewed tables live in `docs/REVIEWED.md`, not a competing root README.',
        '- `docs/DIRECTORY.md`: generated supporting directory, preserving the quick-start, original X/media gallery, attribution, task paths, and discovery status. Reviewed evidence tables remain in `docs/REVIEWED.md`.')
replace('AGENTS.md',
        'Keep safety details collapsible but retain one warning near the top.',
        'Keep extended safety details in the supporting directory and retain one warning near the top of the root README.')
write('AGENTS.md', read('AGENTS.md') + '''
## Awesome index preparation

Read `docs/AWESOME_SUBMISSION.md` before any upstream submission. Do not claim this AI-assisted repository is non-AI-generated, purely human-authored, accepted, or fully eligible. Passing formatting tests is not editorial acceptance. Do not post reviews merely to satisfy an upstream quota or submit while upstream submissions are restricted. Preserve the honest AI-assistance disclosure and the license scopes in `LICENSING.md`.
''')
replace('CONTRIBUTING.md',
        'Commit source changes and generated changes together. The unified builder keeps both READMEs, reviewed picks, catalog, local viewer, freshness, X and media pages consistent. Edit `templates/README.md` for hierarchy or menu changes; do not edit generated READMEs. Do not run the older component scripts\' standalone CLIs for publication.',
        '''Edit root `README.md` directly when proposing a front-page selection. Use `- [Project](URL) - Description.` with a concise, objective description beginning with a capital and ending in a period. Keep `Contents` first, use its existing categories, and leave `Contributing` and `Footnotes` out of the contents list. Do not add archived, undocumented, or deprecated projects to the front page; preserve useful historical material in the supporting catalog with clear notes.

Commit source changes and generated supporting views together. `scripts/build.py` checks the editorial README against `data/curated.json` and exclusions, but never rewrites it. `templates/README.md` controls `docs/DIRECTORY.md`, which retains the original demo gallery and quick-start. The builder also maintains reviewed evidence, the catalog, viewer, freshness, and X/media indexes. Do not recreate `.github/README.md` or use the disabled legacy publishing CLIs.

Run the upstream formatting checker separately with Node.js 20+ and Git:

```sh
npx --yes --ignore-scripts awesome-lint@2.3.0 README.md
```

This is the full check, including repository age; do not suppress eligibility failures or claim a clean result when it reports them. See [Awesome submission status](docs/AWESOME_SUBMISSION.md). AI assistance must be disclosed honestly; direct editing does not make past AI-assisted work human-authored.

For new original list text contributed under these guidelines, apply CC0 to the rights you own. Original code contributions remain MIT. Existing contributions, imported metadata, and media keep their original terms; see [licensing scope](LICENSING.md).''')
write('docs/EDITORIAL_WORKFLOW.md', '''# Maintain the list and supporting directory

[Editorial list](../README.md) · [Contribute](../CONTRIBUTING.md) · [Curation rules](CURATION.md)

## Editorial source stays separate

Root `README.md` is directly maintained Markdown. Neither a build nor the scheduled discovery job rewrites it. There is no `.github/README.md` to shadow it. Update front-page selections deliberately, with primary-source evidence in `data/curated.json`; a source-reviewed record may remain only in the supporting catalog.

The original quick-start, task paths, curated X/media gallery, creator attribution, and discovery information remain in [DIRECTORY.md](DIRECTORY.md). Its template retains the historical path `templates/README.md` for existing maintenance instructions, but its output is no longer a README.

## Source and generated views

| Source | Generated surface |
|---|---|
| `templates/README.md` and catalog/media data | `docs/DIRECTORY.md` |
| `data/curated.json` | `docs/REVIEWED.md` and reviewed records in the catalog |
| Merged catalog and `templates/catalog.html` | `docs/CATALOG.md` and local `docs/catalog.html` |
| `data/x_demos.json` | `docs/X_DEMOS.md` and the supporting directory's X index |
| `data/media.json` and access receipts | Original gallery in `docs/DIRECTORY.md` and `docs/MEDIA.md` |
| Discovery receipt and rotating metadata checks | `docs/STATUS.md` and supporting-directory freshness |
| `data/exclusions.json` | Persistent exclusions applied after import/discovery |

The unified builder also validates README membership, formatting, contents links, and the independent-model/supporting-driver distinctions. It never selects a new front-page entry. Legacy component publication CLIs are disabled.

## Review and publication

Read implementation evidence and relevant examples/tests before selecting a project. Disclose affiliation, paid providers, observation/privacy boundaries, and author-reported benchmarks. Keep source inspection, runtime testing, and media access receipts distinct. Do not execute discovered projects or install their skills during curation.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
git diff --check
```

These commands are offline. `--refresh` and `--refresh-media` explicitly request bounded public discovery and media checks. The existing four-hour cadence remains unchanged. The publisher only stages generated supporting views; staged editorial source is rejected, not silently committed.

Maintain canonical X links and attribution in the existing source data. A successfully retrieved media URL does not establish that a demonstration ran live. Preserve prior media on transient access failures.

For upstream Awesome preparation, consult [AWESOME_SUBMISSION.md](AWESOME_SUBMISSION.md). Formatting checks cannot establish non-AI authorship, maturity, or editorial acceptance. Historical review notes remain dated records, not live approval checkpoints.
''')

for path in ('docs/BROWSE.md', 'docs/START_HERE.md', 'docs/CUA.md', 'SOURCES.md'):
    text = read(path)
    text = text.replace('../README.md#watch-jev-in-action', 'DIRECTORY.md#watch-jev-in-action')
    text = text.replace('https://github.com/Amal-David/awesome-jev#watch-jev-in-action', 'https://github.com/Amal-David/awesome-jev/blob/main/docs/DIRECTORY.md#watch-jev-in-action')
    write(path, text)

write('.github/workflows/curate.yml', '''name: Refresh Jev directory

on:
  schedule:
    - cron: '23 */4 * * *'
  workflow_dispatch:
  push:
    branches: [main]
    paths:
      - 'README.md'
      - 'scripts/**'
      - 'tests/**'
      - 'data/curated.json'
      - 'data/x_demos.json'
      - 'data/media.json'
      - 'data/exclusions.json'
      - 'templates/**'
      - 'examples/**'
      - '.github/workflows/curate.yml'

permissions:
  contents: read

concurrency:
  group: awesome-jev-curation
  cancel-in-progress: false

jobs:
  curate:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803
        with:
          fetch-depth: 0
      - name: Run offline tests
        run: python3 -m unittest discover -s tests -v
      - name: Build editorial changes offline
        if: github.event_name == 'push'
        run: python3 scripts/build.py
      - name: Discover and build the complete directory
        if: github.event_name != 'push'
        env:
          GITHUB_TOKEN: ${{ github.token }}
          PYTHONUNBUFFERED: '1'
        run: python3 scripts/build.py --refresh --refresh-media
      - name: Normalize refreshed catalog with editorial source of truth
        if: github.event_name != 'push'
        run: python3 scripts/build.py
      - name: Validate every generated surface offline
        run: python3 scripts/build.py --check
      - name: Commit and verify directory updates
        env:
          DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
        run: bash scripts/publish.sh
''')
(ROOT / '.maintenance/prepare_awesome.py').unlink()
print('Prepared only source/documentation changes. No repository or third-party tests executed.')
