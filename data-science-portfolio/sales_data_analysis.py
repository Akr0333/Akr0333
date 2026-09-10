"""Sales Data Analysis - reproducible portfolio example."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 1500
dates = pd.date_range("2025-01-01", periods=365, freq="D")
df = pd.DataFrame({
    "date": rng.choice(dates, n),
    "region": rng.choice(["North", "South", "East", "West"], n),
    "category": rng.choice(["Electronics", "Furniture", "Office Supplies"], n),
    "quantity": rng.integers(1, 8, n),
    "unit_price": rng.uniform(10, 500, n).round(2),
})
df["revenue"] = (df["quantity"] * df["unit_price"]).round(2)
df["date"] = pd.to_datetime(df["date"])

print("Total revenue:", round(df["revenue"].sum(), 2))
print("\nRevenue by region:")
print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))
print("\nRevenue by category:")
print(df.groupby("category")["revenue"].sum().sort_values(ascending=False))
print("\nMonthly revenue:")
print(df.groupby(df["date"].dt.to_period("M"))["revenue"].sum())
