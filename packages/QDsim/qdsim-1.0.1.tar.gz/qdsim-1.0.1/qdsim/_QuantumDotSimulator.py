"""
@author: VGualtieri

"""
from ._CapacitanceQDArray import CapacitanceQuantumDotArray
from ._QuantumDotDevice import QDDevice
import tqdm
from ._plotCSD import *  # for plotting
import matplotlib.pyplot as plt
from ._auxiliaryfunctions import *
import copy
import json
import os
from datetime import datetime

from itertools import combinations


class QDSimulator:
    """
    Class for simulating the charge stability diagram of a quantum dot array, in the constant interaction model.

    This class is used to simulate the charge stability diagram of a quantum dot array, in the constant interaction
    model. It is based on the `CapacitanceQuantumDotArray` class, which is used to create the maxwell capacitance
    matrices of the quantum dot array. The `QDSimulator` class is used to run the simulation and generate the
    charge stability diagram. It also includes methods to plot the charge stability diagram and the physical
    array of the quantum dot device.

    Args:
       simulate (str) : The type of simulation to run. Supported values are 'Electrons' and 'Holes'.
                Defaults to 'Electrons'.

    Attributes:
        _qd_device (QDDevice): The `QDDevice` object to be simulated.
        _physics_to_be_simulated (str): The type of simulation to run. Supported values are 'Electrons' and 'Holes'.
        _num_voltage_per_axis (int): The number of points to probe on the _x- and y-axis.
        _num_probe_points (int): The total number of points to probe in the voltage space.
        _voltage_array (np.array): The array containing the coordinates to probe in the voltage space.
        _occupation_array (np.array): The array containing the occupation state at each point in the voltage space.
        _energy_array (np.array): The array containing the energy at each point in the voltage space.
        _time_list (list): The list containing the timestamps of each run for the simulator chose, useful to do some
                benchmarking/speed comparison.
        _variable_gate_index_1 (int): The index of the first variable gate.
        _variable_gate_index_2 (int): The index of the second variable gate.
        _voltage_ranges (list): The minimum and maximum voltages to probe on the x- and y-axis. E.g.
                [[v_min_x, v_max_x], [v_min_y, v_max_y]].
        _gate_voltages (list): The list containing the voltages to apply to each gate. The variable gates are set to
                None values.
        _potential_array (np.array): The array containing the potential sensed by each sensor at each point in the
                voltage space.
        _current_array (np.array): The array containing the current sensed by each sensor at each point in the voltage
                space. It is obtained from the `_potential_array` attribute.
        _sensor_locations (list): The list containing the coordinates (x,y) of each sensor.
        _num_sensors (int): The number of sensors.
        _system_maxwell_matrix (np.array): The maxwell capacitance matrix of the quantum dot device (whole system).
    """

    def __init__(self, simulate='Electrons'):
        self._qd_device = QDDevice()

        if simulate in ['Electrons', 'Holes']:
            self._physics_to_be_simulated = simulate
        else:
            raise ValueError("Invalid value for 'simulate'. It must be 'Electrons' or 'Holes'.")

        self._variable_gate_index_1 = None
        self._variable_gate_index_2 = None
        self._voltage_ranges = None
        self._gate_voltages = None

        #self._num_sensors = None
        self._sensor_locations = None

        self._num_voltage_per_axis = None
        self._num_probe_points = None
        self._voltage_array = None
        self._voltage_occupation_data = None

        self._occupation_array = None
        self._energy_array = None
        self._time_list = None

        self._potential_array = None
        self._current_array = None

        self._system_maxwell_matrix = None

    def simulate_polytopes(self, quantum_dot_device, solver, v_range, num_points_per_axis, v_ranges=None, use_ray=True):
        """
        Simulate the polytopes of the quantum dot array.

        Args:
            quantum_dot_device:
            solver:
            v_range:
            num_points_per_axis:
            v_ranges:

        Returns:

        """
        # prepare the simulation
        self._qd_device = quantum_dot_device
        self._num_voltage_per_axis = num_points_per_axis
        self._num_probe_points = self._num_voltage_per_axis ** self.qd_device.num_gates  # plot resolution

        if v_ranges is None:
            self._voltage_ranges = [v_range] * self.qd_device.num_gates
        else:
            self._voltage_ranges = v_ranges

        self._voltage_ranges = [v_range] * self.qd_device.num_gates
        self._voltage_array = generate_linspace_arrays(self._voltage_ranges, self._num_voltage_per_axis)

        # Create the CapacitanceQuantumDotArray object and select the solver
        my_qd_arr = CapacitanceQuantumDotArray(simulate=self._physics_to_be_simulated)
        my_qd_arr.select_solver(solver)

        # This is the main "simulate" command, and the two vars on the left are the results, plus the time
        self._occupation_array, self._energy_array, self._time_list = my_qd_arr.probe_voltage_space(self,
                                                                                                    use_ray=use_ray)
        # Store the system maxwell matrix just for ease of use, in case I want to check it
        self._system_maxwell_matrix = my_qd_arr.system_maxwell_matrix

    def save_to_json(self, json_file_path, extra_attr_to_save=None):

        """
        Save the simulation and quantum dot device setup to a JSON file.

        The use of the .json extension is suggested. It saves some of the attributes of the calling object to a JSON
        file. The attributes saved by default are:

            - `_qd_device`
            - `_physics_to_be_simulated`
            - `_num_voltage_per_axis`
            - `_num_probe_points`
            - `_variable_gate_index_1`
            - `_variable_gate_index_2`
            - `_voltage_ranges`
            - `_gate_voltages`
            - `_sensor_locations`
            - `_num_sensors`

        If the user wants to save additional attributes, they can be specified via the `extra_attr_to_save` argument.

        Args:
            json_file_path (str): The path, name and extension of the JSON file to save the simulation setup to.
            extra_attr_to_save (list, optional): The list of additional attributes to save to the JSON file. If None,
                    no additional attributes are saved. Defaults to None.

        Returns:
            None

        """

        attributes = vars(self._qd_device)

        # Create the dictionary with the specified structure
        qd_device_dic = {
            "_qd_device": {
                "_device_type": self.qd_device.device_type,
                "_num_dots": self.qd_device.num_dots,
                "_num_gates": self.qd_device.num_gates,
                "_c0": self.qd_device.c0,
                "_physical_dot_locations": self.qd_device.physical_dot_locations,
                # "_physical_gate_locations": self.qd_device_physical_gate_locations,
                "_dot_dot_mutual_capacitance_matrix": self.qd_device.dot_dot_mutual_capacitance_matrix.tolist(),
                "_dot_gate_mutual_capacitance_matrix": self.qd_device.dot_gate_mutual_capacitance_matrix.tolist()
            }}

        basic_object_dict = {
            "_physics_to_be_simulated": self._physics_to_be_simulated,
            "_num_voltage_per_axis": self._num_voltage_per_axis,
            "_num_probe_points": self._num_probe_points,
            "_variable_gate_index_1": self._variable_gate_index_1,
            "_variable_gate_index_2": self._variable_gate_index_2,
            "_voltage_ranges": self._voltage_ranges,
            "_gate_voltages": self._gate_voltages,
            "_sensor_locations": self._sensor_locations,
            # "_num_sensors": self._num_sensors,
            "_system_maxwell_matrix": self._system_maxwell_matrix.tolist() if self._system_maxwell_matrix is not None else "None"
        }

        qd_device_dic.update(basic_object_dict)

        if extra_attr_to_save is not None:
            qd_device_dic.update(self._get_attributes_as_dict(extra_attr_to_save))

        with open(json_file_path, "w") as json_file:
            json.dump(qd_device_dic, json_file, indent=4)

    def load_from_json(self, json_file_path):
        """
        Update the QDSimulator attributes from a JSON file.

        This method updates the attributes of the `QDSimulator` object from a JSON file. The JSON file must have been
        generated by the `save_to_json` method.
        The attributes loaded by default are:

            - `_qd_device`
            - `_physics_to_be_simulated`
            - `_num_voltage_per_axis`
            - `_num_probe_points`
            - `_variable_gate_index_1`
            - `_variable_gate_index_2`
            - `_voltage_ranges`
            - `_gate_voltages`
            - `_sensor_locations`
            - `_num_sensors`


        Args:
            json_file_path (str): The path, name, and extension of the JSON file to load the simulation setup from.
        """
        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"File not found: {json_file_path}")

        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        for key, value in data.items():
            if hasattr(self, key):
                if key in ["_voltage_array", "_occupation_array", "_energy_array", "_potential_array",
                           "_current_array", "_system_maxwell_matrix"] and isinstance(value, list):
                    setattr(self, key, np.array(value))
                elif key == "_qd_device":
                    # Ensure QDDevice.load_from_json is adapted to update an instance
                    self._qd_device.load_from_json(data=value)  # update the QDDevice object
                else:
                    setattr(self, key, value)

    def print_simulation_info(self, print_device_info=False):

        """
        Print the simulation setup. Optionally, print the quantum dot device information too.
        """
        if print_device_info:
            self._qd_device.print_device_info()

        print("Simulation setup:")
        print(f"Physics to be simulated: {self._physics_to_be_simulated}")
        print(f"Number of voltage points per axis: {self._num_voltage_per_axis}")
        print(f"Number of probe points: {self._num_probe_points}")
        print(f"Variable gate index 1: {self._variable_gate_index_1}")
        print(f"Variable gate index 2: {self._variable_gate_index_2}")
        print(f"Voltage ranges: {self._voltage_ranges}")
        print(f"Gate voltages: {self._gate_voltages}")
        print(f"Sensor locations: {self._sensor_locations}")
        # print(f"Number of sensors: {self._num_sensors}")

    def set_sensor_locations(self, sensor_locations):

        """
        Sets the locations of the sensors used to sense the potential of the quantum dot array.

        This is the first method to be called when running the simulation.
        It sets the locations of the sensors used to sense the potential of the quantum dot array.
        The locations are specified as a list of coordinates (x,y) in the same coordinate system as the
        `physical_dot_locations` attribute of the `QDDevice` object.
        It also updates the `_num_sensors` attribute of the `QDSimulator` object.

        Sensors should not be placed on top of any dot whose controlling gate is being scanned, as this will cause
        the simulation to fail.

        Args:
            sensor_locations (list): The list containing the coordinates (x,y) of each sensor.

        Returns:
            None

        """

        self._sensor_locations = sensor_locations
        # self._num_sensors = len(sensor_locations)

    def simulate_charge_stability_diagram(self, qd_device, scanning_gate_indexes, n_points_per_axis,
                                          v_range_x, v_range_y=None, solver='SCIP', fixed_voltage=0, gates_voltages=None,
                                          save_voltage_occupation_data_to_filepath=None,
                                          save_occupation_data_to_filepath=None, save_sensing_data_to_filepath=None,
                                          save_current_data_to_filepath=None, use_ray=False):

        """
        Runs the simulation for determining the charge stability diagram of the quantum dot array.

        This method creates a `CapacitanceQuantumDotArray` object with the specified capacitance
        matrices obtained from the quantum_dot_device. It then selects the _solver (e.g. 'MOSEK', or 'SCIP') to use for
        the simulation and runs it using the specified voltage points. The resulting occupation array,
        energy array, and time list are stored in the attributes `_occupation_array`, `_energy_array`, and
        `_time_list`, respectively.


        Args:
            save_voltage_occupation_data_to_filepath:
            qd_device (QDDevice): The `QDDevice` object to be simulated.
            solver (str): The _solver to use for the simulation. Supported values are, for instance, 'SCIP'
                    (open source) and 'MOSEK' (licensed). It defaults to 'SCIP', since it is open source.
            scanning_gate_indexes (list): The indexes of the gates to scan. The length of this list must be 2.
            n_points_per_axis (int): The number of points to probe on the x- and y-axis.
            v_range_x (list): The minimum and maximum voltage to probe on the x-axis. E.g. [-3, 2].
            v_range_y (list, optional): The minimum and maximum voltage to probe on the y-axis. E.g. [-5, 6].
                    Defaults to None, in which case the same range as v_range_x is used.
            fixed_voltage (float, optional): The voltage to apply to all the gates that are not being scanned.
                    Defaults to 0. Either use this argument or `gates_voltages`, not both.
            gates_voltages (list, optional): The list containing the voltages to apply to each gate. If None,
                    the voltages of the non-variable gates are all set equal to fixed_voltage. Defaults to None.
                    In order to use this argument, the length of the array must be equal to the number of gates, and the
                    elements of the array indexed by the index gates to scan must be set to None.
                    E.g. 3 gates, scan gates 0 and 2 and set gate 1 voltage to 1.5, gates_voltages = [None, 1.5, None]
                    Either use this argument or `fixed_voltage`, not both.
            save_occupation_data_to_filepath (str, optional): The path and the name of the file where the .npy
                    file with the occupation array will be saved. If None, the file will not be saved. Defaults to None.
            save_sensing_data_to_filepath (str, optional): The path and the name of the file (no extension)
                    where the .npy file with the potential array will be saved. If None, the file will not be saved.
                    Defaults to None.
            save_current_data_to_filepath (str, optional): The path and the name of the file (no extension) where the
                    .npy
                    file with the current array will be saved. If None, the file will not be saved. Defaults to None.

        Returns:
            None

        """
        assert len(scanning_gate_indexes) == 2, "scanning_gate_indexes length must be equal to 2. " \
                                                "You can only scan 2 gates at a time."
        self._qd_device = qd_device
        self._variable_gate_index_1, self._variable_gate_index_2 = scanning_gate_indexes
        self._num_voltage_per_axis = n_points_per_axis
        self._num_probe_points = self._num_voltage_per_axis ** 2  # plot resolution

        # Generate the fixed voltages array if not provided
        if gates_voltages is None:
            fixed_voltages = generate_fixed_voltages(qd_device.num_gates, self._variable_gate_index_1,
                                                     self._variable_gate_index_2, fixed_voltage)
        else:
            fixed_voltages = gates_voltages

        self._gate_voltages = copy.deepcopy(fixed_voltages)

        if v_range_y is None:
            v_range_y = v_range_x

        self._voltage_ranges = [v_range_x, v_range_y]

        # Generate the voltage array to probe
        self._evaluate_csd_voltage_2d_space_to_probe(fixed_voltages)

        # Create the CapacitanceQuantumDotArray object and select the solver
        my_qd_arr = CapacitanceQuantumDotArray(simulate=self._physics_to_be_simulated)
        my_qd_arr.select_solver(solver)
        # This is the main "simulate" command, and the two vars on the left are the results, plus the time
        self._occupation_array, self._energy_array, self._time_list = my_qd_arr.probe_voltage_space(self,
                                                                                                    use_ray=use_ray)

        # Reshape the arrays for another saving format
        voltage_matrix = self.voltage_array.reshape((n_points_per_axis, n_points_per_axis,
                                                     qd_device.num_gates))
        occupation_matrix = self._occupation_array.reshape((n_points_per_axis, n_points_per_axis,
                                                            qd_device.num_dots))

        # Here I concatenate the voltages and the occupation, such that the first n = num_gates columns are the voltages
        # for each gate and the last m = num_dots columns are the occupation numbers per for each dot
        self._voltage_occupation_data = np.concatenate((voltage_matrix, occupation_matrix), axis=-1)

        if save_occupation_data_to_filepath is not None:
            np.save(f"{save_occupation_data_to_filepath}", self._occupation_array)

        if save_voltage_occupation_data_to_filepath is not None:
            np.save(f"{save_voltage_occupation_data_to_filepath}", self._voltage_occupation_data)  # saves to .npy file

        # Run charge sensing, as a visualization tool of the charge stability diagram
        self._run_charge_sensing(save_sensing_data_to_filepath, save_current_data_to_filepath)

        # Store the system maxwell matrix just for ease of use, in case I want to check it
        self._system_maxwell_matrix = my_qd_arr.system_maxwell_matrix

    def save_results_to_npy(self, save_voltage_occupation_data_to_filepath=None,
                            save_sensing_data_to_filepath=None, save_current_data_to_filepath=None):

        """ Save the simulation results to .npy files.

        Args:
            save_voltage_occupation_data_to_filepath: if not None, the file will be saved.
            save_sensing_data_to_filepath: if not None, the file will be saved.
            save_current_data_to_filepath: if not None, the file will be saved.

        """

        if save_voltage_occupation_data_to_filepath is not None:
            np.save(f"{save_voltage_occupation_data_to_filepath}", self._voltage_occupation_data)

        if save_sensing_data_to_filepath is not None:
            np.save(f"{save_sensing_data_to_filepath}", self._potential_array)

        if save_current_data_to_filepath is not None:
            np.save(f"{save_current_data_to_filepath}", self._current_array)

    def load_results_from_npy(self, voltage_occupation_data_filepath=None, sensing_data_filepath=None,
                                current_data_filepath=None):

        """ Load the simulation results from .npy files.

        Args:
            voltage_occupation_data_filepath: if not None, the file will be loaded. Users must include filename and
             extension.
            sensing_data_filepath: if not None, the file will be loaded.
            current_data_filepath: if not None, the file will be loaded.

        """

        if voltage_occupation_data_filepath is not None:
            if not os.path.exists(voltage_occupation_data_filepath):
                raise FileNotFoundError(f"File not found: {voltage_occupation_data_filepath}")
            else:
                self._voltage_occupation_data = np.load(voltage_occupation_data_filepath)
                self._occupation_array = self._voltage_occupation_data[:, :, self._qd_device.num_gates:]
                self._voltage_array = self._voltage_occupation_data[:, :, :self._qd_device.num_gates]

        if sensing_data_filepath is not None:
            if not os.path.exists(sensing_data_filepath):
                raise FileNotFoundError(f"File not found: {sensing_data_filepath}")
            else:
                self._potential_array = np.load(sensing_data_filepath)
            # self._current_array = evaluate_current_array_from_potential_array(self._potential_array)

        if current_data_filepath is not None:
            if not os.path.exists(current_data_filepath):
                raise FileNotFoundError(f"File not found: {current_data_filepath}")
            else:
                self._current_array = np.load(current_data_filepath)


    def get_charge_configuration(self, voltage_point):

        """
        Get the charge configuration at a specific voltage point.

        This method returns the charge configuration at a specific voltage point in the voltage space. The charge
        configuration is returned as a list of the occupation state of each dot in the quantum dot array.

        Args:
            voltage_point (list): The list containing the voltages to apply to each gate. [v1, v2, ..., vn].

        Returns:
            list: The list containing the occupation state of each dot in the quantum dot array.

        """
        # check whether the voltage point is in the voltage space simulated
        for i, v in enumerate(voltage_point):
            if v < self._voltage_ranges[i][0] or v > self._voltage_ranges[i][1]:
                raise ValueError("Voltage point out of the voltage space simulated")

        if len(voltage_point) == 2:
            index_v_x = self._convert_generic_voltage_coordinate_to_nearest_data_index(self._variable_gate_index_1,
                                                                                        voltage_point[0])
            index_v_y = self._convert_generic_voltage_coordinate_to_nearest_data_index(self._variable_gate_index_2,
                                                                                        voltage_point[1])

            print('Voltage point considered:', self._voltage_occupation_data[index_v_x, index_v_y, : self._qd_device.num_gates])
            print('Charge configuration:', self._voltage_occupation_data[index_v_x, index_v_y, self._qd_device.num_gates:])
            return (self._voltage_occupation_data[index_v_x, index_v_y, : self._qd_device.num_gates],
                    self._voltage_occupation_data[index_v_x, index_v_y, self._qd_device.num_gates:])

        # TO DO
        elif len(voltage_point) == self._qd_device.num_gates:
            index_v = []
            for i in range(self._qd_device.num_gates):
                index_v.append(self._convert_generic_voltage_coordinate_to_nearest_data_index(i, voltage_point[i]))

            print('NOT ENABLED IN THIS VERSION')

            # print('Voltage point considered:', self._voltage_occupation_data[index_v[0], index_v[1], : self._qd_device.num_gates])
            # print('Charge configuration:', self._voltage_occupation_data[index_v[0], index_v[1], self._qd_device.num_gates:])
            # return (self._voltage_occupation_data[index_v[0], index_v[1], : self._qd_device.num_gates],
            #         self._voltage_occupation_data[index_v[0], index_v[1], self._qd_device.num_gates:])

        else:
            raise ValueError("The number of voltages in the voltage point must be equal to 2 or to the number of gates")

        return self._occupation_array[np.where((self._voltage_array == voltage_point).all(axis=1))[0][0]]

    def _convert_generic_voltage_coordinate_to_nearest_data_index(self, gate_index, v):

            """
            Converts a generic voltage coordinate to the nearest data index.

            This method converts a generic voltage coordinate to the nearest data index in the voltage space.

            Args:
                gate_index (int): The index of the gate.
                v (float): The voltage coordinate.

            Returns:
                int: The nearest data index in the voltage space.

            """
            v_min = self._voltage_ranges[gate_index][0]
            v_max = self._voltage_ranges[gate_index][1]
            unit = (v_max - v_min) / self._num_voltage_per_axis
            return int((v - v_min) / unit)

    def _run_charge_sensing(self, save_sensing_data_to_filepath=None, save_current_data_to_filepath=None):

        """
        Runs the charge sensing simulation.

        This method runs the charge sensing simulation, which is used to sense the potential of the quantum dot array
        at each sensor location, stored in _sensor_locations . The potential sensed by each sensor is stored in
        the `_potential_array` attribute of the `QDSimulator` object. Note that the charge-sensing is mainly a
        visualization technique, as the full occupation state at each point has already been generated.

        It shows a progress bar.


        Args:
            save_sensing_data_to_filepath (str, optional): The path and the name of the file where the .npy
                    file with the potential array will be saved. If None, the file will not be saved. Defaults to None.
            save_current_data_to_filepath (str, optional): The path and the name of the file where the .npy
                    file with the current array will be saved. If None, the file will not be saved. Defaults to None.

        Returns:
            None

        """

        # Initialise
        self._potential_array = np.zeros(shape=(self._num_probe_points, len(self._sensor_locations)))

        # Fill the array by sensing based on the simulation results
        for lv_sensor in tqdm.tqdm(range(0, len(self._sensor_locations))):  # for each sensor, tqdm shows a progress bar
            for lv_pt in range(0, self._num_probe_points):
                current_occupation = self._occupation_array[lv_pt]
                self._potential_array[lv_pt, lv_sensor] = self._sense_potential(current_occupation,
                                                                                self._sensor_locations[
                                                                                    lv_sensor])

        # Need to change the ordering of the array for plotting:
        # this implies a flipud and a transpose to opposite diagonal
        # the results of the plots have been checked with the voltage-occupation combinations and are correct
        tmp_potential_array = np.zeros(
            shape=(self._num_voltage_per_axis, self._num_voltage_per_axis, len(self._sensor_locations)))
        for lv_sensor in range(len(self._sensor_locations)):
            tmp = self._potential_array[:, lv_sensor]
            tmp_potential_array[:, :, lv_sensor] = np.flipud(
                np.reshape(tmp, (self._num_voltage_per_axis, self._num_voltage_per_axis)))

        tmp_potential_array = transpose_opposite_diagonal_anything(tmp_potential_array)
        self._potential_array = tmp_potential_array
        self._current_array = evaluate_current_array_from_potential_array(self._potential_array)

        # Save the potential array if desired, it is saved in an imshow-friendly ordering
        if save_sensing_data_to_filepath is not None:
            np.save(f"{save_sensing_data_to_filepath}", self._potential_array)  # saves to .npy file

        if save_current_data_to_filepath is not None:
            np.save(f"{save_current_data_to_filepath}", self._current_array)  # saves to .npy file

    def _sense_potential(self, current_occupation, sensor_coordinates):
        """
        Calculates the electrostatic potential sensed by a sensor.

        This method calculates the absolute value of electrostatic potential sensed by a sensor,
        based on the current occupation state of the quantum dot array and the coordinates of the sensor.
        The potential is calculated as the sum of the potential generated by each dot, weighted by the
        occupation (= number of charges) state of the dot. The potential is calculated in atomic units.

        Args:
            current_occupation (list): The occupation state of the quantum dot array.
            sensor_coordinates (tuple): The coordinates (x,y) of the sensor.

        Returns:
            float: The electrostatic potential sensed by the sensor.


        """
        # initialise at 0
        potential = 0

        # For each dot
        for lv_dot in range(self._qd_device.num_dots):
            big_r = calculate_distance(sensor_coordinates, self._qd_device.physical_dot_locations[lv_dot])
            assert big_r > 1e-10  # ensure sensor isn't on any dots

            potential += current_occupation[lv_dot] / big_r

        return potential

    def _evaluate_csd_voltage_2d_space_to_probe(self, fixed_voltages):

        """
        Generates the array of tuples representing the voltages (v1, v2) to probe in the voltage space.

        This method generates the array of tuple representing the voltages (v1, v2) to probe in the voltage space.
        The voltages are generated based on the specified voltage range and sensitivity. The array is stored in the
        `_voltage_array` attribute of the `QDSimulator` object.

        Args:
            fixed_voltages (list): The list containing the voltages to apply to each gate.

        Returns:
            None

        """

        vl = np.linspace(self._voltage_ranges[0][0], self._voltage_ranges[0][1], self._num_voltage_per_axis)
        vr = np.linspace(self._voltage_ranges[1][0], self._voltage_ranges[1][1], self._num_voltage_per_axis)

        self._fill_voltage_arr(fixed_voltages, vl, vr)
        self._voltage_array = np.array(self._voltage_array)

    def _fill_voltage_arr(self, fixed_voltages, vl, vr):

        """
        Fills the `_voltage_array` attribute of the `QDSimulator` object with the voltages to probe in the voltage
        space.

        Args:
            fixed_voltages (list): The list containing the voltages to apply to each non-variable gate.
            vl (np.array): The array containing the voltages to apply to the first variable gate.
            vr (np.array): The array containing the voltages to apply to the second variable gate.

        Returns:
            None

        """

        self._voltage_array = []
        for m1 in vl:
            fixed_voltages[self._variable_gate_index_1] = m1
            for m2 in vr:
                fixed_voltages[self._variable_gate_index_2] = m2
                self._voltage_array.append(fixed_voltages.copy())

    def plot_charge_stability_diagrams(self, cmapvalue='RdPu', gaussian_noise=False, white_noise=False,
                                       pink_noise=False, plot_potential=False, only_plot_sensors=None, gaussian_noise_params=None,
                                       white_noise_params=None, pink_noise_params=None,
                                       save_plot_to_filepath=None, save_noisy_npy_data_to_filepath=None):

        """
        Generates a plot of the charge stability diagram and saves the plot if the path file is provided.

        This method generates a plot of the charge stability diagram and saves the plot if the path file is provided.
        It shows a progress bar.

        Args:
            cmapvalue (str, optional): The colormap to use for the plot. Defaults to 'RdPu'.
            gaussian_noise (bool, optional): Whether to add gaussian noise to the plot. Defaults to False.
            white_noise (bool, optional): Whether to add white noise to the plot. Defaults to False.
            pink_noise (bool, optional): Whether to add pink noise to the plot. Defaults to False.
            plot_potential (bool, optional): Whether to plot the potential map instead of the current map
                    (considered default). Defaults to False.
            gaussian_noise_params (list, optional): The parameters [avg, std_dev] of the gaussian noise to add
                    to the plot. Defaults to None - in this case, the default parameters are used.
            white_noise_params (list, optional): The parameters [min, max] of the white noise to add to the plot.
                    Defaults to None - in this case, the default parameters are used.
            pink_noise_params (list, optional): The parameters [f_max, amplitude_range] of the pink noise to add
                    to the plot. Defaults to None - in this case, the default parameters are used.
            save_plot_to_filepath (str, optional): File path (including name and file extension) to save the plots. If
                    None, the plots will not be saved. Defaults to None.

            only_plot_sensors (list, optional): The list containing the indexes of the sensors to plot. If None, all
                    sensors are plotted. Defaults to None.

        Returns:
            None

        Notes:
            - The shape of the `_potential_array` should be (_num_voltage_per_axis,
              _num_voltage_per_axis, len(sensor_locations)).
        """
        # For each sensor...
        if only_plot_sensors is not None:
            sensors_to_plot = only_plot_sensors
        else:
            sensors_to_plot = range(len(self._sensor_locations))

        for lv_sensor in sensors_to_plot:
            # Plot CSD
            plot_title = f"Sensor {lv_sensor}"

            if plot_potential:
                big_z = self._potential_array[:, :, lv_sensor]
            else:
                big_z = self._current_array[:, :, lv_sensor]

            csd = plot_csd(physical_quantity_matrix=big_z, voltage_ranges=self._voltage_ranges,
                           variable_gate_indices=[self._variable_gate_index_1, self._variable_gate_index_2],
                           cmapvalue=cmapvalue, plot_title=plot_title, gaussian_noise=gaussian_noise,
                           white_noise=white_noise, pink_noise=pink_noise, plot_potential=plot_potential,
                           gaussian_noise_custom_params=gaussian_noise_params,
                           white_noise_custom_params=white_noise_params,
                           pink_noise_custom_params=pink_noise_params, save_noisy_data_npy_to_filepath=
                            save_noisy_npy_data_to_filepath)

            # If desired, save the plot
            plt.figure(csd)
            if save_plot_to_filepath is not None:
                plt.savefig(f"{save_plot_to_filepath}", bbox_inches='tight')

    # def load_data(self, voltage_ranges, variable_gate_indices, sensor_locations, occupation_data_path=None,
    #               sensing_data_path=None, current_data_path=None, voltage_occupation_data_path=None):
    #     """
    #     Loads the data from the specified files.
    #
    #     This method loads the data from the specified files and stores it in the corresponding attributes of the
    #     `QDSimulator` object.
    #
    #     Args:
    #         voltage_ranges (list): The minimum and maximum voltages to probe on the x- and y-axis. E.g.
    #                 [[v_min_x, v_max_x], [v_min_y, v_max_y]].
    #         variable_gate_indices (list): The indexes of the gates that are varied, e.g. [0, 1] for the first two gates.
    #         sensor_locations (list): The list containing the coordinates (x,y) of each sensor.
    #         occupation_data_path (str, optional): The path and the name of the file where the .npy file with the
    #                 occupation array is stored. If None, the file will not be loaded. Defaults to None.
    #         sensing_data_path (str, optional): The path and the name of the file where the .npy file with the
    #                 potential array is stored. If None, the file will not be loaded. Defaults to None.
    #         current_data_path (str, optional): The path and the name of the file where the .npy file with the
    #                 current array is stored. If None, the file will not be loaded. Defaults to None.
    #     Returns:
    #         None
    #
    #     """
    #     if occupation_data_path is not None:
    #         self._occupation_array = np.load(f'{occupation_data_path}.npy')
    #
    #     if sensing_data_path is not None:
    #         self._potential_array = np.load(f'{sensing_data_path}.npy')
    #
    #     if current_data_path is not None:
    #         self._current_array = np.load(f'{current_data_path}.npy')
    #
    #     if voltage_occupation_data_path is not None:
    #         self._voltage_occupation_data = np.load(f'{voltage_occupation_data_path}.npy')
    #
    #     self._voltage_ranges = voltage_ranges
    #
    #     self._variable_gate_index_1 = variable_gate_indices[0]
    #     self._variable_gate_index_2 = variable_gate_indices[1]
    #     self._sensor_locations = sensor_locations

    @property
    def num_probe_points(self):
        return self._num_probe_points

    @property
    def qd_device(self):
        return self._qd_device

    @property
    def voltage_array(self):
        return self._voltage_array

    @property
    def potential_array(self):
        return self._potential_array

    @property
    def current_array(self):
        return self._current_array

    @property
    def occupation_array(self):
        return self._occupation_array

    @property
    def voltage_occupation_data(self):
        return self._voltage_occupation_data

    @property
    def energy_array(self):
        return self._energy_array

    @property
    def time_list(self):
        return self._time_list

    @property
    def sensor_locations(self):
        return self._sensor_locations

    # @property
    # def num_sensors(self):
    #     return self._num_sensors

    @property
    def system_maxwell_matrix(self):
        return self._system_maxwell_matrix

    @property
    def variable_gate_index_1(self):
        return self._variable_gate_index_1

    @property
    def variable_gate_index_2(self):
        return self._variable_gate_index_2

    @property
    def volt_ranges(self):
        return self._voltage_ranges

    @property
    def gate_voltages(self):
        return self._gate_voltages

    def _get_attributes_as_dict(self, attribute_names):
        """
        Returns a dictionary containing the specified attributes of an object.

        This function returns a dictionary containing the specified attributes of an object. It is used to save the
        attributes of an object to a file.

        Args:
            attribute_names (list): The list of attributes to save.

        Returns:
            attribute_dict (dict): The dictionary containing the specified attributes of the object.

        """
        attribute_dict = {}
        for attr_name in attribute_names:
            attr_value = getattr(self, attr_name)

            # Convert NumPy arrays to lists for JSON serialization
            if isinstance(attr_value, np.ndarray):
                attr_value = attr_value.tolist()

            attribute_dict[attr_name] = attr_value

        return attribute_dict

    def save(self, path_to_root=None):
        """
        Saves all the information of the device and the simulation in a structured way.
        Useful for creating datasets.


        Args:
            path_to_root (str, optional): The path to the root directory where a 'dataset' folder will be created and
            filled with one folder per simulation. If None, the current working directory is used. Defaults to None.

        Returns:
            None

        """
        if path_to_root is None:
            path_to_root = os.getcwd()

        # Create the directory if it does not exist
        if not os.path.exists(path_to_root):
            os.makedirs(f"{path_to_root}/dataset")

        # Create a directory for the simulation in the dataset folder
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        simulation_folder = f"{path_to_root}/dataset/simulation_{timestamp}"
        os.makedirs(simulation_folder)

        # Save the QDDevice and QDSimulator information in a JSON file (but not the simulated results)
        self.save_to_json(self, f"{simulation_folder}/simulation_info_{timestamp}.json")

        npy_folder = f"{simulation_folder}/npy_files"
        os.makedirs(npy_folder)

        # Save the simulated results in .npy files
        self.save_results_to_npy(f"{npy_folder}/voltage_occupation_data.npy", f"{npy_folder}/sensing_data.npy",
                                    f"{npy_folder}/current_data.npy")




