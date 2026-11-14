"""Validated, configurable individual-student calculations."""
from __future__ import annotations

from typing import Any, Mapping

DEFAULT_GRADING_SCALE = [
    {"min": 80, "grade": "A", "remark": "Excellent"},
    {"min": 70, "grade": "B", "remark": "Very Good"},
    {"min": 60, "grade": "C", "remark": "Good"},
    {"min": 50, "grade": "D", "remark": "Pass"},
    {"min": 0, "grade": "F", "remark": "Needs Improvement"},
]


def validate_student(student: Mapping[str, Any]) -> None:
    if not isinstance(student, Mapping):
        raise ValueError("Each student must be an object.")
    for field in ("id", "name", "scores"):
        if field not in student:
            raise ValueError(f"Missing required field: {field}")
    if not isinstance(student["id"], str) or not student["id"].strip():
        raise ValueError("Student id must be a non-empty string.")
    if not isinstance(student["name"], str) or not student["name"].strip():
        raise ValueError("Student name must be a non-empty string.")
    scores = student["scores"]
    if not isinstance(scores, Mapping) or not scores:
        raise ValueError(f"{student['id']}: scores must be a non-empty object.")
    for subject, score in scores.items():
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject names must be non-empty strings.")
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise ValueError(f"{student['id']}: {subject} score must be numeric.")
        if not 0 <= score <= 100:
            raise ValueError(f"{student['id']}: {subject} score must be between 0 and 100.")


def validate_students(students: list[Mapping[str, Any]]) -> None:
    if not isinstance(students, list) or not students:
        raise ValueError("Provide a non-empty list of students.")
    seen: set[str] = set()
    for student in students:
        validate_student(student)
        student_id = student["id"]
        if student_id in seen:
            raise ValueError(f"Duplicate student id: {student_id}")
        seen.add(student_id)


def get_grade(score: float, grading_scale: list[dict] | None = None) -> dict[str, str]:
    scale = grading_scale or DEFAULT_GRADING_SCALE
    for band in sorted(scale, key=lambda item: item["min"], reverse=True):
        if score >= band["min"]:
            return {"grade": band["grade"], "remark": band["remark"]}
    raise ValueError("Grading scale must include a minimum boundary of 0.")


def analyze_student(student: Mapping[str, Any], grading_scale: list[dict] | None = None) -> dict:
    validate_student(student)
    scores = dict(student["scores"])
    total = sum(scores.values())
    average = total / len(scores)
    highest = max(scores, key=scores.get)
    lowest = min(scores, key=scores.get)
    overall = get_grade(average, grading_scale)
    subject_results = {}
    for subject, score in scores.items():
        subject_grade = get_grade(score, grading_scale)
        subject_results[subject] = {
            "score": score,
            "grade": subject_grade["grade"],
            "remark": subject_grade["remark"],
        }
    return {
        "id": student["id"],
        "name": student["name"],
        "department": student.get("department"),
        "total": round(total, 2),
        "average": round(average, 2),
        "highest_subject": highest,
        "highest_score": scores[highest],
        "lowest_subject": lowest,
        "lowest_score": scores[lowest],
        "grade": overall["grade"],
        "remark": overall["remark"],
        "subject_results": subject_results,
    }
