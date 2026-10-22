from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    output_path = RAW_DIR / "students.csv"

    rng = np.random.default_rng(42)
    n = 1000

    study_hours = rng.uniform(0, 10, n)
    attendance = rng.uniform(40, 100, n)
    previous_score = rng.uniform(20, 100, n)
    assignments_completed = rng.integers(0, 11, n)

    noise = rng.normal(0, 5, n)

    final_score = (
        2.5 * study_hours
        + 0.25 * attendance
        + 0.30 * previous_score
        + 1.2 * assignments_completed
        + noise
    )

    final_score = np.clip(final_score, 0, 100)

    df = pd.DataFrame({
        "study_hours": study_hours.round(2),
        "attendance": attendance.round(2),
        "previous_score": previous_score.round(2),
        "assignments_completed": assignments_completed,
        "final_score": final_score.round(2),
    })

    df.to_csv(output_path, index=False)

    print(f"Dataset saved: {output_path}")
    print(f"Dataset shape: {df.shape}")
    print(df.head())


if __name__ == "__main__":
    main()