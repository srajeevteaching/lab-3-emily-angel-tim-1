# Emily Catanzariti, Angel Scott, Tim Hunt
# CS 151, Dr. Rajeev
# 9/30/2021
# Lab 3
# Program Inputs: weight of package and distance to be shipped
# Program Outputs: cost to ship package

# ask user for weight of package

weight = float(input("What is the weight of your package in kg?"))

if weight <= 0 or weight > 20:
    print("Sorry, your package cannot be shipped.")
else:
    if weight > 0 and weight <= 2:
        cost_per_mile = 0.0022
    elif weight > 2 and weight <= 6:
        cost_per_mile = 0.0044
    elif weight > 6 and weight <= 10:
        cost_per_mile = 0.0074
    elif weight > 10 and weight <= 20:
        cost_per_mile = 0.0096

# ask user for distance to be shipped

distance = float(input("How many miles would your package be shipped?"))
if distance < 10 or distance > 3000:
    print("Sorry, your package cannot be shipped.")
else:
    total_cost = distance * cost_per_mile
total_cost = float(total_cost)

# give user output
print("The total cost to ship your package is: $%.2f" % total_cost)
