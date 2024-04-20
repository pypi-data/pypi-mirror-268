
import numpy as np
import numpy.typing as npt

from itertools import pairwise

from typing import Any
from pathlib import Path


class ArraySizeError(Exception):
    """
    Error raise when an array
    """
    def __init__(self, expected_size: int, actual_size: int):
        message = f"Expected array of size {expected_size} but got {actual_size} instead"
        super().__init__(message)


def check_dim(array: npt.NDArray[Any], dim: int) -> bool:
    """

    :param array:
    :param dim:
    """
    return array.ndim == dim


def check_min_size(array: npt.NDArray[Any], min_size: int) -> bool:
    return array.size >= min_size


def contains_negative(array: npt.NDArray[Any]) -> bool:
    return bool(np.any(array < 0))


def contains_NaN(array: npt.NDArray[Any]) -> bool:
    return bool(np.any(np.isnan(array)))


def is_array_sorted(array: npt.NDArray[Any]) -> bool:
    """
    For 1 dimensional array
    :param array:
    :type array:
    :return:
    :rtype:
    """
    if array.ndim > 1:
        raise ValueError("Do not work on multidimensional array")
    for a, b in pairwise(array):
        if a > b:
            return False
    return True


def validate_counts(counts: npt.NDArray[np.float64], dim: int) -> None:
    """
    Check that the dimension is the one expected and counts do not contain NaN or negative value.
    :param dim: expected dimension of the array.
    :param counts: array containing the counts
    :raise ValueError: if array.dim != dim, if contains negative values / NaN
    """

    if not check_dim(array=counts, dim=dim):
        raise ValueError(f"Counts array must be one dimensional. Got {counts.ndim=} instead.")
    if contains_NaN(array=counts):
        raise ValueError("Counts array contains NaN value.")
    if contains_negative(array=counts):
        raise ValueError("Counts array contains negative value.")
    return None


def validate_bins_and_counts_shape(counts: npt.NDArray[np.float64],
                                   bins: npt.NDArray[np.float64], axis: int = 0) -> None:
    """
    Ensure the number of bins agrees with the counts (with underflow and overflow)
    :param counts:
    :param bins:
    :param axis: for multidimensional data
    :raise ValueError:
    """
    if axis > (counts.ndim-1):
        raise ValueError(f"ndim too low ({counts.ndim=}) with {axis=}")
    if counts.shape[axis] != (bins.size + 1):
        raise ValueError(f"The number of bins do not match the counts over axis {axis}. {counts.shape[axis]} "
                         f"vs {(bins.size + 1)}")
    return None


def sanitize_file_path(path_to_file: str | Path, extension: str) -> Path:
    """
    Checks the extension of the file, if it exists, if it is a file and converts it into a Path object
    :param path_to_file:
    :param extension:
    :return: pathlib.Path object
    """
    if isinstance(path_to_file, str):
        path_to_file = Path(path_to_file)
    if path_to_file.suffix != extension:
        raise ValueError(f"Wrong file extension: {extension} expected but got {path_to_file.suffix}.")
    if not path_to_file.exists():
        raise FileNotFoundError(f"{path_to_file} not found.")
    if not path_to_file.is_file():
        raise ValueError(f'{path_to_file} is not a file')

    return path_to_file

