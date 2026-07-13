# Verification Script

Run from the repository root:

```bash
python scripts/verify_scaling_cancellation.py --precision 100 --scale 3 --outdir outputs
```

The calculation uses `mpmath` and the unit-circle polygon sequence
\(P_N=2N\sin(\pi/N)\). It checks convergence orders and normalized leading
coefficients for both the raw and accelerated approximations.
