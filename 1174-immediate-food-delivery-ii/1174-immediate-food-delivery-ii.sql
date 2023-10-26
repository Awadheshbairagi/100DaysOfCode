WITH FirstOrders AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS immediate_percentage
FROM Delivery d
JOIN FirstOrders fo ON d.customer_id = fo.customer_id
WHERE d.order_date = fo.first_order_date;
