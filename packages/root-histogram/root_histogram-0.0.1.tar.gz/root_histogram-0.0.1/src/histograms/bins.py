
import numpy as np
import numpy.typing as npt

from itertools import pairwise
from typing import Self

from src.tools import data_checker as dc


class Bins:
    """
    Code logic : the class relies on properties. The only true attribute is _bins_edges

    """

    def __init__(self, bins_edges: npt.ArrayLike):
        """

        :param bins_edges: one dimensional array-like with at least 2 elements
        """
        bins_edges = self._bins_converter(bins_edges)
        self._bins_edges_validator(bins_edges)
        self._bins_edges = bins_edges
        self._update_centers_and_widths()

    def __getitem__(self, item: int) -> npt.NDArray[np.float64]:
        self.validate_bin_nb_parameter(item)
        if item >= 0:
            return self.bins_edges[[item, item+1]]
        else:
            return self.bins_edges[[item-1, item]]

    @property
    def bins_edges(self) -> npt.NDArray[np.float64]:
        return self._bins_edges

    @bins_edges.setter
    def bins_edges(self, value: npt.ArrayLike) -> None:
        bins_edges = self._bins_converter(value)
        self._bins_edges_validator(bins_edges)
        self._bins_edges = bins_edges
        self._update_centers_and_widths()

    @property
    def bins_centers(self) -> npt.NDArray[np.float64]:
        return self._bins_centers

    @property
    def bins_widths(self) -> npt.NDArray[np.float64]:
        return self._bins_widths

    @property
    def nb_bins(self) -> int:
        """"
        without overflow and underflow bin
        """
        return self._bins_edges.size - 1

    def __len__(self) -> int:
        return self.nb_bins

    def __str__(self) -> str:
        msg_to_print = "bins_edges: "
        if self.nb_bins < 10:
            msg_to_print += str(self.bins_edges)
            msg_to_print += '\n'
        else:
            msg_to_print += f'[{self.get_first_edge()}, ..., {self.get_last_edge()}]\n'
        msg_to_print += f'nb of bins : {self.nb_bins}\n'
        msg_to_print += 'type : np.float64'

        return msg_to_print

    @staticmethod
    def _bins_converter(bins_edges: npt.ArrayLike) -> npt.NDArray[np.float64]:
        """
        converts one dimensional array-like to a numpy array of type float64
        :param bins_edges:
        :return:
        """
        return np.array(bins_edges, dtype=np.float64)

    @staticmethod
    def _bins_edges_validator(array: npt.NDArray[np.float64]) -> None:
        """
        For a given array, check its dimension, the size and if it is sorted.

        :param array:
        :raise TypeError:
        :raise ValueError: if the array is not one dimensional, or contains less than two elements, or is not sorted
        """
        if not isinstance(array, np.ndarray):
            raise TypeError(f"Numpy array expected. Got {type(array)} instead.")
        if not dc.check_dim(array=array, dim=1):
            raise ValueError(f"Bins edges array must be one dimensional. Got {array.ndim=} instead")
        if not dc.check_min_size(array=array, min_size=2):
            raise ValueError(f"At least 2 edges are required. Got {array.size=} instead.")
        if not dc.is_array_sorted(array):
            raise ValueError("Bin edges must be sorted.")

        return None

    def _update_centers_and_widths(self) -> None:
        """
        Update the centers and widths of the bins. Called when the bin edges are initialized or modified.
        """
        self._bins_centers: npt.NDArray[np.float64] = self.center_bins()
        self._bins_widths: npt.NDArray[np.float64] = np.array([right_edge - left_edge for (left_edge, right_edge)
                                                               in pairwise(self._bins_edges)])

        return None

    def validate_bin_nb_parameter(self, bin_nb: int, param_name: str = "bin number") -> None:
        """

        :param bin_nb: bin's number (between 0 and self.nb_bins-1)
        :param param_name:
        :raise TypeError: if bin_nb is not an int
        :raise ValueError: if bin_nb is not valid
        """
        if not isinstance(bin_nb, int):
            raise TypeError(f"Bin number must be a int. Got {type(bin_nb)} instead.")
        if bin_nb < -self.nb_bins or (bin_nb >= self.nb_bins):
            raise ValueError(f"Wrong value for {param_name}. It must be between {-self.nb_bins} and {self.nb_bins-1}. "
                             f"Got {bin_nb}")

        return None

    def validate_value_parameter(self, value: float | int, param_name: str = "value") -> None:
        """
        Check if the given value lies between the bins range
        :param value:
        :param param_name: for error logging purpose
        :raise TypeError: if value not a float or int
        :raise ValueError: if the given value is outside the range defined by the bins edges
        """
        if not isinstance(value, (float, int)):
            raise TypeError(f"int or float expected. Got {type(value)} instead.")

        # to avoid floating point weird behaviour when the value is close to the extreme values of the bins' edges
        if np.isclose(value, self.get_first_edge()) or np.isclose(value, self.get_last_edge()):
            return

        if value < self.get_first_edge() or value > self.get_last_edge():
            raise ValueError(
                f"The value of {param_name} must be between {self.get_first_edge():.3f} and {self.get_last_edge():.3f}")

        return None

    def center_bins(self) -> npt.NDArray[np.float64]:
        """
        Return the center of each bin.\n

        :return: array of size N-1
        """
        centered_bins = np.array(
            [(left_edge + right_edge) / 2 for (left_edge, right_edge) in pairwise(self.bins_edges)], dtype=np.float64
        )

        return centered_bins

    def find_bin(self, value: float | int) -> int:
        """
        Find the number of the bin containing the value. \n
        if out of range, raise ValueError

        b = Bins([1, 2, 3, 4])
        b.find_bin(1) -> 0
        b.find_bin(2) -> 1
        b.find_bin(2.7) -> 1
        b.find_bin(0.2) -> -1

        :param value:
        :return: the index of the bin
        """
        # self.validate_value_parameter(value=value)
        # if np.isclose(value, self.bins_edges[-1]):
        #     return self.nb_bins - 1
        # if np.isclose(value, self.bins_edges[0]):
        #     return 0
        # if value < self.get_first_edge():
        #     return -1
        # if value > self.get_last_edge():
        #     return self.nb_bins + 1
        self.validate_value_parameter(value)

        return int(np.searchsorted(self.bins_edges, value, side="right")) - 1

    def get_first_edge(self) -> float:
        return float(self.bins_edges[0])

    def get_last_edge(self) -> float:
        return float(self.bins_edges[-1])

    def get_bin_width(self, bin_nb: int) -> float:
        self.validate_bin_nb_parameter(bin_nb=bin_nb)

        return float(self.bins_widths[bin_nb])

    def get_bin_edges(self, x: float) -> tuple[float, float]:
        self.validate_value_parameter(value=x, param_name="x")
        bin_nb = self.find_bin(x)
        return float(self.bins_edges[bin_nb]), float(self.bins_edges[bin_nb + 1])

    def get_bin_center(self, x: float) -> float:
        self.validate_value_parameter(value=x, param_name="x")
        bin_nb = self.find_bin(x)
        return float(self._bins_centers[bin_nb])

    def rebin(self, n: int) -> Self:
        """
        Create a new Bins instance
        :param n: must divide the total number of bins
        :return:
        """
        if not isinstance(n, int):
            raise TypeError(f"n must be a int. Got {type(n)} instead.")
        if n <= 0:
            raise ValueError(f"n must be > 0. Got {n}")

        if (self.nb_bins % n) != 0:
            raise ValueError("n must be a divider of the number of bins")

        N = self.nb_bins // n + 1
        new_bins = np.zeros((N, ))

        for i in range(N):
            new_bins[i] = self.bins_edges[i * n]
        return Bins(new_bins)

