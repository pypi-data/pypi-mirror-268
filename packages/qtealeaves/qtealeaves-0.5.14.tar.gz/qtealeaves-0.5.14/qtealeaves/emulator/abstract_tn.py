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
The module contains an abstract tensor network, from which other tensor
networks can be derived.
"""
import warnings
from copy import deepcopy
import numpy as np
import scipy as sp
import scipy.sparse.linalg as ssla
import mpmath as mp

# Try to import cupy
try:
    import cupy as cp
    import cupyx.scipy.sparse.linalg as csla
    from cupy_backends.cuda.api.runtime import CUDARuntimeError

    try:
        _ = cp.cuda.Device()
        GPU_AVAILABLE = True
    except CUDARuntimeError:
        GPU_AVAILABLE = False
except ImportError:
    cp = None
    GPU_AVAILABLE = False

# try to import mpi4py
try:
    from mpi4py import MPI
except ImportError:
    MPI = None

from qtealeaves.convergence_parameters import TNConvergenceParameters
from qtealeaves.modeling import IndexedOperator

__all__ = [
    "_AbstractTN",
    "postprocess_statedict",
    "UnitarySetupProjMeas",
    "TNnode",
    "MPI",
    "TN_MPI_TYPES",
]


# pickle in deepcopy fails if stored within the TN type
if MPI is not None:
    TN_MPI_TYPES = {
        "<c16": MPI.DOUBLE_COMPLEX,
        "<c8": MPI.COMPLEX,
        "<f4": MPI.REAL,
        "<f8": MPI.DOUBLE_PRECISION,
        "<i8": MPI.INT,
    }
else:
    TN_MPI_TYPES = {}


class TNnode:
    """
    Class to encode a node in a tensor network, to work
    with arbitrary tensor network.

    Parameters
    ----------
    layer: int
        Layer of the network where the node lives
    index: int
        Index of the tensor inside the layer
    children: list of TNnode
        Children nodes
    link_idx: int
        Number for the new index for the links
    """

    def __init__(self, layer, index, children, link_idx):
        self.layer = layer
        self.index = index

        if children is not None:
            self.link_idxs = []
            for child in children:
                child.add_parent(self)
                self.link_idxs.append(child.link_idxs[-1])
            self.link_idxs.append(link_idx)
        else:
            self.link_idxs = [link_idx + ii for ii in range(3)]
        self.children = children
        # By default, the parent is None and should be added with
        # the appropriate method
        self.parent = None

    def __repr__(self) -> str:
        return f"({self.layer}, {self.index})"

    def is_child(self, parent_node):
        """
        Check if the class is the child of `parent_node`

        Parameters
        ----------
        parent_node : TNnode
            Potential parent node

        Returns
        -------
        bool
            True if `parent_node` is the parent
        """
        return parent_node == self.parent

    def is_parent(self, child_node):
        """
        Check if the class is the parent of `child_node`

        Parameters
        ----------
        child_node : TNnode
            Potential child node

        Returns
        -------
        bool
            True if `child_node` is the child
        """
        return child_node in self.children

    def add_parent(self, parent):
        """
        Add the node `parent` as parent node of the class

        Parameters
        ----------
        parent : TNnode
            New parent node
        """
        self.parent = parent


class UnitarySetupProjMeas:
    """
    Setup for applying unitaries prior to a projective measurement
    via `meas_projective`.

    Parameters
    ----------

    unitaries : list of xp.ndarrays of rank-2
        List of unitaries, which will be applied to the local
        Hilbert space according to the mode.
    mode : char
        Mode `R`, we draw randomly unitaries from the list
        and apply them before the projective measurement.
        Mode `S` select the unitary at the corresponding site,
        i.e., the i-th site applies always the i-th unitary.
    """

    def __init__(self, unitaries, mode="R"):
        self.unitaries = unitaries
        self.mode = mode

        if mode not in ["R", "S"]:
            raise ValueError("Unknown mode for UnitarySetupProjMeas.")

    def get_unitary(self, site_idx):
        """
        Retrieve the unitary for a site.

        Parameters
        ----------
        site_idx : int
            Get unitary for this site. Although it has to be passed always,
            it is only evaluated in `mode=S`.

        Returns
        -------
        unitary : np.ndarray of rank-2
            Tensor to be applied as local unitary to the site.
        """
        if self.mode == "R":
            idx = np.random.randint(len(self.unitaries))
            return self.unitaries[idx]
        else:
            if site_idx >= len(self.unitaries):
                raise Exception("List of provided unitaries not long enough.")

            return self.unitaries[site_idx]


class _AbstractTN:
    """
    Abstract tensor network class with methods applicable to any
    tensor network.

    Parameters
    ----------

    num_sites: int
        Number of sites

    local_dim: int, optional
        Local dimension of the degrees of freedom. Default to 2.

    convergence_parameters: :py:class:`TNConvergenceParameters`
        Class for handling convergence parameters. In particular,
        in the python TN simulator, we are interested in:
        - the *maximum bond dimension* :math:`\\chi`;
        - the *cut ratio* :math:`\\epsilon` after which the singular
            values are neglected, i.e. if :math:`\\lamda_1` is the
            bigger singular values then after an SVD we neglect all the
            singular values such that
            :math:`\\frac{\\lambda_i}{\\lambda_1}\\leq\\epsilon`
    device: string, optional
        Device where to create the MPS. Default to 'cpu'.
        Implemented devices:
        - 'cpu'
        - 'gpu'
    dtype: np.dtype, optional
        Type of the tensors in the TN. By default `np.complex128`
    """

    implemented_devices = ("cpu", "gpu")

    def __init__(
        self,
        num_sites,
        convergence_parameters,
        local_dim=2,
        device="cpu",
        dtype=np.complex128,
    ):
        if isinstance(convergence_parameters, TNConvergenceParameters):
            max_bond_dim = convergence_parameters.max_bond_dimension
            cut_ratio = convergence_parameters.cut_ratio
        else:
            raise TypeError(
                "convergence parameters must be " + "TNConvergenceParameters class"
            )

        if max_bond_dim < 1:
            raise ValueError("The minimum bond dimension for a product state is 1")

        if cut_ratio <= 0:
            raise ValueError("The cut_ratio value must be positive")

        self._num_sites = num_sites
        self._local_dim = local_dim
        self.dtype = dtype

        self._convergence_parameters = convergence_parameters
        self._max_bond_dim = max_bond_dim
        self._cut_ratio = cut_ratio
        self._device = device
        self._iso_center = None
        self.eff_op = None
        self.comm = None

        self._initialize_mpi()

    def __repr__(self):
        """
        Return the class name as representation.
        """
        return self.__class__.__name__

    def __len__(self):
        """
        Provide number of sites in the TN.
        """
        return self.num_sites

    @property
    def cut_ratio(self):
        """Cut ratio for truncation of singular values"""
        return self._convergence_parameters.cut_ratio

    @property
    def num_sites(self):
        """Number of sites property"""
        return self._num_sites

    @property
    def local_dim(self):
        """Local dimension property"""
        return self._local_dim

    @property
    def device(self):
        """Device where the Tensor network is stored"""
        return self._device

    @property
    def max_bond_dim(self):
        """Maximum bond dimension property"""
        return self._convergence_parameters.max_bond_dimension

    def get_tensor_of_site(self, idx):
        """
        Generic function to retrieve the tensor for a specific site. Compatible
        across different tensor network geometries.

        Parameters
        ----------
        idx : int
            Return tensor containin the link of the local
            Hilbert space of the idx-th site.
        """
        raise NotImplementedError("This function has to be overwritten.")

    def norm(self):
        """
        Calculate the norm of the state.
        """
        raise NotImplementedError("This function has to be overwritten.")

    def normalize(self):
        """
        Normalize the state depending on its current norm.
        """
        factor = 1.0 / self.norm()
        self.scale(factor)

    def site_canonize(self, idx, keep_singvals=False):
        """
        Shift the isometry center to the tensor containing the
        corresponding site, i.e., move the isometry to a specific
        Hilbert space. This method can be implemented independent
        of the tensor network structure.

        Parameters
        ----------
        idx : int
            Index of the physical site which should be isometrized.
        keep_singvals : bool, optional
            If True, keep the singular values even if shifting the iso with a
            QR decomposition. Default to False.
        """
        raise NotImplementedError("This function has to be overwritten.")

    def get_rho_i(self, idx):
        """
        Get the reduced density matrix of the site at index idx

        Parameters
        ----------
        idx : int
            Index of the site
        """
        raise NotImplementedError("This function has to be overwritten.")

    def iso_towards(self, new_iso, keep_singvals=False, trunc=False, conv_params=None):
        """
        Shift the isometry center to the tensor at the
        corresponding position, i.e., move the isometry to a
        specific tensor, that might not be a physical.

        Parameters
        ----------
        new_iso :
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
        raise NotImplementedError("This function has to be overwritten.")

    def scale(self, factor):
        """
        Multiply the tensor network state by a scalar factor.

        Parameters
        ----------
        factor : float
            Factor for multiplication of current tensor network state.
        """
        raise NotImplementedError("This function has to be overwritten.")

    @staticmethod
    def tensordot_diagonal(tensor, diagonal, contr_legs):
        """
        Optimally contract a diagonal matrix represented as a vector
        with a tensor along the `contr_legs`.
        Instead of a matrix-matrix multiplication we perform a
        elementwise multiplication.

        Parameters
        ----------
        tensor : xp.ndarray
            Tensor to which the diagonal is contract
        diagonal : xp.ndarray
            Vector representing the diagonal matrix to contract
        contr_legs : list of ints
            Legs of the tensor along which you contract the diagonal

        Returns
        -------
        xp.ndarray
            Output tensor after the contraction
        """
        if np.isscalar(contr_legs):
            contr_legs = [contr_legs]

        t_shape = np.array(tensor.shape)
        # Legs to be contracted (columns in the matrix representation)
        contr_legs = list(contr_legs)
        # Legs that are not going to be contracted (rows in the matrix rep)
        not_contr_legs = [ss for ss in range(tensor.ndim) if ss not in contr_legs]
        transposition = not_contr_legs + contr_legs
        # Transpose and reshape in matrix
        matrix = tensor.transpose(transposition).reshape(
            -1, np.prod(t_shape[contr_legs])
        )
        # * is shorthand for xp.multiply
        matrix = matrix * diagonal

        return matrix.reshape(t_shape[transposition]).transpose(
            np.argsort(transposition)
        )

    def tSVD(
        self,
        tensor,
        legs_left,
        legs_right,
        perm_left=None,
        perm_right=None,
        contract_singvals="N",
        conv_params=None,
    ):
        """Perform a truncated Singular Value Decomposition by
        first reshaping the tensor into a legs_left x legs_right
        matrix, and permuting the legs of the ouput tensors if needed.
        If the contract_singvals = ('L', 'R') it takes care of
        renormalizing the output tensors such that the norm of
        the MPS remains 1 even after a truncation.

        Parameters
        ----------
        tensor : ndarray
            Tensor upon which apply the SVD
        legs_left : list of int
            Legs that will compose the rows of the matrix
        legs_right : list of int
            Legs that will compose the columns of the matrix
        perm_left : list of int, optional
            permutations of legs after the SVD on left tensor
        perm_right : list of int, optional
            permutation of legs after the SVD on right tensor
        contract_singvals: string, optional
            How to contract the singular values.
                'N' : no contraction
                'L' : to the left tensor
                'R' : to the right tensor
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters to use in the procedure. If None is given,
            then use the default convergence parameters of the TN.
            Default to None.

        Returns
        -------
        tens_left: ndarray
            left tensor after the SVD
        tens_right: ndarray
            right tensor after the SVD
        singvals: ndarray
            singular values kept after the SVD
        singvals_cutted: ndarray
            singular values cutted after the SVD, normalized with the biggest singval
        """
        xp = self._device_checks(tensor=tensor)

        if conv_params is None:
            conv_params = self._convergence_parameters
        elif not isinstance(conv_params, TNConvergenceParameters):
            raise ValueError(
                "conv_params must be TNConvergenceParameters or None, "
                + f"not {type(conv_params)}."
            )

        # Reshaping
        matrix = xp.transpose(tensor, legs_left + legs_right)
        shape_left = np.array(tensor.shape)[legs_left]
        shape_right = np.array(tensor.shape)[legs_right]
        matrix = matrix.reshape(np.prod(shape_left), np.prod(shape_right))

        # SVD decomposition
        try:
            mat_left, singvals_tot, mat_right = xp.linalg.svd(
                matrix, full_matrices=False
            )
        except np.linalg.LinAlgError:
            warnings.warn("gesdd SVD decomposition failed. Resorting to gesvd.")
            mat_left, singvals_tot, mat_right = sp.linalg.svd(
                matrix, full_matrices=False, lapack_driver="gesvd"
            )

        # Truncation
        cut, singvals, singvals_cutted = self._truncate_singvals(
            singvals_tot, conv_params
        )
        mat_left = mat_left[:, :cut]
        mat_right = mat_right[:cut, :]

        # Contract singular values if requested
        if contract_singvals.upper() == "L":
            mat_left = xp.multiply(mat_left, singvals)
        elif contract_singvals.upper() == "R":
            mat_right = xp.multiply(singvals, mat_right.T).T
        elif contract_singvals.upper() != "N":
            raise ValueError(
                f"Contract_singvals option {contract_singvals} is not "
                + "implemented. Choose between right (R), left (L) or None (N)."
            )

        # Reshape back to tensors
        tens_left = mat_left.reshape(list(shape_left) + [cut])
        if perm_left is not None:
            tens_left = xp.transpose(tens_left, perm_left)

        tens_right = mat_right.reshape([cut] + list(shape_right))
        if perm_right is not None:
            tens_right = xp.transpose(tens_right, perm_right)

        return tens_left, tens_right, singvals, singvals_cutted

    def QR(self, tensor, legs_left, legs_right, perm_left=None, perm_right=None):
        """Perform a QR Decomposition by
        first reshaping the tensor into a legs_left x legs_right
        matrix, and permuting the legs of the ouput tensors if needed.

        Parameters
        ----------
        tensor : ndarray
            Tensor upon which apply the QR
        legs_left : list of int
            Legs that will compose the rows of the matrix
        legs_right : list of int
            Legs that will compose the columns of the matrix
        perm_left : list of int, optional
            permutations of legs after the QR on left tensor
        perm_right : list of int, optional
            permutation of legs after the QR on right tensor

        Returns
        -------
        tens_left: ndarray
            left tensor after the QR (orthogonal tensor)
        tens_right: ndarray
            right tensor after the QR (triangular tensor)
        """
        xp = self._device_checks(tensor=tensor)

        # Reshaping
        matrix = xp.transpose(tensor, legs_left + legs_right)
        shape_left = np.array(tensor.shape)[legs_left]
        shape_right = np.array(tensor.shape)[legs_right]
        matrix = matrix.reshape(np.prod(shape_left), np.prod(shape_right))
        k_dim = np.min([matrix.shape[0], matrix.shape[1]])

        # QR decomposition
        mat_left, mat_right = xp.linalg.qr(matrix)

        # Reshape back to tensors
        tens_left = mat_left.reshape(list(shape_left) + [k_dim])
        if perm_left is not None:
            tens_left = xp.transpose(tens_left, perm_left)

        tens_right = mat_right.reshape([k_dim] + list(shape_right))
        if perm_right is not None:
            tens_right = xp.transpose(tens_right, perm_right)

        return tens_left, tens_right

    def tEQR(self, tens_left, tens_right, singvals_left, operator=None):
        """
        Perform an truncated ExpandedQR decomposition, generalizing the idea
        of https://arxiv.org/pdf/2212.09782.pdf for a general bond expansion
        given the isometry center of the network on  `tens_left`.
        It should be rather general for three-legs tensors, and thus applicable
        with any tensor network ansatz. Notice that, however, you do not have
        full control on the approximation, since you know only a subset of the
        singular values truncated.

        Parameters
        ----------
        tens_left: xp.array
            Left tensor
        tens_right: xp.array
            Right tensor
        singvals_left: xp.array
            Singular values array insisting on the link to the left of `tens_left`
        operator: xp.array or None
            Operator to contract with the tensors. If None, no operator is contracted

        Returns
        -------
        tens_left: ndarray
            left tensor after the EQR
        tens_right: ndarray
            right tensor after the EQR
        singvals: ndarray
            singular values kept after the EQR
        singvals_cutted: ndarray
            subset of thesingular values cutted after the EQR,
            normalized with the biggest singval
        """
        xp = self._device_checks()

        # Trial bond dimension
        eta = int(
            np.ceil(
                (1 + self._convergence_parameters.min_expansion_qr) * tens_left.shape[0]
            )
        )

        # Contract the two tensors together
        twotensors = xp.tensordot(tens_left, tens_right, (2, 0))
        twotensors = xp.tensordot(np.diag(singvals_left), twotensors, (1, 0))

        # Contract with the operator if present
        if operator is not None:
            twotensors = xp.tensordot(twotensors, operator, ([1, 2], [2, 3]))
        # For simplicity, transpose in the same order as obtained
        # after the application of the operator
        else:
            twotensors = twotensors.transpose(0, 3, 1, 2)

        # Apply first phase in expanding the bond dimension
        expansor = xp.eye(eta, np.prod(tens_left.shape[:2])).reshape(
            eta, *tens_left.shape[:2]
        )
        expanded_y0 = xp.tensordot(expansor, twotensors, ([1, 2], [0, 2]))
        expanded_y0 = xp.transpose(expanded_y0, [0, 2, 1])

        # Contract with the (i+1)th site dagger
        first_qr = xp.tensordot(twotensors, xp.conj(expanded_y0), ([1, 3], [2, 1]))
        first_q, _ = xp.linalg.qr(first_qr.reshape(-1, first_qr.shape[2]))
        first_q = first_q.reshape(first_qr.shape)

        # Contract the new q with the i-th site. The we would need a rq decomposition.
        second_qr = xp.tensordot(twotensors, np.conj(first_q), ([0, 2], [0, 1]))
        second_qr = second_qr.transpose(2, 1, 0)
        second_q, second_r = xp.linalg.qr(second_qr.reshape(second_qr.shape[0], -1).T)
        second_q = second_q.T.reshape(second_qr.shape)
        # To get the real R matrix I would have to transpose, but to avoid a double
        # transposition I simply avoid that
        # second_r = second_r.T

        # Second phase in the expansor
        eigvl, eigvc = xp.linalg.eigh(np.conj(second_r) @ second_r.T)
        # Singvals are sqrt of eigenvalues, and sorted in the opposite order
        singvals = np.sqrt(eigvl)[::-1]

        # Routine to select the bond dimension
        cut, singvals, singvals_cutted = self._truncate_singvals(singvals)
        tens_right = xp.tensordot(eigvc[:cut, ::-1], second_q, ([1], [0]))

        # Get the last tensor
        tens_left = xp.tensordot(twotensors, xp.conj(tens_right), ([1, 3], [2, 1]))

        return tens_left, tens_right, singvals, singvals_cutted

    def _truncate_singvals(self, singvals, conv_params=None):
        """
        Truncate the singular values followling the
        strategy selected in the convergence parameters class

        Parameters
        ----------
        singvals : np.ndarray
            Array of singular values
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters to use in the procedure. If None is given,
            then use the default convergence parameters of the TN.
            Default to None.

        Returns
        -------
        cut : int
            Number of singular values kept
        singvals_kept : np.ndarray
            Normalized singular values kept
        singvals_cutted : np.ndarray
            Normalized singular values cutted
        """
        xp = self._device_checks()

        if conv_params is None:
            conv_params = self._convergence_parameters
        elif not isinstance(conv_params, TNConvergenceParameters):
            raise ValueError(
                "conv_params must be TNConvergenceParameters or None, "
                + f"not {type(conv_params)}."
            )

        if conv_params.trunc_method == "R":
            cut = self._truncate_sv_ratio(singvals, conv_params)
        elif conv_params.trunc_method == "N":
            cut = self._truncate_sv_norm(singvals, conv_params)
        else:
            raise Exception(f"Unkown trunc_method {conv_params.trunc_method}")

        # Divide singvals in kept and cut
        singvals_kept = singvals[:cut]
        singvals_cutted = singvals[cut:]
        # Renormalizing the singular values vector to its norm
        # before the truncation
        norm_kept = xp.sum(singvals_kept**2)
        norm_trunc = xp.sum(singvals_cutted**2)
        normalization_factor = np.sqrt(norm_kept) / np.sqrt(norm_kept + norm_trunc)
        singvals_kept /= normalization_factor

        # Renormalize cut singular values to track the norm loss
        singvals_cutted /= np.sqrt(norm_trunc + norm_kept)

        return cut, singvals_kept, singvals_cutted

    def _truncate_sv_ratio(self, singvals, conv_params):
        """
        Truncate the singular values based on the ratio
        with the bigger one

        Parameters
        ----------
        singvals : np.ndarray
            Array of singular values
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters to use in the procedure.

        Returns
        -------
        cut : int
            Number of singular values kept
        """
        xp = self._device_checks()

        # Truncation
        lambda1 = singvals[0]
        cut = xp.nonzero(singvals / lambda1 < conv_params.cut_ratio)[0]
        if xp == cp:
            cut = cut.get()

        # Confront the cut w.r.t the maximum bond dimension
        if len(cut) > 0:
            cut = min(conv_params.max_bond_dimension, cut[0])
        else:
            cut = conv_params.max_bond_dimension
        cut = min(cut, len(singvals))

        return cut

    def _truncate_sv_norm(self, singvals, conv_params):
        """
        Truncate the singular values based on the
        total norm cut

        Parameters
        ----------
        singvals : np.ndarray
            Array of singular values
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters to use in the procedure.

        Returns
        -------
        cut : int
            Number of singular values kept
        """
        xp = self._device_checks()

        norm = xp.cumsum(singvals[::-1] ** 2) / xp.sum(singvals**2)
        # You get the first index where the constraint is broken,
        # so you need to stop an index before
        cut = xp.nonzero(norm > conv_params.cut_ratio)[0]
        if xp == cp:
            cut = cut.get()

        # Confront the cut w.r.t the maximum bond dimension
        if len(cut) > 0:
            cut = len(singvals) - cut[0]
            cut = min(conv_params.max_bond_dimension, cut)
        else:
            cut = conv_params.max_bond_dimension

        return cut

    def _postprocess_singvals_cut(self, singvals_cut, conv_params=None):
        """
        Postprocess the singular values cut after the application of a
        tSVD based on the convergence parameters. Either take the sum of
        the singvals (if `conv_params.trunc_tracking_mode` is `"C"`) or the maximum
        (if `conv_params.trunc_tracking_mode` is `"M"`).

        Parameters
        ----------
        singvals_cut : np.ndarray
            Singular values cut in a tSVD
        conv_params : TNConvergenceParameters, optional
            Convergence parameters. If None, the convergence parameters
            of the tensor network class is used, by default None

        Returns
        -------
        float
            The processed singvals
        """
        if conv_params is None:
            conv_params = self._convergence_parameters
        # If no singvals was cut append a 0 to avoid problems
        if len(singvals_cut) == 0:
            return 0

        if conv_params.trunc_tracking_mode == "M":
            singvals_cut = singvals_cut.max()
        elif conv_params.trunc_tracking_mode == "C":
            singvals_cut = (singvals_cut**2).sum()
        else:
            raise Exception(f"Unkown trunc_tracking_mode {conv_params.trunc_method}")

        return singvals_cut

    def to_device(self, device):
        """
        Move the TN class to the new device.
        Should be implemented by the derived class

        Parameters
        ----------
        device : string
            Device where to move the tensor network
        """
        if not device in self.implemented_devices:
            raise ValueError(
                f"Device {device} is not implemented. Select from "
                + f"{self.implemented_devices}"
            )
        return NotImplementedError("to_device must be implemented by the class")

    def _device_checks(self, return_sla=False, **kwargs):
        """
        Check if all the arguments of the function where
        _device_checks is called are on the correct device,
        select the correct

        Parameters
        ----------
        device : str
            Device where the computation should take place.
            If called inside an emulator it should be the
            emulator device
        return_sla : bool, optional
            If True, returns the handle to the sparse linear algebra.
            Either sp.sparse.linalg or cp.scipy.sparse.linalg.
            Default to False.
        **kwargs : array-like
            Array-like inputs to the function. If they are
            on the wrong device an exception is raised.
            The keyword is the identifier used in the raise
            statement

        Returns
        -------
        module handle
            cp if the device is GPU
            np if the device is CPU
        """
        if not GPU_AVAILABLE:
            xp = np
            xsla = ssla
        else:
            if self.device == "gpu":
                xp = cp
                xsla = csla
            elif self.device == "cpu":
                xp = np
                xsla = ssla

            for key, value in kwargs.items():
                xp_arg = cp.get_array_module(value)
                if xp_arg != xp:
                    raise ValueError(
                        f"Argument {key} is not "
                        + f"on the correct device. Should be {xp} but is {xp_arg}."
                    )

        if return_sla:
            return xp, xsla
        else:
            return xp

    #########################################
    ########## MEASUREMENT METHODS ##########
    #########################################

    def meas_local(self, op):
        """
        Measure a local observable along all sites of the MPS

        Parameters
        ----------
        op : ndarray, shape (local_dim, local_dim)
            local operator to measure

        Return
        ------
        measures : ndarray, shape (num_sites)
            Measures of the local operator along each site
        """
        self.check_obs_input(op)
        xp = self._device_checks()

        measures = xp.zeros(self.num_sites)

        # This subroutine can be parallelized if the singvals are stored using
        # joblib
        for ii in range(self.num_sites):
            rho_i = self.get_rho_i(ii)

            expectation = xp.trace(rho_i @ op)
            measures[ii] = xp.real(expectation)

        # Come back to CPU if on GPU
        if xp == cp:
            measures = measures.get()

        return measures

    def meas_magic(
        self, renyi_idx=2, num_samples=1000, return_probabilities=False, precision=14
    ):
        """
        Measure the magic of the state as defined
        in https://arxiv.org/pdf/2303.05536.pdf, with a given number of samples.
        To see how the procedure works see meas_unbiased_probabilities.

        Parameters
        ----------
        renyi_idx : int, optional
            Index of the renyi entropy you want to measure.
            If 1, measure the Von Neumann entropy. Default to 2.
        num_samples : int | List[int], optional
            Number of random number sampled for the unbiased probability measurement.
            If a List is passed, then the algorithm is run over several superiterations
            and each entry on num_samples is the number of samples of a superiteration.
            Default to 1000.
        return_probabilities : bool, optional
            If True, return the probability dict. Default to False.
        precision: int, optional
            Precision for the probability interval computation. Default to 14.
            For precision>15 mpmath is used, so a slow-down is expected.

        Returns
        -------
        float
            The magic of the state
        """
        if np.isscalar(num_samples):
            num_samples = [num_samples]

        # Sample the state probabilities
        opes_bound_probs = {}
        opes_probs = np.array([])
        for num_samp in num_samples:
            # Sample the numbers
            samples = np.random.rand(int(num_samp))
            # Do not perform the computation for the already sampled numbers
            probs, new_samples = _check_samples_in_bound_probs(
                samples, opes_bound_probs
            )
            opes_probs = np.hstack((opes_probs, probs))
            # Perform the sampling for the unseen samples
            bound_probs = self.meas_unbiased_probabilities(
                new_samples, mode="magic", precision=precision
            )
            opes_bound_probs.update(bound_probs)
            # Add the sampled probability to the numpy array
            probs, _ = _check_samples_in_bound_probs(new_samples, bound_probs)
            opes_probs = np.hstack((opes_probs, probs))

        # Compute the magic with the samples
        magic = -self.num_sites * np.log(2)
        # Pass from probability intervals to probability values
        if renyi_idx > 1:
            magic += np.log((opes_probs ** (renyi_idx - 1)).mean()) / (1 - renyi_idx)
        else:
            magic += -(np.log(opes_probs)).mean()

        if return_probabilities:
            return magic, opes_bound_probs
        else:
            return magic

    def meas_projective(
        self,
        nmeas=1024,
        qiskit_convention=False,
        seed=None,
        unitary_setup=None,
        do_return_probabilities=False,
    ):
        """
        Perform projective measurements along the computational basis state

        Parameters
        ----------
        nmeas : int, optional
            Number of projective measurements. Default to 1024.
        qiskit_convention : bool, optional
            If the sites during the measure are represented such that
            |201> has site 0 with value one (True, mimicks bits ordering) or
            with value 2 (False usually used in theoretical computations).
            Default to False.
        seed : int, optional
            If provided it sets the numpy seed for the random number generation.
            Default to None
        unitary_setup : `None` or :class:`UnitarySetupProjMeas`, optional
            If `None`, no local unitaries are applied during the projective
            measurements. Otherwise, the unitary_setup provides local
            unitaries to be applied before the projective measurement on
            each site.
            Default to `None`.
        do_return_probabilities : bool, optional
            If `False`, only the measurements are returned. If `True`,
            two arguments are returned where the first are the
            measurements and the second are their probabilities.
            Default to `False`

        Return
        ------
        measures : dict
            Dictionary where the keys are the states while the values the number of
            occurrences. The keys are separated by a comma if local_dim > 9.
        """
        if nmeas == 0:
            return {}

        if seed is not None and isinstance(seed, int):
            np.random.seed(seed)
        xp = self._device_checks()
        # Put in canonic form
        self.site_canonize(0)

        measures = []
        probabilities = []
        # Loop over number of measurements
        for _ in range(nmeas):
            state = np.zeros(self.num_sites, dtype=int)
            temp_tens = deepcopy(self.get_tensor_of_site(0))
            # Loop over tensors
            cumulative_prob = 1.0
            for ii in range(self.num_sites):
                target_prob = xp.random.rand()
                measured_idx, temp_tens, prob_ii = self._get_child_prob(
                    temp_tens, ii, target_prob, unitary_setup, state, qiskit_convention
                )
                cumulative_prob *= prob_ii

                # Save the measured state either with qiskit or
                # theoretical convention
                if qiskit_convention:
                    state[self.num_sites - 1 - ii] = measured_idx
                else:
                    state[ii] = measured_idx

            if self._local_dim.max() < 10:
                measures.append(xp.array2string(state, separator="")[1:-1])
            else:
                measures.append(xp.array2string(state, separator=",")[1:-1])

            probabilities.append(cumulative_prob)

        # Come back to CPU if on GPU
        if xp == cp:
            measures = cp.asnumpy(measures)
        states, counts = np.unique(measures, return_counts=True)
        probabilities = dict(zip(measures, probabilities))
        measures = dict(zip(states, counts))

        if do_return_probabilities:
            return measures, probabilities
        else:
            return measures

    def meas_unbiased_probabilities(
        self,
        num_samples,
        qiskit_convention=False,
        bound_probabilities=None,
        do_return_samples=False,
        precision=15,
        mode="projection_z",
    ):
        """
        Compute the probabilities of measuring a given state if its probability
        falls into the explored in num_samples values.
        The functions divide the probability space in small rectangles, draw
        num_samples random numbers and then follow the path until the end.
        The number of states in output is between 1 and num_samples.

        For a different way of computing the probability tree see the
        function :py:func:`meas_even_probabilities` or
        :py:func:`meas_greedy_probabilities`

        Parameters
        ----------
        num_samples : int
            Maximum number of states that could be measured.
        qiskit_convention : bool, optional
            If the sites during the measure are represented such that
            |201> has site 0 with value one (True, mimicks bits ordering) or
            with value 2 (False usually used in theoretical computations).
            Default to False.
        probability_bounds : dict, optional
            Bounds on the probability computed previously with this function,
            i.e. if a uniform random number has value
            `left_bound< value< right_bound` then you measure the state.
            The dict structure is `{'state' : (left_bound, right_bound)}`.
            If provided, it speed up the computations since the function will
            skip values in the intervals already known. By default None.
        do_return_samples : bool, optional
            Enables, if `True`, to return the random number used for sampling
            in addition to the `bound_probabilities`. If `False`, only the
            `bound_probabilities` are returned.
            Default to `False`
        precision : int, optional
            Decimal place precision for the mpmath package. It is only
            used inside the function, and setted back to the original after
            the computations. Default to 15.
            If it is 15 or smaller, it just uses numpy.
        mode : str, optional
            Mode of the unbiased sampling. Default is "projection_z", equivalent
            to sampling the basis states on the Z direction.
            Possibilities:
            - "projection_z"
            - "magic"

        Return
        ------
        bound_probabilities : dict
            Dictionary analogous to the `probability_bounds` parameter.
            The keys are separated by a comma if local_dim > 9.
        samples : np.ndarray
            Random numbers from sampling, only returned if activated
            by optional argument.
        """
        # Handle internal cache; keep if possible: if bound probabilities
        # are passed, it must be the same state and we can keep the
        # cache.
        do_clear_cache = bound_probabilities is None

        # Always set gauge to site=0; even if cache is not cleared,
        # the actual isometry center did not move
        self.site_canonize(0)

        # Normalize for quantum trajectories
        old_norm = self.norm()
        self.normalize()

        if mode == "projection_z":
            local_dim = self.local_dim
            get_children_prob = self._get_children_prob
            initial_tensor = self.get_tensor_of_site(0)
        elif mode == "magic":
            local_dim = np.repeat(4, self.num_sites)
            get_children_prob = self._get_children_magic
            initial_tensor = np.ones((1, 1))
        else:
            raise ValueError(f"mode {mode} not available for unbiased sampling")

        # ==== Initialize variables ====
        # all_probs is a structure to keep track of already-visited nodes in
        # the probability tree. The i-th dictionary of the list correspond to
        # a state measured up to the i-th site. Each dictionary has the states
        # as keys and as value the list [state_prob, state_tens]
        all_probs = [{} for _ in range(self.num_sites)]
        # Initialize precision
        old_precision = mp.mp.dps
        # This precision is pretty much independent of the numpy-datatype as
        # it comes from multiplication. However, it is important when we sum
        # for the intervals
        mpf_wrapper, almost_equal = _mp_precision_check(precision)
        # Sample uniformly in 0,1 the samples, taking into account the already
        # sampled regions given by bound_probabilities
        if np.isscalar(num_samples):
            samples, bound_probabilities = _resample_for_unbiased_prob(
                num_samples, bound_probabilities
            )
        else:
            samples = num_samples
            bound_probabilities = (
                {} if bound_probabilities is None else bound_probabilities
            )
        # ==== Routine ====
        for idx, sample in enumerate(samples):
            # If the sample is in an already sampled area continue
            if idx > 0:
                if left_prob_bound < sample < left_prob_bound + cum_prob:
                    continue
            # Set the current state to no state
            curr_state = ""
            # Set the current tensor to be measured to the first one
            tensor = deepcopy(initial_tensor)
            # Initialize the probability to 1
            curr_prob = 1
            # Initialize left bound of the probability interval. Arbitrary precision
            left_prob_bound = mpf_wrapper(0.0)
            # Loop over the sites
            for site_idx in range(0, self.num_sites):
                # Initialize new possible states, adding the digits of the local basis to
                # the state measured up to now
                if site_idx > 0:
                    states = [
                        curr_state + f",{ii}" for ii in range(local_dim[site_idx])
                    ]
                else:
                    states = [curr_state + f"{ii}" for ii in range(local_dim[site_idx])]

                # Compute the children if we didn't already follow the branch
                if not np.all([ss in all_probs[site_idx] for ss in states]):
                    # Remove useless information after the first cycle. This operation is
                    # reasonable since the samples are ascending, i.e. if we switch path
                    # we will never follow again the old paths.
                    if idx > 0:
                        all_probs[site_idx:] = [
                            {} for _ in range(len(all_probs[site_idx:]))
                        ]

                    # Compute new probabilities
                    probs, tensor_list = get_children_prob(
                        tensor, site_idx, curr_state, do_clear_cache
                    )

                    # Clear cache only upon first iteration
                    do_clear_cache = False

                    # get probs to arbitrary precision
                    # if precision > 15:
                    #    probs = mp.matrix(probs)
                    # Multiply by the probability of being in the parent state
                    # Multiplication is safe from the precision point of view
                    probs = curr_prob * probs

                    # Update probability tracker for next branch, avoiding
                    # useless additional computations
                    for ss, prob, tens in zip(states, probs, tensor_list):
                        all_probs[site_idx][ss] = [prob, tens]

                # Retrieve values if already went down the path
                else:
                    probs = []
                    tensor_list = []
                    for prob, tens in all_probs[site_idx].values():
                        probs.append(prob)
                        tensor_list.append(tens)

                # Select the next branch if we didn't reach the leaves
                # according to the random number sampled
                if site_idx < self.num_sites - 1:
                    cum_probs = np.cumsum(probs)  # Compute cumulative
                    # Select first index where the sample is lower than the cumulative
                    try:
                        meas_idx = int(np.nonzero(sample < cum_probs)[0][0])
                    except IndexError:
                        break
                    # Update run-time values based on measured index
                    tensor = deepcopy(tensor_list[meas_idx])
                    curr_state = states[meas_idx]
                    curr_prob = probs[meas_idx]
                    # Update value of the sample based on the followed path
                    sample -= np.sum(probs[:meas_idx])
                    # Update left-boundary value with probability remaining on the left
                    # of the measured index
                    if meas_idx > 0:
                        left_prob_bound += cum_probs[meas_idx - 1]
                # Save values if we reached the leaves
                else:
                    cum_prob = mpf_wrapper(0.0)
                    for ss, prob in zip(states, probs):
                        if not almost_equal((prob, 0)):
                            bound_probabilities[ss] = (
                                left_prob_bound + cum_prob,
                                left_prob_bound + cum_prob + prob,
                            )
                        cum_prob += prob

            # For TTN with caching strategy (empy interface implemeted
            # also for any abstract tensor network)
            all_probs = self.clear_cache(all_probs=all_probs, current_key=curr_state)

        # Rewrite with qiskit convention and remove commas if needed
        bound_probabilities = postprocess_statedict(
            bound_probabilities,
            local_dim=self.local_dim,
            qiskit_convention=qiskit_convention,
        )

        self.scale(old_norm)
        mp.mp.dps = old_precision

        if do_return_samples:
            return bound_probabilities, samples

        return bound_probabilities

    def _get_children_prob(self, tensor, site_idx, curr_state, do_clear_cache):
        """
        Compute the probability and the relative tensor state of all the
        children of site `site_idx` in the probability tree

        Parameters
        ----------

        tensor : np.ndarray
            Parent tensor, with respect to which we compute the children

        site_idx : int
            Index of the parent tensor

        curr_state : str
            Comma-separated string tracking the current state of all
            sites already done with their projective measurements.

        do_clear_cache : bool
            Flag if the cache should be cleared. Only read for first
            site when a new meausrement begins.

        Returns
        -------

        probabilities : list of floats
            Probabilities of the children

        tensor_list : list of ndarray
            Child tensors, already contracted with the next site
            if not last site.
        """
        # Cannot implement it here, it highly depends on the TN
        # geometry
        raise NotImplementedError("This function has to be overwritten.")

    def _get_children_magic(
        self, transfer_matrix, site_idx, curr_state, do_clear_cache
    ):
        """
        Compute the magic probability and the relative tensor state of all the
        children of site `site_idx` in the probability tree, conditioned on
        the transfer matrix

        Parameters
        ----------

        transfer_matrix : np.ndarray
            Parent tranfer matrix, with respect to which we compute the children

        site_idx : int
            Index of the parent tensor

        curr_state : str
            Comma-separated string tracking the current state of all
            sites already done with their projective measurements.

        do_clear_cache : bool
            Flag if the cache should be cleared. Only read for first
            site when a new meausrement begins.

        Returns
        -------

        probabilities : list of floats
            Probabilities of the children

        tensor_list : list of ndarray
            Child tensors, already contracted with the next site
            if not last site.
        """
        # Cannot implement it here, it highly depends on the TN
        # geometry
        raise NotImplementedError("This function has to be overwritten.")

    def clear_cache(self, num_qubits_keep=None, all_probs=None, current_key=None):
        """
        Clear cache until cache size is below cache limit again. This function
        is empty and works for any tensor network without cache. If the inhereting
        tensor network has a cache, it has to be overwritten.

        **Arguments**

        all_probs : list of dicts
            Contains already calculated branches of probability tree. Each
            TTN has to decide if they need to be cleaned up as well.
        """
        if self is None:
            # Never true, but prevent linter warning (needs self when
            # cache is actually defined) and unused arguments
            print("Args", num_qubits_keep, all_probs, current_key)
            return None

        return all_probs

    def _get_child_prob(
        self,
        tensor,
        site_idx,
        target_prob,
        unitary_setup,
        curr_state,
        qiskit_convention,
    ):
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

        curr_state : np.ndarray of rank-1 and type int
            Record of current projective measurements done so far.

        qiskit_convention : bool
            Qiskit convention, i.e., ``True`` stores the projective
            measurement in reverse order, i.e., the first qubit is stored
            in ``curr_state[-1]``. Passing ``False`` means indices are
            equal and not reversed.
        """
        # Cannot implement it here, it highly depends on the TN
        # geometry
        raise NotImplementedError("This function has to be overwritten.")

    def _contr_to_eff_op(self, tensor, ops_list, idx_list, idx_out):
        """
        Contract operators lists with tensor T and its dagger. Return effective
        Hamiltonian operators along idx_out (relative to T),
        resulting from contraction.

        Parameters
        ----------
        T: np.ndarray
                Tensor of the TTN to contract
        ops_list: list of lists of Operator
            list of local operator lists, each corresponding to a
            specific link.
        idx_list:   list of ints
            link indices (relative to T), each corresponding to
            a local operator list in ops_list.

        Returns
        ---------
        list
            list of Operators after contractions
        """
        xp = self._device_checks(tensor=tensor)

        # Put everything in the correct order
        sorting = np.argsort(idx_list)
        ops_list = np.array(ops_list, dtype=object)
        idx_list = np.array(idx_list)
        ops_list = ops_list[sorting]
        idx_list = idx_list[sorting]

        # Retrieve the ID of all the operator passed
        ops_ids = np.array(
            [[opjj.op_id for opjj in opii] for opii in ops_list], dtype=object
        )
        ops_ids_flattened = [op for ops_list in ops_ids for op in ops_list]
        # Get a list of unique IDs
        ids = np.sort(np.unique(ops_ids_flattened))

        tensor_len = len(tensor.shape)
        avail_idx = np.arange(tensor_len, dtype=int)
        avail_idx = np.delete(avail_idx, idx_out)

        new_ops = []
        # We could run this for cycle in parallel
        for op_id in ids:
            idxs = [np.nonzero(ops_id == op_id)[0] for ops_id in ops_ids]
            temp = deepcopy(tensor)
            entered = False
            for ii, common_id in enumerate(idxs):
                # If that ID is present in the list
                if len(common_id) == 1:
                    # Perform the contraction
                    temp = xp.tensordot(
                        temp, ops_list[ii][common_id[0]].op, ([idx_list[ii]], [1])
                    )
                    temp = temp.transpose(_transpose_idx(tensor_len, idx_list[ii]))
                    # Record the coefficient
                    coeff = ops_list[ii][common_id[0]].coeff
                    entered = True

            if entered:
                # Perform the contraction with the complex conjugate
                # This order avoids an extra transposition
                new_t = xp.tensordot(xp.conj(tensor), temp, (avail_idx, avail_idx))

                # Append to the new operators
                new_ops.append(IndexedOperator(new_t, op_id, coeff))

        return new_ops

    def _contract_tensor_lists(self, vector, pos, ops_list, idx_list):
        """
        Linear operator to contract all the effective operators
        around the tensor in position `pos`. Used in the optimization.

        Parameters
        ----------
        vector : np.ndarray
            tensor in position pos in vector form
        pos : list of int
            list of [layer_idx, tensor_idx]

        Returns
        -------
        np.ndarray
            vector after the contraction of the effective operators
        """
        if pos != self._iso_center:
            raise RuntimeError(
                "Tried efficient operators contraction not at the iso_center"
            )
        xp = self._device_checks()

        tensor_shape = self[pos].shape
        tensor_len = len(tensor_shape)
        tensor = vector.reshape(tensor_shape)

        # Put everything in the correct order
        sorting = np.argsort(idx_list)
        ops_list = np.array(ops_list, dtype=object)
        idx_list = np.array(idx_list)
        ops_list = ops_list[sorting]
        idx_list = idx_list[sorting]

        # Retrieve the ID of all the operator passed
        ops_ids = np.array(
            [[opjj.op_id for opjj in opii] for opii in ops_list], dtype=object
        )
        # Get a list of unique IDs
        ops_ids_flattened = [op for ops_list_id in ops_ids for op in ops_list_id]
        ids = np.sort(np.unique(ops_ids_flattened))

        new_tens = xp.zeros_like(tensor, dtype=complex)
        # We could run this for cycle in parallel
        for op_id in ids:
            idxs = [np.nonzero(ops_id == op_id)[0] for ops_id in ops_ids]
            temp = deepcopy(tensor)
            entered = False
            for ii, common_id in enumerate(idxs):
                # If that ID is present in the list
                if len(common_id) == 1:
                    # Perform the contraction
                    temp = xp.tensordot(
                        temp, ops_list[ii][common_id[0]].op, ([idx_list[ii]], [1])
                    )
                    temp = temp.transpose(_transpose_idx(tensor_len, idx_list[ii]))
                    # Record the coefficient
                    coeff = ops_list[ii][common_id[0]].coeff
                    entered = True
            # Update the tensor
            if entered:
                new_tens += coeff * temp

        return new_tens.reshape(-1)

    def _get_eff_op_on_pos(self, pos):
        """
        Obtain the list of effective operators adjacent
        to the position pos and the index where they should
        be contracted

        Parameters
        ----------
        pos :
            key to the desired tensor

        Returns
        -------
        list of IndexedOperators
            List of effective operators
        list of ints
            Indexes where the operators should be contracted
        """
        raise NotImplementedError("This function has to be overwritten")

    def compute_energy(self, pos=None):
        """
        Compute the energy of the TTN through the effective operator
        at position pos.

        Parameters
        ----------
        pos : list, optional
            If a position is provided, the isometry is first shifted to
            that position and then the energy is computed. If None,
            the current isometry center is computed, by default None

        Returns
        -------
        float
            Energy of the TTN
        """
        xp = self._device_checks()
        if self.eff_op is None:
            raise RuntimeError("Tried to compute energy with no effective operators")
        # Move the iso center if needed
        if pos is not None:
            self.iso_towards(pos)

        # Retrieve the tensor at the isometry
        tens = self[self._iso_center]
        # Get the list of operators to contract
        ops_list, ops_idxs = self._get_eff_op_on_pos(self._iso_center)
        # Contract the tensor with the effective operators around
        vec = self._contract_tensor_lists(
            tens.reshape(-1), self._iso_center, ops_list, ops_idxs
        )

        # Contract the obtained tensor with the complex conjugate of the tree
        cidxs = np.arange(len(tens.shape))
        energy = xp.tensordot(vec.reshape(tens.shape), np.conj(tens), (cidxs, cidxs))
        if xp == cp:
            energy = energy.get()

        return np.real(energy)

    #########################################################################
    ######################### Optimization methods ##########################
    #########################################################################

    def optimize_single_tensor(self, pos, verbose=False):
        """
        Optimize the tensor at position `pos` based on the
        effective operators loaded in the TTN

        Parameters
        ----------
        pos : list of ints or int
            Position of the tensor in the TN
        verbose : bool, optional
            If True, prints informations about the diagonalization.
            Default to False.
        """
        xp, xsla = self._device_checks(return_sla=True)
        if verbose:
            print("-" * 50)
            print(f"Optimizing tensor {pos[1]} in layer {pos[0]}")
        # Isometrise towards the desired tensor
        self.iso_towards(pos)
        # Retrieve the tensor
        tensor = self[pos]
        ham_dim = int(np.prod(tensor.shape))

        # Get the list of operators to contract
        ops_list, ops_idxs = self._get_eff_op_on_pos(self._iso_center)
        # perform the diagonalization of the effective Hamiltonian
        # with the ARNOLDI method of ARPACK (in Scipy), by using
        # the LinearOperator strategy
        # ------------------------------- IMPORTANT ---------------------------------
        # | We put a - sign in the linear operator in order to use the              |
        # | Largest Amplitude search (LA) instead of Smallest Amplitude search (SA) |
        # | in eigsh routine, since the latter is not available for the GPU.        |
        # ---------------------------------------------------------------------------
        lin_op = xsla.LinearOperator(
            (ham_dim, ham_dim),
            matvec=lambda v: -self._contract_tensor_lists(v, pos, ops_list, ops_idxs),
        )

        tolerance = self._convergence_parameters.sim_params["arnoldi_min_tolerance"]
        if xp == np:
            eigenvalues, eigenvectors = xsla.eigsh(
                lin_op,
                k=1,
                which="LA",
                v0=tensor.reshape(-1),
                ncv=None,
                maxiter=None,
                tol=tolerance,
                return_eigenvectors=True,
            )
        else:
            eigenvalues, eigenvectors = xsla.eigsh(
                lin_op,
                k=1,
                which="LA",
                ncv=None,
                maxiter=None,
                tol=tolerance,
                return_eigenvectors=True,
            )

        # Substitute old tensor with new optimized tensor
        self[pos] = eigenvectors.reshape(tensor.shape)
        if verbose:
            print(f"New energy is E={np.real(eigenvalues[0])}")
            print("-" * 50)

    #########################################################################
    ########################## Observables methods ##########################
    #########################################################################
    def check_obs_input(self, ops, idxs=None):
        """
        Check if the observables are in the right
        format

        Parameters
        ----------
        ops : list of np.ndarray or np.ndarray
            Observables to measure
        idxs: list of ints, optional
            If has len>0 we expect a list of operators, otherwise just one.

        Return
        ------
        None
        """
        if np.isscalar(self.local_dim):
            local_dim = np.repeat(self.local_dim, self.num_sites)
        else:
            local_dim = self.local_dim
        if not np.all(local_dim == local_dim[0]):
            raise RuntimeError("Measurement not defined for non-constant local_dim")

        if idxs is None:
            ops = [ops]

        for op in ops:
            if list(op.shape) != [local_dim[0]] * 2:
                raise ValueError(
                    "Input operator should be of shape (local_dim, local_dim)"
                )

        if idxs is not None:
            if len(idxs) != len(ops):
                raise ValueError(
                    "The number of indexes must match the number of operators"
                )

    #########################################################################
    ############################## MPI methods ##############################
    #########################################################################
    def _initialize_mpi(self):
        if (MPI is not None) and (MPI.COMM_WORLD.Get_size() > 1):
            self.comm = MPI.COMM_WORLD

    def mpi_send_tensor(self, tensor, to_):
        """
        Send the tensor in position `tidx` to the process
        `to_`.

        Parameters
        ----------
        tensor : xp.ndarray
            Tensor to send
        to_ : int
            Index of the process where to send the tensor

        Returns
        -------
        None
        """
        # Send the dim of the shape
        self.comm.send(tensor.ndim, to_)
        shape = np.array(list(tensor.shape), dtype=int)
        # Send the shape first
        self.comm.Send([shape, TN_MPI_TYPES["<i8"]], to_)
        # Send the tensor
        self.comm.Send([tensor, TN_MPI_TYPES[tensor.dtype.str]], to_)

    def mpi_receive_tensor(self, from_):
        """
        Receive the tensor from the process `from_`.


        Parameters
        ----------
        from_ : int
            Index of the process that sent the tensor

        Returns
        -------
        xp.ndarray
            Received tensor
        """
        # Receive the number of legs
        ndim = self.comm.recv(source=from_)

        # Receive the shape
        shape = np.empty(ndim, dtype=int)
        self.comm.Recv([shape, TN_MPI_TYPES["<i8"]], from_)

        # Receive the tensor
        tens = np.empty(shape, dtype=self.dtype)
        self.comm.Recv([tens, TN_MPI_TYPES[np.dtype(self.dtype).str]], from_)

        return tens


def postprocess_statedict(state_dict, local_dim=2, qiskit_convention=False):
    """
    Remove commas from the states defined as keys of statedict
    and, if `qiskit_convention=True` invert the order of the
    digits following the qiskit convention

    Parameters
    ----------
    state_dict : dict
        State dictionary, which keys should be of the format
        'd,d,d,d,d,...,d' with d from 0 to local dimension
    local_dim : int or array-like of ints, optional
        Local dimension of the sites. Default to 2
    qiskit_convention : bool, optional
        If True, invert the digit ordering to follow qiskit
        convention

    Return
    ------
    dict
        The postprocessed state dictionary
    """
    # Check on parameter
    if np.isscalar(local_dim):
        local_dim = [local_dim]

    postprocecessed_state_dict = {}
    for key, val in state_dict.items():
        # If the maximum of the local_dim is <10
        # remove the comma, since the definition
        # is not confusing
        if np.max(local_dim) < 10:
            key = key.replace(",", "")
        # Invert the values if qiskit_convention == True
        if qiskit_convention:
            postprocecessed_state_dict[key[::-1]] = val
        else:
            postprocecessed_state_dict[key] = val

    return postprocecessed_state_dict


def _resample_for_unbiased_prob(num_samples, bound_probabilities):
    """
    Sample the `num_samples` samples in U(0,1) to use in the function
    :py:func:`meas_unbiased_probabilities`. If `bound_probabilities`
    is not None, then the function checks that the number of samples
    outside the ranges already computed in bound_probabilities are
    not in total num_samples. The array returned is sorted ascendingly

    Parameters
    ----------
    num_samples : int
        Number of samples to be drawn for :py:func:`meas_unbiased_probabilities`
    bound_probabilities : dict or None
        See :py:func:`meas_unbiased_probabilities`.

    Return
    ------
    np.ndarray
        Sorted samples in (0,1)
    dict
        Empty dictionary if bound_probabilities is None, otherwise the
        bound_probabilities input parameter.
    """
    if (bound_probabilities is None) or (len(bound_probabilities) == 0):
        # Contains the boundary probability of measuring the state, i.e. if a uniform
        # random number has value left_bound< value< right_bound then you measure the
        # state. The dict structure is {'state' : [left_bound, right_bound]}
        bound_probabilities = {}
        samples = np.random.uniform(0, 1, num_samples)
    else:
        # Prepare the functions to be used later on based on precision
        mpf_wrapper, almost_equal = _mp_precision_check(mp.mp.dps)
        # Go on and sample until you reach an effective number of num_samples,
        # withouth taking into account those already sampled in the given
        # bound_probabilities
        bounds_array = np.zeros((len(bound_probabilities), 2))
        for idx, bound in enumerate(bound_probabilities.values()):
            bounds_array[idx, :] = bound
        bounds_array = bounds_array[bounds_array[:, 0].argsort()]

        # Immediatly return if almost all the space has been measured
        if almost_equal(
            (np.sum(bounds_array[:, 1] - bounds_array[:, 0]), mpf_wrapper(1.0))
        ):
            return np.random.uniform(0, 1, 1), bound_probabilities

        # Sample unsampled areas. First, prepare array for sampling
        array_for_sampling = []
        last_bound = 0
        last_idx = 0
        while not almost_equal((last_bound, mpf_wrapper(1.0))):
            # Skip if interval already measured
            if last_idx < len(bounds_array) and almost_equal(
                (last_bound, bounds_array[last_idx, 0])
            ):
                last_bound = bounds_array[last_idx, 1]
                last_idx += 1
            # Save interval
            else:
                if 0 < last_idx < len(bounds_array):
                    array_for_sampling.append(
                        [bounds_array[last_idx - 1, 1], bounds_array[last_idx, 0]]
                    )
                    last_bound = bounds_array[last_idx, 0]
                elif last_idx == len(bounds_array):
                    array_for_sampling.append([bounds_array[last_idx - 1, 1], 1])
                    last_bound = 1
                else:  # Initial case
                    array_for_sampling.append([0, bounds_array[last_idx, 0]])
                    last_bound = bounds_array[last_idx, 0]

        nparray_for_sampling = np.array(array_for_sampling)
        # Sample from which intervals you will sample
        sample_prob = nparray_for_sampling[:, 1] - nparray_for_sampling[:, 0]
        sample_prob /= np.sum(sample_prob)
        intervals_idxs = np.random.choice(
            np.arange(len(array_for_sampling)),
            size=num_samples,
            replace=True,
            p=sample_prob,
        )
        intervals_idxs, num_samples_per_interval = np.unique(
            intervals_idxs, return_counts=True
        )

        # Finally perform uniform sampling
        samples = np.zeros(1)
        for int_idx, num_samples_int in zip(intervals_idxs, num_samples_per_interval):
            interval = nparray_for_sampling[int_idx, :]
            samples = np.hstack(
                (samples, np.random.uniform(*interval, size=num_samples_int))
            )
        samples = samples[1:]

    # Sort the array
    samples = np.sort(samples)

    return samples, bound_probabilities


def _transpose_idx(num_legs, contracted_idx):
    """
    Transpose in the original order the indexes
    of a n-legs tensor contracted over the
    index `contracted_idx`

    Parameters
    ----------
    contracted_idx : int
        Index over which there has been a contraction

    Returns
    -------
    tuple
        Indexes for the transposition
    """
    if contracted_idx > num_legs - 1:
        raise ValueError(
            f"Cannot contract leg {contracted_idx} of tensor with {num_legs} legs"
        )
    # Until the contracted idx the ordering is correct
    idxs = np.arange(contracted_idx)
    # Then the last
    idxs = np.append(idxs, num_legs - 1)
    idxs = np.hstack((idxs, np.arange(contracted_idx, num_legs - 1)))

    return idxs


def _projector(idxs, shape, xp=np):
    """
    Generate a projector of a given shape on the
    subspace identified by the indexes idxs

    Parameters
    ----------
    idxs : int or array-like of ints
        Indexes where the diagonal of the projector is 1,
        i.e. identifying the projector subspace
    shape : int or array-like of ints
        Dimensions of the projector. If an int, it is
        assumed a square matrix
    xp : module handle
        Module handle for the creation of the projector.
        Possible are np (cpu) or cp (cpu). Default to np.
    """
    if np.isscalar(idxs):
        idxs = [idxs]
    if np.isscalar(shape):
        shape = (shape, shape)

    idxs = np.array(idxs, dtype=int)
    projector = xp.zeros(shape)
    projector[idxs, idxs] = 1
    return projector


def _mp_precision_check(precision):
    """
    Based on the precision selected, gives
    a wrapper around the initialization of
    variables and almost equal check.
    In particolar, if `precision>15`,
    use mpmath library

    Parameters
    ----------
    precision : int
        Precision of the computations

    Return
    ------
    callable
        Initializer for variables
    callable
        Almost equal check for variables
    """
    if precision > 15:
        mpf_wrapper = lambda x: mp.mpf(x)
        almost_equal = lambda x: mp.almosteq(
            x[0], x[1], abs_eps=mp.mpf(10 ** (-precision))
        )
    else:
        mpf_wrapper = lambda x: x
        almost_equal = lambda x: np.isclose(x[0], x[1], atol=10 ** (-precision), rtol=0)

    return mpf_wrapper, almost_equal


def _check_samples_in_bound_probs(samples, bound_probabilities):
    """
    Check if the samples are falling in the probability intervals
    defined by the dictionary bound_probabilities, received as
    output by the OPES/unbiased sampling

    Parameters
    ----------
    samples : np.ndarray
        List of samples
    bound_probabilities : dict
        Dictionary of bound probabilities, where the key is the
        measure and the values the intervals of probability

    Returns
    -------
    np.ndarray(float)
        The probability sampled by samples, repeated the correct
        amount of times
    np.ndarray(float)
        The subset of the original samples not falling into the
        already measured intervals
    """
    if len(bound_probabilities) == 0:
        return [], samples

    bound_probs = np.array(list(bound_probabilities.values()))
    left_bound = bound_probs[:, 0]
    right_bound = bound_probs[:, 1]
    probs = bound_probs[:, 1] - bound_probs[:, 0]
    new_samples = []

    def get_probs(sample, new_samples):
        condition = np.logical_and(sample < right_bound, sample > left_bound)

        if not any(condition):
            new_samples.append(sample)
            return -1
        else:
            res = probs[condition]
            return res[0]

    # get_probs = np.vectorize(get_probs)
    probablity_sampled = np.array([get_probs(ss, new_samples) for ss in samples])

    probablity_sampled = probablity_sampled[probablity_sampled > 0].astype(float)

    return probablity_sampled, np.array(new_samples)
