import pyplnoise
import numpy as np


def add_gaussian_noise(physical_quantity_matrix, noise_params=None):

    """
    Add Gaussian noise to the physical quantity matrix.

    If no custom noise parameters are selected via the plot_charge_stability_diagram function, the default parameters
    are used. The default parameters are calculated as follows:
    - avg = 0
    - std_dev = 1/7 * max_value_of_physical_quantity_matrix

    Args:
        physical_quantity_matrix (np.array): The physical quantity matrix to which the noise is added.
        noise_params (list): The parameters [avg, std_dev] of the gaussian noise to add to the plot. If None, the
                    default parameters are used.

    Returns:
        np.array: The physical quantity matrix with added noise.

    """

    if noise_params is None:
        avg = 0
        std_dev = 0.14*np.max(np.max(physical_quantity_matrix))

    else:
        avg = noise_params[0]
        std_dev = noise_params[1]

    physical_quantity_matrix = physical_quantity_matrix + np.random.normal(avg, std_dev, physical_quantity_matrix.shape)
    return physical_quantity_matrix


def add_white_noise(physical_quantity_matrix, noise_params=None):
    """
    Add white noise to the physical quantity matrix.

    If no custom noise parameters [min_value, max_value] are selected via the plot_charge_stability_diagram function,
    the default parameters are used. The default parameters are calculated as follows:

    - min_value = -0.06 * max_value_of_physical_quantity_matrix
    - max_value = 0.06 * max_value_of_physical_quantity_matrix

    Args:
        physical_quantity_matrix (np.array): The physical quantity matrix to which the noise is added.
        noise_params (list): The parameters [min_value, max_value] of the white noise to add to the plot. If None, the
                    default parameters are used.

    Returns:
        np.array: The physical quantity matrix with added noise.

    """

    if noise_params is None:
        min_value = -0.06 * np.max(np.max(physical_quantity_matrix))
        max_value = 0.06 * np.max(np.max(physical_quantity_matrix))
    else:
        min_value = noise_params[0]
        max_value = noise_params[1]

    physical_quantity_matrix = physical_quantity_matrix + np.random.uniform(min_value, max_value,
                                                                            physical_quantity_matrix.shape)
    return physical_quantity_matrix


def add_pink_noise(physical_quantity_matrix, noise_params=None):
    """
    Add pink noise to the physical quantity matrix.

    The pink noise is generated via the pyplnoise package. If no custom noise parameters [f_max, amplitude_range] are
    selected via the plot_charge_stability_diagram function, the default parameters are used. The default parameters
    are the followings:
    - f_max = 10000
    - amplitude_range = 2

    Args:
        physical_quantity_matrix (np.array): The physical quantity matrix to which the noise is added.
        noise_params (list): The parameters [f_max, amplitude_range] of the pink noise to add to the plot. If None, the
                    default parameters are used.

    Returns:
        np.array: The physical quantity matrix with added noise.

    """

    if noise_params is None:
        f_max = 10000
        desired_amplitude_range = 2  # establish the desired amplitude range, the higher, the stronger the noise
    else:
        f_max = noise_params[0]
        desired_amplitude_range = noise_params[1]

    pk_noise = pyplnoise.PinkNoise(f_max * 2, f_max / 2, f_max)
    pink_noise_signal = pk_noise.get_series(physical_quantity_matrix.shape[0] * physical_quantity_matrix.shape[1])
    pink_noise_signal = desired_amplitude_range * (pink_noise_signal - np.min(pink_noise_signal)) / (
            np.max(pink_noise_signal) - np.min(pink_noise_signal)) - (desired_amplitude_range / 2)

    pink_noise_signal = np.reshape(pink_noise_signal, physical_quantity_matrix.shape)
    physical_quantity_matrix = physical_quantity_matrix + pink_noise_signal

    return physical_quantity_matrix
