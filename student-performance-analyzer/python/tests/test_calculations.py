from student_analyzer.core.calculations import calculate_result
from student_analyzer.analytics.individual import analyze_student
from student_analyzer.analytics.class_analysis import analyze_class

def test_summary_calculation():
    result = calculate_result({"Math": 80, "English": 90})
    assert result["total"] == 170 and result["average"] == 85
    assert result["highest"] == 90 and result["lowest"] == 80 and result["grade"] == "A"

def test_zero_score_is_valid():
    assert calculate_result({"Math": 0, "English": 100})["grade"] == "D"

def test_individual_course_grades():
    result = analyze_student({"id":"S1","name":"Alex","scores":{"Math":80,"English":65}})
    assert result["grade"] == "B"
    assert result["course_results"][0]["grade"] == "A"

def test_class_ranking():
    report = analyze_class([{"id":"S1","name":"Alex","scores":{"Math":80}},
                            {"id":"S2","name":"Sam","scores":{"Math":90}}])
    assert report["rankings"][0]["student_id"] == "S2"
