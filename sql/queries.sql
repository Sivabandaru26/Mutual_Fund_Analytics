-- 1 Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV per Month

SELECT
strftime('%Y-%m', date) AS month,
ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY month;

-- 3 SIP YoY Growth

SELECT month, yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- 4 Transactions by State

SELECT state,
COUNT(*) AS transactions
FROM investor_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 5 Funds with Expense Ratio below 1%

SELECT scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6 Top Performing Funds

SELECT scheme_name,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7 Highest Sharpe Ratio Funds

SELECT scheme_name,
sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8 Category Wise Net Inflows

SELECT category,
SUM(net_inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

-- 9 Fund House Wise AUM

SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 10 Top Portfolio Holdings

SELECT stock_name,
SUM(weight_pct) AS total_weight
FROM portfolio_holdings
GROUP BY stock_name
ORDER BY total_weight DESC
LIMIT 10;