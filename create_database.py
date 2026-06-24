import pandas as pd
import sqlite3

# Create database
conn = sqlite3.connect("bluestock_mf.db")

# Load cleaned files
pd.read_csv("data/processed/fund_master_clean.csv").to_sql(
    "fund_master", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/nav_history_clean.csv").to_sql(
    "nav_history", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/aum_by_fund_house_clean.csv").to_sql(
    "aum_by_fund_house", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/monthly_sip_inflows_clean.csv").to_sql(
    "monthly_sip_inflows", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/category_inflows_clean.csv").to_sql(
    "category_inflows", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/industry_folio_count_clean.csv").to_sql(
    "industry_folio_count", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/scheme_performance_clean.csv").to_sql(
    "scheme_performance", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/investor_transactions_clean.csv").to_sql(
    "investor_transactions", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/portfolio_holdings_clean.csv").to_sql(
    "portfolio_holdings", conn, if_exists="replace", index=False
)

pd.read_csv("data/processed/benchmark_indices_clean.csv").to_sql(
    "benchmark_indices", conn, if_exists="replace", index=False
)

print("Database created successfully!")

conn.close()