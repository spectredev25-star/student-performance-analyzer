SELECT s.student_id,s.full_name,ROUND(AVG(r.score),2) AS average_score,
       SUM(r.score) AS total_score,MAX(r.score) AS highest_score,MIN(r.score) AS lowest_score
FROM students s JOIN results r USING(student_id)
GROUP BY s.student_id,s.full_name ORDER BY average_score DESC;
