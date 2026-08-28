# Formal validation boundary

The algebraic core of Proposition 3 is now machine-checked against
[EconCSLib](https://github.com/nikhgarg/EconCSLib).

## Checked claims

`Proposition3.lean` proves:

- the interior effort candidate is positive exactly under the paper's
  individual interiority inequality;
- substitution of the candidate satisfies the cleared first-order condition;
- the candidate and first-order root give the reported interior value;
- the individual gain equals `theta Gamma / s`;
- condition (30) is equivalent to a negative moment gap and implies the
  negative intercept in equation (83) under positive payoff moments;
- a negative variance-derivative intercept and positive slope give a unique
  positive turning point;
- the derivative is positive at `theta = 1` exactly when that turning point is
  below one;
- the paper's listed sign conditions do not imply the endpoint claim;
- gain variance is strictly increasing over nonnegative tool quality;
- the rational two-type counterexample has derivative `-14/45` at one and
  turning point `12/5`.

`exact_audit.py` independently checks the source assumptions, interiority,
value substitution, moments, endpoint sign, and both variance objects using
`fractions.Fraction`. It has no third-party dependencies.

## Reproduce

Using an EconCSLib checkout with its pinned dependencies:

```text
lake env lean <path-to-this-repository>/formal/Proposition3.lean
python <path-to-this-repository>/formal/exact_audit.py
```

Checked environment:

```text
Lean 4.30.0-rc2
EconCSLib checkout cf500b748ac63dbff55faf97d989d4935c8eff50
EconCSLib package  95fdc7dc863ff83e9d6c3a68fcb2505540462a4d
Mathlib package    5450b53e5ddc75d46418fabb605edbf36bd0beb6
```

## Deliberate boundary

This is not a formalization of the whole economics paper. The probability
space, independence-to-moment derivation, constrained global optimization, and
Propositions 1, 2, 4, and 5 remain outside Lean. See
`VALIDATION_REPORT.md` for the source-to-formalization ledger and exact verdict.
