# This code is part of qtealeaves.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Module defining the convergence parameters for tensor network simulations.
"""

import os
from collections import OrderedDict
from qtealeaves import write_nml, StrBuffer
from qtealeaves.parameterized import _ParameterizedClass


__all__ = ["TNConvergenceParameters"]


class TNConvergenceParameters(_ParameterizedClass):
    """
    Handling of the convergence parameters for the tensor network
    simulations.

    **Arguments**

    max_iter : integer, optional
        Number of sweeps in the ground state search.
        default to 20

    abs_deviation : float, optional
        exit criterion for ground state search if the energy of the
        current sweep has an absolute deviation from the previous
        data points below this threshold.
        default to 4e-12

    rel_deviation : float, optional
        exit criterion for ground state search if the energy of the
        current sweep has a relative deviation from the previous data
        points below this threshold.
        default to 1e-12

    n_points_conv_check : int, optional
        number of points to check convergence, e.g., for the ground
        state search. If the value is smaller than the number of sweeps,
        the exit criteria for the sweeps will never be checked.
        default to 4

    max_bond_dimension : int, optional
        The maximal bond dimension used during the simulations.
        The default value is purely a starting point for testing
        simulations.
        default to 5

    data_type : str, optional
        The data precision used during the simulations. (Not queried for now).
        Values are automatic ("A"), single ("S"), double ("D"),
        singe complex ("C"), and double complex ("Z").
        The default value is "A".

    trunc_method: str, optional
        Method use to truncate the singular values. Default to "R".
        Available:
        - "R": use cut_ratio
        - "N": use maximum norm

    cut_ratio: float, optional
        If trunc_method="r":
            Cut ratio :math:`\\epsilon` after which the singular values are
            neglected, i.e. if :math:`\\lamda_1` is the bigger singular values
            then after an SVD we neglect all the singular values such that
            :math:`\\frac{\\lambda_i}{\\lambda_1}\\leq\\epsilon`.
        If trunc_method="n":
            Maximum value of the norm neglected for the singular values during
            the trunctation.
        Default to 1e-9

    increase_precision
        TBA

    measure_obs_every_n_iter : int
        Modulo for measuring statics every n iterations. Not
        propagated through yet on the fortran side.

    svd_ctrl : character, optional
        Control for the SVD algorithm, either 'V', 'D', or 'E'
        Default to 'V'.

    random_sweep : bool
        Use random sweep scheme instead of default scheme.

    skip_exact_rgtensors : logical, optional
        Allows to skip space expansion if the tensors has already
        reached the maximal bond dimension of the underlying
        local Hilbert spaces, i.e., full Hilbert space is captured
        without truncation of entanglement. Only applies to
        sweep with space expansion.
        Default to False.

    svd_threshold : float
        TBA (only first accessed if array on fortran side)

    min_expansion : int, optional
        Bond dimension expansion used in the fortran code for a single
        site optimization. The bond dimension is increased of this integer.
        It is also used in the python simulation to increase the
        bond dimension when doing an expanding QR. In that case,
        the integer represent the percentage.
        Default to 10.

    expansion_cycles
        TBA

    arnoldi_initial_tolerance
        TBA

    arnoldi_min_tolerance
        TBA

    arnoldi_max_tolerance
        TBA

    aggression_tolerance
        TBA

    aggression_expansion
        TBA

    statics_method : integer, optional
        Method to run ground state search for this/all iteration.
        0 : default (1)
        1 : sweep
        2 : sweep with space expansion (can still be reduced to sweep
            during the simulation based on a energy condition)
        3 : imaginary time evolution with TDVP single-site

    imag_evo_dt : float, optional
        Time-step size for the imaginary time evolution.
        Default to 0.1.

    filename_conv : str, optional
        The convergence parameters are saved under this filename
        inside the input folder.
        default to ``ConvergenceInput.dat``

    trunc_tracking_mode : str, optional
        Modus for storing truncation, 'M' for maximum, 'C' for
        cumulated of the singvals squared (Norm truncated) (default).

    """

    def __init__(
        self,
        max_iter=20,
        abs_deviation=4e-12,
        rel_deviation=1e-12,
        n_points_conv_check=4,
        max_bond_dimension=5,
        trunc_method="R",
        cut_ratio=1e-9,
        increase_precision=False,
        measure_obs_every_n_iter=1,
        svd_ctrl="V",
        random_sweep=False,
        skip_exact_rgtensors=False,
        svd_threshold=1e-15,
        min_expansion=20,
        expansion_cycles=1,
        arnoldi_initial_tolerance=1e-2,
        arnoldi_min_tolerance=0.0,
        arnoldi_max_tolerance=1e-2,
        aggression_tolerance=1.0,
        aggression_expansion=1.0,
        statics_method=2,
        imag_evo_dt=0.1,
        filename_conv="ConvergenceInput.dat",
        trunc_tracking_mode="C",
        data_type="A",
    ):
        self.filename_conv = filename_conv

        # Convergence parameters for statics / decision on convergence
        self.max_iter = max_iter
        self.abs_deviation = abs_deviation
        self.rel_deviation = rel_deviation
        self.n_points_conv_check = n_points_conv_check
        self.measure_obs_every_n_iter = measure_obs_every_n_iter
        self.svd_ctrl = svd_ctrl

        # Consumed in python
        self.trunc_method = trunc_method.upper()
        self.cut_ratio = cut_ratio
        self.trunc_tracking_mode = trunc_tracking_mode.upper()

        # Settings for one or all iterations
        self.sim_params = {}
        self.sim_params["max_bond_dimension"] = max_bond_dimension
        self.sim_params["increase_precision"] = increase_precision
        self.sim_params["random_sweep"] = random_sweep
        self.sim_params["skip_exact_rgtensors"] = skip_exact_rgtensors
        self.sim_params["svd_threshold"] = svd_threshold
        self.sim_params["min_expansion"] = min_expansion
        self.sim_params["expansion_cycles"] = expansion_cycles
        self.sim_params["arnoldi_initial_tolerance"] = arnoldi_initial_tolerance
        self.sim_params["arnoldi_min_tolerance"] = arnoldi_min_tolerance
        self.sim_params["arnoldi_max_tolerance"] = arnoldi_max_tolerance
        self.sim_params["aggression_tolerance"] = aggression_tolerance
        self.sim_params["aggression_expansion"] = aggression_expansion
        self.sim_params["statics_method"] = statics_method
        self.sim_params["imag_evo_dt"] = imag_evo_dt
        self.sim_params["data_type"] = data_type

    def prepare_parameters_for_iteration(self, params):
        """
        Preparation to write parameters for each iteration. It checks
        if a list of convergence settings has to be written and builds
        a dictionary with the resolved entries for each parameters,
        which is either a the value or a list of values.

        **Arguments**

        params : dict
            Dictionary with the simulation parameters.

        **Results**

        has_vector_of_settings : bool
            True if settings change over the iterations and
            the parameters have to be written for each iteration.

        sim_param_all : dict
            Contains the resolved convergence parameters, i.e.,
            strings and functions are resolved with the actual values.
        """
        max_iter = self.eval_numeric_param(self.max_iter, params)

        sim_params_all = {}
        has_vector_of_settings = False

        str_params = ["data_type"]

        for key, value in self.sim_params.items():
            if isinstance(value, str):
                # Have to catch strings first as they have a length
                # attribute
                if key in str_params:
                    # String parameters
                    entry = self.eval_str_param(value, params)
                else:
                    # Numeric parameters
                    entry = self.eval_numeric_param(value, params)
            elif hasattr(value, "__len__"):
                # List of any kind
                if key in str_params:
                    # String parameters
                    entry = [
                        self.eval_str_param(value[ii], params)
                        for ii in range(len(value))
                    ]
                else:
                    # Numeric parameters
                    entry = [
                        self.eval_numeric_param(value[ii], params)
                        for ii in range(len(value))
                    ]
            else:
                # Scalar values (cannot be a str parameter, which
                # would go into the first if)
                entry = self.eval_numeric_param(value, params)

            if isinstance(entry, str):
                # String never activates list
                pass
            elif hasattr(entry, "__len__"):
                has_vector_of_settings = True
                if len(entry) != max_iter:
                    raise Exception(
                        "Length of convergence parameter list for "
                        + "%s must match " % (key)
                        + "max_iter=%d." % (max_iter)
                    )

            sim_params_all[key] = entry

        return has_vector_of_settings, sim_params_all

    @property
    def max_bond_dimension(self):
        """
        Provide the getter method for this property important to
        the MPS emulator. It allows to get values without a
        dictionary, but prevents doing it if the values is not
        an integer.
        """
        value = self.sim_params["max_bond_dimension"]
        if hasattr(value, "__len__"):
            value = value[0]

        if isinstance(value, int):
            return value

        raise Exception("Try to use getter on non-int bond dimension.")

    @property
    def data_type(self):
        """
        Provide the getter method for this property important to
        the MPS emulator. It allows to get values without a
        dictionary, but prevents doing it if the values is not
        an integer. (Not queried from the MPS for now).
        """
        value = self.sim_params["data_type"]
        if isinstance(value, str):
            # Value is string itself, return first
            return value

        if hasattr(value, "__len__"):
            value = value[0]

        raise Exception("Try to use getter on non-str data type.")

    @property
    def min_expansion_qr(self):
        """
        Provide the getter method for this property important to
        the python emulator. It is the percentage of the bond dimension
        increase in the qr
        """
        value = self.sim_params["min_expansion"]
        if hasattr(value, "__len__"):
            value = value[0]

        if isinstance(value, int):
            return value / 100

        raise Exception("Try to use getter on non-valid min_expansion")

    def get_chi(self, params):
        """
        Shortcut to evaluate the bond dimension as numeric parameter.

        **Arguments**

        params : dict
            The parameter dictionary for the simulation.
        """
        return self.eval_numeric_param(self.sim_params["max_bond_dimension"], params)

    def write_input(self, folder_name, params):
        """
        Write convergence parameters for input version 2 and 3.

        **Arguments**

        folder_name : str
            Name of the input folder, where the file with the convergence
            parameters is written to.

        params : dict
            Dictionary with the simulation parameters.
        """
        # First build a dictionary which allows listed entries
        has_vector_of_settings, sim_params_all = self.prepare_parameters_for_iteration(
            params
        )

        filename_conv = self.eval_str_param(self.filename_conv, params)

        full_nml = os.path.join(folder_name, filename_conv)
        if not full_nml.endswith(".nml"):
            full_nml += ".nml"

        conv_params = OrderedDict()
        conv_params["num_cpoints"] = self.eval_numeric_param(
            self.n_points_conv_check, params
        )

        conv_params["max_iterations"] = self.eval_numeric_param(self.max_iter, params)

        conv_params["abs_dev"] = self.eval_numeric_param(self.abs_deviation, params)

        conv_params["rel_dev"] = self.eval_numeric_param(self.rel_deviation, params)

        conv_params["has_vector_of_settings"] = has_vector_of_settings

        conv_params["measure_obs_every_n_iter"] = self.eval_numeric_param(
            self.measure_obs_every_n_iter, params
        )

        if self.svd_ctrl in ["S", "V", "D"]:
            # Single characters are vulnerable to having some Hamiltonian
            # parameter named V etc
            conv_params["svd_ctrl"] = self.svd_ctrl
        else:
            conv_params["svd_ctrl"] = self.eval_str_param(self.svd_ctrl, params)

        file_content = StrBuffer()
        write_nml("CONV_VARS", conv_params, file_content)

        # Require maximum(1, ...) for skipping statics
        for ii in range(max(1, conv_params["max_iterations"])):
            sim_params_ii = OrderedDict()

            for key in self.sim_params:
                entry = sim_params_all[key]

                if isinstance(entry, str):
                    sim_params_ii[key] = entry
                elif hasattr(entry, "__len__"):
                    sim_params_ii[key] = entry[ii]
                else:
                    sim_params_ii[key] = entry

            write_nml("SIM_PARAMS", sim_params_ii, file_content)

            if not has_vector_of_settings:
                break

        with open(full_nml, "w+") as fh:
            fh.write(file_content())

        return full_nml
