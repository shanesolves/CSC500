# Average Rainfall Calculation
total_months = 0
total_rainfall = 0.0

# number of years
years = int(input("Enter the number of years: "))

# Outer loop for each year
for year in range(1, years + 1):
    print("Year", year)
    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input("Enter the rainfall (in inches) for month {}: ".format(month)))
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall
avg_rainfall = total_rainfall / total_months

# results
print("\nTotal months: {}".format(total_months))
print("Total rainfall: {:.2f} inches".format(total_rainfall))
print("Average monthly rainfall: {:.2f} inches".format(avg_rainfall))