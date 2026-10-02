import re

text = "zenci123purna456döner789"

numbers = re.findall(r"\d+", text)

print(numbers)