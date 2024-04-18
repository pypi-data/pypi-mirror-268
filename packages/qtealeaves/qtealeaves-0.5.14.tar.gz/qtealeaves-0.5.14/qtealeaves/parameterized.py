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
The tooling to have parameterized models and instances.
"""

__all__ = ["_ParameterizedClass"]


class _ParameterizedClass:
    """
    Abstract base class for any other class which needs to evaluate
    parameterization.
    """

    def eval_numeric_param(self, elem, params):
        """
        Evaluate a numeric parameter which might be defined via the
        parameter dictionary.

        **Arguments**

        elem : callable, string, or int/float
            Defines the parameter either via a function which return
            the value, a string being an entry in the parameter
            dictionary, or directly as the numeric value.

        params : dict
            The parameter dictionary, which will be passed to callables
            and used to evaluate string parameters.
        """
        if isinstance(elem, list):
            return [self.eval_numeric_param(subelem, params) for subelem in elem]

        if hasattr(elem, "__call__"):
            val = elem(params)
        elif isinstance(elem, str):
            val = params[elem]
        else:
            val = elem

        return val

    @staticmethod
    def eval_str_param(elem, params):
        """
        Evaluate a string parameter.

        **Arguments**

        elem : callable, string, or int/float
            Defines the parameter either via a function which return
            the value, or directly as the numeric value.

        params : dict
            The parameter dictionary, which will be passed to callables.
        """
        if hasattr(elem, "__call__"):
            val = elem(params)
        elif elem in params:
            val = params[elem]
        else:
            val = elem

        return val

    @staticmethod
    def eval_str_param_default(elem, params, default):
        """
        Evaluate a string parameter and allow to set default. It
        sets the default as soon as elem is not callable.

        **Arguments**

        elem : callable, ...
            Defines the parameter via a callable. Any other variable
            will be overwritten by the default.

        params : dict
            The parameter dictionary passed to the callable.

        default : str
            The default value if elem is not callable.
        """
        if hasattr(elem, "__call__"):
            val = elem(params)
        else:
            val = default

        return val
