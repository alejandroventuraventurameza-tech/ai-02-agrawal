"""Exact rational audit of the algebra used in Proposition 3.

This script deliberately uses ``fractions.Fraction`` rather than floating-point
arithmetic.  It checks the source assumptions, the interior solution on
``theta in [0, 1]``, the value formula, and the endpoint claim challenged in
the validation report.
"""

from __future__ import annotations

from fractions import Fraction as F
from typing import Callable, Iterable


ALPHA = F(1)
DELTA_VALUE = F(4)
GAMMA_0 = F(4, 5)
GAMMA = F(2, 5)
DISCOUNT = F(1, 2)
SKILLS = (F(3, 5), F(1))


def mean(values: Iterable[F]) -> F:
    values = tuple(values)
    return sum(values, start=F(0)) / len(values)


def variance(values: Iterable[F]) -> F:
    values = tuple(values)
    center = mean(values)
    return mean((value - center) ** 2 for value in values)


def effort_candidate(skill: F, theta: F) -> F:
    return ALPHA**2 * DELTA_VALUE**2 * skill / 4 - theta / skill


def interior_value(skill: F, theta: F, gamma_multiplier: F) -> F:
    per_opportunity = (
        ALPHA**2 * DELTA_VALUE**2 * skill / 4 + theta / skill
    )
    return gamma_multiplier * per_opportunity


def evaluate(label: str, expression: Callable[[], bool]) -> None:
    if not expression():
        raise AssertionError(label)
    print(f"PASS  {label}")


def main() -> None:
    gamma_multiplier = GAMMA_0 / (1 - DISCOUNT * GAMMA)
    mean_skill = mean(SKILLS)
    skill_variance = variance(SKILLS)
    inverse_skills = tuple(1 / skill for skill in SKILLS)
    mean_inverse_skill = mean(inverse_skills)
    inverse_skill_variance = variance(inverse_skills)

    condition_left = F(1)
    condition_right = mean_skill * mean_inverse_skill
    a0 = DELTA_VALUE**2 * ALPHA**2 / 2 * (
        condition_left - condition_right
    )
    theta_star = -a0 / (2 * inverse_skill_variance)
    derivative_at_one = a0 + 2 * inverse_skill_variance
    first_corner = min(
        ALPHA**2 * DELTA_VALUE**2 * skill**2 / 4 for skill in SKILLS
    )

    evaluate("continuation multiplier Gamma = 1", lambda: gamma_multiplier == 1)
    evaluate("mean skill mu_s = 4/5", lambda: mean_skill == F(4, 5))
    evaluate("skill variance = 1/25", lambda: skill_variance == F(1, 25))
    evaluate("support check mu_s > 3 sigma_s", lambda: F(4, 5) > 3 * F(1, 5))
    evaluate("heterogeneity condition 1 < 16/15", lambda: condition_left < condition_right)
    evaluate("Var(Gamma/s) = 1/9", lambda: inverse_skill_variance == F(1, 9))
    evaluate("variance-derivative intercept a0 = -8/15", lambda: a0 == -F(8, 15))
    evaluate("turning point theta* = 12/5", lambda: theta_star == F(12, 5))
    evaluate("theta* lies beyond one", lambda: theta_star > 1)
    evaluate("derivative at theta = 1 is -14/45", lambda: derivative_at_one == -F(14, 45))
    evaluate("all agents remain interior on [0, 1]", lambda: first_corner == F(36, 25) > 1)

    for skill in SKILLS:
        effort = effort_candidate(skill, F(1))
        effective_input = skill * effort + 1
        first_order_root = ALPHA * DELTA_VALUE * skill / 2
        net_value_from_foc = ALPHA * DELTA_VALUE * first_order_root - effort
        evaluate(
            f"positive effort at theta = 1 for s = {skill}",
            lambda effort=effort: effort > 0,
        )
        evaluate(
            f"effective-input identity for s = {skill}",
            lambda effective_input=effective_input, first_order_root=first_order_root:
                effective_input == first_order_root**2,
        )
        evaluate(
            f"value substitution for s = {skill}",
            lambda skill=skill, net_value_from_foc=net_value_from_foc:
                net_value_from_foc == interior_value(skill, F(1), gamma_multiplier),
        )

    values_at_zero = tuple(
        interior_value(skill, F(0), gamma_multiplier) for skill in SKILLS
    )
    values_at_one = tuple(
        interior_value(skill, F(1), gamma_multiplier) for skill in SKILLS
    )
    gains_at_one = tuple(
        value_one - value_zero
        for value_one, value_zero in zip(values_at_one, values_at_zero)
    )

    evaluate("Var(V(0)) = 16/25", lambda: variance(values_at_zero) == F(16, 25))
    evaluate("Var(V(1)) = 49/225", lambda: variance(values_at_one) == F(49, 225))
    evaluate("total value variance is still falling by theta = 1", lambda: variance(values_at_one) < variance(values_at_zero))
    evaluate("Var(V(1)-V(0)) = 1/9", lambda: variance(gains_at_one) == F(1, 9))

    print()
    print("Exact quantities")
    print(f"Gamma                    = {gamma_multiplier}")
    print(f"E[s] E[1/s]             = {condition_right}")
    print(f"a0                       = {a0}")
    print(f"Var(Gamma/s)             = {inverse_skill_variance}")
    print(f"theta*                   = {theta_star}")
    print(f"d Var(V)/d theta at 1    = {derivative_at_one}")
    print(f"first effort corner      = {first_corner}")
    print("Verdict: the paper's stated assumptions do not imply a positive derivative at theta = 1.")


if __name__ == "__main__":
    main()
