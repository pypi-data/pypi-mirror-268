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
Sparse matrix product operators for simulations. This MPO covers a
full system with a list of `SparseMatrixOperator`.
"""

from .sparsematrixoperator import SparseMatrixOperator


class SparseMatrixProductOperator:
    """
    Indexed sparse MPO for a set of sites.

    **Arguments**

    params : dict
        Parameterization of a simulation.

    model : instance of `QuantumModel`
        The physical model to be converted into an MPO.

    operator_map : dict
        Mapping the operators to their integer IDs.

    param_map : dict
        Mapping the parameters to their integer IDs.
    """

    def __init__(self, params, model, operator_map, param_map):
        ll = model.get_number_of_sites(params)
        ll_xyz = model.get_number_of_sites_xyz(params)

        self.sp_mat_ops = []
        for ii in range(ll):
            self.sp_mat_ops.append(SparseMatrixOperator(ii == 0, ii + 1 == ll, True))

        for term in model.hterms:
            sp_mat_ops_new = term.get_sparse_matrix_operators(
                ll_xyz, params, operator_map, param_map, dim=model.dim
            )
            self.add_terms(sp_mat_ops_new)

    def add_terms(self, sp_mat_ops_list):
        """
        Add a list of `SparseMatrixOperators` to the existing
        one in-place.

        **Arguments**

        sp_mat_ops_list : list of `SparseMatrixOperators`
            Another interaction to be added to the MPO.
        """
        ll = len(self.sp_mat_ops)
        nn = len(sp_mat_ops_list)

        if ll != nn:
            raise Exception("Can only combine same lengths.")

        for ii in range(ll):
            self.sp_mat_ops[ii] += sp_mat_ops_list[ii]

    def write(self, fh):
        """
        Write out the sparse MPO compatible with reading it in fortran.

        **Arguments**

        fh : open filehandle
            Information about MPO will be written here.
        """
        nn = len(self.sp_mat_ops)
        fh.write("%d \n" % (nn))
        fh.write("-" * 32 + "\n")

        for ii in range(nn):
            self.sp_mat_ops[ii].write(fh)
            fh.write("-" * 32 + "\n")
