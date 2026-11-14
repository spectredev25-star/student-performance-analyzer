# Student Performance Analyzer

A modular toolkit for student score validation, individual reports, class analytics, charts, a Python CLI, reusable TypeScript/React components, and PostgreSQL storage.

## Python quick start
```bash
cd python
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
student-analyzer analyze ../shared/fixtures/students.json
pytest
```

## JavaScript quick start
```bash
cd javascript
npm install
npm test
npm run build
```

## CLI commands
```bash
student-analyzer analyze ../shared/fixtures/students.json
student-analyzer student ../shared/fixtures/students.json STU001
student-analyzer chart ../shared/fixtures/students.json --output performance.png
```

Scores are numeric percentages from 0–100. Courses have equal weight. Missing scores are rejected, not treated as zero. Default grading bands are configurable and documented in `docs/grading-system.md`.

PostgreSQL is optional. Apply `database/migrations/001_initial_schema.sql`, then `database/seeds/001_sample_data.sql`. A browser must never connect directly to PostgreSQL; use a trusted server/API.
