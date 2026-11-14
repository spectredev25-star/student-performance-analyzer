# Student Performance Analyzer

**An extensible, multi-platform toolkit for analyzing student academic performance.**

Student Performance Analyzer is an open-source software project designed to help developers, educators, and academic institutions calculate, understand, visualize, and manage student performance data.

The project combines Python, TypeScript/JavaScript, React, and PostgreSQL to provide a modular solution for individual student analysis and class-wide academic insights.

Rather than being limited to calculating totals and averages, the goal is to build a reusable analytical system that can grow into a foundation for academic dashboards, student management systems, educational platforms, and other data-driven applications.

---

## Project Vision

Academic performance data contains more information than examination scores alone.

With the right tools, raw scores can become meaningful insights that help answer questions such as:

- How is an individual student performing?
- Which subjects are a student's strongest and weakest?
- What is the overall performance of a class?
- Which students are performing exceptionally well?
- How are grades distributed across a group?
- Which subjects have the highest or lowest class averages?
- Are there noticeable performance patterns across students?

Student Performance Analyzer aims to make these analyses accessible through a reusable, developer-friendly toolkit.

## Key Features

### 1. Individual Student Analysis

Analyze a student's academic records and calculate:

- Total scores
- Average score
- Highest and lowest scores
- Overall grade
- Performance classification
- Individual subject grades and remarks

### 2. Class Performance Analysis

Analyze multiple student records to generate:

- Overall class average
- Highest and lowest student averages
- Student rankings
- Grade distribution
- Subject-level statistics
- Comparative performance reports

### 3. Statistical Analysis

The analytics module supports:

- Mean
- Median
- Mode
- Population variance
- Population standard deviation
- Minimum and maximum scores

### 4. Data Visualization

The Python visualization module uses Matplotlib to generate graphical representations of student performance.

The JavaScript component library also provides reusable visual elements for integrating performance data into React applications.

### 5. Multiple Data Sources

The project supports:

- JSON data input
- CSV data input
- PostgreSQL database integration

This allows student records to be loaded from files or retrieved from a relational database.

### 6. Configurable Grading System

The grading engine uses configurable grade boundaries rather than permanently fixing grading assumptions inside calculation functions.

The default grading scale is:

| Score Range | Grade | Remark |
| --- | --- | --- |
| 80–100 | A | Excellent |
| 70–79.99 | B | Very Good |
| 60–69.99 | C | Good |
| 50–59.99 | D | Pass |
| 0–49.99 | F | Needs Improvement |

These are default project settings and can be adjusted to suit different academic grading policies.

---

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Core calculations, analytics, CLI and visualization |
| TypeScript | Typed, reusable calculation engine |
| JavaScript | Application integration |
| React | Reusable user interface components |
| PostgreSQL | Relational data storage |
| Matplotlib | Data visualization |
| Pytest | Python testing |
| Vitest | JavaScript testing |
| Git & GitHub | Version control and collaboration |

---

## Project Architecture

The project follows a modular architecture that separates calculations, analytics, data storage, and presentation.

```text
student-performance-analyzer/
│
├── docs/                 # Project documentation
│
├── shared/               # Shared schemas and test fixtures
│
├── examples/             # Usage examples
│
├── python/               # Python analytical engine
│   ├── src/
│   │   └── student_analyzer/
│   │       ├── core/          # Calculations and validation
│   │       ├── analytics/     # Individual and class analysis
│   │       ├── visualization/ # Charts and graphs
│   │       ├── inputs/        # JSON and CSV readers
│   │       ├── database/      # Database integration
│   │       └── cli/           # Terminal interface
│   └── tests/
│
├── javascript/            # TypeScript and React library
│   ├── src/
│   │   ├── core/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── types/
│   └── tests/
│
├── database/              # PostgreSQL resources
│   ├── migrations/
│   ├── seeds/
│   └── queries/
│
└── .github/               # GitHub workflows and templates
```

### Architectural Principle

The calculation engine is independent of the user interface and database.

This means developers can use the analytical functions without needing to install the entire application or depend on a particular presentation framework.

The Python and TypeScript implementations also aim to follow the same data contracts and calculation rules.

---

## Getting Started

### Requirements

- Python 3.10 or newer
- Node.js 20 or newer
- Git
- PostgreSQL (optional, for database integration)

### Clone the repository

```bash
git clone https://github.com/spectredev25-star/student-performance-analyzer.git

cd student-performance-analyzer
```

### Set up Python

```bash
cd python

py -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\\Scripts\\Activate.ps1
```

Install the package and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the tests:

```bash
pytest
```

### Set up JavaScript

Open another terminal:

```bash
cd javascript

npm install
```

Run tests:

```bash
npm test
```

Build the TypeScript project:

```bash
npm run build
```

---

## Using the Python CLI

After installing the Python package, you can analyze the included sample dataset.

From the project root:

```bash
student-analyzer analyze shared/fixtures/students.json
```

Analyze an individual student:

```bash
student-analyzer student shared/fixtures/students.json STU001
```

Generate a performance chart:

```bash
student-analyzer chart shared/fixtures/students.json --output performance.png
```

---

## Data Structure

A student record follows this general structure:

```json
{
  "id": "STU001",
  "name": "Alex",
  "department": "Computer Engineering",
  "scores": {
    "Mathematics": 78,
    "Programming": 85,
    "Physics": 90,
    "Databases": 67,
    "English": 88
  }
}
```

Each student has a unique identifier, personal academic information, and a collection of course scores.

### Data Validation Rules

- Scores must be numeric.
- Scores must fall between 0 and 100.
- A student must have at least one course score.
- Missing scores are rejected rather than silently treated as zero.
- Duplicate student identifiers are not allowed.

---

## Reusability

One of the main goals of this project is to make its analytical functionality reusable.

Developers should be able to integrate the project into:

- Student management systems
- School administration platforms
- Educational dashboards
- Academic reporting applications
- Learning management systems
- Data analysis projects

The React components are designed to be independently reusable, while the Python engine can be integrated into other Python applications.

---

## Testing

Testing is an important part of the project's development.

The repository includes:

- Python unit tests using Pytest.
- TypeScript unit tests using Vitest.
- Shared calculation fixtures for consistent expected results.
- GitHub Actions workflow for automated testing.

Run Python tests from the `python/` directory:

```bash
pytest
```

Run JavaScript tests from the `javascript/` directory:

```bash
npm test
```

---

## Project Roadmap

The project is intended to grow incrementally.

- Establish project architecture.
- Implement initial Python calculation engine.
- Implement validation and grading.
- Implement individual and class analysis.
- Add JSON and CSV readers.
- Add initial Python visualization.
- Establish TypeScript calculation engine.
- Create initial reusable React components.
- Create PostgreSQL schema and sample data.
- Expand visualization and statistical reporting.
- Add more configurable grading policies.
- Expand database integration and data management.
- Improve reusable component customization.
- Add comprehensive documentation and integration examples.
- Prepare stable Python and JavaScript package releases.

---

## Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Add or update tests.
5. Submit a pull request with a clear explanation.

Please read CONTRIBUTING.md before submitting changes.

---

## License

This project is distributed under the MIT License. See LICENSE for details.

---

## Project Philosophy

Student Performance Analyzer is built around three principles:

**Modularity:** Every major part of the system should have a clear responsibility and be reusable.

**Consistency:** The Python and TypeScript implementations should follow shared contracts and produce equivalent analytical results.

**Extensibility:** The architecture should make it possible to introduce new analytical features, integrations, and interfaces without rebuilding the entire system.

---

**Built to turn academic scores into meaningful data and reusable software.**
