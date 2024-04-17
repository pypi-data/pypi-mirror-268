
import matplotlib.pyplot as plt

from ._noisefunctions import *


def plot_style():

    """
    Set the style of the plots.

    Returns:
        None
    """
    fig_size_dim = 8
    golden_ratio = (1 + np.sqrt(5)) / 2
    fig_size = (fig_size_dim, fig_size_dim / golden_ratio)
    font_size = 8
    dpi = 500

    params = {'figure.figsize': fig_size,
              'figure.dpi': dpi,
              'savefig.dpi': dpi,
              'font.size': font_size,
              'font.family': "Tahoma",
              'figure.titlesize': font_size,
              'legend.fontsize': font_size,
              'axes.labelsize': font_size,
              'axes.titlesize': font_size,
              'xtick.labelsize': font_size,
              'ytick.labelsize': font_size}

    plt.rcParams.update(params)


def generate_ticks_labels(voltage_range, n_ticks):
    """
    Generate the ticks labels for one axis with specific voltage_range the CSD plot.


    Args:
        voltage_range (list): voltage range of the axis (e.g. [-1, 1]), with [min_v, max_v]
        n_ticks (int): number of ticks to generate

    Returns:
        list: list of ticks values

    """

    if voltage_range[0] < 0 < voltage_range[1]:
        # If voltage_range spans zero, create ticks with both positive and negative values
        tick_values = np.linspace(voltage_range[0], voltage_range[1], n_ticks + 1)
    elif voltage_range[1] < 0:
        # If voltage_range is entirely negative, create negative ticks
        tick_values = np.linspace(voltage_range[0], voltage_range[1], n_ticks + 1)
    else:
        # If voltage_range is entirely positive, create positive ticks
        tick_values = np.linspace(voltage_range[0], voltage_range[1], n_ticks + 1)

    return tick_values


def plot_csd(physical_quantity_matrix, voltage_ranges, variable_gate_indices, cmapvalue, plot_title, gaussian_noise,
             white_noise, pink_noise, plot_potential, gaussian_noise_custom_params, white_noise_custom_params,
             pink_noise_custom_params, save_noisy_data_npy_to_filepath=None):

    """
    Plot the CSD map.

    Args:
        physical_quantity_matrix (np.array): The potential matrix to plot.
        voltage_ranges (list): The voltage range of the gates, expressed as [[v_min_x, v_max_x], [v_min_y, v_max_y]].
        variable_gate_indices (list): The indices of the gates that are varied, e.g. [0, 1] for the first two gates.
        cmapvalue (str): The colormap to use, e.g. 'viridis', 'jet', 'plasma', 'magma', 'inferno', 'cividis', 'Greys'.
        plot_title (str): The title of the plot.
        gaussian_noise (bool): If True, add Gaussian noise to the plot.
        white_noise (bool): If True, add white noise to the plot.
        pink_noise (bool): If True, add pink noise to the plot.
        plot_potential (bool): If True, plot the potential map. If False, plot the current map.
        gaussian_noise_custom_params (list): The parameters [avg, std_dev] of the gaussian noise to add
                    to the plot. If None, the default parameters are used.
        white_noise_custom_params (list): The parameters [min, max] of the white noise to add to the plot. If None,
                    the default parameters are used.
        pink_noise_custom_params (list): The parameters [f_max, amplitude_range] of the pink noise to add
                    to the plot. If None, the default parameters are used.

    Returns:
        matplotlib.figure.Figure: The figure object.

    """

    x_lims = voltage_ranges[0]
    y_lims = voltage_ranges[1]

    # Generate the ticks labels for both axes
    n_ticks = 5  # Number of ticks
    x_tick_values = generate_ticks_labels(x_lims, n_ticks)
    x_tick_labels = [str(np.round(tmp, 2)) for tmp in x_tick_values]
    x_tick_values = np.linspace(0, physical_quantity_matrix.shape[0], n_ticks + 1)

    y_tick_values = generate_ticks_labels(y_lims, n_ticks)
    y_tick_labels = [str(np.round(tmp, 2)) for tmp in y_tick_values]
    y_tick_values = np.linspace(0, physical_quantity_matrix.shape[1], n_ticks + 1)
    y_tick_labels = y_tick_labels[::-1]  # Invert the y_tick_labels because imshow inverts the y-axis

    # Generate the axis titles
    x_axis_title = "Gate {} Voltage (au)".format(variable_gate_indices[0])
    y_axis_title = "Gate {} Voltage (au)".format(variable_gate_indices[1])

    # Set the plot style
    plot_style()
    # Create the figure
    fig, ax = plt.subplots(figsize=(3.40457, 1.8), dpi=300)
    fig.subplots_adjust(bottom=0.2, top=0.95, left=0.125, right=0.885)

    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(0.5)
    ax.tick_params(width=0.5, which='both')
    ax.tick_params(length=2.5, which='major')
    ax.tick_params(length=1.5, which='minor')

    p_max = np.max(np.max(np.max(physical_quantity_matrix)))
    p_min = np.min(np.min(np.min(physical_quantity_matrix)))
    bar_range = (p_min, p_max)

    if plot_potential:
        bar_label = "Potential sensed (au)"

    else:
        bar_label = "Current Sensed (au)"

    # add noise
    if gaussian_noise:
        physical_quantity_matrix = add_gaussian_noise(physical_quantity_matrix, gaussian_noise_custom_params)

    if white_noise:
        physical_quantity_matrix = add_white_noise(physical_quantity_matrix, white_noise_custom_params)

    if pink_noise:
        physical_quantity_matrix = add_pink_noise(physical_quantity_matrix, pink_noise_custom_params)

    # Save the noisy data
    if save_noisy_data_npy_to_filepath is not None:
        np.save(save_noisy_data_npy_to_filepath, physical_quantity_matrix)

    im = ax.imshow(physical_quantity_matrix, cmap=cmapvalue, vmin=bar_range[0], vmax=bar_range[1])

    color_bar = plt.colorbar(im, ax=ax)
    color_bar.set_label(f"{bar_label}")
    ax.set_xticks(x_tick_values)
    ax.set_xticklabels(x_tick_labels, fontsize=8)
    ax.set_yticks(y_tick_values)
    ax.set_yticklabels(y_tick_labels, fontsize=8)
    ax.set_xlabel(x_axis_title, fontsize=8)
    ax.set_ylabel(y_axis_title, fontsize=8, labelpad=3)
    ax.set_title(f'CSD, {plot_title}', fontsize=8)

    return fig
