#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ####################################################################################
# Copyright (c) 2016, Francesco De Carlo                                             #
# All rights reserved.                                                               #
#                                                                                    #
# Redistribution and use in source and binary forms, with or without                 #
# modification, are permitted provided that the following conditions are met:        #
#                                                                                    #
# * Redistributions of source code must retain the above copyright notice, this      #
#   list of conditions and the following disclaimer.                                 #
#                                                                                    #
# * Redistributions in binary form must reproduce the above copyright notice,        #
#   this list of conditions and the following disclaimer in the documentation        #
#   and/or other materials provided with the distribution.                           #
#                                                                                    #
# * Neither the name of project nor the names of its                                 #
#   contributors may be used to endorse or promote products derived from             #
#   this software without specific prior written permission.                         #
#                                                                                    #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"        #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE          #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE     #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE       #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL         #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR         #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER         #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,      #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE      #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.               #
# ####################################################################################

"""
Module for describing .....
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy

__authors__ = "First Name Last Name"
__copyright__ = "Copyright (c) 2016, Affiliation"
__version__ = "0.1.0"
__docformat__ = "restructuredtext en"
__all__ = ['function_01',
           'function_02']

def function_01(parameter_01, parameter_02, parameter_03):
    """
    This is an example of a module level function.

    Ref.:
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy

    Function parameters should be documented in the ``Parameters`` section.
    The name of each parameter is required. The type and description of each
    parameter is optional, but should be included if not obvious.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name : type
            description

            The description may span multiple lines. Following lines
            should be indented to match the first line of the description.
            The ": type" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Parameters
    ----------
    parameter_01 : int
        The first parameter.
    parameter_02 : :obj:`str`, optional
        The second parameter.
    parameter_03 : :obj:`str`, optional
        The second parameter.
    *args
        Variable length argument list.
    **kwargs
        Arbitrary keyword arguments.

    Returns
    -------
    bool
        True if successful, False otherwise.

        The return type is not optional. The ``Returns`` section may span
        multiple lines and paragraphs. Following lines should be indented to
        match the first line of the description.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises
    ------
    AttributeError
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError
        If `param2` is equal to `param1`.



    Examples
    --------
    Examples should be written in doctest format, and should illustrate how
    to use the function.

    >>> print([i for i in example_generator(4)])
    [0, 1, 2, 3]

    More Reference:

    http://www.sphinx-doc.org/en/stable/domains.html#python-roles


    More examples:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    .. warning:: Warning text.

    .. note:: Note text.
    
    .. image:: img/plot_profile_animation.gif

    """

    return_01 = parameter_01 + parameter_02 + parameter_03
    
    return return_01


def function_02(parameter_01, parameter_02, parameter_03):
    """
    Function description.

    Parameters
    ----------
    parameter_01 : type
        Description.

    parameter_02 : type
        Description.

    parameter_03 : type
        Description.

    Returns
    -------
    return_01
        Description.
    """

    return_01 = parameter_01 + parameter_02 + parameter_03
    
    return return_01

