"""End-to-end house price prediction project.

Dataset: California Housing (built into scikit-learn).
Models: Linear Regression and Random Forest Regression.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42
OUTPUT_DIR = Path("outputs")


def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)
    return mae, rmse, r2, predictions


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1. Load data
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame.copy()

    print("Dataset shape:", df.shape)
    print("\nMissing values:\n", df.isna().sum())
    print("\nSummary statistics:\n", df.describe().round(2))

    # 2. EDA: correlation heatmap
    plt.figure(figsize=(10, 7))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("California Housing Feature Correlation")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=150)
    plt.close()

    # 3. Split features and target
    X = df.drop(columns="MedHouseVal")
    y = df["MedHouseVal"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=RANDOM_STATE
    )

    # 4. Models
    linear_model = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", LinearRegression()),
    ])

    forest_model = RandomForestRegressor(
        n_estimators=250,
        max_depth=18,
        min_samples_leaf=2,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )

    models = {
        "Linear Regression": linear_model,
        "Random Forest": forest_model,
    }

    results = []
    predictions_for_plot = None

    for name, model in models.items():
        model.fit(X_train, y_train)
        mae, rmse, r2, predictions = evaluate(model, X_test, y_test)
        results.append({"Model": name, "MAE": mae, "RMSE": rmse, "R2": r2})
        if name == "Random Forest":
            predictions_for_plot = predictions

    results_df = pd.DataFrame(results).sort_values("R2", ascending=False)
    print("\nModel comparison:\n", results_df.round(4).to_string(index=False))
    results_df.to_csv(OUTPUT_DIR / "model_results.csv", index=False)

    # 5. Actual vs predicted plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, predictions_for_plot, alpha=0.25)
    plt.xlabel("Actual Median House Value")
    plt.ylabel("Predicted Median House Value")
    plt.title("Random Forest: Actual vs Predicted")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "actual_vs_predicted.png", dpi=150)
    plt.close()

    # 6. Feature importance
    importances = pd.Series(
        forest_model.feature_importances_, index=X.columns
    ).sort_values(ascending=False)
    print("\nRandom Forest feature importance:\n", importances.round(4))

    plt.figure(figsize=(9, 5))
    importances.sort_values().plot(kind="barh")
    plt.xlabel("Importance")
    plt.title("Random Forest Feature Importance")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "feature_importance.png", dpi=150)
    plt.close()

    print(f"\nSaved analysis outputs to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
