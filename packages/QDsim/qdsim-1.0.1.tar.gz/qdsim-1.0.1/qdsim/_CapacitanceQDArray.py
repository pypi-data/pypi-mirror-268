"""
@author: VGualtieri

"""
import numpy as np
import cvxpy as cp
from ._QuantumDotDevice import QDDevice
import time
import tqdm

# parallelize the code
import ray


def _matrices_dimension_test(qdd: QDDevice):
    assert np.shape(qdd.dot_dot_mutual_capacitance_matrix) == (qdd.num_dots, qdd.num_dots)
    assert np.all(qdd.dot_dot_mutual_capacitance_matrix == qdd.dot_dot_mutual_capacitance_matrix.T)
    assert np.all(qdd.dot_dot_mutual_capacitance_matrix >= 0)
    assert np.all(qdd.dot_gate_mutual_capacitance_matrix >= 0)


class CapacitanceQuantumDotArray:

    """
    Class for implementing the quantum dot device simulation within the framework of the constant interaction model.

    It is based on the solution of a convex optimisation problem, which is solved using the CVXPY package.
    It minimizes the free energy of the system, which is given by: F = U - q_G * V_G, with U = 1/2 * V^T * C * V,
    where V = ( V_D, V_G) is the vector of the dot and gate voltages, C is the maxwell capacitance matrix of the system,
    and q_G is the vector of the gate charges. The free energy is manipulated to be expressed as a function of N_D and
    V_G, where N_D is the vector of the dot occupations. The free energy is then minimized with respect to N_D, with
    the constraint that N_D is an integer vector. V_G is the parameter. The solution of the optimisation problem is the
    ground state of the system, i.e. the dot occupations in the ground state.

    The unit charge |e| is set to 1, so that the free energy is expressed in units of eV.

    The class is initialized with the following arguments:
    - simulate: it can be 'Electrons' or 'Holes', depending on the type of charge carriers to simulate

    The class has the following methods:
    - select_solver: it selects the solver to use for the convex optimisation problem. Possible solvers are 'MOSEK'
        (license required) and 'SCIP' (free)
    - probe_voltage_space: it probes the voltage space, i.e. it calculates the ground state of the system for all the
        points in the voltage space. It returns the dot occupations and the energy of the ground state for each point.
    - _find_ground_state: it finds the ground state of the system for a given point in the voltage space. It returns
        the dot occupations and the energy of the ground state for that point.
    - _set_up_convex_optimization_problem: it sets up the convex optimisation problem to be solved. It is called by
        _find_ground_state.
    - _evaluate_maxwell_matrices: it evaluates the maxwell capacitance matrix of the system. It is called by
        _set_up_convex_optimization_problem.
    - _mutual_to_maxwell: it converts the mutual capacitance matrix to the maxwell capacitance matrix. It is called by
        _evaluate_maxwell_matrices.
    - system_maxwell_matrix: it returns the maxwell capacitance matrix of the system.

    """

    unitCharge = 1  #ge  eV

    def __init__(self, simulate):
        self._quantum_dot_device = None
        self._simulate = simulate
        self._system_mutual_capacitance_matrix = None
        self._system_maxwell_matrix = None
        self._dot_dot_maxwell_matrix = None
        self._dot_gate_maxwell_matrix = None
        self._gate_gate_maxwell_matrix = None
        self._inverse_dot_dot_capacitance_matrix = None

        self._A = None
        self._b = None
        self._c = None
        self._x = None
        self._energy_expr = None
        self._ground_state_problem = None

        self._solver = 'SCIP'  # default solver, open source

    def select_solver(self, solver: str):

        """
        Select the solver to use for the convex optimisation problem.

        Args:
            solver (str): e.g. 'MOSEK' (license required) or 'SCIP' (free)

        Returns:
            None
        """
        self._solver = solver

    def probe_voltage_space(self, qd_simulator, use_ray=False):

        """
        Function which probes the voltage space, i.e. calculates the ground state of the system for all the points in
        the voltage space.

         It returns the dot occupations and the energy of the ground state for each point. It calls
        _find_ground_state for each point in the voltage space.

        Args:
            qd_simulator (QDSimulator): the quantum dot device simulator object

        Returns:
            occupation_arr (np.array): array of the dot occupations in the ground state for each point in the voltage
                space
            energy_arr (np.array): array of the energy of the ground state for each point in the voltage space
            time_list (list): list of the time taken by the convex optimisation problem for each point in the voltage
                space

        """

        num_probe_points = qd_simulator.num_probe_points
        qd_device = qd_simulator.qd_device
        self._set_up_convex_optimization_problem(qd_device)

        # initialise arrays for storing results
        occupation_arr = np.zeros(shape=(num_probe_points, qd_device.num_dots))
        energy_arr = np.zeros(shape=num_probe_points)

        time_list = []

        # parallelize the code using ray
        if use_ray:
            # Initialize a Ray cluster only when using ray
            ray.init(ignore_reinit_error=True)
            # List to store Ray remote tasks
            tasks = []

            for lv, voltage in enumerate(tqdm.tqdm(qd_simulator.voltage_array)):
                # Call _find_ground_state_remote as a remote task and pass the 'voltage' argument
                task = self._find_ground_state_remote.remote(self, voltage)
                tasks.append(task)

            # Gather results from the remote tasks if using ray
            results = ray.get(tasks)
            for lv, result in enumerate(results):
                occupation, energy, timestep = result
                occupation_arr[lv, :] = occupation
                energy_arr[lv] = energy
                time_list.append(timestep)

            # Shutdown the Ray cluster if using ray
            ray.shutdown()

        else:
            for lv, voltage in enumerate(tqdm.tqdm(qd_simulator.voltage_array)):
                occupation, energy, timestep = self._find_ground_state(voltage)
                occupation_arr[lv, :] = occupation
                energy_arr[lv] = energy
                time_list.append(timestep)

        return occupation_arr, energy_arr, time_list

    @ray.remote
    def _find_ground_state_remote(self, voltage):
        """
        Function which finds the ground state of the system for a given point in the voltage space.
        It is used for parallelization.

        It returns the dot
        occupations and the energy of the ground state for that point. It also returns the time taken by the convex
        optimisation problem to find the ground state for the given point in the voltage space. It solves the convex
        optimisation problem.

        Args:
            voltage (np.array): array of the gate voltages. The length of the array must be equal to the number
                    of gates of the system. The order of the gates must be the same as the order of the gates in the
                    quantum dot device object.

        Returns:
            occupation (list): list of the dot occupations in the ground state for the given point in the voltage
                    space.
            energy (float): energy of the ground state for the given point in the voltage space.
            timestep (float): time taken by the convex optimisation problem to find the ground state for the given
                    point in the voltage space. It is expressed in seconds.

        """
        occupation, energy, timestep = self._find_ground_state(voltage)
        return occupation, energy, timestep

    def _find_ground_state(self, gate_voltages):

        """
        Function which finds the ground state of the system for a given point in the voltage space. It returns the dot
        occupations and the energy of the ground state for that point. It solves the convex optimisation problem.

        The occupation of each dot is the decision variable of the optimisation problem. The free energy is expressed
        as a function of the dot occupations and the gate voltages. The free energy is minimized with respect to the dot
        occupations, with the constraint that the dot occupations are integer numbers. The gate voltages are the
        parameters of the problem.

        The solution may not be unique, but it is guaranteed to be the ground state of the system.

        Args:
            gate_voltages (np.array): array of the gate voltages. The length of the array must be equal to the number
                    of gates of the system. The order of the gates must be the same as the order of the gates in the
                    quantum dot device object.

        Returns:
            ground_state_occupations (list): list of the dot occupations in the ground state for the given point in the
                    voltage space.
            ground_state_energy (float): energy of the ground state for the given point in the voltage space. It is
                    expressed in units of eV.
            wall_time (float): time taken by the convex optimisation problem to find the ground state for the given
                    point in the voltage space. It is expressed in seconds.

        """

        # NEW ENERGY FUNCTION
        # _A stays the same, already calculated
        if self._simulate == 'Electrons':
            self._b.value = - self.unitCharge * (gate_voltages.T @ self._dot_gate_maxwell_matrix.T @
                                                 self._inverse_dot_dot_capacitance_matrix)
        else:
            self._b.value = self.unitCharge * (gate_voltages.T @ self._dot_gate_maxwell_matrix.T @
                                               self._inverse_dot_dot_capacitance_matrix)

        # self._c.value = gate_voltages.T @ self._dot_gate_maxwell_matrix.T @ self._inverse_dot_dot_capacitance_matrix @\
        #     self._dot_gate_maxwell_matrix @ gate_voltages
        self._energy_expr = 0.5 * (cp.quad_form(self._x, self._A)) - self._b.T @ self._x  # + 0.5 * self._c
        self._ground_state_problem = cp.Problem(cp.Minimize(self._energy_expr), [self._x >= 0])  # constraint on N >= 0

        # measure time
        tic = time.time()
        # solve the problem
        self._ground_state_problem.solve(solver=self._solver, warm_start=True)
        toc = time.time()
        wall_time = toc - tic
        assert self._ground_state_problem.status == 'optimal'

        ground_state_occupations = self._x.value
        assert np.all([abs(a - np.rint(a)) < 1e-4 for a in ground_state_occupations])
        ground_state_occupations = [np.rint(a) for a in ground_state_occupations]
        ground_state_energy = self._ground_state_problem.value

        return ground_state_occupations, ground_state_energy, wall_time

    def _set_up_convex_optimization_problem(self, qdd: QDDevice):

        """
        Function which sets up the convex optimisation problem to be solved. It is called by _find_ground_state.

        The occupation of each dot is the decision variable of the optimisation problem. The free energy is expressed
        as a function of the dot occupations and the gate voltages. The free energy is minimized with respect to the dot
        occupations, with the constraint that the dot occupations are integer numbers. The gate voltages are the
        parameters of the problem.

        Args:
            qdd (QDDevice): the quantum dot device object to be simulated

        Returns:
            None

        """
        # Tests to ensure dimensions are as assumed and matrices symmetric where required
        _matrices_dimension_test(qdd)

        self._evaluate_maxwell_matrices(qdd)

        # # The Free energy equation is:
        # # U(N)= 1/2 * (e^2 * N^T*Ec*N - 2*e * (C_DG V_G)^T*Ec*N + (C_DG V_G)^T * Ec * (C_DG V_G))
        # # where N is the vector of dot occupations, Ec is the charging energy matrix C_DD^(-1),
        # # C_DG is the dot-gate maxwell capacitance matrix,
        # # Write as U(N) = 0.5 * N*_A*N - _b*N + 0.5*_c -->
        # # _A = Ec *e^2
        # # _b = +/- |e| (C_DG @ V_G)^T @ Ec, depends on whether we are simulating electrons (-) or holes (+)

        # NB we do NOT store the 0.5 as part of the _A expression
        self._A = self._inverse_dot_dot_capacitance_matrix * (self.unitCharge ** 2)
        self._b = cp.Parameter(qdd.num_dots)
        self._c = cp.Parameter()
        self._x = cp.Variable(qdd.num_dots, integer=True)

    def _evaluate_maxwell_matrices(self, qdd: QDDevice):

        """
        Function which evaluates the maxwell capacitance matrix of the system. It is called by
        _set_up_convex_optimization_problem.

        It also evaluates the dot-dot, dot-gate and gate-gate maxwell capacitance matrices. These are used to calculate
        the free energy of the system.

        Args:
            qdd (QDDevice): the quantum dot device object to be simulated

        Returns:
            None

        """
        # Calculate the maxwell capacitance matrix
        # C = [[C_DD, C_DG^T], [C_DG, C_GG]]
        # Dx(D+G) = DxD + DxG, ax=1
        tmp_left = np.concatenate((qdd.dot_dot_mutual_capacitance_matrix, qdd.dot_gate_mutual_capacitance_matrix),
                                  axis=1)
        # Gx(D+G) = GxD + GxG, ax = 1
        # NB here, the second matrix is the gate-gate capacitance matrix
        tmp_right = np.concatenate((qdd.dot_gate_mutual_capacitance_matrix.T, np.identity(qdd.num_gates)), axis=1)
        # (D+G)_x(D+G) = Dx(D+G) + Gx(D+G) , ax = 0
        self._system_mutual_capacitance_matrix = np.concatenate((tmp_left, tmp_right), axis=0)
        # check dimensions
        assert np.shape(self._system_mutual_capacitance_matrix) == (
            qdd.num_dots + qdd.num_gates, qdd.num_dots + qdd.num_gates)

        # finally, calculate the Maxwell matrix for hte whole system
        self._system_maxwell_matrix = self._mutual_to_maxwell()
        # NB per problem formulation, charging-energy matrix is C_DD^-1, BUT
        # this nonetheless includes the dot-gate capacitances, as they go to
        # the diagonal entries; effectively increasing self-capacitance

        # Get dot-dot portion of the block matrix
        self._dot_dot_maxwell_matrix = self._system_maxwell_matrix[:qdd.num_dots, :qdd.num_dots]
        # evaluate the E_C matrix
        self._inverse_dot_dot_capacitance_matrix = np.linalg.inv(self._dot_dot_maxwell_matrix)

        # Get dot-gate portion of the block matrix
        self._dot_gate_maxwell_matrix = self._system_maxwell_matrix[:qdd.num_dots, qdd.num_dots:]
        # Get gate-gate portion of the block matrix
        self._gate_gate_maxwell_matrix = self._system_maxwell_matrix[qdd.num_dots:, qdd.num_dots:]

        # check dimensions
        assert np.shape(self._dot_gate_maxwell_matrix) == (qdd.num_dots, qdd.num_gates)

    def _mutual_to_maxwell(self):

        """
        Function which converts the mutual capacitance matrix to the maxwell capacitance matrix.

        It is called by _evaluate_maxwell_matrices.
        The maxwell capacitance matrix is the capacitance matrix of the system, which
        includes the self-capacitances of the dots and gates. This capacitance matrix solves the electrostatic problem
        Q = CV, where Q is the vector of the charges, C is the maxwell capacitance matrix and V is the vector of the
        voltages. Specifically, Q = (Q_D, Q_G), where Q_D is the vector of the dot charges and Q_G is the vector of the
        gate charges. V = (V_D, V_G), where V_D is the vector of the dot voltages and V_G is the vector of the gate
        voltages. The maxwell capacitance matrix is given by C = [[C_DD, C_DG^T], [C_DG, C_GG]], where C_DD is the
        dot-dot mutual capacitance matrix, C_DG is the dot-gate mutual capacitance matrix and C_GG is the gate-gate
        mutual capacitance matrix. The dot-dot mutual capacitance matrix is a square matrix of size DxD, where D is the
        number of dots. The dot-gate mutual capacitance matrix is a matrix of size DxG, where G is the number of gates.
        The gate-gate mutual capacitance matrix is a square matrix of size GxG. The maxwell capacitance matrix is a
        matrix of size (D+G)x(D+G).


        Returns:
            system_maxwell_matrix (np.array): the maxwell capacitance matrix of the system (D+G)x(D+G)


        """
        system_maxwell_matrix = -1.0 * self._system_mutual_capacitance_matrix
        for lv in range(len(self._system_mutual_capacitance_matrix)):
            system_maxwell_matrix[lv, lv] = np.sum(self._system_mutual_capacitance_matrix[:, lv])
        return system_maxwell_matrix

    @property
    def system_maxwell_matrix(self):
        return self._system_maxwell_matrix
