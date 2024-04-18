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
import numpy as np
from shutil import rmtree

import qtealeaves as qtl
from qtealeaves import modeling
from qtealeaves.models import get_quantum_ising_1d


class TestsTTNsimulation(unittest.TestCase):
    def setUp(self):
        """
        Provide some default settings.
        """
        np.random.seed([11, 13, 17, 19])

        self.conv = qtl.convergence_parameters.TNConvergenceParameters(
            max_bond_dimension=16, cut_ratio=1e-16, max_iter=10
        )

        self.in_folder = "TEST_INPUT"
        self.out_folder = "TEST_OUTPUT"

    def tearDown(self):
        """
        Remove input and output folders again
        """
        if os.path.isdir(self.in_folder):
            rmtree(self.in_folder)
        if os.path.isdir(self.out_folder):
            rmtree(self.out_folder)

        return

    def run_ising(self, model, my_ops, my_obs):
        """
        Run TTN simulation and test results for ising model.
        """
        simulation = qtl.ATTNSimulation(
            model,
            my_ops,
            self.conv,
            my_obs,
            tn_type=5,
            tensor_backend=2,
            version_input_processor=3,
            folder_name_input=self.in_folder,
            folder_name_output=self.out_folder,
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
            simulation.run(elem, delete_existing_folder=True)
            results = simulation.get_static_obs(elem)

            msg = f"Energy vs energy via system size for J={jj} is wrong."
            self.assertAlmostEqual(results["energy"], -elem["L"], msg=msg)
            for ii in range(elem["L"]):
                self.assertAlmostEqual(
                    results["sz"][ii], -1, msg=f"Sz for J={jj} is wrong"
                )

            energy_0 = np.linalg.eigh(model.build_ham(my_ops, elem))[0][0]

            msg = f"Energy vs energy via ED for J={jj} is wrong."
            self.assertAlmostEqual(results["energy"], energy_0, msg=msg)

    def test_ising(self):
        """
        Testing Ising with TTNs
        """
        model, my_ops = get_quantum_ising_1d()

        my_obs = qtl.observables.TNObservables(num_trajectories=3)
        my_obs += qtl.observables.TNObsLocal("sz", "sz")

        self.run_ising(model, my_ops, my_obs)

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

        self.run_ising(model, my_ops, my_obs)

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

        simulation = qtl.ATTNSimulation(
            model,
            my_ops,
            self.conv,
            my_obs,
            tn_type=5,
            tensor_backend=2,
            version_input_processor=3,
            folder_name_input=self.in_folder,
            folder_name_output=self.out_folder,
            has_log_file=True,
            verbosity=False,
        )

        for elem in [
            {
                "L": 8,
            }
        ]:
            energy_0 = np.linalg.eigh(model.build_ham(my_ops, elem))[0][0]
            simulation.run(elem, delete_existing_folder=True)
            results = simulation.get_static_obs(elem)

            self.assertAlmostEqual(results["energy"], energy_0, msg=f"Energy is wrong")
