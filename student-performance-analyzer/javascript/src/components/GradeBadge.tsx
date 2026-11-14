import React from "react";
export function GradeBadge({grade,performance}:{grade:string;performance?:string}) {
  return <span className={`spa-grade-badge spa-grade-${grade.toLowerCase()}`} title={performance}>{grade}{performance?` — ${performance}`:""}</span>;
}
