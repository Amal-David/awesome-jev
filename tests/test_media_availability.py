import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('media_availability', ROOT / 'scripts/curate_media.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MediaAvailabilityTests(unittest.TestCase):
    def test_failed_video_is_a_source_link_not_a_broken_player(self):
        data = json.loads((ROOT / 'data/media.json').read_text())
        video = next(item for item in data['items'] if item['group'] == 'videos')
        rendered = m.render(data, {video['id']: {'error': 'HTTPError', 'checked': m.TODAY}})
        self.assertNotIn('\n' + video['watch'] + '\n', rendered)
        self.assertIn(video['source'], rendered)
        self.assertIn('could not be verified', rendered)
        self.assertEqual(sum(line.startswith('https://github.com/user-attachments/assets/')
                             for line in rendered.splitlines()), 2)


if __name__ == '__main__': unittest.main()
