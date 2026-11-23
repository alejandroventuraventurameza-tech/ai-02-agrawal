# Extensions and reproducible findings

The useful extensions are the ones that change a named equation and can be
distinguished from repairs to the published derivation.

## 1. Repair before extension: impose the effort constraint globally

The Section 4 FOC gives an interior candidate, not the global solution. Replace

$$
e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}
$$

with

$$
e^*(\theta)=\max\left\{
\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s},0\right\}.
$$

This changes the value function to

$$
M^*(\theta)=
\begin{cases}
\alpha^2\Delta^2s/4+\theta/s,
& \theta<\alpha^2\Delta^2s^2/4,\\
\alpha\Delta\sqrt\theta,
& \theta\ge\alpha^2\Delta^2s^2/4.
\end{cases}
$$

**Expected result.** Skill types hit the zero-effort corner at different tool
qualities. The aggregate variance is no longer one global quadratic, so the
number and location of turning points become distribution-dependent.

This is a correction, not a new economic mechanism. It should be done before
claiming any global U-shape.

## 2. Correlated skill and judgment

The paper assumes mutual independence of $\alpha$, $\gamma_0$, $\gamma$, and
$s$. Relax this by specifying a joint distribution for $(\Gamma,\alpha,s)$.
The value equation is unchanged:

$$
V(\theta)=\Gamma\left(K\alpha^2s+\frac\theta s\right),
\qquad K=\Delta^2/4,
$$

but the derivative of the variance is most transparently written as

$$
\frac{d\operatorname{Var}(V)}{d\theta}
=2\operatorname{Cov}\left(\Gamma K\alpha^2s,\frac\Gamma s\right)
+2\theta\operatorname{Var}(\Gamma/s).
$$

**Expected result.** Positive correlation between opportunity judgment and
implementation skill can make the covariance term less negative or positive,
eliminating the initial equalising phase. Negative correlation can lengthen it.
This is empirically meaningful because expertise and judgment are unlikely to be
independent.

## 3. Replace variance with welfare-relevant inequality measures

The paper briefly discusses the coefficient of variation but Proposition 3 uses
absolute variance. Simulate:

- variance;
- coefficient of variation;
- log variance;
- Gini coefficient;
- percentile ratios.

**Equation changed.** Only the mapping from the cross-sectional distribution of
$V(\theta)$ to the inequality statistic changes.

**Expected result.** Since the mean increases with tool quality, absolute and
relative inequality can move in opposite directions. A verbal claim that “AI
increases inequality” is incomplete unless the measure is named.

## 4. Endogenize opportunity judgment

Currently $\Gamma=\gamma_0/(1-\delta\gamma)$ is an endowment. Let agents invest
in search or evaluation effort $j$:

$$
\max_{e,j\ge0}
\frac{\gamma_0(j,\theta)}{1-\delta\gamma(j,\theta)}
\left[p(se;\theta)\alpha\Delta-c(e;\theta)\right]-k(j).
$$

**Expected result.** If AI makes opportunities easier to recognize, human search
effort may fall even as the number of realized opportunities rises. This mirrors
the implementation-effort result and turns the paper's asserted complementarity
with opportunity judgment into an endogenous object.

## 5. Identification and measurement

The paper maps $\operatorname{Var}(V)$ to wage inequality without directly
observing the three capabilities. A useful empirical extension would use repeated
tasks with separate stages:

1. opportunity detection;
2. proposed action quality;
3. implementation quality;
4. randomized access to tool quality.

This design could identify proxies for $(\gamma,\alpha,s)$ and test whether the
independence assumption is even approximately true.

## Reproducible audit in `sim.py`

The script reports two findings that should not be conflated:

1. A two-type population satisfying the paper's heterogeneity condition and all
   listed support/moment restrictions can still have a **negative** derivative of
   wage variance at $\theta=1$; condition (30) does not imply the paper's second
   sign in equation (32).
2. In the interior region, the variance of the individual tool benefit is
   $\theta^2\operatorname{Var}(\Gamma/s)$ and therefore increases monotonically.

It also plots the constrained corner solution against the interior extrapolation
to show where the quadratic argument ceases to describe the model.

