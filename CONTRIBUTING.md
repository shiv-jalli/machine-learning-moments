# Contributing

Thank you for helping improve **Machine Learning Moments**.

The aim of this repo is to make AI, machine learning and Python easier to learn through small, practical, beginner-friendly examples.

## Contribution types

Useful contributions include:

- fixing typos
- improving explanations
- adding beginner-friendly examples
- adding exercises or quiz questions
- improving notebook readability
- suggesting datasets
- improving setup instructions
- reporting broken notebooks

## Teaching style

Please keep the tone:

- clear
- practical
- friendly
- beginner-safe
- jargon-light

Prefer:

```text
A feature is an input column used by a model.
```

Over:

```text
A feature is an independent explanatory variable in the feature space.
```

Technical terms are fine, but introduce them gently.

## Notebook structure

Each teaching notebook should follow this pattern where possible:

```text
Title
Learning goals
Plain-English explanation
Small example
Code cell
Try it yourself
Mini challenge
Common mistakes
Summary
Next step
```

## File naming

Use lowercase names with hyphens:

```text
01-python-basics.ipynb
02-lists-dictionaries-and-loops.ipynb
03-functions-and-errors.ipynb
```

Avoid:

```text
Test.ipynb
final.ipynb
final-final-v2.ipynb
my_new_notebook.ipynb
```

## Data policy

Do not commit:

- private data
- personal data
- confidential data
- large datasets
- API keys
- access tokens
- passwords
- generated model binaries

Use small public or synthetic datasets where possible.

## Licence of contributions

By contributing, you agree that:

- code contributions are licensed under the MIT License
- educational content contributions are licensed under CC BY 4.0

## Pull request checklist

Before opening a pull request, check:

- [ ] the notebook runs from top to bottom
- [ ] explanations are beginner-friendly
- [ ] file names follow the naming convention
- [ ] no private data or secrets are included
- [ ] the content index is updated if needed
- [ ] the roadmap is updated if needed
- [ ] `python scripts/validate-repo-structure.py` passes
