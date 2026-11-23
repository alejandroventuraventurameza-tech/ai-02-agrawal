"""A separately labeled, probability-bounded extension of AGG (2025).

This is NOT Proposition 3 with its original functional form:
    p(se;theta) = min(sqrt(se+theta), 1), alpha=Gamma=1, Delta=2.
There are two equally likely skill types s=3/5 and s=1.

Run:
    python bounded_model.py
    python -m unittest discover -s tests -v

Proof of the analytic formulas is in extra/bounded-probability-variant.md.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


S_LOW = 3.0 / 5.0
S_HIGH = 1.0
GAP_AT_ZERO = S_HIGH - S_LOW
LOW_CORNER = S_LOW**2


def optimized_effort(skill: float, theta: np.ndarray) -> np.ndarray:
    """Global optimizer of 2 min(sqrt(s e + theta), 1) - e for s<=1."""
    t = np.asarray(theta, dtype=float)
    if np.any(t < 0):
        raise ValueError("Tool quality theta must be nonnegative")
    return np.maximum(skill - t / skill, 0.0)


def optimized_value(skill: float, theta: np.ndarray) -> np.ndarray:
    """Optimized value, accounting for the success-probability cap."""
    t = np.asarray(theta, dtype=float)
    e = optimized_effort(skill, t)
    p = np.minimum(np.sqrt(skill * e + t), 1.0)
    return 2.0 * p - e


def value_gap(theta: np.ndarray) -> np.ndarray:
    """Analytic value advantage of the high-skill type."""
    t = np.asarray(theta, dtype=float)
    if np.any(t < 0):
        raise ValueError("theta must be nonnegative")
    return np.where(
        t <= LOW_CORNER,
        2.0 / 5.0 - 2.0 * t / 3.0,
        np.where(t <= 1.0, (1.0 - np.sqrt(t)) ** 2, 0.0),
    )


def verify() -> None:
    theta = np.linspace(0.0, 1.5, 1501)
    gap = optimized_value(S_HIGH, theta) - optimized_value(S_LOW, theta)
    expected_gap = value_gap(theta)
    assert np.allclose(gap, expected_gap, atol=2e-13, rtol=1e-12)
    assert np.all(gap >= -2e-13)
    assert np.all(np.diff(gap) <= 2e-13)
    total_variance = gap**2 / 4.0
    gain_variance = (gap - GAP_AT_ZERO) ** 2 / 4.0
    assert np.all(np.diff(total_variance) <= 2e-13)
    assert np.all(np.diff(gain_variance) >= -2e-13)
    assert np.isclose(total_variance[0], 1.0 / 25.0)
    assert np.isclose(total_variance[-1], 0.0)
    assert np.isclose(gain_variance[-1], 1.0 / 25.0)
    print("VERIFIED: p in [0, 1]; total variance falls 1/25 -> 0")
    print("VERIFIED: individual-gain variance rises 0 -> 1/25")
    print("NOTE: the capped p has a saturation kink; not the original p")


def plot(output: Path) -> None:
    theta = np.linspace(0.0, 1.2, 601)
    gap = value_gap(theta)
    var_total = gap**2 / 4.0
    var_gain = (gap - GAP_AT_ZERO) ** 2 / 4.0

    fig, ax = plt.subplots(figsize=(7.6, 4.25))
    ax.plot(theta, var_total, linewidth=3.0, color="#183153",
            label=r"Var(total value)")
    ax.plot(theta, var_gain, linewidth=3.0, color="#2A9D8F",
            label=r"Var(individual gains)")
    ax.axvline(LOW_CORNER, color="#888888", linestyle=":", linewidth=1.4)
    ax.axvline(1.0, color="#888888", linestyle=":", linewidth=1.4)
    ax.text(LOW_CORNER + 0.01, 0.0335, r"low-skill corner $0.36$", fontsize=9)
    ax.text(1.005, 0.007, "all effort zero", rotation=90, fontsize=9)
    ax.set_xlabel(r"Tool quality $\theta$", fontsize=12)
    ax.set_ylabel("Cross-sectional variance", fontsize=12)
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 0.045)
    ax.set_title("Probability cap: inequality in levels and gains", fontsize=12)
    ax.legend(loc="center right", frameon=False, fontsize=10)
    ax.grid(alpha=0.15)
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path("figures/prop3-bounded-success.png"))
    args = parser.parse_args()
    verify()
    plot(args.output)
    print(f"figure: {args.output.resolve()}")
