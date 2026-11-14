from pathlib import Path
import json
from ..inputs.json_reader import load_students_json
from ..inputs.csv_reader import load_students_csv
from ..analytics.class_analysis import analyze_class
from ..analytics.individual import analyze_student
from ..visualization.charts import create_average_chart

def load_records(path):
    suffix = Path(path).suffix.lower()
    if suffix == ".json": return load_students_json(path)
    if suffix == ".csv": return load_students_csv(path)
    raise ValueError("input must be a .json or .csv file")

def run_analyze(path):
    report = analyze_class(load_records(path))
    print(f"Students: {report['student_count']}")
    print(f"Class average: {report['class_average']:.2f}")
    print(f"Highest average: {report['highest_average']:.2f}")
    print(f"Lowest average: {report['lowest_average']:.2f}")
    print("Grade distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")
    print("Rankings:")
    for row in report["rankings"]:
        print(f"  {row['rank']}. {row['name']} — {row['average']:.2f}% ({row['grade']})")

def run_student(path, student_id):
    records = load_records(path)
    student = next((item for item in records if item["id"] == student_id), None)
    if student is None: raise ValueError(f"student {student_id!r} was not found")
    print(json.dumps(analyze_student(student), indent=2))

def run_chart(path, output):
    print(f"Chart saved to: {create_average_chart(load_records(path), output)}")
