# Write your MySQL query statement below
-- Retrieving employees with primary_flag set to 'Y'
SELECT 
  employee_id, 
  department_id 
FROM 
  Employee 
WHERE 
  primary_flag = 'Y' 
UNION 
-- Retrieving employees that appear exactly once in the Employee table
SELECT 
  employee_id, 
  department_id 
FROM 
  Employee 
GROUP BY 
  employee_id 
HAVING 
  COUNT(employee_id) = 1;
