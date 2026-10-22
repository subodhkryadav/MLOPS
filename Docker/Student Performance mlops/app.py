from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from flask import Flask, render_template, request


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "model.pkl"

app = Flask(__name__)

FEATURES = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
]


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Run 'dvc repro' before starting Flask."
        )
    return joblib.load(MODEL_PATH)


model = load_model()


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            values = [
                float(request.form["study_hours"]),
                float(request.form["attendance"]),
                float(request.form["previous_score"]),
                float(request.form["assignments_completed"]),
            ]

            if not all(np.isfinite(v) for v in values):
                raise ValueError("Please enter valid numeric values.")

            study_hours, attendance, previous_score, assignments = values

            if not 0 <= study_hours <= 24:
                raise ValueError("Study hours must be between 0 and 24.")

            if not 0 <= attendance <= 100:
                raise ValueError("Attendance must be between 0 and 100.")

            if not 0 <= previous_score <= 100:
                raise ValueError("Previous score must be between 0 and 100.")

            if not 0 <= assignments <= 10 or not assignments.is_integer():
                raise ValueError(
                    "Assignments completed must be a whole number from 0 to 10."
                )

            input_data = pd.DataFrame([values], columns=FEATURES)

            predicted_score = float(model.predict(input_data)[0])

            prediction = round(
                min(100.0, max(0.0, predicted_score)), 2
            )

        except (ValueError, KeyError) as exc:
            error = str(exc)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
    )


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "model_loaded": model is not None}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)