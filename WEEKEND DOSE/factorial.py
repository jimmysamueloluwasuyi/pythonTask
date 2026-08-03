
number = int(input("Enter a number: "))

factorial = 1

for current_number in range(1, number + 1):
    factorial = factorial * current_number

print("Factorial =", factorial)
