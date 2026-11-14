# Student Performance Analyzer

**A reusable toolkit for turning academic scores into meaningful analysis.**

Student Performance Analyzer provides matching Python and TypeScript calculation engines, a Python command-line interface, class-level statistics, and performance charts. Both engines follow shared JSON fixtures so their results can be checked against the same expected outputs.

## Stage 1 capabilities

- Validate student records, score ranges, required fields, and unique IDs.
- Calculate totals, averages, highest/lowest subjects, subject grades, and overall remarks.
- Configure grading boundaries through the Python and TypeScript APIs.
- Analyze a class: rankings, grade distribution, class average, and subject-level mean, median, range, and population standard deviation.
- Generate a three-panel Matplotlib dashboard for student averages, subject averages, and grade distribution.
- Run matching Python and TypeScript tests against `shared/fixtures/calculation-cases.json`.

Default grading policy (customizable): A 80–100, B 70–79.99, C 60–69.99, D 50–59.99, F 0–49.99.

## Repository layout

```text
student-performance-analyzer/
├── python/
│   ├── pyproject.toml
│   ├── src/student_analyzer/
│   │   ├── core.py
│   │   ├── analytics.py
│   │   ├── visualization.py
│   │   └── cli.py
│   └── tests/
├── javascript/
│   ├── package.json
│   ├── tsconfig.json
│   ├── src/index.ts
│   └── tests/index.test.ts
├── shared/fixtures/calculation-cases.json
└── .github/workflows/tests.yml
```

## Data contract

A student record has a unique string ID, a name, an optional department, and at least one subject score. Scores must be finite numbers from 0 to 100 inclusive. Missing scores are not silently converted to zero.

```json
{
  "id": "STU001",
  "name": "Ada",
  "department": "Computer Engineering",
  "scores": {
    "Mathematics": 78,
    "Programming": 85,
    "Physics": 90
  }
}
```

The dataset is a JSON array of student records. The CLI also accepts an object containing a `students` array.

## Python setup

Python 3.10+ is required. From the repository root:

```powershell
cd python
py -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install -e ".[dev]"
pytest
```

### CLI commands

Run these from the `python/` directory after installation. Dataset paths below are relative to the repository root, so use `../shared/fixtures/calculation-cases.json` from this directory.

```bash
# Class report (JSON)
student-analyzer analyze ../shared/fixtures/calculation-cases.json

# One student's report
student-analyzer student ../shared/fixtures/calculation-cases.json STU001

# Save a class dashboard graph
student-analyzer chart ../shared/fixtures/calculation-cases.json --output ../performance-dashboard.png
```

You can also run the CLI without installing its command entry point:

```bash
python -m student_analyzer.cli analyze ../shared/fixtures/calculation-cases.json
```

The chart contains student averages, subject averages, and grade distribution. Matplotlib saves it to the path supplied with `--output`.

### Python API

```python
from student_analyzer import analyze_student, analyze_class

individual = analyze_student(student_record)
class_report = analyze_class(student_records)
```

## TypeScript setup

Node.js 20+ is recommended. From the repository root:

```bash
cd javascript
npm install
npm test
npm run build
```

### TypeScript API

```ts
import { analyzeStudent, analyzeClass } from "./src/index.js";

const individual = analyzeStudent(studentRecord);
const report = analyzeClass(studentRecords);
```

Both APIs accept an optional grading scale. A scale is an array of objects with `min`, `grade`, and `remark` properties. The highest matching minimum boundary is applied.

## Cross-language validation

The shared fixture file contains the input records and exact expected outputs. Python's pytest suite and TypeScript's Vitest suite both read that same file. This is the contract that keeps the two implementations aligned as features are added.

GitHub Actions runs both test suites and the TypeScript build on pushes and pull requests.

## What the class report includes

- Overall class average (the mean of individual student averages).
- Ranked students, sorted by average descending and then ID for deterministic ties.
- Grade distribution.
- Per-subject count, average, median, minimum, maximum, and population standard deviation.
- Individual student reports embedded in the class report.

A student who does not have a score for a particular subject is excluded from that subject's statistics; their missing score is never treated as zero.

## Next: relational database layer

The next stage will introduce a normalized PostgreSQL schema for students, departments, subjects, academic sessions, assessments, and scores. The database will store source records; Python and TypeScript will remain responsible for reusable calculations and presentation.

## Project principles

**Modularity:** calculations, analytics, visualization, CLI, and persistence have separate responsibilities.

**Consistency:** Python and TypeScript use the same input contract and shared expected results.

**Extensibility:** future dashboards, APIs, and database adapters can build on the engines without coupling the core calculations to a UI or database.

## License

MIT. See [LICENSE](LICENSE) when the license file is added.
