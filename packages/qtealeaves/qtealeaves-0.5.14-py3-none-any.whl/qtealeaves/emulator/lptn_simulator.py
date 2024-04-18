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
This module contains a light-weight LPTN emulator.
"""
from copy import deepcopy
import numpy as np
import numpy.linalg as nla
from qtealeaves.convergence_parameters import TNConvergenceParameters
from ..fortran_interfaces import write_tensor, read_tensor
from .abstract_tn import _AbstractTN


class LPTN(_AbstractTN):
    """
    LOCALLY PURIFIED TENSOR NETWORK CLASS - operator
    order of legs: 0 - left bond, 1 - lower (physical) leg,
    2 - upper leg, 3 - right bond


    Parameters
    ----------
    num_sites : int
        Number of sites
    conv_params : :py:class:`TNConvergenceParameters`
        Input for handling convergence parameters.
        In particular, in the LPTN simulator we
        are interested in:
        - the maximum bond dimension (max_bond_dimension)
        - the cut ratio (cut_ratio) after which the
        singular values in SVD are neglected, all
        singular values such that
        :math:`\\lambda` /:math:`\\lambda_max`
        <= :math:`\\epsilon` are truncated

    local_dim : int, optional
        Dimension of Hilbert space of single site
        (defined as the same for each site).
        Default is 2
    iso_center : None or list of two ints, optional
        Isometry center is between the two sites
        specified in a list. The counting starts at 1.
        If the LPTN has no
        isometry center, iso_center = None.
        Default is None
    dtype : dtype, optional
        Type of entries for the tensor.
        Default is np.complex128

    Initialization
    --------------

    |000...000><000---000|

    Tensor representation
    ---------------------

    .. codeblock::

      |   |   |   |   |
    --O---O---O---O---O--  } --> complex conjugates of tensors below,
      |   |   |   |   |          access with LPTN.cc_tensors
    --O---O---O---O---O--  } --> these are contained in LPTN.tensors
      |   |   |   |   |


    Attributes
    ----------
    LPTN.num_sites : int
        Number of sites
    LPTN.local_dim : int
        Local Hilbert space dimension
    LPTN.tensors : list
        Values of tensors in LPTN
    LPTN.cc_tensors : list
        Values of tensors in complex conjugate part of
        LPTN
    LPTN._max_bond_dim : int
        Maximal bond dimension
    LPTN._cut_ratio : float
        Cut ratio
    LPTN.iso_center : None or list of int, optional
        Isometry center is between the two sites
        specified in a list. The counting starts at 1.
        If the LPTN has no
        isometry center, iso_center = None.
    """

    def __init__(
        self, num_sites, conv_params, local_dim=2, iso_center=None, dtype=np.complex128
    ):
        super().__init__(num_sites, conv_params, local_dim=local_dim)

        self.dtype = dtype

        # initialize tensors as |00...0>
        one_site = np.zeros((1, local_dim, local_dim, 1), dtype=dtype)
        one_site[0, 0, 0, 0] = 1
        default = [one_site for ii in np.repeat(None, num_sites)]
        self.tensors = default

        if isinstance(iso_center, (np.ndarray, list)):
            if not all(isinstance(element, int) for element in iso_center) or (
                len(iso_center) != 2
            ):
                raise TypeError(
                    "iso_center must be None or list of two"
                    " ints, not list of "
                    f"{len(iso_center)} "
                    f"{type(iso_center[0])}."
                )

        elif iso_center is not None:
            raise TypeError(
                f"iso_center must be None or list of two ints, not {type(iso_center)}."
            )

        self.iso_center = iso_center

    @property
    def cc_tensors(self):
        """
        complex conjugate part of LPTN, returns complex conjugate tensors
        """
        c_conj = [np.conjugate(x) for x in self.tensors]
        return c_conj

    def __len__(self):
        """
        Provide number of sites in the LPTN
        """
        return self.num_sites

    def __getitem__(self, key):
        """You can access tensors in the LPTN using

        .. code-block::
            LPTN[0]
            >>> tensor for a site at position 0

        Parameters
        ----------
        key : int
            index (=site) of the LPTN you are interested in

        Return
        ------
        np.ndarray
            Tensor at position key in the LPTN.tensor array
        """
        return self.tensors[key]

    def __setitem__(self, key, value):
        """
        Modify a tensor in the LPTN by using a syntax corresponding
        to lists.

        .. code-block::
            tens = np.ones( (1, 2, 1) )
            LPTN[1] = tens

        Parameters
        ----------
        key : int
            index of the array
        value : np.array
            value of the new tensor

        Return
        ------
        None
        """
        if not isinstance(value, np.ndarray):
            raise TypeError("New tensor must be a numpy array, not {type(value)}")
        self.tensors[key] = value

        return None

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
        return self[idx]

    def norm(self):
        """
        Calculate the norm of the state, where the state is X of
        rho = X Xdagger.
        """
        if self.iso_center is None:
            self.install_gauge_center()

        tensor = self[self.iso_center[0]]
        norm = np.sum(np.real(tensor * np.conj(tensor)))

        return np.sqrt(norm)

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
        if keep_singvals:
            raise ValueError("keep_singvals not implemented for LPTN `site_canonize`")

        self.shift_gauge_center([idx, idx + 2])

    def scale(self, factor):
        """
        Multiply the tensor network state by a scalar factor.

        Parameters
        ----------
        factor : float
            Factor for multiplication of current tensor network state.
        """
        if self.iso_center is None:
            self.install_gauge_center()

        self[self.iso_center[0]] *= factor

    def print_tensors(self, how_many=None):
        """
        Prints the tensors in LPTN together with their shape

        Parameters
        ----------
        how_many : int, optional
            Only the first :py:name::`how_many` tensors are printed.
            If :py:name::`how_many=None`, all of the tensors are printed

        Return
        ------
        None
        """
        if how_many is None:
            how_many = len(self.tensors)
        if how_many > len(self.tensors) or how_many < 0:
            raise ValueError("Invalid number of tensors")

        for ii in range(0, how_many):
            print("site", ii, ":")
            print("Shape: ", self.tensors[ii].shape)
            print(self.tensors[ii], "\n")
        print("\n")

    def print_tensor_shapes(self, how_many=None):
        """
        Prints the shape of tensors in LPTN

        Parameters
        ----------
        how_many : int
            Only the shapes of the first <how_many> tensors
            are printed. If how_many=None, shapes of all of
            the tensors are printed

        Return
        ------
        None
        """
        if how_many is None:
            how_many = len(self.tensors)
        if how_many > len(self.tensors) or how_many < 0:
            raise ValueError("Invalid number of tensors")

        for ii in range(0, how_many):
            print("site", ii, ":")
            print("Shape: ", self.tensors[ii].shape)
        print("\n")

        return None

    def kronecker(self, other):
        """
        Concatenate LPTN tensors with other LPTN's
        tensors

        Parameters
        ----------
        other : LPTN
            LPTN to concatenate

        Return
        ------
        lptn_kron : LPTN
            kronecker product of the
            two LPTN's
        """

        if not isinstance(other, LPTN):
            raise TypeError(
                "Only two LPTN classes can be concatenated, not "
                f"{type(other)} and LPTN."
            )
        if self.tensors[-1].shape[3] != other.tensors[0].shape[0]:
            raise ValueError(
                "Given LPTN with boundary bond dimension "
                f"{other.tensors[0].shape[0]}, not compatible"
                " for performing Kronecker product with LPTN"
                " with boundary bond dimension "
                f"{self.tensors[-1].shape[3]}"
            )

        # concatenates the tensors from both LPTN's to one list
        tensor_list = self.tensors + other.tensors
        max_bond_dim = max(self.max_bond_dim, other.max_bond_dim)
        cut_ratio = min(self.cut_ratio, other.cut_ratio)
        conv_params = TNConvergenceParameters(
            max_bond_dimension=max_bond_dim, cut_ratio=cut_ratio
        )

        lptn_kron = LPTN.from_tensor_list(
            tensor_list=tensor_list, conv_params=conv_params
        )

        return lptn_kron

    def reduced_dm(self, sites, max_qubits=10):
        """
        Get a reduced density matrix of a given LPTN. The
        result is in a matrix form.

        Parameters
        ----------
        sites : list of int
            Specifies the sites for the reduced density
            matrix. The partial trace is performed over
            all of the other tensors.
            Currently, a reduced density matrix is implemented
            only for single and neighbour sites.
            The sites are counted from zero to num_sites-1.

        max_qubits : int, optional
            Maximal number of qubits a reduced density matrix
            can have. If the number of qubits is greater, it
            will throw an exception.
            If the local Hilbert space dimension is not 2, The
            number of qubits is calculated as np.log2(D),
            where D is a total Hilbert space dimension of
            reduced density matrix.
            Default to 10.

        Returns
        -------
        red_dm : 2D np.ndarray
            Reduced density matrix.
        """
        if self.iso_center is None:
            self.install_gauge_center()
            print(
                "Warning: passed an LPTN with no gauge center. The"
                " gauge center installed."
            )

        if not isinstance(sites, (np.ndarray, list)):
            raise TypeError(f"Input sites must be list of ints, not {type(sites)}.")

        if not all(isinstance(element, (int, np.int64, np.int32)) for element in sites):
            raise TypeError(
                "Input sites must be int or list of"
                f" ints. First element type: {type(sites[0])}."
            )

        if min(sites) < 0 or max(sites) > self.num_sites - 1:
            raise ValueError(
                "Invalid input for remaining sites. The"
                " site index must be between"
                f" [0,{self.num_sites-1}], not"
                f" [{min(sites)},{max(sites)}]"
            )

        if np.any(np.array(sites[:-1]) > np.array(sites[1:])):
            raise ValueError(
                "Remaining sites must be ordered from the"
                " smallest to the largest value."
            )

        if np.log2(self.local_dim ** len(sites)) > max_qubits:
            raise RuntimeError(
                "Cannot generate a density matrix of"
                f" {len(sites)} qubits. Maximal"
                " number of qubits a reduced density"
                f" matrix can have is set to {max_qubits}."
            )

        if len(sites) > 2:
            raise ValueError(
                "Partial trace for more than"
                " two remaining particles is not"
                " yet implemented."
            )

        # shift the gauge center to one of the sites remaining in
        # the reduced density matrix
        iso_index = self.iso_center[0]
        if iso_index < min(sites):
            self.shift_gauge_center([min(sites), min(sites) + 2])
        elif iso_index > max(sites):
            self.shift_gauge_center([max(sites), max(sites) + 2])

        # Since the gauge center of the LPTN is now among the sites
        # in the reduced density matrix, the other sites can simply be
        # ignored because they are unitary and will add into identity
        # when the partial trace is performed.
        # Therefore, the operation we need to perform is:
        # (suppose there are two sites left in the reduced dm)

        #     |   |
        #  ---O---O---               |   |            ||          |
        # |   |   |   |   --->       O===O    --->    O   --->    O
        #  ---O---O---               |   |            ||          |
        #     |   |

        # step:            [1]                  [2]         [3]

        if len(sites) > 1:
            # step [1]
            tens_left = np.tensordot(
                self[sites[0]], np.conj(self[sites[0]]), axes=[[0, 2], [0, 2]]
            )
            tens_right = np.tensordot(
                self[sites[1]], np.conj(self[sites[1]]), axes=[[2, 3], [2, 3]]
            )
            # step [2]
            dm_red = np.tensordot(tens_left, tens_right, axes=[[1, 3], [0, 2]])
            dm_red = np.transpose(dm_red, axes=[0, 2, 1, 3])
            # step [3]
            dm_red = np.reshape(
                dm_red,
                (dm_red.shape[0] * dm_red.shape[1], dm_red.shape[2] * dm_red.shape[3]),
            )

        # analog procedure with the one tensor, now only step [1] is needed
        else:
            dm_red = np.tensordot(
                self[sites[0]], np.conj(self[sites[0]]), axes=[[0, 2, 3], [0, 2, 3]]
            )

        return dm_red

    def get_rho_i(self, idx):
        """
        Calculate the reduced density matrix for a single site.

        Parameters
        ----------
        idx : integer
            Calculate the reduced density matrix of site ``idx``.
            Recall python indices start at zero.

        Returns
        -------
        2D np.ndarray :
            Reduced density matrix.
        """
        return self.reduced_dm(sites=[idx])

    def get_rho_ij(self, idx):
        """
        Calculate the reduced density matrix for two
        neighbour sites.

        Parameters
        ----------
        idx : integer
            Calculate the reduced density matrix of sites ``idx``
            and ``idx``+1.
            Recall python indices start at zero.

        Returns
        -------
        2D np.ndarray :
            Reduced density matrix.
        """
        return self.reduced_dm(sites=[idx, idx + 1])

    def install_gauge_center(self):
        """
        Install a gauge center to the rightmost site
        of the LPTN.

        Returns
        -------
        None
        """

        if self.iso_center is not None:
            raise ValueError(
                f"LPTN already has a gauge center between the sites {self.iso_center}."
            )

        # How to install a gauge center:

        #   |  |  |                                        |     |  |
        # --O--O--O--  --(QR decompose the first one)->  --Q--R--O--O--
        #   |  |  |                                        |     |  |

        #                                              |  |  |
        # --(contract R with tensor on the right)->  --Q--O--O--
        #           (Q is now unitary)                 |  |  |

        # - repeat the same for the next tensor, and so on until all
        #   the tensors except the last one are unitary.

        for ii in range(0, self.num_sites - 1):
            work = np.reshape(
                self[ii],
                (
                    self[ii].shape[0] * self[ii].shape[1] * self[ii].shape[2],
                    self[ii].shape[3],
                ),
            )
            q_mat, r_mat = nla.qr(work)
            self[ii + 1] = np.tensordot(r_mat, self[ii + 1], axes=[[1], [0]])
            self[ii] = np.reshape(
                q_mat,
                (
                    self[ii].shape[0],
                    self[ii].shape[1],
                    self[ii].shape[2],
                    q_mat.shape[1],
                ),
            )

        self.iso_center = [self.num_sites - 1, self.num_sites + 1]
        return None

    def shift_gauge_center(self, ind_final):
        """
        Shift a gauge center of the LPTN.

        ind_final : list or np.array of two ints
            The new gauge center will be installed between
            these two sites (when considering the non-python
            index starting at 1).

        Returns
        -------
        None
        """
        # checks of input
        if isinstance(ind_final, (np.ndarray, list)):
            if not all(
                isinstance(element, (int, np.int64, np.int32)) for element in ind_final
            ) or (len(ind_final) != 2):
                raise TypeError(
                    "iso_center must be None or list of two"
                    " ints, not list of "
                    f"{len(ind_final)}"
                    f" {type(ind_final[0])}."
                )

        elif ind_final is not None:
            raise TypeError(
                f"iso_center must be None or list of two ints, not {type(ind_final)}."
            )

        ind_init = self.iso_center
        if ind_init is None:
            raise ValueError(
                "The input LPTN must already have the gauge center installed."
            )

        # How to shift? Suppose X is the gauge center and we want to shift it to
        # one place to the right.

        #   |  |  |                                     |  |     |
        # --O--X--O--  --(QR decompose middle one)->  --O--Q--R--O--
        #   |  |  |                                     |  |     |

        #                                              |  |  |
        # --(contract R with tensor on the right)->  --O--O--X--  :)
        #           (rename Q --> O)                   |  |  |

        # Remark: when shifting gauge center to the left, we must ensure
        # that the unitary matrix (Q) is on the right, and the upper
        # triangular matrix (R) is on the left.

        # calculate the direction in which the QR decompositions must be
        # done (direction = -1 means we shift gauge center to the left,
        # and direction = 1 means we shift gauge center to the right)
        center_init = ind_init[0]
        center_final = ind_final[0]
        if center_init == center_final:
            print(
                f"Input gauge center position at {center_final} corresponds "
                "to the current one. LPTN not changed."
            )
            return None
        direction = np.sign(center_final - center_init)

        # two separate cases for shifting to the left and to the right

        if direction > 0:
            for ii in range(center_init, center_final):
                work = np.reshape(
                    self[ii],
                    (
                        self[ii].shape[0] * self[ii].shape[1] * self[ii].shape[2],
                        self[ii].shape[3],
                    ),
                )
                q_mat, r_mat = nla.qr(work)
                self[ii + 1] = np.tensordot(r_mat, self[ii + 1], axes=[[1], [0]])
                self[ii] = np.reshape(
                    q_mat,
                    (
                        self[ii].shape[0],
                        self[ii].shape[1],
                        self[ii].shape[2],
                        q_mat.shape[1],
                    ),
                )

        else:
            for ii in range(center_init, center_final, -1):
                work = np.reshape(
                    self[ii],
                    (
                        self[ii].shape[0],
                        self[ii].shape[1] * self[ii].shape[2] * self[ii].shape[3],
                    ),
                )
                work = np.transpose(work, axes=[1, 0])
                q_mat, r_mat = nla.qr(work)
                q_mat = np.transpose(q_mat, axes=[1, 0])
                r_mat = np.transpose(r_mat, axes=[1, 0])
                self[ii - 1] = np.tensordot(self[ii - 1], r_mat, axes=[[3], [0]])
                self[ii] = np.reshape(
                    q_mat,
                    (
                        q_mat.shape[0],
                        self[ii].shape[1],
                        self[ii].shape[2],
                        self[ii].shape[3],
                    ),
                )

        self.iso_center = [center_final, center_final + 2]
        return None

    @classmethod
    def from_tensor_list(cls, tensor_list, conv_params=None, iso_center=None):
        """
        Initialize the LPTN tensors using a list of correctly
        shaped tensors

        Parameters
        ----------
        tensor_list : list of ndarrays
            List of tensors for initializing the LPTN
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Input for handling convergence parameters.
            In particular, in the LPTN simulator we
            are interested in:
            - the maximum bond dimension (`max_bond_dimension`)
            - the cut ratio (`cut_ratio`) after which the
            singular values in SVD are neglected, all
            singular values such that :math:`\\lambda` /
            :math:`\\lambda_max` <= :math:`\\epsilon` are truncated
        iso_center : None or list of int, optional
            Isometry center is between the two sites
            specified in a list. If the LPTN has no
            isometry center, iso_center = None.
            Default is None

        Return
        ------
        obj : :py:class:`LPTN`
            The LPTN class composed of the given tensors
        --------------------------------------------------------------------
        """
        local_dim = tensor_list[0].shape[1]
        max_bond_dim = deepcopy(local_dim)
        for tens in enumerate(tensor_list):
            t_shape = tens[1].shape
            max_bond_dim = max(max_bond_dim, t_shape[0])

        if conv_params is None:
            conv_params = TNConvergenceParameters(max_bond_dimension=int(max_bond_dim))
        obj = cls(len(tensor_list), conv_params=conv_params, local_dim=local_dim)
        obj.tensors = tensor_list
        obj.iso_center = iso_center

        return obj

    @classmethod
    def from_tensor_list_mps(cls, tensor_list, conv_params=None, iso_center=None):
        """
        Initialize the LPTN tensors using a list of MPS
        shaped tensors. A dummy leg is added and then the function
        from_tensor_list is called.

        Parameters
        ----------
        tensor_list : list of ndarrays
            List of tensors for initializing the LPTN
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Input for handling convergence parameters.
            In particular, in the LPTN simulator we
            are interested in:
            - the maximum bond dimension (`max_bond_dimension`)
            - the cut ratio (`cut_ratio`) after which the
            singular values in SVD are neglected, all
            singular values such that :math:`\\lambda` /
            :math:`\\lambda_max` <= :math:`\\epsilon` are truncated
        iso_center : None or list of int, optional
            Isometry center is between the two sites
            specified in a list. If the LPTN has no
            isometry center, iso_center = None.
            Default is None

        Return
        ------
        obj : :py:class:`LPTN`
            The LPTN class composed of the given tensors
        --------------------------------------------------------------------
        """
        if iso_center is not None:
            if len(iso_center) != 2:
                raise ValueError(
                    "Iso-center for LPTN has to be of length two (f90-index)."
                )

        # reshape to rank 4
        new_tensor_list = []
        for tens in tensor_list:
            new_tensor_list.append(
                tens.reshape((tens.shape[0], tens.shape[1], 1, tens.shape[2]))
            )

        obj = cls.from_tensor_list(
            tensor_list=new_tensor_list, conv_params=conv_params, iso_center=iso_center
        )
        return obj

    def to_tensor_list_mps(self):
        """
        Return the tensor list representation of the LPTN
        as MPS. If the upper link has dimension one, the tensors
        are reshaped to rank 3.

        Return
        ------
        list
            List of tensors of the LPTN as MPS.
        """
        # check if link of complex conjugate has dimension 1
        for tens in self.tensors:
            if tens.shape[2] != 1:
                raise Exception(
                    "Tensor with upper leg dimension other than 1 found in the list."
                )

        # reshape to rank 3
        new_tensors = []
        for tens in self.tensors:
            new_tensors.append(
                tens.reshape((tens.shape[0], tens.shape[1], tens.shape[3]))
            )

        return new_tensors

    @classmethod
    def dm_to_lptn(cls, rho, n_sites, dim, conv_params, prob=False):
        """
        For a given density matrix in matrix form returns LPTN form

        Parameters
        ----------
        rho : ndarray
            Density matrix
        n_sites : int
            Number of sites
        dim : int
            Local Hilbert space dimension
        conv_params : :py:class:`TNConvergenceParameters`
            Input for handling convergence parameters.
            In particular, in the LPTN simulator we
            are interested in:
            - the maximum bond dimension (max_bond_dimension)
            - the cut ratio (cut_ratio) after which the
            singular values in SVD are neglected, all
            singular values such that
            :math:`\\lambda` /:math:`\\lambda_max`
            <= :math:`\\epsilon` are truncated
        prob : Boolean, optional
            If True, returns eigenvalues of initial eigenvalue
            decomposition. If everything is correct, should
            correspond to mixed state probabilities

        Return
        ------
        rho_lptn : :py:class::`LPTN`
            Density matrix in LPTN form
        (if prob==True) :
        val : 1D np.ndarray
            Eigenvalues of initial EVD
            = mixed state probabilities
        """
        if not isinstance(n_sites, int):
            raise TypeError(
                "Input number of sites must be an integer, not {type(n_sites)}"
            )
        if not isinstance(dim, int):
            raise TypeError(
                "Input local Hilbert space dimension must be an integer, "
                "not {type(dim)}"
            )

        rho_lptn = cls(n_sites, local_dim=dim, conv_params=conv_params)
        rho_lp = []

        """
        --O--   --[EVD, no truncating]--> --O--o--O--
        """
        val, vec = nla.eigh(rho)
        val, vec = val[::-1], vec[:, ::-1]
        """
        absorb the eigenvalues,    | --> dimension dim**n_sites
        square root to each side,  O
        and take only one side:    | --> physical legs, dimension dim**n_sites
        """
        work = vec * np.sqrt(val)
        bond_dim = 1
        for ii in range(0, n_sites - 1):
            """
                           dim  dim**(n_sites-1)
            |                 ||
            O  --[unfuse]-->  O   --[fuse upper and lower legs]-->
            |                 ||

            ==O==  --[SVD, truncating]-->  ==O-o-O==

                           | |
            --[unfuse]-->  O-O           ---iterate
                           | |
                        dim   dim**(n_sites-1)
            """
            work = np.reshape(
                work,
                (
                    bond_dim,
                    dim,
                    dim ** (n_sites - 1 - ii),
                    dim,
                    dim ** (n_sites - 1 - ii),
                ),
            )
            tens_left, work, _, _ = rho_lptn.tSVD(
                work, [0, 1, 3], [2, 4], contract_singvals="R", conv_params=conv_params
            )
            rho_lp.append(tens_left)
            bond_dim = deepcopy(work.shape[0])
        work = np.reshape(work, (work.shape[0], dim, dim, 1))
        rho_lp.append(work)

        rho_lptn.tensors = rho_lp

        if prob:
            return rho_lptn, val

        return rho_lptn

    @classmethod
    def read(cls, filename, cmplx=True, order="F"):
        """
        Read the LPTN written by FORTRAN in a formatted way on file.
        Reads in column-major order but the output is in row-major.

        Parameters
        ----------
        filename: str
            PATH to the file
        cmplx: bool, optional
            If True the LPTN is complex, real otherwise. Default to True
        order: str, optional
            If 'F' the tensor is transformed from column-major to row-major, if 'C'
            it is left as read.

        Returns
        -------
        obj: py:class:`LPTN`
            LPTN class read from file
        """
        tensors = []
        with open(filename, "r") as fh:
            # read real/complex datatype stored in file
            _ = fh.readline()

            # total number of sites
            num_sites = int(fh.readline())

            # isometry
            iso = fh.readline().split()
            iso_center = [int(iso[0]), int(iso[1])]

            # ds, bc, sr N-N and sr N-N+1
            for _ in range(num_sites):
                _ = fh.readline()
            _ = fh.readline()

            # reading tensors
            for _ in range(num_sites):
                tens = read_tensor(fh, cmplx=cmplx, order=order)
                # skip empty lines
                if not fh.readline():
                    continue
                tensors.append(tens)

        obj = cls.from_tensor_list(tensors, iso_center=iso_center)

        return obj

    def write(self, filename, cmplx=True):
        """
        Write an LPTN in python format into a FORTRAN format, i.e.
        transforms row-major into column-major

        Parameters
        ----------
        filename: str
            PATH to the file
        cmplx: bool, optional
            If True the MPS is complex, real otherwise. Default to True

        Returns
        -------
        obj: py:class:`LPTN`
            LPTN class read from file
        """
        with open(filename, "w") as fh:
            # write real/complex
            # currently it is always set to 'Z'!
            fh.write("%c\n" % ("Z"))

            # write total number of sites
            fh.write("%d\n" % (len(self.tensors)))

            # isometry
            fh.write("%d %d\n" % (self.iso_center[0], self.iso_center[1]))

            # local dim, kappa, bond dimension to the left for each site (this
            # information refers to the maximum allowed for kappa and the bond
            # dimension, not to the current one. Usually, this should be overwritten
            # or set from the simulations reading the LPTN, but set it to sensbile
            # value derived from the convergence parameters stored)
            for tens in self.tensors:
                fh.write(
                    "%d %d %d\n" % (tens.shape[1], self.max_bond_dim, self.max_bond_dim)
                )

            # bond dimension to the right for the last site
            fh.write("%d\n" % (self.tensors[-1].shape[3]))

            for tens in self.tensors:
                write_tensor(tens, fh, cmplx=cmplx)

        return None

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
        raise NotImplementedError("No support projective measurements for LPTN.")

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
        raise NotImplementedError("No support projective measurements for LPTN.")
