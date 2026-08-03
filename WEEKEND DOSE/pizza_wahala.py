number_of_guests = int(input("Enter number of guests: "))
pizza_type = input("Enter pizza type: ")

if pizza_type == "Sapa size":
    slices_per_box = 4
    price_per_box = 2500

elif pizza_type == "Small Money":
    slices_per_box = 6
    price_per_box = 2900

elif pizza_type == "Big boys":
    slices_per_box = 8
    price_per_box = 4000

elif pizza_type == "Odogwu":
    slices_per_box = 12
    price_per_box = 5200

else:
    print("Invalid pizza type")
    exit()

number_of_boxes = number_of_guests // slices_per_box

if number_of_guests % slices_per_box != 0:
    number_of_boxes = number_of_boxes + 1

total_slices = number_of_boxes * slices_per_box

leftover_slices = total_slices - number_of_guests

total_price = number_of_boxes * price_per_box

print("Number of boxes to buy =", number_of_boxes)
print("Number of slices left over =", leftover_slices)
print("Total price =", total_price)
