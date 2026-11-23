# Issue #1: follow-up audit and release boundaries

Date: 2026-11-22. This note documents checks without claiming a
retroactive or complete submission.

## Demonstrated

- The independent two-type calculation is exact: (H) holds
  (\(1<16/15\)), the interior region contains \([0,1]\), and
  \(d\operatorname{Var}(V)/d\theta|_{\theta=1}=-14/45\).
- The quadratic extrapolation turns at \(12/5=2.4\), **beyond** the first
  effort corner \(36/25=1.44\); that extrapolated turning point alone
  is not a turning point of the globally constrained model.
- In the interior region, the individual-benefit variance equals
  \(\theta^2\operatorname{Var}(\Gamma/s)\).
- At the interior candidate, \(p^*=\alpha\Delta s/2\). In this example
  \(p^*\in\{6/5,2\}\), which exceeds one. The counterexample concerns
  the paper's algebraic specification, **not** a bounded probability
  implementation. A literal \(p\le1\) would require separate treatment.

Reproduce without extra packages:

    python -m unittest discover -s tests -v

The existing simulation and figure use NumPy and Matplotlib:

    python -m pip install -r requirements.txt
    python sim.py --no-plot
    python sim.py

## Presentation

Source: \`presentation.tex\`. Generated output: \`presentation.pdf\`.
The follow-up GitHub Action runs exact-rational tests, compiles the five-slide
Beamer deck, and commits the resulting PDF on the audit branch when writable.
The PDF must be checked against the latest source before merging.

## Not certified

- **Handwritten evidence:** \`hand/prop3-derivation.jpg\` is not present.
  Only a genuinely handwritten photograph supplied by the student can
  satisfy that requirement; a typeset equation or AI image cannot.
- **Lean:** \`formal/Proposition3.lean\` is an EconCSLib-compatible *draft*.
  It has not been compiled here; no formal proof certificate is asserted.
- **Source verification:** the original NBER working-paper text requires a
  page-by-page primary-document check when accessible, especially the precise
  domain assumptions on \(p\) and \(\theta\).
- **Instructor access:** the repository is private. The course guide allows
  private repositories only when the instructor has read access; this
  connection does not expose collaborator invitations.
- **Deadline:** the August 25, 2026 submission time is historical and cannot
  be reconstructed by a later PR or issue comment.

The preceding statements deliberately distinguish exact algebraic proof,
reproducible numerical code, and outstanding evidence.
