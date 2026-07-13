# A Scaling-Cancellation Principle for Chord-Based Geometric Approximations

**Author:** C. Wayne Baker  
**Date:** June 28, 2026  
**Status:** Preprint / source and reproducibility archive

This repository contains the paper, LaTeX source, and numerical verification script for:

> **A Scaling-Cancellation Principle for Chord-Based Geometric Approximations**

## Read the paper

- [`paper/scaling_cancellation_principle.pdf`](paper/scaling_cancellation_principle.pdf)
- [`paper/scaling_cancellation_principle.tex`](paper/scaling_cancellation_principle.tex)

## Main result

Suppose a chord-based approximation satisfies

\[
Q-Q_N=C_2N^{-2}+C_4N^{-4}+O(N^{-6}).
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
Q-\widehat Q_{N,k}=O(N^{-4}),
\]

and more precisely,

\[
Q-\widehat Q_{N,k}
=
-\frac{C_4}{k^2}N^{-4}+O(N^{-6}).
\]

The paper also records the higher-order fixed-scale moment conditions and distinguishes this Richardson-type mechanism from the nonlinear cubic residual map in the Baker \(4{:}3\) trisection cascade.

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

The scaling-cancellation theorem is conditional on the stated even-power asymptotic expansion. The note does not claim new Richardson theory, a new value of \(\pi\), or an identification of fixed N-series extrapolation with modular transformation.

The comparison with the Baker trisection cascade is taxonomic: fixed-resolution cancellation raises asymptotic order, whereas the nonlinear residual map multiplies error order under iteration.

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
