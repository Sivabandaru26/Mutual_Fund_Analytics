<<<<<<< HEAD
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("Missing Codes:")
print(missing)

if len(missing) == 0:
=======
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("Missing Codes:")
print(missing)

if len(missing) == 0:
>>>>>>> 5e6528c2a8b061ca81cf7bebe5426257dfbb7c06
    print("All AMFI codes are present.")