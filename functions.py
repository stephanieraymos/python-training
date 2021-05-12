# Variables
toUnits = 24
nameOfUnit = "hours"

# Functions
def daysToUnits(days):
    return f"{days} days are {days * toUnits} {nameOfUnit}"


def validateAndExecute():
    try:
        # Changing string to number
        userInputToNum = int(numberOfDays)
        # Check for correct positive numbers
        if userInputToNum > 0:
            calculatedValue = daysToUnits(userInputToNum)
            print(calculatedValue)
        # Check for 0
        elif userInputToNum == 0:
            print("You entered 0, please enter a number greater than 0 to continue with conversion.")
        # Check for negative numbers
        else:
            print("You entered a negative number, please enter a valid number.")

    except ValueError:
        # Check for other values; string for example
        print("Your input is not a valid number, stop trying to trick the system.")


userInput = ""
# While loop to run program until manually stopped or until "exit" is entered
while userInput != "exit":
    userInput = input("Enter a number of days and I will convert it to hours! \n")
    for numberOfDays in userInput.split(","):
        validateAndExecute()
