export type Student = {
  id: string; name: string; department?: string;
  scores: Record<string, number>;
};
export type GradeBand = { min: number; grade: string; remark: string };
export const DEFAULT_GRADING_SCALE: GradeBand[] = [
  {min:80,grade:"A",remark:"Excellent"},
  {min:70,grade:"B",remark:"Very Good"},
  {min:60,grade:"C",remark:"Good"},
  {min:50,grade:"D",remark:"Pass"},
  {min:0,grade:"F",remark:"Needs Improvement"}
];
export function validateStudent(student: Student): void {
  if (!student || typeof student !== "object") throw new Error("Each student must be an object.");
  if (!student.id?.trim()) throw new Error("Student id must be a non-empty string.");
  if (!student.name?.trim()) throw new Error("Student name must be a non-empty string.");
  if (!student.scores || typeof student.scores !== "object" || Array.isArray(student.scores) || Object.keys(student.scores).length === 0)
    throw new Error(`${student.id}: scores must be a non-empty object.`);
  for (const [subject, score] of Object.entries(student.scores)) {
    if (!subject.trim()) throw new Error("Subject names must be non-empty strings.");
    if (typeof score !== "number" || !Number.isFinite(score)) throw new Error(`${student.id}: ${subject} score must be numeric.`);
    if (score < 0 || score > 100) throw new Error(`${student.id}: ${subject} score must be between 0 and 100.`);
  }
}
export function validateStudents(students: Student[]): void {
  if (!Array.isArray(students) || students.length === 0) throw new Error("Provide a non-empty list of students.");
  const ids = new Set<string>();
  for (const student of students) {
    validateStudent(student);
    if (ids.has(student.id)) throw new Error(`Duplicate student id: ${student.id}`);
    ids.add(student.id);
  }
}
export function getGrade(score: number, scale: GradeBand[] = DEFAULT_GRADING_SCALE) {
  const band = [...scale].sort((a,b)=>b.min-a.min).find(item=>score>=item.min);
  if (!band) throw new Error("Grading scale must include a minimum boundary of 0.");
  return {grade:band.grade,remark:band.remark};
}
export function analyzeStudent(student: Student, scale: GradeBand[] = DEFAULT_GRADING_SCALE) {
  validateStudent(student);
  const entries = Object.entries(student.scores);
  const total = entries.reduce((sum,[,score])=>sum+score,0);
  const average = total / entries.length;
  const highest = entries.reduce((best,current)=>current[1]>best[1]?current:best);
  const lowest = entries.reduce((best,current)=>current[1]<best[1]?current:best);
  const overall = getGrade(average,scale);
  const subjectResults = Object.fromEntries(entries.map(([subject,score])=>[subject,{score,...getGrade(score,scale)}]));
  return {
    id:student.id,name:student.name,department:student.department ?? null,
    total:Number(total.toFixed(2)),average:Number(average.toFixed(2)),
    highest_subject:highest[0],highest_score:highest[1],
    lowest_subject:lowest[0],lowest_score:lowest[1],
    grade:overall.grade,remark:overall.remark,subject_results:subjectResults
  };
}
function round(value:number):number { return Number(value.toFixed(2)); }
export function analyzeClass(students: Student[], scale: GradeBand[] = DEFAULT_GRADING_SCALE) {
  validateStudents(students);
  const results = students.map(student=>analyzeStudent(student,scale));
  const ranked = [...results].sort((a,b)=>b.average-a.average || a.id.localeCompare(b.id));
  const rankings = ranked.map((row,index)=>({rank:index+1,id:row.id,name:row.name,average:row.average}));
  const subjects = [...new Set(students.flatMap(student=>Object.keys(student.scores)))].sort();
  const subjectStatistics = Object.fromEntries(subjects.map(subject=>{
    const values=students.flatMap(student=>subject in student.scores?[student.scores[subject]]:[]);
    const sorted=[...values].sort((a,b)=>a-b);
    const avg=values.reduce((a,b)=>a+b,0)/values.length;
    const middle=Math.floor(sorted.length/2);
    const med=sorted.length%2?sorted[middle]:(sorted[middle-1]+sorted[middle])/2;
    const variance=values.reduce((sum,value)=>sum+(value-avg)**2,0)/values.length;
    return [subject,{count:values.length,average:round(avg),median:round(med),minimum:Math.min(...values),maximum:Math.max(...values),population_std_dev:round(Math.sqrt(variance))}];
  }));
  const gradeDistribution:Record<string,number> = {};
  for (const row of results) gradeDistribution[row.grade]=(gradeDistribution[row.grade]??0)+1;
  const sortedGrades=Object.fromEntries(Object.entries(gradeDistribution).sort(([a],[b])=>a.localeCompare(b)));
  return {
    student_count:results.length,
    class_average:round(results.reduce((sum,row)=>sum+row.average,0)/results.length),
    highest_student:rankings[0],lowest_student:rankings[rankings.length-1],
    grade_distribution:sortedGrades,rankings,subject_statistics:subjectStatistics,students:results
  };
}
