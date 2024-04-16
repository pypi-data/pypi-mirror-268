import logging
import random
import string
from functools import wraps
from typing import List, Tuple, Union

import numpy as np
import pandas as pd
from pandas._typing import RandomState


def _check_num_unique_labels(data: pd.DataFrame, y_col_name: str):
    """Check if there are atleast two labels in the input data

    Args:
        data (pd.DataFrame): Input data with noisy labels
        y_col_name (str): Label column in data

    Raises:
        ValueError: if number of labels <= 1
    """
    count = len(pd.unique(data[y_col_name]))
    if count <= 1:
        raise ValueError(f"Number of distinct labels should be > 1 " f"Found {count}")


def _check_columns(data: pd.DataFrame, X_col_name: str, y_col_name: str):
    """Sanity checks for column names in input data

    Args:
        data (pd.DataFrame): Input data with noisy labels
        X_col_name (str): Column to be used to extract input features
        y_col_name (str): Label column in data

    Raises:
        ValueError: If any of the expected columns are not present in data
    """
    actual_columns = data.columns.tolist()

    if not X_col_name:
        raise ValueError("'X_col_name' cannot be None. Please pass a valid column name")

    if not y_col_name:
        raise ValueError("'y_col_name' cannot be None ")

    expected_columns = [X_col_name, y_col_name]

    if set(expected_columns) > set(actual_columns):
        raise ValueError(
            f"Data does not contain the expected columns. "
            f"Expected(X_col_name, y_col_name): {expected_columns}, "
            f"Actual: {actual_columns}"
        )


def _check_null_values(data: pd.DataFrame, X_col_name: str, y_col_name: str):
    """Sanity checks to detect null values in data

    Args:
        data (pd.DataFrame): Input data with noisy labels
        X_col_name (str): Column to be used to extract input features
        y_col_name (str): Label column in data

    Raises:
        ValueError: If null values are found in the data
    """
    if any(data[col].isnull().any() for col in [X_col_name, y_col_name]):
        raise ValueError(
            "Null values found in the data. \
                    Automatically imputing missing values is not supported yet."
        )


def _is_valid(data: pd.DataFrame, X_col_name: str, y_col_name: str):
    """Run collection of sanity checks on input data

    Args:
        data (pd.DataFrame): Input data with noisy labels
        X_col_name (str): Column to be used to extract input features
        y_col_name (str): Label column in data
    """
    _check_columns(data, X_col_name, y_col_name)
    _check_num_unique_labels(data, y_col_name)
    _check_null_values(data, X_col_name, y_col_name)


def add_asymmetric_noise(
    labels: pd.Series,
    noise_prob: float = 0.3,
    random_state: Union[RandomState, None] = None,
):
    """
    Util function to add asymmetric noise to labels
    for simulation of noisy label scenarios.

    Args:
        labels (pd.Series): Input pandas Series with integer values
                        ranging from 0 to n - 1.
        noise_prob (float): Probability of adding noise to each value.
        random_state (Union[RandomState, None]): Random seed for reproducibility
    Returns:
        pd.Series: Series with asymmetric noise added to it.
    """
    # Set seed
    np.random.seed(random_state)

    # Avoid modifying the original data
    noisy_labels = labels.copy()

    # Assuming labels are in the range 0 to n, get n
    max_value = noisy_labels.max()

    # Determine the number of samples to modify based on the noise ratio
    num_samples = min(len(noisy_labels), int(len(noisy_labels) * noise_prob + 1))

    # Sample random indices from the labels to introduce noise
    target_indices = np.random.choice(len(noisy_labels), num_samples, replace=False)

    for idx in target_indices:
        # Generate random noise for the value in this position
        noise = np.random.choice([-1, 1], size=1, p=[noise_prob, 1 - noise_prob])

        # Add noise to the series values
        noisy_labels[idx] += noise

        # Ensure values remain within the valid range [0, max_value]
        noisy_labels[idx] = noisy_labels[idx] % max_value

    return noisy_labels


def _exception_handler(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except ValueError as ve:
            if "cannot be greater than the number of members in each class" in str(ve):
                raise ValueError(
                    f"Not enough data samples per label with n_splits={self.n_splits} in CrossValCurate."
                )
            raise

    return wrapper
