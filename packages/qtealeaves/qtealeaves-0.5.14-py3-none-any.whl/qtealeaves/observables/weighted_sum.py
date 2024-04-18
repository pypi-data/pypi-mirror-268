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
Observable to measure the weighted sum of tensor product observables
"""

import numpy as np
from .tnobase import _TNObsBase
from .tensor_product import TNObsTensorProduct

__all__ = ["TNObsWeightedSum"]


class TNObsWeightedSum(_TNObsBase):
    r"""
    Class to measure observables which is the weighted sum of tensor product,
    which means of the type

    .. math::

        O = \sum_{i=0}^m \alpha_i\left( o_1^i\otimes o_2^i \otimes \dots \otimes o_n^i
        \right)

    where :math:`m` is the number of addends and :math:`n` the number of sites.
    For further informations about the single observable
    :math:`O_i=o_1^i\otimes o_2^i \otimes \dots \otimes o_n^i` see the documentation
    of :class:`TNObsTensorProduct`.

    The output of the measurement will be a dictionary where:

    - The key is the `name` of the observable
    - The value is its expectation value

    An example of this observable are Pauli decompositions of Hamiltonian, i.e.
    Hamiltonians written as a weighted sum of tensor product operators formed
    by Pauli matrices.
    They are usually used in the Quantum chemistry applications, such as
    the Variational Quantum Eigensolver.

    Parameters
    ----------
    name: str
        Name to identify the observable
    tp_operators: :class:`TNObsTensorProduct`
        Tensor product observables. Its length, i.e. the number of tensor product
        observables contained in it, shoud be the same of the number of complex
        coefficients.
    coeffs: list of complex
        Coefficients of the weighted sum for each tp_operators

    """

    def __init__(self, name, tp_operators, coeffs):
        if np.isscalar(coeffs):
            coeffs = [coeffs]
        self.tp_operators = [tp_operators]
        self.coeffs = [coeffs]

        _TNObsBase.__init__(self, name)

    @classmethod
    def empty(cls):
        """
        Documentation see :func:`_TNObsBase.empty`.
        """
        obj = cls(None, None, None)
        obj.name = []
        obj.tp_operators = []
        obj.coeffs = []

        return obj

    def __len__(self):
        """
        Provide appropriate length method
        """
        return len(self.name)

    def __iadd__(self, other):
        """
        Documentation see :func:`_TNObsBase.__iadd__`.
        """
        if isinstance(other, TNObsWeightedSum):
            self.name += other.name
            self.tp_operators += other.tp_operators
            self.coeffs += other.coeffs
        else:
            raise Exception("__iadd__ not defined for this type.")

        return self

    def from_pauli_string(self, name, pauli_string):
        """Initialize the observable from a qiskit chemistry pauli string format.
        First, outside of the function use the WeightedPauliOperator method to_dict()
        and then give that dict as input to this function

        Parameters
        ----------
        name: str
            Name of the observable
        pauli_string: dict
            Dictionary of pauli strings

        Returns
        -------
        None: None
        """
        assert (
            "paulis" in pauli_string.keys()
        ), "Dictionary is not in pauli string format"
        assert name not in self.name, f"Observable {name} already initialized"

        addends = pauli_string["paulis"]

        coeffs = []
        tp_operators = TNObsTensorProduct.empty()
        # First, we look at each term in the weighted sum
        for term in addends:
            string = term["label"]
            coef = term["coeff"]["real"] + 1j * term["coeff"]["imag"]
            operators = []
            sites = []
            for idx, pauli in enumerate(string):
                if pauli != "I":
                    operators.append(pauli)
                    sites.append([idx])

            tp_operators += TNObsTensorProduct(string, operators, sites)

            coeffs += [coef]

        obs_wt = TNObsWeightedSum(name, tp_operators, coeffs)
        self += obs_wt

        return None

    def read(self, fh, **kwargs):
        """
        Read the measurements of the correlation observable from fortran.

        Parameters
        ----------

        fh : filehandle
                Read the information about the measurements from this filehandle.
        """
        fh.readline()  # separator
        is_meas = fh.readline().replace("\n", "").replace(" ", "")
        self.is_measured = is_meas == "T"

        for name in self.name:
            if self.is_measured:
                value = fh.readline().replace("\n", "").replace(" ", "")
                value = np.array(value.split(","), dtype=float)

                yield name, value[0] + 1j * value[1]
            else:
                yield name, None

    def write(self, fh, **kwargs):
        """
        Write fortran compatible definition of observable to file.

        Parameters
        ----------

        fh : filehandle
                Write the information about the measurements to this filehandle.
        """
        operator_map = kwargs.get("operator_map")

        str_buffer = "------------------- tnobsweightedsum\n"

        str_buffer += "%d\n" % (len(self))

        for ii in range(len(self)):
            # Write observable name and number of TNObsTensorProduct
            str_buffer += "%d %s \n" % (len(self.tp_operators[ii]), self.name[ii])
            # Cycle over tensor product operators
            for jj in range(len(self.tp_operators[ii])):
                # Write coefficient of the string
                str_buffer += "(%30.15E, %30.15E) \n" % (
                    np.real(self.coeffs[ii][jj]),
                    np.imag(self.coeffs[ii][jj]),
                )
                # Write number of operators
                str_buffer += "%d \n" % (len(self.tp_operators[ii].operators[jj]))
                # Cycle over single operators
                for kk in range(len(self.tp_operators[ii].operators[jj])):
                    # Write number of sites on which the operator is defined
                    str_buffer += "%d \n" % (len(self.tp_operators[ii].sites[jj][kk]))
                    # Write operator ID and sites
                    sites = np.array(self.tp_operators[ii].sites[jj][kk]) + 1
                    sites_string = " ".join(sites.astype(str))
                    str_buffer += "%d " % (
                        operator_map[self.tp_operators[ii].operators[jj][kk]]
                    )
                    str_buffer += sites_string + " \n"
            str_buffer += ".true. \n"

        fh.write(str_buffer)
        return

    def write_results(self, fh, is_measured, **kwargs):
        """
        Write the results mocking a fortran output

        Parameters
        ----------
        fh : filehandle
            Write the information about the measurements to this filehandle.
        """
        # Write separator first
        fh.write("-" * 20 + "\n")
        # Assignment for the linter
        _ = fh.write("T \n") if is_measured else fh.write("F \n")

        if is_measured:
            for name_ii in self.name:
                fh.write(f"{np.real(self.results_buffer[name_ii])}, ")
                fh.write(f"{np.imag(self.results_buffer[name_ii])} \n")
