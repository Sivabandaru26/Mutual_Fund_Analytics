# 📊 Mutual Fund Analytics

A complete end-to-end Mutual Fund Analytics project developed as part of the **Bluestock Fintech Internship Capstone**.

The project builds a full data analytics pipeline covering data ingestion, cleaning, database creation, exploratory data analysis, performance analytics, advanced risk analytics, investor behavior analysis, and interactive dashboard visualization.

---

# Project Objectives

- Build an end-to-end ETL pipeline
- Clean and validate mutual fund datasets
- Store cleaned data in SQLite
- Perform Exploratory Data Analysis (EDA)
- Compute mutual fund performance metrics
- Perform advanced risk analytics
- Build a mutual fund recommendation engine
- Create an interactive Power BI dashboard

---

# Project Workflow

```
Raw CSV Files
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
EDA
      │
      ▼
Performance Analytics
      │
      ▼
Advanced Analytics
      │
      ▼
Recommendation Engine
      │
      ▼
Power BI Dashboard
```

---

# Features

## ETL Pipeline

- Data ingestion
- Data validation
- Missing value handling
- Duplicate removal
- Data quality checks
- Clean CSV generation

---

## Database

- SQLite Database
- Normalized schema
- SQL Queries
- Data Dictionary

---

## Exploratory Data Analysis

- NAV Trend Analysis
- SIP Growth Analysis
- AUM Analysis
- Fund House Analysis
- Category Inflows
- State-wise Investments
- Investor Demographics
- Portfolio Sector Allocation

Interactive charts generated using Plotly and Matplotlib.

---

## Performance Analytics

Calculated important mutual fund performance metrics including:

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown

Generated outputs:

- fund_performance_metrics.csv
- fund_scorecard.csv

---

## Advanced Analytics

Implemented advanced financial analytics including:

### Risk Analytics

- Historical Value at Risk (VaR)
- Conditional Value at Risk (CVaR)

Generated:

- var_cvar_report.csv

---

### Rolling Sharpe Ratio

Calculated rolling Sharpe Ratio to evaluate changing fund performance over time.

Generated:

- rolling_sharpe_chart.png

---

### Cohort Analysis

Analyzed investor retention using cohort-based analysis.

---

### Investor Risk Segmentation

Identified At-Risk Investors based on inactivity period.

---

### Portfolio Diversification

Calculated Sector Concentration using Herfindahl-Hirschman Index (HHI).

Generated:

- sector_hhi_report.csv

---

## Mutual Fund Recommendation System

Developed a recommendation engine based on:

- Risk Appetite
- Sharpe Ratio
- Annual Return
- Volatility

Risk Categories:

- Low Risk
- Moderate Risk
- High Risk

Returns Top Recommended Mutual Funds for investors.

---

## Power BI Dashboard

Interactive dashboard with multiple report pages including:

- Executive Summary
- Fund Performance
- Investor Insights
- Risk Analytics

Features:

- Interactive slicers
- KPI cards
- Trend charts
- Drill-down analysis

---

# Folder Structure

```
Mutual_Fund_Analytics/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   └── charts/
│
├── scripts/
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── README.md
├── requirements.txt
└── data_dictionary.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- SciPy
- SQLite
- SQLAlchemy
- Power BI
- Jupyter Notebook
- Git
- GitHub

---

# Project Deliverables

- ETL Pipeline
- Cleaned CSV Files
- SQLite Schema
- SQL Queries
- Data Dictionary
- EDA Notebook
- Performance Analytics Notebook
- Advanced Analytics Notebook
- Recommendation Engine
- Power BI Dashboard
- Technical Documentation
- Charts and Reports

---

# Outputs

Generated reports include:

- Fund Scorecard
- Performance Metrics
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Sector HHI Report
- Rolling Sharpe Ratio Chart
- EDA Charts
- Performance Charts

---

# Future Enhancements

- Streamlit Dashboard
- Live NAV API Integration
- Portfolio Optimizer
- Monte Carlo Simulation
- Automated Email Reporting

---

# Author

**Ratna Siva Kumar Bandaru**

Bluestock Fintech Internship Capstone Project