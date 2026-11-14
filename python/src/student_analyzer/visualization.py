"""Matplotlib charts for student and class performance."""
from pathlib import Path
import matplotlib.pyplot as plt
from .analytics import analyze_class


def create_class_dashboard(students: list[dict], output: str | Path) -> Path:
    report = analyze_class(students)
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    rankings = report["rankings"]
    axes[0].bar([row["name"] for row in rankings], [row["average"] for row in rankings])
    axes[0].set_title("Student averages")
    axes[0].set_ylabel("Average score")
    axes[0].tick_params(axis="x", rotation=35)
    subjects = report["subject_statistics"]
    axes[1].bar(list(subjects), [row["average"] for row in subjects.values()])
    axes[1].set_title("Subject averages")
    axes[1].set_ylabel("Average score")
    axes[1].tick_params(axis="x", rotation=35)
    distribution = report["grade_distribution"]
    axes[2].bar(list(distribution), list(distribution.values()))
    axes[2].set_title("Grade distribution")
    axes[2].set_ylabel("Number of students")
    fig.suptitle(f"Class performance overview (n={report['student_count']})")
    fig.tight_layout()
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return output_path
