import csv
from pathlib import Path
from ..core.validation import validate_students

def load_students_csv(path):
    """Read long-format CSV: id,name,department,course,score."""
    grouped = {}
    with Path(path).open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        required = {"id", "name", "department", "course", "score"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV headers must include id,name,department,course,score")
        for row in reader:
            sid, course = row["id"].strip(), row["course"].strip()
            if not sid or not course:
                raise ValueError("student id and course cannot be empty")
            if sid not in grouped:
                grouped[sid] = {"id": sid, "name": row["name"].strip(),
                                "department": row["department"].strip(), "scores": {}}
            if course in grouped[sid]["scores"]:
                raise ValueError(f"duplicate course {course!r} for student {sid}")
            try:
                grouped[sid]["scores"][course] = float(row["score"])
            except ValueError as exc:
                raise ValueError(f"invalid score for {sid}/{course}") from exc
    return validate_students(list(grouped.values()))
