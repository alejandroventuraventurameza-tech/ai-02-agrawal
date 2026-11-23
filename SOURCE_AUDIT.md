# Primary-source and proposition audit — Repository 2

**Version targeted by course issue #1:** Agrawal, Gans and Goldfarb (2025), *The Economics of Bicycles for the Mind*, NBER Working Paper 34034, July 2025. The instructor identifies a **53-page teaching copy** at \`papers/05-agrawal-gans-goldfarb-2025-bicycles-for-the-mind.pdf\`. That file is **not available in the course Git history**: \`papers/.gitignore\` excludes locally downloaded PDFs.

## What was actually inspected (23 November 2026)

| Source or evidence | What it directly supports | Scope |
| --- | --- | --- |
| [Professor's issue #1](https://github.com/alexanderquispe/AI-Econ-Modeling/issues/1) and [repository guide](https://github.com/alexanderquispe/AI-Econ-Modeling/blob/main/syllabus/repository-guide.md) | Assignment, required structure, named paper, oral criteria and original due date | **Course instruction checked** |
| [NBER landing page](https://www.nber.org/papers/w34034) | Correct title/authors/year/DOI, three-capability model, substitution of implementation skill and complementarity with opportunity judgment | **Bibliographic/abstract verified** |
| [SSRN NBER record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5350364) | NBER working-paper listing, July 2025 posting and a **later** June 2026 revision | **Version metadata verified** |
| [User's four-page handwritten proof](hand/prop3-handwritten-full.pdf) | FOC, interior condition, value substitution, variance derivative and the example's invalid success-probability values | **Hand algebra checked**, not an original-paper transcription |
| [Unit tests](tests/test_proposition3.py) and [Lean proofs](formal/Proposition3.lean) | Exact rational identities and selected downstream real-algebra statements | **Executable checks**, not a proof of the paper's full proposition |

**Access limitation:** The full NBER PDF was attempted from the publisher's direct URL and returned HTTP 403 to the available web reader; it was not embedded in the connected course repository, nor did the alternative public listing supply readable full text. Accordingly, the precise wording, equation numbers, quantifiers and *all* assumptions of **the published Proposition 3** have **not** been certified by a page-by-page comparison. Do not cite a fabricated page number or describe any mathematical qualification below as a confirmed authorial typo. The same title appears in a 49-page SSRN variant; do not silently substitute that version.

## Mathematics independently verified from the stated specialization

For \(\alpha,s,\Gamma,\Delta>0\), \(\delta\gamma<1\), required finite moments, and independence of \(\alpha,\gamma_0,\gamma,s\), consider the specialization written in the repository:

\[
p(se;\theta)=\sqrt{se+\theta},\quad c(e)=e,\quad
e^*=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s},
\quad
V=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right).
\]

**Domain:** These expressions are for \(e^*>0\), i.e., \(\theta<\alpha^2\Delta^2s^2/4\) for every realized type. A statement at \(\theta=1\) needs that bound there. Nonnegative effort without this bound requires recomputing corners.

Let \(A=\Delta^2\Gamma\alpha^2s/4\) and \(B=\Gamma/s\), so \(V=A+\theta B\). Independence gives

\[
2\operatorname{Cov}(A,B)
=\frac{\Delta^2E[\alpha^2]}{2}
\big[E[\Gamma^2]-E[\Gamma]^2E[s]E[1/s]\big]
=:a_0,
\quad
\frac{d\operatorname{Var}(V)}{d\theta}
=a_0+2\theta\operatorname{Var}(B).
\]

The *heterogeneity condition* \(E[\Gamma^2]/E[\Gamma]^2<E[s]E[1/s]\) makes \(a_0<0\). If \(q=\operatorname{Var}(B)>0\), there is an algebraic turning point \(\theta^*=-a_0/(2q)>0\). **It does not follow** that \(\theta^*<1\), or that the common interior formula is valid at that point. To claim \(\operatorname{Var}'(1)>0\), independently check \(a_0+2q>0\) **and** interiority.

Individual gains \(G_i(\theta)=V_i(\theta)-V_i(0)=\theta B_i\) have \(\operatorname{Var}(G(\theta))=\theta^2 q\) **within the common interior region**. This is not the variance of total value levels, nor a variance of AI predictions.

### Two-type illustration and probability-domain caveat

For \(s\in\{3/5,1\}\) equally likely, \(\alpha=\Gamma=1,\Delta=4\):
\(1<16/15\), \(a_0=-8/15\), \(q=1/9\), \(\operatorname{Var}'(1)=-14/45<0\), and \(\theta^*=12/5\). The first effort corner occurs at \(36/25<12/5\). But \(p^*=\alpha\Delta s/2\in\{6/5,2\}>1\). It refutes **the algebraic inference from (H) alone to a positive endpoint derivative**, not an economically admissible probability model. In [our modified capped model](extra/bounded-probability-variant.md) the success probability is bounded and the value variance decreases while gain variance rises; saturation introduces a kink, so it is **not** claimed to satisfy all original paper assumptions.

## Outstanding source check — exact procedure

To resolve textual fidelity, obtain the instructor's **July 2025 53-page PDF** (not a different SSRN revision), confirm checksum and version, then compare: Proposition 1–3 statements; Definition of a cognitive tool; equations for \(p,c,e^*,V,\Gamma\); joint-support, independence and moment assumptions; the heterogeneity inequality and any claimed endpoint sign; and the appendix's treatment of effort corners and success-probability bounds. Record **actual PDF pages and exact quoted hypotheses** only after reading that file. Do not call this source-to-text check completed in its absence.

This audit distinguishes **verified mathematics**, **verified source metadata**, and **unverified published wording**. The student's professor-approved extension and digital handwriting are administrative matters, not substitutes for primary-source verification.
