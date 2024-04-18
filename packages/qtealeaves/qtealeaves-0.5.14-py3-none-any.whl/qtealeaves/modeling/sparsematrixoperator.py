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
Sparse matrix operators for simulations. The operator covers a single site
of a larger system.
"""

import numpy as np


class SparseMatrixOperator:
    """
    A single indexed sparse MPO representing one site.

    **Arguments**

    is_first : bool
        Flag if sparse matrix operator represents first site.

    is_last : bool
        Flag if sparse matrix operator represents last site.

    do_vecs : bool
        For periodic boundary conditions aiming at actual matrices
        for all sites, set to `False`. For `True`, the first and
        last site will use vectors.
    """

    def __init__(self, is_first, is_last, do_vecs):
        if is_first and is_last:
            raise Exception("1-site system not covered.")

        if is_first and do_vecs:
            self._sp_mat = np.zeros((1, 2), dtype=int)
        elif is_last and do_vecs:
            self._sp_mat = np.zeros((2, 1), dtype=int)
        else:
            self._sp_mat = np.zeros((2, 2), dtype=int)

        self._weightid = np.zeros(self._sp_mat.shape, dtype=int)
        self._prefactor = np.zeros(self._sp_mat.shape, dtype=np.complex128)

        if is_first and do_vecs:
            self._sp_mat[-1, -1] = 1
            self._weightid[-1, -1] = -1
            self._prefactor[-1, -1] = 1.0
        elif is_last and do_vecs:
            self._sp_mat[0, 0] = 1
            self._weightid[0, 0] = -1
            self._prefactor[0, 0] = 1.0
        else:
            self._sp_mat[0, 0] = 1
            self._sp_mat[-1, -1] = 1
            self._weightid[0, 0] = -1
            self._weightid[-1, -1] = -1
            self._prefactor[0, 0] = 1.0
            self._prefactor[-1, -1] = 1.0

        self.local_terms = []
        self.local_prefactor = []
        self.local_param_id = []
        self.local_is_oqs = []

        self.tensors = None

    @property
    def shape(self):
        """Returns the dimension of the MPO matrix."""
        return self._sp_mat.shape

    def add_local(self, operator_id, param_id, prefactor, is_oqs):
        """
        Add a local term to the MPO.

        **Arguments**

        operator_id : int
            Operator index being used as local term.

        param_id : int
            Index being used as parameter in Hamiltonian.

        prefactor : scalar
            Scalar for the local term.

        is_oqs : bool
            Flag if term is Lindblad (`True`) or standard
            local term in the Hamiltonian (`False`).
        """
        self.local_terms.append(operator_id)
        self.local_param_id.append(param_id)
        self.local_prefactor.append(prefactor)
        self.local_is_oqs.append(is_oqs)

    def add_term(self, sp_mat, weightid, prefactor):
        """
        Add another sparse MPO to the existing one via terms.

        **Arguments**

        sp_mat : integer np.ndarray
            Index matrix of MPO to be added.

        weightid : integer np.ndarray
            Index of parameters of the MPO to be added.

        prefactor : np.ndarray
            Prefactors of the MPO to be added.
        """
        self._sp_mat = self._stack(self._sp_mat, sp_mat)
        self._weightid = self._stack(self._weightid, weightid)
        self._prefactor = self._stack(self._prefactor, prefactor)

    @staticmethod
    def _stack_matrices(mat1, mat2):
        """
        Stack to matrices for the MPO taking into account
        where local terms are etc.

        **Arguments**

        mat1 : np.ndarray
            Matrix for the first term.

        mat2 : np.ndarray
            Matrix for second term; cannot contain local terms.
        """
        n1, n2 = mat1.shape
        m1, m2 = mat2.shape

        if mat2[0, -1] != 0:
            raise Exception("No local can be in `mat2`.")

        l1 = n1 + m1 - 2
        l2 = n2 + m2 - 2

        mat_out = np.zeros((l1, l2), dtype=mat1.dtype)

        # Upper left rectangle, lowest row left part, lower right corner
        mat_out[: n1 - 1, : n2 - 1] = mat1[: n1 - 1, : n2 - 1]
        mat_out[-1, : n2 - 1] = mat1[-1, : n2 - 1]
        mat_out[-1, -1] = mat1[-1, -1]

        # Central matrix around diagonal, first column, last row
        mat_out[n1 - 1 : l1 - 1, n2 - 1 : l2 - 1] = mat2[1:-1, 1:-1]
        mat_out[n1 - 1 : l1 - 1, 0] = mat2[1:-1, 0]
        mat_out[-1, n2 - 1 : l2 - 1] = mat2[-1, 1:-1]

        return mat_out

    @staticmethod
    def _stack_rowvec(vec1, vec2):
        """
        Stack to row-vector for the MPO taking into account
        where local terms are etc.

        **Arguments**

        vec1 : np.ndarray
            Vector for the first term.

        vec2 : np.ndarray
            Vector for second term; cannot contain local terms.
        """
        n1, n2 = vec1.shape
        m1, m2 = vec2.shape

        if n1 != 1 or m1 != 1:
            raise Exception("Ain't no row vector.")

        l1 = 1
        l2 = n2 + m2 - 2

        vec_out = np.zeros((l1, l2), dtype=vec1.dtype)

        vec_out[0, : n1 - 1] = vec1[0, : n1 - 1]
        vec_out[0, -1] = vec1[0, -1]

        vec_out[0, n2 - 1 : l2 - 1] = vec2[0, 1 : m2 - 1]

        return vec_out

    @staticmethod
    def _stack_colvec(vec1, vec2):
        """
        Stack to column vector for the MPO taking into account
        where local terms are etc.

        **Arguments**

        vec1 : np.ndarray
            Vector for the first term.

        vec2 : np.ndarray
            Vector for second term; cannot contain local terms.
        """
        n1, n2 = vec1.shape
        m1, m2 = vec2.shape

        if n2 != 1 or m2 != 1:
            raise Exception("Ain't no col vector.")

        l1 = n1 + m1 - 2
        l2 = 1

        vec_out = np.zeros((l1, l2), dtype=vec1.dtype)

        vec_out[: n1 - 1, 0] = vec1[: n1 - 1, 0]
        vec_out[-1, 0] = vec1[-1, 0]

        vec_out[n1 - 1 : l1 - 1, 0] = vec2[1 : m1 - 1, 0]

        return vec_out

    @staticmethod
    def _stack(mat1, mat2):
        """
        Stack to matrix or vector for the MPO taking into account
        where local terms are etc. Matrix or vector is chosen
        based on dimension.

        **Arguments**

        mat1 : np.ndarray
            Matrix or vector for the first term.

        mat2 : np.ndarray
            Matrix or vector for second term; cannot contain local terms.
        """
        n1, n2 = mat1.shape
        m1, m2 = mat2.shape

        if n1 == 1 and m1 == 1:
            # Row vector
            return SparseMatrixOperator._stack_rowvec(mat1, mat2)

        if n2 == 1 and m2 == 1:
            # Column vector
            return SparseMatrixOperator._stack_colvec(mat1, mat2)

        return SparseMatrixOperator._stack_matrices(mat1, mat2)

    def __iadd__(self, spmat):
        """
        In-place addition of two sparse MPOs.

        **Arguments**

        spmat : instance of `SparseMatrixOperator`
            Sparse MPO to be added to the existing one.
        """
        if isinstance(spmat, SparseMatrixOperator):
            # Adding two spMPOs
            if (self.tensors is not None) or (spmat.tensors is not None):
                raise Exception("Cannot add sparse matrices after settings tensors.")

            self._sp_mat = self._stack(self._sp_mat, spmat._sp_mat)
            self._weightid = self._stack(self._weightid, spmat._weightid)
            self._prefactor = self._stack(self._prefactor, spmat._prefactor)

            self.local_terms += spmat.local_terms
            self.local_prefactor += spmat.local_prefactor
            self.local_param_id += spmat.local_param_id
            self.local_is_oqs += spmat.local_is_oqs
        else:
            raise Exception("Data type not implemented for `__iadd__`. Use add_term.")

        return self

    def get_list_tensors(self):
        """Generate a list of the unique indices used in the MPO."""
        list_tensors = list(self._sp_mat.flatten()) + self.local_terms
        list_tensors = list(set(list_tensors))

        if 0 in list_tensors:
            list_tensors.remove(0)

        return list_tensors

    def write(self, fh):
        """
        Write out the sparse MPO compatible with reading it in fortran.

        **Arguments**

        fh : open filehandle
            Information about MPO will be written here.
        """
        num_rows, num_cols = self.shape
        num_nonzero = np.sum(self._sp_mat > 0)

        list_tensors = self.get_list_tensors()
        num_tensors = len(list_tensors)

        fh.write("%d %d %d %d \n" % (num_rows, num_cols, num_nonzero, num_tensors))

        # contains parameterization (always for things written from python)
        fh.write("T \n")

        for ii in range(num_rows):
            for jj in range(num_cols):
                if self._sp_mat[ii, jj] == 0:
                    continue

                fh.write("%d %d %d \n" % (ii + 1, jj + 1, self._sp_mat[ii, jj]))

                # parameterization always as stated above
                fh.write("%d \n" % (self._weightid[ii, jj]))
                fh.write("%30.15E \n" % (self._prefactor[ii, jj]))

        for ii in range(num_tensors):
            fh.write("%d \n" % (list_tensors[ii]))

        fh.write("%d \n" % (len(self.local_terms)))
        for ii, elem in enumerate(self.local_terms):
            param_id = int(self.local_param_id[ii])
            prefactor = self.local_prefactor[ii]
            is_oqs = "T" if self.local_is_oqs[ii] else "F"
            fh.write("%d %d %30.15E %s \n" % (elem, param_id, prefactor, is_oqs))
