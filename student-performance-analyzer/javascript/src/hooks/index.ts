import {useMemo} from "react";
import type {StudentRecord} from "../types/index";
import {analyzeClass} from "../core/calculations";
export function usePerformanceAnalysis(students:StudentRecord[]) {
  return useMemo(()=>analyzeClass(students),[students]);
}
