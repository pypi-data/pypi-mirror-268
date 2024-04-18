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

#include "neml2/tensors/BatchTensorBase.h"
#include "neml2/tensors/tensors.h"
#include "neml2/tensors/macros.h"

namespace neml2
{
template <class Derived>
BatchTensorBase<Derived>::BatchTensorBase(const torch::Tensor & tensor, TorchSize batch_dim)
  : torch::Tensor(tensor),
    _batch_dim(batch_dim)
{
  neml_assert_dbg((TorchSize)sizes().size() >= _batch_dim,
                  "Tensor dimension ",
                  sizes().size(),
                  " is smaller than the requested number of batch dimensions ",
                  _batch_dim);
}

template <class Derived>
BatchTensorBase<Derived>::BatchTensorBase(const Derived & tensor)
  : torch::Tensor(tensor),
    _batch_dim(tensor.batch_dim())
{
}

template <class Derived>
Derived
BatchTensorBase<Derived>::empty_like(const Derived & other)
{
  return Derived(torch::empty_like(other), other.batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::zeros_like(const Derived & other)
{
  return Derived(torch::zeros_like(other), other.batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::ones_like(const Derived & other)
{
  return Derived(torch::ones_like(other), other.batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::full_like(const Derived & other, Real init)
{
  return Derived(torch::full_like(other, init), other.batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::linspace(
    const Derived & start, const Derived & end, TorchSize nstep, TorchSize dim, TorchSize batch_dim)
{
  neml_assert_broadcastable_dbg(start, end);
  neml_assert_dbg(nstep > 0, "nstep must be positive.");

  using namespace torch::indexing;

  auto res = start.batch_unsqueeze(dim);

  if (nstep > 1)
  {
    auto Bd = broadcast_batch_dim(start, end);
    auto diff = (end - start).batch_unsqueeze(dim);

    TorchSlice net(dim, None);
    net.push_back(Ellipsis);
    net.insert(net.end(), Bd - dim, None);
    Scalar steps = torch::arange(nstep, diff.options()).index(net) / (nstep - 1);

    res = res + steps * diff;
  }

  return Derived(res, batch_dim >= 0 ? batch_dim : res.batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::logspace(const Derived & start,
                                   const Derived & end,
                                   TorchSize nstep,
                                   TorchSize dim,
                                   TorchSize batch_dim,
                                   Real base)
{
  auto exponent = Derived::linspace(start, end, nstep, dim, batch_dim);
  return math::pow(base, exponent);
}

template <class Derived>
bool
BatchTensorBase<Derived>::batched() const
{
  return _batch_dim;
}

template <class Derived>
TorchSize
BatchTensorBase<Derived>::batch_dim() const
{
  return _batch_dim;
}

template <class Derived>
TorchSize &
BatchTensorBase<Derived>::batch_dim()
{
  return _batch_dim;
}

template <class Derived>
TorchSize
BatchTensorBase<Derived>::base_dim() const
{
  return dim() - batch_dim();
}

template <class Derived>
TorchShapeRef
BatchTensorBase<Derived>::batch_sizes() const
{
  return sizes().slice(0, _batch_dim);
}

template <class Derived>
TorchSize
BatchTensorBase<Derived>::batch_size(TorchSize index) const
{
  return batch_sizes()[index >= 0 ? index : index + batch_dim()];
}

template <class Derived>
TorchShapeRef
BatchTensorBase<Derived>::base_sizes() const
{
  return sizes().slice(_batch_dim);
}

template <class Derived>
TorchSize
BatchTensorBase<Derived>::base_size(TorchSize index) const
{
  return base_sizes()[index >= 0 ? index : index + base_dim()];
}

template <class Derived>
TorchSize
BatchTensorBase<Derived>::base_storage() const
{
  return utils::storage_size(base_sizes());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_index(TorchSlice indices) const
{
  indices.insert(indices.end(), base_dim(), torch::indexing::Slice());
  auto res = this->index(indices);
  return Derived(res, res.dim() - base_dim());
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_index(const TorchSlice & indices) const
{
  TorchSlice indices2(batch_dim(), torch::indexing::Slice());
  indices2.insert(indices2.end(), indices.begin(), indices.end());
  return BatchTensor(this->index(indices2), batch_dim());
}

template <class Derived>
void
BatchTensorBase<Derived>::batch_index_put(TorchSlice indices, const torch::Tensor & other)
{
  indices.insert(indices.end(), base_dim(), torch::indexing::Slice());
  this->index_put_(indices, other);
}

template <class Derived>
void
BatchTensorBase<Derived>::base_index_put(const TorchSlice & indices, const torch::Tensor & other)
{
  TorchSlice indices2(batch_dim(), torch::indexing::Slice());
  indices2.insert(indices2.end(), indices.begin(), indices.end());
  this->index_put_(indices2, other);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_expand(TorchShapeRef batch_size) const
{
  // We don't want to touch the base dimensions, so put -1 for them.
  auto net = batch_size.vec();
  net.insert(net.end(), base_dim(), -1);
  return Derived(expand(net), batch_size.size());
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_expand(TorchShapeRef base_size) const
{
  // We don't want to touch the batch dimensions, so put -1 for them.
  auto net = base_size.vec();
  net.insert(net.begin(), batch_dim(), -1);
  return BatchTensor(expand(net), batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_expand_copy(TorchShapeRef batch_size) const
{
  return Derived(batch_expand(batch_size).contiguous(), batch_size.size());
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_expand_copy(TorchShapeRef base_size) const
{
  return BatchTensor(base_expand(base_size).contiguous(), batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_reshape(TorchShapeRef batch_shape) const
{
  return Derived(reshape(utils::add_shapes(batch_shape, base_sizes())), _batch_dim);
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_reshape(TorchShapeRef base_shape) const
{
  return BatchTensor(reshape(utils::add_shapes(batch_sizes(), base_shape)), _batch_dim);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_unsqueeze(TorchSize d) const
{
  auto d2 = d >= 0 ? d : d - base_dim();
  return Derived(unsqueeze(d2), _batch_dim + 1);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::list_unsqueeze() const
{
  return batch_unsqueeze(-1);
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_unsqueeze(TorchSize d) const
{
  auto d2 = d < 0 ? d : d + batch_dim();
  return BatchTensor(torch::Tensor::unsqueeze(d2), batch_dim());
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_transpose(TorchSize d1, TorchSize d2) const
{
  return Derived(
      torch::Tensor::transpose(d1 < 0 ? d1 - base_dim() : d1, d2 < 0 ? d2 - base_dim() : d2),
      _batch_dim);
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_transpose(TorchSize d1, TorchSize d2) const
{
  return BatchTensor(
      torch::Tensor::transpose(d1 < 0 ? d1 : _batch_dim + d1, d2 < 0 ? d2 : _batch_dim + d2),
      _batch_dim);
}

template <class Derived>
BatchTensor
BatchTensorBase<Derived>::base_movedim(TorchSize d1, TorchSize d2) const
{
  return BatchTensor(
      torch::Tensor::movedim(d1 < 0 ? d1 : _batch_dim + d1, d2 < 0 ? d2 : _batch_dim + d2),
      _batch_dim);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::clone(torch::MemoryFormat memory_format) const
{
  return Derived(torch::Tensor::clone(memory_format), _batch_dim);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::detach() const
{
  return Derived(torch::Tensor::detach(), _batch_dim);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::to(const torch::TensorOptions & options) const
{
  return Derived(torch::Tensor::to(options), _batch_dim);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::operator-() const
{
  return Derived(-torch::Tensor(*this), _batch_dim);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::batch_sum(TorchSize d) const
{
  neml_assert_dbg(_batch_dim > 0, "Must have a batch dimension to sum along");
  auto d2 = d >= 0 ? d : d - base_dim();
  return Derived(torch::sum(*this, d2), _batch_dim - 1);
}

template <class Derived>
Derived
BatchTensorBase<Derived>::list_sum() const
{
  return batch_sum(-1);
}

#define BATCHTENSORBASE_INSTANTIATE(T) template class BatchTensorBase<T>
FOR_ALL_BATCHTENSORBASE(BATCHTENSORBASE_INSTANTIATE);
} // end namespace neml2
