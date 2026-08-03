
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

for current_number in numbers:
    if current_number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)
