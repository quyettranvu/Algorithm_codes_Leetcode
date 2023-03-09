def digit_difference(n):
    digits = [int(d) for d in str(n)]
    return max(digits) - min(digits)

# example usage
n = int(input("Enter the number: "))
diff = digit_difference(n)
print("The difference between the largest and smallest digit of", n, "is", diff)
