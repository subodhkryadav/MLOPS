from pathlib import Path

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = ROOT / "data" / "raw" / "students.csv"
PROCESSED_DIR = ROOT / "data" / "processed"

FEATURES = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
]
TARGET = "final_score"


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    with open(ROOT / "params.yaml", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    df = pd.read_csv(RAW_FILE)

    required_columns = FEATURES + [TARGET]

    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    df = df[required_columns].drop_duplicates()

    for column in required_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna()

    if len(df) < 20:
        raise ValueError("Not enough valid rows to train the model.")

    if not df[TARGET].between(0, 100).all():
        raise ValueError("Final scores must be between 0 and 100.")

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=params["data"]["test_size"],
        random_state=params["data"]["random_state"],
    )

    train_df = X_train.copy()
    train_df[TARGET] = y_train

    test_df = X_test.copy()
    test_df[TARGET] = y_test

    train_df.to_csv(PROCESSED_DIR / "train.csv", index=False)
    test_df.to_csv(PROCESSED_DIR / "test.csv", index=False)

    print(f"Training rows: {len(train_df)}")
    print(f"Testing rows: {len(test_df)}")
    print("Transformation completed.")


if __name__ == "__main__":
    main()