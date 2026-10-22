
# 🎓 Student Performance Prediction – End-to-End MLOps

An end-to-end Machine Learning Operations (MLOps) project that predicts student performance and demonstrates the complete workflow from data processing and model training to experiment tracking, Docker containerization, and live deployment.

## 🌐 Live Demo

🚀 **[Try the Student Performance Prediction App](https://student-performance-mlops.subodhkryadav.blitz.cloud/)**

The application allows users to enter student-related details and receive a predicted performance score through a web interface.

## 🛠️ Technologies Used

### 🐍 Python
Used as the core programming language to build the machine learning pipeline, process data, train the model, and develop the application.

### 📊 Pandas and NumPy
Used for data manipulation, feature preparation, numerical operations, and validating input values.

### 🤖 Scikit-learn
Used to train the machine learning regression model and evaluate its performance using MAE, RMSE, and R² score.

### 📦 Joblib
Used to save the trained model and load it into the Flask application for making predictions.

### 🔄 DVC (Data Version Control)
Used to define and reproduce the machine learning pipeline through separate stages for data ingestion, transformation, model training, and evaluation.

### 📈 MLflow and DagsHub
- **MLflow:** Tracks model parameters, training metrics, and evaluation results.
- **DagsHub:** Provides remote experiment tracking so recorded runs and metrics can be reviewed online.

### 🌐 Flask and HTML
- **Flask:** Handles user requests, validates input data, loads the trained model, and returns predictions.
- **HTML:** Provides the web form through which users enter student information.

### 🐳 Docker and Docker Hub
- **Docker:** Packages the Flask application, model, templates, and required dependencies into a container.
- **Docker Hub:** Stores the published Docker image so it can be pulled and deployed on another system or hosting platform.

### ☁️ blitz.cloud
Used to deploy the Docker image and make the prediction application accessible through a public HTTPS URL.

### 🔧 Git and GitHub
Used for source code version control, maintaining project files, and sharing the project repository.

## 🔄 Project Workflow

1. **Data Ingestion:** Loads the dataset and prepares it for the next pipeline stage.
2. **Data Transformation:** Processes the input features for model training.
3. **Model Training:** Trains a regression model to predict student performance.
4. **Model Evaluation:** Calculates evaluation metrics and checks model performance.
5. **Experiment Tracking:** Logs parameters and metrics using MLflow and DagsHub.
6. **Pipeline Management:** Uses DVC to track pipeline dependencies and reproduce stages.
7. **Web Application:** Flask accepts student details and generates a predicted score.
8. **Containerization:** Docker packages the application and trained model.
9. **Deployment:** The Docker image is published to Docker Hub and deployed through blitz.cloud.

## 📊 Model Performance

Initial model evaluation results:

- **MAE:** 2.4097
- **RMSE:** 2.9792
- **R² Score:** 0.9441

These results represent an initial experiment and may vary when the dataset, features, or model configuration changes.

## 📁 Project Structure

```text
Student Performance mlops/
├── src/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   └── model_evaluation.py
├── data/
├── models/
├── reports/
├── templates/
│   └── index.html
├── app.py
├── params.yaml
├── dvc.yaml
├── dvc.lock
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/subodhkryadav/MLflow.git
cd MLflow
```

### 2. Navigate to the project folder

```powershell
cd "Docker/Student Performance mlops"
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the machine learning pipeline

```bash
dvc repro
```

### 5. Start the Flask application

```bash
python app.py
```

Open the application at `http://127.0.0.1:5000`.

**Note:** Ensure the required dataset and model artifacts are available before running the application. MLflow and DagsHub tracking also require valid credentials if tracking is enabled.

## 🐳 Run with Docker

Pull the published image:

```bash
docker pull subodhkryadav/student-performance-mlops:latest
```

Start the container:

```bash
docker run -d --name student-performance-app -p 5000:5000 subodhkryadav/student-performance-mlops:latest
```

Open `http://127.0.0.1:5000` in your browser.

## 🔗 Project Links

- **Live Application:** [Student Performance Prediction](https://student-performance-mlops.subodhkryadav.blitz.cloud/)
- **GitHub Repository:** [Source Code](https://github.com/subodhkryadav/MLflow)
- **Docker Hub:** [Docker Image](https://hub.docker.com/r/subodhkryadav/student-performance-mlops)
- **DagsHub:** [Experiment Tracking](https://dagshub.com/subodhkryadav/MLflow)
- **Portfolio:** [Personal Portfolio](https://subodhkryadav.github.io/)

## 👨‍💻 Author

**Subodh Kumar Yadav**

- GitHub: [subodhkryadav](https://github.com/subodhkryadav)
- LinkedIn: [Subodh Kumar Yadav](https://www.linkedin.com/in/subodh-kumar-yadav-522828293)
- Portfolio: [subodhkryadav.github.io](https://subodhkryadav.github.io/)

---

⭐ If you find this project useful, consider giving the repository a star.
