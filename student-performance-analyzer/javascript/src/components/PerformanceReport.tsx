import React from "react";
import type {StudentAnalysis} from "../types/index";
import {StudentTable} from "./StudentTable";
import {PerformanceChart} from "./PerformanceChart";
export function PerformanceReport({students,title="Performance report"}:{students:StudentAnalysis[];title?:string}) {
  const average=students.length?students.reduce((sum,s)=>sum+s.average,0)/students.length:0;
  return <main className="spa-report"><h2>{title}</h2><p>{students.length} students · Class average {average.toFixed(2)}%</p>
    <StudentTable students={students}/>
    <PerformanceChart labels={students.map(s=>s.name)} values={students.map(s=>s.average)}/>
  </main>;
}