########################################################################################################################
# Auxiliary functions, not part of the class


def generate_linspace_arrays(v_ranges, n_points):
    """
    Generates a meshgrid of linspace arrays.

    This function generates a meshgrid of linspace arrays, given a list of voltage ranges and the number of points to
    generate for each range. It is used to generate the voltage array to probe in the voltage space for the polytope
    simulation.

    Args:
        v_ranges (list): The list of voltage ranges to generate the linspace arrays for. E.g. for only two gates,
                [[v_min_x, v_max_x], [v_min_y, v_max_y]]. Its length must be equal to the number of gates.
        n_points (int): The number of points to generate for each range.

    Returns:
        result (np.array): The array containing the voltages to probe in the voltage space. Its shape is
                (n_points**len(v_ranges), len(v_ranges)).

    """
    # Generate a linspace for each range and store them in a list
    lin_spaces = [np.linspace(vmin, vmax, n_points) for vmin, vmax in v_ranges]

    # Create a meshgrid from the linspace arrays
    mesh = np.meshgrid(*lin_spaces, indexing='ij')

    # Reshape and stack the arrays to get the final result
    result = np.vstack([m.flatten() for m in mesh]).T

    return result

def generate_fixed_voltages(size, g1, g2, fixed_value):

    """
    Generate a list of fixed voltages for all the non-variable gates of a device, with the two variable gates
    set to None.

    It sets all the gates to the same value, given by fixed_value, except for the two variable gates,
    which are set to None.

    Args:
        size (int): Number of gates in the device
        g1 (int): Index of the first variable gate
        g2 (int): Index of the second variable gate
        fixed_value (float): Value of the fixed voltages

    Returns:
        result (list): List of fixed voltages for the gates of the device, with the variable gates set to None

    """
    result = [fixed_value] * size
    result[g1] = None
    result[g2] = None
    return result


