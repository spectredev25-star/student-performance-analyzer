# Architecture

JSON/CSV/PostgreSQL adapters feed validated records into a pure calculation core. Analytics compose core functions. CLI, charts, and React components present results.

`core/` has no I/O. `analytics/` contains individual/class analysis. `inputs/` parses files. `database/` is an optional server-side adapter. `visualization/` creates charts. The browser package must never connect directly to PostgreSQL.
