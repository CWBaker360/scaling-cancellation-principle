#!/usr/bin/env python3
"""Numerically verify the scaling-cancellation law for regular polygons."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import mpmath as mp


def polygon_perimeter(n: int) -> mp.mpf:
    """Perimeter of the regular inscribed n-gon in the unit circle."""
    if n < 3:
        raise ValueError("n must be at least 3")
    return 2 * n * mp.sin(mp.pi / n)


def accelerated_perimeter(n: int, scale: int) -> mp.mpf:
    """Two-scale cancellation of the leading inverse-square error."""
    if scale < 2:
        raise ValueError("scale must be at least 2")
    p_n = polygon_perimeter(n)
    p_kn = polygon_perimeter(scale * n)
    return (scale**2 * p_kn - p_n) / (scale**2 - 1)


def observed_order(err_coarse: mp.mpf, err_fine: mp.mpf, scale: int) -> mp.mpf:
    if err_coarse == 0 or err_fine == 0:
        return mp.nan
    return mp.log(abs(err_coarse / err_fine)) / mp.log(scale)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--scale", type=int, default=3)
    parser.add_argument("--outdir", type=Path, default=Path("outputs"))
    parser.add_argument(
        "--n-values",
        type=int,
        nargs="+",
        default=[12, 24, 48, 96, 192, 384],
    )
    args = parser.parse_args()

    if args.precision < 40:
        raise ValueError("precision must be at least 40 decimal digits")
    if args.scale < 2:
        raise ValueError("scale must be at least 2")
    if any(n < 3 for n in args.n_values):
        raise ValueError("all n-values must be at least 3")

    mp.mp.dps = args.precision
    target = 2 * mp.pi
    c2 = mp.pi**3 / 3
    c4 = -(mp.pi**5) / 60
    predicted_acc_coeff = -c4 / (args.scale**2)

    rows = []
    for n in args.n_values:
        p_n = polygon_perimeter(n)
        p_acc = accelerated_perimeter(n, args.scale)
        raw_error = target - p_n
        acc_error = target - p_acc

        p_n_fine = polygon_perimeter(args.scale * n)
        p_acc_fine = accelerated_perimeter(args.scale * n, args.scale)
        raw_error_fine = target - p_n_fine
        acc_error_fine = target - p_acc_fine

        rows.append(
            {
                "N": n,
                "scale": args.scale,
                "raw_error": mp.nstr(raw_error, 30),
                "accelerated_error": mp.nstr(acc_error, 30),
                "raw_observed_order": mp.nstr(
                    observed_order(raw_error, raw_error_fine, args.scale), 20
                ),
                "accelerated_observed_order": mp.nstr(
                    observed_order(acc_error, acc_error_fine, args.scale), 20
                ),
                "N2_raw_error": mp.nstr((n**2) * raw_error, 30),
                "predicted_C2": mp.nstr(c2, 30),
                "N4_accelerated_error": mp.nstr((n**4) * acc_error, 30),
                "predicted_accelerated_coefficient": mp.nstr(
                    predicted_acc_coeff, 30
                ),
            }
        )

    args.outdir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outdir / "scaling_cancellation_verification.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    last = rows[-1]
    raw_order = mp.mpf(last["raw_observed_order"])
    acc_order = mp.mpf(last["accelerated_observed_order"])

    # Conservative finite-N acceptance thresholds.
    passed = abs(raw_order - 2) < mp.mpf("0.02") and abs(acc_order - 4) < mp.mpf("0.05")

    summary_path = args.outdir / "scaling_cancellation_summary.txt"
    summary = [
        "Scaling-cancellation verification",
        f"precision_dps: {args.precision}",
        f"scale: {args.scale}",
        f"largest_N: {args.n_values[-1]}",
        f"raw_observed_order: {last['raw_observed_order']}",
        f"accelerated_observed_order: {last['accelerated_observed_order']}",
        f"N2_raw_error: {last['N2_raw_error']}",
        f"predicted_C2: {last['predicted_C2']}",
        f"N4_accelerated_error: {last['N4_accelerated_error']}",
        "predicted_accelerated_coefficient: "
        f"{last['predicted_accelerated_coefficient']}",
        f"verification_passed: {passed}",
    ]
    summary_path.write_text("\n".join(summary) + "\n", encoding="utf-8")

    print("\n".join(summary))
    if not passed:
        raise SystemExit("verification thresholds were not met")


if __name__ == "__main__":
    main()
