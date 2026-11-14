from typing import Any
from ..core.calculations import calculate_result
from ..core.grading import get_grade
from ..core.validation import validate_student

def analyze_student(student: dict[str, Any], grading_scale=None) -> dict[str, Any]:
    validate_student(student)
    summary = calculate_result(student["scores"], grading_scale)
    courses = []
    for course, score in student["scores"].items():
        courses.append({"course": course, "score": score, **get_grade(score, grading_scale)})
    return {"student_id": student["id"], "name": student["name"],
            "department": student.get("department", ""), **summary, "course_results": courses}
