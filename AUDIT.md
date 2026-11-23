# Verified Repository 2 audit — July 2025 primary paper

**Original primary PDF:** 53 pages, supplied by the student on
23 November 2026. SHA-256:
\`11b8f4eda55480fcb1eaf4ee42598ce9c6640da535ed0fa551fc7597ee7bae8d\`.
Full source-to-claim ledger and actual equation numbers:
[SOURCE_AUDIT.md](SOURCE_AUDIT.md).

**Source-confirmed qualifications:**

1. Printed Proposition 3(b), p. 18, eq. (32) claims
   \(\operatorname{Var}'(V(1))>0\) given (30). Appendix A.3
   (p. 41, eq. 81) requires the extra
   \(\theta^*<1\) to establish this sign.
2. The printed condition \(\Delta>2/(s\sqrt\alpha)\)
   (pp. 18, 39) is insufficient for \(e^*(1)>0\),
   which requires \(\Delta>2/(s\alpha)\).
3. The general \(p\in[0,1]\) definition (p. 12) conflicts
   with \(p=\sqrt{se+\theta}\) (p. 17) at \(\theta=1\)
   whenever \(e>0\). The old counterexample is **algebraic**,
   not a globally admissible probability model.

**Verified work:** actual four-page digital handwritten derivation
[PDF](hand/prop3-handwritten-full.pdf) and [page-four image](hand/prop3-derivation.jpg);
[raw AI exchange](prompts.md); [six compiled Lean algebra lemmas](formal/Proposition3.lean);
[exact regressions](tests/); [bounded-model extension](extra/bounded-probability-variant.md);
[Beamer source](presentation.tex) and [compiled five-page PDF](presentation.pdf).

**Important scope:** the PDF comparison covers the relevant
definitions and Propositions 1–3 and Appendix A.1–A.3,
not all 53 pages' theorems formally. The independently solved
capped probability model changes the original strict tool
definition; a green CI or Lean certificate does not settle
economic-model correspondence. The source PDF is copyrighted and
is **not redistributed** in this public GitHub repository.

The professor approved both the extended submission window and
iPad handwriting as evidence. Formal submission still follows
the course issue's requirements; the original deadline is
historical metadata, not an assertion of retroactive delivery.

[Previous November audit history](extra/audit-history-20261122.md)
is preserved for provenance, but its statement that the original
PDF was inaccessible has been superseded.
