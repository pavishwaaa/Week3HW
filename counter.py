
# Create a program that asks the user for a number and
#     then prints a countdown from that number to 1.
num = int(input("Enter number: "))
for x in reversed(range(1, num+1)):
   print(x)
