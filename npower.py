print("Power Calculator")

base = float(input("Enter a number: "))
count = int(input("How many powers do you want to calculate? "))

for i in range(1, count + 1):
    result = base ** i
    print(base, "raised to", i, "is", result)
