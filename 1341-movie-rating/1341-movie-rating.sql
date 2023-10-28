# Write your MySQL query statement below
WITH UserRatings AS (
    SELECT u.name AS user_name, COUNT(*) AS num_ratings
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.user_id
    ORDER BY num_ratings DESC, user_name ASC LIMIT 1
),
MovieAvgRatings AS (
    SELECT m.title AS movie_title, AVG(mr.rating) AS avg_rating
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE YEAR(mr.created_at) = 2020 AND MONTH(mr.created_at) = 2
    GROUP BY m.movie_id
    ORDER BY avg_rating DESC, movie_title ASC LIMIT 1
)
SELECT user_name AS results FROM UserRatings
UNION ALL
SELECT movie_title FROM MovieAvgRatings;
