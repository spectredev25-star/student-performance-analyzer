import os
from contextlib import contextmanager

@contextmanager
def get_connection():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError("Install psycopg with pip install 'psycopg[binary]'") from exc
    connection = psycopg.connect(url)
    try:
        yield connection
    finally:
        connection.close()

def fetch_students():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT s.student_id, s.full_name, s.department, c.course_name, r.score
            FROM students s JOIN results r USING (student_id)
            JOIN courses c USING (course_id)
            ORDER BY s.student_id, c.course_name
        """).fetchall()
    grouped = {}
    for sid, name, department, course, score in rows:
        grouped.setdefault(sid, {"id": sid, "name": name, "department": department or "", "scores": {}})
        grouped[sid]["scores"][course] = float(score)
    return list(grouped.values())
