import {describe,it,expect} from "vitest";
import {getGrade} from "../src/core/grading";
describe("grading",()=>{it.each([[80,"A"],[79.99,"B"],[70,"B"],[60,"C"],[50,"D"],[0,"F"]] as const)("grades %s",(score,grade)=>expect(getGrade(score).grade).toBe(grade));});
