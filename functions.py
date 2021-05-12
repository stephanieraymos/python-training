toUnits = 24
nameOfUnit = "hours"


def daysToUnits(days):
    return f"{days} days are {days * toUnits} {nameOfUnit}"


def validateAndExecute():
    if userInput.isdigit():
        userInputToNum = int(userInput)
        if userInputToNum > 0:
            calculatedValue = daysToUnits(userInputToNum)
            print(calculatedValue)
        elif userInputToNum == 0:
            print("You entered 0, please enter a number greater than 0 to continue with conversion")
    else:
        print("Your input is not a valid number, stop trying to trick the system.")


userInput = input("Enter a number of days and I will convert it to hours! \n")
validateAndExecute()

