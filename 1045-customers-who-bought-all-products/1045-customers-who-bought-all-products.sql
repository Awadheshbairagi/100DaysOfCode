# Write your MySQL query statement below
SELECT customer_id
FROM Customer
WHERE product_key IN (SELECT product_key FROM Product)
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
