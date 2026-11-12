#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""

for i in range (1000):
    if (i + 1) % 5 == 0:
        print(i + 1, end = ",")