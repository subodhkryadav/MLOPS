
from pathlib import Path

import dagshub
import joblib
import mlflow
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


ROOT = Path(__file__).resolve().parents[1]
TRAIN_FILE = ROOT / "data" / "processed" / "train.csv"
MODEL_DIR = ROOT / "models"


def main():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    with open(ROOT / "params.yaml", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    train_df = pd.read_csv(TRAIN_FILE)

    X_train = train_df.drop(columns=["final_score"])
    y_train = train_df["final_score"]

    model_params = params["model"]

    # Connect MLflow to DagsHub
    dagshub.init(
        repo_owner="subodhkryadav",
        repo_name="MLflow",
        mlflow=True,
    )

    mlflow.set_experiment("Student-Performance-Prediction")

    with mlflow.start_run(run_name="RandomForest-Training"):
        model = RandomForestRegressor(
            n_estimators=model_params["n_estimators"],
            max_depth=model_params["max_depth"],
            random_state=model_params["random_state"],
            n_jobs=-1,
        )

        model.fit(X_train, y_train)
        predictions = model.predict(X_train)

        mae = mean_absolute_error(y_train, predictions)
        rmse = mean_squared_error(y_train, predictions) ** 0.5
        r2 = r2_score(y_train, predictions)

        mlflow.log_params(model_params)
        mlflow.log_param("model_type", "RandomForestRegressor")
        mlflow.log_param("training_rows", len(X_train))
        mlflow.log_param("number_of_features", X_train.shape[1])

        mlflow.log_metric("train_mae", mae)
        mlflow.log_metric("train_rmse", rmse)
        mlflow.log_metric("train_r2", r2)

        model_path = MODEL_DIR / "model.pkl"
        joblib.dump(model, model_path)
        mlflow.log_artifact(str(model_path))

        print(f"Model saved: {model_path}")
        print(f"MLflow Run ID: {mlflow.active_run().info.run_id}")
        print(f"Training MAE: {mae:.4f}")
        print(f"Training RMSE: {rmse:.4f}")
        print(f"Training R2: {r2:.4f}")


if __name__ == "__main__":
    main()
