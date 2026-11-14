# Contributing

Keep core calculations pure and independent of databases, terminal I/O, and UI. Keep Python and TypeScript behavior aligned. Add tests and update docs for behavior changes.

Setup: install Python with `python -m pip install -e ".[dev]"` from `python/`; install JS with `npm install` from `javascript/`.

Checks: `pytest` in `python/`; `npm test && npm run build` in `javascript/`.
