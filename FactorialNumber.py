# Program to take user input and find factorial number

# User input
num = int(input("Enter number: "))
factNum = 1 # assigning 1 for multiplication
for x in range(1, num+1):
    # print("x= ", x) -- printing x for visual
    factNum = x * factNum
    # print("Factorial: ", factNum) -- printing factorial num for visual

print("Factorial of number", num," : ", factNum)
