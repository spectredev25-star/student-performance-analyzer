from math import isfinite
from typing import Any, Iterable

class ValidationError(ValueError):
    """Raised when student data or a score is invalid."""

def validate_scores(scores: dict[str, Any]) -> None:
    if not isinstance(scores, dict) or not scores:
        raise ValidationError("scores must be a non-empty course-to-score dictionary")
    for course, score in scores.items():
        if not isinstance(course, str) or not course.strip():
            raise ValidationError("course names must be non-empty strings")
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise ValidationError(f"score for {course!r} must be numeric")
        if not isfinite(score) or not 0 <= score <= 100:
            raise ValidationError(f"score for {course!r} must be between 0 and 100")

def validate_student(student: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(student, dict):
        raise ValidationError("student must be an object")
    for field in ("id", "name"):
        if not isinstance(student.get(field), str) or not student[field].strip():
            raise ValidationError(f"{field} must be a non-empty string")
    if not isinstance(student.get("department", ""), str):
        raise ValidationError("department must be a string")
    validate_scores(student.get("scores"))
    return student

def validate_students(students: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    if isinstance(students, (str, bytes, dict)):
        raise ValidationError("students must be an iterable of student objects")
    records = list(students)
    if not records:
        raise ValidationError("at least one student is required")
    seen = set()
    for student in records:
        validate_student(student)
        if student["id"] in seen:
            raise ValidationError(f"duplicate student id: {student['id']}")
        seen.add(student["id"])
    return records
