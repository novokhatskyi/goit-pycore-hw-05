from datetime import datetime
import re

def parse_log_line (line: str) -> dict:
    match = re.search (r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ([A-Z]+)(.+)",line)
    date = match.group(1)
    level = match.group(2)
    message = match.group(3)
    datetime.strptime (date,"%Y-%m-%d %H:%M:%S")
    dict_log = {"date": date, "level": level, "message": message}
    return dict_log
    
