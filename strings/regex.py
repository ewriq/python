import re

text = "zenci123purna456doner789"

numbers = re.findall(r"\d+", text)

print(numbers)