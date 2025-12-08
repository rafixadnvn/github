

def mirrored_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

def main():
    print("=== Mirrored Right-Angled Triangle ===")
    rows = int(input("Enter number of rows: "))
    mirrored_triangle(rows)

if __name__ == "__main__":
    main()
