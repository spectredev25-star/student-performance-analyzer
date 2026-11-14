import json
from pathlib import Path
from ..core.validation import validate_students

def load_students_json(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("JSON file must contain a list of student records")
    return validate_students(data)
