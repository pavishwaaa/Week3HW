
# Sum of a Series: Write a program that calculates the
# sum of the first n natural numbers,
# where n is provided by the user.

num = int(input("Enter number: "))
sum = 0
for x in range(1, num+1):
    print("x= ", x)
    sum = x + sum

print("Sum: ", sum)
