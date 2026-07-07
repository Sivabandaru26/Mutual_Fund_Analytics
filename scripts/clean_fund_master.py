import pandas as pd

# Load data
df = pd.read_csv("data/raw/01_fund_master.csv")

print("Original Shape:", df.shape)

# Convert launch_date
df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)

# Remove duplicates
df = df.drop_duplicates()

# Expense ratio should not be negative
df = df[df["expense_ratio_pct"] >= 0]

# Exit load should not be negative
df = df[df["exit_load_pct"] >= 0]

# SIP amount should not be negative
df = df[df["min_sip_amount"] >= 0]

# Lumpsum amount should not be negative
df = df[df["min_lumpsum_amount"] >= 0]

# Remove rows with missing AMFI code
df = df.dropna(subset=["amfi_code"])

# Save cleaned file
df.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Fund Master cleaned successfully!")