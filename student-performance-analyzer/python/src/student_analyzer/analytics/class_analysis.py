from collections import Counter
from ..core.validation import validate_students
from .individual import analyze_student
from .statistics import summarize_scores

def analyze_class(students, grading_scale=None):
    records = validate_students(students)
    results = [analyze_student(student, grading_scale) for student in records]
    averages = [item["average"] for item in results]
    ranked = sorted(results, key=lambda item: item["average"], reverse=True)
    course_scores = {}
    for student in records:
        for course, score in student["scores"].items():
            course_scores.setdefault(course, []).append(score)
    return {
        "student_count": len(results),
        "class_average": sum(averages) / len(averages),
        "highest_average": max(averages),
        "lowest_average": min(averages),
        "grade_distribution": dict(Counter(item["grade"] for item in results)),
        "rankings": [{"rank": i, "student_id": item["student_id"], "name": item["name"],
                      "average": item["average"], "grade": item["grade"]}
                     for i, item in enumerate(ranked, 1)],
        "course_analysis": {course: summarize_scores(scores) for course, scores in course_scores.items()},
        "students": results,
    }
