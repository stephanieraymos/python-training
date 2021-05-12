toUnits = 24
nameOfUnit = "hours"


def daysToUnits(days):
    if days > 0:
        return f"{days} days are {days * toUnits} {nameOfUnit}"
    elif days == 0:
        return "You entered 0, please enter a number greater than 0 to continue with conversion"


userInput = input("Enter a number of days and I will convert it to hours! \n")

if userInput.isdigit():
    userInputToNum = int(userInput)
    calculatedValue = daysToUnits(userInputToNum)
    print(calculatedValue)
else:
    print("Your input is not a valid number, stop trying to trick the system.")

