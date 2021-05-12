toUnits = 24
nameOfUnit = "hours"


def daysToUnits(days):
    if days > 0:
        return f"{days} days are {days * toUnits} {nameOfUnit}"
    elif days == 0:
        return "You entered 0, please enter a number greater than 0 to continue with conversion"
    else:
        return "You entered a negative number, please enter a number greater than 0 to continue with conversion."


userInput = input("Enter a number of days and I will convert it to hours! \n")
userInputToNum = int(userInput)
calculatedValue = daysToUnits(userInputToNum)
print(calculatedValue)
