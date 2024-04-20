from typing import Dict, Callable, Any

import numpy as np
import numpy.typing as npt

from scipy.special import erf, erfc  # type: ignore
from scipy.stats import norm, crystalball, moyal  # type: ignore


def linear_model(x: npt.ArrayLike, slope: float, offset: float):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return slope * x + offset


def gaussian(x: npt.ArrayLike, amplitude, mean, std) -> float:
    """

    :param x:
    :param amplitude:
    :param mean:
    :param std:
    :return:
    """
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return amplitude * norm.pdf(x, loc=mean, scale=std)


def gaussian_offset(x: npt.ArrayLike, amplitude: float, mean: float, std: float, offset: float) -> float:
    """

    :param x:
    :param amplitude:
    :param mean:
    :param std:
    :param offset:
    :return:
    """
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return amplitude * norm.pdf(x, loc=mean, scale=std) + offset


def gaussian_linear(x: npt.ArrayLike, amplitude: float, mean: float, std: float, slope: float, offset: float):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return gaussian(x, amplitude=amplitude, mean=mean, std=std) + linear_model(x, slope=slope, offset=offset)


def double_gaussian(x: npt.ArrayLike, mean_1, std_1, mean_2, std_2, amplitude, ratio):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return amplitude * (norm.pdf(x, loc=mean_1, scale=std_1) + ratio * norm.pdf(x, loc=mean_2, scale=std_2))


def EMGl(x: npt.ArrayLike, amp, mu, std, lam):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return amp * lam / 2 * np.exp(lam / 2 * (-2 * mu + lam * std * std - 4 / lam + 2 * x)) * erfc(
        (-mu + lam * std * std - 2 / lam + x) / (np.sqrt(2) * std))


def EMGr(x, amp, mu, std, lam):
    return amp * lam / 2 * np.exp(lam / 2 * (2 * mu + lam * std ** 2 - 2 * x)) * (
            1 - erf((mu + lam * std ** 2 - x) / (np.sqrt(2) * std)))


def CrystalBall(x: float | int, mean: float, std: float, amplitude: float, alpha: float, n: float):
    """
    https://en.wikipedia.org/wiki/Crystal_Ball_function

    :param x:
    :param amplitude: amplitude
    :param alpha:
    :param n: exponent
    :param mean: mean
    :param std: std
    :return:
    """

    A = pow((n / (abs(alpha))), n) * np.exp(-alpha * alpha / 2)
    B = n / abs(alpha) - abs(alpha)

    C = n / (abs(alpha) * (n - 1)) * np.exp(-alpha * alpha / 2)
    D = np.sqrt(np.pi / 2) * (1 + erf(abs(alpha) / np.sqrt(2.)))

    N = 1 / (std * (C + D))

    if (x - mean) / std > (-alpha):
        f = N * np.exp((-1) * (x - mean) ** 2 / (2 * std ** 2))
    else:
        f = N * A * pow((B - (x - mean) / std), -n)
    return amplitude * f


def ExpGaussExp(x: float | int, amplitude: float, mean: float, std: float, k_left: float, k_right: float):
    """

    :param amplitude:
    :param x:
    :param mean:
    :param std:
    :param k_left:
    :param k_right:
    :return:
    """

    x_c = (x - mean) / std

    if x_c < - k_left:
        f = np.exp(k_left * k_left / 2 + k_left * x_c)

    elif x_c > k_right:
        f = np.exp(k_right * k_right / 2 - k_right * x_c)

    else:
        f = np.exp(-0.5 * x_c ** 2)

    N1 = np.exp(-0.5 * (k_left ** 2)) * std / k_left
    N2 = (erf(k_right / np.sqrt(2)) + erf(k_left / np.sqrt(2))) * std * np.sqrt(2 * np.pi) / 2
    N3 = np.exp(-0.5 * (k_right ** 2)) * std / k_right
    N = N1 + N2 + N3

    return amplitude / N * f


