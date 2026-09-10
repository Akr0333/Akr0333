# Data Science Portfolio — House Price Prediction

An end-to-end **Data Science and Machine Learning** project that predicts California house prices using the Scikit-learn California Housing dataset.

## Project Highlights

- Data loading and validation
- Exploratory Data Analysis (EDA)
- Correlation analysis and visualisation
- Feature/target preparation
- Train/test split and feature scaling
- Linear Regression baseline
- Random Forest Regression
- Model evaluation with MAE, RMSE and R²
- Feature importance analysis
- Reproducible Python workflow

## Tech Stack

Python • Pandas • NumPy • Matplotlib • Seaborn • Scikit-learn

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── house_price_prediction.py
└── notebooks/
    └── house_price_prediction.ipynb
```

## How to Run

```bash
git clone https://github.com/Akr0333/Akr0333.git
cd Akr0333
pip install -r requirements.txt
python src/house_price_prediction.py
```

The script downloads the California Housing dataset through Scikit-learn, so no dataset file needs to be committed.

## What I Learned

This project demonstrates a complete beginner-to-intermediate machine-learning workflow: understanding data, exploring patterns, preparing features, training multiple regression models, comparing metrics, and interpreting model behaviour.

## Results

The script prints MAE, RMSE and R² for both models and identifies the most important features from the Random Forest model. Exact results can vary slightly with library versions.

## Future Improvements

- Hyperparameter tuning with GridSearchCV
- Cross-validation
- Streamlit prediction dashboard
- Experiment tracking
- Model deployment with an API
