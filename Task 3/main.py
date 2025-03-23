from parse_log import parse_log_line
from load_logs import load_logs
from filtr import filter_logs_by_level
from display import display_log_counts
from count import count_logs_by_level
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print ("Помилка: потрібно передати шлях до директорії.")
    sys.exit(1)
directory_path = sys.argv[1]
print(f"Отриманий шлях: {directory_path}")
file_path = Path(sys.argv[1])

if not file_path.exists():
    print("Помилка: файл не існує!")
    sys.exit(1)

if not file_path.is_file():
    print("Помилка: шлях не веде до файлу!")
    sys.exit(1)