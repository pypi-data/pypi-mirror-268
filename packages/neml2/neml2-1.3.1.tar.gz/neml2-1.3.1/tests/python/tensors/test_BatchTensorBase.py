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
from functools import reduce

# fixtures
from common import *


from neml2.tensors import BatchTensor


@pytest.fixture
def base_shape():
    """
    Base shape for all sample BatchTensors
    """
    return (7, 1, 2, 1)


@pytest.fixture
def _A(base_shape, tensor_options):
    """
    Sample BatchTensor A, unbatched
    """
    storage = reduce((lambda x, y: x * y), base_shape, 1)
    sample = torch.arange(storage, **tensor_options).reshape(base_shape)
    sample = (sample - torch.mean(sample) + 1.1) / storage
    return BatchTensor(sample, 0)


@pytest.fixture
def _B(base_shape, tensor_options):
    """
    Sample BatchTensor B, batched and is (non-trivially) broadcastable with sample C
    """
    batch_shape = (5, 3, 1)
    shape = batch_shape + base_shape
    storage = reduce((lambda x, y: x * y), shape, 1)
    sample = torch.arange(storage, **tensor_options).reshape(shape)
    sample = (sample - torch.mean(sample) - 0.5) / storage
    return BatchTensor(sample, 3)


@pytest.fixture
def _C(base_shape, tensor_options):
    """
    Sample BatchTensor C, batched and is (non-trivially) broadcastable with sample B
    """
    batch_shape = (2, 5, 1, 2)
    shape = batch_shape + base_shape
    storage = reduce((lambda x, y: x * y), shape, 1)
    sample = torch.arange(storage, **tensor_options).reshape(shape)
    sample = (sample - torch.mean(sample) + 0.3) / storage
    return BatchTensor(sample, 4)


@pytest.fixture(params=["_A", "_B", "_C"], ids=["A", "B", "C"])
def sample(request, tensor_options):
    return request.getfixturevalue(request.param)


def test_basic(sample, base_shape, tensor_options):
    # Default c'tor
    A = BatchTensor()
    assert not A.defined()

    # From a torch.Tensor and a batch dim
    A0 = torch.ones(3, 4, 5, 6, **tensor_options)
    A = BatchTensor(A0, 2)
    assert torch.allclose(A.tensor(), A0)

    # From another BatchTensor
    A = BatchTensor(sample)
    assert torch.allclose(A.tensor(), sample.tensor())

    # Basic properties
    assert sample.batched() == (sample.dim() > len(base_shape))


def test_batch_view(sample, base_shape):
    sample0 = sample.clone()
    Z = sample.tensor()

    # dimension
    batch_dim = sample.batch.dim()
    assert batch_dim == sample.dim() - len(base_shape)

    # shape
    batch_shape = sample.batch.shape
    assert batch_shape == sample.shape[: sample.batch.dim()]

    # __getitem__
    assert torch.allclose(sample.batch[None].tensor(), Z[None])
    assert torch.allclose(sample.batch[...].tensor(), Z[...])
    if sample.batched():
        assert torch.allclose(sample.batch[0].tensor(), Z[0])
        assert torch.allclose(sample.batch[0:5:2].tensor(), Z[0:5:2])
        assert torch.allclose(sample.batch[:, 0].tensor(), Z[:, 0])

    # __setitem__
    sample0.batch[...] = Z + 1.3
    assert torch.allclose(sample0.tensor(), Z + 1.3)

    # expand
    B = sample.batch.expand((10, 2) + batch_shape)
    assert torch.allclose(B.tensor(), Z.expand((10, 2) + Z.shape))

    # unsqueeze
    B = sample.batch.unsqueeze(0)
    assert torch.allclose(B.tensor(), Z.unsqueeze(0))
    B = sample.batch.unsqueeze(-1)
    assert torch.allclose(B.tensor(), Z.unsqueeze(batch_dim))

    # transpose
    if batch_dim >= 2:
        B = sample.batch.transpose(0, 1)
        assert torch.allclose(B.tensor(), torch.transpose(Z, 0, 1))


