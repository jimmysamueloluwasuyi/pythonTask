sum_of_numbers = 0

for count in range(1, 11):
    number = float(input("Enter number " + str(count) + ": "))
    sum_of_numbers = sum_of_numbers + number

average = sum_of_numbers / 10

print("Average =", average)
