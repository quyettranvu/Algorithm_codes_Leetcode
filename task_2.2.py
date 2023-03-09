count = 0
for num in range(100000, 1000000):
    digits = set(str(num))
    if len(digits) == 6:
        count += 1

print("Total number of six-digit numbers with unique digits:", count)