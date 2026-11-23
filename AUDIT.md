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

Source: `presentation.tex`. Generated output: `presentation.pdf`.
The follow-up GitHub Action runs exact-rational tests, compiles the five-slide
Beamer deck, and commits the resulting PDF on the audit branch when writable.
The PDF must be checked against the latest source before merging.


## Exact additional result: effort constraint, two types

This is **our calculation**, not a claim that the authors proved a global
monotonicity theorem. The example is algebraic and its success index is not
bounded by one.

With \(\Gamma=\alpha=1\), \(\Delta=4\), equal weights on
\(s_L=3/5\), \(s_H=1\), and effort constrained by \(e\ge0\), the
effort corner is at \(\theta_s=4s^2\). The value gap between high and
low skill is therefore

\[
D(\theta)=V_H(\theta)-V_L(\theta)=
\begin{cases}
8/5-2\theta/3,&0\le\theta\le36/25,\\
4+\theta-4\sqrt\theta=(\sqrt\theta-2)^2,&36/25\le\theta\le4,\\
0,&\theta\ge4.
\end{cases}
\]

The pieces match at \(\theta=36/25\), where \(D=16/25\), and
at \(\theta=4\), where \(D=0\). On the first interval \(D'=-2/3\).
On the second \(D'=1-2/\sqrt\theta\le0\). Thus \(D\) is
nonnegative and nonincreasing everywhere. Since types have equal weights,

\[
\operatorname{Var}(V(\theta))=\frac{D(\theta)^2}{4}
\]

is nonincreasing, strictly decreasing up to \(\theta=4\), then zero.
Meanwhile the within-person gains relative to \(\theta=0\) have gap
\(D(\theta)-8/5\), so

\[
\operatorname{Var}(V(\theta)-V(0))
=\frac{(8/5-D(\theta))^2}{4}
\]

is nondecreasing, reaching \(16/25\) and then constant for
\(\theta\ge4\). This maintains the vital distinction between level
inequality and the dispersion of individual gains beyond the common
interior region.

**Non-claim:** these are not global inequalities for a bounded
probability of success. Their source function \(\sqrt{se+\theta}\)
can exceed one. Any repaired probability model must be re-analysed
from its altered primitive.

## The actual AI answer I disputed (slide 4)

In prompts.md, the assistant answered "Yes" when asked for a
counterexample satisfying every listed condition. Its calculations of
heterogeneity, interiority and the sign at theta=1 were algebraically
correct, but it did not check the bounded-probability interpretation
of the primitive success function. At the FOC, p*=2s is either 6/5 or
2, exceeding one. The claimed counterexample is therefore invalid
as a literal probability model even though it refutes an algebraic
sign inference.

We do not invent a raw unconditional U-shaped AI statement:
the logged answer to that separate question was already nuanced.

## Verified Lean certificate (2026-11-22)

[GitHub Actions run 45104051271](https://github.com/alejandroventuraventurameza-tech/ai-02-agrawal/actions/runs/45104051271) returned **success** for `formal/Proposition3.lean` at revision `df2b7d81023b78626238935a2727ff8f2c9b04ce`, with Lean `4.30.0-rc2` and pinned Mathlib. All six `#print axioms` outputs contain only `propext`, `Classical.choice`, and `Quot.sound`; none contains `sorryAx`. This is a formal certificate for the encoded *algebraic lemmas only*, not the full published proposition or the validity of the probability primitive.

## Separate bounded-probability extension (2026-11-22)

We constructed a **new** model with \(p=\min\{1,\sqrt{se+\theta}\}\),
\(\Delta=2\), \(\alpha=\Gamma=1\), and the same two skill types.
Its closed-form optimizer is \(e^*=\max\{s-\theta/s,0\}\).
For \(\theta\ge1\), the success cap binds at zero effort.
The exact high-minus-low gap is

\[
D(\theta)=
\begin{cases}
2/5-2\theta/3,&0\le\theta\le9/25,\\
(1-\sqrt\theta)^2,&9/25\le\theta\le1,\\
0,&\theta\ge1.
\end{cases}
\]

Consequently \(\operatorname{Var}(V)=D^2/4\) decreases from \(1/25\)
to zero while the variance of individual gains
\((D-2/5)^2/4\) increases from zero to \(1/25\).
The monotonicity is established by differentiating the pieces;
sample-point tests are corroboration, not the proof. The new
cap changes the differentiability and strict-substitution assumptions
and is not equivalent to the original published functional form.
See \`extra/bounded-probability-variant.md\`.

## Primary-source verification boundary

The publisher's [NBER page](https://www.nber.org/papers/w34034)
confirms the 2025 working-paper citation and broad theoretical mechanism.
The direct NBER 53-page PDF endpoint did not provide accessible content
in this session. The
[SSRN NBER listing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5350364)
reports a revision on 2026-06-29; the course issue refers to the
July 2025 teaching version. Accordingly, we have **not** certified
a page-by-page source audit or assumed these two versions have identical
equation/footnote numbering. Our mathematical conclusions are explicitly
conditional on the functional forms transcribed in the repository.

## Reproduction certificate: bounded variant

[GitHub Actions #45111360008](https://github.com/alejandroventuraventurameza-tech/ai-02-agrawal/actions/runs/45111360008) completed successfully on the capped-model code at commit `a18e286f69cda9759b2a0e2f5ff2102f8963308a`. Its Python stage reported **10 passing tests**, including exact-rational checks of all three capped-model regions. The script checked numerical agreement of the level/gain variance curves with the analytical functions, and the Beamer workflow produced a verified **five-page PDF** and the regenerated chart. These are numerical/reproducibility receipts; the monotonicity argument depends on the separate analytic proof, not on sampling alone.

## New authentic handwritten evidence received (23 November 2026)

The user supplied `ai-02.pdf`, four pages of handwritten mathematical work.
We preserved the **original uploaded PDF bytes**, renamed only to
`hand/prop3-handwritten-full.pdf`. For slide 4 we rendered original
PDF page 4 directly to `hand/prop3-derivation.jpg` with no generated
handwriting, added annotations or content changes.

- **Page 1:** \(M(e)=\alpha\Delta\sqrt{se+\theta}-e\); FOC,
  \(e^*=\alpha^2\Delta^2 s/4-\theta/s\); interiority bound.
- **Page 2:** \(M^*=\alpha^2\Delta^2s/4+\theta/s\),
  \(V=\Gamma M^*\) and variance decomposition \(V=X+\theta Y\).
- **Page 3:** \(\operatorname{Var}'(V)=a_0+2\theta\operatorname{Var}(\Gamma/s)\);
  \(a_0<0\) only gives a positive algebraic turning point, and
  \(\operatorname{Var}'(1)>0\) would additionally require \(\theta^*<1\).
- **Page 4:** \(\alpha=1,\Delta=4,\Gamma=1,s\in\{3/5,1\}\),
  giving \(-8/15+2\theta/9\), turning point \(12/5\),
  derivative \(-14/45\) at \(\theta=1\).
  The author circles \(p^*\in\{6/5,2\}\) and explicitly notes
  that this violates the literal probability range \([0,1]\).

These steps are correct **inside the algebraic model's common
interior region**. The handwritten notes do not purport to prove
global validity under a bounded probability. The later capped
model remains a distinct extension.

PDF SHA-256: `f38c710d6099b81e6195667429f2369e7ac01f89e8f7d95129a8ded8141e71ee`.
JPEG SHA-256: `1eab251ec0a7825ce132d71e4cb627b6acc7c85bc23b878b4bc527089c9941a1`.

## Outstanding obligations

- **Handwritten evidence:** four-page user-supplied annotated manuscript stored as `hand/prop3-handwritten-full.pdf` and an image of page 4 stored as `hand/prop3-derivation.jpg`; both SHA-256 hashes are recorded in `hand/SHA256SUMS`. This is a rendered image of the original handwritten PDF, **not** an asserted camera photograph of paper. If the instructor requires a literal camera photograph, that separate condition must be checked.
- **Full-model Lean formalization:** six downstream algebraic theorems compile,
  but the original stochastic optimization, independence hypotheses, and
  source-to-Lean correspondence are **not formalized**.
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
