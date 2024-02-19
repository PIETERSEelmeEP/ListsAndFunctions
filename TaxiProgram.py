"""Write a program which keep track of details for a taxi. The program should
start off by asking for the driver’s name. It should then repeatedly ask to
start a new trip. If the user says "yes", ask for the time the trip took in
minutes. It should print out the cost at the end of the trip which is a base
cost of $10 plus $2 extra for each minute the trip took.
"""


def number_checker(question):
    error = "\nPlease enter a name\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


def answer_checker(question):
    error = "\nPlease enter a name\n"
    answer = ""
    while not answer:
        try:
            answer = str(input(question))
            return answer
        except ValueError:
            print(error)


def yes_no_checker(question):
    error = "\nPlease enter a valid answer (Yes or No)"
    answer = ""
    while not answer:
        try:
            answer = str(input(question)).lower()
            if answer == "yes" or answer == "no":
                return answer
            else:
                print(error)
        except ValueError:
            print(error)


def new_trip():
    total_trips = 0
    total_time = 0
    total_income = 0
    while True:
        start_new_trip = answer_checker("Do you want to start a new "
                                        "trip -- Yes or No: ").lower()
        if start_new_trip == "yes":
            FIXED_COST = 10
            time_minutes = number_checker("Enter the duration of the trip -- "
                                          "in minutes: ")
            COST_PER_MINUTE = 2
            final_cost = time_minutes * COST_PER_MINUTE + FIXED_COST
            print(f"This trip cost ${final_cost:.2f}\n")
            total_time += time_minutes
            total_income += final_cost
            total_trips += 1
        if start_new_trip == "no":
            average_time = total_time / total_trips
            average_cost = total_income / total_trips
            print(30 * "--")
            print(f"Driver {driver_name} had {total_trips} trips totalling "
                  f"{total_time} minutes")
            print(f"The average time of all the trips was "
                  f"{average_time} minutes")
            print(f"The total income for the day was ${total_income}")
            print(f"The average cost of all the trips was ${average_cost}")
            return


# Main Routine
driver_name = answer_checker("Enter drivers name: ")
print()
new_trip()
