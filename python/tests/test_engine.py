import json
from pathlib import Path
import pytest
from student_analyzer import analyze_student, analyze_class

FIXTURES = Path(__file__).parents[2] / "shared" / "fixtures" / "calculation-cases.json"


def cases():
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def test_shared_student_expected_results():
    fixture = cases()
    for case in fixture["student_cases"]:
        assert analyze_student(case["input"]) == case["expected"]


def test_shared_class_expected_results():
    fixture = cases()
    assert analyze_class(fixture["class_case"]["input"]) == fixture["class_case"]["expected"]


@pytest.mark.parametrize("scores", [{}, {"Math": -1}, {"Math": 101}, {"Math": "90"}, {"Math": True}])
def test_invalid_scores_are_rejected(scores):
    with pytest.raises(ValueError):
        analyze_student({"id": "X1", "name": "Test", "scores": scores})


def test_duplicate_ids_are_rejected():
    students = [{"id": "X", "name": "A", "scores": {"Math": 70}},
                {"id": "X", "name": "B", "scores": {"Math": 80}}]
    with pytest.raises(ValueError, match="Duplicate"):
        analyze_class(students)
