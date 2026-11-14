# Data contracts

Student input:
```json
{"id":"STU001","name":"Alex","department":"Computer Engineering","scores":{"Mathematics":78,"Programming":85}}
```
`id`, `name`, and non-empty `scores` are required. Scores are finite numbers from 0 to 100. `department` is optional.

Individual result includes `student_id`, `name`, `total`, `average`, `highest`, `lowest`, `grade`, `performance`, `score_count`, and `course_results`.
