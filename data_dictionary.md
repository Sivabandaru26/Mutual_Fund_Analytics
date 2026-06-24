# Mutual Fund Analytics - Data Dictionary

## fund_master

| Column | Description |
|----------|------------|
| amfi_code | Unique AMFI scheme code |
| fund_house | Mutual fund company |
| scheme_name | Name of the scheme |
| category | Fund category |
| sub_category | Fund sub-category |
| plan | Direct/Regular plan |
| launch_date | Scheme launch date |
| benchmark | Benchmark index |
| expense_ratio_pct | Expense ratio percentage |
| exit_load_pct | Exit load percentage |
| min_sip_amount | Minimum SIP amount |
| min_lumpsum_amount | Minimum lump sum investment |
| fund_manager | Fund manager name |
| risk_category | Risk category |
| sebi_category_code | SEBI category code |

---

## nav_history

| Column | Description |
|----------|------------|
| amfi_code | Unique AMFI code |
| date | NAV date |
| nav | Net Asset Value |

---

## scheme_performance

| Column | Description |
|----------|------------|
| amfi_code | AMFI code |
| scheme_name | Scheme name |
| fund_house | Fund house |
| category | Fund category |
| plan | Plan type |
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| benchmark_3yr_pct | Benchmark return |
| alpha | Alpha value |
| beta | Beta value |
| sharpe_ratio | Sharpe ratio |
| sortino_ratio | Sortino ratio |
| std_dev_ann_pct | Annualized standard deviation |
| max_drawdown_pct | Maximum drawdown |
| aum_crore | Assets under management |
| expense_ratio_pct | Expense ratio |
| morningstar_rating | Morningstar rating |
| risk_grade | Risk grade |

---

## investor_transactions

| Column | Description |
|----------|------------|
| investor_id | Investor ID |
| transaction_date | Transaction date |
| amfi_code | Scheme code |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| city_tier | City tier |
| age_group | Age group |
| gender | Investor gender |
| annual_income_lakh | Annual income |
| payment_mode | Payment mode |
| kyc_status | KYC verification status |

---

## aum_by_fund_house

| Column | Description |
|----------|------------|
| date | Reporting date |
| fund_house | Fund house |
| aum_lakh_crore | AUM in lakh crore |
| aum_crore | AUM in crore |
| num_schemes | Number of schemes |

---

## monthly_sip_inflows

| Column | Description |
|----------|------------|
| month | Month |
| sip_inflow_crore | SIP inflow |
| active_sip_accounts_crore | Active SIP accounts |
| new_sip_accounts_lakh | New SIP accounts |
| sip_aum_lakh_crore | SIP AUM |
| yoy_growth_pct | Year-on-year growth |

---

## category_inflows

| Column | Description |
|----------|------------|
| month | Month |
| category | Category name |
| net_inflow_crore | Net inflow amount |

---

## industry_folio_count

| Column | Description |
|----------|------------|
| month | Month |
| total_folios_crore | Total folios |
| equity_folios_crore | Equity folios |
| debt_folios_crore | Debt folios |
| hybrid_folios_crore | Hybrid folios |
| others_folios_crore | Other folios |

---

## portfolio_holdings

| Column | Description |
|----------|------------|
| amfi_code | AMFI code |
| stock_symbol | Stock symbol |
| stock_name | Stock name |
| sector | Sector |
| weight_pct | Portfolio weight |
| market_value_cr | Market value |
| current_price_inr | Current stock price |
| portfolio_date | Portfolio date |

---

## benchmark_indices

| Column | Description |
|----------|------------|
| date | Index date |
| index_name | Benchmark index name |
| close_value | Closing index value |