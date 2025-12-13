import random

numbers = []

for _ in range(10):
    num = random.randint(1, 100)   # you can change the range if you want
    numbers.append(num)

print("Generated numbers:", numbers)
