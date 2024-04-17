"""
@author: VGualtieri

"""

from ._auxiliaryfunctions import calculate_distance
import numpy as np
import random
import matplotlib.pyplot as plt  # to plot the device
from ._plotCSD import plot_style  # to plot the device
import json
import os
import re

class QDDevice:
    """
    This class is used to define the quantum dot device.
    It is just about the geometry and design of the device.
    Here we define the number of dots, the number of gates, the physical locations of the dots, and the dot-dot and
    dot-gate mutual capacitance matrices.

    The class initializes an empty object. The user can then use the methods to define the device.
    Within the methods, the user can define the physical locations of the dots, and the dot-dot and dot-gate mutual
    capacitance matrices.

    The class offers a few standard options for the device design. The user can also define a custom design.
    The standard options are:
        - one_dimensional_dots_array: A line of dots with individual gate control. The user can specify the number of
                dots, the dot naked self-capacitance. The user can also specify whether the dots have equal capacitance
                or not. The user can also specify whether the gates have equal capacitance or not. The user can also
                specify the crosstalk strength. Double dot devices are a special case of this option, with num_dots = 2.
        - bi_dimensional_10_dots_array: A 2D array of 10 dots with individual gate control. The user can specify the
                dot naked self-capacitance. The user can also specify whether the dots have equal capacitance or not.
                The user can also specify whether the gates have equal capacitance or not. The user can also specify
                the crosstalk strength.
        - crossbar_array_shared_control: A crossbar array of dots with shared control. The user can specify the number
                of dots per side of the square lattice. The user can also specify the dot naked self-capacitance. The
                user can also specify whether the dots have equal capacitance or not. The user can also specify whether
                the gates have equal capacitance or not. The user can also specify the crosstalk strength.

    The class has the following attributes:
        - device_type (str): The type of device. It can be 'crossbar' or None. Its purpose is only for plotting. Cannot
                be set by the user.
        - num_dots (int): The number of dots in the device.
        - num_gates (int): The number of gates in the device.
        - c0 (float): The dot naked self-capacitance.
        - physical_dot_locations (list of 2-tuples): A list of 2-tuples representing the coordinates (x,y) of each dot.
        - dot_dot_mutual_capacitance_matrix (ndarray): A 2D array of non-negative floats, shape = (num_dots, num_ots).
                Element (i, j) of this matrix is the capacitance between dot i and dot j.
                Note that this should not be confused with the Maxwell capacitance matrix between the dots.
        - dot_gate_mutual_capacitance_matrix (ndarray): A 2D array of non-negative floats,
                shape = (num_dots, num_gates). Element i,j of this matrix is the mutual capacitance between dot i and
                gate j.

    The class has the following methods:
        - set_physical_dot_locations(physical_dot_locations): Assign the physical dot locations to the calling object.
        - set_num_gates(num_gates): Assign the number of gates to the calling object.
        - set_dot_dot_mutual_capacitance_matrix(dot_dot_mutual_capacitance_matrix): Assign a custom dot-dot mutual
                capacitance matrix to the calling object's attribute dot_dot_mutual_capacitance_matrix.
        - set_dot_gate_mutual_capacitance_matrix(dot_gate_mutual_capacitance_matrix): Assign a custom dote-gate mutual
                capacitance matrix to the calling object's attribute dot_gate_mutual_capacitance_matrix.
        - evaluate_dot_dot_mutual_capacitance_matrix(c0): Evaluate the dot-dot mutual capacitance matrix of the calling
                object based on physical dot locations. The dot-dot capacitance matrix is calculated using a
                distance-based model using the data contained in physical_dot_locations. The result of the calculation
                is assigned to the dot_dot_mutual_capacitance_matrix.
        - evaluate_dot_gate_mutual_capacitance_matrix(c0): Evaluate the dot-gate mutual capacitance matrix of the
                calling object based on physical dot locations. The dot-gate capacitance matrix is calculated using a
                distance-based model using the data contained in physical_dot_locations, the location of the gates is
                assumed to be the same as the location of the dots (one gate per each dot, no shared control).
                The result of the calculation is assigned to the dot_gate_mutual_capacitance_matrix.
        - evaluate_dot_gate_mutual_capacitance_matrix_shared_control(c0): Evaluates the dot-gate mutual capacitance
                matrix of the calling object based on physical dot locations.
                The dot-gate capacitance matrix is calculated using a distance-based model using the data contained
                in physical_dot_locations, the location of the gates is assumed to be the same as the location of the
                dots (one gate overlap multiple dot diagonally, shared control). The ordering of the dots is assumed to
                be a square lattice. The result of the calculation is assigned to the
                dot_gate_mutual_capacitance_matrix. The top left dot is assumed to be the first dot, and the bottom
                right dot to be the last dot (index num_dots - 1) . The indices grow from top to bottom, from
                left to right,diagonally.
                The top left oblique gate is assumed to be the first gate (index 0), and the bottom right oblique gate
                is assumed to be the last gate (index num_gates - 1). These gates are the only ones that control only
                one dot each.
        - evaluate_dot_gate_mutual_capacitance_matrix_crossbar(c0): Evaluate the dot-gate mutual capacitance matrix
                of the calling object based on physical dot locations. The dot-gate capacitance matrix is calculated
                using a distance-based model using the data contained in physical_dot_locations, the location of the
                gates is assumed to be a line crossing over the dots it controls diagonally (one gate overlap multiple
                dot diagonally, shared control).
        - plot_device(sensor_locations, sensor_labels, dots_labels, save_to_filepath ): Plot the device. It is possible
                to plot the device with or without the sensors, and with or without the dots labels. The user can also
                save the plot to a file.
        - print_device_info(): Print the device information in a nicely formatted way.
    """


    def __init__(self):
        self._device_type = None
        self._num_dots = None
        self._c0 = 1.2e-1
        self._num_gates = None
        self._physical_dot_locations = None
        self._dot_dot_mutual_capacitance_matrix = None
        self._dot_gate_mutual_capacitance_matrix = None

    import numpy as np

    def print_device_info(self):
        """
        Print the device information in a nicely formatted way.

        This method prints the device type, the number of dots, the number of gates, the physical dot locations, and the
        dot-dot and dot-gate mutual capacitance matrices in a nicely formatted way.

        Returns:
            None
        """
        print(f"Device type: {self._device_type}")
        print(f"Number of dots: {self._num_dots}")
        print(f"Number of gates: {self._num_gates}")
        # print(f"Dot naked self-capacitance: {self._c0}")
        print(f"Physical dot locations: {self._physical_dot_locations}")

        print("Dot-dot mutual capacitance matrix:")
        if self._dot_dot_mutual_capacitance_matrix is not None:
            print(np.array2string(self._dot_dot_mutual_capacitance_matrix, formatter={'float_kind': lambda x: "%.2f" % x}))
        else:
            print("None")

        print("Dot-gate mutual capacitance matrix:")
        if self._dot_gate_mutual_capacitance_matrix is not None:
            print(np.array2string(self._dot_gate_mutual_capacitance_matrix, formatter={'float_kind': lambda x: "%.2f" % x}))
        else:
            print("None")

    def save_to_file(self, file):

        """
        Save the device to a file. In order to save all the information concerning device set up and simulation's
        characteristics, the user should call the save_to_file method of the QuantumDotSimulator class.

        It saves the device type, the number of dots, the number of gates, the physical dot locations, and the dot-dot
        and dot-gate mutual capacitance matrices. It is used iteratively by the save_to_file method of the
        QuantumDotSimulator class.

        Args:
            file (file): The file to which the device is saved.

        Returns:
            None

        """
        for attr_name, attr_value in vars(self).items():
            # Exclude specific attribute by name
            if attr_name == '_c0':
                continue
            file.write(f"sub_attr: {attr_name}: {attr_value}\n")

        # self._save_to_json(file_path)

    def save_to_json(self, json_file_path):

        """
        This method saves the quantum dot device attributes to a JSON file.

        The saved file can be used to load the device at a later time, using the load_from_json method of the
        QDDevice class.

        Args:
            json_file_path (str): The path (including name and extension) to the JSON file to which the device is saved.
             The file is created if it does not exist, and overwritten if it does exist.

        Returns:
            None

        """

        object_dict = {
            "_device_type": self._device_type,
            "_num_dots": self._num_dots,
            "_num_gates": self._num_gates,
            "_c0": self._c0,
            "_physical_dot_locations": self._physical_dot_locations,
            # "_physical_gate_locations": self._physical_gate_locations,
            "_dot_dot_mutual_capacitance_matrix": self._dot_dot_mutual_capacitance_matrix.tolist(),
            "_dot_gate_mutual_capacitance_matrix": self._dot_gate_mutual_capacitance_matrix.tolist()
        }

        with open(json_file_path, "w") as json_file:
            json.dump(object_dict, json_file, indent=4)

    def load_from_json(self, json_file_path=None, data=None):
        """
        Update a QDDevice instance from a JSON file or from a dictionary with the device data.

        Args:
            json_file_path (str): The path to the JSON file from which the device's data is updated.
            data (dict): The dictionary from which the device's data is updated.
        """
        if json_file_path is not None:
            if not os.path.exists(json_file_path):
                raise FileNotFoundError(f"File not found: {json_file_path}")

            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

        # Update the instance attributes directly
        for key, value in data.items():
            # Use numpy arrays for specific attributes
            if key in ["_dot_dot_mutual_capacitance_matrix", "_dot_gate_mutual_capacitance_matrix"]:
                setattr(self, key, np.array(value))
            else:
                setattr(self, key, value)

    def one_dimensional_dots_array(self, n_dots, equal_dots=True, equal_gates=True, crosstalk_strength=0,
                                   c0_dot=1.2e-1, c0_gate=1.2e-1):
        """
        This method defines a one-dimensional array of dots with individual gate control.

        It sets the number of dots, the number of gates, the dot naked self-capacitance, the dot-gate stronger
        mutual capacitance value, the physical dot/(gate) locations, and the dot-dot and dot-gate mutual capacitance
        matrices. Gate locations are assumed to be the same as dot locations.

        Args:
            n_dots (int): The number of dots in the array. Must be an integer strictly greater than 1.
            equal_dots (bool): If True, all dots have the same capacitance. If False, the dots have all slightly
                    different capacitance. Default is True.
            equal_gates (bool): If True, all gates have the same capacitance. If False, the gates have all slightly
                    different capacitance. Default is True.
            crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk. Default is 0. Larger values of
                    crosstalk_strength correspond to stronger crosstalk, but are not suggested.
            c0_dot: The dot self-capacitance. Default is 1.2e-1.
            c0_gate: The gate-dot stronger mutual capacitance. Default is 1.2e-1.

        Returns:
            None

        """

        self._device_type = 'in-line array'
        self._num_dots = n_dots
        self._num_gates = n_dots
        self._c0 = c0_dot
        self._physical_dot_locations = generate_1d_dots_location_array(n_dots)
        # self._physical_gate_locations = self.physical_dot_locations
        self.evaluate_dot_dot_mutual_capacitance_matrix(c0_dot, equal_dots)
        self.evaluate_dot_gate_mutual_capacitance_matrix(c0_gate, equal_gates, crosstalk_strength)


    def bi_dimensional_10_dots_array(self, equal_dots=True, equal_gates=True, crosstalk_strength=0, c0_dot=1.2e-1,
                                     c0_gate=1.2e-1):
        """
        This method defines a 2D array of 10 dots with individual gate control.

        It sets the number of dots, the number of gates, the dot naked self-capacitance, the dot-gate stronger
        mutual capacitance value, the physical dot/(gate) locations, and the dot-dot and dot-gate mutual capacitance
        matrices. Gate locations are assumed to be the same as dot locations.



        Args:
            equal_dots (bool): If True, all dots have the same capacitance. If False, the dots have all slightly
                    different capacitance. Default is True.
            equal_gates (bool): If True, all gates have the same capacitance. If False, the gates have all slightly
                    different capacitance. Default is True.
            crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk. Default is 0. Larger values of
                    crosstalk_strength correspond to stronger crosstalk, but are not suggested.
            c0_dot (float): The dot self-capacitance. Default is 1.2e-1.
            c0_gate (float): The gate-dot stronger mutual capacitance. Default is 1.2e-1.

        Returns:
            None

        """

        self._device_type = '10 dots bi-dimensional array'
        self._num_dots = 10
        self._num_gates = 10
        self._c0 = c0_dot
        self._physical_dot_locations = generate_2d_10_dots_location_array()
        # self._physical_gate_locations = self.physical_dot_locations
        self.evaluate_dot_dot_mutual_capacitance_matrix(c0_dot, equal_dots)
        self.evaluate_dot_gate_mutual_capacitance_matrix(c0_gate, equal_gates, crosstalk_strength)

    def crossbar_array_shared_control(self, n_dots_side, equal_dots=True, equal_gates=True, crosstalk_strength=0,
                                      c0_dot=1.2e-1, c0_gate=1.2e-1):
        """
        This method defines a 2D crossbar array of dots with diagonal shared control.

        It sets the number of dots and the number of gates from num_dots_side. It also sets the dot naked
        self-capacitance, the dot-gate stronger mutual capacitance value, the physical dot locations, and the dot-dot
        and dot-gate mutual capacitance matrices. Gate locations are not explicit, but are assumed to be diagonally
        placed, running from the bottom left corner to the top right corner of the square lattice. The ordering of the
        dots follows the order of the gates. The top left dot is assumed to be the first dot (index 0),
        and the bottom right dot is assumed to be the last dot (index num_dots - 1).

        Args:
            n_dots_side (int): The number of dots per side of the square lattice. Must be an integer strictly greater
                    than 1.
            equal_dots (bool): If True, all dots have the same self-capacitance. If False, the dots have all slightly
                    different self-capacitance. Default is True.
            equal_gates (bool): If True, all gates have the same gate-dot capacitance. If False, the gates have all
                    slightly different gate-dot capacitance. Default is True.
            crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk. Default is 0. Larger values of
                    crosstalk_strength correspond to stronger crosstalk, but are not suggested.
            c0_dot (float): The dot self-capacitance. Default is 1.2e-1.
            c0_gate (float): The gate-dot stronger mutual capacitance. Default is 1.2e-1.

        Returns:
            None

        """
        self._device_type = 'crossbar'
        self._num_dots = n_dots_side ** 2
        self._num_gates = n_dots_side * 2 - 1     # geometrical property of the crossbar array
        self._c0 = c0_dot
        self._physical_dot_locations = get_lattice(n_dots_side)
        # self._physical_gate_locations = None

        self.evaluate_dot_dot_mutual_capacitance_matrix(c0_dot, equal_dots)
        self.evaluate_dot_gate_mutual_capacitance_matrix_crossbar(c0_gate, equal_gates, crosstalk_strength)

    def set_custom_dot_locations(self, physical_dot_locations, c0=1.2e-1, equal_dots=True, equal_gates=True,
                                 crosstalk_strength=0.2):
        """
            Assign the physical dot locations and the dot naked self-capacitance to the calling object, and evaluates
            an initial version of the dot-dot mutual capacitance matrix and the dot-gate mutual capacitance matrix,
            under the assumption of individual control.

            This step is mandatory for any custom design.
            It sets the number of dots and the number of gates from the length of the physical_dot_locations list.
            The underlying initial assumption is individual control, therefore one-gate-controls-one-dot, with gate
            locations assumed to be equal to their corresponding dot locations.
            It also calculates a dot-dot mutual capacitance matrix based on the physical dot locations, using the class
            method evaluate_dot_dot_mutual_capacitance_matrix, and evaluates a dot-gate mutual capacitance matrix
            based on the physical dot locations, using the class method evaluate_dot_gate_mutual_capacitance_matrix.

            These matrices and number of gates can be overwritten later by the user using the setter methods,
            if desired, thus achieving a completely custom design.


            Args:
                physical_dot_locations (list of 2-tuple): A list of 2-tuples representing
                        the coordinates (x,y) of each dot in the calling object.
                c0 (float): The dot naked self-capacitance. Default is 1.2e-1.
                equal_dots (bool): If True, all dots have the same self-capacitance. If False, the dots have all
                        slightly different self-capacitance. Default is True.
                equal_gates (bool): If True, all gates have the same gate-dot capacitance. If False, the gates have all
                        slightly different gate-dot capacitance. Default is True.
                crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk. Default is 0. Larger values of
                        crosstalk_strength correspond to stronger crosstalk, but are not suggested.

            Returns:
                None
        """

        self._device_type = 'custom'
        self._physical_dot_locations = physical_dot_locations
        self._c0 = c0
        self._num_dots = len(physical_dot_locations)
        self._num_gates = len(physical_dot_locations)   # assumed to be equal to dots
        self.evaluate_dot_dot_mutual_capacitance_matrix(c0=c0, equal_dots=equal_dots)
        self.evaluate_dot_gate_mutual_capacitance_matrix(c0=c0, equal_gates=equal_gates,
                                                         crosstalk_strength=crosstalk_strength)

    def set_dot_dot_mutual_capacitance_matrix(self, dot_dot_mutual_capacitance_matrix):

        """
        Assign a custom dot-dot mutual capacitance matrix to the calling object's attribute
        dot_dot_mutual_capacitance_matrix.

        It also automatically sets the number of dots from the shape of the matrix, and sets the dot naked
        self-capacitance to the average of the diagonal elements of the matrix.
        The dot_dot_mutual_capacitance_matrix parameter must be a 2D array of (non-negative) floats.


        Args:
            dot_dot_mutual_capacitance_matrix (ndarray): A 2D array of non-negative floats, shape = (num_dots, num_dots)
                    Element (i, j) of this matrix is the capacitance between dot i and dot j.
                    Element (i, i) of this matrix is the dot i naked self-capacitance.
                    Note that this should not be confused with the Maxwell capacitance matrix between the dots.

        Returns:
            None

        """
        self._num_dots = dot_dot_mutual_capacitance_matrix.shape[0]
        self._c0 = np.trace(dot_dot_mutual_capacitance_matrix) / self._num_dots
        self._dot_dot_mutual_capacitance_matrix = dot_dot_mutual_capacitance_matrix

    def set_dot_gate_mutual_capacitance_matrix(self, dot_gate_mutual_capacitance_matrix):

        """
        Assign a custom dot-gate mutual capacitance Matrix to the attribute _dot_gate_mutual_capacitance_matrix.

        It also automatically sets the number of gates and number of dots from the shape of the matrix.
        The dot_gate_mutual_capacitance_matrix parameter must be a 2D array of (non-negative) floats.

        Args:
            dot_gate_mutual_capacitance_matrix (ndarray): 2D array of (non-negative) floats,
                    shape = (num_dots, num_gates).
                    Element i,j of this matrix is the mutual capacitance between dot i and gate j.

        Returns:
            None

        """
        self._num_gates = dot_gate_mutual_capacitance_matrix.shape[1]
        self._num_dots = dot_gate_mutual_capacitance_matrix.shape[0]
        self._dot_gate_mutual_capacitance_matrix = dot_gate_mutual_capacitance_matrix

    def evaluate_dot_dot_mutual_capacitance_matrix(self, c0, equal_dots):

        """
        Evaluate the dot-dot mutual capacitance matrix characterizing the quantum dot device based on physical
        dot locations.

        The dot-dot capacitance matrix is calculated using a distance-based model using the data contained
        in _physical_dot_locations. The result of the calculation is assigned to the dot_dot_mutual_capacitance_matrix.

        Args:
            c0 (float): The dot naked self-capacitance.
            equal_dots (bool): If True, all dots have the same capacitance. If False, the dots have all slightly
                    different capacitance.

        Returns:
            None

        """

        self._c0 = c0
        self._dot_dot_mutual_capacitance_matrix = np.identity(self._num_dots) * c0
        self._fill_dot_dot_distance(c0, equal_dots)

    def evaluate_dot_gate_mutual_capacitance_matrix(self, c0, equal_gates, crosstalk_strength):

        """
        Evaluate the dot-gate mutual capacitance matrix characterizing the quantum dot device based on physical dot
        locations.
        Non-equal gates and cross-talk are implemented via the addition of random values.

        The dot-gate capacitance matrix is calculated using a distance-based model using the data contained
        in _physical_dot_locations, the location (and number) of the gates is assumed to be the same as the location
        (and number) of the dots (one gate per each dot, no shared control). The result of the calculation is assigned
        to the dot_gate_mutual_capacitance_matrix.

        Args:
            c0 (float): The dot naked self-capacitance.
            equal_gates (bool): If True, all gates have the same gate-dot capacitance. If False, the gates have all
                slightly different capacitance.
            crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk.

        Returns:
            None

        """
        # assumes n gates = n dots
        self._dot_gate_mutual_capacitance_matrix = np.identity(self.num_gates) * c0

        if crosstalk_strength != 0:     # takes care of off diagonal elements if we want crosstalk
            for i in range(self.num_gates):
                gate = self._physical_dot_locations[i]

                for j in range(i + 1, self.num_dots):
                    dot = self._physical_dot_locations[j]
                    distance = calculate_distance(gate, dot)**2     # squared, to lower the effect of crosstalk

                    if distance <= 2.5:
                        self._dot_gate_mutual_capacitance_matrix[i, j] = \
                            random.uniform(c0/10, c0/3) * crosstalk_strength * 2
                        self._dot_gate_mutual_capacitance_matrix[j, i] = self._dot_gate_mutual_capacitance_matrix[i, j]

        # add random noise to the diagonal elements if we want non-equal gates
        if not equal_gates:
            rdn = random_diagonal_noise(self.num_gates, c0)
            self._dot_gate_mutual_capacitance_matrix = self.dot_gate_mutual_capacitance_matrix + rdn

    def evaluate_dot_gate_mutual_capacitance_matrix_crossbar(self, c0, equal_gates, crosstalk_strength):

        """
        Evaluate the dot-gate mutual capacitance matrix characterizing the quantum dot device based on physical dot
        locations and diagonal shared control.

        Non-equal gates and cross-talk are implemented via the addition of random values.

        Args:
            c0 (float): The dot-gate stronger mutual capacitance value.
            equal_gates (bool): If True, all gates have the same gate-dot capacitance. If False, the gates have all
                slightly different capacitance.
            crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk. Default is 0. Larger values of
                    crosstalk_strength correspond to stronger crosstalk, but are not suggested.

        Returns:
            None

        """
        num_dots_per_side = round(np.sqrt(self.num_dots))
        num_diagonals = (num_dots_per_side - 1) * 2 + 1

        # Compute index gate - dot representation of the matrix [ (gate_index, dot_index), ... ]
        gate_dot_coupled_pairs = []
        i = 0
        for d in range(num_dots_per_side - 1):
            for _ in range(d + 1):
                # upper left
                gate_dot_coupled_pairs.append((d, i))
                # lower right
                gate_dot_coupled_pairs.append((num_diagonals - 1 - d, self.num_dots - 1 - i))
                i += 1
        for j in range(num_dots_per_side):
            # main diagonal
            gate_dot_coupled_pairs.append((num_dots_per_side - 1, i))
            i += 1

        # Add non-equal gates if needed
        noise = 0
        if not equal_gates:
            noise = c0/2

        capacitance_matrix = []
        for i in range(num_diagonals):
            random_value = np.random.random()
            capacitance_matrix.append([c0 + noise * random_value if (i, j) in gate_dot_coupled_pairs else 0 for j in
                                       range(self.num_dots)])

        self._dot_gate_mutual_capacitance_matrix = np.array(capacitance_matrix)
        # Add crosstalk
        if crosstalk_strength != 0:
            self._add_crosstalk_to_crossbar(gate_dot_coupled_pairs, crosstalk_strength, c0)

        self._dot_gate_mutual_capacitance_matrix = self.dot_gate_mutual_capacitance_matrix.T

    @property
    def device_type(self):
        return self._device_type

    @property
    def num_dots(self):
        return self._num_dots

    @property
    def num_gates(self):
        return self._num_gates

    @property
    def c0(self):
        return self._c0

    @property
    def physical_dot_locations(self):
        return self._physical_dot_locations

    # @property
    # def physical_gate_locations(self):
    #     return self._physical_gate_locations

    @property
    def dot_dot_mutual_capacitance_matrix(self):
        return self._dot_dot_mutual_capacitance_matrix

    @property
    def dot_gate_mutual_capacitance_matrix(self):
        return self._dot_gate_mutual_capacitance_matrix

    # internal functions

    def _fill_dot_dot_distance(self, c0, equal_dots):

        """
        Fill the dot-dot mutual capacitance matrix using a distance-based model (and eventually add random noise).

        Args:
            c0 (float): It is the dot naked self-capacitance.
            equal_dots (bool): If True, all dots have the same capacitance. If False, the dots have all slightly
                    different capacitance. It adds some random noise to the diagonal of the matrix. The maximum noise
                    is 25% of the dot self capacitance c0.

        Returns:
            None

        """
        # assume all dots have same self capacitance
        for lv1 in range(self._num_dots):
            r1 = self._physical_dot_locations[lv1]
            for lv2 in range(lv1+1, self._num_dots):
                r2 = self._physical_dot_locations[lv2]
                big_r = calculate_distance(r1, r2)    # distance between dots
                if big_r <= 1.5:    # define a cap for the distance
                    c = c0 * 0.66 / big_r**2   # squared to reduce effect.
                    # In yang paper, C12 is 66% of the self capacitance.
                    self._dot_dot_mutual_capacitance_matrix[lv1, lv2] = c
                    self._dot_dot_mutual_capacitance_matrix[lv2, lv1] = c
                    assert not np.isnan(c) and not np.isinf(c)

        # if dots do not have equal self capacitance, add some random noise to the diagonal
        if not equal_dots:
            rdn = random_diagonal_noise(self.num_dots, c0)
            self._dot_dot_mutual_capacitance_matrix = self.dot_dot_mutual_capacitance_matrix + rdn/4

    def _add_crosstalk_to_crossbar(self, gate_dot_coupled_tuples, crosstalk_strength, c0):
        """
        Add crosstalk to the dot-gate mutual capacitance matrix of a crossbar array of dots with diagonal shared
        control.

        The crosstalk is added to the matrix in the form of random values. The crosstalk is added to the nearest
        neighbors of the gates. It has the same value for all the nearest neighbors of a given gate.

        Args:
            gate_dot_coupled_tuples (list of 2-tuples): A list of 2-tuples representing the indices of the gates and
                    the corresponding controlled dots. E.g. [(0, 0), (1, 1), (1, 2), (2, 3)] in a 2x2 crossbar array.

            crosstalk_strength (float): If 0, no crosstalk. If 1, full crosstalk. Default is 0. Larger values of
                    crosstalk_strength correspond to stronger crosstalk, but are not suggested.

            c0 (float): The dot-gate stronger mutual capacitance value.

        Returns:
            None

        """
        # step 1: find the gate-dot tuples that are coupled by crosstalk (nearest neighbors)

        subtract_gate_indices = [tup for tup in gate_dot_coupled_tuples if tup[0] != 0]
        add_gate_indices = [tup for tup in gate_dot_coupled_tuples if tup[0] != self.num_gates - 1]

        crosstalk_subtracted = [(tup[0] - 1, tup[1]) for tup in subtract_gate_indices]
        crosstalk_added = [(tup[0] + 1, tup[1]) for tup in add_gate_indices]

        crosstalk_tuples = crosstalk_subtracted + crosstalk_added

        # step 2: transform it to a dictionary in which [[gate_index,[affected_dots]], ..]

        result_dict = {}

        # Iterate through the input list and group the values by the first element
        for tup in crosstalk_tuples:
            key = tup[0]
            value = tup[1]
            if key in result_dict:
                result_dict[key].append(value)
            else:
                result_dict[key] = [value]

        # Convert the dictionary into a list of lists
        result_list = [[key, values] for key, values in result_dict.items()]

        # step 3: add crosstalk to the matrix

        for key, values in result_list:
            cross_talk_values = random.uniform(c0 / 10, c0 / 3) * crosstalk_strength * 2
            self._dot_gate_mutual_capacitance_matrix[key, values] = cross_talk_values

    def plot_device(self, sensor_locations=None, sensor_labels=False, dots_labels=True, custom_dot_labels=None, save_plot_to_filepath=None):

        """
        Generates a plot of the quantum dot device for illustrative purposes, and saves the plot is the path file is
        provided.

        This method generates a plot of the quantum dot device, with sensors represented as triangles, and dots as
        circles. Gates are plotted only for the crossbar type, and are represented as lines.

        Args:
            sensor_locations (list of 2-tuple, optional): A list of 2-tuples representing the coordinates (x,y) of
                    each sensor. If None, no sensors are plotted. Default is None.
            sensor_labels (bool, optional): If True, the sensors are labeled with their index. Default is False.
            dots_labels (bool, optional): If True, the dots are labeled with their index. Default is True.
            custom_dot_labels (list of str, optional): A list of strings representing the custom labels of the dots. If
                    None, the dots are labeled with their index. Default is None.
            save_plot_to_filepath (str, optional): File path (including name and extension) to save the plots. If None,
                    the plots will. not be saved. Default is None.

        Returns:
            None

        """
        fig = self._draw_physical_device(dot_labels=dots_labels, custom_dot_labels=custom_dot_labels,
                                         sensor_labels=sensor_labels, sensor_locations=sensor_locations)

        # Add gates if crossbar
        if self._device_type == "crossbar":
            self._add_crossbar_gates_to_device_plot()

        plt.figure(fig)

        # Save if desired
        if save_plot_to_filepath is not None:
            plt.savefig(f"{save_plot_to_filepath}", bbox_inches='tight')

    def _draw_physical_device(self, dot_labels, custom_dot_labels, sensor_labels, sensor_locations):
        """
        Draws the physical device, with sensors represented as triangles, and dots as circles.

        Args:
            dot_labels (bool): If True, the dots are labeled with their index.
            custom_dot_labels (list of str): A list of strings representing the custom labels of the dots. If None,
                    the dots are labeled with their index. Default is None.
            sensor_labels (bool): If True, the sensors are labeled with their index.
            sensor_locations (list of 2-tuple): A list of 2-tuples representing the coordinates (x,y) of
                    each sensor. If None, no sensors are plotted. Default is None.

        Returns:
            fig: The figure object of the plot.

        """

        plot_style()

        physical_dot_locations = self.physical_dot_locations

        if sensor_locations is None:
            all_locations = physical_dot_locations
        else:
            all_locations = physical_dot_locations + sensor_locations

        assert self.physical_dot_locations is not None

        fig, ax = plt.subplots(figsize=(3.40457, 1.8), dpi=300)
        fig.subplots_adjust(bottom=0.2, top=0.95, left=0.125, right=0.885)

        for axis in ['top', 'bottom', 'left', 'right']:
            ax.spines[axis].set_linewidth(0.5)
        ax.tick_params(width=0.5, which='both')
        ax.tick_params(length=2.5, which='major')
        ax.tick_params(length=1.5, which='minor')

        #####

        x_values = [int(point[0]) for point in all_locations]
        y_values = [int(point[1]) for point in all_locations]

        # Evaluate the minimum and maximum values for x and y
        x_min = min(x_values)
        x_max = max(x_values)
        y_min = min(y_values)
        y_max = max(y_values)

        # Define the tick values and labels within the evaluated ranges
        x_tick_values = [x for x in range(x_min, x_max + 1) if x in x_values]
        x_tick_labels = [int(value) for value in x_tick_values]
        y_tick_values = [y for y in range(y_min, y_max + 1) if y in y_values]
        y_tick_labels = [int(value) for value in y_tick_values]

        #####

        ax.set_xticks(x_tick_values)
        ax.set_xticklabels(x_tick_labels, fontsize=8)
        ax.set_yticks(y_tick_values)
        ax.set_yticklabels(y_tick_labels, fontsize=8)
        ax.set_xlabel('X Location (au)', fontsize=8)
        ax.set_ylabel('Y Location (au)', fontsize=8, labelpad=3)
        ax.set_title('Physical device', fontsize=8)
        ax.grid(True, which='both', linewidth=0.1)

        physical_dot_locations = np.array(physical_dot_locations)

        x_left_dots = np.min(physical_dot_locations[:, 0])
        x_right_dots = np.max(physical_dot_locations[:, 0])

        y_bot_dots = np.min(physical_dot_locations[:, 1])
        y_top_dots = np.max(physical_dot_locations[:, 1])

        for lv in range(self.num_dots):
            legend = "Dot" if lv == 0 else "_nolegend_"
            if dot_labels:
                if custom_dot_labels is not None:
                    txt = custom_dot_labels[lv]
                else:
                    txt = "D" + str(lv)
                plt.annotate(txt, physical_dot_locations[lv, :])
            plt.scatter(*physical_dot_locations[lv], marker='o', label=legend, color="red")

        # Now for sensors as well
        if sensor_locations is not None:
            sensor_locations = np.array(sensor_locations)

            x_left_sensors = np.min(sensor_locations[:, 0])
            x_right_sensors = np.max(sensor_locations[:, 0])

            y_bot_sensors = np.min(sensor_locations[:, 1])
            y_top_sensors = np.max(sensor_locations[:, 1])
            for lv, _ in enumerate(sensor_locations):
                legend = "Sensor" if lv == 0 else "_nolegend_"
                if sensor_labels:
                    txt = "S" + str(lv)
                    plt.annotate(txt, sensor_locations[lv, :])

                plt.scatter(*sensor_locations[lv], marker='v', label=legend, color="green")
            x_left = min(x_left_dots, x_left_sensors)
            x_right = max(x_right_dots, x_right_sensors)
            y_bot = min(y_bot_dots, y_bot_sensors)
            y_top = max(y_top_dots, y_top_sensors)

        else:
            x_left = x_left_dots
            x_right = x_right_dots
            y_bot = y_bot_dots
            y_top = y_top_dots

        width = x_right - x_left
        height = y_top - y_bot

        width_scale = 1.5
        height_scale = 1.5

        x_left -= (width_scale - 1) * width
        x_right += (width_scale - 1) * width
        y_bot -= (height_scale - 1) * height
        y_top += (height_scale - 1) * height

        plt.rc('font', size=15)
        plt.rc('axes', titlesize=15)
        plt.xlim([x_left, x_right])
        plt.ylim([y_bot, y_top])
        plt.xlabel("X Location (au)")
        plt.ylabel("Y Location (au)")
        plt.legend()

        # plt.tight_layout()

        return fig

    def _add_crossbar_gates_to_device_plot(self):
        """
        Adds gates to the plot of the crossbar device.

        The gates are represented as sloped lines, crossing the dots they control. The gates are labeled with their
        index.

        Returns:
            None

        """

        plot_style()

        # Aesthetic code below to plot gates and label them
        num_gates = self.num_gates
        num_dots_side = int(np.sqrt(self.num_dots))

        for lv in range(num_gates):
            mid_gate = (num_gates - 1) / 2
            x_min = -1 if lv < mid_gate else -1 + (lv - mid_gate)
            x_max = 1 + lv if lv < mid_gate else num_dots_side
            x = np.linspace(x_min, x_max)
            m = 1
            b = (num_gates - 1) / 2 - lv
            plt.plot(x, m * x + b, label="Gate" if lv == 0 else "_no label_", color='hotpink')
            text = "G" + str(lv)
            text_x = lv + 1 if lv < mid_gate else num_dots_side
            text_y = num_dots_side if lv < mid_gate else num_dots_side - (lv - mid_gate)

            plt.annotate(text, (text_x, text_y))
        plt.legend(bbox_to_anchor=(1, 1), loc="upper left")

