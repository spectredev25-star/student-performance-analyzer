from pathlib import Path
from ..analytics.class_analysis import analyze_class

def create_average_chart(students, output="performance.png"):
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise RuntimeError("Install optional dependencies: pip install -e '.[dev]'") from exc
    report = analyze_class(students)
    names = [row["name"] for row in report["rankings"]]
    averages = [row["average"] for row in report["rankings"]]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(names, averages)
    ax.set(title="Student Average Scores", xlabel="Student", ylabel="Average (%)", ylim=(0, 100))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    destination = Path(output)
    fig.savefig(destination, dpi=160)
    plt.close(fig)
    return destination
