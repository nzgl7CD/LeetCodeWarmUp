WITH daily_returns AS (
  SELECT 
    asset_id,
    trade_date,
    (close_price - LAG(close_price) OVER (PARTITION BY asset_id ORDER BY trade_date)) 
    -- Time series analysis
     / LAG(close_price) OVER (PARTITION BY asset_id ORDER BY trade_date) AS daily_return
    FROM asset_prices
)

SELECT 
  asset_id,
  AVG(daily_return) AS avg_return,
  STDEV(daily_return) AS volatility,
  AVG(daily_return) / STDEV(daily_return) AS sharpe_ratio
FROM daily_returns

--  Aggregation and statistical functions:
GROUP BY asset_id
HAVING COUNT(*) >= 252  -- Assuming 252 trading days in a year
ORDER BY sharpe_ratio DESC;


-- Procedures are made to make triggers and automated actions in addition to temporary tables

-- INNER JOIN: Returns only the rows that have matching values in both tables.
-- LEFT JOIN (or LEFT OUTER JOIN): Returns all the rows from the left table and the matched rows from the right table. If there’s no match, NULL values will be shown for columns from the right table.
-- RIGHT JOIN (or RIGHT OUTER JOIN): Returns all the rows from the right table and the matched rows from the left table. If there’s no match, NULL values will be shown for columns from the left table.
-- FULL JOIN (or FULL OUTER JOIN): Returns all rows from both tables, with NULLs in places where there is no match.

SELECT Employees.first_name, Departments.department_name
FROM Employees
INNER JOIN Departments ON Employees.department_id = Departments.department_id;