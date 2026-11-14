import argparse
import sys
from .commands import run_analyze, run_student, run_chart

def main():
    parser = argparse.ArgumentParser(description="Analyze student assessment results")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("analyze"); p.add_argument("file")
    p = sub.add_parser("student"); p.add_argument("file"); p.add_argument("student_id")
    p = sub.add_parser("chart"); p.add_argument("file"); p.add_argument("--output", default="performance.png")
    args = parser.parse_args()
    try:
        if args.command == "analyze": run_analyze(args.file)
        elif args.command == "student": run_student(args.file, args.student_id)
        else: run_chart(args.file, args.output)
    except (ValueError, OSError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
