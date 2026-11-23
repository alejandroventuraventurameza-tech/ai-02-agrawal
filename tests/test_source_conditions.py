"""Exact-rational necessary-condition tests grounded in NBER WP 34034 (2025).

Printed pp. 12, 18, 38, 41: equations (30), (32), (58), (81).
These checks are not an entire probabilistic-model formalization.
"""
from fractions import Fraction as Q
import unittest


class PrimarySourceConditions(unittest.TestCase):
    def test_published_delta_bound_does_not_ensure_interior_at_one(self):
        # Printed Delta > 2/(s sqrt(alpha)); set sqrt(alpha)=1/2.
        alpha, s, delta = Q(1, 4), Q(1), Q(5)
        lower_in_source = Q(2)/(s*Q(1, 2))
        actual_lower = Q(2)/(s*alpha)
        effort_one = alpha**2*delta**2*s/4 - 1/s
        self.assertEqual(lower_in_source, Q(4))
        self.assertEqual(actual_lower, Q(8))
        self.assertGreater(delta, lower_in_source)
        self.assertLess(delta, actual_lower)
        self.assertEqual(effort_one, -Q(39, 64))

    def test_heterogeneity_not_enough_for_positive_endpoint_slope(self):
        # The audited two-skill illustration, alpha=Gamma=1, Delta=4.
        a0, q = -Q(8, 15), Q(1, 9)
        self.assertLess(a0, 0)
        self.assertGreater(q, 0)
        self.assertEqual(-a0/(2*q), Q(12, 5))
        self.assertEqual(a0+2*q, -Q(14, 45))

    def test_positive_effort_at_one_violates_probability_range(self):
        # Since se+1>1 for any positive s,e, sqrt(se+1)>1.
        for s in (Q(1, 10), Q(3, 5), Q(1)):
            for e in (Q(1, 100), Q(1), Q(10)):
                self.assertGreater(s*e+1, 1)
        self.assertEqual((Q(4)*Q(3, 5)/2, Q(4)*Q(1)/2),
                         (Q(6, 5), Q(2)))

    def test_original_example_meets_printed_delta_bound(self):
        # This is only an algebraic witness, not a bounded p model.
        skills = (Q(3, 5), Q(1))
        alpha, delta = Q(1), Q(4)
        for s in skills:
            self.assertGreater(delta, Q(2)/s)
            self.assertGreater(alpha**2*delta**2*s/4-1/s, 0)
        mu_s = sum(skills, Q(0))/2
        mu_inverse = sum((1/s for s in skills), Q(0))/2
        self.assertEqual(mu_s*mu_inverse, Q(16, 15))
        self.assertGreater(mu_s*mu_inverse, Q(1))


if __name__ == "__main__":
    unittest.main()
