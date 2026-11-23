# Repository 2 — Agrawal, Gans & Goldfarb (2025)

**Paper:** [*The Economics of Bicycles for the Mind*](https://www.nber.org/papers/w34034), NBER Working Paper 34034 ([DOI](https://doi.org/10.3386/w34034)); circulated for discussion, not peer reviewed.

## Question, mechanism, and agent

How does a cognitive tool change effort, productivity and inequality when people differ in **implementation skill** \(s\), **payoff judgment** \(\alpha\), and **opportunity judgment** \((\gamma_0,\gamma)\)? A tool substitutes for human execution effort while amplifying the value of recognizing improvement opportunities. Its complementarity with payoff judgment is conditional.

For each identified opportunity, with improvement \(\Delta>0\) and tool quality \(\theta\), the agent chooses \(e\ge0\):

\[
M^*(\theta)=\max_{e\ge0}\{p(se;\theta)\alpha\Delta-c(e;\theta)\},\qquad
V(\theta)=\Gamma M^*(\theta),\quad
\Gamma=\frac{\gamma_0}{1-\delta\gamma}.
\]

Here \(p\) is the implementation-success function, \(c\) is effort cost, and the opportunity multiplier is finite when \(\delta\gamma<1\).

## Variance result: assumptions and precise interpretation

**Specialization audited here:** \(p(se;\theta)=\sqrt{se+\theta}\), \(c(e)=e\), positive \(\alpha,s,\Gamma\), mutually independent \((\alpha,\gamma_0,\gamma,s)\), \(\Delta>0\), \(\delta\gamma<1\), and the required finite moments. The closed form applies **only at a common interior optimum**, \(\theta<\alpha^2\Delta^2s^2/4\) for every type:

\[
e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s},\qquad
V(\theta)=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right).
\]

Let \(q=\operatorname{Var}(\Gamma/s)\) and \(\mu_s=E[s]\). Direct variance algebra gives

\[
\operatorname{Var}'(V(\theta))=a_0+2\theta q,\quad
a_0=\frac{\Delta^2E[\alpha^2]}2
\left(E[\Gamma^2]-E[\Gamma]^2\mu_sE[1/s]\right).
\]

The heterogeneity inequality \(E[\Gamma^2]/E[\Gamma]^2<\mu_sE[1/s]\) gives \(a_0<0\): initial **level** variance decreases. With \(q>0\), the algebraic turning point is \(\theta^*=-a_0/(2q)>0\); a **positive slope at \(\theta=1\)** additionally requires \(\theta^*<1\) and a valid common interior region there. Distinctly, the variance of **individual gains** equals \(\theta^2q\) while interior. This is not a universal U-shaped inequality theorem.

## Original-paper verification: three specific gaps

The July 2025 PDF now has been **read directly**, not inferred from
a secondary description (printed pp. 12, 18 and 38–42).
Proposition 3(b), eq. (32), asserts a positive variance slope
at \(\theta=1\), but its proof (81) only establishes \(a_0<0\):
one must additionally check \(\theta^*<1\).
The printed interiority bound \(\Delta>2/(s\sqrt\alpha)\)
does not guarantee \(e^*(1)>0\) (which needs
\(\Delta>2/(s\alpha)\)). Finally, \(p(se;1)=\sqrt{se+1}>1\)
for \(e>0\), conflicting with the source's probability bound.
See the [primary-PDF audit, with exact page citations](SOURCE_AUDIT.md).

## Independent check, evidence, and reproduction

The [handwritten four-page proof](hand/prop3-handwritten-full.pdf) and [slide image](hand/prop3-derivation.jpg) check an algebraic two-type example with \(\operatorname{Var}'(1)=-14/45\). Its fitted \(\sqrt{se+\theta}\) exceeds 1, however, so it is **not a calibrated probability example**. Our [separate capped-probability extension](extra/bounded-probability-variant.md) is analyzed and tested independently.

[Raw AI exchanges](prompts.md) · [Full analysis](extra/full-analysis.md) · [Source-verification ledger](SOURCE_AUDIT.md) · [Audit](AUDIT.md) · [Simulations](sim.py) · [Lean algebra](formal/Proposition3.lean) · [Beamer source](presentation.tex) · [5-page PDF](presentation.pdf).

Run `python -m unittest discover -s tests -v`; figures: `python sim.py` and `python bounded_model.py`. The instructor has access to this repository.
