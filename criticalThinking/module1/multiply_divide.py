# Part 2: Multiplication and Division of Two Numbers

# have user input first number // num1 
# have user input second number // num2 
num1 = float(input("Enter a number number: "))
num2 = float(input("Enter a second number: "))

# calculate product of num1 and num2 and store as var product_result 
product_result = num1 * num2
print("The product of the two numbers is:", product_result)

# make sure num2 is not zero
# if num2 is zero, display error for division 
# if num2 is not zero, calculate division of num1 and num2 store as var // division_result 
# print results 
if num2 != 0:
    division_result = num1 / num2
    print("The result of dividing the first number by the second is:", division_result)
else:
    print("Error: division by zero is undefined.")
