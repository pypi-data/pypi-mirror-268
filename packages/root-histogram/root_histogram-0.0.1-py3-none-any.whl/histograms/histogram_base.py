import numpy.typing as npt

import os

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Self


class HistogramBase(ABC):
    """
    Abstract class describing the methods that a histogram class must implement
    """

    @property
    @abstractmethod
    def is_density(self) -> bool:
        ...

    @classmethod
    @abstractmethod
    def from_data(cls, data: npt.ArrayLike | tuple[npt.ArrayLike, ...], bins: npt.ArrayLike | tuple[npt.ArrayLike, ...],
                  density: bool = False) -> Self:
        ...

    @classmethod
    @abstractmethod
    def from_arrays(cls, counts: npt.ArrayLike, bins: npt.ArrayLike | tuple[npt.ArrayLike, ...],
                    errors: npt.ArrayLike | None = None) -> Self:
        ...

    @classmethod
    @abstractmethod
    def from_npz_file(cls, path_to_file: Path | str, files_name: tuple[str, ...] | None = None) -> Self:
        ...

    @classmethod
    @abstractmethod
    def from_rootfile(cls, path_to_file: Path | str, histo_name: str) -> Self:
        ...

    # @abstractmethod
    # def get_bins_errors(self) -> npt.NDArray[np.float64]:
    #     ...

    @abstractmethod
    def draw(self, log_scale: bool = False) -> None:
        ...

    @abstractmethod
    def save(self, path: Path) -> None:
        """
        Save the histogram as a npz file.
        :param path: path of the file
        """
        ...

    # @abstractmethod
    # def rebin(self, n: int):
    #     ...

    @staticmethod
    def check_file_size_limit(path: Path | str, max_size_mb: int = 500) -> None:
        """

        :param path:
        :param max_size_mb:
        :raise MemoryError:
        """
        size_bytes = os.path.getsize(filename=path)
        size_mega_bytes = size_bytes // 10 ** 6
        if size_mega_bytes > max_size_mb:
            raise MemoryError(f"File size {path} exceeds the limit of {max_size_mb} mb : {size_mega_bytes}")

        return None

