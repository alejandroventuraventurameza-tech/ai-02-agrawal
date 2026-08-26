import EconCSLib

/-!
# Agrawal-Gans-Goldfarb Proposition 3: algebraic audit

This file checks only the one-dimensional quadratic claims that sit downstream
of the paper's probability and optimization assumptions.
-/

namespace AGG25BicyclesForMind

/-- A negative intercept and positive slope give a positive root of the
variance derivative. -/
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

/-- The paper's heterogeneity condition supplies a negative intercept, but that
alone does not make the derivative positive at tool quality one. -/
theorem negativeIntercept_not_enough_at_one :
    ∃ a q : ℝ, a < 0 ∧ 0 < q ∧ a + 2 * q < 0 := by
  refine ⟨-4, 1, ?_, ?_, ?_⟩ <;> norm_num

/-- If gain variance is `q * theta^2` with `q > 0`, it is strictly increasing
between two nonnegative tool-quality levels. -/
theorem gainVariance_strictMono
    (q theta₁ theta₂ : ℝ)
    (hq : 0 < q) (h₁ : 0 ≤ theta₁) (hθ : theta₁ < theta₂) :
    q * theta₁ ^ 2 < q * theta₂ ^ 2 := by
  have h₂ : 0 < theta₂ := lt_of_le_of_lt h₁ hθ
  have hsquare : theta₁ ^ 2 < theta₂ ^ 2 := by nlinarith
  exact (mul_lt_mul_left hq).2 hsquare

end AGG25BicyclesForMind
