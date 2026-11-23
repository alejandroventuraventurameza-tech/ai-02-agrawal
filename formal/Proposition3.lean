import Mathlib.Tactic

/-!
# Algebraic audit of Proposition 3, Agrawal--Gans--Goldfarb (2025)

These are exact downstream algebraic statements, not a formalization of
probability measures, independence, expected values, or the paper's FOC.
In particular, this file DOES NOT prove that the published Proposition 3
holds globally, nor that p is a bounded probability.

See formal/README.md for the source-to-Lean scope and toolchain.
-/

namespace AGG25BicyclesForMind

/-- A negative intercept and positive quadratic coefficient imply an
algebraically positive zero of the variance derivative. -/
theorem turningPoint_pos_and_zero
    (a q thetaStar : ℝ)
    (ha : a < 0) (hq : 0 < q)
    (hstar : thetaStar = -a / (2 * q)) :
    0 < thetaStar ∧ a + 2 * thetaStar * q = 0 := by
  constructor
  · rw [hstar]
    positivity
  · rw [hstar]
    field_simp [ne_of_gt hq]
    ring

/-- A negative initial slope and positive curvature alone do not
imply a positive derivative at theta = 1. -/
theorem negativeIntercept_not_enough_at_one :
    ∃ a q : ℝ, a < 0 ∧ 0 < q ∧ a + 2 * q < 0 := by
  refine ⟨-4, 1, ?_, ?_, ?_⟩ <;> norm_num

/-- Individual-benefit variance q * theta^2 rises strictly between
two ordered nonnegative qualities when q is positive. -/
theorem gainVariance_strictMono
    (q theta₁ theta₂ : ℝ)
    (hq : 0 < q) (h₁ : 0 ≤ theta₁) (hθ : theta₁ < theta₂) :
    q * theta₁ ^ 2 < q * theta₂ ^ 2 := by
  have h₂ : 0 < theta₂ := lt_of_le_of_lt h₁ hθ
  have hsquare : theta₁ ^ 2 < theta₂ ^ 2 := by nlinarith
  exact (mul_lt_mul_left hq).2 hsquare

/-- Exact derivative at tool quality one for the two-skill algebraic case. -/
theorem twoType_derivative_at_one :
    (-8 / 15 : ℝ) + 2 * (1 / 9 : ℝ) = -14 / 45 := by
  norm_num

/-- The extrapolated turning point is beyond the first zero-effort
corner, so the interior formula does not certify a global U-shape. -/
theorem twoType_turningPoint_after_corner :
    (36 / 25 : ℝ) < 12 / 5 := by
  norm_num

/-- In the illustrative interior FOC, p* > 1 for both types:
a warning about interpreting the square-root index as a probability. -/
theorem twoType_sqrt_success_index_exceeds_one :
    (1 : ℝ) < 6 / 5 ∧ (1 : ℝ) < 2 := by
  constructor <;> norm_num

#print axioms turningPoint_pos_and_zero
#print axioms negativeIntercept_not_enough_at_one
#print axioms gainVariance_strictMono
#print axioms twoType_derivative_at_one
#print axioms twoType_turningPoint_after_corner
#print axioms twoType_sqrt_success_index_exceeds_one

end AGG25BicyclesForMind