#######################################################################################################################
# Auxiliary functions used within the class


def get_lattice(n):

    """
    It generates a square lattice of size N x N. N must be a positive integer, strictly greater than 1.

    Args:
        n (int): size of the lattice

    Returns:
        list: list of tuples (i, j)

    Note:
        Return a list of tuples (i, j) where i, j are matrix indices in the order so that
        [(0, N-1), (0, N-2), (1, N-1), (0, N-3), (1, N-2), (2, N-1), ..., (N-2, N-1), (0, 0), (1, 1), ..., (N-1, N-1),
         ..., (N-1, 0)]. i.e., the indices are ordered as if the matrix was flattened and the elements were read on the
        diagonals from the top right to the bottom left.

        For example, if N = 3, the function returns
        [(0, 2), (0, 1), (1, 2), (0, 0), (1, 1), (2, 2), (1, 0), (2, 1), (2, 0)]

    """

    lattice = []
    tail = []
    for d in range(1, n):
        temp = []
        for i in range(d):
            lattice.append((i, n - d + i))
            temp.append((n - d + i, i))
        tail = temp + tail
    for i in range(n):
        lattice.append((i, i))
    lattice.extend(tail)

    return lattice


def random_diagonal_noise(size, c0):
    """
    It generates a random diagonal noise matrix of size (size, size) with values between -c0/4 and c0/4.

    Args:
        size (int): size of the matrix
        c0 (float): scaling value of the noise

    Returns:
        numpy array: random diagonal noise matrix of size (size, size)

    """
    random_diagonal_noises = np.identity(size)
    for i in range(size):
        random_diagonal_noises[i, i] = random.uniform(-c0 / 4, c0 / 4)
    return random_diagonal_noises


