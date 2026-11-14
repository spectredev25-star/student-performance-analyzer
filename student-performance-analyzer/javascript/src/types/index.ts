export interface StudentRecord { id: string; name: string; department?: string; scores: Record<string, number>; }
export interface GradingBand { minScore: number; grade: string; remark: string; }
export interface GradeResult { grade: string; performance: string; }
export interface CalculationResult {
  total: number; average: number; highest: number; lowest: number;
  grade: string; performance: string; scoreCount: number;
}
export interface CourseResult { course: string; score: number; grade: string; performance: string; }
export interface StudentAnalysis extends CalculationResult {
  studentId: string; name: string; department: string; courseResults: CourseResult[];
}
