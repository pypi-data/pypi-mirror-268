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
The module contains a light-weight MPS emulator.
"""
from copy import deepcopy
from warnings import warn
from joblib import delayed, Parallel
import numpy as np
from numpy import double, linalg as nla
from qtealeaves.convergence_parameters import TNConvergenceParameters
from ..fortran_interfaces import write_tensor, read_tensor
from .abstract_tn import _AbstractTN, postprocess_statedict, _projector

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

__all__ = ["MPS"]


class MPS(_AbstractTN):
    """Matrix product states class

    Parameters
    ----------
    num_sites: int
        Number of sites
    convergence_parameters: :py:class:`TNConvergenceParameters`
        Class for handling convergence parameters. In particular, in the MPS simulator we are
        interested in:
        - the *maximum bond dimension* :math:`\\chi`;
        - the *cut ratio* :math:`\\epsilon` after which the singular
            values are neglected, i.e. if :math:`\\lamda_1` is the
            bigger singular values then after an SVD we neglect all the
            singular values such that :math:`\\frac{\\lambda_i}{\\lambda_1}\\leq\\epsilon`
    local_dim: int or list of ints, optional
        Local dimension of the degrees of freedom. Default to 2.
        If a list is given, then it must have length num_sites.
    dtype: type, optional
        Type of the entries of the tensors. Default to np.complex128.
    device: string, optional
        Device where to create the MPS. Default to 'cpu'.
        Implemented devices:
        - 'cpu'
        - 'gpu'

    """

    implemented_devices = ("cpu", "gpu")

    def __init__(
        self,
        num_sites,
        convergence_parameters,
        local_dim=2,
        dtype=np.complex128,
        device="cpu",
    ):
        _AbstractTN.__init__(
            self,
            num_sites,
            convergence_parameters,
            local_dim=local_dim,
            device=device,
            dtype=dtype,
        )

        if np.isscalar(local_dim):
            if local_dim < 2:
                raise ValueError(
                    "The local dimension must be at least 2 to show quantum behavior"
                )
            self._local_dim = np.repeat(local_dim, num_sites)
        elif len(local_dim) == self._num_sites:
            self._local_dim = np.array(local_dim)
        else:
            raise ValueError(
                "An array-like local dimension must have length equal to num_sites"
            )

        # Set orthogonality tracker for left/right-orthogonal form
        self._first_non_orthogonal_left = 0
        self._first_non_orthogonal_right = num_sites - 1

        # Initialize the tensors to the |000....0> state
        self._tensors = []
        for ii in range(num_sites):
            state0 = np.zeros((1, self._local_dim[ii], 1), dtype=dtype)
            state0[0, 0, 0] = 1
            self._tensors.append(state0)
        self._singvals = [np.ones(1, dtype=double) for _ in range(num_sites + 1)]

        # Save device
        self._device = "cpu"
        self.to_device(device)

        # Attribute used for computing probabilities. See
        # meas_probabilities for further details
        self._temp_for_prob = {}

        # Variable to save the maximum bond dimension reached at any moment
        self.max_bond_dim_reached = 1

    def __repr__(self):
        """
        Return the class name as representation.
        """
        return self.__class__.__name__

    def __len__(self):
        """
        Provide number of sites in the MPS
        """
        return self.num_sites

    def __getitem__(self, key):
        """Overwrite the call for lists, you can access tensors in the MPS using

        .. code-block::
            MPS[0]
            >>> [[ [1], [0] ] ]

        Parameters
        ----------
        key : int
            index of the MPS tensor you are interested in

        Returns
        -------
        np.ndarray
            Tensor at position key in the MPS.tensor array
        """
        return self.tensors[key]

    def __setitem__(self, key, value):
        """Modify a tensor in the MPS by using a syntax corresponding to lists.
        It is the only way to modify a tensor

        .. code-block::
            tens = np.ones( (1, 2, 1) )
            MPS[1] = tens


        Parameters
        ----------
        key : int
            index of the array
        value : np.array
            value of the new tensor. Must have the same shape as the old one
        """
        xp = self._device_checks()
        if not isinstance(value, xp.ndarray):
            raise TypeError("New tensor must be a numpy array")
        self._tensors[key] = value

        return None

    def __iter__(self):
        """Iterator protocol"""
        return iter(self.tensors)

    def __add__(self, other):
        """
        Add two MPS states in a "non-physical" way. Notice that this function
        is higly inefficient if the number of sites is very high.
        For example, adding |00> to |11> will result in |00>+|11> not normalized.
        Remember to take care of the normalization yourself.

        Parameters
        ----------
        other : MPS
            MPS to concatenate

        Returns
        -------
        MPS
            Summation of the first MPS with the second
        """
        if not isinstance(other, MPS):
            raise TypeError("Only two MPS classes can be summed")
        elif self.num_sites != other.num_sites:
            raise ValueError("Number of sites must be the same to concatenate MPS")
        elif np.any(self.local_dim != other.local_dim):
            raise ValueError("Local dimension must be the same to concatenate MPS")

        xp = self._device_checks()

        max_bond_dim = max(self.max_bond_dim, other.max_bond_dim)
        cut_ratio = min(self.cut_ratio, other.cut_ratio)
        convergence_params = TNConvergenceParameters(
            max_bond_dimension=int(max_bond_dim), cut_ratio=cut_ratio
        )

        tensor_list = []
        idx = 0
        for tens_a, tens_b in zip(self, other):
            shape_c = np.array(tens_a.shape) + np.array(tens_b.shape)
            shape_c[1] = tens_a.shape[1]
            if idx == 0 and [tens_a.shape[0], tens_b.shape[0]] == [1, 1]:
                shape_c[0] = 1
                tens_c = xp.zeros(shape_c, dtype=self.dtype)
                tens_c[:, :, : tens_a.shape[2]] = tens_a
                tens_c[:, :, tens_a.shape[2] :] = tens_b
            elif idx == self.num_sites - 1 and [tens_a.shape[2], tens_b.shape[2]] == [
                1,
                1,
            ]:
                shape_c[2] = 1
                tens_c = xp.zeros(shape_c, dtype=self.dtype)
                tens_c[: tens_a.shape[0], :, :] = tens_a
                tens_c[tens_a.shape[0] :, :, :] = tens_b
            else:
                tens_c = xp.zeros(shape_c, dtype=self.dtype)
                tens_c[: tens_a.shape[0], :, : tens_a.shape[2]] = tens_a
                tens_c[tens_a.shape[0] :, :, tens_a.shape[2] :] = tens_b

            tensor_list.append(tens_c)
            idx += 1

        addMPS = MPS.from_tensor_list(tensor_list, conv_params=convergence_params)

        return addMPS

    def __iadd__(self, other):
        """Concatenate the MPS other with self inplace"""
        addMPS = self.__add__(other)

        return addMPS

    def __mul__(self, factor):
        """Multiply the mps by a scalar and return the new MPS"""
        if not np.isscalar(factor):
            raise TypeError("Multiplication is only defined with a scalar number")

        other = deepcopy(self)
        if other.iso_center is None:
            other.right_canonize(
                max(0, self.first_non_orthogonal_left), keep_singvals=True
            )
        other._tensors[self.iso_center] *= factor

        return other

    def __imul__(self, factor):
        """Multiply the mps by a scalar in place"""
        if not np.isscalar(factor):
            raise TypeError("Multiplication is only defined with a scalar number")
        mult_mps = self.__mul__(factor)

        return mult_mps

    def __truediv__(self, factor):
        """Divide the mps by a scalar and return the new MPS"""
        if not np.isscalar(factor):
            raise TypeError("Multiplication is only defined with a scalar number")

        other = deepcopy(self)
        if other.iso_center is None:
            other.right_canonize(
                max(0, self.first_non_orthogonal_left), keep_singvals=True
            )
        other._tensors[self.iso_center] /= factor
        return other

    def __itruediv__(self, factor):
        """Divide the mps by a scalar in place"""
        if not np.isscalar(factor):
            raise TypeError("Multiplication is only defined with a scalar number")
        div_mps = self.__truediv__(factor)

        return div_mps

    def __matmul__(self, other):
        """
        Implement the contraction between two MPSs overloading the operator
        @. It is equivalent to doing <self|other>. It already takes into account
        the conjugation of the left-term
        """
        if not isinstance(other, MPS):
            raise TypeError("Only two MPS classes can be contracted")

        return other.contract(self)

    @property
    def tensors(self):
        """List of tensors componing the MPS"""
        return self._tensors

    @property
    def singvals(self):
        """List of singular values in the bonds"""
        return self._singvals

    @property
    def first_non_orthogonal_left(self):
        """First non orthogonal tensor starting from the left"""
        return self._first_non_orthogonal_left

    @property
    def first_non_orthogonal_right(self):
        """First non orthogonal tensor starting from the right"""
        return self._first_non_orthogonal_right

    @property
    def iso_center(self):
        """
        Output the gauge center if it is well defined, otherwise None
        """
        if self.first_non_orthogonal_left == self.first_non_orthogonal_right:
            center = self.first_non_orthogonal_right
        else:
            center = None
        return center

    def get_tensor_of_site(self, idx):
        """
        Generic function to retrieve the tensor for a specific site. Compatible
        across different tensor network geometries. This function does not
        shift the gauge center before returning the tensor.

        Parameters
        ----------
        idx : int
            Return tensor containin the link of the local
            Hilbert space of the idx-th site.
        """
        return self[idx]

    def get_rho_i(self, idx):
        """
        Get the reduced density matrix of the site at index idx

        Parameters
        ----------
        idx : int
            Index of the site

        Returns
        -------
        xp.ndarray
            Reduced density matrix of the site
        """
        xp = self._device_checks()

        s_idx = 1 if self.iso_center > idx else 0
        if self.singvals[idx + s_idx] is None:
            self.iso_towards(idx, keep_singvals=True)
            tensor = self[idx]
        else:
            tensor = self[idx]
            if self.iso_center > idx:
                tensor = xp.tensordot(
                    tensor, xp.diag(self.singvals[idx + s_idx]), ([2], [1])
                )
            elif self.iso_center < idx:
                tensor = xp.tensordot(
                    xp.diag(self.singvals[idx + s_idx]), tensor, ([1], [0])
                )

        rho = xp.tensordot(tensor, np.conj(tensor), [[0, 2], [0, 2]])

        return rho

    def _get_eff_op_on_pos(self, pos):
        """
        Obtain the list of effective operators adjacent
        to the position pos and the index where they should
        be contracted

        Parameters
        ----------
        pos : int
            Index of the tensor w.r.t. which we have to retrieve
            the effective operators

        Returns
        -------
        list of IndexedOperators
            List of effective operators
        list of ints
            Indexes where the operators should be contracted
        """
        raise NotImplementedError("This function has to be overwritten")

    def site_canonize(self, idx, keep_singvals=False):
        """
        Apply the gauge transformation to shift the isoemtry
        center to a specific site `idx`.

        Parameters
        ----------
        idx: int
            index of the tensor up to which the canonization
            occurs from the left and right side.
        keep_singvals : bool, optional
            If True, keep the singular values even if shifting the iso with a
            QR decomposition. Default to False.
        """
        self.iso_towards(idx, keep_singvals=keep_singvals)

    def iso_towards(self, new_iso, keep_singvals=False, trunc=False, conv_params=None):
        """
        Apply yhe gauge transformation to shift the isometry
        center to a specific site `new_iso`.
        The method might be different for
        other TN structure, but for the MPS it is the same.

        Parameters
        ----------
        new_iso : int
            Position in the TN of the tensor which should be isometrized.
        keep_singvals : bool, optional
            If True, keep the singular values even if shifting the iso with a
            QR decomposition. Default to False.
        trunc : Boolean, optional
            If `True`, the shifting is done via truncated SVD.
            If `False`, the shifting is done via QR.
            Default to `False`.
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters to use for the SVD. If `None`, convergence
            parameters are taken from the TTN.
            Default to `None`.
        """
        if conv_params is not None:
            raise ValueError("conv_params not yet supported for MPS.")

        self.left_canonize(new_iso, svd=trunc, keep_singvals=keep_singvals)
        self.right_canonize(new_iso, svd=trunc, keep_singvals=keep_singvals)

    def right_canonize(self, idx, svd=False, keep_singvals=False):
        """
        Apply a gauge transformation to all bonds between
        :py:method:`MPS.num_sites` and `idx`, so that all
        sites between the last (rightmost one) and idx
        are set to (semi)-unitary tensors.

        Parameters
        ----------
        idx: int
            index of the tensor up to which the canonization occurs
        svd: bool, optional
            If True, use the SVD instead of the QR for the canonization.
            It might be useful to reduce the bond dimension. Default to False.
        keep_singvals : bool, optional
            If True, keep the singular values even if shifting the iso with a
            QR decomposition. Default to False.
        """
        if idx > self.num_sites - 1 or idx < 0:
            raise ValueError(
                "The canonization index must be between the "
                + "number of sites-1 and 0"
            )

        xp = self._device_checks()
        for ii in range(self.first_non_orthogonal_right, idx, -1):
            tensor = self[ii]
            tensor_shape = tensor.shape
            matrix = tensor.reshape(tensor_shape[0], np.prod(tensor_shape[1:])).T
            # We want (left) - (right) => (left) - R - Q =
            # So we need R before Q. That is why we transpose:
            # (right).T = Q R => (right) = R.T Q.T (and rename R.T => R and Q.T => Q)
            if svd:
                RR, tensor, singvals, _ = self.tSVD(
                    tensor, [0], [1, 2], contract_singvals="L"
                )
                self._singvals[ii] = singvals
            else:
                QQ, RR = xp.linalg.qr(matrix)
                RR = RR.T
                QQ = QQ.T

                # Reshape back
                tensor = QQ.reshape(-1, *tensor_shape[1:])
                if not keep_singvals:
                    self._singvals[ii] = None

            # Update the tensors in the MPS
            self._tensors[ii] = tensor
            self._tensors[ii - 1] = xp.tensordot(self[ii - 1], RR, ([2], [0]))

        self._first_non_orthogonal_left = min(self.first_non_orthogonal_left, idx)
        self._first_non_orthogonal_right = idx

    def left_canonize(self, idx, svd=False, keep_singvals=False):
        """
        Apply a gauge transformation to all bonds between 0 and `idx`,
        so that all sites between the first (òeftmpst one) and idx
        are set to (semi)-unitary tensors.

        Parameters
        ----------
        idx: int
            index of the tensor up to which the canonization occurs
        svd: bool, optional
            If True, use the SVD instead of the QR for the canonization.
            It might be useful to reduce the bond dimension. Default to False.
        keep_singvals : bool, optional
            If True, keep the singular values even if shifting the iso with a
            QR decomposition. Default to False.
        """
        if idx > self.num_sites - 1 or idx < 0:
            raise ValueError(
                "The canonization index must be between the "
                + "number of sites-1 and 0"
            )

        xp = self._device_checks()
        for ii in range(self.first_non_orthogonal_left, idx):
            tensor = self[ii]
            tensor_shape = tensor.shape
            matrix = tensor.reshape(np.prod(tensor_shape[:2]), tensor_shape[2])

            if svd:
                tensor, RR, singvals, _ = self.tSVD(
                    tensor, [0, 1], [2], contract_singvals="R"
                )
                self._singvals[ii + 1] = singvals
            else:
                QQ, RR = xp.linalg.qr(matrix)

                # Reshape back
                tensor = QQ.reshape(*tensor_shape[:2], -1)
                if not keep_singvals:
                    self._singvals[ii + 1] = None

            # Update the tensors in the MPS
            self._tensors[ii] = tensor
            self._tensors[ii + 1] = xp.tensordot(self[ii + 1], RR, ([0], [1]))
            self._tensors[ii + 1] = xp.transpose(self._tensors[ii + 1], [2, 0, 1])

        self._first_non_orthogonal_left = idx
        self._first_non_orthogonal_right = max(self.first_non_orthogonal_right, idx)

    def normalize(self):
        """
        Normalize the MPS state, by dividing by :math:`\\sqrt{<\\psi|\\psi>}`.
        """
        # Compute the norm. Internally, it set the gauge center
        norm = self.norm()
        # Update the norm
        self._tensors[self.iso_center] /= norm

    def scale(self, factor):
        """
        Scale the MPS state by a scalar constant using the gauge center.

        Parameters
        ----------

        factor : scalar
             Factor is multiplied to the MPS at the gauge center.
        """
        self._tensors[self.iso_center] *= factor

    def modify_local_dim(self, value, idxs=None):
        """
        Modify the local dimension of sites `idxs` to the value `value`.
        By default modify the local dimension of all the sites. If `value` is
        a vector then it must have the same length of `idxs`.
        Notice that there may be loss of information, it is up to the
        user to be sure no error is done in this procedure.

        Parameters
        ----------
        value : int or array-like
            New value of the local dimension. If an int, it is assumed
            it will be the same for all sites idxs, otherwise its length
            must be the same of idxs.
        idxs : int or array-like, optional
            Indexes of the sites to modify. If None, all the sites are
            modified. Default to None.
        """
        # Transform scalar arguments in vectors
        if np.isscalar(value) and idxs is None:
            value = np.repeat(value, self.num_sites).astype(int)
        if idxs is None:
            idxs = np.arange(self.num_sites)
        elif np.isscalar(idxs) and np.isscalar(value):
            idxs = np.array([idxs])
            value = np.array([value])
        # Checks on parameters
        if np.any(idxs > self.num_sites - 1) or np.any(idxs < 0):
            raise ValueError(
                "The index idx must be between the " + "number of sites-1 and 0"
            )
        elif np.min(value) < 2:
            raise ValueError(
                f"The local dimension must be at least 2, not {min(value)}"
            )
        elif len(value) != len(idxs):
            raise ValueError(
                "value and idxs must have the same length, but "
                + f"{len(value)} != {len(idxs)}"
            )

        xp = self._device_checks()

        # Quick return
        if len(idxs) == 0:
            return
        # Sort arguments to avoid moving the gauge back and forth
        value = value[np.argsort(idxs)]
        idxs = np.sort(idxs)

        for ii, idx in enumerate(idxs):
            initial_local_dim = self.local_dim[idx]
            new_local_dim = value[ii]
            self.site_canonize(idx, keep_singvals=True)

            modify_tens = xp.eye(new_local_dim, initial_local_dim)
            initial_norm = self.norm()

            # Modify the local dimension
            res = xp.tensordot(self[idx], modify_tens, ([1], [1]))
            self._tensors[idx] = res.transpose(0, 2, 1)

            final_norm = self.norm()
            self._tensors[self.iso_center] *= initial_norm / final_norm

            self._local_dim[idx] = new_local_dim

    def add_site(self, idx, state=None):
        """
        Add a site in a product state in the link idx
        (idx=0 is before the first site, idx=N+1 is after the last).
        The state of the new index is |0> or the one provided.

        Parameters
        ----------
        idx : int
            index of the link where you want to add the site
        state: None or array-like
            Vector state that you want to add

        Details
        -------
        To insert a new site in the MPS we first insert an identity on a link,
        then add a dimension-1 link to the identity and lastly contract the
        new link with the initial state, usually a |0>
        """
        xp = self._device_checks()
        if idx < 0 or idx > self.num_sites:
            raise ValueError(f"idx must be between 0 and N+1, not {idx}")
        if state is None:
            state = xp.zeros(int(np.min(self.local_dim)), dtype=self.dtype)
            state[0] = 1
        old_norm = self.norm()

        # Insert an identity on link idx
        if idx == 0:
            id_dim = self[0].shape[0]
        else:
            id_dim = self[idx - 1].shape[2]
        identity = xp.eye(id_dim, dtype=self.dtype).reshape(id_dim, 1, id_dim)

        # Contract the identity with the desired state of the new tensor
        state = state.reshape(len(state), 1)
        new_site = xp.tensordot(identity, state, ([1], [1]))
        new_site = new_site.transpose([0, 2, 1])

        # Insert it in the data structure
        self._tensors.insert(idx, new_site)
        self._local_dim = np.insert(self._local_dim, idx, new_site.shape[1])
        self._num_sites += 1
        self._singvals.insert(idx + 1, None)

        # Update the gauge center if we didn't add the site at the end of the chain
        if idx < self.num_sites - 1 and idx < self.iso_center:
            self._first_non_orthogonal_right += 1
            self._first_non_orthogonal_left += 1

        # Renormalize
        new_norm = self.norm()

        self._tensors[self.iso_center] *= old_norm / new_norm

    def to_device(self, device):
        """
        Move the MPS class to the new device.

        Parameters
        ----------
        device : string
            Device where to move the MPS
        """
        if device not in self.implemented_devices:
            raise ValueError(
                f"Device {device} is not implemented. Select from"
                + f" {self.implemented_devices}"
            )
        # We already are in the correct device
        elif device == self.device:
            return
        # We go to the cpu to gpu
        elif device == "gpu":
            if not GPU_AVAILABLE:
                raise ImportError("CUDA GPU is not available")
            self._tensors = [cp.asarray(tens) for tens in self._tensors]
            self._singvals = [
                cp.asarray(singv) if singv is not None else None
                for singv in self._singvals
            ]
        # We go from gpu to cpu
        elif device == "cpu":
            self._tensors = [cp.asnumpy(tens) for tens in self._tensors]
            self._singvals = [
                cp.asnumpy(singv) if singv is not None else None
                for singv in self._singvals
            ]
        self._device = device

        return

    def to_statevector(self, qiskit_order=False, max_qubit_equivalent=20):
        """
        Given a list of N tensors *MPS* [U1, U2, ..., UN] , representing
        a Matrix Product State, perform the contraction in the Examples,
        leading to a single tensor of order N, representing a dense state.

        The index ordering convention is from left-to-right.
        For instance, the "left" index of U2 is the first, the "bottom" one
        is the second, and the "right" one is the third.

        Parameters
        ----------
        qiskit_order: bool, optional
            weather to use qiskit ordering or the theoretical one. For
            example the state |011> has 0 in the first position for the
            theoretical ordering, while for qiskit ordering it is on the
            last position.
        max_qubit_equivalent: int, optional
            Maximum number of qubit sites the MPS can have and still be
            transformed into a statevector.
            If the number of sites is greater, it will throw an exception.
            Default to 20.

        Returns
        -------
        psi : ndarray of shape (d ^ N, )
            N-order tensor representing the dense state.

        Examples
        --------
        >>> U1 - U2 - ... - UN
        >>>  |    |          |
        """
        xp = self._device_checks()
        if np.prod(self.local_dim) > 2**max_qubit_equivalent:
            raise RuntimeError(
                "Maximum number of sites for the statevector is "
                + f"fixed to the equivalent of {max_qubit_equivalent} qubit sites"
            )
        psi = self[0]
        for tensor in self[1:]:
            psi = xp.tensordot(psi, tensor, axes=(-1, 0))

        if qiskit_order:
            order = "F"
        else:
            order = "C"

        return psi.reshape(np.prod(self.local_dim), order=order)

    def to_tensor_list(self):
        """
        Return the tensor list representation of the MPS.
        Required for compatibility with TTN emulator

        Return
        ------
        list
            List of tensors of the MPS
        """
        return self.tensors

    def to_ttn(self):
        """
        Return a tree tensor network (TTN) representation as binary tree.

        Details
        -------

        The TTN is returned as a listed list where the tree layer with the
        local Hilbert space is the first list entry and the uppermost layer in the TTN
        is the last list entry. The first list will have num_sites / 2 entries. The
        uppermost list has two entries.

        The order of the legs is always left-child, right-child, parent with
        the exception of the left top tensor. The left top tensor has an
        additional link, i.e., the symmetry selector; the order is left-child,
        right-child, parent, symmetry-selector.

        Also see :py:func:ttn_simulator:`from_tensor_list`.
        """
        self.to_device("cpu")
        nn = len(self)
        if abs(np.log2(nn) - int(np.log2(nn))) > 1e-15:
            raise Exception(
                "A conversion to a binary tree requires 2**n "
                "sites; but having %d sites." % (nn)
            )

        if nn == 4:
            # Special case: iterations will not work
            left_tensor = np.tensordot(self[0], self[1], [[2], [0]])
            right_tensor = np.tensordot(self[2], self[3], [[2], [0]])

            # Use left link of dimension 1 as symmetry selector
            left_tensor = np.transpose(left_tensor, [1, 2, 3, 0])

            # Eliminate one link
            right_tensor = np.reshape(right_tensor, right_tensor.shape[:-1])

            return [[left_tensor, right_tensor]]

        # Initial iteration
        theta_list = []
        for ii in range(nn // 2):
            ii1 = 2 * ii
            ii2 = ii1 + 1

            theta_list.append(np.tensordot(self[ii1], self[ii2], [[2], [0]]))

        child_list = []
        parent_list = []
        for ii, theta in enumerate(theta_list):
            dims = theta.shape
            tmp = np.transpose(theta, [1, 2, 0, 3])
            tmp = np.reshape(tmp, [np.prod(tmp.shape[:2]), np.prod(tmp.shape[2:])])
            qmat, rmat = nla.qr(tmp)
            qmat = np.reshape(qmat, [dims[1], dims[2], rmat.shape[0]])
            rmat = np.reshape(rmat, [qmat.shape[2], dims[0], dims[3]])
            rmat = np.transpose(rmat, [1, 0, 2])

            child_list.append(qmat)
            parent_list.append(rmat)

        layer_list = [child_list]
        while len(parent_list) > 4:
            theta_list = []
            for ii in range(len(parent_list) // 2):
                ii1 = 2 * ii
                ii2 = ii1 + 1

                theta_list.append(
                    np.tensordot(parent_list[ii1], parent_list[ii2], [[2], [0]])
                )

            child_list = []
            parent_list = []
            for ii, theta in enumerate(theta_list):
                dims = theta.shape
                tmp = np.transpose(theta, [1, 2, 0, 3])
                tmp = np.reshape(tmp, [np.prod(tmp.shape[:2]), np.prod(tmp.shape[2:])])
                qmat, rmat = nla.qr(tmp)
                qmat = np.reshape(qmat, [dims[1], dims[2], rmat.shape[0]])
                rmat = np.reshape(rmat, [qmat.shape[2], dims[0], dims[3]])
                rmat = np.transpose(rmat, [1, 0, 2])

                child_list.append(qmat)
                parent_list.append(rmat)

            layer_list.append(child_list)

        # Last iteration
        left_tensor = np.tensordot(parent_list[0], parent_list[1], [[2], [0]])
        right_tensor = np.tensordot(parent_list[2], parent_list[3], [[2], [0]])

        # The fourth-link is the symmetry selector, i.e., for tensor
        # networks without symmetries a link of dimension one. The link
        # to the left of the MPS fulfills this purpose
        left_tensor = np.transpose(left_tensor, [1, 2, 3, 0])

        right_tensor = np.reshape(right_tensor, right_tensor.shape[:-1])
        right_tensor = np.transpose(right_tensor, [1, 2, 0])

        layer_list.append([left_tensor, right_tensor])

        return layer_list

    @classmethod
    def from_tensor_list(
        cls, tensor_list, conv_params=None, device="cpu", dtype=np.complex128
    ):
        """
        Initialize the MPS tensors using a list of correctly shaped tensors

        Parameters
        ----------
        tensor_list : list of ndarrays or cupy arrays
            List of tensor for initializing the MPS
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters for the new MPS. If None, the maximum bond
            bond dimension possible is assumed, and a cut_ratio=1e-9.
            Default to None.
        device : str
            Computational device. Available 'cpu', 'gpu'. Default to 'cpu'
        dtype : data type preferably numpy
            Data type for constructing MPS.

        Returns
        -------
        obj : :py:class:`MPS`
            The MPS class
        """
        local_dim = []
        max_bond_dim = 2
        for ii, tens in enumerate(tensor_list):
            t_shape = tens.shape
            local_dim.append(t_shape[1])
            max_bond_dim = max(max_bond_dim, t_shape[0])
            if ii > 0 and t_shape[0] != tensor_list[ii - 1].shape[2]:
                raise ValueError(
                    f"The dimension of the left leg of tensor {ii} and "
                    + f"the right leg of tensor {ii-1} must be equal"
                )

        if conv_params is None:
            conv_params = TNConvergenceParameters(max_bond_dimension=int(max_bond_dim))
        obj = cls(len(tensor_list), conv_params, local_dim, dtype=dtype, device=device)
        obj._tensors = tensor_list
        obj.to_device(device)

        return obj

    @classmethod
    def from_statevector(
        cls,
        statevector,
        local_dim=2,
        conv_params=None,
        device="cpu",
        dtype=np.complex128,
    ):
        """
        Initialize the MPS tensors by decomposing a statevector into MPS form.
        All the degrees of freedom must have the same local dimension

        Parameters
        ----------
        statevector : ndarray of shape( local_dim^num_sites, )
            Statevector describing the interested state for initializing the MPS
        local_dim : int, optional
            Local dimension of the degrees of freedom. Default to 2.
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters for the new MPS. If None, the maximum bond
            bond dimension possible is assumed, and a cut_ratio=1e-9.
            Default to None.
        device : str
            Computational device. Available 'cpu', 'gpu'. Default to 'cpu'
        dtype : data type preferably numpy
            Data type for constructing MPS.

        Returns
        -------
        obj : :py:class:`MPS`
            MPS simulator class

        Examples
        --------
        >>> -U1 - U2 - U3 - ... - UN-
        >>>  |    |    |          |
        # For d=2, N=7 and chi=5, the tensor network is as follows:
        >>> -U1 -2- U2 -4- U3 -5- U4 -5- U5 -4- U6 -2- U7-
        >>>  |      |      |      |      |      |      |
        # where -x- denotes the bounds' dimension (all the "bottom-facing" indices
        # are of dimension d=2). Thus, the shapes
        # of the returned tensors are as follows:
        >>>      U1         U2         U3         U4         U5         U6         U7
        >>> [(1, 2, 2), (2, 2, 4), (4, 2, 5), (5, 2, 5), (5, 2, 4), (4, 2, 2), (2, 2, 1)]
        """
        if not isinstance(statevector, np.ndarray):
            raise TypeError("Statevector must be numpy array")
        num_sites = int(np.log(len(statevector)) / np.log(local_dim))

        max_bond_dim = local_dim ** (num_sites // 2)
        if conv_params is None:
            conv_params = TNConvergenceParameters(max_bond_dimension=int(max_bond_dim))
        obj = cls(num_sites, conv_params, local_dim, dtype=dtype)

        state_tensor = statevector.reshape([1] + [local_dim] * num_sites + [1])
        for ii in range(num_sites - 1):
            legs = list(range(len(state_tensor.shape)))
            tens_left, tens_right, singvals, _ = obj.tSVD(
                state_tensor, legs[:2], legs[2:], contract_singvals="R"
            )

            obj._tensors[ii] = tens_left
            obj._singvals[ii + 1] = singvals
            state_tensor = tens_right
        obj._tensors[-1] = tens_right

        # After this procedure the state is in left canonical form
        obj._first_non_orthogonal_left = obj.num_sites - 1
        obj._first_non_orthogonal_right = obj.num_sites - 1
        obj.to_device(device)

        return obj

    def apply_one_site_operator(self, op, pos):
        """
        Applies a one operator `op` to the site `pos` of the MPS.

        Parameters
        ----------
        op: numpy array shape (local_dim, local_dim)
            Matrix representation of the quantum gate
        pos: int
            Position of the qubit where to apply `op`.

        """
        if pos < 0 or pos > self.num_sites - 1:
            raise ValueError(
                "The position of the site must be between 0 and (num_sites-1)"
            )
        # elif not isinstance(op, np.ndarray):
        #    raise TypeError('Input operator must be a ndarray')
        elif list(op.shape) != [self._local_dim[pos]] * 2:
            raise ValueError(
                "Shape of the input operator must be (local_dim, local_dim)"
            )

        xp = self._device_checks(operator=op)
        res = xp.tensordot(self[pos], op, (1, 1))
        self._tensors[pos] = res.transpose(0, 2, 1)

    def apply_two_site_operator(self, op, pos, swap=False, svd=True, parallel=False):
        """
        Applies a two-site operator `op` to the site `pos`, `pos+1` of the MPS.

        Parameters
        ----------
        op: numpy array shape (local_dim, local_dim, local_dim, local_dim)
            Matrix representation of the quantum gate
        pos: int or list of ints
            Position of the qubit where to apply `op`. If a list is passed,
            the two sites should be adjacent. The first index is assumed to
            be the control, and the second the target. The swap argument is
            overwritten if a list is passed.
        swap: bool
            If True swaps the operator. This means that instead of the
            first contraction in the following we get the second.
            It is written is a list of pos is passed.
        svd: bool
            If True, apply the usual contraction plus an SVD, otherwise use the
            QR approach explained in https://arxiv.org/pdf/2212.09782.pdf.
        parallel: bool
            If True, perform an approximation of the two-qubit gates faking
            the isometry center

        Returns
        -------
        singular_values_cutted: ndarray
            Array of singular values cutted, normalized to the biggest singular value

        Examples
        --------

        .. code-block::

            swap=False  swap=True
              -P-M-       -P-M-
              2| |2       2| |2
              3| |4       4| |3
               GGG         GGG
              1| |2       2| |1
        """
        if not np.isscalar(pos) and len(pos) == 2:
            pos = min(pos[0], pos[1])
        elif not np.isscalar(pos):
            raise ValueError(
                f"pos should be only scalar or len 2 array-like, not len {len(pos)}"
            )

        if pos < 0 or pos > self.num_sites - 1:
            raise ValueError(
                "The position of the site must be between 0 and (num_sites-1)"
            )
        elif list(op.shape) != [self._local_dim[pos], self._local_dim[pos + 1]] * 2:
            raise ValueError(
                "Shape of the input operator must be (local_dim, "
                + "local_dim, local_dim, local_dim)"
            )

        xp = self._device_checks(operator=op)
        if swap:
            op = xp.transpose(op, [1, 0, 3, 2])

        if parallel:
            self[pos] = self.tensordot_diagonal(self[pos], self.singvals[pos], 0)
        else:
            # Set orthogonality center
            self.site_canonize(pos, keep_singvals=True)

        # Perform SVD
        if svd:
            # Contract the two qubits
            twoqubit = xp.tensordot(self[pos], self[pos + 1], (2, 0))

            # Contract with the gate
            twoqubit = xp.tensordot(twoqubit, op, ([1, 2], [2, 3]))
            twoqubit = xp.transpose(twoqubit, [0, 2, 3, 1])
            tens_left, tens_right, singvals, singvals_cutted = self.tSVD(
                twoqubit, [0, 1], [2, 3], contract_singvals="R"
            )
        else:
            tens_left, tens_right, singvals, singvals_cutted = self.tEQR(
                self[pos], self[pos + 1], self.singvals[pos], op
            )

        # Update state
        self._tensors[pos] = tens_left
        self._tensors[pos + 1] = tens_right
        self._singvals[pos + 1] = singvals

        if parallel:
            self[pos] = self.tensordot_diagonal(self[pos], 1 / self.singvals[pos], 0)

        else:
            self._first_non_orthogonal_left = pos + 1
            self._first_non_orthogonal_right = pos + 1

        # Update maximum bond dimension reached
        if self[pos].shape[2] > self.max_bond_dim_reached:
            self.max_bond_dim_reached = self[pos].shape[2]

        return singvals_cutted

    def apply_projective_operator(self, site, selected_output=None, remove=False):
        """
        Apply a projective operator to the site **site**, and give the measurement as output.
        You can also decide to select a given output for the measurement, if the probability is
        non-zero. Finally, you have the possibility of removing the site after the measurement.

        .. warning::

            Applying projective measurements/removing sites is ALWAYS dangerous. The information
            of the projective measurement should be in principle carried over the entire mps,
            by iteratively applying SVDs across all sites. However, this procedure is highly
            suboptimal, since it is not always necessary and will be processed by the
            following two-sites operators. Thus, the procedure IS NOT applied here. Take care
            that entanglement measures through :class:`TNObsBondEntropy` may give incorrect
            results right after a projective operator application. Furthermore, if working
            with parallel approaches, projective operators should be treated with even more
            caution, since they CANNOT be applied in parallel.

        Parameters
        ----------
        site: int
            Index of the site you want to measure
        selected_output: int, optional
            If provided, the selected state is measured. Throw an error if the probability of the
            state is 0
        remove: bool, optional
            If True, the measured index is traced away after the measurement. Default to False.

        Returns
        -------
        meas_state: int
            Measured state
        state_prob : float
            Probability of measuring the output state
        """
        if selected_output is not None and selected_output > self._local_dim[site] - 1:
            raise ValueError("The seleted output must be at most local_dim-1")
        xp = self._device_checks()

        # Set the orthogonality center
        self.site_canonize(site, keep_singvals=True)

        # Normalize
        old_norm = self.norm()
        self._tensors[site] = self._tensors[site] / old_norm

        # Measure
        cum_prob = 0
        random_u = np.random.rand()
        rho_i = self.get_rho_i(site)
        for ii in range(self._local_dim[site]):
            if selected_output is not None and ii != selected_output:
                continue

            projector = _projector(ii, self._local_dim[site], xp)
            prob_ii = xp.trace(rho_i @ projector)
            cum_prob += prob_ii
            if cum_prob >= random_u or selected_output == ii:
                meas_state = ii
                state_prob = prob_ii
                break

        # Renormalize and come back to previous norm
        if remove:
            projector_vect = xp.zeros(int(self._local_dim[site]))
            projector_vect[meas_state] = 1
            # Project the state in the measured one
            tens_to_remove = xp.tensordot(
                self._tensors[site], projector_vect, ([1], [0])
            )

            if site < self.num_sites - 1:
                # contract the measured tensor in the next tensor
                self._tensors[site + 1] = xp.tensordot(
                    tens_to_remove, self[site + 1], ([1], [0])
                )
            else:
                self._tensors[site - 1] = xp.tensordot(
                    self[site - 1], tens_to_remove, ([2], [0])
                )

            self._tensors.pop(site)
            self._singvals.pop(site)
            self._local_dim = np.delete(self._local_dim, site)
            self._num_sites -= 1
            site = min(site, self._num_sites - 1)
            self._first_non_orthogonal_left = site
            self._first_non_orthogonal_right = site
        else:
            self.apply_one_site_operator(projector, site)

        # Renormalize
        self._tensors[site] = self._tensors[site] / self.norm()
        self._tensors[site] = self._tensors[site] * old_norm

        # Set to None all the singvals
        self._singvals = [None for _ in self.singvals]

        return meas_state, state_prob

    def apply_nonlocal_two_site_operator(self, op, control, target, swap=False):
        """Apply a non-local two-site operator, by taking first the SVD of the operator,
        contracting the almost-single-site operator to the respective sites and then
        propagating the operator to the correct site

        .. warning::
            The operations in this method are NOT ALWAYS well defined. If the left-operator
            tensor is not unitary, then we are applying a non-unitary operation to the
            state, and thus we will see a vanishing norm. Notice that, if the error can
            happen a warning message will be printed

        Parameters
        ----------
        op : np.ndarray
            Operator to be applied
        control : int
            control qubit index
        target : int
            target qubit index
        swap : bool, optional
            If True, transpose the tensor legs such that the control and target
            are swapped. Default to False

        Returns
        -------
        np.ndarray
            Singular values cutted when the gate link is contracted
        """

        if min(control, target) < 0 or max(control, target) > self.num_sites - 1:
            raise ValueError(
                "The position of the site must be between 0 and (num_sites-1)"
            )
        elif list(op.shape) != [self._local_dim[control], self._local_dim[target]] * 2:
            raise ValueError(
                "Shape of the input operator must be (local_dim, "
                + "local_dim, local_dim, local_dim)"
            )
        if swap:
            op = op.transpose(1, 0, 3, 2)

        xp = self._device_checks()

        min_site = min(control, target)
        max_site = max(control, target)
        left_gate, right_gate, _, _ = self.tSVD(
            op,
            [0, 2],
            [1, 3],
            perm_left=[0, 2, 1],
            perm_right=[1, 0, 2],
            contract_singvals="R",
        )

        test = xp.tensordot(left_gate, left_gate.conj(), ([0, 1], [0, 1]))
        if not xp.isclose(xp.identity(test.shape[0]), test):
            warn(
                "Left-tensor is not unitary. Thus, the contraction is not optimal. We"
                " suggest"
                + " to linearize the circuit instead of using non-local operators",
                RuntimeWarning(),
            )

        self.site_canonize(min_site, keep_singvals=True)
        self._tensors[min_site] = xp.tensordot(
            self[min_site], left_gate / np.sqrt(2), ([1], [2])
        )

        self._tensors[min_site] = self._tensors[min_site].transpose(0, 2, 3, 1)

        for idx in range(min_site, max_site):
            double_site = xp.tensordot(self[idx], self[idx + 1], ([3], [0]))
            # if np.isnan(double_site).any(): print(op)
            self._tensors[idx], self._tensors[idx + 1], _, singvals_cut = self.tSVD(
                double_site,
                [0, 1],
                [2, 3, 4],
                perm_right=[0, 2, 1, 3],
                contract_singvals="R",
            )

        self._tensors[max_site] = xp.tensordot(
            self[max_site], right_gate * np.sqrt(2), ([1, 2], [2, 1])
        )
        self._tensors[max_site] = self._tensors[max_site].transpose(0, 2, 1)

        # double_site = np.tensordot(self[max_site-1], self[max_site], ([3, 2], [0, 2]) )
        # self._tensors[max_site-1], self._tensors[max_site], _, singvals_cut = \
        #        self.tSVD(double_site, [0, 1], [2, 3], contract_singvals='R' )

        self._first_non_orthogonal_left = max_site
        self._first_non_orthogonal_right = max_site

        return singvals_cut

    def reset(self, idxs=None):
        """
        Reset the states of the sites idxs to the |0> state

        Parameters
        ----------
        idxs : int or list of ints, optional
            indexes of the sites to reinitialize to 0.
            If default value is left all the sites are restarted.
        """
        if idxs is None:
            idxs = np.arange(self.num_sites)
        elif np.isscalar(idxs):
            idxs = [idxs]
        else:
            idxs = np.array(idxs)
            idxs = np.sort(idxs)

        for idx in idxs:
            state, _ = self.apply_projective_operator(idx)
            if state != 0:
                new_projector = np.zeros((self._local_dim[idx], self._local_dim[idx]))
                new_projector[0, state] = 1
                self.apply_one_site_operator(new_projector, idx)

        self.left_canonize(self.num_sites - 1, svd=True)
        self.right_canonize(0, svd=True)

    def norm(self):
        """
        Returns the norm of the MPS <self|self>

        Return
        ------
        norm: float
            norm of the MPS
        """
        xp = self._device_checks()
        idx = self.first_non_orthogonal_right

        if self.first_non_orthogonal_left == self.first_non_orthogonal_right:
            norm = xp.tensordot(self[idx], xp.conj(self[idx]), ([0, 1, 2], [0, 1, 2]))
        else:
            self.left_canonize(self.first_non_orthogonal_right, keep_singvals=True)
            norm = xp.tensordot(self[idx], xp.conj(self[idx]), ([0, 1, 2], [0, 1, 2]))

        return np.sqrt(np.real(norm))

    def contract(self, other, boundaries=None):
        """
        Contract the MPS with another MPS other <other|self>.
        By default it is a full contraction, but also a partial
        contraction is possible

        Parameters
        ----------
        other : MPS
            other MPS to contract with
        boundaries : tuple of ints, optional
            Contract to MPSs from boundaries[0] to boundaries[1].
            In this case the output will be a tensor.
            Default to None, which is  full contraction

        Returns
        -------
        contraction : complex
            Result of the contraction
        """
        if not isinstance(other, MPS):
            raise TypeError("Only two MPS classes can be contracted")
        elif np.any(self.local_dim != other.local_dim):
            raise ValueError("Local dimension must be the same to contract MPS")
        elif self.num_sites != other.num_sites:
            raise ValueError(
                "Number of sites must be the same to contract two MPS together"
            )
        if boundaries is None:
            full_contraction = True
            boundaries = (0, self.num_sites, 1)
        else:
            full_contraction = False
            boundaries = (*boundaries, np.sign(boundaries[1] - boundaries[0]))

        xp = self._device_checks()

        idx = 0 if boundaries[1] > boundaries[0] else 2
        transfer_mat = xp.eye(self[boundaries[0]].shape[idx])
        for ii in range(*boundaries):
            if boundaries[2] > 0:
                transfer_mat = xp.tensordot(transfer_mat, self[ii], ([0], [idx]))
            else:
                transfer_mat = xp.tensordot(self[ii], transfer_mat, ([idx], [0]))

            transfer_mat = xp.tensordot(
                transfer_mat, xp.conj(other[ii]), ([idx, 1], [idx, 1])
            )
        if full_contraction:
            transfer_mat = transfer_mat.flatten()
            contraction = transfer_mat[0]
        else:
            new_shape = (
                (1, *transfer_mat.shape)
                if boundaries[1] > boundaries[0]
                else (*transfer_mat.shape, 1)
            )
            contraction = transfer_mat.reshape(new_shape)
        return contraction

    def kron(self, other, inplace=False):
        """
        Concatenate two MPS, taking the kronecker/outer product
        of the two states. The bond dimension assumed is the maximum
        between the two bond dimensions.

        Parameters
        ----------
        other : :py:class:`MPS`
            MPS to concatenate
        inplace : bool, optional
            If True apply the kronecker product in place. Instead, if
            inplace=False give as output the product. Default to False.

        Returns
        -------
        :py:class:`MPS`
            Concatenation of the first MPS with the second in order
        """
        if not isinstance(other, MPS):
            raise TypeError("Only two MPS classes can be concatenated")
        elif self[-1].shape[2] != 1 and other[0].shape[0] != 1:
            raise ValueError(
                "Head and tail of the MPS not compatible. Last "
                + "and first dimensions of the tensors must be the same"
            )
        elif self.device != other.device:
            raise RuntimeError(
                "MPS to be kron multiplied must be on the same "
                + f"device, not {self.device} and {other.device}"
            )
        max_bond_dim = max(self.max_bond_dim, other.max_bond_dim)
        cut_ratio = min(self.cut_ratio, other.cut_ratio)
        convergence_params = TNConvergenceParameters(
            max_bond_dimension=int(max_bond_dim), cut_ratio=cut_ratio
        )
        tensor_list = self.tensors + other.tensors

        addMPS = MPS.from_tensor_list(
            tensor_list, convergence_params, device=self.device
        )
        addMPS._singvals[: self.num_sites + 1] = self.singvals
        addMPS._singvals[self.num_sites + 1 :] = other.singvals[1:]

        if inplace:
            self.__dict__.update(addMPS.__dict__)
            return None
        else:
            return addMPS

    # ---------------------------
    # ----- MEASURE METHODS -----
    # ---------------------------

    def meas_tensor_product(self, ops, idxs):
        """
        Measure the tensor products of n operators `ops` acting on the indexes `idxs`

        Parameters
        ----------
        ops : list of ndarrays
            List of numpy arrays which are one-site operators
        idxs : list of int
            Indexes where the operators are applied

        Returns
        -------
        measure : float
            Result of the measurement
        """
        self.check_obs_input(ops, idxs)

        if len(idxs) == 0:
            return 1
        xp = self._device_checks()
        order = np.argsort(idxs)
        idxs = np.array(idxs)[order]
        ops = xp.array(ops)
        ops = ops[order]
        self.site_canonize(idxs[0], keep_singvals=True)

        transfer_mat = xp.eye(self[idxs[0]].shape[0], dtype=xp.complex64)
        jj = 0
        closed = False
        for ii in range(idxs[0], self.num_sites):
            if closed:
                break

            # Case of finished tensors
            if jj == len(idxs):
                # close with transfer matrix of correct size
                closing_transfer_mat = xp.eye(self[ii].shape[0])
                measure = xp.tensordot(
                    transfer_mat, closing_transfer_mat, ([0, 1], [0, 1])
                )
                closed = True
            # Case of operator inside
            elif idxs[jj] == ii:
                transfer_mat = xp.tensordot(transfer_mat, self[ii], ([0], [0]))
                transfer_mat = xp.tensordot(transfer_mat, ops[jj], ([1], [1]))
                transfer_mat = xp.transpose(transfer_mat, [0, 2, 1])
                transfer_mat = xp.tensordot(
                    transfer_mat, xp.conj(self[ii]), ([0, 1], [0, 1])
                )
                jj += 1
            # Case of no operator between the sites
            else:
                transfer_mat = xp.tensordot(transfer_mat, self[ii], ([0], [0]))
                transfer_mat = xp.tensordot(
                    transfer_mat, xp.conj(self[ii]), ([0, 1], [0, 1])
                )

        if not closed:
            # close with transfer matrix of correct size
            closing_transfer_mat = xp.eye(self[-1].shape[2])
            measure = xp.tensordot(transfer_mat, closing_transfer_mat, ([0, 1], [0, 1]))
            closed = True

        if xp == cp:
            measure = measure.get()

        return np.real(measure)

    def meas_weighted_sum(self, op_strings, idxs_strings, coefs):
        """
        Measure the weighted sum of tensor product operators.
        See :py:func:`meas_tensor_product`

        Parameters
        ----------
        op_strings : list of lists of ndarray
            list of tensor product operators
        idxs_strings : list of list of int
            list of indexes of tensor product operators
        coefs : list of complex
            list of the coefficients of the sum

        Return
        ------
        measure : complex
            Result of the measurement
        """
        if not (
            len(op_strings) == len(idxs_strings) and len(idxs_strings) == len(coefs)
        ):
            raise ValueError(
                "op_strings, idx_strings and coefs must all have the same length"
            )

        measure = 0.0
        for ops, idxs, coef in zip(op_strings, idxs_strings, coefs):
            measure += coef * self.meas_tensor_product(ops, idxs)

        return measure

    def meas_bond_entropy(self):
        """
        Measure the entanglement entropy along all the sites of the MPS
        using the Von Neumann entropy :math:`S_V` defined as:

        .. math::

            S_V = - \\sum_i^{\\chi} s^2 \\ln( s^2)

        with :math:`s` the singular values

        Return
        ------
        measures : dict
            Keys are the range of the bipartition from 0 to which the entanglement
            (value) is relative
        """
        xp = self._device_checks()
        measures = {}
        for ii, ss in enumerate(self.singvals[1:-1]):
            if ss is None:
                s_von_neumann = None
            else:
                s_von_neumann = -xp.sum(ss**2 * xp.log(ss**2))

            measures[(0, ii + 1)] = s_von_neumann

        return measures

    def meas_even_probabilities(self, threshold, qiskit_convention=False):
        """
        Compute the probabilities of measuring a given state if it is greater
        than a threshold. The function goes down "evenly" on the probability
        tree. This means that there is the possibility that no state is
        returned, if their probability is lower then threshold. Furthermore,
        notice that the **maximum** number of states returned is
        :math:`(\frac{1}{threshold})`.

        For a different way of computing the probability tree see the
        function :py:func:`meas_greedy_probabilities` or
        :py:func:`meas_unbiased_probabilities`.

        Parameters
        ----------
        threshold : float
            Discard all the probabilities lower then the threshold
        qiskit_convention : bool, optional
            If the sites during the measure are represented such that
            |201> has site 0 with value one (True, mimicks bits ordering) or
            with value 2 (False usually used in theoretical computations).
            Default to False.

        Return
        ------
        probabilities : dict
            Dictionary where the keys are the states while the values their
            probabilities. The keys are separated by a comma if local_dim > 9.
        """
        if threshold < 0:
            raise ValueError("Threshold value must be positive")
        elif threshold < 1e-3:
            warn(
                "be careful when you keep too much info: the function might"
                + "be exponentially slower"
            )

        # Put in canonic form
        self.right_canonize(0, keep_singvals=True)
        old_norm = self.norm()
        self._tensors[0] /= old_norm

        self._temp_for_prob = {}
        self._measure_even_probabilities(threshold, 1, "", 0, self[0])

        # Rewrite with qiskit convention
        probabilities = postprocess_statedict(
            self._temp_for_prob,
            local_dim=self.local_dim,
            qiskit_convention=qiskit_convention,
        )

        self._tensors[0] *= old_norm

        return probabilities

    def _measure_even_probabilities(self, threshold, probability, state, idx, tensor):
        """
        Hidden recursive function to compute the probabilities

        Parameters
        ----------
        threshold : float
            Discard of all state with probability less then the threshold
        probability : float
            probability of having that state
        states : string
            string describing the state up to that point
        idx : int
            Index of the tensor currently on the function
        tensor : np.ndarray
            Tensor to measure

        Returns
        -------
        probabilities : dict
            Dictionary where the keys are the states while the values their
            probabilities. The keys are separated by a comma if local_dim > 9.
        """
        local_dim = self.local_dim[idx]

        if probability > threshold:
            probabilities, tensors_list = self._get_children_prob(tensor, idx)
            # Multiply by the probability of having the given state
            probabilities = probability * probabilities
            states = [state + str(ii) + "," for ii in range(local_dim)]

            if idx < self.num_sites - 1:
                # Call recursive part
                for tens, prob, ss in zip(tensors_list, probabilities, states):
                    self._measure_even_probabilities(threshold, prob, ss, idx + 1, tens)
            else:
                # Save the results
                for prob, ss in zip(probabilities, states):
                    if prob > threshold:
                        ss = ss[:-1]  # Remove trailing comma
                        self._temp_for_prob[ss] = prob

    def meas_greedy_probabilities(self, max_prob, qiskit_convention=False):
        """
        Compute the probabilities of measuring a given state until the total
        probability measured is greater than the threshold max_prob.
        The function goes down "greedily" on the probability
        tree. This means that there is the possibility that a path that was
        most promising at the tree root will become very computationally
        demanding and not so informative once reached the leaves. Furthermore,
        notice that there is no **maximum** number of states returned, and so
        the function might be exponentially slow.

        For a different way of computing the probability tree see the
        function :py:func:`meas_even_probabilities` or
        :py:func:`meas_unbiased_probabilities`

        Parameters
        ----------
        max_prob : float
            Compute states until you reach this probability
        qiskit_convention : bool, optional
            If the sites during the measure are represented such that
            |201> has site 0 with value one (True, mimicks bits ordering) or
            with value 2 (False usually used in theoretical computations).
            Default to False.

        Return
        ------
        probabilities : dict
            Dictionary where the keys are the states while the values their
            probabilities. The keys are separated by a comma if local_dim > 9.
        """
        if max_prob > 0.95:
            warn(
                "Execution of the function might be exponentially slow due "
                + "to the highness of the threshold",
                RuntimeWarning,
            )

        # Set gauge on the left and renormalize
        self.right_canonize(0)
        old_norm = self.norm()
        self._tensors[0] /= old_norm

        all_probs = [{}]
        probabilities = {}
        probability_sum = 0

        tensor = self[0]
        site_idx = 0
        curr_state = ""
        curr_prob = 1
        while probability_sum < max_prob:
            if len(all_probs) < site_idx + 1:
                all_probs.append({})
            if site_idx > 0:
                states = [
                    curr_state + f",{ii}" for ii in range(self.local_dim[site_idx])
                ]
            else:
                states = [
                    curr_state + f"{ii}" for ii in range(self.local_dim[site_idx])
                ]
            # Compute the children if we didn't already follow the branch
            if not np.all([ss in all_probs[site_idx] for ss in states]):
                probs, tensor_list = self._get_children_prob(tensor, site_idx)
                probs = curr_prob * probs

                # Update probability tracker for next branch
                for ss, prob, tens in zip(states, probs, tensor_list):
                    all_probs[site_idx][ss] = [prob, tens]
            # Retrieve values if already went down the path
            else:
                probs = []
                tensor_list = []
                for ss, (prob, tens) in all_probs[site_idx].items():
                    probs.append(prob)
                    tensor_list.append(tens)
            # Greedily select the next branch if we didn't reach the leaves
            if site_idx < self.num_sites - 1:
                # Select greedily next path
                tensor = tensor_list[np.argmax(probs)]
                curr_state = states[np.argmax(probs)]
                curr_prob = np.max(probs)
                site_idx += 1
            # Save values if we reached the leaves
            else:
                for ss, prob in zip(states, probs):
                    if not np.isclose(prob, 0, atol=1e-10):
                        probabilities[ss] = prob
                        probability_sum += prob
                # Remove this probability from the tree
                for ii in range(self.num_sites - 1):
                    measured_state = states[0].split(",")[: ii + 1]
                    measured_state = ",".join(measured_state)
                    all_probs[ii][measured_state][0] -= np.sum(probs)
                # Restart from the beginning
                site_idx = 0
                curr_state = ""

        # Rewrite with qiskit convention
        final_probabilities = postprocess_statedict(
            probabilities, local_dim=self.local_dim, qiskit_convention=qiskit_convention
        )

        self._tensors[0] *= old_norm

        return final_probabilities

    def _get_children_prob(self, tensor, site_idx, *args):
        """
        Compute the probability and the relative tensor state of all the
        children of site `site_idx` in the tensor tree

        Parameters
        ----------
        tensor : np.ndarray
            Parent tensor, with respect to which we compute the children
        site_idx : int
            Index of the parent tensor
        args : list
            other arguments are not needed for the MPS implementation
            and stored in `*args`.

        Returns
        -------
        probabilities : list of floats
            Probabilities of the children
        tensor_list : list of ndarray
            Child tensors, already contracted with the next site
            if not last site.
        """
        xp = self._device_checks()
        local_dim = self.local_dim[site_idx]
        if tensor is None:
            return xp.zeros(local_dim), np.repeat(None, local_dim)

        conjg_tens = xp.conj(tensor)
        probabilities = []
        tensors_list = []

        # Construct rho at effort O(chi_l * chi_r * d^2) which is
        # equal to contracting one projector to one tensor
        reduced_rho = xp.diag(xp.tensordot(tensor, conjg_tens, ([0, 2], [0, 2])))

        # Loop over basis states
        for jj, prob_jj in enumerate(reduced_rho):
            # Compute probabilities of the state; projecting always to
            # one index `j`, we can read the diagonal entries of the
            # reduced density matrix
            probabilities.append(np.real(prob_jj))

            # Create list of updated tensors after the projection
            if prob_jj > 0 and site_idx < self.num_sites - 1:
                # Extract the rank-2 tensor without tensordot as we operator
                # on a diagonal projector with a single index
                temp_tens = tensor[:, jj, :]

                # Contract with the next site in the MPS
                temp_tens = xp.tensordot(temp_tens, self[site_idx + 1], ([1], [0]))
                tensors_list.append(temp_tens * (prob_jj ** (-0.5)))
            else:
                tensors_list.append(None)

        probabilities = xp.array(probabilities)
        if xp == cp:
            probabilities = probabilities.get()

        return probabilities, tensors_list

    def _get_children_magic(self, transfer_matrix, site_idx, *args):
        """
        Compute the probability and the relative tensor state of all the
        children of site `site_idx` in the tensor tree

        Parameters
        ----------
        transfer_matrix : np.ndarray
            Parent tensor, with respect to which we compute the children
        site_idx : int
            Index of the parent tensor
        args : list
            other arguments are not needed for the MPS implementation
            and stored in `*args`.

        Returns
        -------
        probabilities : list of floats
            Probabilities of the children
        tensor_list : list of ndarray
            Child tensors, already contracted with the next site
            if not last site.
        """
        xp = self._device_checks()

        if transfer_matrix is None:
            return xp.zeros(4), np.repeat(None, 4)

        tensor = deepcopy(self.get_tensor_of_site(site_idx))
        probabilities = xp.zeros(4)
        tensors_list = []

        paulis = [
            xp.identity(2),
            xp.array([[0, 1], [1, 0]]),
            xp.array([[0, -1j], [1j, 0]]),
            xp.array([[1, 0], [0, -1]]),
        ]
        original_transfer_matrix = deepcopy(transfer_matrix)
        for ii, pauli in enumerate(paulis):
            temp_tens = xp.tensordot(tensor, pauli, ([1], [1]))
            transfer_matrix = xp.tensordot(
                original_transfer_matrix, temp_tens, ([0], [0])
            )
            transfer_matrix = xp.tensordot(
                transfer_matrix, tensor.conj(), ([0, 2], [0, 1])
            )
            probabilities[ii] = np.real(
                xp.tensordot(transfer_matrix, transfer_matrix.conj(), ([0, 1], [0, 1]))
                / 2
            )
            if probabilities[ii] > 0 and site_idx < self.num_sites - 1:
                tensors_list.append(transfer_matrix / np.sqrt(probabilities[ii] * 2))
            else:
                tensors_list.append(None)

        if xp == cp:
            probabilities = probabilities.get()

        return probabilities, tensors_list

    def _get_child_prob(self, tensor, site_idx, target_prob, unitary_setup, *args):
        """
        Compute which child has to be selected for a given target probability
        and return the index and the tensor of the next site to be measured.

        Parameters
        ----------
        tensor : np.ndarray
            Tensor representing the site to be measured with a projective
            measurement.
        site_idx : int
            Index of the site to be measured and index of `tensor`.
        target_prob : scalar
            Scalar drawn from U(0, 1) and deciding on the which projective
            measurement outcome will be picked. The decision is based on
            the site `site_idx` only.
        unitary_setup : instance of :class:`UnitarySetupProjMeas` or `None`
            If `None`, no local unitaries are applied. Otherwise,
            unitary for local transformations are provided and applied
            to the local sites.
        args : list
            Other argument are not needed for the MPS implementation
            and stored in `*args`.
        """
        xp = self._device_checks()
        local_dim = self.local_dim[site_idx]

        if unitary_setup is not None:
            # Have to apply local unitary
            unitary = unitary_setup.get_unitary(site_idx)

            # Contract and permute back
            tensor = np.tensordot(unitary, tensor, ([1], [1]))
            tensor = np.transpose(tensor, [1, 0, 2])

        conjg_tens = xp.conj(tensor)

        # Calculate the cumulated probabilities via the reduced
        # density matrix
        reduced_rho = xp.tensordot(tensor, conjg_tens, ([0, 2], [0, 2]))
        probs = xp.real(xp.diag(reduced_rho))
        cumul_probs = xp.cumsum(probs)

        measured_idx = None

        for jj in range(local_dim):
            if cumul_probs[jj] < target_prob:
                continue

            prob_jj = probs[jj]

            # Reached interval with target probability ... project
            measured_idx = jj
            temp_tens = tensor[:, jj, :]
            temp_tens /= probs[jj] ** 0.5

            if site_idx < self.num_sites - 1:
                temp_tens = xp.tensordot(temp_tens, self[site_idx + 1], ([1], [0]))
            else:
                temp_tens = None

            break

        return measured_idx, temp_tens, prob_jj

    # ------------------------
    # ---- I/O Operations ----
    # ------------------------

    def write(self, filename, cmplx=True):
        """
        Write an MPS in python format into a FORTRAN format, i.e.
        transforms row-major into column-major

        Parameters
        ----------
        filename: str
            PATH to the file
        cmplx: bool, optional
            If True the MPS is complex, real otherwise. Default to True

        Returns
        -------
        None
        """
        self.to_device("cpu")
        with open(filename, "w") as fh:
            fh.write(str(len(self)) + " \n")
            for tens in self:
                write_tensor(tens, fh, cmplx=cmplx)

        return None

    @classmethod
    def read(cls, filename, cmplx=True, order="F", device="cpu"):
        """
        Read an MPS written by FORTRAN in a formatted way on file.
        Reads in column-major order but the output is in row-major.
        This is the only method that overrides the number of sites,
        since you may not know before reading.

        Parameters
        ----------
        filename: str
            PATH to the file
        cmplx: bool, optional
            If True the MPS is complex, real otherwise. Default to True
        order: str, optional
            If 'F' the tensor is transformed from column-major to row-major, if 'C'
            it is left as read.
        device: str, optional
            Device where the MPS is stored


        Returns
        -------
        obj: py:class:`MPS`
            MPS class read from file
        """
        tensors = []
        with open(filename, "r") as fh:
            num_sites = int(fh.readline())

            for _ in range(num_sites):
                tens = read_tensor(fh, cmplx=cmplx, order=order)
                tensors.append(tens)

        obj = cls.from_tensor_list(tensors)
        obj.to_device(device)

        return obj

    # ------------------------
    # ---- ML Operations -----
    # ------------------------
    def ml_get_gradient_tensor(self, idx, data_sample, true_label):
        """
        Get the gradient w.r.t. the tensors at position `idx`, `idx+1`
        of the MPS following the procedure explained in
        https://arxiv.org/pdf/1605.05775.pdf for the
        data_sample given

        Parameters
        ----------
        idx : int
            Index of the tensor to optimize
        data_sample : py:class:`MPS`
            Data sample in MPS class
        true_label : int
            True label of the datasample

        Returns
        -------
        xp.ndarray
            Gradient tensor
        """
        xp = self._device_checks()
        self.site_canonize(idx, True)

        if idx == 0:
            left_effective_feature = np.ones(1).reshape(1, 1)
        else:
            left_effective_feature = xp.squeeze(
                self.contract(data_sample, (0, idx)), axis=0
            )
        if idx == self.num_sites - 2:
            right_effective_feature = np.ones(1).reshape(1, 1)
        else:
            right_effective_feature = xp.squeeze(
                self.contract(data_sample, (self.num_sites - 1, idx + 1)), axis=2
            )

        # Compute the label efficiently
        label = left_effective_feature
        for ii in (idx, idx + 1):
            label = xp.tensordot(label, self[ii], ([0], [0]))
            label = xp.tensordot(label, xp.conj(data_sample[ii]), ([0, 1], [0, 1]))
        label = xp.tensordot(label, right_effective_feature, ([0, 1], [0, 1]))

        # Compute the loss function
        loss = true_label - xp.real(label)

        # Compute the gradient
        grad = xp.tensordot(left_effective_feature.conj(), data_sample[idx], ([1], [0]))
        grad = xp.tensordot(grad, data_sample[idx + 1], ([2], [0]))
        grad = xp.tensordot(grad, right_effective_feature.conj(), ([3], [1]))
        grad *= loss

        return grad, loss

    def ml_optmize_tensor(
        self, idx, data_samples, true_labels, learning_rate, n_jobs=1, direction=1
    ):
        """
        Optimize a single tensor using a batch of data damples

        Parameters
        ----------
        idx : int
            Index of the tensor to optimize
        data_samples : List[py:class:`MPS`]
            List of data samples
        true_labels : xp.ndarray
            List of labels (0 or 1)
        learning_rate : float
            Learining rate for the tensor update
        n_jobs : int, optional
            Number of parallel jobs for the optimization, by default 1

        Returns
        -------
        xp.ndarray
            Singular values cut in the optimization
        float
            Value of the loss function
        """
        xp = self._device_checks()

        # Canonize to idx
        self.site_canonize(idx, True)

        # Run in parallel the data batch
        res = xp.array(
            Parallel(n_jobs=n_jobs)(
                delayed(self.ml_get_gradient_tensor)(idx, ds, tl)
                for ds, tl in zip(data_samples, true_labels)
            ),
            dtype=object,
        )

        # Sum the values for computing gradient and loss
        grad = xp.sum(res[:, 0])
        loss = xp.sum(res[:, 1])

        # Compute the two_tensor of site idx, idx+1 for the update
        two_tensors = xp.tensordot(self[idx], self[idx + 1], ([2], [0]))
        two_tensors += learning_rate * grad

        # Split the tensor back and update the MPS
        direction = "R" if direction > 0 else "L"
        left, right, singvals, singval_cut = self.tSVD(
            two_tensors, [0, 1], [2, 3], contract_singvals=direction
        )
        self[idx] = left
        self[idx + 1] = right
        self.singvals[idx + 1] = singvals
        # self.normalize()

        return singval_cut, loss

    def ml_optimize_mps(
        self,
        data_samples,
        true_labels,
        batch_size,
        learning_rate,
        num_sweeps,
        n_jobs=1,
        verbose=False,
    ):
        """
        Optimize the MPS using the algorithm of Stoudenmire

        Parameters
        ----------
        data_samples : List[py:class:`MPS`]
            Feature dataset
        true_labels : List[int]
            Labels of the dataset
        batch_size : int
            Number of samples for a single sweep(epoch)
        learning_rate : float or callable
            Learning rate for the tensor update. If callable, it can depend on the sweep.
        num_sweeps : int
            Number of optimization sweeps (epochs)
        n_jobs : int, optional
            Number of parallel jobs for the optimization, by default 1
        verbose : bool, optional
            If True, print info about the optimization

        Returns
        -------
        xp.ndarray
            Singular values cut in the optimization
        xp.ndarray
            Value of the loss function at each sweep(epoch)
        """
        singvals_cut = np.zeros((self.num_sites - 1) * num_sweeps)
        loss = np.zeros(num_sweeps)

        # If learning rate is not callable do a constant function
        if not callable(learning_rate):
            learning_rate_f = lambda x: learning_rate
        else:
            learning_rate_f = learning_rate

        for nswp in range(num_sweeps):
            if verbose:
                print("=" * 20 + f" Sweep {nswp} started " + "=" * 20)

            # Select the training batch
            indexes = np.random.randint(0, len(data_samples), batch_size)
            current_samples = [data_samples[sii] for sii in indexes]
            current_labels = true_labels[indexes]

            # Left-to-right on even epochs, right-to-left for odd
            boundaries = (
                (0, self.num_sites - 1, 1)
                if nswp % 2 == 0
                else (self.num_sites - 2, -1, -1)
            )

            for ii in range(*boundaries):
                singv_cut, loss_ii = self.ml_optmize_tensor(
                    ii,
                    current_samples,
                    current_labels,
                    learning_rate_f(nswp),
                    n_jobs,
                    direction=boundaries[2],
                )

                # Postprocess the singvals as prescribed in the convergence parameters
                singvals_cut[
                    nswp * (self.num_sites - 1) + ii
                ] = self._postprocess_singvals_cut(singv_cut)
                # Save the loss function
                loss[nswp] += loss_ii

            loss[nswp] /= batch_size
            if verbose:
                print(f"Sweep loss: {loss[nswp]}")

        return singvals_cut, loss

    def ml_predict(self, data_samples, n_jobs=1):
        """
        Predict the labels of the data samples passed

        Parameters
        ----------
        data_samples : List[py:class:`MPS`]
            Feature dataset
        true_labels : List[int]
            Labels of the dataset
        n_jobs : int, optional
            Number of parallel jobs for the optimization, by default 1

        Returns
        -------
        List
            Predicted labels
        """

        labels = Parallel(n_jobs=n_jobs)(
            delayed(self.contract)(sample) for sample in data_samples
        )
        labels = np.round(labels)

        return labels