def evaluate_current_array_from_potential_array(potential_array):
    """
    Calculates the current array from the potential array.

    It calculates the current array from the potential array, by calculating the gradient of the potential array
    and multiplying it by the conductivity value. The details of the calculation are expressed in the
    evaluate_current_matrix_from_potential_matrix function.

    Args:
        potential_array (np.array): The array containing the potential sensed by each sensor at each point in the
                voltage space. Its shape should be:
                (_num_voltage_per_axis, _num_voltage_per_axis, len(sensor_locations)).

    Returns:
        current_array (np.array): The array containing the current sensed by each sensor at each point in the voltage
                space. Its shape is the same as the potential_array.
    """

    current_array = np.zeros_like(potential_array)

    for i in range(potential_array.shape[2]):
        current_array[:, :, i] = evaluate_current_matrix_from_potential_matrix(potential_array[:, :, i])

    return current_array


def evaluate_current_matrix_from_potential_matrix(potential_matrix):

    """
    Calculates the current matrix from the potential matrix.

    It calculates the current matrix from the potential matrix, by calculating the gradient of the potential matrix
    and multiplying it by the conductivity value. The conductivity value is set to 1.0 by default, but it can be
    changed as needed.

    Args:
        potential_matrix (np.array): The matrix containing the potential sensed by each sensor at each point in the
                voltage space. Its shape should be (_num_voltage_per_axis, _num_voltage_per_axis).

    Returns:
        current_matrix (np.array): The matrix containing the current sensed by each sensor at each point in the voltage
                space. Its shape is the same as the potential_matrix.

    """
    grad_x, grad_y = np.gradient(potential_matrix)
    # Define the conductivity value (replace with your actual value)
    conductivity = 1.0  # Adjust as needed

    # Calculate the current density (J) in both x and y directions
    current_density_x = conductivity * grad_x
    current_density_y = conductivity * grad_y
    # Calculate the magnitude of the current density
    current_density_magnitude = np.sqrt(current_density_x ** 2 + current_density_y ** 2)

    return current_density_magnitude


