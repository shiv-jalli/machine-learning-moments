# Machine Learning Moments

**Simple AI and machine learning lessons, one notebook at a time.**

This repository supports the **Machine Learning Moments** public learning journey. It is designed for people who want a practical, beginner-friendly route into AI, machine learning and Python.

The repo is notebook-first, but it is not just a notebook dump. It is structured as a reusable teaching library with a clear core path, supporting posts, exercises, quizzes, projects and templates.

## Who this is for

This repo is for:

- beginners learning Python for AI and machine learning
- readers of the Machine Learning Moments Substack
- people who prefer practical notebooks over abstract theory
- learners who want small examples, exercises and plain-English explanations

## Repository structure

```text
machine-learning-moments/
├── README.md
├── ROADMAP.md
├── CONTENT_INDEX.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── pyproject.toml
├── notebooks/
│   └── core-path/
├── posts/
├── exercises/
├── quizzes/
├── projects/
├── datasets/
├── src/
├── assets/
├── templates/
├── scripts/
└── tests/
```

## The core path

The main learning journey lives here:

```text
notebooks/core-path/
```

It contains the 17-part guided roadmap from Python basics through to machine learning, responsible AI, embeddings and RAG.

Future notebook types can be added later beside `core-path`, for example:

```text
notebooks/theme-labs/
notebooks/real-world-cases/
notebooks/issue-clinics/
notebooks/mini-projects/
notebooks/experiments/
```

For now, this repo starts with only the core path to keep the structure simple.

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

Start JupyterLab:

```bash
jupyter lab
```

## Using Conda instead

```bash
conda env create -f environment.yml
conda activate ml-moments
pip install -e .
jupyter lab
```

## How to use the repo

Start with:

```text
notebooks/core-path/01-python-first-steps/
```

Then work through each folder in order. Each folder contains a short README explaining the learning goal and the notebooks that will be added.

## Keeping the repo consistent

Run the validation script after editing the structure:

```bash
python scripts/validate-repo-structure.py
```

The script checks that the core-path folders, roadmap and content index still align.

## Content status

This repo is intended to grow gradually. Empty folders are included deliberately so the learning structure is visible from the start.

Track progress in:

```text
ROADMAP.md
CONTENT_INDEX.md
```

## Licence

This project uses a permissive dual-licence approach:

- **Code** is licensed under the MIT License.
- **Educational content**, including notebooks, posts, exercises, quizzes, diagrams and written learning material, is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

That means the material is free to use, adapt and share, with attribution for the learning content.
