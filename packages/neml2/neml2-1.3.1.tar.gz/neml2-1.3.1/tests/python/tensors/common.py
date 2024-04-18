# Copyright 2023, UChicago Argonne, LLC
# All Rights Reserved
# Software Name: NEML2 -- the New Engineering material Model Library, version 2
# By: Argonne National Laboratory
# OPEN SOURCE LICENSE (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import pytest
import torch
from neml2.tensors import *


def _stringify_fixture(v):
    return str(v)


@pytest.fixture(params=[torch.float64], ids=_stringify_fixture)
def dtype(request):
    """dtype being tested"""
    return request.param


@pytest.fixture(params=["cpu", "cuda:0"], ids=_stringify_fixture)
def device(request):
    """
    device being tested

    CUDA is skipped if not available
    """
    if request.param == "cuda:0" and not torch.cuda.is_available():
        pytest.skip("CUDA not available")
    return torch.device(request.param)


@pytest.fixture(params=[False], ids=["no grad"])
def requires_grad(request):
    """
    requires_grad
    """
    return request.param


@pytest.fixture
def tensor_options(dtype, device, requires_grad):
    """tensor options being tested"""
    return {"dtype": dtype, "device": device, "requires_grad": requires_grad}


def assert_binary_op(func, x, y):
    assert torch.allclose(
        func(x, y).tensor(), func(x.tensor(), y.tensor()), equal_nan=True
    )


def assert_unary_op(func, x):
    assert torch.allclose(func(x).tensor(), func(x.tensor()), equal_nan=True)
