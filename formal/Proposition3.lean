import EconCSLib.Foundations.Math.AffineThreshold
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# Agrawal--Gans--Goldfarb, Proposition 3: algebraic validation

This file formalizes the deterministic algebra used by Proposition 3. It does
not formalize the source paper's probability space, independence assumptions,
or the translation from the economic model to the moment formulas. Those
items remain part of the source-facing validation ledger.
-/

namespace AGG25BicyclesForMind

noncomputable section

/-- Equation (58): the candidate effort in the interior region. -/
def effortCandidate
    (alpha deltaValue skill theta : ℝ) : ℝ :=
  alpha ^ 2 * deltaValue ^ 2 * skill / 4 - theta / skill

/-- Equation (59), before multiplication by the continuation factor. -/
def interiorPerOpportunityValue
    (alpha deltaValue skill theta : ℝ) : ℝ :=
  alpha ^ 2 * deltaValue ^ 2 * skill / 4 + theta / skill

/-- Equation (60): lifetime value in the interior region. -/
def continuationValue
    (gammaMultiplier alpha deltaValue skill theta : ℝ) : ℝ :=
  gammaMultiplier *
    interiorPerOpportunityValue alpha deltaValue skill theta

/-- Equation (81): the derivative of the cross-sectional value variance. -/
def varianceDerivative (a0 q theta : ℝ) : ℝ :=
  a0 + 2 * theta * q

/-- Equation (83): the intercept implied by the source moments. -/
def derivativeIntercept
    (deltaValue alphaSecondMoment gammaSecondMoment gammaMean
      meanSkill meanInverseSkill : ℝ) : ℝ :=
  deltaValue ^ 2 * alphaSecondMoment / 2 *
    (gammaSecondMoment - gammaMean ^ 2 * meanSkill * meanInverseSkill)

/-- Equation (88): the zero of the affine variance derivative. -/
def turningPoint (a0 q : ℝ) : ℝ :=
  EconCSLib.affineCutoff a0 (2 * q) 0

/-- Variance of the individual gain from the tool, derived in the audit. -/
def gainVariance (q theta : ℝ) : ℝ :=
  q * theta ^ 2

/-- Positive effort is exactly the strict interiority inequality implied by
equation (58). -/
theorem effortCandidate_pos_iff
    (alpha deltaValue skill theta : ℝ) (hskill : 0 < skill) :
    0 < effortCandidate alpha deltaValue skill theta ↔
      theta < alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := by
  unfold effortCandidate
  constructor
  · intro h
    have hdiv :
        theta / skill < alpha ^ 2 * deltaValue ^ 2 * skill / 4 :=
      sub_pos.mp h
    have hmul := (div_lt_iff₀ hskill).mp hdiv
    calc
      theta < (alpha ^ 2 * deltaValue ^ 2 * skill / 4) * skill := hmul
      _ = alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := by ring
  · intro h
    apply sub_pos.mpr
    apply (div_lt_iff₀ hskill).mpr
    calc
      theta < alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := h
      _ = (alpha ^ 2 * deltaValue ^ 2 * skill / 4) * skill := by ring

/-- Nonnegative effort is exactly the weak version of the interiority bound. -/
theorem effortCandidate_nonneg_iff
    (alpha deltaValue skill theta : ℝ) (hskill : 0 < skill) :
    0 ≤ effortCandidate alpha deltaValue skill theta ↔
      theta ≤ alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := by
  unfold effortCandidate
  constructor
  · intro h
    have hdiv :
        theta / skill ≤ alpha ^ 2 * deltaValue ^ 2 * skill / 4 :=
      sub_nonneg.mp h
    have hmul := (div_le_iff₀ hskill).mp hdiv
    calc
      theta ≤ (alpha ^ 2 * deltaValue ^ 2 * skill / 4) * skill := hmul
      _ = alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := by ring
  · intro h
    apply sub_nonneg.mpr
    apply (div_le_iff₀ hskill).mpr
    calc
      theta ≤ alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := h
      _ = (alpha ^ 2 * deltaValue ^ 2 * skill / 4) * skill := by ring

/-- Substituting the candidate effort cancels tool quality from `s e + θ`. -/
theorem effectiveInput_at_candidate
    (alpha deltaValue skill theta : ℝ) (hskill : skill ≠ 0) :
    skill * effortCandidate alpha deltaValue skill theta + theta =
      alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 / 4 := by
  unfold effortCandidate
  field_simp [hskill]
  ring

/-- The cleared first-order condition has the candidate as its unique solution
when skill is nonzero. Clearing the equation avoids hidden sign assumptions
that would arise from squaring a square-root equation. -/
theorem clearedFOC_iff_effortCandidate
    (alpha deltaValue skill theta effort : ℝ) (hskill : skill ≠ 0) :
    4 * (skill * effort + theta) =
        alpha ^ 2 * deltaValue ^ 2 * skill ^ 2 ↔
      effort = effortCandidate alpha deltaValue skill theta := by
  constructor
  · intro hfoc
    unfold effortCandidate
    field_simp [hskill]
    nlinarith
  · intro heffort
    rw [heffort, effectiveInput_at_candidate _ _ _ _ hskill]
    ring

/-- Given the root identity from the first-order condition, substituting the
candidate effort yields the interior per-opportunity value in (59). -/
theorem interiorValue_substitution
    (alpha deltaValue skill theta rootTerm : ℝ)
    (hskill : skill ≠ 0)
    (hroot : rootTerm = alpha * deltaValue * skill / 2) :
    alpha * deltaValue * rootTerm -
        effortCandidate alpha deltaValue skill theta =
      interiorPerOpportunityValue alpha deltaValue skill theta := by
  rw [hroot]
  unfold effortCandidate interiorPerOpportunityValue
  field_simp [hskill]
  ring

