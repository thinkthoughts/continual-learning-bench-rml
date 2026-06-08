"""
Gain-related metrics.

CL-BENCH defines gain as the difference between stateful
and stateless reward trajectories.
"""

from typing import Sequence, List


def compute_gain(
    stateful_rewards: Sequence[float],
    stateless_rewards: Sequence[float],
) -> List[float]:
    """
    Compute per-instance gain.

    Parameters
    ----------
    stateful_rewards : Sequence[float]
        Rewards from the stateful system.

    stateless_rewards : Sequence[float]
        Rewards from the stateless baseline.

    Returns
    -------
    List[float]
        Gain values:
            g_t = r_sf - r_sl
    """
    if len(stateful_rewards) != len(stateless_rewards):
        raise ValueError(
            "Stateful and stateless reward sequences "
            "must have equal length."
        )

    return [
        sf - sl
        for sf, sl in zip(
            stateful_rewards,
            stateless_rewards,
        )
    ]


def cumulative_gain(
    gains: Sequence[float],
) -> float:
    """
    Compute total gain.
    """
    return sum(gains)


def average_gain(
    gains: Sequence[float],
) -> float:
    """
    Compute mean gain.
    """
    return (
        sum(gains) / len(gains)
        if gains
        else 0.0
    )
