from pathlib import Path

import matplotlib.pyplot as plt  # type: ignore
# from matplotlib import colors
# import pandas as pd
# from attrs import define, field, validators

import numpy as np
import numpy.typing as npt

from scipy.interpolate import interp1d  # type: ignore
from scipy.integrate import quad  # type: ignore
from scipy.stats import rv_histogram, norm  # type: ignore
from scipy.optimize import curve_fit  # type: ignore

import uproot  # type: ignore

from typing import Self

from tools import data_checker as dc

from src.histograms.bins import Bins
from src.histograms.histogram_base import HistogramBase


class Histogram1d(HistogramBase):
    """
    Convention for numbering bins :
        bin = 0:         underflow bin,\n
        bin = 1:         first bin with low-edge xlow INCLUDED,\n
        bin = nb_bins:   last bin with upper-edge xup EXCLUDED,\n
        bin = nb_bins+1: overflow bin

        attributes:
         counts : counts corresponding to the bins edges
    """

    def __init__(self,
                 bins: Bins | npt.ArrayLike,
                 counts: npt.NDArray[np.float64],
                 bins_errors: npt.NDArray[np.float64] | None = None,
                 underflow_bin: float = 0., overflow_bin: float = 0.,):
        """
        if counts does not contain the overflow and underflow bin, their count is considered to be 0.
        :param bins: array of size n-1
        :param counts: array on size n or n+1
        :param bins_errors:
        """

        if not isinstance(counts, np.ndarray):
            raise TypeError(f"counts must be an np.ndarray. Got {type(counts)} instead.")

        if isinstance(bins, np.ndarray):
            bins = Bins(bins)
        if not isinstance(bins, Bins):
            raise TypeError(f"counts must be an np.ndarray. Got {type(bins)} instead.")

        self.counts = counts
        self.bins = bins
        self._validate_bins_and_counts_shape()

        if bins_errors is None:
            self.bins_errors = np.sqrt(self.counts)
        else:
            if dc.contains_negative(array=bins_errors):
                raise ValueError("Errors can not be negative.")
            self.bins_errors = bins_errors

        self._underflow_bin: float = float(underflow_bin)
        self._overflow_bin: float = float(overflow_bin)

    @property
    def underflow_bin(self) -> float:
        return self._underflow_bin

    @property
    def overflow_bin(self) -> float:
        return self._overflow_bin

    @property
    def all_counts(self) -> npt.NDArray[np.float64]:
        """
        counts with overflow and underflow bins content
        :return: view of the counts
        """
        return np.insert(self.counts, (0, self.counts.size), (self.underflow_bin, self.overflow_bin))

    @property
    def bins_centers(self):
        return self.bins.bins_centers

    @property
    def is_density(self) -> bool:
        return np.isclose((np.sum(self.counts * self.bins.bins_widths)), 1.)

    def __getitem__(self, item) -> float:
        self.bins.validate_bin_nb_parameter(item)
        return float(self.counts[item])

    @staticmethod
    def _add_value_start_and_end(counts: npt.NDArray[np.float64], value: float = 0.) -> npt.NDArray[np.float64]:
        n = counts.size
        counts = np.insert(counts, (0, n), value)
        return counts

    def _validate_bins_and_counts_shape(self) -> None:
        """
        Check that the number of counts is equal to the number of bins edges +/- 1
        :raise ValueError: if there is a mismatch with the sizes
        """
        nb_bins_expected = self.counts.size + 1
        if self.bins.bins_edges.size != nb_bins_expected:
            raise ValueError(f'Wrong shape for bins. {nb_bins_expected} expected but '
                             f'got {self.bins.bins_edges.size} instead.')
        return None

    @classmethod
    def from_arrays(cls, counts: npt.ArrayLike,
                    bins: npt.ArrayLike | tuple[npt.ArrayLike, ...],
                    bins_errors: npt.ArrayLike | None = None) -> Self:
        """

        :param counts:
        :type counts:
        :param bins:
        :type bins:
        :param bins_errors:
        :type bins_errors:
        :return:
        :rtype:
        """

        counts = np.array(counts, dtype=np.float64)
        if isinstance(bins, tuple):
            raise TypeError(f"Only one bins array is required.")

        dc.validate_counts(counts=counts, dim=1)
        bins = Bins(bins)

        return cls(counts=counts, bins=bins, bins_errors=bins_errors)

    @classmethod
    def from_data(cls, data: npt.ArrayLike, bins: npt.ArrayLike, density: bool = False) -> Self:
        """
        Compute the histogram directly from the data.
        :param data: Array-like. Must be one dimensional
        :param bins: If bins is an int, it defines the number of equal-width bins in the given range
        :param density: If True, the result is the value of the probability density function at the bin, normalized such
         that the integral over the range is 1.
        :return: an instance of Histogram1D
        """
        bins = np.array(bins)
        counts, bins = np.histogram(a=data, bins=bins, density=density)
        return cls(counts, bins)

    @classmethod
    def from_npz_file(cls, path_to_file: Path | str, files_name: list[str] | None = None) -> Self:
        """
        Instantiate a histogram from a npz file

        :param path_to_file:
        :param files_name: filenames for counts, bins. If None, the first array is taken for the counts
        :return: an instance of Histogram1d
        :raise FileNotFoundError: if the file is not found
        :raise ValueError: if the file's extension is not npz
        """

        path_to_file = dc.sanitize_file_path(path_to_file, extension='.npz')
        cls.check_file_size_limit(path_to_file)

        with np.load(str(path_to_file)) as data:
            if len(data.files) != 2:
                raise ValueError(f"Not enough files to unpack for file {path_to_file}")
            if files_name is None:
                counts_filename = data.files[0]
                bins_filename = data.files[1]
            else:
                if len(files_name) != 2:
                    raise ValueError(f"2 files name expected. Got {len(files_name)} instead.")
                counts_filename = files_name[0]
                bins_filename = files_name[1]

            counts, bins = data[counts_filename], data[bins_filename]

        return cls(counts=counts, bins=Bins(bins))

    @classmethod
    def from_rootfile(cls, path_to_file: Path | str, histo_name: str) -> Self:
        """

        :param path_to_file:
        :param histo_name:
        :return:
        """
        path_to_file = dc.sanitize_file_path(path_to_file, extension='.root')
        cls.check_file_size_limit(path_to_file)

        with uproot.open(path_to_file) as file:
            if histo_name not in file.keys() and (histo_name + ';1') not in file.keys():
                raise ValueError(f"Object '{histo_name}' not in the file.")
            histo_data = file.get(histo_name).to_numpy()
        if len(histo_data) != 2:
            raise ValueError(f"Not enough or too much data to unpack for {histo_name} in file {path_to_file}")
        counts, bins = histo_data[0], histo_data[1]

        return cls.from_arrays(counts, bins)

    def save(self, path: Path):
        raise NotImplementedError

    def draw(self, log_scale: bool = False, x_lim: tuple[float, float] | None = None,
             y_lim: tuple[float, float] | None = None,
             figsize: tuple[float, float] = (6, 4)) -> None:
        """

        :param log_scale:
        :param x_lim:
        :param y_lim:
        :param figsize:
        """
        plt.figure(figsize=figsize)

        if x_lim is None:
            x_min = self.bins.get_first_edge() - self.bins.get_bin_width(1)
            x_max = self.bins.get_last_edge() + self.bins.get_bin_width(self.bins.nb_bins)
        else:
            x_min, x_max = x_lim
        plt.xlim(x_min, x_max)
        if y_lim is not None:
            plt.ylim(*y_lim)
        if log_scale:
            plt.semilogy()

        plt.stairs(self.counts, edges=self.bins.bins_edges, linewidth=2)
        plt.grid(alpha=0.7)
        plt.show()

        return None

    def select(self, x_min: float, x_max: float):
        """

        :param x_min:
        :param x_max:
        :return: instance of Histogram1d
        """
        bin_x_min = self.bins.find_bin(x_min)
        bin_x_max = self.bins.find_bin(x_max)

        selected_counts = self.counts[bin_x_min: bin_x_max + 1]
        underflow_counts = self.counts[:bin_x_min].sum()
        overflow_counts = self.counts[bin_x_max + 1:].sum()
        nb_b = selected_counts.size
        # selected_counts = np.insert(selected_counts, (0, nb_b), (underflow_counts, overflow_counts))
        selected_bins = Bins(self.bins.bins_edges[bin_x_min - 1: bin_x_max + 1])

        return Histogram1d(selected_bins, selected_counts, overflow_bin=overflow_counts, underflow_bin=underflow_counts)

    def rebin(self, n: int):
        """
        TO DO : compute the error
        :param n:
        :return:
        """
        new_bins = self.bins.rebin(n=n)
        N = self.bins.nb_bins // n
        rebin_counts = np.zeros((N + 2,))
        rebin_counts[0] = self.underflow_bin
        rebin_counts[N + 1] = self.overflow_bin
        for i in range(N):
            rebin_counts[i + 1] = self.counts[i * n:(i + 1) * n].sum()

        return Histogram1d(new_bins, rebin_counts)

    def get_data(self, bins_position: str = 'center'):
        """
        For fitting purpose
        Return bin center and counts as (x, y)
        :param bins_position:
        :return:
        """
        if bins_position == 'center':
            return self.bins.bins_centers, self.counts, self.bins_errors
        else:
            return self.bins.bins_edges, self.counts, self.bins_errors