/-- In the interior region, the individual value gain is `Γ θ / s`. -/
theorem individualGain_eq
    (gammaMultiplier alpha deltaValue skill theta : ℝ)
    (hskill : skill ≠ 0) :
    continuationValue gammaMultiplier alpha deltaValue skill theta -
        continuationValue gammaMultiplier alpha deltaValue skill 0 =
      theta * gammaMultiplier / skill := by
  unfold continuationValue interiorPerOpportunityValue
  field_simp [hskill]
  ring

/-- With a nonzero mean opportunity multiplier, condition (30) is equivalent
to negativity of the moment gap appearing in equation (83). -/
theorem paperCondition_iff_negativeMomentGap
    (gammaSecondMoment gammaMean meanSkill meanInverseSkill : ℝ)
    (hgammaMean : gammaMean ≠ 0) :
    gammaSecondMoment / gammaMean ^ 2 < meanSkill * meanInverseSkill ↔
      gammaSecondMoment -
          gammaMean ^ 2 * meanSkill * meanInverseSkill < 0 := by
  have hgammaSquare : 0 < gammaMean ^ 2 := sq_pos_of_ne_zero hgammaMean
  rw [div_lt_iff₀ hgammaSquare]
  constructor <;> intro h <;> nlinarith

/-- Condition (30), written without division, makes the variance-derivative
intercept strictly negative when payoff value and its second moment are
positive. -/
theorem derivativeIntercept_neg_of_paperCondition
    (deltaValue alphaSecondMoment gammaSecondMoment gammaMean
      meanSkill meanInverseSkill : ℝ)
    (hdeltaValue : deltaValue ≠ 0)
    (halphaSecondMoment : 0 < alphaSecondMoment)
    (hcondition :
      gammaSecondMoment < gammaMean ^ 2 * meanSkill * meanInverseSkill) :
    derivativeIntercept deltaValue alphaSecondMoment gammaSecondMoment
        gammaMean meanSkill meanInverseSkill < 0 := by
  unfold derivativeIntercept
  have hcoefficient :
      0 < deltaValue ^ 2 * alphaSecondMoment / 2 := by
    positivity
  exact mul_neg_of_pos_of_neg hcoefficient (sub_neg.mpr hcondition)

/-- With a negative intercept and positive slope, the variance derivative has
a positive zero. -/
theorem turningPoint_pos_and_zero
    (a0 q : ℝ) (ha0 : a0 < 0) (hq : 0 < q) :
    0 < turningPoint a0 q ∧
      varianceDerivative a0 q (turningPoint a0 q) = 0 := by
  constructor
  · unfold turningPoint EconCSLib.affineCutoff
    exact div_pos (sub_pos.mpr ha0) (mul_pos (by norm_num) hq)
  · unfold turningPoint EconCSLib.affineCutoff varianceDerivative
    field_simp [ne_of_gt hq]
    ring

/-- The affine derivative is positive exactly to the right of its turning
point. This is the additional endpoint condition omitted from the paper. -/
theorem varianceDerivative_pos_iff_turningPoint_lt
    (a0 q theta : ℝ) (hq : 0 < q) :
    0 < varianceDerivative a0 q theta ↔
      turningPoint a0 q < theta := by
  unfold varianceDerivative turningPoint EconCSLib.affineCutoff
  have hden : 0 < 2 * q := mul_pos (by norm_num) hq
  constructor
  · intro h
    apply (div_lt_iff₀ hden).2
    nlinarith
  · intro h
    have hmul := (div_lt_iff₀ hden).1 h
    nlinarith

/-- In particular, positivity at `θ = 1` is equivalent to the turning point
lying strictly below one. -/
theorem varianceDerivative_at_one_pos_iff
    (a0 q : ℝ) (hq : 0 < q) :
    0 < varianceDerivative a0 q 1 ↔ turningPoint a0 q < 1 := by
  simpa using varianceDerivative_pos_iff_turningPoint_lt a0 q 1 hq

/-- A negative intercept and a positive slope alone do not imply that the
derivative is positive at tool quality one. -/
theorem negativeIntercept_not_enough_at_one :
    ∃ a0 q : ℝ,
      a0 < 0 ∧ 0 < q ∧ varianceDerivative a0 q 1 < 0 := by
  refine ⟨-4, 1, ?_, ?_, ?_⟩ <;>
    norm_num [varianceDerivative]

/-- If gain variance is `q θ²` with `q > 0`, it is strictly increasing between
two nonnegative tool-quality levels. -/
theorem gainVariance_strictMono
    (q theta₁ theta₂ : ℝ)
    (hq : 0 < q) (h₁ : 0 ≤ theta₁) (hθ : theta₁ < theta₂) :
    gainVariance q theta₁ < gainVariance q theta₂ := by
  unfold gainVariance
  have h₂ : 0 < theta₂ := lt_of_le_of_lt h₁ hθ
  have hsquare : theta₁ ^ 2 < theta₂ ^ 2 := by
    nlinarith
  exact mul_lt_mul_of_pos_left hsquare hq

/-- Exact audit of the two-skill counterexample used in the validation report.
It satisfies the paper's negative-intercept condition but has a negative
variance derivative at `θ = 1`; its turning point is `12/5 > 1`. -/
theorem exact_counterexample :
    let a0 : ℝ := -(8 / 15)
    let q : ℝ := 1 / 9
    a0 < 0 ∧
      0 < q ∧
      varianceDerivative a0 q 1 = -(14 / 45) ∧
      turningPoint a0 q = 12 / 5 ∧
      1 < turningPoint a0 q := by
  norm_num [varianceDerivative, turningPoint, EconCSLib.affineCutoff]

end

end AGG25BicyclesForMind
