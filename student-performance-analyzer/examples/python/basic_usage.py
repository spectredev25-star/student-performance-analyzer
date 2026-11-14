import json
from pathlib import Path
from student_analyzer import analyze_student, analyze_class

root = Path(__file__).resolve().parents[2]
records = json.loads((root / "shared/fixtures/students.json").read_text(encoding="utf-8"))
print(analyze_student(records[0]))
print(analyze_class(records)["rankings"])
