# Emily Catanzariti, Angel Scott, Tim Hunt
# CS 151, Dr. Rajeev
# 9/30/2021
# Lab 3
# Program Inputs: weight of package and distance to be shipped
# Program Outputs: cost to ship package

# state purpose of program
print("This program will tell you the cost to ship your package over a certain amount of miles.")

# ask user for weight of package and distance

weight = float(input("What is the weight of your package in kg?"))
distance = float(input("How many miles would your package be shipped?"))
if (weight > 0 and weight <= 20) and (distance >= 10 and distance <= 3000):
    if weight > 0 and weight <= 2:
        cost_per_mile = 0.0022
    elif weight > 2 and weight <= 6:
        cost_per_mile = 0.0044
    elif weight > 6 and weight <= 10:
        cost_per_mile = 0.0074
    elif weight > 10 and weight <= 20:
        cost_per_mile = 0.0096
    total_cost = cost_per_mile * distance
    print("The total cost to ship your package is: $%.2f" % total_cost)
else:
    print("Sorry, your package cannot be shipped.")



print("Thank you for using the program! :)")
