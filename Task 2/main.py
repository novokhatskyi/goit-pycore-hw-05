from generator_numbers import generator_numbers
from sum_profit import sum_profit
import pathlib

current_dir = pathlib.Path(__file__).parent
path = current_dir/"Salary statement.txt"
with open (path, "r", encoding="UTF-8") as file:
    text = file.read()
total_income = sum_profit(text, generator_numbers)
print (f"Загальний дохід: {total_income} доларів")
