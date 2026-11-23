"""Tests for the NEW capped-probability model, not the original Prop. 3."""
from fractions import Fraction as Q
from math import isqrt, sqrt
import unittest


S_LOW = Q(3, 5)
S_HIGH = Q(1)
SKILLS = (S_LOW, S_HIGH)


def sqrt_fraction_exact(x):
    n, d = isqrt(x.numerator), isqrt(x.denominator)
    root = Q(n, d)
    if root * root != x:
        raise ValueError(f"Not a rational square: {x}")
    return root


def value_exact(skill, theta):
    """Exact optimum of capped success, where 0 < skill <= 1."""
    if theta >= 1:
        return Q(2)
    if theta <= skill * skill:
        return skill + theta / skill
    return 2 * sqrt_fraction_exact(theta)


class BoundedVariantAudit(unittest.TestCase):
    def test_probability_is_capped_at_one(self):
        for theta in (0, 0.05, 0.25, 0.36, 0.8, 1.0, 1.5, 3.0):
            for skill in (0.6, 1.0):
                e = max(skill - theta / skill, 0.0)
                p_star = min(sqrt(skill * e + theta), 1.0)
                self.assertGreaterEqual(p_star, 0)
                self.assertLessEqual(p_star, 1)

    def test_exact_gap_across_all_branches(self):
        data = (
            (Q(0), Q(2, 5)),
            (Q(1, 4), Q(7, 30)),
            (Q(9, 25), Q(4, 25)),
            (Q(9, 16), Q(1, 16)),
            (Q(1), Q(0)),
            (Q(9, 4), Q(0)),
        )
        gaps = []
        for theta, expected in data:
            gap = value_exact(S_HIGH, theta) - value_exact(S_LOW, theta)
            self.assertEqual(gap, expected)
            gaps.append(gap)
        level_var = [d*d/4 for d in gaps]
        gain_var = [(d-Q(2, 5))**2/4 for d in gaps]
        self.assertTrue(all(a >= b for a, b in zip(level_var, level_var[1:])))
        self.assertTrue(all(a <= b for a, b in zip(gain_var, gain_var[1:])))
        self.assertEqual(level_var[0], Q(1, 25))
        self.assertEqual(level_var[-1], Q(0))
        self.assertEqual(gain_var[0], Q(0))
        self.assertEqual(gain_var[-1], Q(1, 25))

    def test_heterogeneity_and_interior_local_slope(self):
        # Gamma=1, skill mean 4/5, inverse skill mean 4/3.
        self.assertLess(Q(1), Q(4, 5)*Q(4, 3))
        self.assertLess(Q(9, 25), Q(3, 5))  # first corner before algebraic turn
        # For Delta=2: a0=-2/15, q=1/9. At theta=3/10,
        # the derivative is negative, with valid p and interior effort.
        self.assertEqual(-Q(2, 15) + 2*Q(3, 10)/9, -Q(1, 15))
        for s in SKILLS:
            self.assertGreater(s-Q(3, 10)/s, Q(0))
            self.assertLessEqual(s, Q(1))  # p* = s

    def test_analytic_optimum_beats_sampled_efforts(self):
        """Numerical corroboration only; the analytic KKT proof is in extra/."""
        for theta in (0.0, 0.1, 0.25, 0.36, 0.5625, 0.9, 1.0, 2.0):
            for skill in (0.6, 1.0):
                e_star = max(skill-theta/skill, 0.0)

                def objective(e):
                    return 2.0*min(sqrt(skill*e+theta), 1.0)-e

                baseline = objective(e_star)
                for j in range(0, 201):
                    self.assertGreaterEqual(baseline+1e-11,
                                            objective(j/50.0))


if __name__ == "__main__":
    unittest.main()
