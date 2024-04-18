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

#include "J2FlowDirection.h"
#include "neml2/tensors/SSR4.h"

namespace neml2
{
register_NEML2_object(J2FlowDirection);

OptionSet
J2FlowDirection::expected_options()
{
  auto options = Model::expected_options();
  options.set<VariableName>("mandel_stress") = VariableName("state", "M");
  options.set<VariableName>("flow_direction") = VariableName("state", "NM");
  return options;
}

J2FlowDirection::J2FlowDirection(const OptionSet & options)
  : Model(options),
    _M(declare_input_variable<SR2>("mandel_stress")),
    _N(declare_output_variable<SR2>("flow_direction"))
{
}

void
J2FlowDirection::set_value(bool out, bool dout_din, bool d2out_din2)
{
  neml_assert_dbg(!d2out_din2, "Second derivatives not implemented");

  auto S = SR2(_M).dev();
  auto sn = S.norm(NEML2_EPS);

  if (out)
  {
    _N = S / sn;
  }

  if (dout_din)
  {
    _N.d(_M) = SSR4::identity_dev(options()) / sn - S.outer(S) / sn / sn / sn;
  }
}
} // namespace neml2
