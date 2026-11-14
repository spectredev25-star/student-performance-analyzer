CREATE TABLE IF NOT EXISTS students (
  student_id VARCHAR(30) PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  department VARCHAR(120),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS courses (
  course_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  course_code VARCHAR(30) UNIQUE,
  course_name VARCHAR(120) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS results (
  result_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  student_id VARCHAR(30) NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
  course_id BIGINT NOT NULL REFERENCES courses(course_id),
  score NUMERIC(5,2) NOT NULL CHECK (score >= 0 AND score <= 100),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(student_id,course_id)
);
CREATE INDEX IF NOT EXISTS idx_results_student ON results(student_id);
CREATE INDEX IF NOT EXISTS idx_results_course ON results(course_id);
