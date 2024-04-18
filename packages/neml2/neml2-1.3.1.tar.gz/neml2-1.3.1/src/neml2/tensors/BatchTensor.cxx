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

#include "neml2/tensors/BatchTensor.h"

namespace neml2
{
BatchTensor
BatchTensor::empty(const TorchShapeRef & base_shape, const torch::TensorOptions & options)
{
  return BatchTensor(torch::empty(base_shape, options), 0);
}

BatchTensor
BatchTensor::empty(const TorchShapeRef & batch_shape,
                   const TorchShapeRef & base_shape,
                   const torch::TensorOptions & options)
{
  return BatchTensor(torch::empty(utils::add_shapes(batch_shape, base_shape), options),
                     batch_shape.size());
}

BatchTensor
BatchTensor::zeros(const TorchShapeRef & base_shape, const torch::TensorOptions & options)
{
  return BatchTensor(torch::zeros(base_shape, options), 0);
}

BatchTensor
BatchTensor::zeros(const TorchShapeRef & batch_shape,
                   const TorchShapeRef & base_shape,
                   const torch::TensorOptions & options)
{
  return BatchTensor(torch::zeros(utils::add_shapes(batch_shape, base_shape), options),
                     batch_shape.size());
}

BatchTensor
BatchTensor::ones(const TorchShapeRef & base_shape, const torch::TensorOptions & options)
{
  return BatchTensor(torch::ones(base_shape, options), 0);
}

BatchTensor
BatchTensor::ones(const TorchShapeRef & batch_shape,
                  const TorchShapeRef & base_shape,
                  const torch::TensorOptions & options)
{
  return BatchTensor(torch::ones(utils::add_shapes(batch_shape, base_shape), options),
                     batch_shape.size());
}

BatchTensor
BatchTensor::full(const TorchShapeRef & base_shape, Real init, const torch::TensorOptions & options)
{
  return BatchTensor(torch::full(base_shape, init, options), 0);
}

BatchTensor
BatchTensor::full(const TorchShapeRef & batch_shape,
                  const TorchShapeRef & base_shape,
                  Real init,
                  const torch::TensorOptions & options)
{
  return BatchTensor(torch::full(utils::add_shapes(batch_shape, base_shape), init, options),
                     batch_shape.size());
}

BatchTensor
BatchTensor::identity(TorchSize n, const torch::TensorOptions & options)
{
  return BatchTensor(torch::eye(n, options), 0);
}

BatchTensor
BatchTensor::identity(const TorchShapeRef & batch_shape,
                      TorchSize n,
                      const torch::TensorOptions & options)
{
  return identity(n, options).batch_expand_copy(batch_shape);
}

namespace math
{
BatchTensor
bmm(const BatchTensor & a, const BatchTensor & b)
{
  neml_assert_batch_broadcastable_dbg(a, b);
  neml_assert_dbg(a.base_dim() == 2,
                  "The first tensor in bmm has base dimension ",
                  a.base_dim(),
                  " instead of 2.");
  neml_assert_dbg(b.base_dim() == 2,
                  "The second tensor in bmm has base dimension ",
                  b.base_dim(),
                  " instead of 2.");
  return BatchTensor(torch::matmul(a, b), broadcast_batch_dim(a, b));
}

BatchTensor
bmv(const BatchTensor & a, const BatchTensor & v)
{
  neml_assert_batch_broadcastable_dbg(a, v);
  neml_assert_dbg(a.base_dim() == 2,
                  "The first tensor in bmv has base dimension ",
                  a.base_dim(),
                  " instead of 2.");
  neml_assert_dbg(v.base_dim() == 1,
                  "The second tensor in bmv has base dimension ",
                  v.base_dim(),
                  " instead of 1.");
  return BatchTensor(torch::matmul(a, v.base_unsqueeze(-1)).squeeze(-1), broadcast_batch_dim(a, v));
}

BatchTensor
bvv(const BatchTensor & a, const BatchTensor & b)
{
  neml_assert_batch_broadcastable_dbg(a, b);
  neml_assert_dbg(a.base_dim() == 1,
                  "The first tensor in bvv has base dimension ",
                  a.base_dim(),
                  " instead of 1.");
  neml_assert_dbg(b.base_dim() == 1,
                  "The second tensor in bvv has base dimension ",
                  b.base_dim(),
                  " instead of 1.");
  return BatchTensor(torch::sum(a * b, -1), broadcast_batch_dim(a, b));
}
}

BatchTensor
operator*(const BatchTensor & a, const BatchTensor & b)
{
  neml_assert_broadcastable_dbg(a, b);
  return BatchTensor(torch::operator*(a, b), broadcast_batch_dim(a, b));
}
} // end namespace neml2
