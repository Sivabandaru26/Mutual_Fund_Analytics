import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Find date column automatically
date_cols = [col for col in df.columns if "date" in col.lower()]

if len(date_cols) > 0:
    date_col = date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

# Find NAV column automatically
nav_cols = [col for col in df.columns if "nav" in col.lower()]

if len(nav_cols) > 0:
    nav_col = nav_cols[0]

    df[nav_col] = pd.to_numeric(
        df[nav_col],
        errors="coerce"
    )

    df = df[df[nav_col] > 0]

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("NAV History cleaned successfully!")