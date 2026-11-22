"""Regression tests for local CLI."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pdc", ROOT / "scripts" / "pdc.py")
pdc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pdc)


class TestPDC(unittest.TestCase):
    def test_valid_template(self):
        self.assertEqual(pdc.validate(ROOT / "templates" / "PROJECT-STATE.json"), [])

    def test_initializer_creates_files(self):
        with tempfile.TemporaryDirectory() as folder:
            result = pdc.init_project(folder, "sample-project")
            self.assertTrue((result / "HANDOFF.md").exists())
            state = json.loads((result / "PROJECT-STATE.json").read_text(encoding="utf-8"))
            self.assertEqual(state["project_id"], "sample-project")
            self.assertEqual(pdc.validate(result / "PROJECT-STATE.json"), [])

    def test_prevent_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            pdc.init_project(folder, "sample-project")
            with self.assertRaises(FileExistsError):
                pdc.init_project(folder, "sample-project")

    def test_reject_invalid_json_state(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "state.json"
            path.write_text("{}", encoding="utf-8")
            self.assertGreater(len(pdc.validate(path)), 3)

    def test_reject_unsafe_id(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                pdc.init_project(folder, "../unsafe")

    def test_skill_metadata(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\nname: ai-project-documentation\n"))
        self.assertIn("license: MIT", content)


if __name__ == "__main__":
    unittest.main()
