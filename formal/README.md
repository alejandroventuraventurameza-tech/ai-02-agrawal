# Lean 4 verification: algebraic scope, not the entire economics model

This folder contains `Proposition3.lean`, a compilation-targeted
formalization of **only the real-number algebra downstream of the variance
identity** in Agrawal, Gans & Goldfarb (2025), Proposition 3.

## Toolchain

- Lean: `v4.30.0-rc2` (pinned by `lean-toolchain`).
- Mathlib: `v4.30.0-rc2` (pinned in `lakefile.toml`).
- The suggested **EconCSLib** project was renamed
  [AppliedModelingLib](https://github.com/nikhgarg/AppliedModelingLib),
  whose November 2026 upstream toolchain and Mathlib release use this version.
  The file imports Mathlib directly, not the renamed project's broad facade,
  to avoid claiming the entire external library was built or tested.
- GitHub Actions `.github/workflows/issue-1-lean.yml` is the independent
  Lean compilation receipt. The final status must be read from that CI run,
  not inferred from the fact that the source file exists.

Run (after installing elan and Lake):

```bash
lake update
lake exe cache get
lake env lean formal/Proposition3.lean
```

## What is and is not checked

| Object | Lean status |
| --- | --- |
| Negative derivative intercept + positive quadratic coefficient gives positive root | Encoded as a theorem |
| Negative intercept does not imply derivative positive at one | Encoded as a theorem |
| Increasing `q theta^2` for `q>0`, `theta>=0` | Encoded as a theorem |
| Exact rational counterexample derivative and effort-corner order | Encoded as theorems |
| Square-root success index exceeding one in the illustrative case | Encoded as a theorem |
| Source-to-formalized equivalence for independence, expectations, and the variance identity | **Not formalized** |
| Original constrained optimization problem, unique optimizer, and full economic propositions | **Not formalized** |

A passing Lean run certifies the statements *as encoded*, not their
interpretation or equivalence to all statements in the source PDF. Checking the
latter requires a separate human source translation audit. No `sorry`,
`admit`, or fabricated proof certificate is permitted.