def activation(x: npt.ArrayLike, shift: float = 0., width: float = 1.):
    """
    activation function based on hyperbolic tangent. The conversion factor is defined such that activation(-width) =
    0.01 and activation(1)=0.99. The total rise time (from 1% to 99%) is than 2*width.

    :param x:0
    :param shift:
    :param width: must be strictly positive
    :return:
    :raise ValueError: if width <= 0
    """
    # p = 0.05
    # conv_factor = 2 * abs(np.arctanh(2 * p - 1))  # based on the moment to get to 95 % of the height
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    conv_factor = 2.2975599250672945
    return 0.5 * (np.tanh((x - shift) * conv_factor / width) + 1)


def inhibition(x: npt.ArrayLike, shift=0., width=1.):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    if width <= 0:
        raise ValueError("Width must be strictly positive")
    return activation(x, shift=shift, width=-width)


def linear_model_with_activation(x, slope, offset, shift, width=1):
    """
    Match the behavior of
    y = slope * shift + offset  for x <= shift
    y = slope * x + offset for x > shift

    :param x:
    :param slope:
    :param offset:
    :param shift:
    :param width:
    :return:
    """
    return activation(x, shift, width=width) * slope * (x - shift) + offset + shift * slope


def linear_model_with_inhibition(x, slope, offset, shift, width=1.):
    """
    Match the behavior of y = slope * x + offset until x = shift where it is just y = offset
    :param x:
    :param slope:
    :param offset:
    :param shift: moment when the function starts to inhibate
    :param width:
    :return:
    """

    return inhibition(x, shift, width=width) * slope * (x - shift) + offset + shift * slope


def linear_model_with_activation_bis(x, slope, offset, shift, width=1):
    """
    Match the behavior of
        - y = 0  for x <= shift
        - y = slope * x + offset for x > shift

    :param x:
    :param slope:
    :param offset:
    :param shift:
    :param width:
    :return:
    """
    return activation(x, shift, width=width) * (slope * x + offset)


def linear_model_with_inhibition_bis(x, slope, offset, shift, width=1.):
    """
    Match the behavior of
        - y = slope * x + offset    for x <= shift
        - y = 0                     for x > shift
    With a smooth transition
    :param x:
    :param slope:
    :param offset:
    :param shift: moment when the function starts to inhibate
    :param width:
    :return:
    """

    return inhibition(x, shift, width=width) * (slope * x + offset)


def step_back(x, step_height: float, step_width: float = 1., shift: float = 0.):
    return step_height * inhibition(x, shift=shift, width=step_width)


def background3(x, slope_bp, offset_bp, slope_ap, offset_ap, center, delta, step_height):
    """

    :param x:
    :param slope_bp:
    :param offset_bp:
    :param slope_ap:
    :param offset_ap:
    :param center:
    :param delta:
    :param step_height:
    :return:
    """

    return linear_model_with_inhibition(x, slope=slope_bp, offset=offset_bp, shift=center - delta / 2, width=delta) + \
        linear_model_with_activation(x, slope=slope_ap, offset=offset_ap, shift=center + delta / 2, width=delta) + \
        step_back(x, step_height=step_height, step_width=delta, shift=center)


def double_linear_bg(x, slope_bp, offset_bp, slope_ap, offset_ap, center, delta):
    r_ap = slope_ap * center + offset_ap
    return linear_model_with_inhibition_bis(x, slope=slope_bp, offset=offset_bp - r_ap, shift=center - delta / 2,
                                            width=delta) + \
        linear_model_with_activation(x, slope=slope_ap, offset=offset_ap, shift=center + delta / 2, width=delta)


def G_SB3(x, amplitude, mean, std, offset, slope, step_width, step_height):
    return gaussian(x, amplitude=amplitude, mean=mean, std=std) \
        + step_back(x, shift=mean, step_width=step_width, step_height=step_height) \
        + linear_model(x, slope=slope, offset=offset)