def test_base_view(sample, base_shape):
    sample0 = sample.clone()
    Z = sample.tensor()
    batch_dim = sample.batch.dim()

    # dimension
    base_dim = sample.base.dim()
    assert base_dim == len(base_shape)

    # shape
    assert sample.base.shape == base_shape

    # __getitem__
    I = (slice(None),) * batch_dim
    assert torch.allclose(sample.base[None].tensor(), Z[I + (None,)])
    assert torch.allclose(sample.base[...].tensor(), Z[I + (...,)])
    if sample.batched():
        assert torch.allclose(sample.base[0].tensor(), Z[I + (0,)])
        assert torch.allclose(sample.base[0:5:2].tensor(), Z[I + (slice(0, 5, 2),)])
        assert torch.allclose(sample.base[:, 0].tensor(), Z[I + (slice(None), 0)])

    # __setitem__
    sample0.base[...] = Z + 1.3
    assert torch.allclose(sample0.tensor(), Z + 1.3)

    # expand
    B = sample.base.expand((7, 2, 2, 3))
    assert torch.allclose(B.tensor(), Z.expand(*((-1,) * batch_dim) + (7, 2, 2, 3)))

    # unsqueeze
    B = sample.base.unsqueeze(0)
    assert torch.allclose(B.tensor(), Z.unsqueeze(batch_dim))
    B = sample.base.unsqueeze(-1)
    assert torch.allclose(B.tensor(), Z.unsqueeze(-1))

    # transpose
    B = sample.base.transpose(0, 1)
    assert torch.allclose(B.tensor(), torch.transpose(Z, batch_dim, batch_dim + 1))


def test_binary_ops(_A, _B, _C):
    # add
    assert_unary_op(lambda x: x + 0.5, _A)
    assert_unary_op(lambda x: x + 0.5, _B)
    assert_unary_op(lambda x: 0.5 + x, _A)
    assert_unary_op(lambda x: 0.5 + x, _B)
    assert_binary_op(lambda x, y: x + y, _A, _B)
    assert_binary_op(lambda x, y: x + y, _B, _C)
    # sub
    assert_unary_op(lambda x: x - 0.5, _A)
    assert_unary_op(lambda x: x - 0.5, _B)
    assert_unary_op(lambda x: 0.5 - x, _A)
    assert_unary_op(lambda x: 0.5 - x, _B)
    assert_binary_op(lambda x, y: x - y, _A, _B)
    assert_binary_op(lambda x, y: x - y, _B, _C)
    # mul
    assert_unary_op(lambda x: x * 0.5, _A)
    assert_unary_op(lambda x: x * 0.5, _B)
    assert_unary_op(lambda x: 0.5 * x, _A)
    assert_unary_op(lambda x: 0.5 * x, _B)
    # div
    assert_unary_op(lambda x: x / 0.5, _A)
    assert_unary_op(lambda x: x / 0.5, _B)
    assert_unary_op(lambda x: 0.5 / x, _A)
    assert_unary_op(lambda x: 0.5 / x, _B)
    assert_binary_op(lambda x, y: x / y, _A, _B)
    assert_binary_op(lambda x, y: x / y, _B, _C)
    # pow
    assert_unary_op(lambda x: x**0.5, _A)
    assert_unary_op(lambda x: x**0.5, _B)
    assert_unary_op(lambda x: 0.5**x, _A)
    assert_unary_op(lambda x: 0.5**x, _B)
    assert_binary_op(lambda x, y: x**y, _A, _B)
    assert_binary_op(lambda x, y: x**y, _B, _C)


def test_unary_ops(sample):
    # neg
    assert_unary_op(lambda x: -x, sample)


def test_named_ctors(_A, _B, _C, tensor_options):
    # empty_like
    A = BatchTensor.empty_like(_A)
    assert A.batch.dim() == _A.batch.dim()
    B = BatchTensor.empty_like(_B)
    assert B.batch.dim() == _B.batch.dim()

    # zeros_like
    A = BatchTensor.zeros_like(_A)
    assert A.batch.dim() == _A.batch.dim()
    assert torch.allclose(A.tensor(), torch.zeros_like(_A.tensor()))
    B = BatchTensor.zeros_like(_B)
    assert B.batch.dim() == _B.batch.dim()
    assert torch.allclose(B.tensor(), torch.zeros_like(_B.tensor()))

    # ones_like
    A = BatchTensor.ones_like(_A)
    assert A.batch.dim() == _A.batch.dim()
    assert torch.allclose(A.tensor(), torch.ones_like(_A.tensor()))
    B = BatchTensor.ones_like(_B)
    assert B.batch.dim() == _B.batch.dim()
    assert torch.allclose(B.tensor(), torch.ones_like(_B.tensor()))

    # full_like
    A = BatchTensor.full_like(_A, 1.1)
    assert A.batch.dim() == _A.batch.dim()
    assert torch.allclose(A.tensor(), torch.full_like(_A.tensor(), 1.1))
    B = BatchTensor.full_like(_B, 2.3)
    assert B.batch.dim() == _B.batch.dim()
    assert torch.allclose(B.tensor(), torch.full_like(_B.tensor(), 2.3))

    # linspace
    A = BatchTensor.linspace(_A, _B, 100)
    assert A.batch.dim() == 4
    B = BatchTensor.linspace(_B, _C, 100)
    assert B.batch.dim() == 5

    # logspace
    A = BatchTensor.logspace(_A, _B, 100)
    assert A.batch.dim() == 4
    B = BatchTensor.logspace(_B, _C, 100)
    assert B.batch.dim() == 5
