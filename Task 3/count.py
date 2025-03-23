def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1
    return counts