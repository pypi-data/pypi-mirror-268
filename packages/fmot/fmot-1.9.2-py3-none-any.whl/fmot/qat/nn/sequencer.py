import torch
from torch import nn, Tensor
from . import quantizers, atomics
from ..annotated_tensors import set_dim_annotations
from functools import partial
from typing import *
import logging

logger = logging.getLogger(__file__)


class StateInitializer(nn.Module):
    def __init__(
        self,
        state_shapes,
        bitwidth,
        batch_dim,
        observer=quantizers.DEFAULT_OBSERVERS["default"],
    ):
        super().__init__()
        self.state_shapes = state_shapes
        self.batch_dim = batch_dim
        self.quantizers = nn.ModuleList()
        self.requantizers = nn.ModuleList()
        self.q_groups = []
        for __ in range(len(state_shapes)):
            quant = quantizers.StateQuantizer(bitwidth, observer=observer)
            requant = atomics.Requantize(bitwidth, observer=observer)
            quantizers.share_observer(quant, requant)
            self.quantizers.append(quant)
            self.requantizers.append(requant)
            quant_group = quantizers.PrecisionConstraint()
            quant_group.add(quant)
            quant_group.add(requant.quantizer)
            self.q_groups.append(quant_group)

        self.p_inherit = 0
        self._n_state = None

    @torch.jit.ignore
    def store_state(self, state: List[Tensor]):
        if self.p_inherit > 0:
            for i, x in enumerate(state):
                self.register_buffer(f"_prev_state_{i}", x.detach(), persistent=False)
            self._n_state = len(state)

    @torch.jit.ignore
    def inherit_state(self, batch_size: int, p_inherit: float) -> List[Tensor]:
        state = []
        mask = None
        for i in range(self._n_state):
            x_prev = getattr(self, f"_prev_state_{i}", None)
            if x_prev is None:
                return None
            else:
                # transpose x_prev to put batch_dim first
                if self.batch_dim != 0:
                    x_prev = x_prev.transpose(0, self.batch_dim)

                batch_size_prev = x_prev.shape[0]

                # create an inheritance mask
                if mask is None:
                    # only create mask on the first state, so that inheritance is aligned across all of the tensors
                    mask = (
                        torch.rand(batch_size_prev, device=x_prev.device) >= p_inherit
                    )
                    # broadcast mask to x_prev's shape
                    mask = mask.unsqueeze(-1)

                x_prev = torch.masked_fill(x_prev, mask, 0)

                # trim / pad to new batch size
                if batch_size_prev > batch_size:
                    x_prev = x_prev[:batch_size]
                elif batch_size_prev < batch_size:
                    zeros = torch.zeros(
                        (batch_size - batch_size_prev, x_prev.shape[1]),
                        device=x_prev.device,
                    )
                    x_prev = torch.cat([x_prev, zeros], 0)

                # don't undo the transpose -- we want batch-dim to be first!

                state.append(x_prev)

        return state

    def forward(self, x) -> List[Tensor]:
        batch_size = x.shape[self.batch_dim]

        state = None
        if self.p_inherit > 0 and self._n_state is not None:
            state = self.inherit_state(batch_size, self.p_inherit)

        if state is None:
            state = [
                torch.zeros(batch_size, *shape, device=x.device)
                for shape in self.state_shapes
            ]

        for y in state:
            set_dim_annotations(
                ["B", *["F" for _ in range(len(self.state_shapes[0]))]], y
            )
        return [l(y) for l, y in zip(self.quantizers, state)]

    def observe_state(self, state):
        for l, x in zip(self.quantizers, state):
            l.update_statistics(x)

    def quantize_state(self, state):
        outputs = []
        for l, x in zip(self.requantizers, state):
            outputs.append(l(x))
        return outputs

    @classmethod
    def _from_float(
        cls,
        parent,
        bw_conf,
        interpolate,
        observer=quantizers.DEFAULT_OBSERVERS["default"],
        **kwargs,
    ):
        observer = partial(observer, **kwargs)
        return cls(
            state_shapes=parent.state_shapes,
            bitwidth=bw_conf.activations,
            batch_dim=parent.batch_dim,
            observer=observer,
        )
