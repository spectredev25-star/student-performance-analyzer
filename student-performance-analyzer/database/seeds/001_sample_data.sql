INSERT INTO students(student_id,full_name,department) VALUES
('STU001','Alex','Computer Engineering'),('STU002','Sarah','Computer Engineering'),
('STU003','John','Mechanical Engineering'),('STU004','Mary','Computer Engineering'),
('STU005','David','Mechanical Engineering')
ON CONFLICT(student_id) DO NOTHING;

INSERT INTO courses(course_code,course_name) VALUES
('MTH101','Mathematics'),('CSC101','Programming'),('PHY101','Physics'),
('CSC201','Databases'),('GST101','English')
ON CONFLICT(course_name) DO NOTHING;

INSERT INTO results(student_id,course_id,score)
SELECT v.student_id,c.course_id,v.score FROM (VALUES
('STU001','Mathematics',78.00),('STU001','Programming',85.00),('STU001','Physics',90.00),('STU001','Databases',67.00),('STU001','English',88.00),
('STU002','Mathematics',90.00),('STU002','Programming',92.00),('STU002','Physics',85.00),('STU002','Databases',89.00),('STU002','English',95.00),
('STU003','Mathematics',45.00),('STU003','Programming',56.00),('STU003','Physics',67.00),('STU003','Databases',55.00),('STU003','English',60.00),
('STU004','Mathematics',80.00),('STU004','Programming',75.00),('STU004','Physics',88.00),('STU004','Databases',92.00),('STU004','English',85.00),
('STU005','Mathematics',35.00),('STU005','Programming',42.00),('STU005','Physics',48.00),('STU005','Databases',50.00),('STU005','English',39.00)
) AS v(student_id,course_name,score) JOIN courses c ON c.course_name=v.course_name
ON CONFLICT(student_id,course_id) DO NOTHING;
