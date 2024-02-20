"""You will be designing basic software for a computer inside a police patrol
car. The program keeps track of speeding tickets, and alerts the officer if
an outstanding warrant to arrest the speeder.
"""


def issue_ticket(name, speed):
    global total_fines
    fine = calculate_fine(speed)
    total_fines += fine
    if name in wanted_list:
        print(f"{name.upper()} -- WARRANT TO ARREST")
    else:
        print(f"{name} to be fined ${fine}")
    speeders.append((name, speed))


def calculate_fine(speed):
    if speed < 10:
        return 30
    elif 10 <= speed < 15:
        return 80
    elif 15 <= speed < 20:
        return 120
    elif 20 <= speed < 25:
        return 170
    elif 25 <= speed < 30:
        return 230
    elif 30 <= speed < 35:
        return 300
    elif 35 <= speed < 40:
        return 400
    elif 40 <= speed < 45:
        return 510
    else:
        return 630


def display_summary():
    print(f"Total fines: {len(speeders)}")
    for name, speed in speeders:
        print(f"Name: {name} Amount Over Limit: {speed}")
    print(f"Total amount of fines: ${total_fines}")


# Main Routine
speeders = []
wanted_list = {"James Wilson", "Helga Norman", "Zachary Conroy"}
total_fines = 0
while True:
    print()
    name = input("Enter name of speeder -- to display summary enter 'exit': ")
    if name == "exit":
        print()
        print("#" * 20)
        print("Summary of the day: ")
        break
    speed = int(input("Enter the amount over speed limit - in km/h: "))
    issue_ticket(name, speed)
    print("#" * 20)
display_summary()
