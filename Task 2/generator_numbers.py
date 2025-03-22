import re

def generator_numbers (text:str):
    result = re.findall (r"\d+\.\d+",text)
    for i in result:
        yield float (i)