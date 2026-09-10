"""Credit Card Fraud Detection - portfolio-ready example.

Synthetic transactions keep the project reproducible and privacy-safe.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

rng = np.random.default_rng(42)
n = 3000
amount = rng.lognormal(3.2, 1.0, n).round(2)
hour = rng.integers(0, 24, n)
distance = rng.exponential(20, n).round(2)
merchant_risk = rng.beta(2, 7, n).round(3)
velocity = rng.poisson(2, n)
score = -5 + .7 * np.log1p(amount) + .9 * (hour < 5) + .018 * distance + 4 * merchant_risk + .3 * velocity
p = 1 / (1 + np.exp(-score))
fraud = rng.binomial(1, p)
df = pd.DataFrame({"amount": amount, "hour": hour, "distance_km": distance, "merchant_risk": merchant_risk, "transactions_last_hour": velocity, "fraud": fraud})

X = df.drop(columns="fraud")
y = df["fraud"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=42, stratify=y)
model = RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]
print("Fraud rate:", round(y.mean(), 4))
print("ROC-AUC:", round(roc_auc_score(y_test, prob), 3))
print(classification_report(y_test, pred, zero_division=0))
print(pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False))
