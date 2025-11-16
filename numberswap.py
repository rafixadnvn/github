value_A = 100
value_B = 200
value_C = 300

print("Before Swap")
print(f"Value A: {value_A}")
print(f"Value B: {value_B}")
print(f"Value C: {value_C}")
print("-" * 25)

value_A, value_B, value_C = value_C, value_A, value_B

print("After Circular Swap")
print(f"Value A: {value_A}")
print(f"Value B: {value_B}")
print(f"Value C: {value_C}")
print("-" * 25)