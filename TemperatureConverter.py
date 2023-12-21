# Create a program that converts temperatures from
# Fahrenheit to Celsius and vice versa, depending on the user's choice.

tempNum = int(input("Enter Temp to convert in Celc or Fah: "))
tempType = input("Enter type- C or F: ")

if tempType == "C":
    tempCelc = ((tempNum - 32)) *5  / 9
    print("Temp in Celc: ", tempCelc)

else:
    tempFah = (((tempNum)) * 9 / 5 ) + 32
    print("Temp in Fah: ", tempFah)