def generate_1d_dots_location_array(n, distance_scale=1):

    """
    It generates a list of n points with coordinates (x,y) in a line, with distance_scale between each point.

    Args:
        n (int): number of points to be generated
        distance_scale (float): distance between each point, default is 1

    Returns:
        list: list of points with coordinates (x,y). E.g. [(x1,y1), (x2,y2), ...]

    """
    points = []
    for i in range(n):
        x = i * distance_scale
        y = 0  # Assuming the line is horizontal at y=0
        points.append((x, y))
    return points


def generate_2d_10_dots_location_array(distance_scale=1):

    """
    It generates a list of 10 points with coordinates (x,y) in a 2D plane, with distance_scale between each point.

    The coordinates of the points are pre-defined in a specific pattern.

    Args:
        distance_scale: distance between each point on the same line, default is 1

    Returns:
        list: list of points with coordinates (x,y). E.g. [(x1,y1), (x2,y2), ...]

    """
    points = [(1, 1), (2, 1), (3, 1), (4, 1), (1.5, 2), (2.5, 2), (3.5, 2), (1.5, 0), (2.5, 0), (3.5, 0)]
    new_points = []
    for point in points:
        x = point[0] * distance_scale
        y = point[1] * distance_scale
        new_points.append((x, y))

    return new_points
