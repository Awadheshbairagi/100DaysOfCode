# Write your MySQL query statement below
WITH Managers AS (
    SELECT e.employee_id, e.name
    FROM Employees e
    WHERE e.employee_id IN (SELECT DISTINCT reports_to FROM Employees WHERE reports_to IS NOT NULL)
)
SELECT m.employee_id, 
       m.name, 
       COUNT(e.employee_id) AS reports_count,
       ROUND(AVG(e.age)) AS average_age
FROM Managers m
JOIN Employees e ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;
