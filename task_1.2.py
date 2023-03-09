def print_digits(n):
    if n < 10:
        print(n)
    else:
        print_digits(n // 10)
        print(n % 10)

# example usage
n = int(input("Enter the number: "))
print_digits(n)