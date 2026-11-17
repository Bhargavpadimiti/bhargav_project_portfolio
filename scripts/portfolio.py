#!/usr/bin/env python3
"""Portfolio helper: set up the repo, scaffold projects, and run their tests.

Standard library only, so it works anywhere Python 3.11+ is installed
(Windows, macOS, Linux) with no extra installs.

Usage:
    python scripts/portfolio.py setup
    python scripts/portfolio.py new weather-cli --type python -d "CLI that shows the forecast"
    python scripts/portfolio.py test projects/weather-cli
    python scripts/portfolio.py test            # every project
    python scripts/portfolio.py list [--json] [--changed-since origin/main]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "projects"
TEMPLATES_DIR = ROOT / "templates"
README = ROOT / "README.md"

# Directories that hold buildable projects (one sub-folder per project).
PROJECT_ROOTS = (PROJECTS_DIR, TEMPLATES_DIR)
# Any change under these paths re-tests every project in CI.
SHARED_PATHS = ("scripts/", ".github/workflows/")

TEMPLATE_SLUG = "template-project"
TEMPLATE_PKG = "template_project"
TEMPLATE_TITLE = "Template Project"
TEMPLATE_DESCRIPTIONS = (
    "One-line description of what this project does and who it is for.",
    "One-line description of what this project does.",
)
TECH_LABELS = {"python": "Python", "node": "Node.js", "generic": "—"}
COPY_IGNORE = shutil.ignore_patterns(
    ".venv", "node_modules", "__pycache__", ".pytest_cache", ".ruff_cache", "*.egg-info"
)
TABLE_START = "<!-- projects:start -->"
TABLE_END = "<!-- projects:end -->"
PLACEHOLDER_ROW_MARKER = "_Your first project will appear here_"
NAME_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")

GIT_LOCAL_CONFIG = {
    "commit.template": ".gitmessage",  # pre-filled commit message guide
    "pull.rebase": "true",  # linear history, no merge bubbles
    "rebase.autoStash": "true",  # pull/rebase with uncommitted changes
    "fetch.prune": "true",  # drop remote branches deleted on GitHub
    "push.autoSetupRemote": "true",  # plain `git push` works on new branches
}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def info(msg: str) -> None:
    print(f"==> {msg}")


def fail(msg: str) -> NoReturn:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


def run(cmd: list[str], cwd: Path = ROOT, check: bool = True) -> int:
    print(f"$ {' '.join(cmd)}", flush=True)
    code = subprocess.run(cmd, cwd=cwd).returncode
    if check and code != 0:
        fail(f"command failed with exit code {code}: {' '.join(cmd)}")
    return code


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def project_type(path: Path) -> str | None:
    """Detect how to test a project folder, or None if it has nothing to test."""
    if (path / "pyproject.toml").is_file():
        return "python"
    if (path / "package.json").is_file():
        return "node"
    if (path / "test.sh").is_file():
        return "script"
    return None


def discover() -> list[dict[str, str]]:
    found = []
    for parent in PROJECT_ROOTS:
        if not parent.is_dir():
            continue
        for child in sorted(parent.iterdir()):
            kind = project_type(child) if child.is_dir() else None
            if kind:
                found.append({"path": child.relative_to(ROOT).as_posix(), "type": kind})
    return found


# --------------------------------------------------------------------------- #
# setup
# --------------------------------------------------------------------------- #
def pre_commit_cmd() -> list[str] | None:
    if shutil.which("pre-commit"):
        return ["pre-commit"]
    probe = subprocess.run([sys.executable, "-m", "pre_commit", "--version"], capture_output=True)
    return [sys.executable, "-m", "pre_commit"] if probe.returncode == 0 else None


def cmd_setup(_: argparse.Namespace) -> None:
    if not shutil.which("git"):
        fail("git is not installed: https://git-scm.com/downloads")

    cmd = pre_commit_cmd()
    if cmd is None:
        info("Installing pre-commit")
        attempts = []
        if shutil.which("pipx"):
            attempts.append(["pipx", "install", "pre-commit"])
        attempts.append([sys.executable, "-m", "pip", "install", "--user", "pre-commit"])
        for attempt in attempts:
            if run(attempt, check=False) == 0 and (cmd := pre_commit_cmd()):
                break
        else:
            fail(
                "could not install pre-commit automatically. Install it with one of:\n"
                "  pipx install pre-commit   |   brew install pre-commit   |   "
                "pip install pre-commit\nthen re-run this command."
            )

    info("Installing git hooks (pre-commit + commit-msg)")
    run([*cmd, "install", "--install-hooks"])

    info("Applying repo-local git settings (this repository only)")
    for key, value in GIT_LOCAL_CONFIG.items():
        git("config", "--local", key, value)
        print(f"    {key} = {value}")

    info("Done. Hooks now run automatically on every commit.")


# --------------------------------------------------------------------------- #
# new
# --------------------------------------------------------------------------- #
def replace_in_tree(root: Path, replacements: dict[str, str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # binary file
        new = text
        for old, value in replacements.items():
            new = new.replace(old, value)
        if new != text:
            path.write_text(new, encoding="utf-8")


def add_readme_row(slug: str, title: str, description: str, kind: str) -> bool:
    if not README.is_file():
        return False
    text = README.read_text(encoding="utf-8")
    if TABLE_START not in text or TABLE_END not in text:
        return False
    head, rest = text.split(TABLE_START, 1)
    table, tail = rest.split(TABLE_END, 1)
    lines = [ln for ln in table.strip("\n").splitlines() if PLACEHOLDER_ROW_MARKER not in ln]
    lines.append(
        f"| [{title}](projects/{slug}) | {description} | {TECH_LABELS[kind]} | 🚧 In progress |"
    )
    README.write_text(
        f"{head}{TABLE_START}\n" + "\n".join(lines) + f"\n{TABLE_END}{tail}", encoding="utf-8"
    )
    return True


def cmd_new(args: argparse.Namespace) -> None:
    slug = args.name
    if not NAME_RE.match(slug):
        fail(f"'{slug}' is not a valid name. Use lowercase-words-with-hyphens, e.g. 'weather-cli'.")
    template = TEMPLATES_DIR / args.type
    dest = PROJECTS_DIR / slug
    if not template.is_dir():
        fail(f"template not found: {template.relative_to(ROOT)}")
    if dest.exists():
        fail(f"{dest.relative_to(ROOT)} already exists")

    pkg = slug.replace("-", "_")
    title = args.title or " ".join(word.capitalize() for word in slug.split("-"))
    description = args.description or "Short description of the project."

    if not args.no_branch:
        try:
            current = git("rev-parse", "--abbrev-ref", "HEAD")
        except RuntimeError:
            current = ""
        if current in ("main", "master"):
            branch = f"feat/{slug}"
            try:
                git("switch", "-c", branch)
                info(f"Created and switched to branch {branch}")
            except RuntimeError as exc:
                print(f"    (skipped creating branch {branch}: {exc})")

    info(f"Creating {dest.relative_to(ROOT).as_posix()} from the {args.type} template")
    shutil.copytree(template, dest, ignore=COPY_IGNORE)
    if (dest / "src" / TEMPLATE_PKG).is_dir():
        (dest / "src" / TEMPLATE_PKG).rename(dest / "src" / pkg)

    replacements = {d: description for d in TEMPLATE_DESCRIPTIONS}
    replacements.update({TEMPLATE_SLUG: slug, TEMPLATE_PKG: pkg, TEMPLATE_TITLE: title})
    replace_in_tree(dest, replacements)

    if add_readme_row(slug, title, description, args.type):
        info("Added the project to the table in README.md")

    rel = dest.relative_to(ROOT).as_posix()
    print(
        f"\nNext steps:\n"
        f"  1. Write your code in {rel}/ and fill in {rel}/README.md\n"
        f"  2. Run the tests:  python scripts/portfolio.py test {rel}\n"
        f"  3. Commit:         git add . && git commit   (the template guides the message)\n"
        f"  4. Open a PR:      git push && gh pr create --fill"
    )


# --------------------------------------------------------------------------- #
# list
# --------------------------------------------------------------------------- #
def changed_projects(base: str, projects: list[dict[str, str]]) -> list[dict[str, str]]:
    try:
        changed = git("diff", "--name-only", f"{base}...HEAD").splitlines()
    except RuntimeError as exc:
        print(
            f"warning: git diff against {base} failed ({exc}); selecting all projects",
            file=sys.stderr,
        )
        return projects
    if any(f.startswith(SHARED_PATHS) for f in changed):
        return projects
    return [p for p in projects if any(f.startswith(p["path"] + "/") for f in changed)]


def cmd_list(args: argparse.Namespace) -> None:
    projects = discover()
    if args.changed_since:
        projects = changed_projects(args.changed_since, projects)
    if args.json:
        print(json.dumps(projects))
    else:
        for p in projects:
            print(f"{p['type']:<8} {p['path']}")


# --------------------------------------------------------------------------- #
# test
# --------------------------------------------------------------------------- #
def venv_python(venv: Path) -> Path:
    windows = venv / "Scripts" / "python.exe"
    return windows if windows.exists() else venv / "bin" / "python"


def test_python(path: Path) -> None:
    venv = path / ".venv"
    if not venv.exists():
        run([sys.executable, "-m", "venv", str(venv)])
    py = str(venv_python(venv))
    run([py, "-m", "pip", "install", "--quiet", "--upgrade", "pip"], cwd=path)
    run([py, "-m", "pip", "install", "--quiet", "-e", ".[dev]"], cwd=path)
    code = run([py, "-m", "pytest"], cwd=path, check=False)
    if code == 5:
        print("    (no tests found — add some in tests/)")
    elif code != 0:
        fail(f"tests failed in {path.relative_to(ROOT).as_posix()}")


def test_node(path: Path) -> None:
    npm = shutil.which("npm") or fail("npm is not installed: https://nodejs.org")
    run([npm, "ci" if (path / "package-lock.json").exists() else "install"], cwd=path)
    scripts = json.loads((path / "package.json").read_text(encoding="utf-8")).get("scripts", {})
    for script in ("lint", "test", "build"):
        if script in scripts:
            run([npm, "run", script], cwd=path)


def test_script(path: Path) -> None:
    bash = shutil.which("bash") or fail("bash is required to run test.sh")
    run([bash, "test.sh"], cwd=path)


RUNNERS = {"python": test_python, "node": test_node, "script": test_script}


def cmd_test(args: argparse.Namespace) -> None:
    if args.paths:
        targets = []
        for raw in args.paths:
            path = (Path.cwd() / raw).resolve()
            if not path.is_relative_to(ROOT):
                fail(f"{raw} is outside this repository")
            kind = project_type(path)
            if kind is None:
                fail(f"{raw}: no pyproject.toml, package.json or test.sh found")
            targets.append({"path": path.relative_to(ROOT).as_posix(), "type": kind})
    else:
        targets = discover()

    for target in targets:
        info(f"Testing {target['path']} ({target['type']})")
        RUNNERS[target["type"]](ROOT / target["path"])
    info(f"All {len(targets)} project(s) passed")


# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="portfolio", description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("setup", help="install git hooks and repo-local git settings").set_defaults(
        func=cmd_setup
    )

    new = sub.add_parser("new", help="scaffold a new project from a template")
    new.add_argument("name", help="folder name, lowercase-with-hyphens (e.g. weather-cli)")
    new.add_argument("-t", "--type", choices=sorted(TECH_LABELS), default="python")
    new.add_argument("-d", "--description", help="one-line description for README and metadata")
    new.add_argument("--title", help="display name (default: derived from name)")
    new.add_argument("--no-branch", action="store_true", help="don't create a feat/<name> branch")
    new.set_defaults(func=cmd_new)

    lst = sub.add_parser("list", help="list testable projects")
    lst.add_argument("--json", action="store_true", help="machine-readable output for CI")
    lst.add_argument("--changed-since", metavar="REF", help="only projects changed since REF")
    lst.set_defaults(func=cmd_list)

    tst = sub.add_parser("test", help="install dependencies and run tests")
    tst.add_argument("paths", nargs="*", help="project folders (default: all)")
    tst.set_defaults(func=cmd_test)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
