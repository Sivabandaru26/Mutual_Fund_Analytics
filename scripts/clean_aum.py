import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("Original Shape:", df.shape)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df.drop_duplicates()

df = df[df["aum_lakh_crore"] >= 0]
df = df[df["aum_crore"] >= 0]
df = df[df["num_schemes"] > 0]

df.to_csv(
    "data/processed/aum_by_fund_house_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("AUM data cleaned successfully!")