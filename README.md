# Repository 2 — Agrawal, Gans & Goldfarb (2025)

**Paper:** [*The Economics of Bicycles for the Mind*](https://www.nber.org/papers/w34034), NBER Working Paper 34034, DOI [10.3386/w34034](https://doi.org/10.3386/w34034). This is an **unrefereed working paper**, not a peer-reviewed journal article.

## Question and economic mechanism

When cognitive tools make task implementation easier, which human capabilities do they replace or amplify, and what happens to effort, productivity, and inequality?

Three capabilities play separate roles: implementation skill \(s\), payoff judgment \(\alpha\), and opportunity judgment \((\gamma_0,\gamma)\). Conditional on identifying an improvement opportunity, the agent chooses effort \(e\ge0\):

\[
e^*(\theta)\in\arg\max_{e\ge0}
\{p(se;\theta)\alpha\Delta-c(e;\theta)\},\qquad
V(\theta)=\underbrace{\frac{\gamma_0}{1-\delta\gamma}}_{\Gamma}
\,M(e^*(\theta);\theta).
\]

The general analysis assumes increasing, weakly concave implementation success; increasing, weakly convex effort cost; \(\Delta>0\); \(\alpha,s>0\); \(\delta\gamma<1\); and a tool that improves success and/or reduces cost while reducing the marginal return-to-cost ratio for human implementation effort. The mechanism is substitution of execution effort combined with amplification of opportunity judgment.

## Proposition 3: exact conditions and qualification

For the Section 4 algebra, \(p(se;\theta)=\sqrt{se+\theta}\), \(c(e)=e\), mutually independent positive \((\alpha,\gamma_0,\gamma,s)\), and finite required moments. **Only where the solution remains interior**, \(\theta<\alpha^2\Delta^2s^2/4\) for every type, does the closed form hold:

\[
e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s},\qquad
V(\theta)=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right).
\]

Let \(\mu_s=E[s]\) and \(q=\operatorname{Var}(\Gamma/s)\). Under independence,

\[
\frac{d\operatorname{Var}(V)}{d\theta}
=a_0+2\theta q,\quad
a_0=\frac{\Delta^2E[\alpha^2]}2
\left(E[\Gamma^2]-E[\Gamma]^2\mu_sE[1/s]\right).
\]

The paper's heterogeneity inequality
\(E[\Gamma^2]/E[\Gamma]^2<\mu_sE[1/s]\)
implies \(a_0<0\). If \(q>0\), the **algebraic** turning point is
\(\theta^*=-a_0/(2q)>0\). A positive derivative at \(\theta=1\) **additionally** requires \(\theta^*<1\), and that point must remain interior. This is a conditional result about **cross-sectional variance of total value**, not variance of AI predictions. Separately, individual gains \(B(\theta)=V(\theta)-V(0)\) satisfy \(\operatorname{Var}(B(\theta))=\theta^2q\) in the same interior region.

## Independent audit and extension

With equal weights on \(s\in\{3/5,1\}\), \(\Gamma=\alpha=1\), and \(\Delta=4\), the heterogeneity inequality holds (\(1<16/15\)); effort stays interior on \([0,1]\); yet
\(\operatorname{Var}'(V)|_{\theta=1}=-14/45<0\).
The first effort corner is \(36/25\), before the extrapolated turning point \(12/5\). **Important:** this is a counterexample to the *algebraic sign inference*, not a literal calibrated probability model: the success index at the FOC equals \(p^*\in\{6/5,2\}>1\).

An additional exact calculation shows that, with effort constrained to be nonnegative, the **algebraic** total-value variance in this example decreases to zero rather than becoming U-shaped. The variance of individual gains instead increases and plateaus. Proof and limitations: [AUDIT.md](AUDIT.md) and [the Spanish tutorial](extra/tutorial-prop3.md).

## A probability-admissible extension (new result)

We separately study **a modified primitive**, not the paper's original
Proposition 3: \(p(se;\theta)=\min\{1,\sqrt{se+\theta}\}\),
\(c(e)=e\), \(\alpha=\Gamma=1\), \(\Delta=2\), and equally likely
\(s\in\{3/5,1\}\). The cap guarantees \(0\le p\le1\).
The optimized value gap becomes

\[
D(\theta)=V_H(\theta)-V_L(\theta)=
\begin{cases}
2/5-2\theta/3,&0\le\theta\le9/25,\\
(1-\sqrt{\theta})^2,&9/25\le\theta\le1,\\
0,&\theta\ge1.
\end{cases}
\]

Thus level variance \(D^2/4\) falls from \(1/25\) to zero, whereas
gain variance \((D-2/5)^2/4\) rises from zero to \(1/25\).
The **analytic proof**, full domain qualifications and reproducible figure
are in [the capped-probability extension](extra/bounded-probability-variant.md)
and [\`bounded_model.py\`](bounded_model.py). The probability cap
introduces a kink: we do **not** claim it preserves the paper's globally
strict tool definition at saturation.

## Reproduce and inspect

```bash
python -m unittest discover -s tests -v
python -m pip install -r requirements.txt
python sim.py
python bounded_model.py
pdflatex -interaction=nonstopmode -halt-on-error presentation.tex
```

- [Handwritten verification guide](hand/derivation-guide.md) · [Raw interactions](prompts.md) · [Numerical code](sim.py) · [Full figure](figures/prop3-variance-audit.png) · [Slide preview](preview/beamer-contact-sheet.png).
- [Lean algebraic proofs](formal/Proposition3.lean): six statements **compiled without `sorryAx`** ([CI certificate](https://github.com/alejandroventuraventurameza-tech/ai-02-agrawal/actions/runs/45104051271)); not a proof of the full economic model.
- [Five-minute Beamer](presentation.tex) and [compiled PDF](presentation.pdf) (title + four slides).
- **Required human evidence still missing:** a genuine photograph `hand/prop3-derivation.jpg`; see [instructions](hand/README.md). No fabricated handwriting is included.
- Repository is private; ensure instructor `alexanderquispe` has read access before registering the link. The original August 25, 2026 deadline is historical and cannot be changed.
