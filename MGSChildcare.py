"""You are to design and write a program that will be used by a child day-care
centre. It will keep track of children throughout the day. There will be many
features in the program, but we will take it a step at a time and build each
one in turn.
"""


def number_checker(question):
    error = "\nYou must enter a valid number between 1 and 5\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def dropOff():
    name = input("Enter the name of the child to drop off: ")
    children.append(name)
    print(f"{name} has been checked in.")


def pickUp():
    name = input("Enter the name of the child to pick up: ")
    if name in children:
        children.remove(name)
        print(f"{name} has been checked out.")
    else:
        print(f"Error: {name} is not checked in.")


def calcCost():
    hours = int(input("Enter the number of hours: "))
    cost_per_child = 12
    total_children = len(children)
    total_cost = total_children * cost_per_child * hours
    print(f"The total charge for {total_children} children for {hours} hours "
          f"is ${total_cost}.")


def printRoll():
    total_children = len(children)
    print("Children currently checked in:")
    for child in children:
        print(child)
    if total_children == 0:
        print("There are no children currently checked in")


# Main Routine
children = []
choice = 0
while choice != 5:
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = number_checker("Enter your choice (number between 1 and 5): ")
    print()

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
