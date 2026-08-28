# Repository 2 - Agrawal, Gans & Goldfarb (2025)

**Paper:** *The Economics of Bicycles for the Mind*, NBER Working Paper 34034

**Status:** theoretical working paper, circulated for discussion and not peer reviewed.

**Source:** [NBER paper page](https://www.nber.org/papers/w34034) · [DOI](https://doi.org/10.3386/w34034)

> The headline is not “AI makes inequality U-shaped.” The precise object is the
> **cross-sectional variance of continuation values** as tool quality changes, and
> the claimed U-shape needs both a heterogeneity inequality and an interior-solution
> argument. The paper establishes the first condition but overstates the second.

## What question does the paper answer?

When a cognitive tool makes implementation easier, how does it change human effort,
productivity, and inequality - and which human abilities does it replace or amplify?

The paper separates three abilities that are usually bundled together:

- **implementation skill** $s$: turning effort into a successful improvement;
- **payoff judgment** $\alpha$: knowing which action creates value in a given state;
- **opportunity judgment** $(\gamma_0,\gamma)$: noticing an initial or subsequent
  opportunity to improve the task.

The answer is conditional. A cognitive tool substitutes for implementation effort and
skill, always raises the optimized net value under the paper's definition, and amplifies
opportunity judgment. Its interaction with payoff judgment is ambiguous in the general
model. Consequently, average productivity rises, while inequality can fall or rise
depending on the distributions of skill and judgment and on tool quality.

## The agent's problem

Conditional on noticing an opportunity in round $t$, the agent chooses effort:

$$
e_t^*(\theta)\in\arg\max_{e_t\ge 0}
M(e_t;\theta),\qquad
M(e_t;\theta)=p(se_t;\theta)\alpha\Delta-c(e_t;\theta).
$$

The general assumptions are $p_e\ge0$ and weak concavity, $c_e\ge0$ and weak
convexity, $\alpha\in(0,1]$, $s\in(0,1]$, $\Delta>0$, and a cognitive tool
$\theta$ that weakly raises $p$, weakly lowers $c$, and strictly lowers the
marginal-benefit/marginal-cost ratio $p_e/c_e$. With $\gamma(0)=\gamma_0$,
$\gamma(t)=\gamma$ for $t>0$, and $\delta\gamma<1$,

$$
V(\theta)=\Gamma M(e^*(\theta);\theta),
\qquad \Gamma\equiv\frac{\gamma_0}{1-\delta\gamma}.
$$

## Main result: Proposition 3, with its conditions

Section 4 adds the functional forms

$$
p(se;\theta)=\sqrt{se+\theta},\qquad c(e)=e,
$$

assumes $\alpha,\gamma_0,\gamma,s$ are mutually independent with positive
support, and uses an interior solution. The first-order condition gives

$$
e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s},
\qquad
V(\theta)=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right).
$$

Define $\mu_s=E[s]$. The heterogeneity condition is

$$
\frac{E[\Gamma^2]}{E[\Gamma]^2}<\mu_sE[1/s]. \tag{H}
$$

Under the maintained interior formula, $E[V(\theta)]$ rises with $\theta$ and

$$
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=a_0+2\theta\operatorname{Var}(\Gamma/s),
$$

where

$$
a_0=\frac{\Delta^2E[\alpha^2]}{2}
\left(E[\Gamma^2]-E[\Gamma]^2\mu_sE[1/s]\right).
$$

Thus (H) implies $a_0<0$, strict convexity when
$\operatorname{Var}(\Gamma/s)>0$, and the unique algebraic turning point

$$
\theta^*=-\frac{a_0}{2\operatorname{Var}(\Gamma/s)}>0.
$$

**What is proved:** variance initially falls and the extrapolated interior
formula has a positive algebraic turning point. An economically valid U further
requires that this turning point lie inside the region where effort remains
interior.

**What is not implied by (H):** $d\operatorname{Var}(V)/d\theta>0$ at
$\theta=1$. That additionally requires $\theta^*<1$. The paper states the sign
at $\theta=1$ without this condition.

## This week's trap - audited

1. **Variance of what?** $\operatorname{Var}(V(\theta))$: cross-sectional wage
   or productivity inequality across heterogeneous agents, as a function of
   tool quality $\theta$. It is not uncertainty in the AI output.
2. **Unconditional?** No. The initial decline requires (H); a turn before a
   specified quality level also requires that the turning point lie below that
   level. The closed form further requires $e^*(\theta)>0$ agent by agent.
3. **Variance of the individual benefit?** Under the same interior formula,
   $B(\theta)=V(\theta)-V(0)=\theta\Gamma/s$, so
   $\operatorname{Var}(B(\theta))=\theta^2\operatorname{Var}(\Gamma/s)$ -
   monotonically increasing for $\theta>0$ whenever $\Gamma/s$ is heterogeneous.

## Where I did not believe the AI

The loose claim “wage variance is U-shaped in AI” is **incomplete**, and the
stronger claim in Proposition 3(b) that the derivative is positive at
$\theta=1$ is **not delivered by condition (H)**. The reproducible two-type
counterexample in [`sim.py`](sim.py) satisfies every listed distributional
condition and keeps effort interior on $[0,1]$, yet the variance derivative is
still negative at $\theta=1$.

There is a second domain problem: with $\theta\in[0,\infty)$, no finite $\Delta$
keeps $e^*(\theta)>0$ for all tool qualities. Once effort reaches the constraint
$e=0$, the paper's quadratic variance calculation is no longer the correct
global value function. See [`extra/tutorial-prop3.md`](extra/tutorial-prop3.md)
for the derivation and [`extensions.md`](extensions.md) for the corrected route.

## Repository map

| Path | Contents |
|---|---|
| [`prompts.md`](prompts.md) | Raw prompts and relevant answers, including the variance correction |
| [`extra/tutorial-prop3.md`](extra/tutorial-prop3.md) | Deep-dive tutorial in Spanish, from the model to Proposition 3 |
| [`extra/reading-roadmap.md`](extra/reading-roadmap.md) | Dependency map, notation guide, and rigorous reading order |
| [`sim.py`](sim.py) | Symbolic identities, counterexample, corner solution, and figures |
| [`figures/`](figures/) | Reproducible outputs from the audit |
| [`extensions.md`](extensions.md) | Precise extensions and what each changes |
| [`formal/Proposition3.lean`](formal/Proposition3.lean) | EconCSLib-checked algebraic core |
| [`formal/exact_audit.py`](formal/exact_audit.py) | Dependency-free rational audit of the counterexample |
| [`formal/VALIDATION_REPORT.md`](formal/VALIDATION_REPORT.md) | Claim ledger, build receipt, verdict, and formal boundary |
| [`hand/`](hand/) | Instructions and destination for the required handwritten photo |
| [`presentation.tex`](presentation.tex) / `presentation.pdf` | Five-minute Beamer deck |
| [`paper/`](paper/) | Citation and reproducible retrieval instructions; PDF not committed |

`hand/prop3-derivation.jpg` will show the FOC, the variance derivative, and the
missing $\theta^*<1$ condition. It must be a real phone photo added by the student.
