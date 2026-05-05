#!/usr/bin/env python3
"""Validate the Machine Learning Moments repo scaffold.

Checks:
- required top-level files exist
- no Mac metadata or nested .git folder is present
- all 17 `notebooks/core-path/` folders exist
- ROADMAP.md references each core-path folder
- notebooks/core-path/README.md lists each folder
- CONTENT_INDEX.md references only existing core-path folders
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

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

CORE_PATH_FOLDERS = [
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

DISALLOWED_PATH_PARTS = {".git", "__MACOSX"}
DISALLOWED_FILENAMES = {".DS_Store"}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    root = Path.cwd()
    errors: list[str] = []

    for filename in REQUIRED_TOP_LEVEL_FILES:
        if not (root / filename).is_file():
            fail(f"Missing required top-level file: {filename}", errors)

    for path in root.rglob("*"):
        rel_parts = set(path.relative_to(root).parts)
        if rel_parts & DISALLOWED_PATH_PARTS:
            fail(f"Disallowed metadata path found: {path.relative_to(root)}", errors)
        if path.name in DISALLOWED_FILENAMES:
            fail(f"Disallowed metadata file found: {path.relative_to(root)}", errors)

    core_root = root / "notebooks" / "core-path"
    if not core_root.is_dir():
        fail("Missing notebooks/core-path directory", errors)
    else:
        actual = sorted([p.name for p in core_root.iterdir() if p.is_dir()])
        expected = CORE_PATH_FOLDERS
        if actual != expected:
            fail(f"Core path folders do not match expected list. Expected {expected}, found {actual}", errors)

    roadmap = read(root / "ROADMAP.md") if (root / "ROADMAP.md").exists() else ""
    core_readme = read(core_root / "README.md") if (core_root / "README.md").exists() else ""
    content_index = read(root / "CONTENT_INDEX.md") if (root / "CONTENT_INDEX.md").exists() else ""

    for folder in CORE_PATH_FOLDERS:
        if f"notebooks/core-path/{folder}/" not in roadmap:
            fail(f"ROADMAP.md does not reference notebooks/core-path/{folder}/", errors)
        if f"`{folder}/`" not in core_readme and folder not in core_readme:
            fail(f"notebooks/core-path/README.md does not list {folder}", errors)

    index_rows = [line for line in content_index.splitlines() if line.startswith("|") and not line.startswith("|---")]
    referenced_folders: set[str] = set()
    for line in index_rows[1:]:
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 4:
            folder = parts[3]
            if folder and folder != "Core path folder":
                referenced_folders.add(folder)

    unknown = sorted(folder for folder in referenced_folders if folder not in CORE_PATH_FOLDERS)
    if unknown:
        fail(f"CONTENT_INDEX.md references unknown core-path folders: {unknown}", errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: repo structure, core path, roadmap and content index are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
