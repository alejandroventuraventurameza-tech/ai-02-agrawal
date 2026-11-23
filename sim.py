"""Reproducible audit of Proposition 3 in Agrawal, Gans & Goldfarb (2025).

The script separates three objects:
1. cross-sectional variance of the total continuation value;
2. cross-sectional variance of the individual tool benefit;
3. the constrained optimum after effort reaches the corner e = 0.

Run:
    python sim.py
    python sim.py --no-plot
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ALPHA = 1.0
DELTA = 4.0
GAMMA0 = 0.8
GAMMA = 0.4
DISCOUNT = 0.5
GAMMA_MULTIPLIER = GAMMA0 / (1.0 - DISCOUNT * GAMMA)
SKILLS = np.array([0.6, 1.0])
PROBABILITIES = np.array([0.5, 0.5])
K = ALPHA**2 * DELTA**2 / 4.0


def expectation(values: np.ndarray) -> np.ndarray:
    """Population expectation over the last axis."""
    return np.sum(values * PROBABILITIES, axis=-1)


def variance(values: np.ndarray) -> np.ndarray:
    """Population variance over the last axis."""
    mean = expectation(values)
    return expectation((values - np.expand_dims(mean, axis=-1)) ** 2)


def interior_effort(theta: np.ndarray) -> np.ndarray:
    """Unconstrained FOC candidate; can become negative."""
    return K * SKILLS - np.expand_dims(theta, -1) / SKILLS


def interior_value(theta: np.ndarray) -> np.ndarray:
    """Paper's closed-form continuation value, valid only when effort is positive."""
    return GAMMA_MULTIPLIER * (
        K * SKILLS + np.expand_dims(theta, -1) / SKILLS
    )


def constrained_value(theta: np.ndarray) -> np.ndarray:
    """Value from the true optimum e*(theta) = max{interior candidate, 0}."""
    theta_column = np.expand_dims(theta, -1)
    effort = np.maximum(K * SKILLS - theta_column / SKILLS, 0.0)
    per_opportunity = (
        ALPHA * DELTA * np.sqrt(SKILLS * effort + theta_column) - effort
    )
    return GAMMA_MULTIPLIER * per_opportunity


def analytic_audit() -> dict[str, float]:
    assert np.isclose(GAMMA_MULTIPLIER, 1.0)
    mu_s = expectation(SKILLS)
    sigma_s = np.sqrt(variance(SKILLS))
    inverse_skill = 1.0 / SKILLS
    e_inv_s = expectation(inverse_skill)
    var_inv_s = variance(inverse_skill)

    condition_lhs = 1.0  # E[Gamma^2] / E[Gamma]^2 because Gamma is constant.
    condition_rhs = mu_s * e_inv_s
    a0 = (DELTA**2 * ALPHA**2 / 2.0) * (1.0 - condition_rhs)
    theta_star = -a0 / (2.0 * var_inv_s)
    derivative_at_one = a0 + 2.0 * var_inv_s
    gain_variance_derivative_at_one = 2.0 * var_inv_s
    smallest_corner = np.min(K * SKILLS**2)

    assert mu_s > 3.0 * sigma_s
    assert condition_lhs < condition_rhs
    assert smallest_corner > 1.0
    assert derivative_at_one < 0.0
    assert theta_star > 1.0

    return {
        "mu_s": float(mu_s),
        "sigma_s": float(sigma_s),
        "condition_lhs": float(condition_lhs),
        "condition_rhs": float(condition_rhs),
        "a0": float(a0),
        "var_gamma_over_s": float(var_inv_s),
        "theta_star": float(theta_star),
        "derivative_at_one": float(derivative_at_one),
        "gain_variance_derivative_at_one": float(
            gain_variance_derivative_at_one
        ),
        "smallest_corner": float(smallest_corner),
    }


def print_audit(results: dict[str, float]) -> None:
    print("Proposition 3 exact two-type audit")
    print("----------------------------------")
    print(f"skills: {SKILLS.tolist()} with equal probability")
    print(
        "opportunity parameters: "
        f"gamma0={GAMMA0}, gamma={GAMMA}, delta={DISCOUNT}, "
        f"so Gamma={GAMMA_MULTIPLIER:.1f}"
    )
    print(f"mu_s = {results['mu_s']:.6f}")
    print(f"sigma_s = {results['sigma_s']:.6f}")
    print(
        "support/moment check: "
        f"mu_s > 3 sigma_s is {results['mu_s']:.3f} > "
        f"{3 * results['sigma_s']:.3f}"
    )
    print(
        "condition (30): "
        f"{results['condition_lhs']:.6f} < "
        f"{results['condition_rhs']:.6f}"
    )
    print(f"a0 = {results['a0']:.6f} < 0")
    print(f"Var(Gamma/s) = {results['var_gamma_over_s']:.6f} > 0")
    print(f"algebraic theta* = {results['theta_star']:.6f}")
    print(
        "d Var(V)/d theta at theta=1 = "
        f"{results['derivative_at_one']:.6f} < 0"
    )
    print(
        "d Var(V(theta)-V(0))/d theta at theta=1 = "
        f"{results['gain_variance_derivative_at_one']:.6f} > 0"
    )
    print(
        "first zero-effort corner occurs at theta = "
        f"{results['smallest_corner']:.6f}"
    )
    print("VERDICT: condition (30) does not imply a positive slope at theta=1.")


