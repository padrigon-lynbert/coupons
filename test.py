import os
from Percentage.main import Percentage

# test = Percentage.value_of_percentage(10,120)
# os.system('cls')
# print(f"Test: {test}\n\nTest--pass", end=""); input("")

data = ["1", "2", "3", "1", "b", "10", "c"]

# print(isinstance(1, int))
for i in data:
    if i.isdigit(): print("pass")
    else: print("fail")