def CB_SB(x, amplitude, mean, std, alpha, n, step_height, step_width, offset):
    return CrystalBall(x, amplitude=amplitude, alpha=alpha, n=n, mean=mean, std=std) \
        + step_back(x, shift=mean, step_height=step_height, step_width=step_width) \
        + offset


def CB_SB1(x, amplitude, mean, std, alpha, n, step_height, step_width, offset, slope):
    return CrystalBall(x, amplitude=amplitude, alpha=alpha, n=n, mean=mean, std=std) \
        + linear_model(x, slope=slope, offset=offset) \
        + step_back(x, shift=mean, step_width=step_width, step_height=step_height)


def CB_DL(x, amplitude, alpha, n, mean, std, slope_bp, offset_bp, slope_ap, offset_ap, delta):
    return CrystalBall(x, amplitude=amplitude, alpha=alpha, n=n, mean=mean, std=std) \
        + double_linear_bg(x, slope_bp=slope_bp, offset_bp=offset_bp, slope_ap=slope_ap, offset_ap=offset_ap,
                           center=mean, delta=delta)


def EGE_SB1(x, amplitude, mean, std, k_left, k_right, offset, slope, step_width, step_height):
    return ExpGaussExp(x, amplitude=amplitude, mean=mean, std=std, k_left=k_left, k_right=k_right) \
        + step_back(x, shift=mean, step_width=step_width, step_height=step_height) \
        + linear_model(x, slope=slope, offset=offset)


def EGE_SB(x, amplitude, mean, std, k_left, k_right, offset, step_width, step_height):
    return ExpGaussExp(x, amplitude=amplitude, mean=mean, std=std, k_left=k_left, k_right=k_right) \
        + step_back(x, shift=mean, step_width=step_width, step_height=step_height) \
        + offset


def EGE_DL(x, amplitude, mean, std, k_left, k_right, slope_bp, offset_bp, slope_ap, offset_ap, delta):
    return ExpGaussExp(x, amplitude=amplitude, mean=mean, std=std, k_left=k_left, k_right=k_right) \
        + double_linear_bg(x, slope_bp=slope_bp, offset_bp=offset_bp, slope_ap=slope_ap, offset_ap=offset_ap,
                           center=mean, delta=delta)


def Gd2_SB(x, mean_1, std_1, mean_2, std_2, amplitude, ratio, step_width, step_height, offset):
    return double_gaussian(x, mean_1, std_1, mean_2, std_2, amplitude, ratio) \
        + step_back(x, step_width=step_width, step_height=step_height, shift=(mean_1 + mean_2) / 2) \
        + offset


def Gd2_SB1(x, mean_1, std_1, mean_2, std_2, amplitude, ratio, step_width, step_height, offset, slope):
    return double_gaussian(x, mean_1, std_1, mean_2, std_2, amplitude, ratio) \
        + step_back(x, step_width=step_width, step_height=step_height, shift=(mean_1 + mean_2) / 2) \
        + linear_model(x, slope=slope, offset=offset)


def Gd2_DL(x, mean_1, std_1, mean_2, std_2, amplitude, ratio, slope_bp, offset_bp, slope_ap, offset_ap, delta):
    return double_gaussian(x, mean_1, std_1, mean_2, std_2, amplitude, ratio) \
        + double_linear_bg(x, slope_bp=slope_bp, offset_bp=offset_bp, slope_ap=slope_ap, offset_ap=offset_ap,
                           center=(mean_1 + mean_2) / 2, delta=delta)


def EMGl_SB(x, amplitude, mean, std, lam, step_width, step_height, offset):
    return EMGl(x, amplitude, mean, std, lam) + \
        step_back(x, step_width=step_width, step_height=step_height, shift=mean) \
        + offset


mapping_names: Dict[str, Callable[..., float]] = {
    "gauss": gaussian,
    "gauss0": gaussian_offset,
    "gauss1": gaussian_linear,
    "gauss_db": double_gaussian

}
