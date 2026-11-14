import type { CalculationResult, GradingBand, StudentAnalysis, StudentRecord } from "../types/index";
import {getGrade,DEFAULT_GRADING_SCALE} from "./grading";
import {validateScores,validateStudent,validateStudents} from "./validation";

export function calculateResult(scores: Record<string,number>, gradingScale: GradingBand[] = DEFAULT_GRADING_SCALE): CalculationResult {
  validateScores(scores);
  const values = Object.values(scores);
  const total = values.reduce((sum,score)=>sum+score,0);
  const average = total/values.length;
  const gradeInfo = getGrade(average,gradingScale);
  return {total,average,highest:Math.max(...values),lowest:Math.min(...values),
    grade:gradeInfo.grade,performance:gradeInfo.performance,scoreCount:values.length};
}

export function analyzeStudent(student: StudentRecord, gradingScale: GradingBand[] = DEFAULT_GRADING_SCALE): StudentAnalysis {
  validateStudent(student);
  const summary = calculateResult(student.scores,gradingScale);
  const courseResults = Object.entries(student.scores).map(([course,score])=>({course,score,...getGrade(score,gradingScale)}));
  return {studentId:student.id,name:student.name,department:student.department??"",...summary,courseResults};
}

export function analyzeClass(students: StudentRecord[], gradingScale: GradingBand[] = DEFAULT_GRADING_SCALE) {
  validateStudents(students);
  const analyses = students.map(s=>analyzeStudent(s,gradingScale));
  const averages = analyses.map(s=>s.average);
  const gradeDistribution: Record<string,number> = {};
  for (const item of analyses) gradeDistribution[item.grade]=(gradeDistribution[item.grade]??0)+1;
  const rankings = [...analyses].sort((a,b)=>b.average-a.average).map((s,i)=>({
    rank:i+1,studentId:s.studentId,name:s.name,average:s.average,grade:s.grade
  }));
  return {studentCount:analyses.length,classAverage:averages.reduce((a,b)=>a+b,0)/averages.length,
    highestAverage:Math.max(...averages),lowestAverage:Math.min(...averages),gradeDistribution,rankings,students:analyses};
}
