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
The module contains a light-weight exact state emulator.
"""
import numpy as np
import numpy.linalg as nla
import scipy.sparse as sp
import scipy.sparse.linalg as spla

__all__ = ["StateVector"]


class StateVector:
    """
    State vector class for handling small systems without
    the truncation of entanglement.

    **Arguments**

    num_sites : int
        Number of sites in the system.

    local_dim : int, optional
        Local dimension of the sites
        Default to 2.

    state : ``None`` or np.ndarray, optional
        Pure state passed as numpy array. If ``None``, the |0...0>
        state is initialized; otherwise, the state vector is
        initialized with the numpy array.
        Default to ``None``.

    dtype : type, optional
        Initial data type if no numpy array is passed as initial state.
        The data type might change when executing operations.
        Default to ``np.complex128``
    """

    def __init__(self, num_sites, local_dim=2, state=None, dtype=np.complex128):
        self._num_sites = num_sites

        if hasattr(local_dim, "__len__"):
            if len(local_dim) != num_sites:
                raise Exception(
                    "Lenght of local dim %d does not" % (len(local_dim))
                    + " match number of sites %d." % (num_sites)
                )
            self._local_dim = local_dim
        else:
            self._local_dim = [local_dim] * self.num_sites

        # Dimension of the full Hilbert space
        self._global_dim = np.prod(self.local_dim)

        if state is None:
            psi = np.zeros(self.global_dim, dtype=dtype)
            psi[0] = 1.0
            self._state = np.reshape(psi, self.local_dim)
        else:
            if state.ndim == 1:
                if self.global_dim != np.prod(state.shape):
                    raise Exception(
                        "Dimension of state vector "
                        + "%d does" % (np.prod(state.shape))
                        + " not match dimension of Hilbert "
                        + "space %d." % (self.global_dim)
                    )
            elif state.ndim != self.num_sites:
                raise Exception(
                    "Number of sites in state vector does not "
                    + "match the number of sites defined in the "
                    + "input (%d vs %d)" % (state.ndim, self.num_sites)
                )
            elif list(state.shape) != list(self.local_dim):
                raise Exception("Local dimensions are not matching.")

            self._state = np.reshape(state, self.local_dim)

        #########################################################
        ## OBSERVABLES THE SIMULATOR IS ABLE TO MEASURE IN THE ##
        ## SAME ORDER OF THE ARRAY IN TNObservables            ##
        #########################################################
        self.is_measured = [
            True,  # TNObsLocal
            True,  # TNObsCorr
            True,  # TNDistance2Pure
            True,  # TnState2File
            False,  # TNObsTensorProduct
            False,  # TNObsWeightedSum
            False,  # TNPbsProjective
            False,  # TNObsProbabilities
            False,  # TNObsBondEntropy
            False,  # TNObsTZeroCorr
            False,  # TNObsCorr4
            False,  # TNObsCustom
        ]

    def __add__(self, other):
        """
        Add another state to the current state.

        **Arguments**

        other : :class:`StateVector`
            Second state in addition.

        **Returns**

        psi : :class:`StateVector`
             Result of addition.
        """
        if isinstance(other, np.ndarray):
            return StateVector(
                self.num_sites, local_dim=self.local_dim, state=self.state + other
            )

        if isinstance(other, StateVector):
            return StateVector(
                self.num_sites, local_dim=self.local_dim, state=self.state + other.state
            )

        raise Exception("Unknown type for other")

    def __truediv__(self, factor):
        """
        Division of state by a scalar.

        **Arguments**

        factor : real / complex
             Reciprocal scaling factor for the current state vector.

        **Returns**

        psi : :class:`StateVector`
            Result of the division.
        """
        if not np.isscalar(factor):
            raise TypeError("Division is only defined with a scalar number")

        return StateVector(
            self.num_sites, local_dim=self.local_dim, state=self._state / factor
        )

    def __getitem__(self, key):
        """
        Provide the call for list-syntax to access entries of the
        state vector.

        **Arguments**

        key : int
            index of the element which you want to retrieve
            labeled in the complete Hilbert space.

        **Returns**

        scalar : float / complex
            Entry of the state vector.
        """
        return self._state.flatten()[key]

    def __iadd__(self, other):
        """
        Add another state to the current state in-place.

        **Arguments**

        other : :class:`StateVector`, numpy ndarray
            Second state in addition.
        """
        if isinstance(other, np.ndarray):
            self._state += np.reshape(other, self.local_dim)

        elif isinstance(other, StateVector):
            self._state += other.state
        else:
            raise Exception("Unknown type for other")

        return self

    def __itruediv__(self, factor):
        """
        Divide the state through a scalar in-place.

        **Arguments**

        factor : real / complex
             Reciprocal scaling factor for the current state vector.
        """
        if not np.isscalar(factor):
            raise TypeError("Division is only defined with a scalar number")

        self._state /= factor

        return self

    def __imul__(self, factor):
        """
        Multiply the state by a scalar in-place.

        **Arguments**

        factor : real / complex
             Scaling factor for the current state vector.
        """
        if not np.isscalar(factor):
            raise TypeError("Multiplication is only defined with a scalar number")

        self._state *= factor

        return self

    def __isub__(self, other):
        """
        Subtract another state from the current state in-place.

        **Arguments**

        other : :class:`StateVector`, numpy ndarray
            Second state in subtraction.
        """
        if isinstance(other, np.ndarray):
            self._state -= np.reshape(other, self.local_dim)

        elif isinstance(other, StateVector):
            self._state -= other.state
        else:
            raise Exception("Unknown type for other")

        return self

    def __len__(self):
        """
        Provide number of sites in the state vector.
        """
        return self.num_sites

    def __matmul__(self, other):
        """
        Implements contractions between two objects with the @ operator.
        Enables calculation of the overlap <self | other>.

        **Arguments**

        other : instance of :class:`StateVector`
            Second object for contraction.

        **Returns**

        overlap : scalar
            Overlap between states if other is :class:`StateVector`
        """
        return other.dot(self)

    def __mul__(self, factor):
        """
        Multiply the state by a scalar.

        **Arguments**

        factor : real / complex
             Scaling factor for the current state vector.

        **Returns**

        psi : :class:`StateVector`
            Result of the multiplication.
        """
        if not np.isscalar(factor):
            raise TypeError("Multiplication is only defined with a scalar number")

        return StateVector(
            self.num_sites, local_dim=self.local_dim, state=self._state * factor
        )

    def __repr__(self):
        """
        Return the class name as representation.
        """
        return self.__class__.__name__

    def __sub__(self, other):
        """
        Subtract another state from the current state.

        **Arguments**

        other : :class:`StateVector`
            Second state in subtraction.

        **Returns**

        psi : :class:`StateVector`
             Result of subtract.
        """
        if isinstance(other, np.ndarray):
            return StateVector(
                self.num_sites, local_dim=self.local_dim, state=self.state - other
            )

        if isinstance(other, StateVector):
            return StateVector(
                self.num_sites, local_dim=self.local_dim, state=self.state - other.state
            )

        raise Exception("Unknown type for other")

    @property
    def num_sites(self):
        """
        Number of sites property.
        """
        return self._num_sites

    @property
    def local_dim(self):
        """
        Local dimension property. Returns the array of local dimensions.
        """
        return self._local_dim

    @property
    def global_dim(self):
        """
        Global dimension property. Returns scalar with the dimension of
        the full Hilbert space.
        """
        return self._global_dim

    @property
    def state(self):
        """
        State property.
        """
        return self._state

    def apply_global_operator(self, global_op):
        """
        Applies a global operator to the state; the state is updated
        in-place.

        **Arguments**

        global_op : numpy ndarray, rank-2
            Global operator acting on the whole Hilbert space.

        **Returns**

        Return ``None``; instance of class is updated in-place.
        """
        if global_op.ndim != 2:
            raise Exception("Global operator must be rank-2.")

        if any(global_op.shape != self.global_dim):
            raise Exception(
                "Global operator must match the " + "Hilbert space dimension."
            )

        state = np.reshape(self.state, [global_op.shape[0]])
        self._state = np.reshape(global_op.dot(state), self.local_dim)

    def dot(self, other):
        """
        Calculate the dot-product or overlap between two state vectors, i.e.,
        <other | self>.

        **Arguments**

        other : :class:`StateVector`, numpy ndarray
            Measure the overlap with this other state vector..

        **Returns**

        Scalar representing the overlap; complex valued.
        """
        if isinstance(other, np.ndarray):
            return np.conj(other.flatten()).dot(self._state.flatten())

        if isinstance(other, StateVector):
            return np.conj(other.state.flatten()).dot(self._state.flatten())

        raise Exception("Unknown type for other")

    def meas_global_operator(self, global_op):
        """
        Measure the expectation value of a global operator.

        **Arguments**

        global_op : numpy ndarray, rank-2
            Global operator acting on the whole Hilbert space.

        **Returns**

        Return scalar value with the expectation value.
        """
        state = np.reshape(self.state, [global_op.shape[0]])
        return np.real(np.conj(state).dot(global_op.dot(state)))

    def norm(self):
        """
        Calculate the norm of the state.

        **Returns**

        norm : float
            Real-valued scalar with the norm.
        """
        return np.real(np.sum(np.conj(self._state) * self._state))

    def normalize(self):
        """
        Normalize the current state in-place.

        **Returns**

        psi : :class:`StateVector`
            Normalized version, same object as input (no copy)
        """
        self /= np.sqrt(self.norm())
        return self

    def reduced_rho(self, idx_keep):
        """
        Calculate the reduced density matrix of a subset of sites.

        **Arguments**

        idx_keep : int or list of ints
            The site or sites specified here will be in the
            reduced density matrix.

        **Results**

        rho_ijk : numpy ndarray, rank-2
            Reduced density matrix for all the specified sites.
        """
        if np.isscalar(idx_keep):
            idx_keep = np.array([idx_keep])
        else:
            idx_keep = np.array(idx_keep)

        if len(idx_keep) != len(set(idx_keep)):
            raise Exception("Entries must be unique")

        if np.max(idx_keep) > self.num_sites - 1:
            raise Exception("Site index out-of-bound.")

        if np.min(idx_keep) < 0:
            raise Exception("Site index cannot be negative.")

        # Collect indices to be contracted
        contr_idx = []
        for ii in range(self.num_sites):
            if ii not in idx_keep:
                contr_idx.append(ii)

        # Reduced rho with indices of sites kept in ascending order
        rho_ijk = np.tensordot(
            self._state, np.conj(self._state), [contr_idx, contr_idx]
        )

        # Sort them in the order passed by the call
        nn = len(idx_keep)
        perm = np.zeros(2 * nn, dtype=int)
        perm[idx_keep.argsort()] = np.arange(nn)
        perm[nn:] = perm[:nn] + nn

        rho_ijk = np.transpose(rho_ijk, perm)

        return rho_ijk

    def reduced_rho_i(self, ii):
        """
        Calculate the reduced density matrix for a single site.

        **Arguments**

        ii : int
            Get reduced density matrix for this site.

        **Returns**

        rho_i : numpy ndarray, rank-2
             Reduced density matrix for site ii.
        """
        contr_ind = list(range(ii)) + list(range(ii + 1, self.num_sites))
        return np.tensordot(self._state, np.conj(self._state), [contr_ind, contr_ind])

    def reduced_rho_ij(self, ii, jj):
        """
        Calculate the reduced density matrix for a single site.

        **Arguments**

        ii : int
            Get reduced density matrix for this site and site jj.

        jj : int
            Get reduced density matrix for this site and site ii.

        **Returns**

        rho_ij : numpy ndarray, rank-2
             Reduced density matrix for site ii and jj.
        """
        if ii < jj:
            contr_ind = (
                list(range(ii))
                + list(range(ii + 1, jj))
                + list(range(jj + 1, self.num_sites))
            )
        elif jj < ii:
            contr_ind = (
                list(range(jj))
                + list(range(jj + 1, ii))
                + list(range(ii + 1, self.num_sites))
            )
        else:
            raise Exception("Sites ii and jj are equal.")

        rho_ij = np.tensordot(self._state, np.conj(self._state), [contr_ind, contr_ind])

        if jj < ii:
            rho_ij = np.transpose(rho_ij, [1, 0, 3, 2])

        dim = rho_ij.shape[0] * rho_ij.shape[1]

        return np.reshape(rho_ij, [dim, dim])

    @classmethod
    def from_groundstate(cls, ham, num_sites, local_dim):
        """
        Initialize the state vector with the ground state of a
        Hamiltonian passed as a matrix.

        **Arguments**

        ham : numpy ndarray, rank-2
            Matrix of the system. Lower triangular part is
            sufficient since ``numpy.linalg.eigh`` is used.

        num_sites : int
            Number of sites in the system.

        local_dim : int
            Local dimension of the sites
        """
        use_sparse = isinstance(ham, sp.csr_matrix)

        if not use_sparse:
            # Use dense matrix
            _, vecs = nla.eigh(ham)
        else:
            ham_sp = sp.csr_matrix(ham)
            _, vecs = spla.eigsh(ham_sp, k=1, which="SA")

        groundstate = vecs[:, 0]

        obj = cls(num_sites, local_dim=local_dim, state=groundstate)

        return obj
