# Reproducibility

## Requirements

- Python 3.10 or newer
- `mpmath`

Install the numerical dependency with:

```bash
python -m pip install mpmath
```

## Run the verification

From the repository root:

```bash
python scripts/verify_scaling_cancellation.py --precision 100 --scale 3 --outdir outputs
```

The script writes:

```text
outputs/scaling_cancellation_verification.csv
outputs/scaling_cancellation_summary.txt
```

## What is checked

For the inscribed regular polygon perimeter

\[
P_N=2N\sin(\pi/N),
\]

the script computes:

1. the raw error \(2\pi-P_N\);
2. the two-scale accelerated approximation;
3. the accelerated error;
4. observed convergence orders;
5. the normalized leading coefficients predicted by the paper.

The numerical experiment supports the asymptotic formulas. The theorem itself is analytic and conditional on the even-power expansion.
