import pathlib
from parse_log import parse_log_line
def load_logs(file_path: str) -> list:
    current_dir = pathlib.Path(__file__).parent
    file_path = current_dir/"log.txt"
    with open (file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        logs = []
        for line in lines:
            logs.append(parse_log_line(line))
    return logs
