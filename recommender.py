import pandas as pd
from pathlib import Path

# -----------------------------
# Load scorecard data
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent

scorecard = pd.read_csv(
    BASE_DIR / "data" / "processed" / "fund_scorecard.csv"
)

# -----------------------------
# Create Risk Grade
# -----------------------------
def assign_risk(volatility):
    if volatility < 0.15:
        return "Low"
    elif volatility < 0.18:
        return "Moderate"
    else:
        return "High"

scorecard["risk_grade"] = scorecard["annual_volatility"].apply(assign_risk)

# -----------------------------
# User Input
# -----------------------------
risk = input("Enter Risk Appetite (Low / Moderate / High): ").strip().title()

# -----------------------------
# Filter Funds
# -----------------------------
recommended = (
    scorecard[scorecard["risk_grade"] == risk]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

# -----------------------------
# Display Recommendation
# -----------------------------
print("\nTop 3 Recommended Funds\n")

print(
    recommended[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "annual_return",
            "annual_volatility",
        ]
    ]
)