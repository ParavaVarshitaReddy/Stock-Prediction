
# Stock Price Prediction with Ensemble Learning

This project implements a robust stock price prediction model using machine learning techniques. It combines **LSTM**, **Random Forest**, and **XGBoost** models using **Stacking Ensemble** for enhanced accuracy. The project is complemented by CI/CD pipelines and Docker support for ease of deployment.

---

## **Features**
- **Data Preprocessing**: Clean and prepare stock price data for model training.
- **Machine Learning Models**:
  - **LSTM** for sequential data modeling.
  - **Random Forest** and **XGBoost** for robust predictions.
- **Stacking Ensemble**: Combines predictions from multiple models for better accuracy.
- **CI/CD Integration**: Automated testing and deployment with GitHub Actions.
- **Docker Support**: Containerized application for consistent environments.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**: 
  - TensorFlow (LSTM)
  - scikit-learn (Random Forest, Stacking)
  - XGBoost
  - Pandas & NumPy (Data Handling)
- **Deployment**: Docker, GitHub Actions
- **File Structure**:
  - `src/`: Contains all source code for preprocessing, models, and main script.
  - `tests/`: Unit tests for preprocessing and models.
  - `.github/workflows/`: CI configuration for automated pipelines.
  - `data/`: Example dataset for quick testing.

---

## **Setup Instructions**
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/stock-prediction.git
cd stock-prediction
```

### 2. Install Dependencies
Make sure you have Python 3.9+ installed. Then, install the required libraries:
```bash
pip install -r src/requirements.txt
```

### 3. Provide a Dataset
- Add your stock price dataset in the `data/` folder with the name `stock_prices.csv`.
- Sample dataset included for testing.

### 4. Run the Application
Execute the main script:
```bash
python src/main.py
```

---

## **Testing**
Run unit tests to ensure the functionality works as expected:
```bash
pytest tests/
```

---

## **Docker Instructions**
### Build the Docker Image
```bash
docker build -t stock-prediction .
```

### Run the Docker Container
```bash
docker run -it stock-prediction
```

---

## **CI/CD Pipeline**
This project uses GitHub Actions for:
- Dependency installation
- Unit testing with `pytest`

Pipelines are triggered on every push or pull request to the `main` branch.

---
