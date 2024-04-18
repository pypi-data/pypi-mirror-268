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
Efficient operators to be used in TTN python simulator
"""

import numpy as np

# Try to import cupy
try:
    import cupy as cp
    from cupy_backends.cuda.api.runtime import CUDARuntimeError

    try:
        _ = cp.cuda.Device()
        GPU_AVAILABLE = True
    except CUDARuntimeError:
        GPU_AVAILABLE = False
except ImportError:
    cp = None
    GPU_AVAILABLE = False

__all__ = ["TensorProductOperator", "IndexedOperator"]


class IndexedOperator:
    """
    Class of operator with an index, to keep track
    of tensor product operators in the TTN, i.e.
    MPOs where the bond dimension is 1

    Parameters
    ----------
    op : np.ndarray or str
        Numpy array representing the operator or string of the
        operator
    op_id : int
        Integer op_id of the operator. Operators with the same
        op_id are considered to belong to the same MPO
    coeff : complex
        Coefficient of the operator
    """

    def __init__(self, op, op_id, coeff):
        self._op = op
        self._op_id = op_id
        self._coeff = coeff

    @property
    def op(self):
        """Operator property"""
        return self._op

    @property
    def op_id(self):
        """Operator ID property"""
        return self._op_id

    @property
    def coeff(self):
        """Coefficient property"""
        return self._coeff


class TensorProductOperator:
    """
    Effective operator class.
    It contains the effective operators in a vector with
    as many entries as links. The first `num_physical_links`
    are always used to store the physical hamiltonian.

    TODO: add read/write method for fortran

    Parameters
    ----------
    params:
        The simulation parameters
    model: QuantumModel
        Quantum model defining the quantum operator
    operators: TNOperators
        Class containing the tensors of the operators
    tensor_network: tensor network class
        Tensor network on which links the efficient operator is defined
    device : str, optional
        Device of the computation. Default to "cpu".
    """

    def __init__(self, params, model, operators, tensor_network, device="cpu"):
        # Initialize variables
        self.params = params
        self.model = model
        self.numx = self.model.get_number_of_sites_xyz(params)
        self._ops = operators
        self.num_physical_links = model.get_number_of_sites(params)
        self.num_links = tensor_network.num_links
        self.device = device
        if device == "gpu":
            if not GPU_AVAILABLE:
                raise RuntimeError("GPU is not available")
            for key, val in self._ops.ops.items():
                self._ops.ops[key] = cp.asarray(val)

        self.eff_ops = [[] for _ in range(self.num_links)]
        # Initialize the pysical layer
        self._extract_physical_terms(tensor_network)
        tensor_network.build_effective_operators(self)

    def __getitem__(self, idxs):
        """
        Get the hamiltonian term at index idxs.
        If one index is passed, you receive ALL the hamiltonian
        terms on link `idxs`. If a tuple is passed, then the
        second index is the index of the operator

        Parameters
        ----------
        idxs : int or tuple of ints
            Index of the link and optionally of the operator
            to retrieve

        Returns
        -------
        list of Operator
            efficient operator on the link
        """

        if np.isscalar(idxs):
            eff_ops = self.eff_ops[idxs]
        elif len(idxs) == 2:
            eff_ops = self.eff_ops[idxs[0]][idxs[1]]

        return eff_ops

    def __setitem__(self, idx, other):
        """
        Set the efficient operator on link idx

        Parameters
        ----------
        idx : int
            Index of the link where to substitute the
            effective operator
        other : list
            New list of effective operators in that link
        """
        if np.isscalar(idx):
            self.eff_ops[idx] = other
        else:
            raise ValueError(f"The index must be a scalar integer, not {type(idx)}")

    def __repr__(self):
        """
        Return the class name as representation.
        """
        return self.__class__.__name__

    def __len__(self):
        """
        Provide number of links in efficient operator
        """
        return self.num_links

    def __iter__(self):
        """Iterator protocol"""
        return iter(self.eff_ops)

    @property
    def ops(self):
        """Retrieve the dictionary of operators"""
        return self._ops.ops

    def add_operator(self, name, op):
        """
        Add an operator op named name to the list of
        operators

        Parameters
        ----------
        name : str
            String identifier of the operator
        op : np.ndarray
            Matrix of the operator
        """

        self._ops.ops[name] = op

    def _extract_physical_terms(self, tensor_network):
        """
        Compute the physical hamiltonians on the physical indexes
        of the tensor network based on the input model

        Parameters
        ----------
        tensor_network: tensor network class
            Tensor network on which links the efficient operator is defined
        """
        op_id = 0
        # Mapping from the euclidean indexes to the link index in the network
        # The :-2 is because for a network node the last link is the symmetry
        # selector, and the second last is the parent.
        physical_indexes = tensor_network[-1].op_neighbors[:-2, :].T.reshape(-1)
        # Cycle over the operator terms
        for term in self.model.hterms:
            # Cycle over each element of the terms
            for elem, coords in term.get_interactions(
                self.model.eval_lvals(self.params), self.params, dim=self.model.dim
            ):
                for idx, coord in enumerate(coords):
                    total_scaling = term.prefactor * term.eval_strength(self.params)
                    if "weight" in elem:
                        total_scaling *= elem["weight"]

                    self.eff_ops[physical_indexes[coord]] += [
                        IndexedOperator(
                            self.ops[elem["operators"][idx]],
                            op_id,
                            total_scaling,
                        )
                    ]
                op_id += 1


class IndexedTensorProductOperator(TensorProductOperator):
    """
    Indexed tensor product operators

    Parameters
    ----------
    params:
        The simulation parameters
    model: QuantumModel
        Quantum model defining the quantum operator
    operators: TNOperators
        Class containing the tensors of the operators
    tensor_network: tensor network class
        Tensor network on which links the efficient operator is defined
    device : str, optional
        Device of the computation. Default to "cpu".
    """

    def _extract_physical_terms(self, tensor_network):
        """
        Compute the physical hamiltonians on the physical indexes
        of the tensor network based on the input model

        Parameters
        ----------
        tensor_network: tensor network class
            Tensor network on which links the efficient operator is defined
        """
        op_id = 0
        # Mapping from the euclidean indexes to the link index in the network
        # The :-2 is because for a network node the last link is the symmetry
        # selector, and the second last is the parent.
        physical_indexes = tensor_network[-1].op_neighbors[:-2, :].T.reshape(-1)
        # Cycle over the operator terms
        for term in self.model.hterms:
            # Cycle over each element of the terms
            for elem, coords in term.get_interactions(
                self.numx, self.params, dim=self.model.dim
            ):
                for idx, coord in enumerate(coords):
                    self.eff_ops[physical_indexes[coord]] += [
                        IndexedOperator(
                            elem["operators"][idx],
                            op_id,
                            term.eval_strength(self.params) * term.prefactor,
                        )
                    ]
                op_id += 1
