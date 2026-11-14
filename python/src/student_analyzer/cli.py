"""Command-line interface for JSON-based student analysis."""
import argparse
import json
import sys
from pathlib import Path
from .core import analyze_student
from .analytics import analyze_class
from .visualization import create_class_dashboard


def load_students(path: str) -> list[dict]:
    source = Path(path)
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Could not read valid JSON from {source}: {error}") from error
    if isinstance(data, dict) and "students" in data:
        data = data["students"]
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of students or an object with a 'students' list.")
    return data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="student-analyzer", description="Analyze academic performance records.")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("analyze", "chart"):
        command = commands.add_parser(name)
        command.add_argument("file", help="Path to a JSON student dataset.")
        if name == "chart":
            command.add_argument("--output", default="performance-dashboard.png", help="Output image path.")
    student = commands.add_parser("student", help="Analyze one student by ID.")
    student.add_argument("file")
    student.add_argument("student_id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        students = load_students(args.file)
        if args.command == "analyze":
            result = analyze_class(students)
            print(json.dumps(result, indent=2))
        elif args.command == "student":
            match = next((row for row in students if row.get("id") == args.student_id), None)
            if match is None:
                raise ValueError(f"No student found with id {args.student_id!r}.")
            print(json.dumps(analyze_student(match), indent=2))
        else:
            output = create_class_dashboard(students, args.output)
            print(f"Dashboard saved to: {output.resolve()}")
        return 0
    except (ValueError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
