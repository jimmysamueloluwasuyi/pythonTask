
number = int(input("Enter a positive integer: "))

step_count = 0

while number != 1:

    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

    step_count = step_count + 1

print("Number of steps =", step_count)
