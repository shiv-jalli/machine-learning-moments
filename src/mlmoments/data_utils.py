"""Small reusable helpers for Machine Learning Moments notebooks."""

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file and return a Pandas DataFrame."""
    return pd.read_csv(Path(path))


def preview_dataframe(df: pd.DataFrame, rows: int = 5) -> pd.DataFrame:
    """Return a small preview of a DataFrame."""
    return df.head(rows)