def transpose_opposite_diagonal(matrix):
    """
    Transposes a matrix along the opposite diagonal.

    Args:
        matrix (list): The matrix to transpose.

    Returns:
        lisl: the transposed matrix.

    """
    n = len(matrix)
    m = len(matrix[0])
    transposed_opposite_diagonal = [[matrix[j][i] for j in range(n - 1, -1, -1)] for i in range(m - 1, -1, -1)]
    return transposed_opposite_diagonal


def transpose_opposite_diagonal_anything(tmp_potential_array):
    """
    Transposes all the nxn matrices in an array of shape=(n,n,m) along the opposite diagonal.

    The transpose_opposite_diagonal function only works for square matrices, so this function is used to transpose
    the potential array, which is a 3D array of square matrices.

    Args:
        tmp_potential_array (np.array): The array of matrices to transpose.

    Returns:
        np.array: the transposed array.

    """
    n = tmp_potential_array.shape[2]
    tmp_array_list = []

    for i in range(n):
        # Apply transpose_opposite_diagonal to each (100, 100) matrix in the tmp_potential_array
        transposed_matrix = transpose_opposite_diagonal(tmp_potential_array[:, :, i])
        tmp_array_list.append(transposed_matrix)

    # Stack the results along the last dimension to create the new tmp_array
    return np.stack(tmp_array_list, axis=2)
