import pytest
from student_analyzer.core.grading import get_grade, validate_grading_scale

@pytest.mark.parametrize("score,grade", [(80,"A"),(79.99,"B"),(70,"B"),(60,"C"),(50,"D"),(0,"F"),(100,"A")])
def test_grade_thresholds(score, grade):
    assert get_grade(score)["grade"] == grade

def test_scale_must_include_zero():
    with pytest.raises(ValueError):
        validate_grading_scale([{"min_score":50,"grade":"A","remark":"Good"}])
