from pathlib import Path

import pandas as pd  # type: ignore
import numpy as np
import numpy.typing as npt
import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import uproot

from typing import Tuple, Any, Self

from src.tools import data_checker as dc

from src.histograms.bins import Bins
from src.histograms.histogram_base import HistogramBase


class Histogram2d(HistogramBase):
    """
    Works as a wrapper around three numpy arrays representing the counts and the bins of a 2d histogram.
    Counts must be given with an ij orientation (i correspond to the first coordinate of the array and j the second)
    """

    def __init__(self, counts: npt.NDArray[np.float64],
                 bins_x: Bins, bins_y: Bins | None,
                 errors: npt.NDArray[np.float64] | None = None):
        """

        :param counts:
        :param bins_x:
        :param bins_y:
        :param errors:
        """

        dc.validate_counts(counts, dim=2)
        dc.validate_bins_and_counts_shape(counts=counts, bins=bins_x.bins_edges, axis=0)
        dc.validate_bins_and_counts_shape(counts=counts, bins=bins_y.bins_edges, axis=1)

        self.counts: npt.NDArray[np.float64] = counts
        self.bins_x: Bins = bins_x

        # self._underflow_bins_x = counts[0]
        # self._overflow_bins_x = counts[-1]
        # self._underflow_bins_y = counts[:, 0]
        # self._overflow_bins_y = counts[:, -1]

        if bins_y is None:
            self.bins_y: Bins = bins_x
        else:
            self.bins_y: Bins = bins_y
        if errors is None:
            self.errors = np.sqrt(self.counts)
        else:
            if dc.contains_negative(array=errors):
                raise ValueError("Errors can not be negative.")
            self.errors = errors

    # @property
    # def underflow_bins_x(self) -> npt.NDArray[np.float64]:
    #     return self._underflow_bins_x
    #
    # @property
    # def underflow_bins_y(self) -> npt.NDArray[np.float64]:
    #     return self._underflow_bins_y
    #
    # @property
    # def overflow_bins_x(self) -> npt.NDArray[np.float64]:
    #     return self._overflow_bins_x
    #
    # @property
    # def overflow_bins_y(self) -> npt.NDArray[np.float64]:
    #     return self._overflow_bins_y


    # def counts_in_range(self):
    #     """
    #     counts without overflow and underflow bins content
    #     :return: view of the counts
    #     """
    #     return self.counts[1:-1, 1:-1]


    @property
    def bins_centers_x(self):
        return self.bins_x.bins_centers

    @property
    def bins_centers_y(self):
        return self.bins_y.bins_centers

    @property
    def nb_bins_x(self):
        return self.bins_x.nb_bins

    @property
    def nb_bins_y(self):
        return self.bins_y.nb_bins

    @property
    def is_density(self) -> bool:
        return np.isclose((np.sum(self.counts * self.get_areas())), 1.)

    @property
    def bins_widths_x(self):
        return self.bins_x.bins_widths

    @property
    def bins_widths_y(self):
        return self.bins_y.bins_widths

    @staticmethod
    def _add_padding(counts: npt.NDArray[np.float64], value: float = 0.) -> npt.NDArray[np.float64]:
        with_pad = np.pad(counts, pad_width=1, constant_values=value)
        # n_x, n_y = counts.shape
        # with_pad = value * np.ones((n_x+2, n_y+2))
        # with_pad[1:-1, 1:-1] = counts
        return with_pad

    # def _validate_bins_and_counts_shape(self) -> None:
    #
    #     if (self.bins_x.bins_edges.size + 1) != self.counts.shape[0]:
    #         raise ValueError(f'Wrong shape for X-bins. {self.counts.shape[0]} expected.')
    #
    #     if (self.bins_y.bins_edges.size + 1) != self.counts.shape[1]:
    #         raise ValueError(f'Wrong shape for Y bins. {self.counts.shape[1]} expected.')
    #     return None

    @classmethod
    def from_arrays(cls, counts: npt.ArrayLike,
                    bins: npt.ArrayLike | tuple[npt.ArrayLike, ...],
                    bins_errors: npt.ArrayLike | None = None):

        raise NotImplementedError()

    @classmethod
    def from_npz_file(cls, path_to_file: Path | str, files_name: tuple[str, ...] | None = None) -> Self:
        """
        Instantiate a histogram from a npz file
        :param path_to_file:
        :param files_name: in order for counts, bins_X, and bins_Y
        :return:
        """

        path_to_file = dc.sanitize_file_path(path_to_file, extension='.npz')
        cls.check_file_size_limit(path_to_file)

        with np.load(str(path_to_file)) as data:
            if len(data.files) != 3:
                raise ValueError(f"Not enough files to unpack for file {path_to_file}")
            if files_name is None:
                counts_filename = data.files[0]
                bins_x_filename = data.files[1]
                bins_y_filename = data.files[2]
            else:
                if len(files_name) != 3:
                    raise ValueError(f"3 files name expected. Got {len(files_name)} instead.")
                counts_filename = files_name[0]
                bins_x_filename = files_name[1]
                bins_y_filename = files_name[2]
            counts, bins_x, bin_y = data[counts_filename], data[bins_x_filename], data[bins_y_filename]

        return cls(counts=counts, bins_x=Bins(bins_x), bins_y=Bins(bin_y))

    @classmethod
    def from_data(cls, data, bins, density: bool = False) -> Self:
        """

        :param data:
        :param bins:
        :param density:
        :return:
        """
        data_x, data_y = data
        counts, bins_x, bins_y = np.histogram2d(x=data_x, y=data_y, bins=bins, density=density)
        return cls(counts, Bins(bins_x), Bins(bins_y))

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
                raise ValueError(f"Object {histo_name} not in the file.")
            matrix_data = file.get(histo_name).to_numpy()

        if len(matrix_data) != 3:
            raise ValueError(f"Not enough or too much data to unpack for {histo_name} in file {path_to_file}")

        counts, bins_x, bins_y = matrix_data
        # counts = cls._add_padding(counts)
        return cls(counts, Bins(bins_x), Bins(bins_y))

    def save(self, path: Path) -> None:
        """
        Save as npz file. Keys are : counts, bins_x, bins_y
        :param path:
        :raise ValueError: incorrect extension
        :raise FileNotFoundError:
        """
        file_extension = '.npz'
        if path.suffix == '':
            path = Path(str(path) + file_extension)
        if path.suffix != '.npz':
            raise ValueError(f'File extension is incorrect. "{file_extension}" expected got {path.suffix}')

        if not path.parent.exists():
            raise FileNotFoundError(f'{path.parent} not found.')

        with open(path, 'wb') as f:
            np.savez(f, counts=self.counts, bins_x=self.bins_x.bins_edges, bins_y=self.bins_y.bins_edges)

        return None

    def normalize_counts(self, log: bool = False):
        """
        In place transformation. The counts are divided by the total number of counts
        :return:
        :rtype:
        """
        if log:
            self.counts = np.log10(self.counts / self.counts.sum())
        else:
            self.counts = self.counts / self.counts.sum()
        return None

    def get_max_position(self) -> Tuple[Any, Any]:
        bins_peak = np.unravel_index(self.counts.argmax(), self.counts.shape)
        return self.bins_centers_x[bins_peak[0]], self.bins_centers_y[bins_peak[1]]

    def slice_horizontally(self, y_slice: float, delta_y: float | int = 0) -> np.ndarray:
        """
        Slice the histogram along x-axis at the y coordinate given.
        :param y_slice:
        :param delta_y:
        :return: 1d array with the counts of the slice
        """
        # self.bins_Y.validate_value_parameter(value=y_slice, param_name="y_slice")
        if delta_y > 0:
            row_index_inf = self.bins_y.find_bin(value=y_slice - delta_y) - 1
            row_index_sup = self.bins_y.find_bin(value=y_slice + delta_y)
            return self.counts[:, row_index_inf:row_index_sup].sum(axis=1)[1:-1]
        row_index = self.bins_y.find_bin(value=y_slice) - 1
        return self.counts[:, row_index][1:-1]

    def slice_vertically(self, x_slice: float, delta_x: float | int = 0) -> np.ndarray:
        # self.bins_X.validate_value_parameter(value=x_slice, param_name="x_slice")
        if delta_x > 0:
            col_index_sup = self.bins_y.find_bin(value=x_slice + delta_x)
            col_index_inf = self.bins_y.find_bin(value=x_slice - delta_x) - 1
            return self.counts[col_index_inf:col_index_sup].sum(axis=0)[1:-1]
        col_index = self.bins_x.find_bin(value=x_slice) - 1
        return self.counts[col_index][1:-1]

    def slice_horizontally_bin(self, bin_y: int) -> np.ndarray:
        """
        Slice the histogram along x-axis at the y bin given
        Negative value are allowed (reverse order)
        :param bin_y:
        :return:
        """
        self.bins_y.validate_bin_nb_parameter(bin_nb=bin_y, param_name="bin_y")
        return self.counts[:, bin_y][1:-1]

    def slice_vertically_bin(self, bin_x: int) -> np.ndarray:
        self.bins_x.validate_bin_nb_parameter(bin_nb=bin_x, param_name="bin_x")
        return self.counts[bin_x][1:-1]

    def diagonal_slice(self, starting_point_x: float, starting_point_y: float) \
            -> Tuple[np.ndarray, np.ndarray, np.ndarray]:

        self.bins_x.validate_value_parameter(value=starting_point_x, param_name="starting_point_x")
        self.bins_x.validate_value_parameter(value=starting_point_y, param_name="starting_point_y")

        starting_i = self.bins_x.find_bin(value=starting_point_x)
        starting_j = self.bins_y.find_bin(value=starting_point_y)

        nb_bins = min(self.nb_bins_x - starting_i, self.nb_bins_y - starting_j)
        # reversed_Y = self.Y[::-1]

        return np.array([self.counts[starting_i + i][starting_j + i] for i in range(nb_bins)]), \
            self.bins_centers_x[starting_j:], self.bins_centers_y[starting_i:]

    def get_bin_content(self, x: float, y: float) -> float:
        """

        :param x:
        :param y:
        :return:
        """
        bin_x = self.bins_x.find_bin(value=x)
        bin_y = self.bins_y.find_bin(value=y)

        return float(self.counts[bin_x, bin_y])

    def get_default_bins_error(self):
        """
        return Poisson's error : for a bin with content b, err(b) = sqrt(b)
        :return:
        :rtype:
        """
        return np.sqrt(self.counts)

    def get_areas(self):
        n_1 = self.bins_widths_x.size
        n_2 = self.bins_widths_y.size
        return self.bins_widths_x.reshape((n_1, 1)) @ self.bins_widths_y.reshape((1, n_2))

    def get_area(self, bin_x: int, bin_y: int) -> float:
        self.bins_x.validate_bin_nb_parameter(bin_nb=bin_x, param_name="bin_x")
        self.bins_y.validate_bin_nb_parameter(bin_nb=bin_y, param_name="bin_y")

        return float(self.bins_widths_x[bin_x-1] * self.bins_widths_y[bin_y-1])

    # def to_DataFrame(self, col_names: Iterable[str] | None = None) -> pd.DataFrame:
    #     """
    #     Convert the matrix in a DataFrame where the columns are 'X', 'Y', and 'counts'.
    #     """
    #     if col_names is None:
    #         col_names = ['X', 'Y', 'counts']
    #     file = StringIO()
    #     file.read()
    #     for (x, y), c in zip(product(self.X, self.Y), self.counts.flatten()):
    #         file.write(f'{x}, {y}, {c}\n')
    #     file.seek(0)
    #
    #     df = pd.read_csv(file, names=col_names)
    #
    #     return df

    def project_X(self, first_ybin: int = 0, last_ybin: int = -1):
        self.bins_y.validate_bin_nb_parameter(bin_nb=first_ybin)
        self.bins_y.validate_bin_nb_parameter(bin_nb=last_ybin)

        if last_ybin == -1:
            sl = slice(first_ybin, self.nb_bins_y)
        else:
            sl = slice(first_ybin, last_ybin)
        proj = np.array([col[sl].sum() for col in self.counts.T])

        return proj

    def project_Y(self, first_xbin: int = 1, last_xbin: int = -1):
        self.bins_x.validate_bin_nb_parameter(bin_nb=first_xbin)
        self.bins_x.validate_bin_nb_parameter(bin_nb=last_xbin)
        if last_xbin == -1:
            sl = slice(first_xbin, self.nb_bins_x)
        else:
            sl = slice(first_xbin, last_xbin)
        proj = np.array([row[sl].sum() for row in self.counts])

        return proj

    def draw(self, log_scale: bool = False, orientation: str = 'xy', x_label: str = 'x', y_label: str = 'y') -> None:

        plt.figure(figsize=(7, 6))
        ax = plt.gca()
        if orientation == 'xy':
            x_min, x_max = self.bins_x.get_first_edge(), self.bins_x.get_last_edge()
            y_min, y_max = self.bins_y.get_first_edge(), self.bins_y.get_last_edge()
            extent = [x_min, x_max, y_min, y_max]
            mat = np.rot90(self.counts)
            # x_label, y_label = 'X', 'Y'
        else:
            extent = [self.bins_centers_y[0], self.bins_centers_y[-1], self.bins_centers_x[-1], self.bins_centers_x[0]]
            mat = self.counts
            x_label, y_label = 'i', 'j'
            ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

        plt.xlabel(x_label, fontweight="bold")
        plt.ylabel(y_label, fontweight="bold")

        if log_scale:
            plt.imshow(mat, norm=matplotlib.colors.LogNorm(), extent=extent)
        else:
            plt.imshow(mat, extent=extent)
        ax.set_aspect('auto')
        plt.colorbar()
        plt.show()

        return None

    def find_bin(self, x: float, y: float) -> Tuple[int, int]:
        bin_x = self.bins_x.find_bin(x)
        bin_y = self.bins_y.find_bin(y)

        return bin_x, bin_y

    def interpolate(self, x: float, y: float) -> float:
        """
        TO DO: check if its working
        :param x:
        :type x:
        :param y:
        :type y:
        :return:
        :rtype:
        """
        raise NotImplementedError

        # self.bins_X.validate_value_parameter(value=x, param_name="x")
        # self.bins_Y.validate_value_parameter(value=y, param_name="y")
        #
        # # interp = RegularGridInterpolator((self.bins_X.center_bins(), self.bins_Y.center_bins()),
        # #                                  self.counts, method='linear', bounds_error=False)
        #
        # return float(self._interp((x, y)))

    def select(self, x: float, y: float, dx: float, dy: float):
        """
        Given a point (x, y), return the selected histogram from [x, y] to [x+dx, y+dy]
        :param x:
        :type x:
        :param y:
        :type y:
        :param dx:
        :type dx:
        :param dy:
        :type dy:
        :return: an instance of Histogram_2D
        """
        x_min, x_max = x, x + dx
        y_min, y_max = y, y + dy

        bin_x_min, bin_y_min = self.find_bin(x_min, y_min)
        bin_x_max, bin_y_max = self.find_bin(x_max, y_max)

        selected_counts = self.counts[bin_x_min: bin_x_max+1, bin_y_min:bin_y_max+1]
        selected_counts = self._add_padding(selected_counts, 0)
        selected_bins_x = Bins(self.bins_x.bins_edges[bin_x_min - 1: bin_x_max + 1])
        selected_bins_y = Bins(self.bins_y.bins_edges[bin_y_min - 1: bin_y_max + 1])

        return Histogram2d(selected_counts, selected_bins_x, selected_bins_y)
