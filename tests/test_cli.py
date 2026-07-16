import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "issue_to_plan.py"


class CliBehaviorTests(unittest.TestCase):
    def run_cli(self, *args, input_text=None):
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            input=input_text,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=False,
        )

    def test_generates_normal_implementation_plan(self):
        result = self.run_cli("Add dark mode to settings page")

        self.assertEqual(result.returncode, 0)
        self.assertIn("# Implementation Plan", result.stdout)
        self.assertIn("Add dark mode to settings page", result.stdout)
        self.assertIn("## Steps", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_generates_ai_prompt(self):
        result = self.run_cli("Fix login redirect bug", "--ai-prompt")

        self.assertEqual(result.returncode, 0)
        self.assertIn("Act as an experienced software engineer.", result.stdout)
        self.assertIn("> Fix login redirect bug", result.stdout)
        self.assertIn("## Implementation Steps", result.stdout)
        self.assertNotIn("# Implementation Plan", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_prints_version(self):
        result = self.run_cli("--version")

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "issue-to-plan 0.1.0")
        self.assertEqual(result.stderr, "")

    def test_reads_issue_from_stdin(self):
        result = self.run_cli(input_text="Add password reset flow\n")

        self.assertEqual(result.returncode, 0)
        self.assertIn("# Implementation Plan", result.stdout)
        self.assertIn("Add password reset flow", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_writes_output_to_temporary_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "plan.md"

            result = self.run_cli(
                "Refactor profile card",
                "--output",
                str(output_path),
            )

            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), f"Plan written to {output_path}")
            self.assertEqual(result.stderr, "")
            self.assertTrue(output_path.exists())
            output = output_path.read_text(encoding="utf-8")
            self.assertIn("# Implementation Plan", output)
            self.assertIn("Refactor profile card", output)

    def test_shows_message_when_no_issue_is_supplied(self):
        result = self.run_cli(input_text="")

        self.assertEqual(result.returncode, 0)
        self.assertIn("Please provide an issue description.", result.stdout)
        self.assertIn("Examples:", result.stdout)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
