import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert month
df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(subset=["month"])

# Net inflow can be negative (outflow)
# So no filtering needed

df.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Category Inflows cleaned successfully!")