# REQUIREMENTS — Repository 2

Fuente: [Repository 2 — Agrawal, Gans & Goldfarb, issue #1](https://github.com/alexanderquispe/AI-Econ-Modeling/issues/1).

Checklist de los requisitos del issue, conservando literalmente su texto en inglés y su énfasis. Solo se añaden casillas y se convierte la tabla de archivos en una lista. Las casillas quedan sin marcar hasta verificar cada requisito; no representan una nueva auditoría. La fecha indicada es la original del issue.

## Entrega y flujo Git

- [ ] ⏰ **Due: Tuesday, August 25, 22:00.**
- [ ] The repository must be merged into `main` and its link posted as a comment on this issue.
- [ ] **Start from the template.** [`alexanderquispe/ai-01-aouad`](https://github.com/alexanderquispe/ai-01-aouad) is a worked example of a complete weekly repository — hit **Use this template** on GitHub to create yours with the structure already in place, then replace the content. What it contains beyond the required four files is above the floor; do not take it as the bar.
- [ ] A **new repository** on GitHub named **`ai-02-agrawal`**.
- [ ] **Required workflow** (branch → PR → merge, nothing written directly to `main`):

```bash
# 1. create the repo with a minimal README on main, then:
git checkout -b analysis
# 2. work over the following days, with small commits
git add . && git commit -m "FOC for Prop. 2"
git push -u origin analysis
# 3. open the Pull Request against main and merge it before Tuesday 22:00
```

## Minimum contents

- [ ] `README.md` — One page: what question the paper answers, what the agent's problem is, and the main result **with all its conditions**
- [ ] `prompts.md` — The prompts you used and the relevant answers, **raw** (do not clean them up to look good)
- [ ] `hand/` — At least **one photo** of a derivation done by hand
- [ ] `presentation.tex` and `presentation.pdf` — The 5-minute Beamer deck, source and compiled

## The 5-minute Beamer deck

- [ ] Title slide with the repository link, plus **four slides**:
- [ ] **The paper.** What question it answers, which *single* economic mechanism it formalises, and the agent's problem written out: what is maximised, over which variable, under which constraints.
- [ ] **The main result.** The exact statement of the proposition, **with all its conditions**, and below it the intuition in one sentence.
- [ ] **What I did.** What you explored in the repository: which assumptions you considered relaxing, what you simulated, what came out. Dead ends count if you explain why they led nowhere.
- [ ] **Where I did not believe the AI.** The step you verified by hand — with the photo on screen — what the model had answered, and **your verdict**: correct, incorrect, or unverifiable, with the reason.
- [ ] No animations. No screenshots of the paper: equations are written in LaTeX.

## The handwritten derivation

- [ ] **At least one photo in `hand/`.** You are not asked to derive the whole paper by hand: you are asked to show **at least one place where you did not believe the machine and checked it yourself**.
- [ ] In the `README.md`, add one line saying what the photo shows.

Good candidates this week: the first-order condition of Proposition 2, the use of the envelope theorem, or the geometric-sum step that yields the closed form.

A phone photo, crooked and with crossings-out, is fine. No need to scan or write it out neatly.

## This week's trap

When you ask the LLM about the paper's variance result, it will very likely tell you, with complete confidence, that **"the variance is U-shaped in the level of AI"**, with no conditions attached.

Check it. Pay attention to three things:

- [ ] The U-shape is in the variance **of what**, exactly, and with respect to **which variable**?
- [ ] Is the result **unconditional**, or does it depend on some inequality about heterogeneity?
- [ ] What happens to the variance of the **individual benefit**, which is a different object?

I am not giving you the answer: that is the exercise. But if your `prompts.md` ends up reproducing the loose statement the model gives you, without checking it against the paper, slide 4 will not score.

- [ ] **Bonus:** the paper contains at least one internal slip of its own in the variance section. Finding and documenting it counts as work above the floor.

## Post your link — right here

- [ ] Besides merging the PR, **leave a comment on this issue with your repository URL**, whether or not you are drawn. Just the link:

```
https://github.com/your-user/ai-02-agrawal
```

The pull request link is not needed. GitHub timestamps the comment, so **the comment is the submission record** — no argument about whether it arrived before Tuesday 22:00.

A repository that exists but was never posted here **counts as not submitted**.

> ⚠️ **If the repository is not merged and registered by the Tuesday deadline, the reading check is graded zero**, however good the presentation is.
