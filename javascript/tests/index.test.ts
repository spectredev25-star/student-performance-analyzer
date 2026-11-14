import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { analyzeStudent, analyzeClass, validateStudent } from "../src/index.js";
const fixture = JSON.parse(readFileSync(resolve(process.cwd(),"../shared/fixtures/calculation-cases.json"),"utf8"));
describe("shared calculation contract",()=>{
  it("matches every shared individual result",()=>{
    for (const item of fixture.student_cases) expect(analyzeStudent(item.input)).toEqual(item.expected);
  });
  it("matches the shared class report",()=>{
    expect(analyzeClass(fixture.class_case.input)).toEqual(fixture.class_case.expected);
  });
  it("rejects invalid scores",()=>{
    for (const score of [-1,101,"90",null]) {
      expect(()=>validateStudent({id:"X",name:"Test",scores:{Math:score}})).toThrow();
    }
  });
  it("rejects empty score sets and duplicate IDs",()=>{
    expect(()=>validateStudent({id:"X",name:"Test",scores:{}})).toThrow();
    expect(()=>analyzeClass([{id:"X",name:"A",scores:{Math:70}},{id:"X",name:"B",scores:{Math:80}}])).toThrow(/Duplicate/);
  });
});
