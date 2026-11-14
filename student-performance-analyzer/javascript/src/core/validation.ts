import type { StudentRecord } from "../types/index";

export function validateScores(scores: Record<string, number>): void {
  if (!scores || typeof scores !== "object" || Array.isArray(scores) || Object.keys(scores).length === 0)
    throw new Error("scores must be a non-empty course-to-score object");
  for (const [course, score] of Object.entries(scores)) {
    if (!course.trim()) throw new Error("course name cannot be empty");
    if (typeof score !== "number" || !Number.isFinite(score) || score < 0 || score > 100)
      throw new Error(`score for ${course} must be from 0 to 100`);
  }
}

export function validateStudent(student: StudentRecord): StudentRecord {
  if (!student || typeof student !== "object") throw new Error("student must be an object");
  if (typeof student.id !== "string" || !student.id.trim()) throw new Error("id is required");
  if (typeof student.name !== "string" || !student.name.trim()) throw new Error("name is required");
  if (student.department !== undefined && typeof student.department !== "string") throw new Error("department must be text");
  validateScores(student.scores);
  return student;
}

export function validateStudents(students: StudentRecord[]): StudentRecord[] {
  if (!Array.isArray(students) || students.length === 0) throw new Error("at least one student is required");
  const ids = new Set<string>();
  for (const student of students) {
    validateStudent(student);
    if (ids.has(student.id)) throw new Error(`duplicate student id: ${student.id}`);
    ids.add(student.id);
  }
  return students;
}
