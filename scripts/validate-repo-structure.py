#!/usr/bin/env python3
"""Validate the Machine Learning Moments repository structure.

This script is intended to run inside a real Git working tree.
It ignores normal development folders such as .git and .venv,
but it still flags unwanted public/release artefacts such as .DS_Store
and __MACOSX.
"""

from pathlib import Path
import sys
import re

ROOT = Path.cwd()

REQUIRED_TOP_LEVEL_FILES = [
    "README.md",
    "ROADMAP.md",
    "CONTENT_INDEX.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "requirements.txt",
    "environment.yml",
    "pyproject.toml",
]

CORE_PATH_DIRS = [
    "01-python-first-steps",
    "02-python-thinking-toolkit",
    "03-numbers-arrays-and-patterns",
    "04-data-wrangling-with-pandas",
    "05-seeing-patterns-in-data",
    "06-statistics-without-the-fear",
    "07-your-first-machine-learning-models",
    "08-measuring-model-performance",
    "09-the-maths-behind-the-magic",
    "10-turning-data-into-features",
    "11-words-numbers-and-tfidf",
    "12-finding-hidden-groups",
    "13-learning-from-time-and-trends",
    "14-neural-networks-from-scratch",
    "15-real-world-machine-learning-projects",
    "16-responsible-ai-in-practice",
    "17-modern-ai-embeddings-and-rag",
]

IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ipynb_checkpoints",
    "node_modules",
}

DISALLOWED_NAMES = {
    ".DS_Store",
}

DISALLOWED_DIRS = {
    "__MACOSX",
}


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    errors: list[str] = []

    # Required top-level files
    for file_name in REQUIRED_TOP_LEVEL_FILES:
        if not (ROOT / file_name).is_file():
            errors.append(f"Missing required top-level file: {file_name}")

    # Required top-level directories
    for dir_name in [
        "notebooks",
        "posts",
        "exercises",
        "quizzes",
        "projects",
        "datasets",
        "src",
        "assets",
        "templates",
        "scripts",
    ]:
        if not (ROOT / dir_name).is_dir():
            errors.append(f"Missing required top-level directory: {dir_name}")

    # Core path exists
    core_path = ROOT / "notebooks" / "core-path"
    if not core_path.is_dir():
        errors.append("Missing required directory: notebooks/core-path")

    # Core path directories
    for folder in CORE_PATH_DIRS:
        phase_dir = core_path / folder
        if not phase_dir.is_dir():
            errors.append(f"Missing core-path directory: notebooks/core-path/{folder}")
        if not (phase_dir / "README.md").is_file():
            errors.append(f"Missing README.md in: notebooks/core-path/{folder}")

    # Flag unwanted metadata, but ignore normal Git/development folders
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)

        if is_ignored(rel):
            continue

        if path.name in DISALLOWED_NAMES:
            errors.append(f"Disallowed metadata file found: {rel}")

        if path.is_dir() and path.name in DISALLOWED_DIRS:
            errors.append(f"Disallowed metadata directory found: {rel}")

    # ROADMAP should reference all core path folders
    roadmap = read_text(ROOT / "ROADMAP.md")
    for folder in CORE_PATH_DIRS:
        expected = f"notebooks/core-path/{folder}/"
        if expected not in roadmap and folder not in roadmap:
            errors.append(f"ROADMAP.md does not reference core-path folder: {folder}")

    # notebooks/core-path/README.md should list all core path folders
    core_readme = read_text(core_path / "README.md")
    for folder in CORE_PATH_DIRS:
        if folder not in core_readme:
            errors.append(f"notebooks/core-path/README.md does not list: {folder}")

    # CONTENT_INDEX should not reference invalid core-path folders
    content_index = read_text(ROOT / "CONTENT_INDEX.md")
    referenced_core_folders = set(
        re.findall(r"(?:^|[\\s`|/])((?:0[1-9]|1[0-7])-[a-z0-9-]+)", content_index)
    )

    valid_core_folders = set(CORE_PATH_DIRS)
    for folder in sorted(referenced_core_folders):
        if folder not in valid_core_folders:
            errors.append(f"CONTENT_INDEX.md references unknown core-path folder: {folder}")

    # Licence wording should mention both intended licences
    licence = read_text(ROOT / "LICENSE")
    if "MIT" not in licence:
        errors.append("LICENSE should mention MIT for code")
    if "CC BY 4.0" not in licence and "Creative Commons Attribution 4.0" not in licence:
        errors.append("LICENSE should mention CC BY 4.0 for educational content")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: repo structure, core path, roadmap and content index are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

