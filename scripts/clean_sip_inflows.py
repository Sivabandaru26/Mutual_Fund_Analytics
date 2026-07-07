import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("Original Shape:", df.shape)

df = df.drop_duplicates()

df = df[df["sip_inflow_crore"] >= 0]
df = df[df["active_sip_accounts_crore"] >= 0]
df = df[df["new_sip_accounts_lakh"] >= 0]
df = df[df["sip_aum_lakh_crore"] >= 0]

df.to_csv(
    "data/processed/monthly_sip_inflows_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("SIP Inflows cleaned successfully!")