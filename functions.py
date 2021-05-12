toUnits = 24
nameOfUnit = "hours"


def daysToUnits(days):
    conditionalCheck = days > 0
    print(type(conditionalCheck))
    if days > 0:
        return f"{days} days are {days * toUnits} {nameOfUnit}"
    else:
        return "You entered a negative number, please enter a number greater than 0 to continue with conversion."


userInput = input("Enter a number of days and I will convert it to hours! \n")
userInputToNum = int(userInput)
calculatedValue = daysToUnits(userInputToNum)
print(calculatedValue)
