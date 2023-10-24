# Write your MySQL query statement below
SELECT
    Employee.name, Bonus.bonus
FROM
    Employee
        LEFT OUTER JOIN
    Bonus ON Employee.empid = Bonus.empid
    
WHERE
    bonus < 1000 OR bonus IS NULL
;