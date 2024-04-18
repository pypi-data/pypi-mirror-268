// Copyright 2023, UChicago Argonne, LLC
// All Rights Reserved
// Software Name: NEML2 -- the New Engineering material Model Library, version 2
// By: Argonne National Laboratory
// OPEN SOURCE LICENSE (MIT)
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

#include <pybind11/pybind11.h>

#include "python/neml2/misc/types.h"
#include "neml2/models/Model.h"

namespace py = pybind11;
using namespace neml2;

void
def_Model(py::module_ & m)
{
  py::class_<Model, std::shared_ptr<Model>>(m, "Model")
      .def("reinit",
           py::overload_cast<TorchShapeRef, int, const torch::Device &, const torch::Dtype &>(
               &Model::reinit),
           py::arg("batch_shape"),
           py::arg("deriv_order") = 0,
           py::arg("device") = torch::Device(torch::kCPU),
           py::arg("dtype") = torch::Dtype(NEML2_DTYPE))
      .def(
          "input_axis",
          [](const Model & self) { return &self.input_axis(); },
          py::return_value_policy::reference)
      .def(
          "output_axis",
          [](const Model & self) { return &self.output_axis(); },
          py::return_value_policy::reference)
      .def("value", [](Model & self, const LabeledVector & x) { return self.value(x); })
      .def("value_and_dvalue", py::overload_cast<const LabeledVector &>(&Model::value_and_dvalue))
      .def(
          "named_parameters",
          [](Model & self) { return &self.named_parameters(); },
          py::return_value_policy::reference);
}
