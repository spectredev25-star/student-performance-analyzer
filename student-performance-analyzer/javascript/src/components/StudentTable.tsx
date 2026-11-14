import React from "react";
import type {StudentAnalysis} from "../types/index";
import {GradeBadge} from "./GradeBadge";
export function StudentTable({students}:{students:StudentAnalysis[]}) {
  if (!students.length) return <p>No student records available.</p>;
  return <div className="spa-table-wrapper"><table className="spa-student-table">
    <thead><tr><th>Student</th><th>Department</th><th>Total</th><th>Average</th><th>Grade</th></tr></thead>
    <tbody>{students.map(s=><tr key={s.studentId}><td>{s.name}</td><td>{s.department||"—"}</td>
      <td>{s.total}</td><td>{s.average.toFixed(2)}%</td><td><GradeBadge grade={s.grade} performance={s.performance}/></td></tr>)}</tbody>
  </table></div>;
}
