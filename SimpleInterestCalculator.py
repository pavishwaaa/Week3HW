# Simple Interest Calculator: Write a program that calculates simple interest
# given the principal amount, rate of interest, and time.Use conditions to ensure
# that none of the  input values are negative

# Write a function to take values from user.
def userInput():
    principleAmount = float(input("Enter principle amount: "))
    interestRate = float(input ("Enter Interest rate: "))
    interestRateTime = float(input("Enter time of the Interest in month: "))
    # return principleAmount, interestRate, interestRateTime  # Returns the values. It would be as tuple.
    return [principleAmount, interestRate, interestRateTime]  # Returns the values. It would be as list.


# Stores the values from user to number depend on the return formate(Either list or tuple.)
numbers = userInput()
print(type(numbers))  # Check the type of numbers. (list or tuple.)

if numbers[0] > 0 and numbers[1] > 0 and numbers[2] > 0:  # Condition to check the numbers are not negative.
    SI = numbers[0] * numbers[1] * numbers[2]  # Count the simple interest
    print("\n Simple interest for amount- ", numbers[0], ""
      "\n for period of- ", numbers[1], " months",
      "\n on rate of ", numbers[2], "%", "= ", SI)
else:
    print("\n ** Values can not be negative! ** ")

