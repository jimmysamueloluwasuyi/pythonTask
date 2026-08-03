
base_number = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

power_result = 1

for count in range(exponent):
    power_result = power_result * base_number

print("Answer =", power_result)
