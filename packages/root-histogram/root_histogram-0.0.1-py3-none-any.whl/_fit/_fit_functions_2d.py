import numpy as np

from scipy.special import erf, erfc
from scipy.stats import norm

from typing import Union
import _fit_function_1d as ff1d


def gauss_2d(x: Union[float, np.ndarray], y: Union[float, np.ndarray], amplitude: float,
             mean_x: float, std_x: float, mean_y: float, std_y: float) -> Union[float, np.ndarray]:
    A_r = amplitude / (np.pi * std_x * std_y)
    g1 = np.exp(-np.power((x - mean_x) / std_x, 2))
    g2 = np.exp(-np.power((y-mean_y)/std_y, 2))

    return A_r * g1 * g2


def gauss_2d_theta(x, y, m1, s1, m2, s2, theta):
    a = np.cos(theta) ** 2 / (2 * s1 ** 2) + np.sin(theta) ** 2 / (2 * s2 ** 2)
    b = -np.sin(2 * theta) / (4 * s1 ** 2) + np.sin(2 * theta) / (4 * s2 ** 2)
    c = np.sin(theta) ** 2 / (2 * s1 ** 2) + np.cos(theta) ** 2 / (2 * s2 ** 2)

    return 1 / (2 * np.pi * s1 * s2) * np.exp(-(a * (x - m1) ** 2 + 2 * b * (x - m1) * (y - m2) + c * (y - m2) ** 2))


def vertical_gaussian(x, y, amplitude, mean, std):
    return amplitude / std * norm.pdf((x - mean) / std)


def horizontal_gaussian(x, y, amplitude, mean, std):
    return amplitude / std * norm.pdf((y - mean) / std)


def diagonal_gaussian(x, y, amplitude, mean, std):
    return amplitude / std * norm.pdf((x + y - mean) / std)


def vertical_step_back(x, y, mean_y, step_height, step_width):
    return step_height * ff1d.inhibition(y, shift=mean_y, width=step_width)


def horizontal_step_back(x, y, mean_x, step_height, step_width):
    return step_height * ff1d.inhibition(x, shift=mean_x, width=step_width)


def vertical_gaussian_bg_SB(x, y, amplitude, mean_x, mean_y, std, step_width, step_height):

    pi = np.pi
    Ar = amplitude / (np.sqrt(2. * pi) * std)
    x_c = (x - mean_x) / std

    return (Ar - step_height * ff1d.activation(y, shift=mean_y, width=step_width)) * np.exp(-0.5 * x_c * x_c)


def horizontal_gaussian_bg_SB(x, y, amplitude, mean_x, mean_y, std, step_width, step_height):

    pi = np.pi
    Ar = amplitude / (np.sqrt(2. * pi) * std)
    y_c = (y - mean_y) / std

    return (Ar - step_height * ff1d.activation(x, shift=mean_x, width=step_width)) * np.exp(-0.5 * y_c * y_c)


def exp_gauss_exp_2d(x, y, mu_x, sigma_x, K_l_x, K_r_x, mu_y, sigma_y, K_l_y, K_r_y):
    x_c = (x - mu_x) / sigma_x
    y_c = (y - mu_y) / sigma_y

    if x_c < - K_l_x:
        f_x = np.exp((K_l_x ** 2) / 2 + K_l_x * x_c)
    elif x_c > K_r_x:
        f_x = np.exp((K_r_x ** 2) / 2 - K_r_x * x_c)
    else:
        f_x = np.exp(-0.5 * x_c ** 2)

    if y_c < - K_l_y:
        f_y = np.exp((K_l_y ** 2) / 2 + K_l_y * y_c)
    elif y_c > K_r_y:
        f_y = np.exp((K_r_y ** 2) / 2 - K_r_y * y_c)
    else:
        f_y = np.exp(-0.5 * y_c ** 2)

    f = f_x * f_y

    return f




