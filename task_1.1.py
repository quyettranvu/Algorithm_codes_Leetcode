def reverse_digits(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        reverse_digits(n // 10)

n = int(input("Enter the number: "))
reverse_digits(n)