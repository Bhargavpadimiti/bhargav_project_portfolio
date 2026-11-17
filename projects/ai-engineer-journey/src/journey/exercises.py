"""Run a week's coding exercises with pytest and count the results."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CheckResult:
    passed: int
    total: int

    @property
    def complete(self) -> bool:
        return self.total > 0 and self.passed == self.total


def run_checks(folder: Path, cwd: Path, quiet: bool = False) -> CheckResult:
    """Run pytest on ``folder``; pytest's own output goes straight to the terminal."""
    if not folder.is_dir():
        raise FileNotFoundError(f"no exercises at {folder}")
    with tempfile.TemporaryDirectory() as tmp:
        report = Path(tmp) / "report.xml"
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            str(folder),
            "-q",
            "--tb=short",
            "--no-header",
            "-p",
            "no:cacheprovider",
            f"--junitxml={report}",
        ]
        subprocess.run(cmd, cwd=cwd, capture_output=quiet, check=False)
        if not report.is_file():
            raise RuntimeError("pytest did not produce a report - is pytest installed?")
        return parse_junit(report)


def parse_junit(report: Path) -> CheckResult:
    root = ET.parse(report).getroot()
    # A syntax or import error stops pytest from collecting tests at all:
    # report that as "nothing ran" rather than as a failed test.
    for error in root.iter("error"):
        if "collection failure" in (error.get("message") or ""):
            return CheckResult(passed=0, total=0)
    suites = [root] if root.tag == "testsuite" else root.findall("testsuite")
    total = failed = skipped = 0
    for suite in suites:
        total += int(suite.get("tests", 0))
        failed += int(suite.get("failures", 0)) + int(suite.get("errors", 0))
        skipped += int(suite.get("skipped", 0))
    return CheckResult(passed=total - failed - skipped, total=total)
