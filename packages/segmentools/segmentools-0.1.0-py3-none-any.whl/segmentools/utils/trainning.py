import torch
from torch import Tensor


class Aggregator:
    """Class to accumulate values (in torch) across loop and return mean."""

    def __init__(self):
        self.reset()

    def update(self, value: Tensor):
        """Update statics with value and increment iterations.

        Args:
            value (Tensor): Value as Tensor.
        """
        assert not torch.isnan(value), f"Value to add should be float, got {value}"
        if torch.isnan(self.total):
            self.total = value
        else:
            self.total += value
        self.iterations += 1

    def compute(self) -> Tensor:
        """Return mean of values on iterations."""

        assert not torch.isnan(self.total), f"total should not be nan be float, got {self.total}"
        mean = self.total / self.iterations
        return mean

    def reset(self):
        """reset internal statistics."""
        self.total = torch.full((1,), torch.nan, dtype=torch.float32)
        self.iterations = 0
