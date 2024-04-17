# QDsim
QDsim stands for Quantum Dots simulator. It efficiently and quickly simulates charge stability diagrams for large quantum dot devices (even 100+ dots). 
It was developed to make the simulation process as quick and as user-friendly as possible.
It is based on the constant interaction model, therefore it does not account for the quantum mechanical effects of the dots,
but its simplicity allows for quick and efficient creation of datasets.

## Description

The package is composed of two main classes: `QDDevice` and `QDSimulator`.
The `QDDevice` class is used to create a quantum dot device, which can be either a pre-defined device or a custom device.
The `QDSimulator` class is used to set up the simulation environment and run the simulation.

The package is designed to be user-friendly and efficient, allowing for the simulation of charge stability diagrams for large quantum dot devices (even 100+ dots) in a matter of minutes.

In order to simulate the charge stability diagram of an (arbitrary) quantum dot device, just do the following:
1. Take advantage of a pre-defined device or create your own custom device via a  `QDDevice` object;
2. Set up the simulation environment (e.g. sensor locations, gates to be scanned, voltage ranges, etc.) via a `QDSimulator` object and run the simulation;
3. Save the data (and/or plots) and enjoy!

A practical example is shown below in the Usage section.

All the features available are described in the tutorial folder, in which you can find 4 different Jupyter notebooks, each with a step-by-step guide on how to use the package.
Each notebooks focuses on a different aspect of the package, from the creation of a custom device to the simulation of a charge stability diagram, with all its possible options and features.
We suggest to read them in order, as they are designed to be read sequentially, from the first to the last.
They were designed to reduce redundancy of information and to provide a clear and concise guide on how to fully take advantage of the package.

## Installation
 
This package was developed on Python 3.9.18, and the requirements are tested for this version.  It is recommended to use this version to avoid compatibility issues.

The package can be installed via pip by executing:

```bash
pip install qdsim
```
For the installation in development/editable mode, use the option -e.

In order to use the package, it is required to manually install either the [MOSEK](https://docs.mosek.com/latest/install/installation.html) solver (licensed, free for academics) or the [SCIP](https://scipopt.org/doc/html/INSTALL.php) solver (open source).
## Usage
Here is a quick example of how to use this project. Look at the tutorial folder for more examples and a step-by-step guide on how to use the package.

```python
from qdsim import QDDevice, QDSimulator

# Step 1: Create a quantum dot device
# use a pre-defined double dot device
qddevice = QDDevice() # Create a QDDevice object
qddevice.one_dimensional_dots_array(n_dots=2) # Create a 1D array of 2 quantum dots

# Step 2: Set up the simulator
qdsimulator = QDSimulator('Electrons')
# set the sensor location from which the charge stability diagram is measured
qdsimulator.set_sensor_locations([[2, 1]])
# Simulate the charge stability diagram
qdsimulator.simulate_charge_stability_diagram(
    qd_device=qddevice, v_range_x=[-5, 20], solver='MOSEK',
    v_range_y=[-5, 20], n_points_per_axis=60,
    scanning_gate_indexes=[0, 1])

# Step 3: Plot the charge stability diagram
qdsimulator.plot_charge_stability_diagrams()
```
<img style="float: right;" src="results/figures/DQD_current.png">

## Contributing
We welcome contributors and collaborators.
The person wanting to contribute can start by opening an issue and they will hear from us. 

## Authors and acknowledgment
Here is a list of authors who have contributed to this project:
- [Valentina Gualtieri](https://github.com/vgualtieri)
- Charles Renshaw-Whitman
- [Vinicius F. Hernandes](https://gitlab.com/vfhernandes)
- [Eliška Greplová](https://github.com/greplova)

We also want to thank Francesco Borsoi, Brennan Undseth, and Menno Veldhorst for their fruitful discussions and suggestions.

## License
This work is licensed under a [MIT License](https://opensource.org/licenses/MIT)

