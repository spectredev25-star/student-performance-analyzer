from math import isfinite
from typing import Any

DEFAULT_GRADING_SCALE = [
    {"min_score": 80, "grade": "A", "remark": "Excellent"},
    {"min_score": 70, "grade": "B", "remark": "Very Good"},
    {"min_score": 60, "grade": "C", "remark": "Good"},
    {"min_score": 50, "grade": "D", "remark": "Pass"},
    {"min_score": 0, "grade": "F", "remark": "Needs Improvement"},
]

def validate_grading_scale(scale: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not isinstance(scale, list) or not scale:
        raise ValueError("grading scale must be a non-empty list")
    normalized, grades = [], set()
    for band in scale:
        if not isinstance(band, dict):
            raise ValueError("each grading band must be an object")
        minimum, grade, remark = band.get("min_score"), band.get("grade"), band.get("remark")
        if isinstance(minimum, bool) or not isinstance(minimum, (int, float)) or not isfinite(minimum) or not 0 <= minimum <= 100:
            raise ValueError("min_score must be between 0 and 100")
        if not isinstance(grade, str) or not grade.strip() or grade in grades:
            raise ValueError("grade labels must be non-empty and unique")
        if not isinstance(remark, str) or not remark.strip():
            raise ValueError("each band needs a remark")
        grades.add(grade)
        normalized.append({"min_score": float(minimum), "grade": grade, "remark": remark})
    normalized.sort(key=lambda x: x["min_score"], reverse=True)
    if normalized[-1]["min_score"] != 0 or len({x["min_score"] for x in normalized}) != len(normalized):
        raise ValueError("grading scale must have unique thresholds and include zero")
    return normalized

def get_grade(score: float, grading_scale: list[dict[str, Any]] | None = None) -> dict[str, str]:
    if isinstance(score, bool) or not isinstance(score, (int, float)) or not isfinite(score) or not 0 <= score <= 100:
        raise ValueError("score must be a finite number from 0 to 100")
    for band in validate_grading_scale(grading_scale or DEFAULT_GRADING_SCALE):
        if score >= band["min_score"]:
            return {"grade": band["grade"], "performance": band["remark"]}
    raise ValueError("grading scale does not cover this score")
