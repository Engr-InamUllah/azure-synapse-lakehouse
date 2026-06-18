CREATE OR ALTER VIEW gold.vw_regional_sales AS
SELECT region, DATEFROMPARTS(YEAR(order_date),MONTH(order_date),1) AS sales_month,
       SUM(quantity) AS units, SUM(quantity * unit_price) AS revenue
FROM silver.sales
GROUP BY region, DATEFROMPARTS(YEAR(order_date),MONTH(order_date),1);