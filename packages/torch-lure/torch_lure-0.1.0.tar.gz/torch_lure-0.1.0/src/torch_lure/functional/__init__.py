import math
import warnings

import torch
import torch.distributions as D
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from torch.overrides import handle_torch_function, has_torch_function_variadic
import torch
import torch.distributions as D
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor


def tanh_exp(x, threshold=3.0):
    """
    TanhExp(x) = x * tanh(exp(x))

    - Clamp is necessary to prevent overflow. Using torch.where alone is insufficient;
        there might be issues when x is small.

    - TanhExp converges to 1 when x is large;  x*tanh(exp(x)) - x < 0f64 if x > 3
    """
    return torch.where(
        x > threshold, x, x * torch.tanh(torch.exp(torch.clamp(x, max=threshold)))
    )


class TanhExp(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, threshold=3.0):
        return tanh_exp(x, threshold)


def quantile_loss(
    input: Tensor,
    target: Tensor,
    quantile: float,
    reduction: str = "mean",
) -> Tensor:
    r"""quantile_loss(input, target, quantile, reduction='mean') -> Tensor

    Measures the element-wise quantile loss.

    The quantile loss is defined as:

    .. math::
        \begin{aligned}
        \ell(x, y) = \begin{cases}
            (1 - q) * (y - x), & \text{if } x < y \\
            q * (x - y), & \text{otherwise }
        \end{cases}
        \end{aligned}

    where :math:`x` is the input tensor, :math:`y` is the target tensor, and :math:`q` is the quantile.

    Args:
        input (Tensor): the input tensor
        target (Tensor): the target tensor
        quantile (float): the quantile value, should be between 0 and 1
        reduction (str, optional): Specifies the reduction to apply to the output:
            ``'none'`` | ``'mean'`` | ``'sum'``. ``'none'``: no reduction will be applied,
            ``'mean'``: the sum of the output will be divided by the number of
            elements in the output, ``'sum'``: the output will be summed. Default: ``'mean'``

    Returns:
        Tensor: the quantile loss
    """
    if has_torch_function_variadic(input, target):
        return handle_torch_function(
            quantile_loss,
            (input, target),
            input,
            target,
            quantile=quantile,
            reduction=reduction,
        )
    if not (target.size() == input.size()):
        warnings.warn(
            f"Using a target size ({target.size()}) that is different to the input size ({input.size()}). "
            "This will likely lead to incorrect results due to broadcasting. "
            "Please ensure they have the same size.",
            stacklevel=2,
        )
    if not (0 <= quantile <= 1):
        raise ValueError(f"Quantile value should be between 0 and 1, got {quantile}")

    expanded_input, expanded_target = torch.broadcast_tensors(input, target)
    diff = expanded_target - expanded_input
    loss = torch.max((quantile - 1) * diff, quantile * diff)

    if reduction == "mean":
        loss = torch.mean(loss)
    elif reduction == "sum":
        loss = torch.sum(loss)
    elif reduction != "none":
        raise ValueError(f"Invalid reduction: {reduction}")

    return loss


class QuantileLoss(nn.Module):
    def __init__(self, quantile: float, reduction: str = "mean"):
        super().__init__()
        self.quantile = quantile
        self.reduction = reduction

    def forward(self, input: Tensor, target: Tensor) -> Tensor:
        return quantile_loss(input, target, self.quantile, self.reduction)
