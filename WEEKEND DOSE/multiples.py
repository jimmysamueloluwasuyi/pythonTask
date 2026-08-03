number = int(input("Enter a number: "))

multiple_count = 0

for current_number in range(1, 101):
    if current_number % number == 0:
        multiple_count = multiple_count + 1

print("Number of multiples =", multiple_count)
