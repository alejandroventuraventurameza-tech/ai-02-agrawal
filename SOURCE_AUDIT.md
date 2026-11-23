# Direct primary-source audit — Agrawal, Gans & Goldfarb (2025)

**Source actually examined:** the user supplied the **53-page July 2025**
PDF of *The Economics of Bicycles for the Mind*, NBER WP 34034,
on 23 November 2026. PDF SHA-256:

\`11b8f4eda55480fcb1eaf4ee42598ce9c6640da535ed0fa551fc7597ee7bae8d\`

File size: **456,249 bytes**; 53 pages. The title page identifies
Ajay K. Agrawal, Joshua S. Gans and Avi Goldfarb, July 2025.
The third-party copyright-protected PDF is **not republished** in this
public repository. Publisher record:
[working paper 34034](https://www.nber.org/papers/w34034);
[direct original PDF](https://www.nber.org/system/files/working_papers/w34034/w34034.pdf).
**Pages below refer to printed numbers** (printed p. 18 = PDF page 19);
later editions may have different pagination.

## Source-to-claim ledger

| Printed pages | What was inspected | Verification |
| --- | --- | --- |
| 12–13 | \(p(se;\theta)\in[0,1]\), \(\alpha\) as payoff-judgment probability, \(s\in(0,1]\), \(\theta\ge0\); cognitive-tool Definition 1 (monotone success/cost and strictly decreasing marginal ratio) | Text verified |
| 14; Appendix A.1, 34–35 | Proposition 1: effort falls, per-period effort is stationary, continuation value rises | Statement/proof location checked; not Lean-formalized |
| 16; Appendix A.2, 36–37 | Proposition 2: judgment complementarities and skill/timing effects | Statement/proof location checked; not Lean-formalized |
| 17–18 | Section 4 square-root specialization; independence, positive supports, \(\mu_i>3\sigma_i\); \(\Delta>2/(s\sqrt\alpha)\) | Exact printed restrictions verified |
| 18 | Heterogeneity (30), mean (31), variance signs (32), turning point (33) | **Exact proposition statement** verified |
| 38–39 | First-order condition (57), effort (58), value (59)–(60), variance setup (64)–(67) | Algebra checked |
| 40–41 | Variance expansion (68)–(83), linear derivative (81), curvature (84) | Algebra checked |
| 42 | Turning-point proof (85)–(94) | Algebra checked; its location relative to 1 is not established |

## Finding 1 — Equation (32) asserts an endpoint sign not implied by (30)

The *published* Proposition 3(b), printed p. 18, says that when
\[
\frac{E[\Gamma^2]}{(E[\Gamma])^2}<E[s]E[1/s] \tag{30}
\]
then \(\operatorname{Var}'(V(0))<0\) **and**
\(\operatorname{Var}'(V(1))>0\), equation (32).

The paper's *own* Appendix A.3, printed p. 41, proves equation (81):
\[
\operatorname{Var}'(V(\theta))=a_0+2\theta q,\quad
q=\operatorname{Var}(\Gamma/s)>0,
\]
\[
a_0=\frac{\Delta^2E[\alpha^2]}2
\{E[\Gamma^2]-(E[\Gamma])^2E[s]E[1/s]\}.
\]
The restriction (30) implies \(a_0<0\), **not**
\(a_0+2q>0\). The latter requires
\[
\boxed{\theta^*=-a_0/(2q)<1}
\]
as well as validity of the common interior solution at \(\theta=1\).
The proof (pp. 41–42) establishes \(\theta^*>0\), not
\(\theta^*<1\). Thus a precise **source-confirmed missing
sufficient-condition implication** is present.

Algebraic witness: equally likely \(s\in\{3/5,1\}\),
\(\alpha=\Gamma=1\), \(\Delta=4\) yields
\(E[s]E[1/s]=16/15>1\), \(a_0=-8/15\),
\(q=1/9\), \(\theta^*=12/5\) and
\(\operatorname{Var}'(V(1))=-14/45\).
This satisfies the paper's **printed heterogeneity and
interiority inequalities**, but its fitted success index exceeds
one; it is **not** a complete probability-admissible countermodel.
The logical gap in the algebra should not be conflated with
consistency of all probability primitives.

## Finding 2 — The printed effort-positivity condition is insufficient

Printed pp. 18 and 39 explicitly state
\[
\Delta>\frac{2}{s\sqrt{\alpha}}
\]
as an effort-positivity restriction. But equation (58) is
\(e^*(\theta)=\alpha^2\Delta^2s/4-\theta/s\), hence
\[
e^*(1)>0\iff \Delta>\frac{2}{s\alpha}.
\]
For \(0<\alpha<1\), the printed restriction is weaker.
**Exact witness:** with \(\alpha=1/4\), \(s=1\),
\(\Delta=5\), the original inequality \(\Delta>4\) holds,
yet \(e^*(1)=-39/64<0\), since the necessary
threshold is \(\Delta>8\). This is a separate
source-verified domain error.

## Finding 3 — Success probability and square-root domain conflict

The general model defines \(p(se;\theta)\in[0,1]\) on
printed p. 12. Section 4 uses
\[
p(se;\theta)=\sqrt{se+\theta}
\]
on printed p. 17. At \(\theta=1\), any \(e>0\)
and \(s>0\) imply
\(\sqrt{se+1}>1\), violating the stipulated probability
bound. For \(\theta>1\), even \(e=0\) gives a value above one.

Moreover, equation (58)'s **positive** effort at \(\theta=1\)
requires \(\alpha\Delta s>2\); the interior FOC implies
\(p^*=\alpha\Delta s/2>1\). Thus no positive-effort
interior regime at quality one can satisfy this original
literal probability specification. The original algebra
can be interpreted as an unbounded success *index*,
but that is a different primitive from a probability.

## What remains valid, and what is not claimed

The effort FOC, interior value and variance polynomial
are valid **as algebra** on their common interior region.
The initial variance decline under (30), and a positive
*algebraic* turning point, are established. The endpoint
sign at one is not a consequence of (30) alone;
the variance of individual gains
\(\theta^2\operatorname{Var}(\Gamma/s)\) is a
different object from level inequality.

[Our separate capped variant](extra/bounded-probability-variant.md)
\(p=\min\{1,\sqrt{se+\theta}\}\) restores the bound,
but creates a kink and a flat region. It does **not**
automatically satisfy the original smooth and strict
marginal-ratio assumptions, so we do not call it a
counterexample to *all* hypotheses of the original theorem.

Exact necessary-condition regressions are in
[tests/test_source_conditions.py](tests/test_source_conditions.py);
the six existing Lean lemmas prove only their encoded algebra.
We have checked the **primary text** for the model,
Propositions 1–3 and Appendix A.1–A.3, but have **not**
formally reproved every claim in the 53-page manuscript or
received any author-issued correction. The instructor has
approved the student's deadline extension and digital handwriting.
