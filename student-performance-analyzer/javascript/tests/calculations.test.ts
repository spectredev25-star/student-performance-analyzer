import {describe,it,expect} from "vitest";
import {calculateResult,analyzeClass} from "../src/core/calculations";
describe("calculations",()=>{
 it("calculates totals and average",()=>{const r=calculateResult({Math:80,English:90});expect(r.total).toBe(170);expect(r.average).toBe(85);expect(r.grade).toBe("A");});
 it("accepts zero",()=>expect(calculateResult({Math:0,English:100}).average).toBe(50));
 it("ranks by average",()=>{const r=analyzeClass([{id:"1",name:"Alex",scores:{Math:80}},{id:"2",name:"Sam",scores:{Math:90}}]);expect(r.rankings[0].studentId).toBe("2");});
});
