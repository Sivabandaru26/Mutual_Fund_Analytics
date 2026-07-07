<<<<<<< HEAD
import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Grades:")
=======
import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Grades:")
>>>>>>> 5e6528c2a8b061ca81cf7bebe5426257dfbb7c06
print(df["risk_category"].unique())