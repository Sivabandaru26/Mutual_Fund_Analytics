import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("Original Shape:", df.shape)

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"],
    errors="coerce"
)

df = df.drop_duplicates()

df = df[df["weight_pct"] >= 0]
df = df[df["market_value_cr"] >= 0]
df = df[df["current_price_inr"] >= 0]

df.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Portfolio Holdings cleaned successfully!")