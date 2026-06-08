"""
Stability and plasticity decomposition utilities.
"""

from typing import Sequence, Iterable


def compute_stability(
    gains: Sequence[float],
    variant_boundaries: Iterable[int],
) -> float:
    """
    Estimate stability by measuring gain at
    variant transitions.

    Parameters
    ----------
    gains
        Per-instance gains.

    variant_boundaries
        Indices corresponding to the first
        instance of each new variant.

    Returns
    -------
    float
        Mean gain at boundaries.
    """
    indices = list(variant_boundaries)

    if not indices:
        return 0.0

    selected = [
        gains[i]
        for i in indices
        if 0 <= i < len(gains)
    ]

    return (
        sum(selected) / len(selected)
        if selected
        else 0.0
    )


def compute_plasticity(
    gains: Sequence[float],
    variant_boundaries: Iterable[int],
) -> float:
    """
    Estimate plasticity by measuring gain
    away from variant transitions.
    """
    boundaries = set(variant_boundaries)

    selected = [
        g
        for i, g in enumerate(gains)
        if i not in boundaries
    ]

    return (
        sum(selected) / len(selected)
        if selected
        else 0.0
    )
