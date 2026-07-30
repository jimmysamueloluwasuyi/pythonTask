def calculate_wage(deliveries):
    if deliveries < 50:
        return deliveries * 160 + 5000
    elif deliveries <= 59:
        return deliveries * 200 + 5000
    elif deliveries <= 69:
        return deliveries * 250 + 5000
    else:
        return deliveries * 500 + 5000


# Tests
print(calculate_wage(25))  
print(calculate_wage(55))  
print(calculate_wage(65)) 
print(calculate_wage(80))  
