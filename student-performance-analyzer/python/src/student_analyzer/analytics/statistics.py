from statistics import mean, median, multimode, pstdev, pvariance

def summarize_scores(scores):
    values = list(scores)
    if not values:
        raise ValueError("at least one score is required")
    return {"count": len(values), "mean": mean(values), "median": median(values),
            "mode": multimode(values), "minimum": min(values), "maximum": max(values),
            "population_variance": pvariance(values), "population_std_dev": pstdev(values)}
