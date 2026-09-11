# A Scaling-Cancellation Principle for Chord-Based Geometric Approximations

**Author:** C. Wayne Baker  
**Original date:** June 28, 2026  
**Revised:** September 11, 2026  
**Status:** Revised preprint / source and reproducibility archive

> **A Scaling-Cancellation Principle for Chord-Based Geometric Approximations**

## Read the paper

- [`paper/scaling_cancellation_principle.pdf`](paper/scaling_cancellation_principle.pdf)
- [`paper/scaling_cancellation_principle.tex`](paper/scaling_cancellation_principle.tex)

## Main results

Assume a geometric approximation has an even-power asymptotic expansion

\[
Q-Q_N
=
C_2N^{-2}
+
C_4N^{-4}
+
C_6N^{-6}
+\cdots .
\]

For a fixed scale factor \(k\ge 2\), define

\[
\widehat Q_{N,k}
=
Q_{kN}
+
\frac{Q_{kN}-Q_N}{k^2-1}
=
\frac{k^2Q_{kN}-Q_N}{k^2-1}.
\]

Then

\[
Q-\widehat Q_{N,k}
=
-\frac{C_4}{k^2}N^{-4}
+
O(N^{-6}),
\]

so the leading \(N^{-2}\) error is cancelled without requiring knowledge of
\(C_2\).

The revised paper develops this into a full fixed-scale hierarchy. For the
geometric node family

\[
N,\ bN,\ b^2N,\ldots,b^sN,
\]

the unique Lagrange weights cancelling the first \(s\) even-power terms give

\[
Q-\widehat Q_N^{(s)}
=
(-1)^s C_{2s+2}\,
b^{-s(s+1)}
N^{-2s-2}
+
O(N^{-2s-4}).
\]

The same hierarchy may also be written recursively as a fixed-base
Richardson-style ladder.

For tripling, the first nontrivial higher-order combination is

\[
\widehat Q_N^{(2)}
=
\frac{Q_N-90Q_{3N}+729Q_{9N}}{640},
\]

which cancels both the \(N^{-2}\) and \(N^{-4}\) terms.

The paper applies the framework to polygonal approximation of \(\pi\) and,
using an explicitly cited factorization from the companion ellipse analysis,
to inscribed ellipse perimeters.

It also distinguishes this fixed-resolution cancellation mechanism from the
nonlinear proportional-subtended residual law

\[
\mathscr R_{a,b}(e)
=
-\frac{a^2-b^2}{24a^2}e^3
+
O(e^5),
\]

whose repeated iteration multiplies local error order rather than cancelling
successive powers of a resolution parameter.
## Numerical verification

The script

```text
scripts/verify_scaling_cancellation.py
```

uses the regular inscribed polygon sequence

\[
P_N=2N\sin(\pi/N)
\]

for the unit circle. It verifies the raw second-order error and the accelerated fourth-order error for configurable scale factors.

Run from the repository root:

```bash
python scripts/verify_scaling_cancellation.py --precision 100 --scale 3 --outdir outputs
```

## Scope

The scaling-cancellation results are conditional on an even-power asymptotic
expansion for the underlying approximation family. Such an expansion must be
established separately for each geometry or discretization.

The paper does not claim new Richardson or Romberg extrapolation theory, a
new value of \(\pi\), or an equivalence between fixed-scale N-series
cancellation and modular transformation.

Its contribution is the geometric organization of the cancellation hierarchy,
the explicit geometric-node coefficient law, its applications to the
associated approximation program, and the comparison with nonlinear
proportional-subtended cubic residual refinement.

## Related repositories

- [`constructible-cubic-trisection`](https://github.com/CWBaker360/constructible-cubic-trisection)
- [`proportional-subtended-cubic-refinement`](https://github.com/CWBaker360/proportional-subtended-cubic-refinement)
- [`nseries-pi-acceleration`](https://github.com/CWBaker360/nseries-pi-acceleration)
- [`ramanujan-landen-nseries-refinement`](https://github.com/CWBaker360/ramanujan-landen-nseries-refinement)

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── REPRODUCIBILITY.md
├── LICENSE_NOTICE.md
├── CHANGELOG.md
├── SHA256SUMS.txt
├── .gitignore
├── paper/
│   ├── scaling_cancellation_principle.tex
│   ├── scaling_cancellation_principle.pdf
│   └── README.md
├── scripts/
│   ├── verify_scaling_cancellation.py
│   └── README.md
└── docs/
    ├── abstract.md
    ├── main_result.md
    ├── repository_description.md
    └── github_upload_checklist.md
```

## Rights

Copyright © 2026 C. Wayne Baker. All rights reserved unless otherwise stated.
