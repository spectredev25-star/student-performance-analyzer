from typing import Any
from .grading import get_grade
from .validation import validate_scores

def calculate_result(scores: dict[str, Any], grading_scale=None) -> dict[str, Any]:
    """Calculate summary metrics and grade based on the student's average."""
    validate_scores(scores)
    values = list(scores.values())
    total = sum(values)
    average = total / len(values)
    grade_info = get_grade(average, grading_scale)
    return {"total": total, "average": average, "highest": max(values), "lowest": min(values),
            "grade": grade_info["grade"], "performance": grade_info["performance"], "score_count": len(values)}