def make_figure(output: Path, results: dict[str, float]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    theta_unit = np.linspace(0.0, 1.0, 401)
    total_var_unit = variance(interior_value(theta_unit))
    gains_unit = interior_value(theta_unit) - interior_value(np.zeros_like(theta_unit))
    gain_var_unit = variance(gains_unit)

    theta_long = np.linspace(0.0, 5.0, 1001)
    paper_var_long = variance(interior_value(theta_long))
    true_var_long = variance(constrained_value(theta_long))

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titleweight": "bold",
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), constrained_layout=True)

    axes[0].plot(theta_unit, total_var_unit, color="#183153", linewidth=2.8)
    axes[0].scatter([1.0], [total_var_unit[-1]], color="#d1495b", zorder=3)
    axes[0].set_title("A. Total wage variance on [0, 1]")
    axes[0].set_xlabel(r"tool quality $\theta$")
    axes[0].set_ylabel(r"$\mathrm{Var}[V(\theta)]$")
    axes[0].annotate(
        "slope at 1 < 0",
        xy=(1.0, total_var_unit[-1]),
        xytext=(0.50, total_var_unit[-1] + 0.16),
        arrowprops={"arrowstyle": "->", "color": "#d1495b"},
        color="#9c2333",
    )
    axes[0].grid(alpha=0.18)

    axes[1].plot(theta_unit, gain_var_unit, color="#2a9d8f", linewidth=2.8)
    axes[1].set_title("B. Variance of the individual gain")
    axes[1].set_xlabel(r"tool quality $\theta$")
    axes[1].set_ylabel(r"$\mathrm{Var}[V(\theta)-V(0)]$")
    axes[1].text(
        0.05,
        0.90,
        r"$=\theta^2\mathrm{Var}(\Gamma/s)$",
        transform=axes[1].transAxes,
        color="#16675f",
    )
    axes[1].grid(alpha=0.18)

    axes[2].plot(
        theta_long,
        paper_var_long,
        color="#8d99ae",
        linestyle="--",
        linewidth=2.2,
        label="interior extrapolation",
    )
    axes[2].plot(
        theta_long,
        true_var_long,
        color="#e76f51",
        linewidth=2.8,
        label="constrained optimum",
    )
    for corner in K * SKILLS**2:
        axes[2].axvline(corner, color="#6c757d", linewidth=1, alpha=0.45)
    axes[2].axvline(
        results["theta_star"], color="#183153", linewidth=1.3, alpha=0.65
    )
    axes[2].set_title("C. The corner changes the global result")
    axes[2].set_xlabel(r"tool quality $\theta$")
    axes[2].set_ylabel("cross-sectional variance")
    axes[2].legend(frameon=False, loc="upper right")
    axes[2].grid(alpha=0.18)

    fig.suptitle(
        "Proposition 3 audit: the two variance objects and the missing corner",
        fontsize=14,
        fontweight="bold",
        color="#183153",
    )
    fig.savefig(output, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_slide_figure(output: Path) -> None:
    """One readable panel for the five-minute Beamer deck.

    The three-panel extended audit remains available separately. This chart
    shows an algebraic example, NOT a probability-calibrated model.
    """
    output.parent.mkdir(parents=True, exist_ok=True)
    theta = np.linspace(0.0, 1.0, 401)
    values = variance(interior_value(theta))
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(theta, values, color="#183153", linewidth=3.5)
    ax.scatter([1.0], [values[-1]], color="#d1495b", s=55, zorder=4)
    ax.annotate(
        r"$d\,\mathrm{Var}(V)/d\theta|_{\theta=1}=-14/45$",
        xy=(1.0, values[-1]),
        xytext=(0.32, 0.36),
        textcoords="axes fraction",
        fontsize=13,
        color="#9c2333",
        arrowprops={"arrowstyle": "->", "color": "#9c2333", "lw": 1.5},
    )
    ax.set_xlabel(r"Tool quality $\theta$", fontsize=14)
    ax.set_ylabel(r"Cross-sectional $\mathrm{Var}(V(\theta))$", fontsize=13)
    ax.set_title("Value variance continues to fall on [0, 1]", fontsize=14)
    ax.text(
        0.025, 0.055,
        r"Algebraic illustration only: $p^*>1$",
        transform=ax.transAxes, fontsize=10, color="#555555",
    )
    ax.grid(alpha=0.2)
    fig.tight_layout(pad=1.1)
    fig.savefig(output, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("figures/prop3-variance-audit.png"),
        help="Path for the generated PNG figure.",
    )
    parser.add_argument(
        "--slide-output",
        type=Path,
        default=Path("figures/prop3-slide-audit.png"),
        help="Readable one-panel figure for the Beamer presentation.",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Run exact checks and print the audit without generating a figure.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = analytic_audit()
    print_audit(results)
    if not args.no_plot:
        make_figure(args.output, results)
        print(f"figure: {args.output.resolve()}")
        make_slide_figure(args.slide_output)
        print(f"slide figure: {args.slide_output.resolve()}")


if __name__ == "__main__":
    main()
