# Prime Number Checker: Develop a program that asks the user
# for a number and then tells them whether the number is prime or not.

num = int(input("Enter number to check if it is prime: "))

if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        print("num/2 + 1 =", i)
        if (num % i) == 0:
            print("num % i= ", num % i)
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("not a prime number")
