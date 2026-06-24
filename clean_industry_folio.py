import pandas as pd

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

print("Original Shape:", df.shape)

df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

df = df.drop_duplicates()

folio_cols = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for col in folio_cols:
    df = df[df[col] >= 0]

df.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Industry Folio data cleaned successfully!")