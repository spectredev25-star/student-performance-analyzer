import {analyzeStudent,calculateResult} from "../../javascript/src/index";
const student={id:"DEMO",name:"Ada",department:"Computer Engineering",scores:{Mathematics:91,Programming:96,Physics:88}};
console.log(calculateResult(student.scores));
console.log(analyzeStudent(student));
