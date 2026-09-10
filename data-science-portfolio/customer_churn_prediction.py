"""Customer Churn Prediction - portfolio-ready example.

Uses a synthetic dataset so the project runs without external data downloads.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

rng = np.random.default_rng(42)
n = 1200
age = rng.integers(18, 70, n)
tenure = rng.integers(1, 72, n)
monthly = rng.normal(70, 25, n).clip(20, 180)
contract = rng.choice(["Month-to-month", "One year", "Two year"], n, p=[.55, .25, .20])
service = rng.choice(["Basic", "Standard", "Premium"], n)
support_calls = rng.poisson(2, n)
churn_score = -1.5 + .035 * (monthly - 70) - .018 * tenure + .45 * support_calls + (contract == "Month-to-month") * 1.2
prob = 1 / (1 + np.exp(-churn_score))
churn = rng.binomial(1, prob)

df = pd.DataFrame({"age": age, "tenure_months": tenure, "monthly_charges": monthly.round(2), "contract": contract, "service": service, "support_calls": support_calls, "churn": churn})
X = df.drop(columns="churn")
y = df["churn"]
num = ["age", "tenure_months", "monthly_charges", "support_calls"]
cat = ["contract", "service"]
pre = ColumnTransformer([("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])

for name, model in [("Logistic Regression", LogisticRegression(max_iter=1000)), ("Random Forest", RandomForestClassifier(n_estimators=250, random_state=42))]:
    pipe = Pipeline([("preprocess", pre), ("model", model)])
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)
    pipe.fit(Xtr, ytr)
    pred = pipe.predict(Xte)
    score = pipe.predict_proba(Xte)[:, 1]
    print(f"\n{name}\nROC-AUC: {roc_auc_score(yte, score):.3f}")
    print(classification_report(yte, pred))
