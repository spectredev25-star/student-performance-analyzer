import pytest
from student_analyzer.core.validation import ValidationError, validate_student, validate_students

@pytest.mark.parametrize("score", [-1,101,"80",None,True,float("nan"),float("inf")])
def test_reject_invalid_scores(score):
    student = {"id":"S1","name":"Alex","scores":{"Math":score}}
    with pytest.raises(ValidationError): validate_student(student)

def test_reject_empty_scores():
    with pytest.raises(ValidationError):
        validate_student({"id":"S1","name":"Alex","scores":{}})

def test_reject_duplicate_ids():
    student = {"id":"S1","name":"Alex","scores":{"Math":80}}
    with pytest.raises(ValidationError): validate_students([student, student])
