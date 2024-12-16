# Bookstore Points Calculation

books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine points based on the number of books
if books_purchased == 0:
    points = 0
elif books_purchased >= 1 and books_purchased <= 3:  
    points = 5
elif books_purchased >= 4 and books_purchased <= 5: 
    points = 15
elif books_purchased >= 6 and books_purchased <= 7:  
    points = 30
elif books_purchased >= 8:  
    points = 60
else:
    points = 0  # Default case 

# Display the points
print("You have earned {} points.".format(points))