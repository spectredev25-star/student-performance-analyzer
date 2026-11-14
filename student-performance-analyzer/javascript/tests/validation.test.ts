import {describe,it,expect} from "vitest";
import {validateStudent,validateStudents} from "../src/core/validation";
describe("validation",()=>{
 it("accepts valid data",()=>expect(validateStudent({id:"S1",name:"Alex",scores:{Math:80}}).id).toBe("S1"));
 it("rejects score over 100",()=>expect(()=>validateStudent({id:"S1",name:"Alex",scores:{Math:101}})).toThrow());
 it("rejects duplicate IDs",()=>{const s={id:"S1",name:"Alex",scores:{Math:80}};expect(()=>validateStudents([s,s])).toThrow();});
});
