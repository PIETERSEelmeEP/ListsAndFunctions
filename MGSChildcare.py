"""You are to design and write a program that will be used by a child day-care
centre. It will keep track of children throughout the day. There will be many
features in the program, but we will take it a step at a time and build each
one in turn.
"""


def number_checker(question):
    error = "\nYou must enter a valid number\n"
    number = ""
    while not :
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)

    while not 1 <= choice <= 5:
        print("Choice can only be between 1 and 5")
        choice = number_checker("Enter your choice (number between 1 and 5): ")

def dropOff():
    print()


def pickUp():
    print()


def calcCost():
    print()


def printRoll():
    print()


choice = 0
while choice != 5:
    print("-------------------------------------------------------------------"
          "----")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-------------------------------------------------------------------"
          "----")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = number_checker("Enter your choice (number between 1 and 5): ")
    print()

    length = number_checker("Enter the length of required concrete - in "
                            "centimeters: ")
    width = number_checker("Enter the width of required concrete - in "
                           "centimeters: ")

    if choice == 1:
        dropOff()
    elif choice == 2:
        pickUp()
    elif choice == 3:
        calcCost()
    elif choice == 4:
        printRoll()
    else:
        print("Goodbye")
