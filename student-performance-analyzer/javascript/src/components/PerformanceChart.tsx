import React from "react";
export function PerformanceChart({labels,values,title="Student performance"}:{labels:string[];values:number[];title?:string}) {
  if (labels.length!==values.length) throw new Error("labels and values must have equal lengths");
  return <section className="spa-chart" aria-label={title}><h3>{title}</h3>
    {!labels.length?<p>No chart data.</p>:<div className="spa-chart-bars">{labels.map((label,i)=>{
      const width=Math.max(0,Math.min(100,values[i]));
      return <div className="spa-chart-row" key={`${label}-${i}`}><span>{label}</span>
        <div className="spa-chart-track"><div className="spa-chart-fill" style={{width:`${width}%`}}/></div>
        <strong>{values[i].toFixed(1)}%</strong></div>;
    })}</div>}</section>;
}
