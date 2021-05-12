toUnits = 24
nameOfUnit = "hours"


def daysToUnits(days):
    return f"{days} days are {days * toUnits} {nameOfUnit}"


userInput = input("Enter a number of days and I will convert it to hours! \n")
userInputToNum = int(userInput)
calculatedValue = daysToUnits(userInputToNum)
print(calculatedValue)