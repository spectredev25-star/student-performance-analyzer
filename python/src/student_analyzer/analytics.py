"""Class-level descriptive statistics and rankings."""
from __future__ import annotations

from collections import Counter
from statistics import mean, median, pstdev
from .core import analyze_student, validate_students


def analyze_class(students: list[dict], grading_scale: list[dict] | None = None) -> dict:
    validate_students(students)
    results = [analyze_student(student, grading_scale) for student in students]
    ranked = sorted(results, key=lambda row: (-row["average"], row["id"]))
    rankings = [
        {"rank": index, "id": row["id"], "name": row["name"], "average": row["average"]}
        for index, row in enumerate(ranked, start=1)
    ]
    subjects = sorted({subject for student in students for subject in student["scores"]})
    subject_stats = {}
    for subject in subjects:
        values = [student["scores"][subject] for student in students if subject in student["scores"]]
        subject_stats[subject] = {
            "count": len(values),
            "average": round(mean(values), 2),
            "median": round(median(values), 2),
            "minimum": min(values),
            "maximum": max(values),
            "population_std_dev": round(pstdev(values), 2),
        }
    averages = [row["average"] for row in results]
    return {
        "student_count": len(results),
        "class_average": round(mean(averages), 2),
        "highest_student": rankings[0],
        "lowest_student": rankings[-1],
        "grade_distribution": dict(sorted(Counter(row["grade"] for row in results).items())),
        "rankings": rankings,
        "subject_statistics": subject_stats,
        "students": results,
    }
