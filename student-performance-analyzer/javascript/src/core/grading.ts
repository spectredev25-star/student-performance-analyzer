import type { GradeResult, GradingBand } from "../types/index";

export const DEFAULT_GRADING_SCALE: GradingBand[] = [
  {minScore:80,grade:"A",remark:"Excellent"},
  {minScore:70,grade:"B",remark:"Very Good"},
  {minScore:60,grade:"C",remark:"Good"},
  {minScore:50,grade:"D",remark:"Pass"},
  {minScore:0,grade:"F",remark:"Needs Improvement"},
];

export function validateGradingScale(scale: GradingBand[]): GradingBand[] {
  if (!Array.isArray(scale) || scale.length === 0) throw new Error("grading scale cannot be empty");
  const grades = new Set<string>();
  const sorted = scale.map((band) => {
    if (!Number.isFinite(band.minScore) || band.minScore < 0 || band.minScore > 100) throw new Error("invalid threshold");
    if (!band.grade?.trim() || grades.has(band.grade)) throw new Error("grade labels must be unique");
    if (!band.remark?.trim()) throw new Error("remark is required");
    grades.add(band.grade);
    return {...band};
  }).sort((a,b) => b.minScore-a.minScore);
  if (sorted[sorted.length-1].minScore !== 0 || new Set(sorted.map(x=>x.minScore)).size !== sorted.length)
    throw new Error("grading scale must have unique thresholds and include zero");
  return sorted;
}

export function getGrade(score: number, gradingScale: GradingBand[] = DEFAULT_GRADING_SCALE): GradeResult {
  if (!Number.isFinite(score) || score < 0 || score > 100) throw new Error("score must be from 0 to 100");
  const band = validateGradingScale(gradingScale).find(item => score >= item.minScore);
  if (!band) throw new Error("grading scale does not cover score");
  return {grade:band.grade,performance:band.remark};
}
