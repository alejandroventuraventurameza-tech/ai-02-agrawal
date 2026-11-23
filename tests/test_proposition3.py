"""Exact-rational regression tests for the Proposition 3 algebraic audit.

These tests verify mathematical identities, NOT validity of unbounded
square-root expressions as literal probabilities.
Run: python -m unittest discover -s tests -v
"""
import unittest
from fractions import Fraction as Q

SKILLS = (Q(3, 5), Q(1))
K = Q(4)  # alpha=1, Delta=4 => alpha^2 Delta^2 / 4


def mean_two(xs):
    return sum(xs, Q(0)) / 2


def variance_two(xs):
    mu = mean_two(xs)
    return sum(((x - mu) ** 2 for x in xs), Q(0)) / 2


def interior_value(theta, skill):
    return K * skill + theta / skill


def interior_effort(theta, skill):
    return K * skill - theta / skill


class Proposition3Audit(unittest.TestCase):
    def test_heterogeneity_condition_and_moment(self):
        mu_s = mean_two(SKILLS)
        variance_s = variance_two(SKILLS)
        inverse = tuple(1 / s for s in SKILLS)
        # sigma_s = 1/5; the original repository checks mu_s > 3*sigma_s.
        self.assertEqual(mu_s, Q(4, 5))
        self.assertEqual(variance_s, Q(1, 25))
        self.assertGreater(mu_s, 3 * Q(1, 5))
        self.assertEqual(mu_s * mean_two(inverse), Q(16, 15))
        self.assertLess(Q(1), mu_s * mean_two(inverse))

    def test_derivative_at_one_is_negative(self):
        inverse = tuple(1 / s for s in SKILLS)
        q = variance_two(inverse)
        a0 = Q(8) * (Q(1) - mean_two(SKILLS) * mean_two(inverse))
        self.assertEqual(q, Q(1, 9))
        self.assertEqual(a0, -Q(8, 15))
        self.assertEqual(-a0 / (2 * q), Q(12, 5))
        self.assertEqual(a0 + 2 * q, -Q(14, 45))
        self.assertLess(a0 + 2 * q, 0)

    def test_quadratic_variance_identity(self):
        inverse = tuple(1 / s for s in SKILLS)
        base_var = variance_two(tuple(interior_value(Q(0), s) for s in SKILLS))
        a0 = -Q(8, 15)
        q = Q(1, 9)
        for theta in (Q(0), Q(1, 4), Q(1, 2), Q(1)):
            actual = variance_two(tuple(interior_value(theta, s) for s in SKILLS))
            expected = base_var + a0 * theta + q * theta * theta
            self.assertEqual(actual, expected)
            gains = tuple(interior_value(theta, s) - interior_value(Q(0), s)
                          for s in SKILLS)
            self.assertEqual(variance_two(gains), theta * theta * q)

    def test_interiority_and_corner_order(self):
        thresholds = tuple(K * s * s for s in SKILLS)
        self.assertEqual(thresholds, (Q(36, 25), Q(4)))
        for theta in (Q(0), Q(1, 2), Q(1)):
            self.assertTrue(all(interior_effort(theta, s) > 0 for s in SKILLS))
        # The algebraic turning point arrives after the first corner.
        self.assertGreater(Q(12, 5), min(thresholds))
        self.assertLess(interior_effort(Q(2), SKILLS[0]), 0)

    def test_probability_domain_caveat(self):
        # sqrt(s*e_star+theta) = alpha*Delta*s/2 = 2*s at the FOC.
        self.assertEqual(tuple(2*s for s in SKILLS), (Q(6, 5), Q(2)))
        self.assertTrue(all(2*s > 1 for s in SKILLS))
        # This flags that the algebraic example is not a literal p<=1 model.


if __name__ == "__main__":
    unittest.main()
