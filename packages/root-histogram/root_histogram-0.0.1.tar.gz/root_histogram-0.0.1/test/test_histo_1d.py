import pytest
import numpy as np

from src.histograms.histogram_1d import Histogram1d
from histograms.bins import Bins
from tools import data_checker as dc


class TestConstructor:

    default_bins = Bins([0, 1, 2, 3])

    def test_from_arrays(self):
        with pytest.raises(dc.ArraySizeError):
            Histogram1d.from_arrays(counts=np.array([0., 1.]), bins=[0, 1, 2, 3])

    def test_underflow_and_overflow_bin(self):
        h1 = Histogram1d.from_arrays(counts=np.array([2., 1., 0., 1., 5.]), bins=[0, 1, 2, 3])
        h2 = Histogram1d.from_arrays(counts=np.array([1., 0., 1.]), bins=[0, 1, 2, 3])
        assert h1.underflow_bin == 2.
        assert h1.overflow_bin == 5.
        assert h2.underflow_bin == 0.
        assert h2.overflow_bin == 0.


