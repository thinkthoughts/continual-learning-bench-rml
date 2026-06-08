"""
Concept drift utilities.
"""

from typing import Sequence, List


def detect_drift(
    gains: Sequence[float],
    threshold: float = -0.10,
) -> List[int]:
    """
    Identify potential drift events.

    Drift is flagged whenever gain drops
    below the supplied threshold.

    Parameters
    ----------
    gains
        Per-instance gains.

    threshold
        Drift cutoff.

    Returns
    -------
    List[int]
        Indices where drift may have occurred.
    """
    return [
        i
        for i, g in enumerate(gains)
        if g < threshold
    ]
