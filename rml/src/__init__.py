"""
RML extensions for CL-BENCH.

Utilities for analyzing continual-learning trajectories,
including gain, stability, plasticity, and drift.
"""

from .gain import compute_gain
from .stability import compute_stability
from .drift import detect_drift

__all__ = [
    "compute_gain",
    "compute_stability",
    "detect_drift",
]
