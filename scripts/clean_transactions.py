import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert transaction date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Keep only valid transaction types
valid_types = ["SIP", "Lumpsum", "Redemption"]

df = df[
    df["transaction_type"].isin(valid_types)
]

# Amount should be greater than 0
df = df[
    df["amount_inr"] > 0
]

# Keep only valid KYC values
valid_kyc = ["Verified", "Pending"]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Investor Transactions cleaned successfully!")