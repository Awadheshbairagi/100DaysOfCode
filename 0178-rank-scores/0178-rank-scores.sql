SELECT S.score, COUNT(S2.score) AS "Rank" FROM Scores S,
(SELECT DISTINCT score FROM Scores) S2
WHERE S.score<=S2.score
GROUP BY S.Id
ORDER BY S.score DESC;