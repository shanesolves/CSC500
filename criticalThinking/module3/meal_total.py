# Part 1: Calculate the total meal cost
food_charge = float(input("Enter the charge for the food: $"))

# Calculate amounts
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Display results
print("\nFood Charge: ${:.2f}".format(food_charge))
print("Tip (18%): ${:.2f}".format(tip))
print("Sales Tax (7%): ${:.2f}".format(tax))
print("Total Amount: ${:.2f}".format(total))
