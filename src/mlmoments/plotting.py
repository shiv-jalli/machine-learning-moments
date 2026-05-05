"""Plotting helpers for Machine Learning Moments notebooks."""

import matplotlib.pyplot as plt
import pandas as pd


def simple_histogram(df: pd.DataFrame, column: str, bins: int = 20) -> None:
    """Draw a simple histogram for a numeric column."""
    df[column].hist(bins=bins)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.title(f"Distribution of {column}")
    plt.show()
