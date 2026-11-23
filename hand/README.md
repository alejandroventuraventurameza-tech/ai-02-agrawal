# Handwritten mathematical verification (source and provenance)

The user supplied `ai-02.pdf` on 23 November 2026. It contains **four
pages of handwritten mathematics**, not an AI-generated drawing. The
following two files preserve the evidence:

- [`prop3-handwritten-full.pdf`](prop3-handwritten-full.pdf):
  the **exact bytes of the user-supplied PDF**, renamed for clarity.
- [`prop3-derivation.jpg`](prop3-derivation.jpg):
  a direct rasterization of **page 4 of that original document**,
  which is displayed on slide 4 of the five-minute Beamer deck.

Page 4 was rendered with PyMuPDF at scale 1.65, RGB, then saved as a
high-quality JPEG (quality 81, no cropping or annotations added).
It is an image of original tablet/digital handwriting, **not a claim
that a physical camera took a photograph of paper**. The student confirms the instructor **accepted this digital handwritten evidence**;
a separate camera photograph is therefore not treated as an outstanding requirement.

## Audited contents of the original PDF

1. Page 1: \(\alpha\Delta\sqrt{se+\theta}-e\), its interior FOC and
   \(e^*=\alpha^2\Delta^2s/4-\theta/s\), plus the interiority threshold.
2. Page 2: \(V(\theta)=\Gamma[\alpha^2\Delta^2s/4+\theta/s]\) and
   \(\operatorname{Var}(X+\theta Y)=\operatorname{Var}(X)+2\theta\operatorname{Cov}(X,Y)+\theta^2\operatorname{Var}(Y)\).
3. Page 3: derivative and turning point, with the explicit observation
   that \(a_0<0\) does not imply \(\theta^*<1\).
4. Page 4: two-type example, \(\operatorname{Var}'(1)=-14/45<0\),
   \(p^*=\alpha\Delta s/2=2s\in\{6/5,2\}\), and a handwritten
   conclusion that the numerical counterexample is algebraically correct
   but not a literal probability-admissible example.

The audit distinguishes an interior algebraic counterexample from a
true probability-constrained model. The four-page PDF includes the
actual author's mathematical working and final red corrections.

## Integrity check

File hashes in [`SHA256SUMS`](SHA256SUMS) allow byte-for-byte
validation of the original PDF and the displayed JPEG:

```bash
sha256sum -c hand/SHA256SUMS
```

Do not replace either with AI-generated handwriting. If the user supplies
a replacement photograph or additional pages, keep the original PDF
and update the hashes/documentation, then rerun GitHub Actions.
