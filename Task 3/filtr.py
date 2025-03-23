from load_logs import load_logs

def filter_logs_by_level(logs: list, level: str) -> list:
        filtr_list = [log for log in logs if logs["level"] == level]
        return filtr_list
