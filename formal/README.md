# Formal verification boundary

`Proposition3.lean` is a small EconCSLib-compatible check of the algebraic core:

- a negative derivative intercept plus positive slope gives a positive unique
  turning point;
- a negative intercept alone does **not** imply a positive derivative at
  `theta = 1`;
- the variance of the individual gain is increasing for positive tool quality.

It deliberately does not claim to formalize the whole economics paper. A full
formalization would also have to encode random variables, independence,
integrability, the constrained optimization problem, and the source-to-Lean
translation ledger.

To check it with [EconCSLib](https://github.com/nikhgarg/EconCSLib), copy the file
into an EconCSLib checkout (for example under `papers/AGG25BicyclesForMind/`),
retain `import EconCSLib`, and run `lake env lean Proposition3.lean` or register
the file in that project's Lake build.

Status in this repository: the source is prepared for the package; the checked
mathematical evidence currently comes from the exact symbolic and numerical
audit in `sim.py`. A successful Lean build receipt should be added before
claiming machine-checked formalization.

