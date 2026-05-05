#!/usr/bin/env python3
"""Generate the Machine Learning Moments starter repo structure.

This script is intentionally aligned with the public repo scaffold:

- it creates the same `notebooks/core-path/` folders
- it creates the same required top-level files
- it keeps the core path, roadmap and content index consistent

Usage:
    python scripts/create-repo-structure.py
    python scripts/create-repo-structure.py --target ./machine-learning-moments
    python scripts/create-repo-structure.py --target ./machine-learning-moments --overwrite
"""

from __future__ import annotations

import argparse
from pathlib import Path

PHASES = [
    ("01-python-first-steps", "Python First Steps", "Learn the basics of Python in a gentle, notebook-first way."),
    ("02-python-thinking-toolkit", "Python Thinking Toolkit", "Use lists, dictionaries, loops, functions and simple algorithms to solve problems."),
    ("03-numbers-arrays-and-patterns", "Numbers, Arrays and Patterns", "Start numerical computing with NumPy and learn how machines represent data."),
    ("04-data-wrangling-with-pandas", "Data Wrangling with Pandas", "Load, clean, filter, group, reshape and prepare data using Pandas."),
    ("05-seeing-patterns-in-data", "Seeing Patterns in Data", "Use charts and exploratory analysis to understand data before modelling."),
    ("06-statistics-without-the-fear", "Statistics Without the Fear", "Build practical intuition for averages, variation, correlation and uncertainty."),
    ("07-your-first-machine-learning-models", "Your First Machine Learning Models", "Train your first supervised learning models with Scikit-Learn."),
    ("08-measuring-model-performance", "Measuring Model Performance", "Evaluate models using metrics, validation and sensible baselines."),
    ("09-the-maths-behind-the-magic", "The Maths Behind the Magic", "Build intuition for vectors, matrices, loss functions and gradient descent."),
    ("10-turning-data-into-features", "Turning Data into Features", "Prepare useful model inputs using encoding, scaling, imputation and pipelines."),
    ("11-words-numbers-and-tfidf", "Words, Numbers and TF-IDF", "Convert text into numbers and build simple text analytics models."),
    ("12-finding-hidden-groups", "Finding Hidden Groups", "Discover patterns using clustering, PCA and unsupervised learning."),
    ("13-learning-from-time-and-trends", "Learning from Time and Trends", "Work with time-series data, rolling windows, trends and simple forecasts."),
    ("14-neural-networks-from-scratch", "Neural Networks from Scratch", "Understand neural networks before using high-level deep learning tools."),
    ("15-real-world-machine-learning-projects", "Real-World Machine Learning Projects", "Apply the learning path to end-to-end practical projects."),
    ("16-responsible-ai-in-practice", "Responsible AI in Practice", "Learn about data quality, privacy, bias, explainability and governance."),
    ("17-modern-ai-embeddings-and-rag", "Modern AI, Embeddings and RAG", "Connect traditional ML to embeddings, semantic search, LLMs and RAG."),
]

INITIAL_PLAN = [
    ("001", "What is machine learning?", "Post", "01-python-first-steps", "N/A"),
    ("002", "Why Python is used for AI and data science", "Post", "01-python-first-steps", "N/A"),
    ("003", "What is a Jupyter notebook?", "Post + notebook", "01-python-first-steps", "00-how-to-use-jupyter.ipynb"),
    ("004", "Python basics for machine learning", "Post + notebook", "01-python-first-steps", "01-python-basics.ipynb"),
    ("005", "Lists, dictionaries and loops explained simply", "Post + notebook", "02-python-thinking-toolkit", "01-lists-dictionaries-and-loops.ipynb"),
    ("006", "What is an algorithm?", "Post + notebook", "02-python-thinking-toolkit", "02-algorithm-thinking.ipynb"),
    ("007", "Why Big-O matters, explained gently", "Post + notebook", "02-python-thinking-toolkit", "03-big-o-for-beginners.ipynb"),
    ("008", "What is a dataset?", "Post + notebook", "04-data-wrangling-with-pandas", "00-what-is-a-dataset.ipynb"),
    ("009", "Introduction to Pandas DataFrames", "Post + notebook", "04-data-wrangling-with-pandas", "01-pandas-dataframe-basics.ipynb"),
    ("010", "Cleaning missing data", "Post + notebook", "04-data-wrangling-with-pandas", "02-cleaning-missing-data.ipynb"),
    ("011", "Grouping and summarising data", "Post + notebook", "04-data-wrangling-with-pandas", "03-groupby-and-aggregation.ipynb"),
    ("012", "Visualising data before modelling", "Post + notebook", "05-seeing-patterns-in-data", "01-basic-charts.ipynb"),
    ("013", "Mean, median and standard deviation", "Post + notebook", "06-statistics-without-the-fear", "01-descriptive-statistics.ipynb"),
    ("014", "Correlation explained simply", "Post + notebook", "06-statistics-without-the-fear", "02-correlation.ipynb"),
    ("015", "What is a feature?", "Post", "07-your-first-machine-learning-models", "N/A"),
    ("016", "What is a label?", "Post", "07-your-first-machine-learning-models", "N/A"),
    ("017", "Your first machine learning model", "Post + notebook", "07-your-first-machine-learning-models", "01-first-ml-model.ipynb"),
    ("018", "Train/test split explained", "Post + notebook", "07-your-first-machine-learning-models", "02-train-test-split.ipynb"),
    ("019", "Accuracy is not always enough", "Post + notebook", "08-measuring-model-performance", "01-accuracy-is-not-enough.ipynb"),
    ("020", "What is TF-IDF?", "Post + notebook", "11-words-numbers-and-tfidf", "01-what-is-tfidf.ipynb"),
]


