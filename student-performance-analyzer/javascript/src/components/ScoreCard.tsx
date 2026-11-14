import React from "react";
import type {CalculationResult} from "../types/index";
export function ScoreCard({result,studentName}:{result:CalculationResult;studentName?:string}) {
  return <section aria-label="Score summary" className="spa-score-card">
    {studentName && <h3>{studentName}</h3>}
    <dl>
      <div><dt>Total</dt><dd>{result.total}</dd></div>
      <div><dt>Average</dt><dd>{result.average.toFixed(2)}%</dd></div>
      <div><dt>Highest</dt><dd>{result.highest}</dd></div>
      <div><dt>Lowest</dt><dd>{result.lowest}</dd></div>
      <div><dt>Grade</dt><dd>{result.grade}</dd></div>
      <div><dt>Remark</dt><dd>{result.performance}</dd></div>
    </dl>
  </section>;
}
