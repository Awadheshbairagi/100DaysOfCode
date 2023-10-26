# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) as unit
FROM Products p
LEFT JOIN Orders o
ON p.product_id = o.product_id
AND EXTRACT(YEAR_MONTH FROM o.order_date) = 202002
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
