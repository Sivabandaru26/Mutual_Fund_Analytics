import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Original Shape:", df.shape)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df.drop_duplicates()

df = df[df["close_value"] > 0]

df.to_csv(
    "data/processed/benchmark_indices_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Benchmark Indices cleaned successfully!")