def write_file(path: Path, content: str, overwrite: bool = False) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def roadmap_text() -> str:
    text = "# AI/ML with Python Roadmap\n\nThis roadmap is the guided learning path for **Machine Learning Moments**.\n\n## Core path\n\n"
    for idx, (folder, title, desc) in enumerate(PHASES, 1):
        text += f"### {idx:02d}. {title}\n\n**Folder:** `notebooks/core-path/{folder}/`\n\n{desc}\n\n**Status:** Planned\n\n"
    return text


def content_index_text() -> str:
    text = "# Content Index\n\nThis file maps Substack posts, notebooks, exercises and quizzes.\n\n"
    text += "| # | Content title | Type | Core path folder | Related notebook | Status |\n"
    text += "|---:|---|---|---|---|---|\n"
    for row in INITIAL_PLAN:
        text += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | Planned |\n"
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="machine-learning-moments", help="Target repo folder")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.target)
    root.mkdir(parents=True, exist_ok=True)

    top_level_files = {
        "README.md": "# Machine Learning Moments\n\nSimple AI and machine learning lessons, one notebook at a time.\n\nStart with `notebooks/core-path/`.\n",
        "ROADMAP.md": roadmap_text(),
        "CONTENT_INDEX.md": content_index_text(),
        "CONTRIBUTING.md": "# Contributing\n\nKeep contributions clear, practical, beginner-friendly and free of private data.\n",
        "LICENSE": "MIT for code; CC BY 4.0 for educational content.\n",
        "requirements.txt": "jupyterlab\nnotebook\nipykernel\nnumpy\npandas\nscipy\nmatplotlib\nscikit-learn\nnbformat\npytest\n",
        "environment.yml": "name: ml-moments\nchannels:\n  - conda-forge\ndependencies:\n  - python=3.11\n  - jupyterlab\n  - notebook\n  - ipykernel\n  - numpy\n  - pandas\n  - scipy\n  - matplotlib\n  - scikit-learn\n  - pytest\n  - nbformat\n  - pip\n",
        "pyproject.toml": "[build-system]\nrequires = [\"setuptools>=68\", \"wheel\"]\nbuild-backend = \"setuptools.build_meta\"\n\n[project]\nname = \"machine-learning-moments\"\nversion = \"0.1.0\"\nrequires-python = \">=3.11\"\nlicense = { text = \"MIT for code; CC BY 4.0 for educational content\" }\n\n[tool.setuptools.packages.find]\nwhere = [\"src\"]\n",
        ".gitignore": "__pycache__/\n.venv/\n.ipynb_checkpoints/\n.DS_Store\n__MACOSX/\n.env\n.env.*\ndatasets/private/\nmodels/\noutputs/\n",
    }

    for filename, content in top_level_files.items():
        write_file(root / filename, content, args.overwrite)

    folders = [
        "notebooks/core-path",
        "posts/drafts",
        "posts/published",
        "posts/templates",
        "exercises/core-path",
        "quizzes/core-path",
        "projects",
        "datasets/sample",
        "datasets/external",
        "src/mlmoments",
        "assets/images",
        "assets/diagrams",
        "assets/screenshots",
        "templates",
        "scripts",
        "tests",
    ]
    for folder in folders:
        (root / folder).mkdir(parents=True, exist_ok=True)
        write_file(root / folder / ".gitkeep", "", args.overwrite)

    write_file(root / "notebooks" / "README.md", "# Notebooks\n\nStart with `core-path/`.\n", args.overwrite)
    write_file(root / "notebooks" / "core-path" / "README.md", "# Core Path\n\nThe main guided learning path.\n", args.overwrite)

    for idx, (folder, title, desc) in enumerate(PHASES, 1):
        phase_path = root / "notebooks" / "core-path" / folder
        phase_path.mkdir(parents=True, exist_ok=True)
        write_file(phase_path / "README.md", f"# {idx:02d}. {title}\n\n{desc}\n", args.overwrite)
        write_file(phase_path / ".gitkeep", "", args.overwrite)

    write_file(root / "src" / "mlmoments" / "__init__.py", '"""Machine Learning Moments helper package."""\n\n__version__ = "0.1.0"\n', args.overwrite)

    print(f"Created repo structure at: {root.resolve()}")


if __name__ == "__main__":
    main()
