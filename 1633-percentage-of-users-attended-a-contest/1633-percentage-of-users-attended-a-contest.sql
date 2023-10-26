SELECT contest_id,
       ROUND(COUNT(user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
WHERE user_id IN (SELECT user_id FROM Users)
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
