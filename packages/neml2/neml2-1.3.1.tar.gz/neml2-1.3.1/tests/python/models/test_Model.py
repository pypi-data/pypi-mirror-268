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
from pathlib import Path
import torch
import neml2
from neml2.tensors import BatchTensor, LabeledVector
from neml2.tensors import LabeledAxisAccessor as AA


def test_get_model():
    pwd = Path(__file__).parent
    neml2.load_input(pwd / "test_Model.i")
    neml2.get_model("model")


def test_input_axis():
    pwd = Path(__file__).parent
    model = neml2.load_model(pwd / "test_Model.i", "model")
    input_axis = model.input_axis()
    assert input_axis.storage_size() == 8
    assert input_axis.has_subaxis(AA("forces"))
    assert input_axis.has_variable(AA("forces", "t"))
    assert input_axis.has_subaxis(AA("old_forces"))
    assert input_axis.has_variable(AA("old_forces", "t"))
    assert input_axis.has_subaxis(AA("old_state"))
    assert input_axis.has_variable(AA("old_state", "foo"))
    assert input_axis.has_variable(AA("old_state", "bar"))
    assert input_axis.has_subaxis(AA("state"))
    assert input_axis.has_variable(AA("state", "foo"))
    assert input_axis.has_variable(AA("state", "foo_rate"))
    assert input_axis.has_variable(AA("state", "bar"))
    assert input_axis.has_variable(AA("state", "bar_rate"))


def test_output_axis():
    pwd = Path(__file__).parent
    model = neml2.load_model(pwd / "test_Model.i", "model")
    output_axis = model.output_axis()
    assert output_axis.storage_size() == 1
    assert output_axis.has_variable(AA("residual", "foo_bar"))


def test_value():
    pwd = Path(__file__).parent
    model = neml2.load_model(pwd / "test_Model.i", "model")

    a = torch.linspace(0, 1, 8).expand(5, 2, 8)
    x = BatchTensor(a, 2)
    model.reinit(x.batch.shape)
    x = LabeledVector(x, [model.input_axis()])

    y = model.value(x)
    assert y.tensor().batch.shape == (5, 2)
    assert y.tensor().base.shape == (1,)
    assert torch.allclose(
        y.tensor().tensor(), torch.tensor(0.9591836144729537, dtype=torch.float64)
    )


def test_value_and_dvalue():
    pwd = Path(__file__).parent
    model = neml2.load_model(pwd / "test_Model.i", "model")

    a = torch.linspace(0, 1, 8).expand(5, 2, 8)
    x = BatchTensor(a, 2)
    model.reinit(x.batch.shape, 1)
    x = LabeledVector(x, [model.input_axis()])

    y, dy_dx = model.value_and_dvalue(x)
    assert y.tensor().batch.shape == (5, 2)
    assert y.tensor().base.shape == (1,)
    assert torch.allclose(
        y.tensor().tensor(), torch.tensor(0.9591836144729537, dtype=torch.float64)
    )
    assert torch.allclose(
        dy_dx.tensor().tensor(),
        torch.tensor(
            [
                -1.7142857313156128,
                1.7142857313156128,
                -1.0,
                -1.0,
                1.0,
                0.1428571492433548,
                1.0,
                0.1428571492433548,
            ],
            dtype=torch.float64,
        ),
    )
