# from hypothesis import given, strategies as st
# from hypothesis.extra.numpy import arrays

import pytest

import numpy as np

from histograms.bins import Bins


class TestConstructor:
    def test_empty(self):
        with pytest.raises(ValueError):
            Bins([])

    def test_min_size(self):
        with pytest.raises(ValueError):
            Bins([1])

    def test_shape(self):
        with pytest.raises(ValueError):
            Bins(np.ones((2, 2)))

    def test_unordered(self):
        with pytest.raises(ValueError):
            Bins([1, 3, 2])

    def test_dtype(self):
        b = Bins(np.arange(11))
        assert b.bins_edges.dtype == np.float64


class TestMethods:
    def test_center_bins(self):
        b = Bins(np.arange(11))

        assert all(np.isclose(b.center_bins(), np.arange(0.5, 10, 1)))

    def test_find_bin(self):
        b = Bins(np.arange(1, 11, 1))
        with pytest.raises(ValueError):
            b.find_bin(0.5)
            b.find_bin(12.4)

        assert b.find_bin(2.2) == 1
        assert b.find_bin(1.) == 0
        assert b.find_bin(10.) == 9

    def test_bin_center(self):
        b = Bins(np.arange(1, 11, 1))

        # with pytest.raises(ValueError):
        #     b.get_bin_center(0.5)

        assert b.get_bin_center(1.1) == 1.5
        assert b.get_bin_center(9.8) == 9.5

    def test_rebin(self):
        b = Bins(np.arange(0, 11, 1))
        with pytest.raises(TypeError):
            b.rebin(2.)
        with pytest.raises(ValueError):
            b.rebin(-1)
            b.rebin(3)
        new_b = b.rebin(2)
        assert all(np.isclose(new_b.bins_edges, np.arange(0., 12, 2)))



