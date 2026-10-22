
import json
from pathlib import Path

import dagshub
import joblib
import mlflow
import pandas as pd
import yaml
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

ROOT = Path(__file__).resolve().parents[1]
MODEL_FILE = ROOT / "models" / "model.pkl"
TEST_FILE = ROOT / "data" / "processed" / "test.csv"
REPORT_DIR = ROOT / "reports"


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    with open(ROOT / "params.yaml", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    model = joblib.load(MODEL_FILE)
    test_df = pd.read_csv(TEST_FILE)

    X_test = test_df.drop(columns=["final_score"])
    y_test = test_df["final_score"]

    predictions = model.predict(X_test)

    metrics = {
        "mae": float(mean_absolute_error(y_test, predictions)),
        "rmse": float(mean_squared_error(y_test, predictions) ** 0.5),
        "r2": float(r2_score(y_test, predictions)),
    }

    # Save evaluation report locally
    metrics_file = REPORT_DIR / "metrics.json"
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4)

    print("Model evaluation results:")
    print(json.dumps(metrics, indent=4))

    # Connect MLflow to DagsHub
    dagshub.init(
        repo_owner="subodhkryadav",
        repo_name="MLflow",
        mlflow=True,
    )

    mlflow.set_experiment("Student-Performance-Prediction")

    with mlflow.start_run(run_name="RandomForest-Test-Evaluation"):
        mlflow.log_metrics({
            "test_mae": metrics["mae"],
            "test_rmse": metrics["rmse"],
            "test_r2": metrics["r2"],
        })
        mlflow.log_artifact(str(metrics_file))

    # Quality gate
    minimum_r2 = params["evaluation"]["minimum_r2"]

    if metrics["r2"] < minimum_r2:
        raise ValueError(
            f"Model failed quality gate: R2={metrics['r2']:.3f}; "
            f"minimum required={minimum_r2:.3f}"
        )

    print("Model passed the R2 quality gate.")


if __name__ == "__main__":
    main()
