SELECT c.course_name,COUNT(r.result_id) AS student_count,ROUND(AVG(r.score),2) AS course_average,
       MAX(r.score) AS highest_score,MIN(r.score) AS lowest_score
FROM courses c LEFT JOIN results r USING(course_id)
GROUP BY c.course_id,c.course_name ORDER BY c.course_name;
