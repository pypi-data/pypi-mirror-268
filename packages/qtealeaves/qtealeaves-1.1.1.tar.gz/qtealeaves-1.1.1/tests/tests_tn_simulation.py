# This code is part of qtealeaves.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os
import unittest
import tempfile
from shutil import rmtree
import numpy as np

import qtealeaves as qtl
from qtealeaves import modeling
from qtealeaves.models import get_quantum_ising_1d


class TestsTNsimulation(unittest.TestCase):
    def setUp(self):
        """
        Provide some default settings.
        """
        np.random.seed([11, 13, 17, 19])

        self.conv = qtl.convergence_parameters.TNConvergenceParameters(
            max_bond_dimension=16, cut_ratio=1e-16, max_iter=10
        )
        self.ansatz = {5: "TTN", 6: "MPS"}

        self.temp_dir = tempfile.TemporaryDirectory()
        self.in_folder = os.path.join(self.temp_dir.name, "INPUT")
        self.out_folder = os.path.join(self.temp_dir.name, "OUTPUT")

    def tearDown(self):
        """
        Remove input and output folders again
        """
        self.temp_dir.cleanup()

        return

    def run_model(self, model, my_ops, my_obs):
        """
        Run TTN simulation and test results for ising model or similar.
        """

        for tn_type in self.ansatz.keys():
            in_folder = self.in_folder + f"TN{tn_type}"
            out_folder = self.out_folder + f"TN{tn_type}"

            simulation = qtl.QuantumGreenTeaSimulation(
                model,
                my_ops,
                self.conv,
                my_obs,
                tn_type=tn_type,
                tensor_backend=2,
                folder_name_input=in_folder,
                folder_name_output=out_folder,
                has_log_file=True,
                verbosity=False,
            )

            for elem in [
                {
                    "L": 8,
                    "J": 0.0,
                    "g": -1,
                }
            ]:
                jj = elem["J"]
                simulation.run(elem)
                results = simulation.get_static_obs(elem)
                prefix = f"For ansatz {self.ansatz[tn_type]} "
                msg = prefix + f"Energy vs energy via system size for J={jj} is wrong."
                self.assertAlmostEqual(results["energy"], -elem["L"], msg=msg)
                for ii in range(elem["L"]):
                    self.assertAlmostEqual(
                        results["sz"][ii], -1, msg=prefix + f"Sz for J={jj} is wrong"
                    )

                energy_0 = np.linalg.eigh(model.build_ham(my_ops, elem))[0][0]

                msg = prefix + f"Energy vs energy via ED for J={jj} is wrong."
                self.assertAlmostEqual(results["energy"], energy_0, msg=msg)

    def test_ising(self):
        """
        Testing Ising with TTNs
        """
        model, my_ops = get_quantum_ising_1d()

        my_obs = qtl.observables.TNObservables(num_trajectories=3)
        my_obs += qtl.observables.TNObsLocal("sz", "sz")

        self.run_model(model, my_ops, my_obs)

    def test_spinglass_1(self):
        """
        Testing spinglass with TTNs. In this first test, the random couplings
        are set to 1, in order to retrieve the same results of test_ising.
        """
        model_name = lambda params: "Spinglass_g%2.4f" % (params["g"])

        # test if we get the same results of ising by setting
        # the coupling to one
        get_zrand = lambda params: np.ones(params["L"])
        get_xrand = lambda params: np.ones((params["L"], params["L"]))

        model = modeling.QuantumModel(1, "L", name=model_name)
        model += modeling.RandomizedLocalTerm(
            "sz", get_zrand, strength="g", prefactor=-1
        )
        model += modeling.TwoBodyAllToAllTerm1D(
            ["sx", "sx"], get_xrand, strength="J", prefactor=-1
        )

        my_ops = qtl.operators.TNSpin12Operators()
        my_obs = qtl.observables.TNObservables()
        my_obs += qtl.observables.TNObsLocal("sz", "sz")

        self.run_model(model, my_ops, my_obs)

    def test_spinglass_2(self):
        """
        Testing spinglass with TTNs. In the second test, the energy with
        random couplings is compared with the result of exact diagonalization.
        """
        model_name = lambda params: "Spinglass"

        rvec = np.random.rand(8)
        rmat = np.random.rand(8, 8)

        def get_rvec(params, rvec=rvec):
            return rvec

        def get_rmat(params, rmat=rmat):
            return rmat

        get_zrand = get_rvec
        get_xrand = get_rmat

        model = modeling.QuantumModel(1, "L", name=model_name)
        model += modeling.RandomizedLocalTerm("sz", get_zrand, prefactor=-1)
        model += modeling.TwoBodyAllToAllTerm1D(["sx", "sx"], get_xrand, prefactor=-1)

        my_ops = qtl.operators.TNSpin12Operators()
        my_obs = qtl.observables.TNObservables()

        for tn_type in self.ansatz.keys():
            in_folder = self.in_folder + f"TN{tn_type}"
            out_folder = self.out_folder + f"TN{tn_type}"

            simulation = qtl.QuantumGreenTeaSimulation(
                model,
                my_ops,
                self.conv,
                my_obs,
                tn_type=tn_type,
                tensor_backend=2,
                folder_name_input=in_folder,
                folder_name_output=out_folder,
                has_log_file=True,
                verbosity=False,
            )

            for elem in [
                {
                    "L": 8,
                }
            ]:
                energy_0 = np.linalg.eigh(model.build_ham(my_ops, elem))[0][0]
                simulation.run(elem)
                results = simulation.get_static_obs(elem)

                prefix = f"For ansatz {self.ansatz[tn_type]} "
                self.assertAlmostEqual(
                    results["energy"], energy_0, msg=prefix + f"Energy is wrong"
                )

    def base_checkpoints_statics(self, intrasweep=False, mid_sweep=False, max_iter=3):
        """Base test for statics checkpoints."""
        model, my_ops = get_quantum_ising_1d()

        my_obs = qtl.observables.TNObservables()
        my_obs += qtl.observables.TNObsLocal("sz", "sz")

        if intrasweep:
            qtl.emulator.tn_simulation.QTEA_TIMELIMIT_INTRASWEEP_CHECKPOINTS = 0

        for tn_type in self.ansatz.keys():
            self.conv.max_iter = max_iter - 1

            in_folder = self.in_folder + f"TN{tn_type}"
            out_folder = self.out_folder + f"TN{tn_type}"

            if tn_type in [5]:
                sweep_order_short = [(1, 3), (1, 2), (1, 1), (1, 0), (0, 0)]
            elif tn_type in [6]:
                sweep_order_short = [0, 1, 2, 3]
            else:
                raise Exception("Define short sweep order for unit test.")

            simulation = qtl.QuantumGreenTeaSimulation(
                model,
                my_ops,
                self.conv,
                my_obs,
                tn_type=tn_type,
                tensor_backend=2,
                folder_name_input=in_folder,
                folder_name_output=out_folder,
                has_log_file=True,
                verbosity=False,
            )

            params = [
                {
                    "L": 8,
                    "J": 0.0,
                    "g": -1,
                }
            ]

            if mid_sweep:
                params[0]["sweep_order"] = sweep_order_short
                params[0]["exclude_from_hash"] = ["sweep_order", "exclude_from_hash"]

            sim_status = simulation.status(params)
            self.assertEqual(
                sim_status, (1, 0, 0), msg=f"Failed for TN {tn_type} & not started."
            )

            for elem in params:
                simulation.run(elem)

            # Reset conv params iterations and remove file tracking finished
            # simulations
            self.conv.max_iter = max_iter
            finished_json = os.path.join(out_folder, "has_finished.json")
            os.remove(finished_json)
            if mid_sweep:
                del params[0]["sweep_order"]
                del params[0]["exclude_from_hash"]

            sim_status = simulation.status(params)
            self.assertEqual(
                sim_status, (0, 1, 0), msg=f"Failed for TN {tn_type} & interrupted."
            )

            for elem in params:
                simulation.run(elem)

            sim_status = simulation.status(params)
            self.assertEqual(
                sim_status, (0, 0, 1), msg=f"Failed for TN {tn_type} & finished."
            )

    def test_checkpoints_statics(self):
        """Test the checkpoints of statics at end of sweep."""
        self.base_checkpoints_statics()

    def test_checkpoints_statics_intrasweep(self):
        """Test the checkpoints of statics intrasweep."""
        self.base_checkpoints_statics(intrasweep=True)

    def test_checkpoints_statics_intrasweep_midsweep(self):
        """Test the checkpoints of statics intrasweep and midsweep."""
        self.base_checkpoints_statics(intrasweep=True, mid_sweep=True, max_iter=2)

    def test_checkpoints_dynamics(self):
        """Test the checkpoints of a dynamics simulation."""
        model, my_ops = get_quantum_ising_1d()

        my_obs = qtl.observables.TNObservables()
        my_obs += qtl.observables.TNObsLocal("sz", "sz")

        # Dynamics
        quench = qtl.DynamicsQuench(
            "t_grid", measurement_period=2, time_evolution_mode=1
        )
        quench["g"] = lambda tt, params: 2.0 - 2.0 * (tt / 10.0)

        for tn_type in self.ansatz.keys():

            in_folder = self.in_folder + f"TN{tn_type}"
            out_folder = self.out_folder + f"TN{tn_type}"

            simulation = qtl.QuantumGreenTeaSimulation(
                model,
                my_ops,
                self.conv,
                my_obs,
                tn_type=tn_type,
                tensor_backend=2,
                folder_name_input=in_folder,
                folder_name_output=out_folder,
                has_log_file=True,
                verbosity=False,
            )

            params = []
            params.append(
                {
                    "L": 8,
                    "J": 1.0,
                    "g": 2.0,
                    "t_grid": [0.05] * 4,
                    "Quenches": [quench],
                    "exclude_from_hash": ["Quenches", "t_grid"],
                }
            )

            sim_status = simulation.status(params)
            self.assertEqual(
                sim_status, (1, 0, 0), msg=f"Failed for TN {tn_type} & not started."
            )

            simulation.run(params)

            # Prepare restart
            params[0]["t_grid"] = [0.05] * 6
            finished_json = os.path.join(out_folder, "has_finished.json")
            os.remove(finished_json)

            sim_status = simulation.status(params)
            self.assertEqual(
                sim_status, (0, 1, 0), msg=f"Failed for TN {tn_type} & interrupted."
            )

            simulation.run(params)

            sim_status = simulation.status(params)
            self.assertEqual(
                sim_status, (0, 0, 1), msg=f"Failed for TN {tn_type} & finished."
            )
