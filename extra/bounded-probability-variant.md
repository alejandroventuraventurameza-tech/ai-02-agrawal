# Extension: a genuine probability bound changes the inequality path

**Scope:** an independent, exactly solvable **variant** of the model in
Agrawal, Gans and Goldfarb (2025), not a claim that their published Proposition 3
has been formally refuted. Unlike the original square-root *index*, this
variant has success probabilities in \([0,1]\) for every effort and quality.

## 1. Modified primitive and calibrated illustration

Keep the iterative opportunity interpretation but change one primitive:

\[
p(se;\theta)=\min\{1,\sqrt{se+\theta}\},\qquad c(e)=e,\qquad
\theta,e\ge0.
\]

Let \(\alpha=\Gamma=1\), \(\Delta=2\) and \(s\in\{3/5,1\}\) with equal
probability. The opportunity parameters can be chosen, e.g.,
\(\gamma_0=4/5\), \(\gamma=2/5\), \(\delta=1/2\), so that
\(\Gamma=\gamma_0/(1-\delta\gamma)=1\).

The objective for a type \(s\) is

\[
\max_{e\ge0} \quad
F(e;\theta,s)=2\min\{1,\sqrt{se+\theta}\}-e .
\]

This is a **bounded success probability**, even away from the optimizer.
The saturation kink at \(se+\theta=1\) means the original *globally strict*
marginal-substitution condition is not automatically preserved. We claim
a well-defined modified optimization problem, **not** equivalence to every
assumption in the source definition of a cognitive tool.

## 2. Global effort optimum (derivation)

For \(0\le\theta<1\), the unsaturated region is
\(0\le e\le(1-\theta)/s\), where

\[
F_e=\frac{s}{\sqrt{se+\theta}}-1,\qquad
F_{ee}=-\frac{s^2}{2(se+\theta)^{3/2}}<0
\]

away from its zero argument. The interior FOC yields
\(se+\theta=s^2\), hence \(e_{\mathrm{FOC}}=s-\theta/s\).
For \(\theta<s^2\), the candidate is positive and has \(p^*=s\le1\);
it lies in the unsaturated interval. On its right, the objective
eventually has slope \(-1\) once the cap binds, so this candidate is
the global maximizer. If \(s^2\le\theta<1\), the right derivative at
zero is nonpositive and concavity followed by the decreasing capped
branch implies \(e^*=0\).

For \(\theta\ge1\), the probability cap already binds at \(e=0\);
any positive effort only increases cost. Therefore, for all \(\theta\ge0\),

\[
\boxed{e^*(\theta,s)=\max\{s-\theta/s,0\}.}
\]

**Endpoint note:** at \(\theta=0\) and \(e=0\), the derivative is
singular, but the positive FOC solution remains a global optimum.
This does not invalidate the preceding value comparison.

## 3. Exact optimized value, skill gap, and variances

For \(0<s\le1\),

\[
v_s(\theta)=
\begin{cases}
s+\theta/s, & 0\le\theta\le s^2,\\
2\sqrt\theta, & s^2\le\theta\le1,\\
2, & \theta\ge1.
\end{cases}
\]

The pieces agree at the boundaries. The low-skill type stops
working at \(9/25=0.36\); the high-skill type stops at \(1\).
The high-minus-low value gap is

\[
\boxed{
D(\theta)=
\begin{cases}
\frac25-\frac{2\theta}{3}, & 0\le\theta\le\frac9{25},\\
(1-\sqrt\theta)^2, & \frac9{25}\le\theta\le1,\\
0, & \theta\ge1.
\end{cases}}
\]

On the first interval \(D'=-2/3\); on the second,
\(D'=1-1/\sqrt\theta<0\) for \(\theta<1\); thereafter \(D'=0\).
The gap is continuous, nonnegative and nonincreasing. With two types
of equal weight,

\[
\boxed{\operatorname{Var}[V(\theta)]=D(\theta)^2/4\quad
\text{decreases from }1/25\text{ to }0.}
\]

Now define the *individual benefit* \(B_s(\theta)=v_s(\theta)-v_s(0)\).
The across-person difference in benefits equals \(D(\theta)-D(0)\),
where \(D(0)=2/5\). Consequently,

\[
\boxed{\operatorname{Var}[B(\theta)]
=\frac{(D(\theta)-2/5)^2}{4}
\quad\text{increases from }0\text{ to }1/25.}
\]

Both variances are constant for \(\theta\ge1\). An initially
equalizing AI tool can therefore produce **more heterogeneous gains** while
producing **less heterogeneous final productivity levels**, even in a
probability-admissible illustration.

## 4. Relationship to the paper's Proposition 3

The original heterogeneity inequality remains numerically satisfied
because \(\Gamma=1\), \(E[s]=4/5\), \(E[1/s]=4/3\):

\[
\frac{E[\Gamma^2]}{E[\Gamma]^2}=1<
\frac45\frac43=\frac{16}{15}.
\]

In the *common interior segment* \(0\le\theta<9/25\), the same
quadratic variance algebra applies with \(\Delta=2\):
\(a_0=-2/15\), \(q=1/9\), algebraic turning point
\(\theta^*=3/5>9/25\). For instance, at \(\theta=3/10\),
both types are interior, \(p^*\in\{3/5,1\}\), and

\[
\operatorname{Var}'(V)|_{\theta=3/10}
=-\frac{2}{15}+\frac{2}{9}\frac{3}{10}
=-\frac1{15}<0.
\]

The behavior at \(\theta=1\) is **not** tested using the original
interior derivative: the low type is already at a corner.
Hence this extension does **not** establish a direct counterexample to
the exact published endpoint theorem under all its assumptions.

## 5. Reproduction and audit scope

Run from the repository root:

```bash
python -m unittest discover -s tests -v
python -m pip install -r requirements.txt
python bounded_model.py
```

Outputs: `figures/prop3-bounded-success.png`. Tests verify exactly
representable rational values across all three regions, the inequality
threshold and a sampled-grid cross-check of the optimizer.
The global monotonicity claims above rely on the **analytic derivative
proof**, not merely on a numerical grid.

**Proven by hand in this note:** the optimal effort and piecewise value,
the nonincreasing level variance and nondecreasing gain variance under
the stated modified primitives.

**Not proven:** full original paper model, its global strict
tool-complementarity conditions, or statistical representativeness of
two illustrative types. A NBER landing page is publicly verifiable,
but a page-by-page examination of the 53-page teaching-version PDF
was unavailable from the publisher endpoint during this audit.
